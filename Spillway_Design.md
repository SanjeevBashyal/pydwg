## CHAPTER 2

## HYDRAULIC THEORY

## Section I. Introduction

2-l. General. This section presents hydraulic design theory, available experimental data and coefficients, and discussions of analysis and problems related to spillway design. Generally, the presentations assume that the design engineer is acquainted with the hydraulic theories involved in uniform flow, gradually and rapidly varied flow, steady and unsteady flow, energy and momentum principles, and other aspects such as energy losses, cavitation, etc., related to hydraulic design. These matters are normally covered in hydraulic handbooks and texts such as those by King and Brater (item 24), Rouse (items 49 and 50), and Chow (item 10). This manual is presented as guidance in the application of textbook material and as additional information not readily available in general reference material. The application of the theory of flow through spillways is based largely upon empirical coefficients, so the designer should deal with maximum and minimum values as well as averages, depending upon the design objective. To be conservative, the designer should generally use maximum loss factors in computing discharge capacity, and minimum loss factors in computing velocities for the design of energy dissipators. As more model and prototype data become available, the range between maximum and minimum coefficients used in design should be narrowed. An example in which the hydraulic design procedures and guidance discussed in this manual are applied to the computation required to design a typical reservoir spillway is shown in Appendix D.

2-2. Basic Considerations. A spillway is sized to provide the required capacity, usually the entire spillway design flood, at a specific reservoir elevation. This elevation is normally at the maximum operating level or at a surcharge elevation greater than the maximum operating level. Hydraulic analysis of a spillway usually involves four conditions of flow:
a. Subcritical flow in the spillway approach, initially at a low velocity, accelerating, however, as it approaches the crest.
b. Critical flow as the water passes over the spillway crest.
c. Supercritical flow in the chute below the crest.
d. Transitional flow at or near the terminus of the chute where the flow must transition back to subcritical.

When a relatively large storage capacity can be obtained above the normal maximum reservoir elevation by increasing the dam height, a portion of the flood volume can be stored in this reservoir surcharge space and the size of the spillway can be reduced. The use of a surcharge pool for passing the spillway design flood involves an economic analysis that considers the added cost of a dam height compared to the cost of a wider and/or deeper spillway. When a gated spillway is considered, the added cost of higher and/or additional gates and piers must be compared to the cost of additional dam height.

When an ungated spillway is considered, the cost of reduced flood-control benefits due to a reduction in reservoir storage must be compared to the cost of additional dam height. The transition of flow from supercritical on the chute to subcritical usually involves considerable energy dissipation. Dissipation of hydraulic energy is accomplished by various methods such as the hydraulic jump, impact, dispersion, etc. The type of energy dissipator used is dependent upon factors that include site geology, the type of dam structure, and the magnitude of the energy to be dissipated. The design discharge for effective energy dissipation is frequently set at the standard project flood rate; however, each facility must be evaluated, and the design discharge used should be dependent upon the damage consequences when the design discharge is exceeded.

Section II. Spillway Discharge

## 2-3. General.

a. The ogee crest spillway is basically a sharp-crested weir with the space below the lower nappe filled with concrete. The discharge over a spillway crest is limited by the same parameters as the weir, and determined by the following:

$$
\begin{equation*}
Q=C L e_{e}^{H_{e}^{1.5}} \tag{$2-1$}
\end{equation*}
$$

where

$$
\begin{aligned}
Q & =\text { rate of discharge, cubic feet per second }\left(\mathrm{ft}^{3} / \mathrm{sec}\right) \\
C & =\text { coefficient of discharge } \\
L_{e} & =\text { effective length of the crest, feet } \\
H_{e} & =\text { total specific energy above the crest, feet }
\end{aligned}
$$

Extensive investigations of spillway crest shapes, pressures, and coefficients have provided empirical data that will allow the designer to develop a spillway that minimizes the structural size required for the design discharge. Minimization of the structure size is achieved by underdesigning the spillway crest within limits discussed in Chapter 3.
b. An underdesigned crest is defined when the following relationship is true:

$$
\frac{H_{e}}{H_{d}}>1
$$

where $\mathrm{H}_{\mathrm{d}}$ is the crest design head, feet. The design head is a major parameter of the ogee crest shape equation and is discussed in Section II of Chapter 3. Underdesigning the crest results in increasing the discharge coefficient significantly above that of the sharp-crested weir; however, the underdesigned crest results in a reduction of the hydrodynamic pressures on the crest surface. Depending on the degree of underdesigning, the crest pressures can be significantly less than atmospheric.

2-4. Abutment and Piers. All spillways include abutments of some type, and many include intermediate piers. The effect that the abutments and piers have on the discharge must be accounted for; this is accomplished by modifying the crest length using the following equation to determine the effective crest length $\mathrm{L}_{\mathrm{e}}$ :

$$
\begin{equation*}
L_{e}=L-2\left(n K_{p}+K_{a}\right) H_{e} \tag{2-2}
\end{equation*}
$$

where

> L = net length of crest
> $\mathrm{n}=$ number of piers
> K = pier contraction coefficient
> Kp = abutment contraction coefficient

2-5. Effect of Approach Flow. Another factor influencing the discharge coefficient of a spillway crest is the depth in the approach channel relative to the design head defined as the ratio $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$, where P equals the crest elevation minus the approach channel invert elevation. As the depth of the approach channel $P$ decreases relative to the design head, the effect of approach velocity becomes more significant; and at $\mathrm{P} / \mathrm{H}_{\mathrm{a}} \leqq 1.0$, this effect should not be neglected. The slope of the upstream spillway face also influences the coefficient of discharge. As an example, for $\mathrm{P} / \mathrm{H}_{\mathrm{d}}>1$, the
flatter upstream face slopes tend to produce an increase in the discharge coefficient. Several investigators have provided data on approach depth and spillway face slope effects. The most recent work has been done by WES (item 28). Data from this work have been used extensively in this manual. The planform of the approach channel can significantly influence the spillway discharge characteristics. The influence of the planform can be evaluated thoroughly only by the use of a site-specific physical model. In some cases a two-dimensional numerical model will be entirely adequate. In the case of a simple spillway approach, analysis of the water surface profile by a standard step method would be sufficient. Spillway approach channels and slope of the upstream spillway face are further discussed in Chapter 3.

## Section III. Gradients

2-6. General. The basic principle used to analyze steady incompressible flow through a spillway is the law of conservation of energy expressed by the Bernoulli (energy) equation. The energy equation, generalized to apply to the entire cross section of flow, expresses the energy at any point on the cross section in feet of water by equation 2-3:

$$
\begin{equation*}
H=Z+\frac{P}{v}+\alpha \frac{V^{2}}{2 g} \tag{2-3}
\end{equation*}
$$

where

$$
\begin{aligned}
& H=\text { total energy head in feet of water above the datum plane } \\
& Z=\text { height above a datum plane, feet } \\
& P=\text { pressure at the point, pounds per square foot }\left(l \mathrm{~b} / \mathrm{ft}^{2}>\right.
\end{aligned}
$$

$\gamma=$ specific weight of water, pounds per cubic foot ( $\mathrm{lb} / \mathrm{ft}^{3}>$
$\alpha=$ energy correction coefficient
V = average flow velocity, feet per second (ft/sec)
$\mathrm{g}=$ acceleration due to gravity, $\mathrm{ft} / \mathrm{sec}^{2}$
For most practical problems involving regular-shaped channels, the energy correction coefficient may be taken as unity without serious error.

2-7. Hydraulic and Energy Grade Lines. The hydraulic grade line, also referred to as the mean pressure gradient, may be above, below, or at the free water surface. Defining $Z$ as the invert elevation of a point on the chute, then $Z+p / \gamma$ defines the elevation of the hydraulic grade line at that point. The locus of values of $Z+p / \gamma$ along the spillway describes the mean pressure gradient. The mean pressure gradient at any point along the spillway is always lower than the energy grade line by the value of the mean velocity head at that point. The mean pressure gradient is useful in determining pressures acting on the spillway surface and in determining cavitation potential. For most open channel flow the $p / \gamma$ term can be replaced by $Y_{1} \cos \theta$ where $Y_{1}$ is the flow depth normal to the channel bottom and $\theta$ is the slope of the channel bottom. Therefore, the sum $Z+Y_{1} \cos \theta$ will be equal to the elevation of the water surface at the point and the free surface is the hydraulic grade line for all points on the cross section. For this substitution to be valid, the assumption must be made that the pressure distribution at the point must be hydrostatic, a condition that will occur if conditions are such that vertical acceleration of the flow is negligible and the bed slope is mild. ${ }_{2}$ A nonhydrostatic pressure distribution will occur whenever the value of $\cos ^{2} \theta$ departs materially from unity, such as with steep spillway chutes. The departure of the pressure distribution from hydrostatic due to a steep bed slope does not mean the energy equation cannot be used on steep spillway chutes as a design tool. It means that the designer must recognize that the values derived become increasingly inaccurate as the $\cos ^{2} \theta$ value departs further from unity. This condition describes one of the basic reasons that physical model studies may be required when designing a spillway.

2-8. Mean Spillway Pressure Computation. The mean pressure at any location along a chute is determined using the principle of conservation of energy as expressed by the energy equation. Conservation of energy requires that the energy at one location on the spillway be equal to the energy at any downstream location plus all intervening energy losses. Expressed in equation form and in units of feet of water

$$
\begin{equation*}
z_{1}+\frac{p_{1}}{\gamma}+\alpha_{1} \frac{v_{1}^{2}}{2 g}=z_{2}+\frac{p_{2}}{\gamma}+\alpha_{2} \frac{v_{2}^{2}}{2 g}+H_{L} \tag{2-4a}
\end{equation*}
$$

or for the hydraulic assumption

$$
\begin{equation*}
Z_{1}+Y_{1} \cos \theta+\alpha_{1} \frac{V_{1}^{2}}{2 g}=Z_{2}+Y_{2} \cos \theta+\alpha_{2} \frac{V_{2}^{2}}{2 g}+H_{L} \tag{2-4b}
\end{equation*}
$$

Information on the determination of energy losses, $\mathrm{H}_{\mathrm{L}}$, associated with flow over spillways is given in appropriate sections of this engineering manual.

## Section IV. Spillway Energy Loss

2-9. General. The determination of hydraulic energy loss associated with flow through a spillway system is important to the design of the training walls, piers, and terminal structure. Energy loss is the direct result of three conditions: boundary roughness (friction), turbulence resulting from boundary alignment changes (form loss), and boundary layer development. Sufficient data and procedures are available to make a reasonably accurate determination of the energy loss during development of the turbulent boundary layer and for fully turbulent flow. Form losses are usually minimal for most spillways; however, when the configuration of a spillway is such that form losses outside the range of experience are encountered, model studies are required. Methods and data necessary for spillway energy loss computations are provided in the following paragraphs.

## 2-10. Energy Loss for Fully Developed Turbulent Boundary Layer Flow.

a. General. Methods for determining the energy loss related to boundary roughness (friction) have been developed by various investigators. The most notable and widely used methods are the Darcy-Weisbach equation, the Chezy equation, and the Manning equation. The Darcy-Weisbach equation involves the direct use of a known effective roughness value, k , from which a boundary resistance (friction) coefficient, f , can be derived for use in the energy loss computation. The Darcy-Weisbach equation is applicable to all fully turbulent flow conditions. The Chezy equation is essentially similar to the Darcy-Weisbach equation in that it involves the direct use of a known effective roughness value and is applicable to all flow conditions. The Manning equation, probably the most commonly used, involves use of an empirically derived resistance coefficient, n , and is considered only applicable to fully turbulent flow. Some investigators such as Strickler have attempted to correlate the Manning's n value to a measured effective roughness value; others have equated the Manning equation to the Darcy-Weisbach equation and to the Chezy equation in order to take advantage of the effective roughness parameter used in those equations. These modifications to the Manning equation have all been accomplished in order to establish some degree of confidence for an otherwise empirically derived roughness coefficient.
b. Darcy-Weisbach Equation. The Darcy-Weisbach equation expresses the energy loss due to boundary roughness in terms of a resistance coefficient, f , as:

$$
\begin{equation*}
h_{f}=\frac{f L}{4 R}\left(\frac{V^{2}}{2 g}\right) \tag{2-5}
\end{equation*}
$$

where $\mathrm{h}_{\mathrm{f}}$ is the energy loss due to friction through a length of channel L having an average hydraulic radius R and an average velocity V . The energy loss has a length dimension ( $\mathrm{ft}-\mathrm{lb} / \mathrm{lb}$ ) and is usually expressed in feet of water. The resistance coefficient, f , is a dimensionless parameter which
can be determined for fully turbulent flow conditions by a form of the Colebrook-White equation

$$
\begin{equation*}
f=\left[\frac{1}{2 \log \left(\frac{13.8 \mathrm{R}}{\mathrm{k}}\right)}\right]^{2} \tag{2-6}
\end{equation*}
$$

or by the Strickler-Manning equation

$$
\begin{equation*}
f=0.113\left(\frac{k}{R}\right)^{1 / 3} \tag{2-7}
\end{equation*}
$$

which may more accurately derive the resistance coefficient for $R / k>100$. In both equations 2-6 and 2-7, $k$ is the effective roughness value and $R$ is the hydraulic radius. Both equations 2-6 and 2-7 are valid only for fully turbulent flow defined by the relationship:

$$
\begin{equation*}
R_{e}>\frac{200}{f^{1 / 2}}\left(\frac{4 R}{k}\right) \tag{2-8}
\end{equation*}
$$

where $\mathrm{R}_{\mathrm{e}}$ is the Reynolds number. The actual Reynolds number of the flow condition is defined as:

$$
\begin{equation*}
\mathrm{R}_{\mathrm{e}}=\frac{4 \mathrm{RV}}{v} \tag{2-9}
\end{equation*}
$$

where $\nu$ is the kinematic viscosity of the water. Resistance coefficients throughout the entire range of flow conditions can be obtained through the use of Plate 2-1.
C. Chezy Equation. The Chezy equation defines velocity in terms of the hydraulic radius, the slope S , and the Chezy resistance coefficient C in the form of

$$
\begin{equation*}
V=C(R S)^{1 / 2} \tag{2-10}
\end{equation*}
$$

By equating S to $\mathrm{h}_{\mathrm{f}} / \mathrm{L}$ and rearranging terms in equation 2-10, the Chezy equation expresses the energy loss due to boundary roughness as

$$
\begin{equation*}
h_{f}=\frac{L}{R} \frac{V^{2}}{C^{2}} \tag{2-11}
\end{equation*}
$$

The resistance coefficient, $C$, is dependent upon the Reynolds number and the effective roughness value. The C value can be determined through the use of Plate 2-1 or by equation 2-12:

$$
\begin{equation*}
C=32.6 \log \left(\frac{12.2 \mathrm{R}}{\mathrm{k}}\right) \tag{2-12}
\end{equation*}
$$

for fully turbulent flow conditions as defined by the relationship:

$$
\begin{equation*}
\mathrm{R}_{\mathrm{e}}>\frac{50 \mathrm{CR}}{\mathrm{k}} \tag{2-13}
\end{equation*}
$$

Chezy's C can also be determined through the use of the Darcy-Weisbach resistance coefficient, f , by equation 2-14:

$$
\begin{equation*}
C=\left(\frac{8 g}{f}\right)^{1 / 2} \tag{2-14}
\end{equation*}
$$

The characteristics of f in circular pipe flow have been thoroughly investigated by Nikuradse and Colebrook and White; however, a similar complete investigation of the characteristics of $C$ in open channel flow have not been made due to the extra variables and wide range of surface roughness involved. However, reasonably accurate results should be obtained through the use of the Chezy equation.
d. Manning Equation. The Manning equation 2-15 defines velocity in terms of the hydraulic radius and slope, in a similar manner to the Chezy equation; however, the resistance coefficient is defined by the Manning's n value.

$$
\begin{equation*}
\mathrm{v}=\frac{1.486 \mathrm{R}^{2 / 3} \mathrm{~S}^{1 / 2}}{\mathrm{n}} \tag{2-15}
\end{equation*}
$$

The constant 1.486 converts the metric equation to foot-second units. By equating $\mathrm{S}=\mathrm{h}_{\mathrm{f}} / \mathrm{L}$ and rearranging terms in equation 2-15, the Manning equation expresses the energy loss due to boundary roughness as

$$
\begin{equation*}
h_{f}=\frac{V^{2} n^{2} L}{2.21 R^{4 / 3}} \tag{2-16}
\end{equation*}
$$

The Manning's resistance coefficient n , reported in numerous hydraulic publications, is founded on empiricism. It does not address the degree of turbulence or the interaction between the flow and boundary. The empiricism of this coefficient limits its accuracy when applied to conditions somewhat different from those from which it is derived. However, Manning's method is widely used due mainly to the large volume of reference data available to correlate resistance coefficients with boundary conditions and the ease in which the method can be used. When the design involves a significant amount of surface roughness energy loss resulting from fully turbulent flow, such as with a long spillway chute, the Manning's resistance coefficient may be calculated to account for the relative roughness effect by the use of

$$
\begin{equation*}
n=\frac{f^{1 / 2} R^{1 / 6}}{10.8} \tag{2-17}
\end{equation*}
$$

or

$$
\begin{equation*}
\mathrm{n}=1.486 \frac{\mathrm{R}^{1 / 6}}{\mathrm{C}} \tag{2-18}
\end{equation*}
$$

and the procedures described for equation 2-6 or 2-7. A review of energy loss computation using the Manning equation 2-16 modified to account for relative roughness by equations 2-6 or 2-7 and 2-17 or 2-18 will show that, if the effect of relative roughness is required, the Darcy-Weisbach or the Chezy method provides a more direct and simpler procedure.
e. Roughness Values. Values of effective roughness k normally are based on prototype measurements of flow over various boundary materials rather than physically measured values. Essentially all hydraulic textbooks provide extensive data of Chezy's C and Manning's n values; however, data are somewhat limited on effective roughness values k . Some suggested roughness values for various spillway surfaces are provided in the following tabulation:

| Surface | Effective Roughness k, feet |
| :--- | :--- |
| Concrete |  |
| For discharge design | 0.007 |
| For velocity design | 0.002 |
| Excavated rock |  |
| Smooth and uniform | 0.025-0.25 |
| Jagged and irregular | 0.15-0.55 |
| Natural vegetation |  |
| Short grass | 0.025-0.15 |
| Long grass | 0.10-0.55 |
| Scattered brush and weeds | 0.15-1.0 |

Due to the inability to predict the roughness that will be constructed, the designer should use maximum values in computing flow profiles and minimum values in computing energy losses required for terminal structure design.

2-11. Turbulent Boundary Layer Development Energy Loss. The surface roughness energy loss associated with free flow (ungated) on an overflow crest spillway with a $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ ratio greater than one is dependent upon the development of the turbulent boundary layer thickness. Boundary layer development is important to the designer because the principles of energy loss based upon the methods appropriate for fully turbulent flow are not valid until the boundary layer is fully developed. However, the use of the following procedure is dependent upon the spillway flow approach conditions conforming to the following assumptions:
a. The flow approaching the spillway must have potential flow velocity distribution (constant velocity throughout the flow depth).
b. The flow depth is large so that the depth of approach flow can be considered constant.
c. No restrictions exist at the spillway entrance that would cause an abrupt disturbance of the water and velocity distribution.

The turbulent boundary layer thickness $\delta$ (all values in feet) is a function of the length, L , along the spillway from the start of the crest curve and the effective roughness, k , described as

$$
\begin{equation*}
\frac{\delta}{L}=0.08\left(\frac{L}{k}\right)^{-0.233} \tag{2.19}
\end{equation*}
$$

The decrease in energy flux in the turbulent boundary layer caused by friction is by definition the energy thickness $\delta_{3}$. The decrease in, the volume of flow in the boundary layer caused by friction is by definition the displacement thickness $\delta_{1}$. Based on experimental data the relationship between the displacement thickness $\delta_{1}$, the energy thickness $\delta_{3}$, and the turbulent boundary layer thickness is:

$$
\begin{align*}
& \delta_{1}=0.18 \delta  \tag{2-20}\\
& \delta_{3}=0.22 \delta \tag{2-21}
\end{align*}
$$

The potential flow velocity at any location $T$ investigated on the spillway is determined from equation $2-22$, using a trial procedure

$$
\begin{equation*}
h_{T}=d_{P} \cos \theta+\frac{u^{2}}{2 g} \tag{2-22}
\end{equation*}
$$

where

$$
\begin{aligned}
\mathrm{h}_{\mathrm{T}} & =\text { reservoir elevation minus spillway elevation at location } \mathrm{T} \text {, feet } \\
\mathrm{d}_{\mathrm{p}} & =\text { potential flow depth at location } \mathrm{T} \text {, feet } \\
\theta & =\text { interior angle between spillway face at location } \mathrm{T} \text { and } \\
& \text { horizontal, degrees } \\
\mathrm{u} & =\text { potential flow velocity, } \mathrm{ft} / \mathrm{sec}
\end{aligned}
$$

The spillway energy loss, $\mathrm{H}_{\mathrm{L}}$, in terms of feet of head, is defined by the following equation:

$$
\begin{equation*}
H_{L}=\frac{\delta_{3} u^{3}}{2 g q} \tag{2-23}
\end{equation*}
$$

where q is the unit discharge in cubic feet per second per foot $\left(\mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft}\right)$. The actual depth of flow, d , at the location under investigation is equal to the potential flow depth determined from equation 2-23 plus the displacement thickness from equation 2-20.

$$
\begin{equation*}
d=d_{D}+\delta_{1} \tag{2-24}
\end{equation*}
$$

The critical point is defined as the location where the turbulent boundary layer intersects the free surface flow, which is the location where the
turbulent boundary layer thickness becomes equal to the actual flow depth. Downstream from the critical point, energy loss computations are based on fully turbulent flow, as discussed in paragraph 2-10, are appropriate. Reference is made to HDC Sheets and Charts 111-18 to 111-18/5 for additional information on procedures involved in determination of boundary layer development energy loss.

Section V. Hydraulic Jump Energy Dissipator
2-12. General.
a. Types of Energy Dissipators. Spillway energy dissipators are required to operate safely and effectively throughout a wide range of discharges, for extended periods of time, without having to shut down for emergency repairs. Energy dissipators normally used at CE dams are the hydraulic jump stilling basin, the roller bucket, and the flip bucket. Discussion on the selection and merits of each of these dissipators is presented in Chapter 7.
b. Unit Horsepower. When designing an energy dissipator, the horsepower per foot of width entering the dissipator should be determined. Unit horsepower, which provides an index of the severity of the entering energy conditions, can be expressed as

$$
\begin{equation*}
h_{p}=\frac{q \gamma\left(d_{1}+h_{e}\right)}{550} \tag{2-25}
\end{equation*}
$$

where

$$
\begin{aligned}
q & =\text { discharge per unit width of }{ }_{3} \text { spillway, } \mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft} \\
\gamma & =\text { unit weight of water, } 1 \mathrm{~b} / \mathrm{ft}^{3} \\
\mathrm{~d}_{1} & =\text { depth of flow at entrance to dissipator, feet } \\
\mathrm{h}_{\mathrm{e}} & =\text { velocity head }=\mathrm{V}_{1}^{2} / 2 \mathrm{~g} \text { where } \mathrm{V}_{1}=\text { mean velocity of flow at } \\
& \text { entrance to dissipator, ft } / \mathrm{sec}
\end{aligned}
$$

Plate 2-2 depicts the unit horsepower for a number of existing large spillways. This plate is presented to permit the designer to investigate operating experience with energy dissipators subjected to unit horsepower of a magnitude comparable to the projected design.

2-13. Hydraulic Jump Type Energy Dissipator. The hydraulic jump energy dissipator, defined as a stilling basin, is used to dissipate kinetic energy by the formation of a hydraulic jump. The hydraulic jump involves the principle of conservation of momentum. This principle states that the pressure plus momentum of the entering flow must equal the pressure plus momentum of the exiting flow plus the sum of the applied external forces in the basin. The hydraulic jump will form when the entering Froude number $F_{1}$, the entering flow depth $\mathrm{d}_{1}$, and the sequent flow depth $\mathrm{d}_{2}$ satisfy the following equation:

$$
\begin{equation*}
\frac{d_{2}}{d_{1}}=0.5\left[\left(1+8 F_{1}^{2}\right)^{1 / 2}-1\right] \tag{2-26}
\end{equation*}
$$

where

$$
\begin{equation*}
F_{1}=\frac{V_{1}}{\left(g d_{1}\right)^{1 / 2}} \tag{2-27}
\end{equation*}
$$

The energy losses within the basin and the forms of a hydraulic jump are dependent upon the entering Froude number. With Froude numbers $F_{1}$ less than 4.0, the jump is somewhat inefficient in energy dissipation and is hydraulically unstable. The entering flow oscillates between the bottom of the basin and the water surface, resulting in irregular period waves which will propagate downstream. EM 1110-2-1605 presents a discussion on the design of hydraulic jump stilling basins with entering Froude numbers less than 4.0. A well-stabilized and efficient jump will occur with Froude numbers $F$ between 4.5 and 9.0. Jumps with Froude numbers $F_{1}$ greater than 9.0 are highly efficient in energy dissipation; however, a rough surface will exist that will propagate waves downstream. The energy loss $\Delta \mathrm{E}$ resulting in a hydraulic jump is equal to the difference in specific energies before, $\mathrm{E}_{1}$, and after, $\mathrm{E}_{2}$, the jump which can be estimated by the following equation:

$$
\begin{equation*}
\Delta E=E_{1}-E_{2}=\frac{\left(d_{2}-d_{1}\right)^{3}}{4 d_{1} d_{2}} \tag{2-28}
\end{equation*}
$$

The length $\mathrm{L}_{\mathrm{j}}$ of a hydraulic jump on a flat floor without baffles, end sill, or runout slope (not necessarily the stilling basin length) can be estimated by the following equations:

$$
\begin{align*}
& L_{\mathrm{j}}=8.0 \mathrm{~d}_{1} \mathrm{~F}_{1} \text { for } \mathrm{F}_{1}>5  \tag{2-29a}\\
& L_{\mathrm{j}}=3.5 \mathrm{~d}_{1} \mathrm{~F}_{1}^{1.5} \text { for } 2<\mathrm{F}_{1}<5 \tag{2-29b}
\end{align*}
$$

The presence of baffles and/or end sills In the basin will shorten the jump length and reduce the $\mathrm{d}_{2}$ depth required to produce the jump. The analysis of a hydraulic jump can be accomplished using the principle of conservation of momentum which requires that the rate of change of momentum entering and leaving the jump be equal to the summation of forces acting upon the fluid. The forces include the hydrostatic pressure force at each end of the jump which is expressed as

$$
\begin{equation*}
P_{1}=\frac{\gamma d_{1}^{2}}{2} \tag{2-30}
\end{equation*}
$$

$$
\begin{equation*}
P_{3}=\frac{\gamma d_{3}^{2}}{2} \tag{2-31}
\end{equation*}
$$

the force exerted by the baffles, expressed as

$$
\begin{equation*}
P_{B}=C_{D} \rho\left(\frac{V_{B}^{2} h}{2}\right) \tag{2-32}
\end{equation*}
$$

and the force exerted by the face of the end sill which is expressed as:

$$
\begin{equation*}
P_{S}=\gamma h_{s}\left(d_{3}+\frac{h_{s}}{2}\right) \tag{2-33}
\end{equation*}
$$

where

$$
\begin{aligned}
\mathrm{P}_{1} & =\text { hydrostatic pressure of the entering flow, lb/ft } \\
\mathrm{P}_{3} & =\text { hydrostatic pressure of the exiting flow, lb/ft } \\
d_{3} & =\text { depth of flow above the end sill, feet } \\
\mathrm{P}_{\mathrm{B}} & =\text { force exerted by the baffles, lb/ft } \\
C_{\mathrm{D}} & =\text { baffle drag coefficient } \\
\rho & =\text { mass density of water pounds-seconds squared per feet to the fourth } \\
& \text { power (lb-sec²/ft4) } \\
V_{\mathrm{B}} & =\text { average velocity at face of the baffle, ft/sec } \\
\mathrm{h} & =\text { height of the baffle, feet } \\
P_{\mathrm{S}} & =\text { force exerted by the end sill, lb/ft } \\
\mathrm{h}_{\mathrm{s}} & =\text { height of end sill, feet }
\end{aligned}
$$

Equation 2-33 assumes hydrostatic pressure distribution on the end sill. This assumption is considered valid unless the baffle piers are located too near the sill, resulting in a reduced pressure on the face of the end sill. The pressure reduction would require a theoretical increase in the downstream depth to provide the necessary force for jump stabilization. A friction force also exists along the basin wetted perimeter but is small enough to be neglected. Therefore, assuming two-dimensional flow, the momentum equation for a hydraulic jump which includes baffle piers and an end sill can be expressed as

$$
\begin{equation*}
\rho \mathrm{qV}_{1}-\rho \mathrm{qV}_{3}=\mathrm{P}_{3}-\mathrm{P}_{1}+\mathrm{P}_{\mathrm{B}}+\mathrm{P}_{\mathrm{S}} \tag{2-34}
\end{equation*}
$$

where $V_{3}$ is the mean velocity at exit of dissipator or restated as

$$
\begin{equation*}
\gamma\left(\frac{q^{2}}{g d_{1}}-\frac{q^{2}}{g d_{3}}\right)=\gamma\left(\frac{d_{3}^{2}}{2}-\frac{d_{1}^{2}}{2}\right)+C_{D} \rho\left(\frac{V_{B}^{2} h}{2}\right)+\gamma h_{s}\left(d_{3}+\frac{h_{s}}{2}\right) \tag{2-35}
\end{equation*}
$$

Solution of this equation for the required depth $d_{3}$ can be accomplished by successive trials for any specific baffle pier and end sill arrangement provided information is available to evaluate the baffle force. The baffle force is dependent upon the drag coefficient corresponding to the type of baffle
used and the velocity in the vicinity of the baffle. The appropriate velocity can be estimated from Plate 2-3, which shows the distribution of velocity in a hydraulic jump. The baffle drag coefficient is a function of baffle shape and spacing. Limited information available on baffle drag coefficients indicates that the following values should be reasonable: 0.6 for a single row of baffles and 0.4 for a double row. Further discussion on baffles and end sills is found in Chapter 7.

2-14. Sidewall Dynamic Load. The turbulence created by the hydraulic jump imposes forces on the stilling basin sidewalls. The magnitude of the dynamic load is important in the structural design of the walls. Tests to determine sidewall forces were conducted at WES with an instrumented sidewall in a stilling basin that did not contain baffles or an end sill (item 19). These tests were conducted with Froude numbers $F_{1}$ that varied between 2.7 and 8.7, and resulted in the development of the following empirical equation:

$$
\begin{equation*}
\mathrm{R}_{\mathrm{m}}=3.75 \mathrm{H}_{\mathrm{s}}^{-1.05}{ }_{\rho \mathrm{V}_{1}} \mathrm{qF}_{1}^{-1.42} \tag{2.36}
\end{equation*}
$$

where

$$
\begin{aligned}
\mathrm{R}_{\mathrm{m}}= & \text { average minimum static plus dynamic unit force at the toe of } \\
& \text { the hydraulic jump, lb/ft } \\
\mathrm{H}_{\mathrm{s}}= & \text { spillway height, crest elevation minus stilling basin apron } \\
& \text { elevation, feet }
\end{aligned}
$$

The magnitude of the unit force on the sidewall varies along the length of the stilling basin. Plate 2-4 defines the variation in unit force by use of the normalizing functions, described by equations $2-37$ through $2-39$, versus the distance ratio $\mathrm{x} / \mathrm{L}_{\mathrm{b}}$.

$$
\begin{gather*}
\frac{R-R_{m}}{R_{s}-R_{m}}=C  \tag{2-37}\\
\frac{\left(R_{+}\right)-R_{m}}{R_{s}-R_{m}}=C_{+}  \tag{2-38}\\
\frac{\left(R_{-}\right)-R_{m}}{R_{s}-R_{m}}=C_{-} \tag{2-39}
\end{gather*}
$$

where

$$
\begin{aligned}
\mathrm{x}= & \text { distance measured from the point of intersection of the spill- } \\
& \text { way slope and the basin apron to the center line of the wall } \\
& \text { unit being analyzed } \\
\mathrm{R}_{,} \mathrm{R}_{+}, \mathrm{R}_{-}= & \text {length of the stilling basin, feet } \\
& \text { average unit resultant force, maximum instantaneous unit } \\
& \text { force, respectively, acting on the sidewall when the actual }
\end{aligned}
$$

$$
\begin{aligned}
& \text { depth of tailwater } \mathrm{d}_{\mathrm{TW}} \text { is less than or equal to } \mathrm{d} 2 \text { or the } \\
& \text { basin wall height, } \mathrm{lb} / \mathrm{ft} \\
\mathrm{R}_{\mathrm{S}} & =\text { static unit force on the sidewall unit due to the theoretical } \\
& \text { sequent depth for a hydraulic } \mathrm{jump}, \mathrm{lb} / \mathrm{ft}
\end{aligned}
$$

When $\mathrm{d}_{\mathrm{TW}}>\mathrm{d}_{2}, \mathrm{R}, \mathrm{R}_{+}$, and $\mathrm{R}_{-}$must be adjusted as shown by equation 2-40 through 2-42 to account for the increased force resulting from the difference between $\mathrm{d}_{\mathrm{TW}}$ and $\mathrm{d}_{2}$ :

$$
\begin{align*}
& R_{a}=R+\frac{\gamma}{2}\left(d_{T W}^{2}-d_{2}^{2}\right)  \tag{2-40}\\
& R_{a_{+}}=R_{+}+\frac{\gamma}{2}\left(d_{T W}^{2}-d_{2}^{2}\right)  \tag{2-41}\\
& R_{a_{-}}=R_{-}+\frac{\gamma}{2}\left(d_{T W}^{2}-d_{2}^{2}\right) \tag{2-42}
\end{align*}
$$

where $R_{a}, R_{a_{+}}$, and $R_{a_{-}}$are the adjusted average unit resultant force, the adjusted maximum instantaneous unit resultant force, and the adjusted minimum unit resultant force, respectively. The distance above the stilling basin apron, $Y$, to the resultant of the unit force acting on the basin wall is determined by the use of Plate $2-5$, which defines the relationship between $\mathrm{Y} / \mathrm{d}_{\mathrm{TW}}$ and $\mathrm{X} / \mathrm{L}_{\mathrm{b}}$. Appendix E includes an example problem illustrating the recommended application for estimating the magnitude and locations of the resultant dynamic forces acting on a stilling basin sidewall.

## Section VI. Cavitation

2-15. General. Cavitation is defined as the formation of a gas and water vapor phase within a liquid resulting from excessively low localized pressures. When associated with the design of spillways, cavitation is important because the vaporization occurs on or near the nonfluid boundary (spillway surface) resulting from localized boundary shape conditions. Cavitation damage results when the gas and water vapor-filled void is swept from the low-pressure zone into an adjacent higher pressure zone which will not support cavitation, causing the void to collapse. The collapse of the void results in extremely high pressures, and when they occur at or near the nonfluid boundary, will form a small pit. When given sufficient time, numerous void collapses result in numerous small pits which eventually overlap, leading to larger holes. This damage, in turn, aggravates the localized low-pressure zone, thereby creating a self-breeding continuation of the damage. The existence and extent of cavitation damage are dependent upon the boundary shape, the damage resistance characteristics of the boundary, the flow velocity, the flow depth, the elevation of the structure above sea level, and the length of time the cavitation occurs. Cavitation damage can be detected at one or more locations in essentially all high-velocity flow structures; however, and fortunately, most damage is minor and results from cavitation conditions at or very near the incipient damage level. When incipient levels are exceeded,
serious damage will occur. At Libby Dam, a construction-related misalignment of the parabolic-shaped invert of the open channel flow sluices resulted in cavitation damage that removed concrete and reinforcing steel throughout an area 54 feet in length, up to 7 feet wide, and up to 2.5 feet deep on both the floor and the right wall (item 47). At Hoover, Yellowtail, and Glen Canyon Dams, severe cavitation damage occurred in tunnel spillways near the tangent point of the vertical curve which decreases the slope of the spillway. The spillways at these dams are tunnel-type structures which were operating at open channel flow conditions with average flow velocities in excess of $100 \mathrm{ft} / \mathrm{sec}$ when the damage occurred. Similar flow conditions can exist on a spillway chute. Damage to concrete surfaces can occur at velocities significantly less than $100 \mathrm{ft} / \mathrm{sec}$ provided the correct combination of cavitation parameters exists. As a rule of thumb, cavitation should be investigated whenever flow velocities are in excess of $35 \mathrm{ft} / \mathrm{sec}$.

2-16. Cavitation Damage. The damage potential resulting from cavitation is dependent upon the boundary shape, the damage resistance characteristics of the boundary, the flow velocity and depth, the elevation of the structure above mean sea level, and the length of time cavitation occurs. The boundary shape, velocity, and elevation are related by the cavitation index, $\sigma$, which is derived from the energy equation:

$$
\begin{equation*}
\frac{v_{0}^{2}}{2 g}+\frac{P_{0}}{\gamma}+z_{0}=\frac{v_{1}^{2}}{2 g}+\frac{P_{1}}{\gamma}+z_{1} \tag{2-43}
\end{equation*}
$$

where P is the absolute pressure, $\mathrm{lb} / \mathrm{ft}^{2}$. With $\mathrm{H}=\mathrm{P} / \gamma$ the comparable equation is

$$
\begin{equation*}
\frac{\mathrm{H}_{1}-\mathrm{H}_{0}}{\frac{\mathrm{v}_{0}^{2}}{2 \mathrm{~g}}}=1-\left(\frac{\mathrm{v}_{1}}{\mathrm{v}_{0}}\right)^{2}+\frac{\mathrm{z}_{0}-\mathrm{z}_{1}}{\frac{\mathrm{v}_{0}^{2}}{2 \mathrm{~g}}} \tag{2-44}
\end{equation*}
$$

For high velocities the elevation term in equation 2-44 can be ignored. The dimensionless parameter on the left side of the equation is known as the pressure parameter. Replacing $\mathrm{H}_{1}$ with the absolute head required for vaporization of water at the elevation of the structure above sea level and rearranging terms in order that $\sigma$ will be positive, the flow cavitation index is

$$
\begin{equation*}
\sigma=\frac{H_{0}-H_{V}}{\frac{v_{0}^{2}}{2 g}} \tag{2-45}
\end{equation*}
$$

where

$$
\begin{aligned}
& H_{0}=\text { reference head, feet } \\
& H_{V}=\text { vapor head of water, feet }
\end{aligned}
$$

Various investigators have experimentally determined the o-incipient
cavitation relationship for a number of specific boundary shapes. These experimentally derived data have been reduced to curves describing the incipient cavitation level for specific boundary shapes (Plates 2-6 through 2-9). Cavitation damage can be expected if a specific u-boundary shape relationship can be plotted on or to the right side of the curve. When this condition is evident, a design change must be made that either increases the $\sigma$ value, smoothes the boundary shape, or both. As $\sigma$ decreases below the incipient cavitation level, the cavitation damage potential increases very rapidly. Investigations (item 14) have found that the cavitation energy absorbed by the nonfluid boundary increases by the eleventh power of the velocity.

2-17. Cavitation Damage Prevention. Cavitation-induced damage can be prevented by a number of methods. As shown in paragraph 2-16, damage can be prevented by increasing the cavitation index and/or by providing a smoother boundary shape. However, changes of this type are usually impractical or at best difficult to accomplish due to the physical limitations imposed by the required design and construction practices. Changing the damage resistance characteristics of the boundary will inhibit the damage produced over-a finite period of time. As an example, structural concrete exposed to cavitation resulting from a flow velocity of $98 \mathrm{ft} / \mathrm{sec}$ for 3 hours resulted in a hole 0.5 inch deep. Under the same conditions with polymerized concrete, the same size hole resulted after 6,000 hours. The use of hardened boundaries also has physical limitations, and results only in resisting the cavitation forces for a given period of time. A relatively new and very effective method of preventing cavitation-induced damage is to disperse a quantity of air along the flow boundary. This is achieved by passing the water over an aeration slot specially designed to entrain air along the boundary. This method has been used to prevent cavitation damage at various high-velocity flow facilities including Libby Dam sluices (item 46). Prototype tests of boundary pressures were obtained at identical locations and hydraulic conditions for pre- and post-boundary aeration. These tests showed that aeration of the boundary resulted in raising instantaneous pressures that were very close to absolute zero to pressures near atmospheric. Data collected from these tests were used to derive the cavitation index. The post-boundary aeration cavitation index showed an average increase of about 50 percent above the preaeration condition. The aeration slot geometry and location must be designed for the specific application. Some design guidance has been developed (item 13) to assist in aeration slot design and should be used to develop an initial design. Until significantly more experience, data, and design guidance are developed, model studies of aeration slot design are recommended.

## CHAPTER 3

## SPILLWAY CREST

Section I. Introduction

## 3-1. General.

a. All spillways discussed in this manual require a spillway crest design. The crest and/or gates located near the crest provide the flow control through the spillway system. The capacity of the spillway is dependent upon the crest shape, crest length, and the hydraulic head. The hydraulic head is modified by approach conditions, pier and/or abutment effects, and submergence. The basic purpose of a spillway is to convey large floods through a project without incurring unacceptable damage either upstream or downstream from the spillway. The spillway design is accomplished in a manner that will minimize cost subject to providing:
(1) Sufficient crest length to convey the design discharge.
(2) Acceptable minimum pressures acting on the crest boundary.
(3) Acceptable maximum energy head on the spillway crest.
(4) Acceptable velocities and flow characteristics through the spillway system.
(5) Acceptable environmental and aesthetic conditions.
b. Engineering-economic investigations will usually show that a narrow spillway with high unit discharge is more economical than a wide spillway with moderate unit discharge. Thus, the most economic design will produce a spillway that includes a large energy head on the crest, a moderate design head, and a large unit discharge. Higher head spillways can create excessive abutment and pier contractions, cause energy dissipation problems, increase the possibilities of cavitation or pulsating nappe on the spillway crest, and create poor flow characteristics through the spillway system. The demand placed on the designer for economical designs requires the use of high head, high-efficiency spillways which, in turn, requires a sound design methodology. The objective of this chapter is to assist in providing this methodology.

## Section II. Crest Characteristics

3-2. General. To provide a high-efficiency spillway and yet produce a safe, low-maintenance structure, the crest shape must provide a high discharge coefficient and fairly uniform and predictable pressures on the crest boundary. These constraints can best be met if the shape of the overflow spillway closely approximates that of a fully ventilated nappe of water flowing over a sharp-crested weir. The shape of the nappe is affected by the relative head on the weir, the approach depth and velocity, and the upstream slope of the weir. Experimental data gathered throughout a suitable range of these variables have led to the development of a spillway design methodology. The
earliest attempts at fitting equations to lower nappe surfaces utilized the data of Bazin (item 6). Data developed by the US Bureau of Reclamation (USBR) (item 76) have served as a basis for most CE crest design procedures. Recent spillway investigations at WES (items 28, 32, and 33) have added considerably to the USBR data.

## 3-3. Crest Shape.

a. The complete shape of the lower nappe, which is also the spillway crest surface, is described by separating it into two quadrants upstream and downstream from the high point (apex) of the lower nappe. The apex is normally defined as the crest axis. The spillway crest shape is proportionally based on the design head $\mathrm{H}_{\mathrm{d}}$ (see Chapter 2, Section II, for detailed definition of symbols used. The energy head H can be greater than, equal to, or less than $\mathrm{H}_{\mathrm{d}}$. The equation for the do\&stream quadrant of the
crest for all spillways can be expressed as

$$
\begin{equation*}
X^{n}=K H_{d}^{n-1} Y \tag{3-1}
\end{equation*}
$$

where
$\mathrm{x}=$ horizontal coordinate positive to the right, feet
$\mathrm{n}=$ variable, however usually set equal to 1.85
$\mathrm{K}=$ variable dependent upon $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$
Y - vertical coordinate positive downward, feet
Equation 3-1 can be used to define the downstream crest shape for any $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ ratio by a systematic variation of K from 2.0 for a deep approach to 2.2 for a very shallow approach. See Plates 3-1 and 3-2.
b. Difficulties existed when a single equation was fit to the upstream quadrant. The efficiency of the spillway is highly dependent on the curvature of the crest immediately upstream of the crest axis (items 32 and 51). A sudden change in curvature or a discontinuity not only disrupts the boundary layer but can also lead to flow separation and cavitation. Murphy (item 33) reported a three percent increase in the discharge coefficient when a small discontinuity between the upstream face and upstream quadrant was removed.
c. A general design procedure was advanced by Murphy (item 33) by which a sloping face spillway and a vertical face spillway can be designed in the same manner. For the upstream quadrant Murphy found that, by systematically varying the axes of an ellipse with depth of approach, he could closely approximate the lower nappe surfaces generated by USBR. Furthermore, any sloping upstream face could be used with little loss of accuracy if the slope became tangent to the ellipse calculated for a vertical upstream face.
d. The equation of the upstream elliptical shape is expressed as

$$
\begin{equation*}
\frac{X^{2}}{A^{2}}+\frac{(B-Y)^{2}}{B^{2}}=1 \tag{3-2}
\end{equation*}
$$

where
$\mathrm{x}=$ horizontal coordinate origin at crest axis positive to the right
A = one-half horizontal axis of ellipse, feet
B = one-half vertical axis of ellipse, feet
$\mathrm{Y}=$ vertical coordinate origin at the crest axis positive downward
These three parameters ( A , B , and K ) then fully define the crest shape. Their variation with relative approach depth is given in Plate 3-2. This plate also includes a definition sketch.

3-4. Crest Discharge Coefficient. Discharge over a spillway crest is classified as either free flow or submerged flow. Free flow implies that the value of the discharge coefficient is not influenced by conditions downstream from the crest. Submerged flow occurs either when the tailwater is sufficiently high that a reduction in the discharge coefficient occurs, or when there is a change in the crest profile so close to the crest axis that the full benefits of the crest shape cannot be obtained. Flow over a spillway is governed by the relationship

$$
\begin{equation*}
Q=C L e_{e}^{1.5} \tag{3-3}
\end{equation*}
$$

where Q is the rate of discharge and C is the discharge coefficient which is a measure of the efficiency of the spillway system. The discharge coefficient is a variable dependent upon generalized and site-specific factors. The factors which have been accounted for in generalized laboratory studies are the effect of relative approach depth $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$, the slope of the upstream face, the relative head on the crest $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}$, crest submergence, and selected crest and abutment shapes. Site-specific factors such as flow angularity resulting from complex approach flow geometry or unusually shaped piers, for example, can be significant and must be investigated by a site-specific model study.
a. Free Discharge. Laboratory studies accomplished at WES (items 28 and 33) have defined spillway coefficients for free flow over a wide range of the following generalized factors: upstream slope, $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$, and $\mathrm{H} / \mathrm{H}_{\mathrm{d}}$. Discharge coefficients reflecting these factors are given in Plates $3-3$ and 3-4. Due to possible scale effects, discharges were not measured below $H_{e} / H_{d} =0.4$. However, prototype experience has shown that spillway crests at very low heads exhibit the same discharge characteristics as a broad-crested weir. Therefore, for extrapolation purposes, the discharge coefficient should be equal to 3.08 as $H_{e} / H_{d}$ approaches zero. As the $P / H_{d}$ values decrease, and particularly for higher values of $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}$, control of the flow begins to shift upstream, efficiency is lost, the discharge coefficient decreases, and the value of $C$ again approaches that of a broad-crested weir (in this case a free overfall). Also to be noted is the characteristic increase in discharge coefficient for heads greater than design head. This is the concept of underdesigning the spillway crest to obtain greater efficiency. Underdesigning does not result in increased discharge coefficients with $P / H_{d}<0.5$. The limitations of underdesigning the crest are dependent on the extent of negative pressure developed on the spillway crest. See Section IV, Crest Pressures, of this chapter.
b. Submerged Discharge. Submerged flow resulting from either excessive tailwater or changes in the crest profile will effectively reduce the free crest discharge coefficient. The reduction in the coefficient is dependent upon the degree of submergence. Due to the variance in the discharge coefficient, the effect of submergence cannot be described by a single relationship over the full range of the dependent variable. HDC 111-4 provides a discussion on tailwater submergency and provides a chart which defines a percent decrease in the unsubmerged crest coefficient for a full range of submergence. This chart is reproduced as Plate 3-5 for convenience. The curves shown on Plate $3-5$ were based on three different test conditions: the approach and apron floors at the same constant elevation; both floors at the same elevation but varied with respect to the crest elevation; and the approach floor elevation held constant and the apron elevation varied. The percent decrease in the discharge coefficient was based on the unsubmerged discharge coefficient for each condition tested. EM 1110-2-1605 provides additional information on the effect of tailwater submergence on broad-crested spillways that are often used in conjunction with navigation dams. The reduction in the discharge coefficient resulting from crest geometry submergence is not as well defined as that for tailwater submergence. Abecasis (item 1) has accomplished some experiments that show when the chute tangent intersects the crest curve close to crest, a reduction in the discharge coefficient of two to eight percent will occur. The amount of reduction is dependent upon the location of the point of tangent intersection and the crest. When designs of this type are used and the discharge coefficient is critical, model studies will be necessary to verify the design.

Section III. Spillway Piers, Abutments, and Approach
3-5. General. Crest piers, abutments, and approach configurations of a variety of shapes and sizes have been used in conjunction with spillways. All of the variations in design were apparently used for good reasons. Not all of the designs have produced the intended results. Improper designs have led to cavitation damage, drastic reduction in the discharge capacity, unacceptable waves in the spillway chute, and harmonic surges in the spillway bays upstream from the gates. Maintaining the high efficiency of a spillway requires careful design of the spillway crest, the approach configuration, and the piers and abutments. For this reason, when design considerations require departure from established design data, model studies of the spillway system should be accomplished.

3-6. Contraction Coefficients. Crest piers and abutments effectively reduce the rate of discharge over the crest. The reduction in discharge is determined by the use of a contraction coefficient which, when applied in equation 2-2, defines the effective length of spillway crest. Conversely, additional crest length must be provided to offset the crest length reduction resulting from piers and abutments. Pier contraction coefficients have been determined from generalized model studies. Plate $3-6$ shows plots of these contraction coefficients for five different pier nose shapes having the pier nose located in the same vertical plane as the spillway face and with $\mathrm{P} / \mathrm{H}_{\mathrm{A}}>1$. Plate 3-7 shows a plot of the contraction coefficient for a truncated elliptical pier nose that includes a bulkhead slot. This pier nose shape has been used on a number of the Columbia and Snake River projects. The
contraction coefficients for the type 2 pier nose with piers extending upstream from the spillway face and $P / H>1$ are shown in Plate 3-8. The contraction coefficients for $P / H_{d}<1$ for the type 2 pier nose are shown in
Plate 3-9. The contraction coefficients for the type 3 pier with an elliptical-shaped upstream crest with vertical or $1: 1$ upstream spillway slope and various $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ ratios are shown in Plate 3-10. The contraction coefficients for the variety of shapes and conditions show significant variation throughout a range of -0.075 to 0.10 , thus the reason for careful consideration of the pier shape. Although some of these pier contraction coefficients show an increase in the efficiency of the spillway, it may be at the expense of lower pressures on the crest or undesirable flow conditions in the chute. As an example, the type 4 pier shown in Plate $3-6$ provides increased efficiency throughout a wide range of $H_{e} / H_{d}$; however, the flow conditions in the chute may be undesirable. Abutment contraction coefficients are not as available, as abutments are somewhat more site-specific. Plates 3-11 and 3-12 provide some basic information pertinent to abutments with adjacent concrete or embankment sections. (See paragraph 3-8 for additional information on abutment effects.)

3-7. Spillway Bay Surge. Surging of the water surface upstream from tainter gates has been observed during model studies of gated spillway crests on both high and low spillway crest. Model measurements indicate that water surface fluctuations as great as 10 feet with periods less than 10 seconds would occur in alternate bays of the prototype for certain combinations of gate bay width, $\mathrm{w}_{\mathrm{b}}$; gate opening, $\mathrm{G}_{\mathrm{O}}$; pier length, $\mathrm{P}_{\mathrm{L}}$ defined as the distance from the upstream-most point of the gate face to the pier nose; and head on the crest, ${ }_{\mathbf{r}}$. Model studies have shown that decreasing $P_{L}$, increasing $W_{b}$, or both, will effectively eliminate periodic surge. Excessive surging can be prevented by applying the following guidelines on spillway pier and gate bay design:
a. Low head spillways, $\mathrm{P} / \mathrm{H}_{\mathrm{d}}<1$

$$
\mathrm{W}_{\mathrm{b}} \geqq 1.1 \mathrm{H}_{\mathrm{c}} \text { for } \mathrm{P}_{\mathrm{L}}<0.3 \mathrm{~W}_{\mathrm{b}}
$$

or

$$
\mathrm{W}_{\mathrm{b}} \geqq 1.25 \mathrm{H}_{\mathrm{c}} \text { for } 0.3 \mathrm{~W}_{\mathrm{b}}<\mathrm{P}_{\mathrm{L}}<0.4 \mathrm{~W}_{\mathrm{b}}
$$

b. High head spillways, $P / H_{d}>1$

$$
\mathrm{W}_{\mathrm{b}} \geqq 0.8 \mathrm{H}_{\mathrm{c}} \text { for } \mathrm{P}_{\mathrm{L}}<0.3 \mathrm{~W}_{\mathrm{b}}
$$

or

$$
\mathrm{W}_{\mathrm{b}} \geqq 1.2 \mathrm{H}_{\mathrm{c}} \text { for } 0.3<\mathrm{P}_{\mathrm{L}}<0.4 \mathrm{~W}_{\mathrm{b}}
$$

where $H_{C}$ is the maximum head on the crest where the gate controls the discharge. The maximum gate opening for which tainter gates will control the discharge should be taken as 0.625 times the head on the weir crest. By utilizing the spillway discharge curves for various gate openings, the maximum head on the weir crest for which the gates will control the discharge can be
determined. These guidelines apply to all gated spillways regardless of the gate size. Due to the limited model tests used to develop the guidelines, model tests should be considered on those spillways which would operate with $\mathrm{G}_{0}>20$ feet and $\mathrm{H}_{\mathrm{e}}>40$ feet. Conditions may dictate a design that is within the above limits, such as the increase in dam height which occurred at Chief Joseph Dam. At this project the model studies showed approximately five feet of surge alternating across the 19-bay spillway. Changing the dimensions of $\mathrm{W}_{\mathrm{b}}$ or $\mathrm{P}_{\mathrm{L}}$ was constrained by the existing structure so model studies were undertaken to evaluate surge suppressor designs. A simple design of two triangular concrete protrusions on the side of the pier upstream from the gate reduced the surge to well within acceptable limits without reducing the discharge characteristics of the spillway. See item 56 for detailed information.

3-8. Spillway Approach. Spillway approach configuration will influence the abutment contraction coefficient, the nappe profile, and possibly the flow characteristics throughout the spillway chute and stilling basin. There are three general configurations for the spillway approach, each of which requires a different treatment at the abutments in order to provide acceptable spillway characteristics.
a. Deep Approach. First, there is the high spillway where approach velocities are negligible. This condition usually exists at a spillway in the main river channel flanked by concrete nonoverflow sections. The $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ ratio for a deep approach spillway is defined as being greater than 1.0. The shape of the abutment adjoining concrete sections of a high head dam is a major factor influencing the abutment contraction coefficient. For this type of structure, the extension of the abutment upstream from the dam face to develop a larger abutment radius has provided improved flow characteristics in the end bays of the spillway (item 41). The abutment contraction coefficient curve shown in Plate 3-11 is applicable to this type of approach condition.
b. Shallow Approach. Second, there is the broad but relatively shallow approach that results in strong lateral currents at the abutments. This condition frequently is found at spillways in the river valley flanked by embankment sections. The $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ ratio for the shallow approach spillway is defined as being equal to or less than 1.0. When a spillway includes adjacent embankment sections, and particularly where approach velocities are appreciable, the configuration of the abutments and adjoining topography, the depth of approach flow, and the angularity of approach flow have significant influence on abutment contraction coefficients and flow characteristics. The embankment should not be carried at full height to the spillway training walls. Embankment wraparounds with concrete nonoverflow sections joining the top of the embankment to the spillway training walls should be considered. Abutment pier noses should not extend upstream of the face of the nonoverflow sections as this configuration has been noted to cause surging at the abutments. Rock dikes extending into the reservoir have been used to improve flow conditions at the abutments (item 66); however, optimum configurations are essential and can be developed only in a model study. An abutment contraction coefficient curve recommended for approach depths that are at least one-half of the design head and approach flow relatively perpendicular to the spillway are provided in Plate 3-12. Abutment contraction coefficients as large as 0.75 have been
measured in model studies with very shallow approach ( $\mathrm{P} / \mathrm{H}_{\mathrm{d}}<0.2$ ) and a curved approach channel (item 69).
c. Confined Approach. The third configuration results when the spillway is remote from the main dam and an excavated approach channel is required. In this type of approach, velocities may be high and flow distribution may be unequal but there will not be strong lateral currents at the abutments. When conditions require an excavated approach channel to the spillway, friction losses in the channel should be considered in determination of spillway capacity. Guidance for computing friction losses is given in Chapter 2. For confined channels the abutment contraction coefficient curve shown in Plate 3-11 may be used to account for abutment effects.

## Section IV. Spillway Crest Pressures

3-9. General. Free discharge over a spillway crest designed to the shape discussed in paragraph 3-3 will develop pressures on the concrete boundary somewhat inversely proportional to the $H_{e} / H_{d}$ ratio. When $H_{e} / H_{d}$ is nearly one, the pressures on the crest are essentially atmospheric. As $H_{e} / H_{d}$ increases, crest pressures drop below atmospheric. These negative pressures are the reason for the increase in the discharge coefficient over that of a ventilated sharp-crested weir. A reasonable approximation of the crest pressures will provide the data necessary for structural stability analysis for certain design cases. Crest pressure calculations will also provide the hydraulic design guidance on the limiting pressures that crest underdesigning yields prior to reaching pressures where cavitation damage occurs. Previous recommendations (item 77) have stated that $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}$ should not exceed 1.33 when underdesigning a spillway crest. Bauer and Beck ${ }^{\text {d }}$ (item 5) and Abecasis (item 2) have shown that the actual minimum pressure fluctuation level in relation to local atmospheric pressure is what leads to cavitation. Vacuum tank observations by Abecasis (item l) indicated that cavitation on the crest would be incipient at an average pressure of about -25 feet. Fluctuations and duration of actual pressures at or near absolute, not the average pressure on the crest boundary, are the cause of cavitation damage. A spillway crest should be designed so that the maximum expected head will result in average pressures on the crest no lower than - 15 feet of water at sea level and 40 -degree Fahrenheit temperature. The -15 feet of water must be adjusted to account for elevation and water temperature at the spillway crest site. HDC 000-2 and 001-2 will provide data to assist in this adjustment. For spillways with and without piers, Plates $3-13$ and $3-14$, respectively, show a relationship between $H_{e}$ and $H_{d}$ defining the maximum limit of underdesign allowed based on the recommended minimum crest pressure of -15 feet of water. The curves for -25 feet and -20 feet of water are also shown on these plates for comparison.

3-10. Controlled and Uncontrolled Crests. A controlled crest is one that includes gates which are used to control the flow; the uncontrolled crest is one unencumbered by gates. Pressures on controlled and uncontrolled crests with vertical $1: 1$ upstream sloped faces with $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ values of $0.25,0.5$, and 1.0 were investigated at WES (item 28). At $\mathrm{P} / \mathrm{H}_{\mathrm{d}}=0.25$, pressures were measured for $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}=0.5$ and 1.0 only. Use of an underdesigned crest with a
$\mathrm{P} / \mathrm{H}_{\mathrm{d}} \quad$ value as low as 0.25 does not result in a significant increase in the discharge coefficient above $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}=1.0$. WES investigations included two piers placed on a model crest. The pier nose used for all crests was the type 3 shown on Plate 3-6. The pier nose was located in the same plane as the upstream face for the vertical spillway. For the $1 \mathrm{~V}: 1 \mathrm{H}$ upstream slope, the pier nose location was determined by maintaining the same distance from pier nose to crest axis as used in the vertical upstream faced crest. See item 28 for detailed information on crest pressure distribution for various $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$
ratio spillways, with and without a sloping upstream face, and various $\mathrm{H}_{0} / \mathrm{H}$ ratios. For spillways that include piers, the minimum pressure along the pier limits the amount of underdesigning permissible. When a crest with piers is designed for negative pressures, the piers must be extended downstream beyond the negative pressure zone in order to prevent aeration of the nappe, nappe separation or undulation, and loss of the underdesign efficiency advantage. For preliminary design purposes, the approximate range of the dimensionless horizontal distance from the crest axis ( $\mathrm{X} / \mathrm{H}_{\mathrm{d}}$ ) where pressures were found to return to positive, are as follows:

| $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}$ | $\mathrm{X} / \mathrm{H}_{\mathrm{d}}$ |
| :--- | ---: |
| 1.17 | $0.1-0.4$ |
| 1.33 | $0.7-0.9$ |
| 1.5 | $1.1-1.5$ |

## Section V. Upper Nappe Profile

3-11. General. The upper nappe profile or the water surface profile for free flow over a spillway crest with or without piers is of acute interest in the design of sidewalls adjacent to the spillway crest, equipment bridges over the spillway crest, and spillway gate trunnion location. The nappe profile unencumbered by crest piers is somewhat different from one with piers. The upper nappe profile will also be modified by the direction of the approach flow with respect to the crest axis. Procedures to determine nappe profiles have been derived from experimental work based on specific conditions involving $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ and $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}$ ratios, spillways with and without piers, and approach flow perpendicular to the crest axis. These procedures provide a sound basis for design of nappe profile-related features. When hydraulic conditions vary somewhat from the experimental conditions, or the upper nappe profile is critical to the design, model studies to accurately determine the profile are recommended.

3-12. Nappe Profile. The design procedure used to determine the upper nappe profile is based on generalized experimental data. Upper nappe profile data for two spillway conditions are presented. The first is for high spillways with negligible approach velocities as discussed in paragraph 3-8a. The second condition is for low spillways with appreciable approach velocities as discussed in paragraphs $3-8 \mathrm{~b}$ and c.
a. High Spillways. Plate 3-15 shows generalized data in the form of dimensionless coordinates of the upper nappe profile in terms of the design head for $H_{e} / H_{d}$ ratios of $0.50,1.00$ and 1.33 without the influence of crest
piers. Plates $3-16$ and $3-17$ show the dimensionless coordinates for the same conditions with the influence of crest piers.
b. Low Spillways. Plates $3-18$ through $3-20$ show generalized data in the form of dimensionless coordinates of the upper nappe profile along the center line and along the edge of a crest pier in terms of the design head. These data are presented for $\mathrm{H}_{\mathrm{e}} / \mathrm{H}_{\mathrm{d}}$ ratios of 0.05 , 1.0 , and 1.5 for $\mathrm{P} / \mathrm{H}_{\mathrm{d}}$ ratios of $1.0,0.50$, and 0.25 .

## CHAPTER 4

SPILLWAY CHUTE<br>Section I. Basic Considerations

## 4-1. General.

a. The chute is that portion of the spillway which connects the crest curve to the terminal structure. The term chute when used in conjunction with a spillway implies that the velocity is supercritical; thus the Froude number is greater than one. When the spillway is an integral part of a concrete gravity monolith, the chute is usually very steep. Chutes as steep as 1.0 vertical on 0.7 horizontal are not uncommon. The steepness thus minimizes the chute length. Chutes used in conjunction with embankment dams often must be long with a slope slightly steeper than the critical slope. This long, prominent structure is termed a chute spillway. The designs for long spillway chutes and steep chutes on concrete dam monoliths involve many of the same geometric and hydraulic considerations. Due to the extreme slope and short length of a steep chute, many of the hydraulic characteristics that become prominent in spillway chutes have insufficient time to develop prior to reaching the terminal structure.
b. Hydraulic characteristics that must be considered in the design of a chute are the velocity and depth of flow, air entrainment of the flow, pier and abutment waves, floor and wall pressures, cavitation indices, superelevation of the flow surface at curves, and standing waves due to the geometry of the chute. Obtaining acceptable hydraulic characteristics is dependent upon developing proper geometric conditions that include chute floor slope changes, horizontal alignment changes (curves), and sidewall convergence. This chapter presents data to assist the designer in obtaining an acceptable chute design. A model study is recommended to confirm any design that involves complex geometric considerations and/or large discharges and velocities.

4-2. Sidewalls. The height of a chute sidewall should be designed to contain the flow of the spillway design flood. The flow profile of the spillway design flood can be computed using the methods discussed in Chapters 2 and 3. The computed profile may require adjustment to account for the effects of pier end waves, slug flow or roll waves, and air entrainment. Sidewall freeboard is added above the adjusted profile; as a mimimum, two feet of freeboard is recommended. A conservative, empirical freeboard criterion recommended by USBR (item 77) is as follows:

$$
\begin{equation*}
\text { Freeboard }=2.0+0.025 \mathrm{Vd}^{1 / 3} \tag{4-1}
\end{equation*}
$$

where V and d are the mean velocity and mean depth in feet, respectively, in the chute reach under consideration.
a. Pier End Waves. Supercritical flow expands after flowing past the downstream end of a spillway pier. The expanding flow from each side of a pier will intersect and form a disturbance which is termed a pier end wave. These waves travel laterally as they move downstream. Multiple piers will
cause the formation of a diamond pattern of waves within the chute. The impact at the intersection of the flow can be so severe that a rooster taillike plume of water will form. A large plume was noted during the Libby Dam model studies (item 58) and was of sufficient concern to require the design of a streamlined pier end to eliminate it. Referring to Figure 4-1, the location on the sidewall where the wave from the first pier intersects the wall can be estimated by the equation:

$$
\begin{equation*}
z=\frac{x}{\tan \left[\sin ^{-1} \frac{(g y)^{1 / 2}}{V_{s}}\right]} \tag{4-2}
\end{equation*}
$$

where

```
z = distance from downstream end of pier to wave and wall intersection,
feet
x = distance from first pier to the wall
Y = depth of flow
vs = surface velocity of flow, ft/sec
```

Equation 4-2 is qualified by the following conditions: The wave height at the end of the pier should be relatively small compared to the depth of flow and the velocity should be taken as the surface velocity which can be approximated by twice the average velocity. Flow disturbances from pier ends should be contained within the chute. The magnitude of the pier end wave height is difficult to determine without a model study. For a design without the benefit of a model study, an additional 25 percent of the depth of flow should be included in the sidewall height to account for pier end waves.

![](https://cdn.mathpix.com/cropped/59f740da-7b8c-4d04-aa98-940afdd24247-27.jpg?height=662&width=1190&top_left_y=1547&top_left_x=405)
Figure 4-1. Pier end waves downstream of spillway piers

b. Slug Flow. Slug flow or roll waves may form in long chutes and should be considered in sidewall height determinations. Observations of
existing chutes indicate that these waves can reach a maximum height of approximately five percent above the mean depth. Knowledge of this type of instability is limited; therefore, further study of the phenomenon in the prototype is suggested when the condition is known to exist.
c. Air Entrainment. When air is entrained in supercritical flow, there is an increase in volume, sometimes called bulking, which will result in a greater depth of flow. This effect is noticeable in flow with Froude numbers greater than 1.5. Air entrainment must be considered in the design of chute sidewalls, bridges, or other features dependent upon the water surface profile. EM 1110-2-1601, provides the designer with a basis for increasing the flow depth due to bulking. Plate 4-1, reprinted from EM 1110-2-1601, defines the ratio of flow depth with and without air to the Froude number.

## 4-3. Convergent and Divergent Chutes.

a. Convergent Chute. Laboratory and field evaluation by Cox (item 11) has resulted in design criteria and guidance applicable to spillway chutes having convergence affected by horizontal curves of long radii. Optimum chute flow conditions prevail when the following criteria are satisfied, and a design that meets these criteria should perform adequately. The design flow Froude number should gradually increase continuously throughout the convergence. Optimum flow conditions occur with a crest formed by the break in invert grade or by a low sill formed as an integral part of the chute slope. However, for structural or economic reasons, the use of a spillway crest with a toe curve may be required, and less favorable flow conditions in the chute will result. Curving the chute crest in the form of a horizontal arc is noted not to appreciably affect flow conditions in the converging chute. Straightlined converging walls in the vicinity of the crest are desirable to effect the initial convergence of the flow. Parallel walls in this vicinity should be avoided. The straight-lined walls should extend upstream beyond the crest into the subcritical flow area. These straight-lined walls should not extend downstream beyond the point where the Froude number exceeds 1.5. Straightlined walls should have a convergence factor of $\Delta \mathrm{L} / \Delta \mathrm{W} \geqq 5.0$, where $\Delta \mathrm{L}$ is the change in center-line length and $\Delta \mathrm{W}$ is the change in width for centerline length increment $\Delta \mathrm{L}$. Chute walls curved horizontally with long radii should be used when the local Froude number exceeds 1.5. These curved walls should be designed so that the convergence factor down the chute complies with the relationship:

$$
\begin{equation*}
\frac{\Sigma \Delta L}{\Sigma \Delta W} \geqq \frac{1}{0.382-0.116 F} \tag{4-3}
\end{equation*}
$$

where
> $\Sigma \Delta L=$ center-line station distance from the intersection of the crest axis and sidewall
> $\Sigma \Delta W=$ accumulated sidewall convergence beginning at the intersection of the sidewall with the spillway crest
> $F=$ local design flow Froude number at the station $\sum \Delta L$ for the design flow

The minimum recommended design value of $\Sigma \Delta L / \Sigma \Delta W$ is 5.0 . When the Froude number exceeds approximately 3.25 , parallel walls are considered necessary. Vertical chute walls in the converging section are preferable to sloping walls due to the adverse effects sloping walls have on the local Froude number. When sloping walls are used, these walls should be sloped normal to the chute invert slope rather than normal to the horizontal. Hydraulic model studies are usually conducted to verify the design of a convergent chute spillway.
b. Divergent Chute. When site or economic conditions indicate that a short crest length and a widened terminal structure are desirable, diverging chute walls will be required. Model studies conducted by USBR (item 77) provide examples of designs required for chute type of spillways. USBR uses a straight crest and recommends a maximum sidewall flare angle, $\alpha$, of

$$
\begin{equation*}
\tan \alpha=\frac{1}{3 \mathrm{~F}_{1}} \tag{4-4}
\end{equation*}
$$

where $F_{1}$ is the average Froude number of the flow at the location in the reach where the flare originates.

## Section II. Chute Spillways

4-4. General. Chute spillways are normally designed to minimize excavation. This is accomplished by setting the invert profile to approximate the profile of the natural ground. Profile changes in both the vertical and horizontal alignment may be involved when obtaining a minimum excavation design. The chute spillway is essentially a high-velocity channel, the design of which is discussed in detail in EM 1110-2-1601. The primary concerns for the design of the chute spillway are to provide an invert slope that will ensure supercritical flow throughout the chute for all discharges, and to provide a design of piers, abutments, and sidewall transitions and bends that will minimize wave disturbances.

4-5. Invert and Water Surface Profile. Flow characteristics near critical depth are unstable, and excessive wave action or undulations of the water surface can occur. To avoid these instabilities, supercritical flow depth less than 0.9 of the critical depth or a Froude number greater than 1.13 is necessary. Computations of depth, velocity, and Froude number should consider the boundary layer development over the crest and downstream to the critical point where fully turbulent flow is developed. The remainder of the chute should be analyzed by an open channel flow method for determining energy loss for fully turbulent flow, A relatively large roughness value should be used for the determination of flow stability and water surface profiles. To assess flow stability for all operating conditions, velocity and depth computations for the full range of discharge are suggested. A second analysis of velocity and depth throughout the chute should be undertaken with a relatively small roughness value. The data derived from the second set of analyses are for consideration in the design of the sidewall alignment, sidewall height, and terminal structure design.

4-6. Invert Pressure. Details of the chute floor slabs deserve careful attention in the interest of structural safety and economy. Structural
aspects are discussed in EM 1110-2-2400. In addition to the static uplift pressures from reservoir or tailwater seepage, there are two conditions of hydrodynamic uplift that must be considered. The first consideration is at vertical curves from a steep slope to a flatter slope. Transmission of high boundary pressure through construction joints is possible and should be analyzed in determining uplift on chute slabs. Construction joints should be excluded from locations that include vertical curves from a steep to flatter slope. Theoretical studies and model and prototype data indicate that the pressures resulting from the change in direction of the flow are changing continuously throughout the curve and are influenced by the curve radius, flow velocity, and discharge. Pressures immediately upstream and downstream of the curve are influenced by the invert curvature but reduce rapidly to hydrostatic pressures a short distance away from the curve. These pressures can best be evaluated by means of a flow net or model study. An estimate of the pressures can be obtained by extrapolating the pressure pattern of the curve. Flip bucket pressures discussed in paragraph 7-21 are applicable in this analysis. The second consideration is at vertical curves from a flatter slope to a steeper slope. Negative pressures can occur unless the vertical curve is properly designed. The design of this type of vertical curve is similar to a parabolic drop from a tunnel exit portal to a stilling basin floor. The floor profile should be based on the theoretical equation for a free trajectory:

$$
\begin{equation*}
y=-x \tan \phi-\frac{g x^{2}}{2(1.25 V)^{2} \cos ^{2} \phi} \tag{4-5}
\end{equation*}
$$

where
> x and $\mathrm{y}=$ horizontal and vertical coordinates measured from the beginning of the curve, feet
> $\phi=$ angle between the horizontal and the floor at the beginning of the trajectory, degrees

To prevent flow separation from the floor, the average velocity used should be derived from flow computations using a relatively small roughness value. As a conservative measure this velocity as used in equation $4-5$ has been increased by 25 percent. If site conditions require a design whose trajectory is steeper than that described by equation $4-5$, model studies are recommended; and special construction practices must be specified to obtain surface tolerances and other provisions such as boundary aeration, so that the chute floor surface is compatible with low boundary pressure design.

## CHAPTER 5

## SPECIALIZED SPILLWAYS

## Section I. Side Channel Spillways

5-1. General. The side channel spillway has certain advantages which make it adaptable to topography where the overflow is most economically returned to the original streambed by a deep, narrow channel or by open channel flow through a tunnel. The conventional side channel spillway consists of an overflow weir discharging into a narrow channel in which the direction of flow is approximately parallel to the weir crest. A typical side channel spillway configuration is shown in Plate 5-la. A modification to the conventional side channel spillway crest includes the addition of a short crest length perpendicular to the channel at the upstream end resulting in an L-shaped crest as illustrated in Plate 5-lb. Preliminary design of side channel spillways can be accomplished using the following procedures. In view of the complex nature of the flow, hydraulic model studies are normally required to ensure adequate and economical details for the final design.

5-2. Crest Design. Crest shape design and discharge determination for side channel spillways are accomplished using the procedures discussed in Chapters 2 and 3. Two crest sections have been connected with a circular arc of radius equal to $0.4 \mathrm{H}_{\mathrm{d}}$ to form the L-shaped crest (item 65). The crest length in the discharge equation 2-1 must be corrected for the loss in effective crest length caused by angularity of flow at the junction of the crest sections. Plate 5-2 gives the loss of effective length as a function of head on the crest and design head. These data are considered suitable for preliminary designs even though some variation would occur with various approach depths and junction configurations.

5-3. Channel Design. The theory of flow in the channel of a conventional side channel spillway was developed by Hinds (item 22) and is based on the law of conservation of linear momentum. The assumption is made that the energy of flow over the crest is dissipated by turbulence as it turns and mixes with the side channel flow and that the only force producing longitudinal motion in the side channel results from gravitation. This theory also assumes that the frictional resistance of the channel is sufficiently small enough to be neglected without seriously affecting the accuracy of the computations. The soundness of this theory has been demonstrated by model investigations and prototype experience. Application of the theory to practical design of such a structure was illustrated by McCormmach (item 30). Hydraulic model studies have demonstrated that the energy of flow over the end section of an L-shaped crest helps in moving water down the side channel. Farney and Markus (item 16) developed a generalization of the Hinds theory to permit consideration of nonuniform velocity distribution and corresponding changes in momentum in the channel caused by flow over the L-shaped crest end section. Design of the channel (chute) downstream from the crest sections should follow procedures outlined in Chapter 4.

## Section II. Limited Service Spillways

## 5-4. General.

a. A limited service spillway is designed to operate very infrequently, and with the knowledge that some degree of damage or erosion will occur during operation. The decision to include a limited service spillway must be based on the premise that the risk of future repair and/or reconstruction is acceptable; however, the risk of sudden, uncontrolled, catastrophic release of water is unacceptable. Limited service spillways include structures classified as emergency and/or auxiliary spillways. Normally, limited service spillways are designed to take every possible advantage of local topography. There is no restriction on alignment and consideration should be given to designing unpaved spillways to blend in with the natural environment; however, topography, geology, and hydrology must be carefully evaluated in order to assure that when the facility does operate, the following conditions will be attained.
(1) The spillway flow and/or resulting erosion will not endanger the dam or dam foundation.
(2) The control of the discharge will remain at the predetermined control section and will not be lost due to erosion.
(3) There will be sufficient time available after a spillway use event to evaluate the resultant conditions and perform repairs or reconstruction prior to the next event.
b. Gates are not normally included with a limited service spillway. Topographical and geological conditions must be extremely favorable if this type of design is to be used, because gates permit greater spillway capacity with a smaller structure, thus increasing the unit discharge and consequently the erodibility of the spillway channel.

5-5. Discharge. Infrequent, short-duration operation of a limited service spillway is highly desirable. Projects on watersheds with relatively short duration floods are the best candidates for this type of spillway; however, projects with a large flood control storage volume to runoff ratio and those with outlet works that have capacity to control floods up to the standard project flood should also be considered. The limited service spillway should not be considered for long-duration use, defined as many days or weeks, unless extreme confidence can be placed in the damage and/or erosion resistance of the facility. The determination of discharge through the limited service spillway will involve the hydraulic theory of open channel flow. When low ogee crest discharge characteristics are involved, the procedures discussed in Chapters 2 and 3 are applicable. When backwater or drawdown computations are performed to analyze the discharge capacity and flow profiles, section-tosection velocity changes should be limited to no more than 10 percent of the velocity near the control section and no more than 20 percent at remaining sections. Two sets of discharge computations are suggested. The first set of computations is to assure that the spillway will have an adequate capacity for passage of the design flood; for this set, the maximum probable energy
losses should be assumed. The second set, involving minimum probable energy losses, is used for determination of depths and velocities for the evaluation of erosion and the design of erosion protection.

5-6. Erosion. Evaluation of expected erosion will be the most difficult and critical problem encountered in the design of limited service spillways. The designer must not only decide whether the channel materials will be eroded but also make reasonable estimates pertaining to the rate at which erosion will progress. Extensive exploration, testing of encountered materials, and geological profiles to a depth in excess of any anticipated scour are required to assist in the erosion estimates. Guidance on erosion progression is limited. Suggested permissible velocities for nonscouring channels are given in EM 1110-2-1601. The flow depth and turbulence are other important factors of incipient movement and rate of movement of channel materials; these factors should not be overlooked. Study of the history of erosion in the project area and research of erosion experiences at projects with similar facilities should be undertaken as part of the evaluation of expected erosion. Some additional information on erosion downstream from emergency spillways is given in item 21. WES has investigated scour downstream from emergency spillways and has produced a video report on this subject (item 18).

5-7. Control Section. A positive discharge control section is required for the limited service spillway. This section should be permanently fixed either in a rock cut or by construction of a concrete structure. The simplest type of control structure is a flat concrete slab with sidewalls, placed at a break in grade that will result in critical depth on the slab. A low ogee spillway crest will provide a more positive relation between reservoir elevation and discharge, a reduction in approach channel velocities, and an increase in the efficiency of the spillway. Normally a concrete apron is included downstream from the ogee crest in order to protect the toe of the crest and to align the flow with the erodible exit channel. The location of the control section is usually near the edge of the reservoir and well away from the dam structure. At sites where the channel is located in erodible material, three solutions exist:
a. The control section may be located to provide a long spillway channel with a large portion of the channel at a subcritical slope. This is done in order to ensure that the erosion, or head cutting, will start downstream from the subcritical slope and that the channel length is maximized, in order to maximize the material to be eroded and the time that will be required for the erosion to reach the control section.
b. The control section may be located at the downstream end of a cut or draw in order to maintain subcritical velocities through most of the spillway system. This configuration requires that side slopes of the cut or draw be sufficiently high to contain the design flow at the maximum reservoir elevation, and that the remaining in situ material be sufficiently competent to act as dam structure.
c. The control section located near the center of the channel length is sometimes preferred. At this position the control section is less likely to be lost due to scour than one at the downstream end. When the spillway is
sited in a bedrock structure, the most economical configuration may result by placing the control section at the upstream end of the channel and allowing supercritical velocities through most of the channel.

## Section III. Shaft Spillways

5-8. General. Shaft spillways include various configurations of crest designs, with or without gates, all of which transition into a closed conduit (tunnel) system immediately downstream from the crest. The closed conduit system on a shaft spillway is in lieu of the open channel chute used on conventional spillways. All configurations of shaft spillways have many of the same disadvantages. This section will present the disadvantages and the design problems involved in designing shaft spillways, one of which is the morning-glory spillway. This spillway may be designed to operate with crest control for a range of reservoir elevations immediately above the crest apex elevation and then conduit control as the reservoir elevation continues to increase. A shaft spillway should be designed in a manner that will prevent flow control shift from the crest to the conduit or outlet when the discharge is greater than 50 percent of the design flow. This recommendation is based on preventing the following hydraulic conditions from occurring when the reservoir is at or near full pool:
a. Unstable flow characteristics during the transition from crest to conduit control, which would occur over an extended period of time, resulting in unacceptable noise, rapid pressure fluctuations, and vibrations.
b. The undesirable change in reservoir elevation-to-discharge relationship associated with conduit or outlet control, wherein the reservoir elevation increases rapidly with comparatively small increases in discharge. This condition could lead to a rapid and unpreventable overtopping of the dam during the peak of a large flood.

Ideally, a shaft spillway should be designed to operate with crest control throughout the entire expected range of discharge. However, the range of expected discharge is based on the current hydrologic data. Spillway design flood flow rates may change due to updated probable maximum precipitation quantities; changes in the basin runoff characteristics could vary significantly with time; and the project operation may be revised at a future date which may result in an increase to the spillway design flood. Any of these factors, separately or in combination, could be sufficient to cause a spillway designed for crest control to shift to conduit control in the upper range of expected discharge. Another condition that could cause the control shift at essentially any discharge is partial plugging of the conduit. Plugging could occur either by external debris (logs and ice) or an internal problem resulting from cavitation damage. Projects incorporating a shaft spillway should consider this feature an outlet works, to be used in conjunction with another form of open channel auxiliary spillway.

5-9. Morning-Glory Outlet. The morning-glory outlet utilizes a crest circular in plan, with outflow conveyed by a vertical or sloping shaft, usually to a horizontal tunnel at approximately streambed elevation. This type structure is especially adaptable to damsites where a portion of the diversion
tunnel can be used as the horizontal tunnel. Plate $5-3$ shows typical layouts of vertical and sloping shaft designs. Hydraulic design data for the morningglory outlet are presented in HDC 140-1 to 140-1/2. Problems frequently encountered in this type of structure involve vortex action, unstable flow, and cavitation. Local topography may initiate vortex trends in the approach flow to the spillway, resulting in reduced capacity, flow instability, and surges in the spillway shaft and tunnel, as revealed by the USBR studies (items 7, 29, and 75). Posey and Hsu (item 42) performed laboratory studies that indicated the vortex over a submerged circular orifice can reduce the discharge by as much as 75 percent. Piers, fins, vanes, and curtain walls have been used to suppress vortex action. However, model studies are imperative to verify the effectiveness of this type of feature. When the flow control shifts from the crest to the conduit and vice versa, violent surging, originating in the shaft, can cause severe pressure and flow pulsations throughout the structure. Deflectors and vents in the shaft have been used to prevent these surges and pulsations (items 29 and 39). The need for deflectors and vents and verification of their design must be established by a hydraulic model study. The likelihood of cavitation near the point of tangency of the curve connecting the shaft to the horizontal tunnel should be considered.

## Section IV. Labyrinth Spillway

5-10. General. The labyrinth spillway is characterized by a broken axis in plan in order to create a greater length of crest compared to a conventional spillway crest occupying the same lateral space. The broken axis forms a series of interconnected V-shaped weirs (see Plate 5-4). Each of the V-shapes is termed a cycle. The spillway shown in Plate 5-4 is a lo-cycle labyrinth spillway. The labyrinth spillway is particularly well-suited for rehabilitation of existing spillways and for providing a large-capacity spillway in a site with restricted width. This is due to significant increase in crest length for a given width. The free-overflow labyrinth spillway can be designed to allow reservoir storage capacity equal to that provided when using a gated spillway, but without increasing the maximum reservoir elevation. This is achieved by the extremely large increase in discharge with a relatively small increase in reservoir stage. The labyrinth spillway hydraulic characteristics are extremely sensitive to approach flow conditions. This requires siting the crest configuration as far upstream into the reservoir as possible in order to achieve approach flow nearly perpendicular to the axis. For additional information on labyrinth spillways, see items 12, 20, and 26. Serious consideration of this type of spillway will require verification of the design by a physical model study.

Section V. Box Inlet Drop Spillways

## 5-11. General.

a. For small dams, where topographic and foundation conditions permit, the box inlet drop spillway provides an economical means of passing large flows through the dam with relatively small head increases. The concept is similar to that of a labyrinth spillway (Chapter 5, Section IV), in that a
folded crest is used to increase crest length within a relatively confined space.
b. Many configurations of box drop inlet spillways have been studied by the USDA (item 9). Two particularly useful types, which are not covered in item 9 are the flush-approach box drop developed by WES for the TennesseeTombigbee Waterway (Plate 5-5 and item 3), and the elevated box drop studied by the Agricultural Research Service (ARS) (Plate 5-6 and item 44).
(1) Design Guidance for the Flush-Approach Box Drop Spillway. Although a straight-on flow approach to the box drop (parallel to the stream and at right angles to the dam) is a more common configuration (see item 9), the Tenn-Tom flush-approach box drop is useful in situations where flow approaches the drop laterally rather than straight on. The dimensions of the box inlet drop spillway upstream of a steep chute can be determined from a known discharge and allowable head H or width of chute W , using the calibration data in Plate 5-7. For this data set, with drop length B to chute width ratios B/W range 1 to 4, and drop depth D to chute width ratios D/W range 0 to 1 , the abutment radius is equal to three times the width of the chute. If it becomes necessary to increase the radius of the abutments to allow more space for water to approach the box drop from the sides, as will be the case for smaller chutes, the curve in Plate 5-7 labelled "D $=0$ " should be used for design. This design without a drop will provide a conservative estimate of the discharge rating curve, and the change in the radius of abutments will have little effect on the discharge. A variation on this design, developed by the Nashville District, allows direct determination of chute width for a known discharge and head (see Plate 5-8) when $\mathrm{D} / \mathrm{W}=0.6$ and $\mathrm{D} / \mathrm{W}=3.0$. This guidance applies to box drop inlet spillways upstream from steep chutes. The slope of the chute will have little effect on the drop structure discharge capacity as long as supercritical flow occurs within the chute; however, the horizontal channel shown in Plate 5-5 could be long enough to cause a backwater effect on the head on the structure during high discharges. Note that the Tenn-Tom box drops were used as drainage structures and not spillways.
(2) Design Guidance for the Elevated Box Drop Spillway. In this spillway type, the drop box protrudes above the surrounding approach elevation. Controlled storage can thus be maintained up to the lip of the box, and a simple gated outlet can be placed through the wall of the box at the stream invert. A generalized elevated drop box spillway is shown in Plate 5-6. Item 44 contains a model study by the ARS of three different drop box configurations.

## CHAPTER 6

## CREST GATES

## 6-l. General.

a. The value of an uncontrolled fixed crest spillway in providing an extremely reliable operation and a very low cost maintenance facility is undeniable. Topographical, geological, economical, and political considerations at many damsites may restrict the use of an uncontrolled fixed crest spillway. The solution to these problems is usually the inclusion of crest gates; however, the uncontrolled fixed crest spillway should be used regardless of these considerations when the time of concentration of the basin runoff into the reservoir is less than 12 hours. When the time of concentration is between 12 and 24 hours, an uncontrolled fixed crest spillway should be given preference over a gated spillway. Basically, the inclusion of crest gates allows the spillway crest to be placed significantly below the maximum operating reservoir level, in turn permitting the entire reservoir to be used for normal operating purposes; and results in a much narrower spillway facility, avoiding the problems associated with high unit discharge/high-velocity flow and increased operation and maintenance costs. A gated spillway must include, as a minimum, two or preferably three spillway gates in order to satisfy safety concerns. Two common types of crest gates used extensively by the CE are the tainter (radial) gate and the vertical lift gate. These and other types of crest gates have been used throughout the world. This manual discusses only the tainter and vertical lift gates. A good discussion of all types of gates can be found in item 27.
b. The hydraulic design of crest gates involves the determination of the hydrostatic and hydrodynamic forces acting on the gate and crest in the immediate vicinity of the gate; the design and evaluation of gate seals, seats, and slots with respect to flow-induced vibrations and cavitationrelated problems; the determination of the rate of flow from partially open gates; and the evaluation of gate seat locations, the trunnion elevation, and other hydraulics-related structural features.

6-2. Tainter Gates. Recent controlled crest spillway designs tend to favor use of the tainter gate almost exclusively over any other type of crest gate. This is due to the relatively inexpensive first cost and the ease and low cost of operation and maintenance. The conventional tainter gate consists of a skin plate and a framework of horizontal and vertical members all of which are formed to a segment of a cylinder. This cylindrical segment is held in place by radial struts that converge downstream to a central location called the trunnion. The cylindrical skin plate structure is concentric to the trunnion which causes the resultant of the hydrostatic force to pass through the trunnion; thus, there is no moment resulting from this force to be overcome by the gate hoist. The gate lip is essentially sharp-edged, which results in minimizing downpull forces as well as vibration-inducing forces. The main load that the hoist must accommodate is a portion of the gate weight, side seal friction, and trunnion friction. The tainter gate does not require slots in the pier. This type of gate is noted for good discharge characteristics.
a. Gate Size and Trunnion Location. The tainter gate height is dependent upon the required damming height between the gate seat elevation and the maximum operating elevation. The gate width is related to the spillway monolith width because spillway piers are normally located in the center of the monolith with the gate spanning the space between the piers and the monolith joint. The gate trunnion is located above the water surface of the maximum uncontrolled discharge (see Chapters 2 and 3 for water surface profile determination). Usually the water surface location and gate geometry are such that the trunnion can be located at the optimum structural location of one-third the vertical distance above the lip of the gate. The horizontal location of the trunnion is dependent upon the gate seat location and the gate radius. Table 6-l shows the major dimensions of some of the large tainter gates used on the Columbia River Basin Projects. There appears to be no reason that gates significantly larger than those listed in Table 6-1 could not be used. The only constraints on gate size are economics and safety. Safety considerations require that at a minimum two spillway gates should be provided. Three gates are preferred to satisfy safety concerns.

TABLE 6-1

Major Tainter Gate Dimensions, Feet

| Project | Height | Width | Gate Radius | Horizontal Distance Seat To Crest | Vertical Distance Trunnion To Seat |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Lower Monumental | 60.6 | 50.0 | 60.0 | 11.2 | 18.6 |
| John Day | 60.0 | 50.0 | 60.0 | 10.2 | 20.0 |
| Libby | 56.0 | 48.0 | 55.0 | 15.6 | 18.1 |
| Chief Joseph | 58.2 | 36.0 | 55.0 | 10.7 | 20.2 |
| Dworshak | 56.7 | 50.0 | 55.0 | 7.0 | 18.0 |

b. Gate Seat Location. The location of the gate seat affects the height of the gate, the local crest pressures, and the discharge coefficients at partial gate openings. The coefficient effect is relatively unimportant from a design standpoint, as the gate opening can be adjusted to obtain the desired discharge. The gate seat should not be located upstream of the crest axis, as the jet issuing under the gate would tend to spring away from the crest boundary, resulting in negative pressures and possible cavitation damage on the crest. The gate seat can be located either on or downstream from the crest apex. The location of the gate seat is usually dictated by structural requirements such as the spillway bridge, hoist equipment location, etc. The gate seat location influences the trunnion location and the height that the gate must be raised to clear the water surface at the maximum uncontrolled discharge. Gate and trunnion clearance above the maximum uncontrolled discharge profile should include considerations for floating debris and ice and inaccuracies in the flow profile. Impact to the gate and trunnion by debris, ice, or high-velocity flow should be avoided.
c. Discharge Coefficient. The development of the rating curve for a partly open unsubmerged tainter gate, mounted on a spillway crest, is based on the following high head orifice equation:

$$
\begin{equation*}
Q=C W_{b} G_{0}(2 g H)^{1 / 2} \tag{6-1}
\end{equation*}
$$

where

$$
\begin{aligned}
W_{b} & =\text { gate width, feet } \\
G_{0} & =\text { gate opening, minimum distance from gate lip to crest } \\
\text { boundary, feet } & \\
H & =\text { distance from reservoir surface to center of } G_{0}, \text { feet }
\end{aligned}
$$

Plate 6-l shows suggested design discharge coefficient curves for various gate seat locations. The data points were computed from model and prototype data for several crest shapes and tainter gate designs with nonsubmerged flow. Data shown are based principally on tests with three or more bays in operation. Discharge coefficients for a single bay would tend to be lower because of side contractions. The discharge coefficient C shown in Plate 6-l is plotted as a function of the angle $\beta$ formed by the tangent to the gate lip and the tangent to the crest curve location intersected by the minimum distance line from the gate lip to the crest (see sketch in Plate 6-l). The computation of discharge under a partially open spillway crest tainter gate is complicated by the geometry involved in determining the gate opening, $\mathrm{G}_{0}$,
and the $\beta$ angle the gate lip makes with the crest. HDC 311-1 through 311-5 describe a method for the numerical solution of $G_{0}$ and $\beta$. The CORPS program H 3106 will perform the numerical solution for the gate opening and the discharge.
d. Crest Pressure. Flow characteristics at a control section gate are conducive to low pressures. Depending upon the situation, the pressure may be low enough to result in cavitation. Upstream from a gated spillway crest the flow velocity and resulting turbulence along the crest boundary are of a very low magnitude. At the control section a very rapid acceleration of the flow occurs without extensive turbulent boundary layer development. Thus, the velocity immediately adjacent to the crest boundary is essentially the potential velocity. As the turbulent boundary develops, the velocity immediately against the crest boundary becomes less than the average velocity. Because of the lack of a turbulent boundary layer near the control section, cavitation is much more likely to be tripped by surface irregularities here than further downstream. The pressure regime on the spillway crest boundary resulting from flow under a partially open tainter gate is a function of gate opening, gate radius, trunnion location, and hydraulic head on the gate. Lemos' results (item 25) indicate that the effects of radius and trunnion location are small and can be neglected. Dimensionless crest pressure profiles for small, medium, and large gate openings for the design head and for 1.33 times the design head are given in Plates 6-2 and 6-3, respectively. These data indicate that with the gate seat on the crest axis, a minimum pressure of about $-0.2 \mathrm{H}_{\mathrm{d}}$ can be expected on the spillway crest with a gate partially open and with the reservoir pool at $1.33 \mathrm{H}_{\mathrm{d}}$. The data also show that the pressures are somewhat higher with the gate seat located downstream from the crest axis.

As an example, for a spillway with gates operating under a 53-foot head on a crest designed for a 40 -foot head, a minimum pressure on the crest surface of -8 feet can be expected and a potential velocity of about $58 \mathrm{ft} / \mathrm{sec}$. A pressure-velocity combination of the magnitude in the example has the same potential for cavitation at surface irregularities as a pressure of zero and velocity of $73 \mathrm{ft} / \mathrm{sec}$. Where cavitation damage has occurred at control sections in the field, with pressures at about zero, velocities have been in excess of $100 \mathrm{ft} / \mathrm{sec}$. The magnitude of surface irregularities (tolerances) that can be allowed in the vicinity of the tainter gate should be developed using the potential velocity and the procedures discussed in Section VI of Chapter 2. Pressure fluctuations on the spillway crest boundary have been investigated at both Chief Joseph Dam and Table Rock Dam (items 64 and 68). These investigations have shown that pressures as low as -3.2 feet of water occurred at Chief Joseph Dam at a large gate opening. The pressure fluctuations recorded were random and are considered to be caused by the development of the turbulent boundary layer.
e. Gate Seals. Tainter gates included on spillways for multipurpose reservoir projects normally include rubber seals on both the sides and bottom of the gate. The design and construction of the sealing system must be precise for the seal to function as planned. The design of the bottom seal is critical because an incorrectly designed bottom seal can become the cause of flow-induced vibrations that could damage the gate. Figure 6-l shows a typical detail for both the side and the bottom seal. EM 1110-2-1605 is referenced as a source of additional information on tainter gate seals.

![](https://cdn.mathpix.com/cropped/59f740da-7b8c-4d04-aa98-940afdd24247-40.jpg?height=695&width=1327&top_left_y=1497&top_left_x=403)
Figure 6-l. Typical details for tainter gate seals

In the northern latitudes where freezing temperatures can occur, seal heaters are usually provided. The most common type of heater is a system that circulates heated fluid through tubes attached to the concrete side of the seal plates. Studies should be made to determine if heating the seals of every
gate is required. Studies showed that at Chief Joseph Dam side seal heaters were required for only 9 of the 19 gates.

6-3. Vertical Lift Gates. The vertical lift gate is rectangular in shape and consists of a structural frame to which a flat skin plate is attached, normally on the upstream face. The hydrostatic load on-the gate is transferred to the concrete structure through surfaces located in slots formed into the sides of the piers. The gate moves vertically within these slots in its own plane on a type of sliding bearing which characterizes the gate as a slide gate, wheel gate, tractor gate, etc. The hoisting system frequently consists of a track-mounted gantry crane which can be moved from gate to gate for opening and closing operations. This procedure leads to an expensive operation due to its labor intensiveness. For this reason, some projects have been designed or modified to include individual hoists for each gate. The principal hydraulic design aspects of the vertical lift gate are the shape of the bottom lip, the shape of the gate slots, and the determination of the hydraulic capacity.
a. Gate Bottom Shape. High-velocity flow under the vertical lift gate has a substantial influence on the hydraulic downpull (increased hoist load) or upthrust. The hydrodynamics of the flow under a gate may cause vertical oscillations (vibrations). Both of these conditions are dependent upon shape of the geometry of the gate bottom. Discussion, data, and references that would be useful for hydrodynamic load analysis on vertical lift gates can be found in HDC 320-2 to 320-2/3. Vibrations of the vertical lift spillway gates at Bonneville Dam were eliminated by a change in the gate bottom geometry (item 15).
b. Gate Slots. Flow past a discontinuity such as a gate slot will result in lowering the localized pressure immediately downstream from the discontinuity. Model and prototype data have shown that low pressures exist in and downstream from gate slots formed into the sides of spillway piers, and that with specific slot geometry and flow conditions, these pressures can be low enough to result in cavitation-induced damage. This is especially significant with projects that operate at heads greater than 40 feet with small gate openings. Proper geometric proportions of the slot will assist in maintaining higher boundary pressures in the vicinity of the slot. Details of various slot geometry and resulting pressure regimes are described in HDC 212-1 through 212-1/2. Spillways for hydroelectric projects usually provide for use of spillway bay bulkheads upstream from the spillway service gate. Normally these bulkheads are vertical lift type which require slots in the pier to hold the bulkhead. These slots are usually located at or upstream from the crest and sometimes extend into the pier nose geometry. Model studies for John Day Dam (item 38) included detailed studies of various bulkhead slot locations and shape. These studies led to the present use of the 90 -degree upstream edge on the slot. Model studies for Chief Joseph Dam (item 57) included the John Day Dam type slot and investigated the shape of the downstream return to the pier face. The results of these studies can be applied to vertical lift gate slot design equally as well.
c. Discharge Coefficients. The discharge under a vertical lift gate can be derived using the basic orifice equation described in equation 6-l.

The coefficient of discharge used must be based on vertical lift gates on spillway crests. WES (item 70) has developed a concept of relating vertical lift gate controlled discharge to free discharge. This procedure requires the determination of the head-discharge relationship for free flow. See Chapters 2 and 3 and the determination of gate opening to head on the crest ratio as described in Plate 6-4. See HDC 312 for additional information on vertical lift gate discharge coefficients.

6-4. Ice and Wave Forces on Gates. Horizontal forces acting on gates can be caused by both wind waves and ice or a combination of both. The periodic force of-waves on the gate should be considered when there is sufficient reservoir fetch to generate substantial waves. There is adequate theory presented in various texts including the CE "Shore Protection Manual" (item 74) to develop these wave forces. Forces against a gate can be caused by ice in various forms. Expanding sheet ice has been the subject of considerable study. A large force can also be induced by either current-or winddriven floe ice. The possibility also exists for local impact forces to occur from blocks of ice impelled by breaking waves. Design of spillway gates in the northern latitudes and/or at high elevations should include studies to determine ice loads. EM 1110-2-1612 should be consulted for additional information on ice forces.

## CHAPTER 7

## ENERGY DISSIPATORS

## Section I. Basic Considerations

7-1. General. The design of the energy dissipator probably includes more options than any other phase of spillway design. The selection of the type and design details of the dissipator is largely dependent upon the pertinent characteristics of the site, the magnitude of energy to be dissipated, and to a lesser extent upon the duration and frequency of spillway use. Good judgment is imperative to assure that all requirements of the particular project are met. Regardless of the type of dissipator selected, any spillway energy dissipator must operate safely at high discharges for extended periods of time without having to be shut down for emergency repairs. An emergency shutdown of the spillway facility during a large flood could cause overtopping of the dam and/or create unacceptable upstream flooding. The three most common types of energy dissipator used at CE projects are as follows:
a. The stilling basin which employs the hydraulic jump for energy dissipation.
b. The roller bucket which achieves energy dissipation in surface rollers over the bucket and ground rollers downstream of the bucket.
C. The flip bucket which deflects the flow downstream, thereby transferring the energy to a position where impact, turbulence, and resulting erosion will not jeopardize safety of the dam or appurtenant structures.

7-2. Design Discharge. The design discharge for a given spillway energy dissipator must be uniquely determined for each facility and should be dependent upon the damage consequences when the design discharge is exceeded. As a general rule, a spillway energy dissipator should be designed to operate at maximum efficiency and essentially damage-free with discharges at least equal to the magnitude of the standard project flood. The Chief Joseph Dam stilling basin is designed to contain the full spillway design flood (SDF) because failure to do so would compromise the integrity of the project's powerhouse which is located downstream of the basin. The dissipator need not be designed for the spillway design flood if operation with the spillway design flood does not create conditions endangering the dam or causing unacceptable economic damages. Libby Dam is an example where the stilling basin is designed to fully contain the standard project flood while the jump is allowed to entirely sweep out of the basin with a discharge equal to 70 percent of the spillway design flood. A flood that will cause sweepout of this basin would be an extremely remote possibility and would result in damage to the tailrace channel, tailrace channel bridge, and a power transmission tower. However, an economic analysis showed that the cost to dissipate the SDF energy within the stilling basin significantly exceeded the cost to repair and/or replace the damaged features.

7-3. Operation. Optimum energy dissipation will occur when the flow enters the dissipator uniformly. The hydraulic designer is responsible to ensure
that project operating schedules are developed to maintain balanced flow operation of a gated, multiple-bay spillway at equal gate openings. The designer must realize, however, that conditions may occur that require unbalanced operation, e.g., development of fish attraction flows, operator error, or emergencies. Such conditions should be considered during evaluation of energy dissipation and stilling basin performance under conditions of nonuniform flow distribution.

## Section II. Stilling Basins

7-4. General. The stilling basin employs the hydraulic jump for energy dissipation and is the most effective method of dissipating energy in flow over spillways. The theory of the hydraulic jump is discussed in paragraph 2-13 of this manual. The two basic parameters to be determined for design of a stilling basin are the apron elevation and length. Effective energy dissipation can be attained with a stilling basin having either a horizontal or sloping apron. The use of a sloping or horizontal apron is based solely upon economics in order to provide the least costly basin.

## 7-5. Horizontal Apron Basin.

a. Apron Length. The optimum stilling basin design would have an apron of sufficient length to confine the entire hydraulic jump. The jump length is a function of entering Froude number $\mathrm{F}_{1}$, and entering depth, $\mathrm{d}_{1}$. The approximate length of a hydraulic jump on a flat floor is $3.5 d_{1} F_{1}^{1.5}$ for $F_{1}$ less than five and $8.0 d_{1} F_{1}$ for $F_{1}$ greater than five (item 40). However, a basin of such length is normally not cost-effective. Appurtenances such as baffle blocks and end sills on the apron can be used to decrease the length of the jump without compromising the efficiency of energy dissipation. A limited review of stilling basins for high and low head spillway structures has shown that a stilling basin length can be reasonably defined by the equation:

$$
\begin{equation*}
\mathrm{L}_{\mathrm{b}}=\mathrm{Kd}_{1} \mathrm{~F}_{1}^{1.5} \tag{7-1}
\end{equation*}
$$

where $K$ is the stilling basin length coefficient from Table 7-1. Equation 7-1 is considered applicable in the range of Froude numbers, $F_{1}$, between 2 and 20, and will provide a basin length that is adequate for feasibility level designs and the basic basin length necessary to proceed into model verification. The coefficient $K$ in equation $7-1$ has been found to vary between 1.4 and 2.0 dependent upon the use of baffles and end sill. This coefficient is also dependent on the basin use, such as single gate or other unbalanced spillway flow conditions commonly found with low head navigation structures. Table 7-1 gives values for various conditions.
b. Apron Elevation. The optimum design for a stilling basin without baffles would have an apron elevation such that the jump curve defining the required $\mathrm{d}_{2}$ depth would superimpose on the tailwater curve for the full range of discharge. However, only in extremely rare circumstances will site and hydraulic conditions coexist that result in the jump curve superimposing

TABLE 7-1
Values of K for Various Types of Stilling Basins
| Type of Stilling Basin | K | Remarks |
| :--- | :--- | :--- |
| Stilling basin with a vertical, stepped, or sloping end sill and one or two rows of baffles | 1.4 | Items 41, 53, 54, 67, and 72 Suggested upper limit of $\mathrm{F}_{1}$ is approximately eight |
| Stilling basin with a vertical, stepped, or sloping end sill only | 1.7 | Items 38, 58, 60, and 62 |
| Stilling basin for low head broad-crested weir navigation dam spillways with one or two rows of baffles and a sloping end sill | 2.0 | See EM 1110-2-1605 |


on the tailwater curve. Experience indicates that if less than optimum energy dissipation can be tolerated, satisfactory performance can be maintained with a stilling basin that includes baffles and end sill when the apron elevation is set at full $\mathrm{d}_{2}$ depth at the stilling basin design discharge and not less than $0.85 \mathrm{~d}_{2}$ depth at the spillway design flood. If optimum energy dissipation is required, the basin apron should be set to provide for full $\mathrm{d}_{2}$ depth with the spillway design flood. Excessive tailwater tends to hold the spillway jet against the apron resulting in high velocity flow exiting over the end sill which may cause damage in the exit channel. Baffles located on the apron will deflect the jet upward through the tailwater to assist in energy dissipation even when tailwater depth is excessive. When determining the apron elevation, the hydraulic designer must evaluate the potential for tailwater changes resulting from downstream channel aggradation or degradation during the life of the project and design the basin accordingly.

7-6. Sloping Aprons. Depending on site foundation conditions, some degree of economy may be realized if the stilling basin is designed with a downstream sloping apron rather than horizontal apron. The hydraulic jump is allowed to form on a portion, or all, of the sloping apron. Plates 7-1 and 7-2, which were developed from tests by USBR (item 40), can be used to determine the jump length and tailwater depth required to evaluate the hydraulic jump on aprons of various slopes. In design of a basin, either with a continuous or a noncontinuous slope, baffles and an end sill should be considered. The basin apron can be considered horizontal when the slope is flatter than $1 \mathrm{~V}: 6 \mathrm{H}$.

## 7-7. Baffles.

a. General. Baffles are frequently used to aid in formation of the hydraulic jump. Their use can significantly reduce the length of the jump, decrease the required $\mathrm{d}_{2}$ depth for a given discharge condition, and provide stability to the jump. Baffle location, shape, size, and spacing are the important parameters to be considered in design of a baffle-aided stilling basin. Cavitation damage on baffles and surrounding surfaces will occur when baffles are used in conjunction with high Froude number flow. The stilling basin design discharge, Froude number and the expected frequency and duration of use are major factors that must be included in the decision to include baffle blocks on a stilling basin apron. The USBR (item 40) recommends the upper Froude number be limited to about 5.8 for a baffled basin when the basin is to be used frequently for such structures as canals, outlet works, and small spillways. Baffles have been used in the Chief Joseph Dam stilling basin (item 53) which has a design discharge Froude number of about five and is designed for frequent use over long-duration flood events. The baffles at Chief Joseph Dam have experienced significant cavitation damage. Green Peter Dam (item 54) has two rows of baffles with a relatively high design discharge Froude number of 8.5. The spillway of Green Peter Dam is expected to be used quite infrequently and for relatively short duration events; however, this stilling basin also provides energy dissipation for flow through the sluices which operate frequently for relatively short periods of time.
b. Shape. The standard CE baffle (Plate 7-3) with a rectangular upstream face and sloping downstream face is the preferred shape. Although a 6-inch bevel on all edges is acceptable, streamlined baffles are not recommended. Streamlining the baffles does not provide as effective energy dissipation as the standard baffle, and contrary to belief, is more likely to cause cavitation damage to the stilling basin floor and to the baffle.
c. Location. The first (upstream) row of baffles plays a dominant role in establishing the type of hydraulic action that the stilling basin will display. Baffles located too far downstream reduce the basin's effective length, while baffles located too far upstream will result in spray originating from the baffle faces. Tests accomplished at WES (item 35) indicate that the optimum location of the baffles is a function of entering Froude number. Data in Plate 7 - 4 a define the location of the upstream face of the first row of baffles. Model studies for which qualitative scour tests were conducted indicate that the second row of baffles assists in decreasing scour downstream from the stilling basin. A second row of baffles should be considered where downstream channel scour is expected to be a problem. When a second row of baffles is used, the upstream face of this row should be located about two and one-half baffle heights downstream from the upstream face of the first row and staggered with respect to baffles in the first row. Minimum spacing between the basin sidewall and a baffle is that required for forming purposes, with the maximum spacing being about one-half baffle width.
d. Size. The baffle height is a function of the entering Froude number as shown in Plate 7-4b. With Froude numbers less than 4.6, the baffle height should be $\mathrm{d}_{2} / 6$. The baffle width is essentially equal to the height although any reasonable width less than the height is satisfactory.

7-8. End Sills. An end sill is commonly used as the terminal wall of a stilling basin and forms a step or rise to channel bed elevation. The end sill deflects the higher velocity filaments which exist near the basin apron away from the channel bed. Results of qualitative scour tests with stilling basins containing baffles indicate that minimum exit channel scour results when the end sill has a height of $\mathrm{d}_{1} / 2$ or $\mathrm{d}_{2} / 12$, whichever is lower.
Higher end sills result in deeper scour near the end sill while low sills result in longer and deeper scour holes. The shape of the end sill does not affect its performance. A 1 V on 1 H sloping face end sill has the advantage of minimizing the potential for debris to be trapped in the stilling basin.

7-9. Sidewalls. Vertical stilling basin walls are preferred over battered walls because of unacceptable eddy conditions which occur with battered walls. When battered walls are required, the width at midheight of the stilling basin should equal the spillway width to minimize expansion and contraction of flow at the design discharge. Sidewalls should extend at least to maximum tailwater elevation, since return flow over stilling basin walls may create unsatisfactory basin performance, such as drowning of the jump, excessive turbulence, and localized scour downstream from the basin. Model studies are recommended when stilling basin design includes battered or low sidewalls. Computation of hydrodynamic forces acting on stilling basin sidewalls is discussed in paragraph 2-13.

7-10. Wing Walls. A design with free-standing sidewalls is preferable to one incorporating wing walls. Wing walls tend to reflect waves, resulting in a more severe attack on the exit channel side slope than that resulting when the basin sidewalls are terminated at the end sill. When wing walls are required for structural reasons, a wall rotated 90 degrees from the sidewall is preferable to other alignments.

## 7-11. Exit Channel.

a. General. Except in some unusual conditions, an exit channel is required to transition between the stilling basin and the main channel of the river. Since dissipation of the entire spillway discharge energy within the stilling basin is not normally accomplished, enlarging the channel width immediately downstream from the basin will assist in dissipating the residual energy. Due to the erosive nature of the highly turbulent flow exiting from a stilling basin, protection of the exit channel bed and side slopes is usually required to prevent channel scour and potential undermining of the stilling basin.
b. Size and Shape. The toe of the exit channel should be offset away from the sidewall a distance of $0.15 \mathrm{~d}_{2}$ or at least five feet. The invert elevation of the exit channel immediately downstream of the end sill should be set $0.25-0.5$ times the 100 percent diameter of stone, $\mathrm{d}_{100}$, used for channel protection below the top of the end sill. The setting of the channel invert lower than the end sill is beneficial in reducing the hydrodynamic lift and drag on the stones. Mild invert slopes are recommended to transition the exit channel to the river bottom. At Libby Dam, the originally designed 1 V on 6 H sloping runout proved to be unstable during prototype operation and was
subsequently modified to 1 V on 10 H . In some instances, sloping depressions or level areas immediately downstream from the end sill have been used to minimize potential for material to migrate down the runout slope and enter the stilling basin. Exit channel designs which abruptly contract the flow downstream from the basin tend to induce lateral eddies and should be avoided.
c. Protection. Unless sited in high-quality rock, the exit channel will require protection to prevent scour and potential damage to the stilling basin. Flow leaving a stilling basin is highly turbulent and as such has a larger erosive force than that due to similar velocities in a low turbulence area. Guidance for design of rock protection adjacent to stilling basins is given in HDC 712-1. Protection based upon this guidance should extend a distance of $10 d_{2}$ downstream from the stilling basin end sill and transition to the natural channel using gradually varying gradations as necessary to prevent major changes in adjacent rock sizes. The designer should be aware that inadequately sized rock or spalls could potentially be transported back into the stilling basin and cause significant damage. Model studies may be necessary to confirm design of the exit channel protection measures.

7-12. Abrasion and Cavitation. Stilling basin damage can occur as a result of abrasion, cavitation, or a combination of both. As discussed in Chapter 2, cavitation is possible wherever boundary irregularities cause a separation of flow with resultant localized pressure drops. In stilling basins, locations where irregularities may exist are at and around baffles, at misaligned joints, and at other irregularities. Cavitation damage is distinguished by its ragged, angular appearance. Abrasion damage, on the other hand, has a smooth and rounded appearance and can be attributed to rock and debris moving through or being trapped in the basin. Depressions which are initially caused by abrasion can form boundary irregularities sufficient to initiate cavitation damage. Rock, gravel, scrap metal, and other hard material may find their way into the energy dissipator by various means. Rock may be carried into a stilling basin by diversion configurations and project operation during the project's construction or by eddies transporting debris in from the downstream channel. In some cases, contractors may fail to clean out all hard material after construction, or rocks may be thrown into a basin by the public. Unbalanced gate operation in a multibay, gated spillway can create strong eddy conditions which draw material from the downstream channel into the basin. Major stilling basin damage requiring dewatering and costly repairs occurred at Libby and Dworshak Dams (item 47) as a result of abrasion following three years of operation (Figure 7-1). Practical measures which can be taken during design, construction, and operation of a project to reduce the possibility of damage to stilling basins are as follows:
a. Use wider exit channels with mild upward sloping runouts to transition from the basin apron to the river channel.
b. Specify close tolerances at construction joints and ensure that construction inspection enforces those tolerances.
c. Avoid baffles in high Froude number basins and never join baffles to basin sidewalls.

![](https://cdn.mathpix.com/cropped/59f740da-7b8c-4d04-aa98-940afdd24247-49.jpg?height=564&width=998&top_left_y=380&top_left_x=575)
Figure 7-l. Damage to Dworshak Dam stilling basin

d. Require that all channel excavations and erosion protection measures downstream and adjacent to basins be complete prior to operation of the basin.
e. Provide barriers around and above basins to prevent construction material from falling into the basin.
f. Plan diversions to reduce potential for depositing material adjacent to basins.
g. Require inspections and cleanup of basins at end of construction.
h. Require basins to be operated with balanced flow conditions.
i. Require regular monitoring of basins.

When material is known to be in the basin, immediately remove the material either by flushing with a uniform distribution of water, if possible, or by shutdown and removal by other means.

Hydraulic models may be used to plan and design diversions and operation during construction, to determine flow conditions substantial enough to flush material out of a basin, and to evaluate the effect of nonuniform flow distribution on eddy conditions in basins.

## Section III. Roller Buckets

7-13. General. A roller bucket energy dissipator consists of a circular arc bucket tangent to the spillway face terminating with an upward slope. This geometry when located at an appropriate depth below tailwater will produce hydraulic conditions consisting of a back roller having a horizontal axis above the bucket and a surge immediately downstream from the bucket. Solid and slotted buckets have been used successfully. The boundary geometry of a solid roller bucket is similar to that for a flip bucket except that the roller bucket is located well below the tailwater elevation. The geometry of
a slotted bucket is variable; however, it is similar to the solid bucket except for the addition of dentates on the downstream quadrant and a downstream apron. A roller bucket can be used where excessive tailwater depths exist either from hydraulic characteristics of the river channel or foundation conditions that require siting an energy dissipator well below the depth necessary for adequate hydraulic jump energy dissipation. For adequate energy dissipation to occur with a roller bucket, the tailwater depth must be within defined limits. These limits are dependent upon the inflow energy and the bucket radius. Insufficient tailwater depth will result in the flow sweeping out of the bucket and forming a jet, typical of a flip bucket. A more undesirable condition can occur just prior to sweepout when an instability develops which could result in excessive erosion and undesirable wave conditions in the tailrace and downstream channel. Excessive tailwater depth will cause the flow to dive from the bucket lip resulting in the development of a roller and surging downstream from the bucket. This action will cause erosion and movement of large volumes of bed material resulting in hydraulic instabilities, inadequate energy dissipation, and bucket erosion. Because the bucket is located immediately adjacent to the toe of the spillway, the roller bucket should be designed to efficiently dissipate the energy of the spillway design discharge to ensure against compromising the integrity of the dam structure proper. Appendix F contains an example problem for the design of a roller bucket.

7-14. Bucket Depth and Radius. The hydraulic design of the roller bucket is derived strictly from empirical data, the majority of which is from model studies (item 35). The minimum radius for a roller bucket, $r_{\text {min }}$, is defined as

$$
\begin{equation*}
r_{\min }=\frac{5.19\left(d_{1}+\frac{v_{1}^{2}}{2 g}\right)}{F_{1}^{1.64}} \tag{7-2}
\end{equation*}
$$

where

$$
\begin{aligned}
& d_{1}=\text { depth of flow entering the bucket, feet } \\
& v_{1}^{1}=\text { velocity of flow entering the bucket, ft } / \mathrm{sec} \\
& F_{1}^{1}=\text { Froude number of the entering flow }
\end{aligned}
$$

The bucket invert elevation limits, maximum tailwater depth $\mathrm{h}_{2} \max$, and minimum tailwater depth $h_{2} \min$, are related to the bucket radius ${ }^{2}, F_{1}, d_{1}$, and the specific energy of the entering flow $d_{1}+V_{1}^{2} / 2 g$. These relationships are provided in Plates 7-5 and 7-6. The roller height $h_{b}$ and the surge height $h_{s}$ are related to the difference in reservoir and bucket invert elevations $h_{1}$, the tailwater height $h_{2}$, and the parameter
$\left(\mathrm{q} \times 10^{3}\right) /\left(\mathrm{g}^{1 / 2} \cdot \mathrm{~h}^{3 / 2}\right)$ as shown in Plates 7-7 and 7-8. The important characteristics which must be evaluated in design of the roller bucket include the minimum tailwater depth which does not result in bucket sweepout, the maximum tailwater depth at which diving of the jet does not occur, and the maximum
surge height downstream of the bucket and the height of the back roller above the bucket. Hydraulic model tests to verify the design of roller buckets are recommended under the following conditions:
a. Sustained operation near the limiting conditions is expected.
b. Discharges exceed $500 \mathrm{ft}^{3} / \mathrm{sec}$ per foot of width.
C. Velocities entering the bucket exceed $75 \mathrm{ft} / \mathrm{sec}$.
d. Eddies appear possible.
e. Waves in the channel downstream from the structure would be a problem.

7-15. Slotted Buckets. A disadvantage of the solid roller bucket is that the downstream surge can move loose material from the channel bed back into the bucket where the action of the back roller can result in serious abrasion damage to the bucket surfaces. For this reason, USBR (item 40) developed a slotted bucket design which reduces the possibility of extraneous material being drawn back into the back roller. The slotted bucket also exhibits better self-cleaning properties. The slotted bucket disperses and distributes flow into the downstream surge over a greater depth resulting in less violent flow concentrations than does the solid bucket (item 34). The slotted bucket developed by USBR consists of upward rounded teeth with vertical sides and a rounded top. This slotted bucket configuration also includes a 16-degree upward-sloping, 20-foot-long apron downstream from the teeth. Model studies of the Little Goose Dam spillway (item 23) were made to develop a design having more easily constructed, plane surface teeth rather than the curved surface design developed by USBR. The Little Goose Dam studies resulted in a design (Plate 7-9) which consisted of teeth trapezoidal-shaped in cross section with an apron configuration downstream from the teeth identical to that of the USBR design. In addition to the less complicated geometrical shape, the Little Goose bucket teeth exhibited more acceptable pressures than the curved-shaped design.

7-16. Exit Channel. Because of the roller bucket's tendency to move loose material from the downstream channel into the bucket itself, design of the exit channel is relatively critical to acceptable performance of the structure. As previously discussed for the hydraulic jump stilling basin, gently sloped well-protected runout slopes should be used to transition from the roller bucket to the river channel. Roller bucket surging will result in the propagation of waves throughout the tailrace and in the downstream channel. The effect of these conditions on the river banks and other structures must be considered. Hydraulic models are necessary to evaluate, at least qualitatively, the performance of the exit channel.

## Section IV. Flip Buckets

7-17. General. The flip bucket itself is not an energy dissipator; however, it is an integral part of an energy dissipation system. The purpose of the flip bucket is to direct high-velocity flow (the jet) well away from the dam,
powerhouse, spillway, and/or other appurtenances. A small amount of energy is dissipated by friction through the bucket. During the jet's trajectory to its impact location, extremely turbulent flow exists and the jet spreads and frays. The extreme turbulence of the jet entrains a large volume of air. A portion of the jet's energy is dissipated by the interaction of the water and the air boundary resulting in considerable spray. The effect of heavy spray on adjacent structures, especially in cold regions, should be considered. The impact of the jet and the interaction of the turbulent flow and the boundary at the impact area account for the major portion of energy dissipation. The impact will almost certainly cause adjustment to the riverbed even if the bed material is rock. For this reason, use of a flip bucket should be considered only where bed scour caused by the impact of the water jet cannot endanger the dam, power plant, or other structures (including the flip bucket itself) or cause unacceptable environmental damage. Where the flip bucket can be appropriately used, it offers an attractive economical alternative to a stilling basin or roller bucket structure; however, the flip bucket includes more uncertainties as to adequacy than do stilling basins or roller buckets. The parameters of prime importance to the hydraulic designer are the bucket geometry, pressures acting on the bucket boundaries, and the jet trajectory characteristics. Flip bucket design is based on empiricism essentially derived from model studies. For this reason, any deviations from the flip bucket design parameters and guidelines discussed in this manual should be verified by hydraulic model studies. Appendix F contains an example problem for the design of a flip bucket.

## 7-18. Bucket Geometry.

a. General. The geometric parameters required for design of a flip bucket include the bucket radius, $r$, the minimum height of the bucket lip, $h_{\min }$, the trajectory angle at the end of the bucket, $\theta$, the bucket invert elevation, and the planimetric alignment of the bucket. The parameters $r$, $h_{1 n}$ and $\theta$ are closely related and may require trial-and-error adjustment inlnorder to obtain a satisfactory design. The planimetric alignment can be developed to direct the location of the jet impact area. Figure $7-2$ depicts the various terms used for the flip bucket design process.

![](https://cdn.mathpix.com/cropped/59f740da-7b8c-4d04-aa98-940afdd24247-52.jpg?height=538&width=1364&top_left_y=1846&top_left_x=407)
Figure 7-2. Parameters used in the design of a flip bucket

b. Radius. The minimum radius, $r_{\text {min }}$, is a function of the allowable theoretical unit load on the bucket invert $P_{T}$, the velocity of flow, $V_{1}$, and the depth of flow, $d_{1}$, entering the bucket defined as

$$
\begin{equation*}
r_{\min }=\frac{\rho V_{1}^{2} d_{1}}{P_{T}-\gamma d_{1}} \tag{7-3}
\end{equation*}
$$

As a general design guide, previous experience suggests that a bucket radius at least equal to four times the maximum flow depth will turn most of the water before it leaves the bucket.
c. Minimum Height. The height of the bucket lip must be sufficient to prevent the water from merely overriding the bucket lip in lieu of being turned and flipped out of the bucket. To effectively turn the flow, the bucket height must be at least high enough to intersect the forward-projected slope of the water surface at the point of curvature of the spillway and the bucket curve. The minimum bucket height described by equation 7-4 will ensure that the flow will follow the bucket curve and not override the downstream lip.

$$
\begin{equation*}
h_{\min }=r-r \cos \left(\phi-\tan ^{-1} S\right) \tag{7-4}
\end{equation*}
$$

where

$$
\phi=\tan ^{-1}\left\{\frac{\left[d_{1}\left(2 r-d_{1}\right)\right]^{1 / 2}}{r-d_{1}}\right\}
$$

describes the minimum deflection angle and $S$ is the slope of the spillway chute adjacent to the bucket.
When $\phi>\tan ^{-1} \mathrm{~s}$, the minimum height of the bucket becomes zero. The height of the bucket is then defined by the required trajectory angle $\theta$. A trial-and-error adjustment of the bucket radius and/or bucket flip angle may be necessary to meet or exceed the minimum bucket height as defined in equation 7-4.
d. Trajectory Angle. The trajectory angle is the angle the bucket lip makes with respect to the horizontal. The trajectory angle is a factor in determining the length of the jet trajectory distance and the general hydraulic characteristics in the impact area. Steeper angles increase the trajectory length and provide better dissipation than flatter angles as they cause the jet to impact in a more vertical direction with less violent side eddies. A 45 -degree flip angle will result in the maximum trajectory distance. The required height of the bucket lip, h , above the bucket invert necessary to satisfy the desired trajectory angle $\theta$ can be determined by the following equation:

$$
\begin{equation*}
h=r-r \cos \theta \tag{7-5}
\end{equation*}
$$

e. Bucket Elevation. For optimum performance, the flip bucket cannot operate under submerged conditions. Depending on the shape of the tailwater curve, raising of the bucket invert elevation or the lip of the bucket may be required. In evaluating tailwater conditions, the designer should consider that the ejector action of the jet as it exits the bucket may tend to cause a drawdown in the tailwater elevation depending on downstream channel geometry. Such drawdown may adversely impact the operation of adjacent structures such as powerhouses, etc. The amount of drawdown which may occur with any given design can best be determined from hydraulic models. For preliminary design purposes, a method of estimating drawdown can be found in item 40.
f. Bucket Termination. The bucket should terminate with a 90-degree cut from the bucket lip, and the sidewalls should terminate at the lip to allow sufficient air to be drawn below the point of the trajectory separation from the bucket lip. Failure to allow sufficient air to the underside of the jet will cause jet flutter with resultant pressure fluctuations and possible cavitation damage. The original design of the flip buckets on the Wynoochee Dam outlets (item 55) terminated in a 20 -degree cut which resulted in cavitation damage to the concrete surfaces downstream from the lip. Extending the bucket length to allow a 90 -degree termination cut has eliminated this damage.
g. Alignment. The flip bucket can be aligned to direct the trajectory impact to a preselected location by curving or adding appurtenances to the bucket. An example of such a directional design is the spillway for the East Branch Reservoir spillway (item 63). Model studies are required to confirm the final design of a directional flip bucket. A bucket alignment which spreads the flow at the impact area across as much of the river channel as possible minimizes riverbed adjustment and return flow from the downstream tailwater.

7-19. Discharge Considerations. Flip buckets perform best when the entering flow is at high velocity and low unit discharge as such conditions result in considerable fraying of the jet by air resistance. Moderately high unit discharges, however, should not be a problem if downstream channel adjustment is not of prime consideration. The flip buckets at Wynoochee Dam (item 55) have operated satisfactorily for extended periods with unit discharges of approximately $350 \mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft}$. The Applegate Dam spillway flip bucket was developed through model studies (item 61) and is designed for a unit discharge of $850 \mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft}$. Flip buckets exist where design unit discharges are well in excess of $1,000 \mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft}$; these designs are extremely critical with respect to cavitation damage due to the extremely high velocities, deep flow depths, and subatmospheric pressures which exist. Model studies are recommended for flip buckets designed with unit discharges in excess of $250 \mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft}$.

7-20. Trajectory Distance. The jet trajectory distance is dependent upon the velocity of flow entering the flip bucket, the trajectory angle, and the vertical distance from the bucket lip to the impact area. The trajectory distance, $\mathrm{X}_{\mathrm{H}}$, which is the horizontal distance from the bucket lip to the impact location, is determined by the equation:

$$
\begin{equation*}
X_{H}=h_{e} \sin 2 \theta+2 \cos \epsilon\left[h_{e}\left(h_{e} \sin ^{2} \theta+Y_{1}\right)\right] 1 / 2 \tag{7-6}
\end{equation*}
$$

where

$$
\begin{aligned}
& h_{1}=\text { velocity head at the bucket lip, feet } \\
& Y_{1}^{e}=\text { vertical distance below the bucket lip to the impact area, feet }
\end{aligned}
$$

When the $Y_{1}$ value is equal to zero, then equation $7-6$ reduces to:

$$
\begin{equation*}
X_{H}=\frac{V^{2}}{2 g} \sin 2 \theta \tag{7-7}
\end{equation*}
$$

The angle at which the jet strikes the impact location, $\theta^{\prime}$, is described by the following equation:

$$
\begin{equation*}
\theta^{\prime}=\tan ^{-1}\left[\sec \theta\left(\sin ^{2} \theta+\frac{Y_{1}}{h_{e}}\right)^{1 / 2}\right] \tag{7-8}
\end{equation*}
$$

Equation 7-8 reduces to $\theta^{\prime}=\theta$ when $Y_{1}$ is equal to zero. Trajectory lengths based on equations 7-6 and 7-7 have been simulated reasonably well in hydraulic models. Prototype trajectories are somewhat shorter and have steeper impact angles than the model or theoretical jet due to the greater air resistance encountered in the prototype.

7-21. Bucket Pressures. Pressures on the invert of the bucket vary throughout the curve and are influenced by the curve radius, the total head on the invert, and the unit discharge. A WES study (item 71) indicated that, for relatively high dams, bucket pressures could be expressed as:

$$
\begin{equation*}
\mathrm{h}_{\mathrm{P}}=f\left(\frac{\mathrm{q}}{\mathrm{r}\left(2 \mathrm{gH}_{\mathrm{T}}\right)^{1 / 2}}, \frac{\alpha}{\alpha_{\mathrm{T}}}\right) \tag{7-9}
\end{equation*}
$$

where

$$
\begin{aligned}
h_{p} & =\text { pressure head against boundary, feet } \\
H_{T} & =\text { total head (point to energy gradient), feet } \\
\alpha & =\text { angle of rotation from beginning of curve, degrees } \\
\alpha_{T} & =\text { total deflection angle, degrees }
\end{aligned}
$$

The term $\alpha / \alpha_{T}$ defines the relative position along the curve. The pressure distribution throughout the length of the flip bucket can be estimated using the data provided in Plate $7-10$. This curve has been developed from model data although some prototype data at a small discharge has been included. This curve is essentially the same as HDC Chart 112-7 plotted in a different form. The term $q /\left[r\left(2 \mathrm{gH}_{\mathrm{T}}\right)^{1 / 2}\right]$ has been replaced by $d_{1}^{1 / 2} / r$ for the usual case where $d_{1}$ is small when compared to $V^{2} / 2 g$. See HDC Chart 112-7 for a more detailed discussion on the data used for Plate 7-10.

7-22. Exit Channel. Optimum performance will occur when the jet trajectory at impact spreads approximately across the entire width of the river channel. Unless the jet impact area is located in extremely durable rock, a scour hole can be expected to occur at the impact point. The material scoured in development of the hole will be deposited downstream where it may adversely impact satisfactory operation of the flip bucket. A preformed scour hole at the impact area can be used to minimize deposition in the downstream channel. Violent wave action can be expected in the impact area, and wave and highvelocity turbulence will likely extend laterally and downstream from the impact. These conditions can lead to streambank damage unless the banks are adequately protected. A model study is recommended to qualitatively evaluate the extent of bed scour and hydraulic conditions existing with operation of a flip bucket.

## 7-23. Miscellaneous.

a. Drainage. The bucket must be adequately drained to prevent water impoundment in the bucket. Due to potential for cavitation damage, floor drains should be avoided and the bucket should be drained laterally through the sidewalls.
b. Low Flow Operation. At low flows, water may pond in the bucket and spill over the lip. Erosion may be caused by these low flows which do not flip and should be considered in the design. A concrete slab, cutoff wall, or large stone may be needed at the toe of the structure to protect the structure from undermining. A double-flip bucket design was developed for the Applegate Dam spillway (item 61) to prevent damage which would result with operation of low, nonflipping discharges.

## Section V. Specialized Energy Dissipators

7-24. Impact Basin. An impact hydraulic jump-type energy dissipator was developed by Blaisdell (item 9) for small drainage structures. The USBR uses a similar dissipator which they designate as a Type III Basin (item 40). Tests at WES on the Rend Lake (item 17) and Oakley (items 31 and 73) projects showed this type basin to be very effective in the Froude number range of 2.5 to 4.5. Preferred dimensions of the basin and its elements for use in this range of Froude numbers are given in Plate 7-11. This type dissipator is not recommended where velocity entering the basin exceeds $60 \mathrm{ft} / \mathrm{sec}$ as the chute blocks would be subject to damage by cavitation. An apron length equal to at least $3 \mathrm{~d}_{2}$ for flows up to the standard project flood, and $2 \mathrm{~d}_{2}$ for the spillway design flood is considered adequate. The basin elevation should provide a depth on the apron of $\mathrm{d}_{2}$ for the standard project flood and at least $0.85 \mathrm{~d}_{2}$ for the spillway design flood.

7-25. Baffled Chute. The baffled chute spillway relies upon multiple rows of baffles to aid in dissemination of energy flowing down a spillway chute. The USBR (item 40) has developed a set of design guidance which can be used in preliminary design of such a structure. Large baffled chute spillways have been used on the Tennessee-Tombigbee Waterway divide cut to convey the flow of streams intercepted by the canal down the cut slope into the canal (item 3). Model studies are recommended for design verification when the design
discharge exceeds $50 \mathrm{ft}^{3} / \mathrm{sec}$ and/or the slope is steeper than 1 V on 2 H . A baffled chute design was developed via model study (item 59) for the proposed Libby Reregulating Dam which was effective not only in energy dissipation, but also in aerating the flow and reducing nitrogen supersaturation. The specially designed baffle (Plate 7-12) for this structure exhibited good aeration characteristics for discharges up to $180 \mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft}$ and adequate energy dissipation for discharges as high as $900 \mathrm{ft}^{3} / \mathrm{sec} / \mathrm{ft}$.

