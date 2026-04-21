from __future__ import annotations

import csv
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import pythoncom
import win32com.client

from myAutoCAD import myAutoCAD


CENTERLINE_LAYER = "0_CenterLines"
BANKLINE_LAYER = "0_BankLines"
XDATA_APP_NAME = "RIVER"
SAMPLING_INTERVAL_M = 1.0
ARC_TESSELLATION_MAX_SEGMENT_M = 0.25
ARC_TESSELLATION_MAX_ANGLE_RAD = math.radians(5.0)
BANK_SEARCH_CUTOFF_M = 8.0
OUTPUT_FOLDER_NAME = "rasgeom_output"
EPSILON = 1e-9

Point2D = Tuple[float, float]


@dataclass
class PolylineData:
    handle: str
    layer: str
    vertices: List[Point2D]
    river_name: str = ""


@dataclass
class SamplePoint:
    sn: int
    chainage: float
    point: Point2D
    tangent: Point2D


@dataclass
class SectionCrossing:
    polyline: PolylineData
    offset: float
    tangent: Point2D


@dataclass
class SectionAnalysis:
    section_type: str
    width_tangent: Point2D
    bank_search_cutoff: float


def distance(p1: Point2D, p2: Point2D) -> float:
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def subtract(p1: Point2D, p2: Point2D) -> Point2D:
    return (p1[0] - p2[0], p1[1] - p2[1])


def add(p1: Point2D, p2: Point2D) -> Point2D:
    return (p1[0] + p2[0], p1[1] + p2[1])


def scale(vector: Point2D, factor: float) -> Point2D:
    return (vector[0] * factor, vector[1] * factor)


def dot(p1: Point2D, p2: Point2D) -> float:
    return p1[0] * p2[0] + p1[1] * p2[1]


def cross(p1: Point2D, p2: Point2D) -> float:
    return p1[0] * p2[1] - p1[1] * p2[0]


def normalize(vector: Point2D) -> Point2D:
    length = math.hypot(vector[0], vector[1])
    if length <= EPSILON:
        return (0.0, 0.0)
    return (vector[0] / length, vector[1] / length)


def perpendicular_unit(tangent: Point2D) -> Point2D:
    return normalize((-tangent[1], tangent[0]))


def append_distinct(points: List[Point2D], point: Point2D) -> None:
    if not points or distance(points[-1], point) > 1e-7:
        points.append(point)


def tessellate_bulge_segment(
    start: Point2D,
    end: Point2D,
    bulge: float,
    max_segment_length: float = ARC_TESSELLATION_MAX_SEGMENT_M,
) -> List[Point2D]:
    if abs(bulge) <= EPSILON:
        return [start, end]

    chord_length = distance(start, end)
    if chord_length <= EPSILON:
        return [start, end]

    sweep_angle = 4.0 * math.atan(bulge)
    sin_half_angle = math.sin(sweep_angle / 2.0)
    tan_half_angle = math.tan(sweep_angle / 2.0)
    if abs(sin_half_angle) <= EPSILON or abs(tan_half_angle) <= EPSILON:
        return [start, end]

    radius = chord_length / (2.0 * abs(sin_half_angle))
    midpoint = ((start[0] + end[0]) / 2.0, (start[1] + end[1]) / 2.0)
    chord_unit = normalize(subtract(end, start))
    left_normal = (-chord_unit[1], chord_unit[0])
    center_offset = chord_length / (2.0 * tan_half_angle)
    center = add(midpoint, scale(left_normal, center_offset))
    start_angle = math.atan2(start[1] - center[1], start[0] - center[0])
    arc_length = abs(radius * sweep_angle)
    safe_max_length = max(max_segment_length, EPSILON)
    segment_count = max(
        1,
        math.ceil(arc_length / safe_max_length),
        math.ceil(abs(sweep_angle) / ARC_TESSELLATION_MAX_ANGLE_RAD),
    )

    points = [start]
    for index in range(1, segment_count):
        angle = start_angle + sweep_angle * index / segment_count
        points.append(
            (
                center[0] + radius * math.cos(angle),
                center[1] + radius * math.sin(angle),
            )
        )
    points.append(end)
    return points


def iter_segments(vertices: Sequence[Point2D]) -> Iterable[Tuple[Point2D, Point2D]]:
    for index in range(len(vertices) - 1):
        yield vertices[index], vertices[index + 1]


def sanitize_filename(text: str) -> str:
    cleaned = re.sub(r"[^\w.-]+", "_", text.strip())
    return cleaned.strip("._") or "river"


def unique_stem_for_run(stem: str, used_stems: Dict[str, int]) -> str:
    count = used_stems.get(stem, 0) + 1
    used_stems[stem] = count
    if count == 1:
        return stem
    return f"{stem}_{count}"


def orient_top_to_bottom(vertices: Sequence[Point2D]) -> List[Point2D]:
    ordered = list(vertices)
    if len(ordered) < 2:
        return ordered

    start = ordered[0]
    end = ordered[-1]
    if start[1] < end[1] or (
        math.isclose(start[1], end[1], abs_tol=EPSILON) and start[0] > end[0]
    ):
        ordered.reverse()
    return ordered


def polyline_length(vertices: Sequence[Point2D]) -> float:
    return sum(distance(p1, p2) for p1, p2 in iter_segments(vertices))


def point_and_tangent_at_chainage(
    vertices: Sequence[Point2D], chainage: float
) -> Tuple[Point2D, Point2D]:
    traversed = 0.0
    last_non_zero_segment: Optional[Tuple[Point2D, Point2D]] = None

    for p1, p2 in iter_segments(vertices):
        segment_length = distance(p1, p2)
        if segment_length <= EPSILON:
            continue

        last_non_zero_segment = (p1, p2)
        if chainage <= traversed + segment_length + EPSILON:
            offset = max(0.0, min(segment_length, chainage - traversed))
            ratio = offset / segment_length
            point = (
                p1[0] + ratio * (p2[0] - p1[0]),
                p1[1] + ratio * (p2[1] - p1[1]),
            )
            tangent = normalize(subtract(p2, p1))
            return point, tangent
        traversed += segment_length

    if last_non_zero_segment is None:
        return vertices[0], (0.0, 0.0)

    p1, p2 = last_non_zero_segment
    return p2, normalize(subtract(p2, p1))


def sample_polyline(vertices: Sequence[Point2D], interval: float) -> List[SamplePoint]:
    if len(vertices) < 2:
        return []

    total_length = polyline_length(vertices)
    if total_length <= EPSILON:
        return []

    chainages: List[float] = []
    current = 0.0
    while current < total_length - EPSILON:
        chainages.append(current)
        current += interval
    chainages.append(total_length)

    samples: List[SamplePoint] = []
    for index, chainage in enumerate(chainages, start=1):
        point, tangent = point_and_tangent_at_chainage(vertices, chainage)
        samples.append(
            SamplePoint(sn=index, chainage=chainage, point=point, tangent=tangent)
        )
    return samples


def segment_intersections(
    p1: Point2D, p2: Point2D, q1: Point2D, q2: Point2D
) -> List[Point2D]:
    r = subtract(p2, p1)
    s = subtract(q2, q1)
    denominator = cross(r, s)
    qp = subtract(q1, p1)

    if abs(denominator) <= EPSILON:
        if abs(cross(qp, r)) > EPSILON:
            return []

        rr = dot(r, r)
        if rr <= EPSILON:
            return []

        t0 = dot(subtract(q1, p1), r) / rr
        t1 = dot(subtract(q2, p1), r) / rr
        start_t = max(0.0, min(t0, t1))
        end_t = min(1.0, max(t0, t1))
        if end_t < -EPSILON or start_t > 1.0 + EPSILON or start_t > end_t + EPSILON:
            return []

        overlap_points: List[Point2D] = []
        for t in (start_t, end_t):
            point = add(p1, scale(r, t))
            if not overlap_points or distance(point, overlap_points[-1]) > 1e-6:
                overlap_points.append(point)
        return overlap_points

    t = cross(qp, s) / denominator
    u = cross(qp, r) / denominator
    if -EPSILON <= t <= 1.0 + EPSILON and -EPSILON <= u <= 1.0 + EPSILON:
        return [add(p1, scale(r, t))]
    return []


def deduplicate_offsets(
    offsets: Iterable[float], tolerance: float = 1e-6
) -> List[float]:
    unique_values: List[float] = []
    for value in sorted(offsets):
        if not unique_values or not math.isclose(
            value, unique_values[-1], abs_tol=tolerance
        ):
            unique_values.append(value)
    return unique_values


def crossings_along_cross_section(
    point: Point2D,
    tangent: Point2D,
    polylines: Sequence[PolylineData],
    cutoff: float,
) -> List[SectionCrossing]:
    normal = perpendicular_unit(tangent)
    if normal == (0.0, 0.0):
        return []

    start = add(point, scale(normal, -cutoff))
    end = add(point, scale(normal, cutoff))
    crossings: List[SectionCrossing] = []

    for polyline in polylines:
        raw_crossings: List[Tuple[float, Point2D]] = []
        for seg_start, seg_end in iter_segments(polyline.vertices):
            seg_tangent = normalize(subtract(seg_end, seg_start))
            for intersection in segment_intersections(start, end, seg_start, seg_end):
                offset = dot(subtract(intersection, point), normal)
                if abs(offset) <= cutoff + 1e-6:
                    raw_crossings.append((offset, seg_tangent))

        unique_offsets: List[float] = []
        for offset, seg_tangent in sorted(raw_crossings, key=lambda item: item[0]):
            if unique_offsets and math.isclose(offset, unique_offsets[-1], abs_tol=1e-6):
                continue
            unique_offsets.append(offset)
            crossings.append(
                SectionCrossing(
                    polyline=polyline,
                    offset=offset,
                    tangent=seg_tangent,
                )
            )

    return crossings


def average_aligned_tangent(
    reference_tangent: Point2D, other_tangents: Sequence[Point2D]
) -> Point2D:
    base_tangent = normalize(reference_tangent)
    if base_tangent == (0.0, 0.0):
        return base_tangent

    x_sum = base_tangent[0]
    y_sum = base_tangent[1]
    for tangent in other_tangents:
        aligned = normalize(tangent)
        if aligned == (0.0, 0.0):
            continue
        if dot(aligned, base_tangent) < 0:
            aligned = scale(aligned, -1.0)
        x_sum += aligned[0]
        y_sum += aligned[1]

    averaged = normalize((x_sum, y_sum))
    return averaged if averaged != (0.0, 0.0) else base_tangent


def analyze_section(
    sample: SamplePoint,
    current_centerline: PolylineData,
    centerlines: Sequence[PolylineData],
    cutoff: float,
) -> SectionAnalysis:
    crossings = crossings_along_cross_section(
        sample.point, sample.tangent, centerlines, cutoff
    )
    other_tangents = [
        crossing.tangent
        for crossing in crossings
        if crossing.polyline.handle != current_centerline.handle
    ]
    if not other_tangents:
        return SectionAnalysis(
            section_type="Normal",
            width_tangent=sample.tangent,
            bank_search_cutoff=cutoff,
        )

    return SectionAnalysis(
        section_type="Junction",
        width_tangent=average_aligned_tangent(sample.tangent, other_tangents),
        bank_search_cutoff=cutoff * 2.0,
    )


def calculate_bank_width(
    point: Point2D,
    tangent: Point2D,
    banklines: Sequence[PolylineData],
    cutoff: float,
) -> Optional[float]:
    offsets = [
        crossing.offset
        for crossing in crossings_along_cross_section(point, tangent, banklines, cutoff)
    ]

    negative_side = [offset for offset in offsets if offset < -1e-6]
    positive_side = [offset for offset in offsets if offset > 1e-6]
    if not negative_side or not positive_side:
        return None

    left_bank = max(negative_side)
    right_bank = min(positive_side)
    return right_bank - left_bank


def get_entity_closed(entity) -> bool:
    try:
        return bool(entity.Closed)
    except Exception:
        return False


def get_segment_bulge(entity, index: int) -> float:
    try:
        return float(entity.GetBulge(index))
    except Exception:
        return 0.0


def expand_bulged_segments(entity, vertices: Sequence[Point2D]) -> List[Point2D]:
    if len(vertices) < 2:
        return list(vertices)

    expanded: List[Point2D] = []
    for index in range(len(vertices) - 1):
        segment_points = tessellate_bulge_segment(
            vertices[index], vertices[index + 1], get_segment_bulge(entity, index)
        )
        for point in segment_points:
            append_distinct(expanded, point)

    if get_entity_closed(entity):
        segment_points = tessellate_bulge_segment(
            vertices[-1], vertices[0], get_segment_bulge(entity, len(vertices) - 1)
        )
        for point in segment_points:
            append_distinct(expanded, point)

    return expanded


def extract_vertices(entity) -> List[Point2D]:
    coords = list(entity.Coordinates)
    object_name = getattr(entity, "ObjectName", "")

    if object_name == "AcDbPolyline":
        stride = 2
    elif object_name == "AcDb3dPolyline":
        stride = 3
    else:
        stride = 3 if len(coords) % 3 == 0 else 2

    vertices: List[Point2D] = []
    for index in range(0, len(coords), stride):
        if index + 1 >= len(coords):
            break
        vertices.append((float(coords[index]), float(coords[index + 1])))

    if object_name in {"AcDbPolyline", "AcDb2dPolyline"}:
        return expand_bulged_segments(entity, vertices)
    return vertices


def read_xdata_from_handle(
    doc, handle: str, app_name: str
) -> Tuple[List[int], List[object]]:
    try:
        entity = doc.HandleToObject(handle)
        xdata_types, xdata_values = entity.GetXData(app_name)
    except Exception:
        return [], []

    type_list = list(xdata_types) if xdata_types else []
    value_list = list(xdata_values) if xdata_values else []

    normalized_types: List[int] = []
    for type_code in type_list:
        try:
            normalized_types.append(int(type_code))
        except (TypeError, ValueError):
            continue
    return normalized_types, value_list


def get_river_name(doc, handle: str, default_name: str) -> str:
    candidate_sets = [
        read_xdata_from_handle(doc, handle, XDATA_APP_NAME),
        read_xdata_from_handle(doc, handle, ""),
    ]

    for type_list, value_list in candidate_sets:
        if not type_list or not value_list:
            continue

        active_group_matches = False
        for type_code, value in zip(type_list, value_list):
            if type_code == 1001:
                active_group_matches = (
                    isinstance(value, str)
                    and value.strip().lower() == XDATA_APP_NAME.lower()
                )
                continue

            if active_group_matches and type_code == 1000:
                if isinstance(value, str) and value.strip():
                    return value.strip()

        for type_code, value in zip(type_list, value_list):
            if type_code == 1000 and isinstance(value, str) and value.strip():
                if value.strip().lower() != XDATA_APP_NAME.lower():
                    return value.strip()

    return default_name


def read_polylines_from_layer(
    acad: myAutoCAD,
    layer_name: str,
    include_river_name: bool = False,
    win32_doc=None,
) -> List[PolylineData]:
    polylines: List[PolylineData] = []
    supported_types = {"AcDbPolyline", "AcDb2dPolyline", "AcDb3dPolyline"}

    for entity in acad.model:
        if getattr(entity, "Layer", None) != layer_name:
            continue
        if getattr(entity, "ObjectName", None) not in supported_types:
            continue

        vertices = extract_vertices(entity)
        if len(vertices) < 2:
            continue

        default_name = f"river_{len(polylines) + 1}"
        handle = str(getattr(entity, "Handle", default_name))
        river_name = (
            get_river_name(win32_doc, handle, default_name)
            if include_river_name and win32_doc is not None
            else default_name if include_river_name else ""
        )
        polylines.append(
            PolylineData(
                handle=handle,
                layer=layer_name,
                vertices=(
                    orient_top_to_bottom(vertices) if include_river_name else vertices
                ),
                river_name=river_name,
            )
        )
    return polylines


def format_value(value: Optional[float]) -> str:
    if value is None:
        return ""
    return f"{value:.3f}"


def build_output_dir(document_name: str) -> Path:
    folder = Path.cwd() / OUTPUT_FOLDER_NAME / Path(document_name).stem
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def write_river_csv(
    centerline: PolylineData,
    banklines: Sequence[PolylineData],
    centerlines: Sequence[PolylineData],
    interval: float,
    cutoff: float,
    output_dir: Path,
    output_stem: str,
) -> Path:
    samples = sample_polyline(centerline.vertices, interval)
    output_path = output_dir / f"{output_stem}.csv"

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "SN",
                "Easting",
                "Northing",
                "Bed width",
                "Bank slope",
                "Bed elevation",
                "Type",
            ]
        )

        for sample in samples:
            section = analyze_section(sample, centerline, centerlines, cutoff)
            bed_width = calculate_bank_width(
                sample.point,
                section.width_tangent,
                banklines,
                section.bank_search_cutoff,
            )
            writer.writerow(
                [
                    sample.sn,
                    format_value(sample.point[0]),
                    format_value(sample.point[1]),
                    format_value(bed_width),
                    "",
                    "",
                    section.section_type,
                ]
            )

    return output_path


def summarize_junction_count(
    centerline_count: int, bankline_count: int
) -> Tuple[float, float]:
    junctions_from_centerlines = (centerline_count - 1) / 2.0
    junctions_from_banklines = bankline_count - 2
    return junctions_from_centerlines, junctions_from_banklines


def main() -> None:
    print("Connecting to the active AutoCAD document...")
    pythoncom.CoInitialize()
    win32_doc = win32com.client.Dispatch("AutoCAD.Application").ActiveDocument
    acad = myAutoCAD(create_if_not_exists=False)
    document_name = acad.doc.Name
    print(f"Active drawing: {document_name}")

    centerlines = read_polylines_from_layer(
        acad, CENTERLINE_LAYER, include_river_name=True, win32_doc=win32_doc
    )
    banklines = read_polylines_from_layer(
        acad, BANKLINE_LAYER, include_river_name=False, win32_doc=win32_doc
    )

    centerline_count = len(centerlines)
    bankline_count = len(banklines)
    junctions_from_centerlines, junctions_from_banklines = summarize_junction_count(
        centerline_count, bankline_count
    )

    print(f"Centerlines found on '{CENTERLINE_LAYER}': {centerline_count}")
    print(f"Banklines found on '{BANKLINE_LAYER}': {bankline_count}")
    print(f"Junction estimate from centerlines: {junctions_from_centerlines:g}")
    print(f"Junction estimate from banklines: {junctions_from_banklines:g}")

    if centerline_count == 0:
        raise RuntimeError(f"No centerlines found on layer '{CENTERLINE_LAYER}'.")
    if bankline_count == 0:
        raise RuntimeError(f"No banklines found on layer '{BANKLINE_LAYER}'.")

    if not math.isclose(
        junctions_from_centerlines, junctions_from_banklines, abs_tol=1e-6
    ):
        print(
            "Warning: junction estimates from centerlines and banklines do not match. "
            "CSV generation will continue using the geometry found in the drawing."
        )

    output_dir = build_output_dir(document_name)
    generated_files: List[Path] = []
    used_stems: Dict[str, int] = {}

    for centerline in centerlines:
        output_stem = unique_stem_for_run(
            sanitize_filename(centerline.river_name), used_stems
        )
        csv_path = write_river_csv(
            centerline=centerline,
            banklines=banklines,
            centerlines=centerlines,
            interval=SAMPLING_INTERVAL_M,
            cutoff=BANK_SEARCH_CUTOFF_M,
            output_dir=output_dir,
            output_stem=output_stem,
        )
        generated_files.append(csv_path)
        print(f"Wrote {centerline.river_name} -> {csv_path}")

    print(f"Generated {len(generated_files)} river CSV file(s) in {output_dir}")


if __name__ == "__main__":
    main()
