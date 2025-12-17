import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
from stl import mesh
from tqdm import tqdm
from collections import deque, defaultdict
import math

# --- Configuration ---
CSV_FILE_PATH = r'J:\My Drive\1 SMDMP Civil-HM ICB-02 2078-79\3 Construction Supervision\Headworks\Left Bank Slope Protection Work\LBS Drawings\point-cloud.csv'
STL_OUTPUT_PATH = r'C:\Users\Ripple\Downloads\surface_mesh_advanced.stl'

# --- Algorithm Parameters (Tuning is Crucial) ---

# BIG_CUTOFF_DISTANCE: Defines the maximum search radius for neighbors when
# building the mesh. This is the most important parameter. It should be slightly
# larger than the typical spacing between points in your densest areas.
BIG_CUTOFF_DISTANCE = 5.0

# MIN_ANGLE_THRESHOLD (degrees): A critical quality control parameter. Any potential
# triangle with an interior angle smaller than this will be rejected.
# Helps prevent "skinny" or "badly conditioned" triangles.
# Good values are typically between 15 and 30 degrees.
MIN_ANGLE_THRESHOLD = 20.0

# --- Helper Functions ---

def calculate_triangle_angles(p1, p2, p3):
    """Calculates the 3 interior angles of a triangle in degrees."""
    # Vectors representing the sides
    v12 = p2 - p1
    v13 = p3 - p1
    v23 = p3 - p2
    
    # Magnitudes (lengths) of the sides
    d12 = np.linalg.norm(v12)
    d13 = np.linalg.norm(v13)
    d23 = np.linalg.norm(v23)
    
    if d12 == 0 or d13 == 0 or d23 == 0:
        return [0, 0, 0] # Degenerate triangle

    # Angle at p1
    angle1 = math.degrees(math.acos(np.dot(v12, v13) / (d12 * d13)))
    # Angle at p2
    angle2 = math.degrees(math.acos(np.dot(-v12, v23) / (d12 * d23)))
    # Angle at p3
    angle3 = 180.0 - angle1 - angle2
    
    return [angle1, angle2, angle3]

def read_penzd_points(filepath):
    """Reads a PENZD CSV file and returns a NumPy array of 3D points."""
    try:
        df = pd.read_csv(
            filepath,
            header=None,
            names=['P', 'N', 'E', 'Z', 'D']
        )
        points_3d = df[['E', 'N', 'Z']].to_numpy()
        print(f"Successfully read {len(points_3d)} points from '{filepath}'.")
        return points_3d
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None

def _triangle_area(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    return 0.5 * np.linalg.norm(np.cross(v1, v2))


def create_surface_mesh_advanced(points, big_cutoff, min_angle_deg):
    """
    Greedy triangulation: prioritize short links and small triangle areas.

    - Build all edges within big_cutoff and sort ascending by length.
    - For each edge, choose the smallest-area triangle that:
      - uses only short links (≤ big_cutoff)
      - keeps each edge manifold (≤ 2 faces per edge)
      - does not span interior chords (only allow if edge is on boundary or introduces new node)
      - optionally respects a minimum-angle threshold to avoid skinny triangles
    - Never duplicates triangles; favors many small triangles over larger overlapping ones.
    """
    if points is None or len(points) < 3:
        return np.array([])

    n = len(points)
    print(f"\nStarting Greedy Mesh Creation for {n} points...")

    # 1) Neighbor search
    print("1. Building KD-Tree for spatial queries...")
    kdtree = cKDTree(points)
    neighbors_list = kdtree.query_ball_point(points, r=big_cutoff)

    # Build candidate edges with distances and adjacency sets
    adjacency_sets = [set() for _ in range(n)]
    edges = []  # (dist, i, j)
    edge_exists = set()  # canonical pairs

    print(f"2. Gathering and sorting edges (r < {big_cutoff})...")
    for i in tqdm(range(n), desc="   Scanning Neighbors"):
        for j in neighbors_list[i]:
            if i < j:
                d = float(np.linalg.norm(points[i] - points[j]))
                edges.append((d, i, j))
                adjacency_sets[i].add(j)
                adjacency_sets[j].add(i)
                edge_exists.add((i, j))

    if not edges:
        print("No edges within cutoff; cannot form mesh.")
        return np.array([])

    edges.sort(key=lambda t: t[0])
    print(f"   - {len(edges)} edges queued.")

    # 2) Mesh state
    faces_set = set()                  # sorted triples
    edge_face_count = defaultdict(int) # edge -> incident faces
    boundary_edges = set()             # edges with exactly 1 face
    nodes_in_mesh = set()              # nodes that appear in at least one face

    def ek(a, b):
        return (a, b) if a < b else (b, a)

    def can_use_edge(a, b):
        return ek(a, b) in edge_exists

    def is_boundary_edge(a, b):
        return edge_face_count[ek(a, b)] == 1

    def add_face(i, j, k):
        f = tuple(sorted((i, j, k)))
        if f in faces_set:
            return False
        e1, e2, e3 = ek(i, j), ek(j, k), ek(k, i)
        # manifold check
        if edge_face_count[e1] >= 2 or edge_face_count[e2] >= 2 or edge_face_count[e3] >= 2:
            return False
        # angle quality (avoid extremely skinny triangles)
        if min_angle_deg is not None and min_angle_deg > 0:
            a1, a2, a3 = calculate_triangle_angles(points[i], points[j], points[k])
            if min(a1, a2, a3) < min_angle_deg:
                return False
        # apply
        faces_set.add(f)
        for e in (e1, e2, e3):
            edge_face_count[e] += 1
            if edge_face_count[e] == 1:
                boundary_edges.add(e)
            elif edge_face_count[e] == 2 and e in boundary_edges:
                boundary_edges.remove(e)
        nodes_in_mesh.update((i, j, k))
        return True

    # 3) Greedy growth with iterative passes until saturation
    print("3. Growing mesh by smallest links and smallest area (iterative passes)...")
    AREA_EPS = 1e-10
    added_any = True
    pass_num = 0
    while added_any:
        added_any = False
        pass_num += 1
        for dist, i, j in tqdm(edges, total=len(edges), desc=f"   Pass {pass_num}"):
            e = ek(i, j)
            # Respect manifold: do not exceed 2 faces per edge
            if edge_face_count[e] >= 2:
                continue

            # Candidates are common neighbors; ensure other two edges exist and are short
            common = adjacency_sets[i].intersection(adjacency_sets[j])
            if not common:
                continue

            best_k = None
            best_area = None
            for k in common:
                if k == i or k == j:
                    continue
                if not (can_use_edge(j, k) and can_use_edge(k, i)):
                    continue
                e2, e3 = ek(j, k), ek(k, i)
                if edge_face_count[e2] >= 2 or edge_face_count[e3] >= 2:
                    continue

                area = _triangle_area(points[i], points[j], points[k])
                if area <= AREA_EPS:
                    continue

                # Optional: avoid extremely skinny triangles
                if min_angle_deg is not None and min_angle_deg > 0:
                    a1, a2, a3 = calculate_triangle_angles(points[i], points[j], points[k])
                    if min(a1, a2, a3) < min_angle_deg:
                        continue

                if best_area is None or area < best_area:
                    best_area = area
                    best_k = k

            if best_k is not None:
                if add_face(i, j, best_k):
                    added_any = True

    print(f"   - Built {len(faces_set)} triangles after {pass_num} pass(es).")
    return np.array(list(faces_set), dtype=int)

def save_to_stl(points, faces, output_path):
    """Saves the mesh (points and faces) to an STL file."""
    if faces.shape[0] == 0:
        print("Warning: No faces were created. Cannot save an empty STL file.")
        return

    print(f"\nSaving mesh to '{output_path}'...")
    surface_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            surface_mesh.vectors[i][j] = points[f[j], :]
            
    try:
        surface_mesh.save(output_path)
        print("Successfully saved STL file.")
    except Exception as e:
        print(f"An error occurred while saving the STL file: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    points_3d = read_penzd_points(CSV_FILE_PATH)

    if points_3d is not None:
        faces_3d = create_surface_mesh_advanced(
            points=points_3d,
            big_cutoff=BIG_CUTOFF_DISTANCE,
            min_angle_deg=MIN_ANGLE_THRESHOLD
        )
        
        save_to_stl(
            points=points_3d,
            faces=faces_3d,
            output_path=STL_OUTPUT_PATH
        )