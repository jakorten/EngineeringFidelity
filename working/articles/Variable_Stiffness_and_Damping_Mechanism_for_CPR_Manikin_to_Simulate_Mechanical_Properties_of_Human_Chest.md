# Variable Stiffness and Damping Mechanism for CPR Manikin to Simulate Mechanical Properties of Human Chest

## Page 1

Received 19 February 2024; revised 29 May 2024; accepted 2 July 2024.
Date of publication 16 July 2024; date of current version 29 July 2024.
Digital Object Identifier 10.1109/JTEHM.2024.3429422
Variable Stiffness and Damping Mechanism for
CPR Manikin to Simulate Mechanical
Properties of Human Chest
HYUNGSOO LIM
1,2, (Graduate Student Member, IEEE), DONG AH SHIN
3, (Member, IEEE),
JAEHOON SIM4, JAEHEUNG PARK
4,5, (Member, IEEE), TAEGYUN KIM6,7, KYUNG SU KIM6,7,
GIL JOON SUH
6,7,8, AND JUNG CHAN LEE
9, (Member, IEEE)
1Interdisciplinary Program in Bioengineering, Seoul National University Graduate School, Seoul 08826, South Korea
2Integrated Major in Innovative Medical Science, Seoul National University Graduate School, Seoul 08826, South Korea
3Institute of Medical and Biological Engineering, Medical Research Center, Seoul National University, Seoul 08826, South Korea
4Graduate School of Convergence Science and Technology, Seoul National University, Seoul 08826, South Korea
5Advanced Institute of Convergence Technology (AICT), Suwon-si 16229, South Korea
6Research Center for Disaster Medicine, Seoul National University Medical Research Center, Seoul 03080, South Korea
7Department of Emergency Medicine, Seoul National University Hospital, Seoul 03080, Republic of Korea
8Department of Emergency Medicine, Seoul National University College of Medicine, Seoul 03080, South Korea
9Department of Biomedical Engineering, Seoul National University College of Medicine, Seoul 03080, South Korea
(Hyungsoo Lim and Dong Ah Shin are co-first authors.) CORRESPONDING AUTHOR: J. C. LEE (ljch@snu.ac.kr)
This work was supported in part by the Basic Science Program through the National Research Foundation of Korea (NRF) funded by the
Ministry of Education under Grant 2021R1A6A3A01087371 and in part by Korea Medical Device Development Fund Grants funded by
Korea Government under Project RS-2022-00141157.
ABSTRACT
Objective: This study introduces a novel system that can simulate diverse mechanical properties
of the human chest to enhance the experience of CPR training by reflecting realistic chest conditions of
patients. Methods: The proposed system consists of Variable stiffness mechanisms (VSMs) and Variable
damper (VD) utilizing stretching silicone bands and dashpot dampers with controllable valves to modulate
stiffness and damping, respectively. Cyclic loading was applied with a robot manipulator to the system.
Compression force and displacement were measured and analyzed to evaluate the system’s mechanical
response. Long-term stability of the system was also validated. Results: A non-linear response of the human
chest under compression is realized through this design. Test results indicated non-linear force-displacement
curves with hysteresis, similar to those observed in the chest of patients. Controlling the VSM and VD
allowed for intentional changes in the slope and area of curves that are related to stiffness and damping,
respectively. Stiffness and damping of the system were computed using performance test results. The stiffness
ranged from 5.34 N/mm to 13.59 N/mm and the damping ranges from 0.127 N·s/mm to 0.511 N·s/mm.
These properties cover a significant portion of the reported mechanical properties of the human chests. The
system demonstrated satisfactory stability even when it was subjected to maximum stiffness conditions of
the long-term compression test. Conclusion: The system is capable of emulating the mechanical properties
and behavior of the human chests, thereby enhancing the CPR training experience.
INDEX TERMS
Cardiopulmonary resuscitation (CPR), manikin, variable damping, variable stiffness,
thorax.
Clinical and Impact: By achieving non-linear mechanical properties including hysteresis, our system has the
potential to be used in medical trainings and research studies that reflect more realistic CPR conditions.
I. INTRODUCTION
C
ARDIOPULMONARY Resuscitation (CPR) is a treatment performed for individuals who have suffered
cardiac arrest to restore blood circulation through chest
compressions preventing damage to major organs such as
brain, and helping the return of spontaneous circulation
(ROSC) [1]. Chest compression is especially related to survival of patients [2], [3]. American Heart Association (AHA)
recommends to keep compression depth of 5 cm and compressions speed of 100 to 120 for a minute during CPR [1].
542
 2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/
VOLUME 12, 2024

## Page 2

H. Lim et al.: Variable Stiffness and Damping Mechanism for CPR Manikin
FIGURE 1. Schematic of human chest expressed with mechanical
components.
Since compression rates [4] and depth [5] affect the survival
rate of the patients [6], it is important to get the technique
right. CPR education for resuscitation skill training is usually conducted using manikins that resemble torso of human
including silicone skin, a pushing element that acts like a
sternum and a spring that exerts stiffness against compression
loading. Because of this structure, the manikin shows almost
linear behavior on dynamic loading. However, mechanical
characteristic of a real human chest demonstrates a non-linear
mechanical behavior which can be expressed with not only
spring but also damper under dynamic loadings [7], [8], [9]
as shown in Fig. 1. Such non-linear mechanical properties
may vary by age, gender, and weight [10], [11], [12], [13],
[14]. These properties are also affected by changes in CPR
conditions such as compression force, depth, and length of
time CPR has been performed [15]. However, the mechanical
properties of commercially available CPR training manikins
remain constant and no information on these properties is not
provided. In addition, it is challenging to modify manikins
to have various stiffness and damping characteristics. For
these reasons, commercially available CPR manikins fail to
accurately simulate diverse mechanical behaviors observed
in real-life patients. The dissimilarities in mechanical characteristics between manikins and actual patients can result
in differences between compression forces and fatigue levels
learned from training and those in actual situations. This
can impede the delivery of optimal CPR in real-world situations. To provide a CPR training reflecting real-world cases,
a manikin that can represent a range of mechanical properties
similar to that of a human under compression loadings is
needed.
Several studies have proposed manikins that can mimic
the non-linear characteristic of human chests [16], [17], [18],
[19], [20]. Nysæther et al. [16] have suggested a manikin with
a spring and damper inside. The proposed manikin expressed
a range of stiffness profiles similar to the measured stiffness
of real patients. However, the damping of the manikin was
fixed, which limits the range of chest properties it can express.
Besides, in order to change the stiffness, the spring must
be replaced to other springs with different stiffness profiles.
Stanley et al. [17] have proposed a system with a damper
system that is controlled with respect to movement of a
manikin’s chest to achieve desired amount of damping, taking
into account the hysteresis profile of a human chest. The
system showed force-displacement curves with hysteresis.
However, the constant stiffness and damping characteristics
only represent a single instance of human chest properties.
Eichhorn et al. [18] have developed a mechanical thorax with
adjustable stiffness and mock heart to simulate the blood
flow during CPR. The system consisted of springs, pneumatic
pistons, one chamber heart and a piston to compress the
heart. The stiffness of the system coincides well with that of
human chest. Blood flow by compression was also simulated.
However, the damping characteristic of the system was not
clarified in the study. Kanakapriya and Manivannan [19]
and Thielen et al. [20] have suggested systems that include
springs connected serially so that stiffness of manikin can
increase with increasing compression depth. However, such
systems achieved smaller magnitude of stiffness than CPR
manikin or human chest.
As far as we know, a manikin that can independently
change both stiffness and damping has not been reported yet.
When both stiffness and damping are controllable, a CPR
manikin has potential to simulate various mechanical properties of human chest and CPR scenarios.
Therefore, the objective of this study was to develop a system with variable stiffness and damping mechanisms for CPR
manikin that could simulate mechanical properties similar to
human chest and enhance the reality of CPR manikin and
CPR training.
II. METHODS
A. DESIGN OF THE SYSTEM
The design of the entire system is shown in Fig. 2(a). Variable
stiffness mechanism (VSM) and Variable damper (VD) were
devised and implemented to satisfy the range of mechanical
characteristics of human chest. Three sets of VSMs and VDs
were mounted on a base plate. A pushing plate that could
transmit dynamic loading to each set was installed on the top
of the VDs. Those mechanisms were implemented for use on
a manikin and controlled with a home-made control system
to achieve desired mechanical characteristics. All parts were
designed using Autodesk Inventor 2023 (Autodesk Inc., US).
1) VARIABLE STIFFNESS MECHANISM (VSM)
As shown in Fig. 2(b), the VSM unit consists of a pair of
subassemblies which include spools, servo motors (XH430V350, Robotis, Korea), and sets of gears and silicone bands
that could act like springs. Silicone bands were used to connect the ring-shaped part of cylinders and spools of either
side. These silicone bands were manufactured using a silicone
material (SH0140U, KCC Co., Korea) with a shore hardness
of 40A, a tensile strength of 8.5 MPa, and a maximum elongation rate of 645%. The spools and ring-shaped parts were
VOLUME 12, 2024
543

## Page 3

H. Lim et al.: Variable Stiffness and Damping Mechanism for CPR Manikin
FIGURE 2. Drawings of the variable stiffness mechanism (VSM), the variable damper (VD) and the total system. (a) A total assembly drawing of the
system that consists of three sets of VSM and VD. (b) A cross-section view of the VSM unit. As spools rotate, silicone bands are wound or unwound
resulting in stiffness modulation. (c) A structure of VD. Controlling the valve beneath the cylinder, damping of the unit is modulated. (d) If the valve
is closed when the cylinder stroked, the air (translucent blue arrow) in and around the cylinder can only flow through a small gap between the
inner surface of the cylinder and the outer surface of the piston, maximizing the damping. (e) If the valve is open when the cylinder is stroked,
most of the air in and around the cylinder can flow through the valve, minimizing the damping.
3D printed (Accura 25 and Projet 7000 HD, 3D Systems Inc.,
US). The translucent lids were machined from polycarbonate.
When the servo motors were activated, spools rotated
outwards (clockwise for right spools, counter clockwise
for left spools), causing a portion of the silicone bands to
wind on spools. As the bands were wound more, they were
stretched further. Thus, required a greater force was required
to elongate them. Consequently, the stiffness of the system in
response to compression forces was increased.
2) VARIABLE DAMPER (VD)
A dashpot damper with a valve is designed to make damping
adjustable as shown in Fig. 2(c).
A piston was inserted into a cylinder that was closed on one
side. A hole was placed on the surface of the closed side of
the cylinder. A bar with a 90-degree curved circular channel,
like an elbow pipe, was placed beneath the cylinder. One end
of the channel met the hole of the cylinder while the other
end was directed to a vent. As the piston moved, air flew in
and out of the cylinder via this channel (Fig. 2(d) and 2(e)).
Linearly translating the bar changes the effective area of the
channel cross-section, serving as a valve to modulate the system’s damping. The piston was machined from acetal with a
diameter of 69.5 mm and a height of 30 mm. The cylinder was
made of poly methyl methacrylate (PMMA). The diameters
of the hole at the bottom of the cylinder and the channel of
the bar are 8 mm. A stepper motor (PKP525N12A, Oriental
Motor, Japan) was used for the linear motion of the bar. The
maximum stroke of the piston was designed to be 60 mm to
satisfy the compression depth requirement of CPR [1].
3) CONTROL SYSTEM
A control system for VSM and VD was built with a Raspberry
Pi 4, a servo interface board (U2D2, Robotis, Korea), stepper
motor drivers (CVD524BR-K, Oriental Motor, Japan) and a
power supply (ADS-15524, Meanwell, US) as depicted in
544
VOLUME 12, 2024

## Page 4

H. Lim et al.: Variable Stiffness and Damping Mechanism for CPR Manikin
FIGURE 3. Schematic diagram of the control system. Blue line = signal;
Black line = power; SMPS: Switching Mode Power Supply.
FIGURE 4. Picture of the experimental setup. Compression loading was
achieved with four-degrees-of-freedom(4-DoF) manipulator (U3robotics,
Korea).
TABLE 1. Stiffness and damping adjustment range of the system.
Fig. 3. A program was developed on Raspberry Pi to control
rotation amounts of each spool and aperture opening areas of
each damper.
B. PERFORMANCE TEST
1) COMPRESSION TESTS WITH PARAMETERS ADJUSTMENT
Compression tests were conducted to validate mechanical
behavior of the system according to the setup shown in Fig. 4.
As shown in Table 1, 12 rotation angles for the spools and
eight opening rates of the apertures were decided. A combination of these gave 96 cases to evaluate.
From the smallest stiffness condition to the largest stiffness
condition, 30 compressions were performed serially at a rate
of 100 compressions per minute with a depth of 5 cm using
a four-degree-of-freedom(4-DoF) manipulator (U3robotics,
Korea). A preload was applied at around 20 N of magnitude
before starting each test to ensure contact between the manipulator and the system.
To avoid any changes in mechanical properties of the silicone bands across the entire stress range from minimum to
maximum, tests were repeated in the same order after all tests
had been completed.
Compression force and depth were collected at a rate
of 1000 Hz from sensors embedded in the robot manipulator.
2) MECHANICAL CHARACTERISTIC ANALYSIS
From collected force and displacement data, spring constant and damping coefficient were calculated. With methods
described in [21], stiffness k and damping coefficient c were
analyzed.
From the equation of motion of the system, external force
Fext can be written as follows:
Fext = kd + c˙d = kd + cv
(1)
where d is the displacement and v is the speed of manipulator
differentiated from the depth by time. Equation (1) can be
rewritten to show compression period and releasing period as
follows:
Fcomp −kdcomp −cvcomp = Frelease −kdrelease −cvrelease
(2)
Since the difference between the force required for compression and the force used for recoil comes from the change
in damping at each period, equation (2) can be written as
follows:
Fcomp (d) −Frelease (d) = c(d)(vcomp −vrelease)
(3)
Rearranging Equation (3), c(d) can be obtained as follows:
c (d) = Fcomp (d) −Frelease (d)
vcomp (d) −vrelease (d)
(4)
Rewriting equation (1) with respect to k, k(d) can be
derived as follows:
k (d) = Fcomp (d) −c (d) vcomp (d)
dcomp
(5)
Values for k(d) and c(d) were computed from these equations using MATLAB R2023b (Mathworks, US) for each
case. These values were then compared with stiffness and
damping values suggested in previous study [14].
3) STABILITY TEST
A long-term cyclic loading experiment was conducted to
assess the reproducibility of the silicone bands that represent
system’s stiffness under repeated loading.
A set of one VSM and one VD was constructed and assembled for this experiment. A pair of unused silicone bands were
VOLUME 12, 2024
545

## Page 5

H. Lim et al.: Variable Stiffness and Damping Mechanism for CPR Manikin
FIGURE 5. Screenshot of control program of the system. Numbers 1 to
6 represent servo motors. A, B, and C represent stepper motors.
installed in the VSM. The same robot manipulator used in the
previous performance test was also used for this test.
The stiffness was set to the maximum rotation angle of
480 degrees. The damper valve was opened to 100 %. This
setting could provide a maximum reaction force of approximately 240 N. Since the original system consisted of three
sets of VSM and VD, this test setting corresponded to the
maximum reaction force of 720 N, surpassing the force in the
range of 300 to 600 N typically required for actual CPR [21].
Compression conditions were set to be the same as those
for the performance test (depth of 5 cm, compression rate of
100 compressions/min).
Repetitive compression was conducted for 90 minutes,
resulting in approximately 90,000 cycles. After compression,
magnitudes of the initial and final peak reaction forces were
compared, followed by the analysis of variation in reaction
forces during the test.
III. RESULTS
A. DESIGN OF THE SYSTEM
The system was built as shown in Fig. 6(a) Its dimension was
280.5 × 297 × 196.3 mm. It could be installed in a modified Little Anne (Laerdal Medical, Norway) CPR training
manikin (Fig. 6(b)) by removing the inner center post for the
spring to be inserted.
A control system and program for motor control was
made. The servo motors utilized for stiffness control were
programmed to rotate in increments of five degrees and they
were controlled with a devised program as shown in Fig. 5.
Stepper motors for damping were programmed to regulate the
rate of cross-sectional area of the airway in 10% increments.
B. PERFORMANCE TEST
1) COMPRESSION TEST
Figs. 7(a) and 7(b) show force-displacement curves of varying damping with fixed stiffness conditions. As the rate
of opening area of valves increased (damping decreases),
the area between compression and release curves became
smaller. However, the mean slope of the curves remained
almost constant. This means that energy dissipation due to
damping is well implemented in the system.
A result of varying the stiffness with a fixed damping
condition is shown in Fig. 7(c). Since the damping was
constant, areas between the compression and recoil curves
remained constant while the slope of curves increased with
stiffness.
These results show that the system can simulate a range of
non-linear mechanical characteristics by regulating damping
and stiffness independently.
2) MECHANICAL CHARACTERISTIC ANALYSIS
Stiffness and damping coefficients according to compression
depth calculated from compression test data set (88 cases) are
presented in Figs. 7(d) and 7(e).
The damping exhibited a nonlinear characteristic along the
compression depth. This characteristic was believed to be due
to the compression waveform. Given that the compression
waveform was trapezoidal, the velocity of compression at
the depths below 1 cm, and over 4 cm changed rapidly.
It was assumed that the damping of the system was adequately
presented in the constant velocity region between 1 and 4 cm.
Therefore, damping values within the depth range of 1 to 4 cm
were determined and plotted.
The value of damping at 30 mm depth ranged from
0.127 N·s/m to 0.511 N·s/m. The value of stiffness at maximum depth ranged from 5.34 to 13.59 N/mm. As reported
in previous study [16], the stiffness at a depth of 50mm and
the damping at a depth of 30 mm was between 4 N/mm
and 10 N/mm, and 0.08 N·s/mm and 0.38 N·s/mm for
patients. Our system was able to represent most of these
ranges of stiffness and damping for patients, with the
exception of the lowest bound where the system can
express greater values of stiffness and damping than these
ranges.
3) STABILITY TEST
As shown in Fig. 7(f), the reaction force decreased as the
cyclic load was maintained for about 90 minutes. The final
number of cycles was 8884. From the initial to the 10th cycle,
the cycle-to-cycle force reduction was greater than 0.5 N and
the force decreased from 285 N to 250 N. The magnitude of
reduction subsequently decreased, reaching less than 0.01 N
from approximately the 500th cycle. This value was notably
small. Therefore, the 500th cycle was set as the point at which
the force started to stabilize. From that point to the last cycle,
the reaction force decreased from 248 N to 235 N, presenting
a 5 % reduction.
IV. DISCUSSION
The human chest can be represented by mechanical properties such as stiffness and damping, which can vary with
age, gender, and body weight. However, limited mechanical properties of commercial manikins might not be able
to represent realistic human chest characteristics for CPR
training or research. Therefore, a system for CPR manikin
546
VOLUME 12, 2024

## Page 6

H. Lim et al.: Variable Stiffness and Damping Mechanism for CPR Manikin
FIGURE 6. (a) The complete system as built. (b) The system installed in Little Anne(Laerdal Medical, Norway) CPR manikin.
to simulate non-linear characteristic of a real human chest
was constructed. The proposed system can obtain various
mechanical characteristics by modulating the stiffness and
damping independently. The stiffness of the system can be
controlled in the range of measured human chest stiffness by
pre-stretching silicone bands. This approach represents a new
method for controlling stiffness that differs from the use of
springs in previous studies. Additionally, the system utilized
controllable dashpot dampers with valves that could allow the
system to express various damping characteristics to include
those of human chests presented in several studies [13],
[16], [21]. Various mechanical characteristics can be achieved
to mimic the human chests by modulating the stiffness
and damping independently. A stability test was conducted
to determine whether the stiffness of the newly proposed
band-based stiffness control system remained the same during repetitive compressions Results revealed that, the system
showed enough stability even after 8,000 cyclic loads. Damping of the system was largely determined by the opening area
of the valve. Therefore, damping was rarely changed over the
prolonged compressions. The initial rapid change of stiffness
was likely due to Mullin’s effect, a phenomenon where an initial stress is applied to an elastic material and then less stress
is appeared for the same strain [22]. After approximately
8,000 cycles, the reaction force underwent a change of only
0.1% over subsequent cycles. This relatively minor alteration
was difficult to discern. Therefore, the stiffness and damping
will be nearly identical for each user after the completion of
8,000 cycles of pre-compression.
The system has some advantages over commercial
manikins and previous studies on CPR manikin. First, the
system can represent various non-linear characteristic of a
human chest and hysteresis resulting from damping without replacing any parts. Desired mechanical property can
be achieved only by controlling motors of the system with
control software.
Secondly, it is the only system that can control both
damping and stiffness independently so far. The system can
simulate numerous cases by combining the damping and the
stiffness parameters while the others can mimic few cases by
changing only stiffness or damping.
These advantages can improve CPR training by providing
trainee with experience of chest compression similar to real
human chest and widening scenarios of training with a variety
of chest properties. Besides for training, this system can be
used for validating performances of CPR devices currently
under development, owing to its capability to simulate diverse
mechanical properties of the chest. Additionally, this system
holds promise for facilitating research aimed at determining
the optimal compression force and depth of CPR across
varying mechanical profiles of patients.
The system also has some limitations. First, the complexity and the weight of the system may reduce its usability.
Since the system includes six servo motors and three stepper
motors, many wires and peripherals are needed to actuate all
motors. Also, most parts of the system are made of aluminum
to ensure stability. As a result, the system weighs around 8 kg,
much heavier than commercial manikins. Also, the system
can be simpler if dedicated control board is used instead
of raspberry pi or motor drivers used for universal usage.
In addition, optimizing the structural design and materials can
lead to lighter system to be carried easily.
Although our proposed system has limitations in weight
and complexity, it has the advantage of being a system that
can simulate mechanical properties of the human chest by
adjusting various stiffness and damping that can advance CPR
training and research. For future studies, we plan to develop a
new control program to simulate various situations such as a
VOLUME 12, 2024
547

## Page 7

H. Lim et al.: Variable Stiffness and Damping Mechanism for CPR Manikin
FIGURE 7. Results of performance tests and mechanical characteristic analysis. (a) Force-displacement curves of the minimum stiffness condition
(180 degrees of spool rotation) with varying damping. As damping increases (valve opening rate goes to 0), the area between compression and
release curves becomes larger, which means that energy dissipation due to damping increases. (b) Force-displacement curves of the maximum
stiffness condition (480 degrees of spool rotation) with varying damping. Similar to (a), the area between compression and release curves
becomes larger as damping increases, which means that the energy dissipation due to damping increases. (c) Force-displacement curves of the
minimum damping condition (valve fully open) with varying stiffness. The slope of each stiffness case increases as the stiffness increases, while
the area between the compression and release curves remains almost constant. (d) Damping characteristics of the system. The amount of the
damping increases as the valve opening rate decreases, depending on the compression depth at the same time. (e) Stiffness characteristics of the
system. The stiffness increases as the spool rotation angle and compression depth increase. (f) Force – displacement curves of the entire cyclic
loadings during stability test. ①is the first cycle, and ②is the last cycle. Although the stiffness and hysteresis of the system decreased as the
loading repeated, from the 500th cycle to the last (8884th) cycle, the reaction force only decreased 5 %.
slanted angle of sternum in real human thorax and dislocation
or fracture of cartilage and rib during CPR. Additionally,
a qualitative study will be conducted with experts, including
clinicians, to evaluate how well the system can mimic the real
human chest.
V. CONCLUSION
We constructed a new system for CPR manikin to simulate mechanical properties of human chests using adjustable
damping and stiffness mechanisms. The system shows
non-linear mechanical characteristics due to viscous damping
like human chest under compression loadings. Such characteristics could be adjusted by controlling both stiffness and
damping. The system is capable of simulating a wide range of
stiffness and damping in the human chest. It has the potential
to be utilized in various CPR training and research for more
realistic results.
REFERENCES
[1] A. R. Panchal et al., ‘‘Part 3: Adult basic and advanced life support:
2020 American heart association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care,’’ Circulation, vol. 142, no. 2,
pp. S366–S468, Oct. 2020, doi: 10.1161/cir.0000000000000916.
[2] K. B. Kern, R. W. Hilwig, R. A. Berg, A. B. Sanders, and G. A. Ewy,
‘‘Importance of continuous chest compressions during cardiopulmonary
resuscitation,’’ Circulation, vol. 105, no. 5, pp. 645–649, Feb. 2002, doi:
10.1161/hc0502.102963.
[3] J. Christenson et al., ‘‘Chest compression fraction determines survival
in patients with out-of-hospital ventricular fibrillation,’’ Circulation,
vol. 120, no. 13, pp. 1241–1247, Sep. 2009, doi: 10.1161/circulationaha.109.852202.
[4] A. H. Idris et al., ‘‘Chest compression rates and survival following outof-hospital cardiac arrest,’’ Crit. Care Med., vol. 43, no. 4, pp. 840–848,
Apr. 2015, doi: 10.1097/ccm.0000000000000824.
[5] T. Vadeboncoeur et al., ‘‘Chest compression depth and survival in outof-hospital cardiac arrest,’’ Resuscitation, vol. 85, no. 2, pp. 182–188,
Feb. 2014, doi: 10.1016/j.resuscitation.2013.10.002.
[6] S. Duval et al., ‘‘Optimal combination of compression rate and depth
during cardiopulmonary resuscitation for functionally favorable survival,’’
JAMA Cardiol., vol. 4, no. 9, p. 900, Sep. 2019, doi: 10.1001/jamacardio.2019.2717.
548
VOLUME 12, 2024

## Page 8

H. Lim et al.: Variable Stiffness and Damping Mechanism for CPR Manikin
[7] I. N. Bankman, K. G. Gruben, H. R. Halperin, A. S. Popel, A. D. Guerci,
and J. E. Tsitlik, ‘‘Identification of dynamic mechanical parameters of the
human chest during manual cadiopulmonary resuscitation,’’ IEEE Trans.
Biomed. Eng., vol. 37, no. 2, pp. 211–217, 1990, doi: 10.1109/10.46262.
[8] B. K. Arbogast, R. M. Maltese, M. V. Nadkarni, A. P. Steen, and
B. J. Nysaether, ‘‘Anterior-posterior thoracic force-deflection characteristics measured during cardiopulmonary resuscitation: Comparison
to post-mortem human subject data,’’ Stapp Car Crash J., vol. 50,
pp. 131–145, Nov. 2006.
[9] S. M. Kang and S. W. Choi, ‘‘Monitoring mechanical impedance of the
thorax with compression and decompression cardiopulmonary resuscitation device,’’ J. Mech. Sci. Technol., vol. 33, no. 2, pp. 981–988, Feb. 2019,
doi: 10.1007/s12206-019-0155-y.
[10] J. M. Dean et al., ‘‘Age-related changes in chest geometry during cardiopulmonary resuscitation,’’ J. Appl. Physiol., vol. 62, no. 6, pp. 2212–2219,
Jun. 1987, doi: 10.1152/jappl.1987.62.6.2212.
[11] H.-Y. Choi and D.-S. Kwak, ‘‘Morphologic characteristics of Korean
elderly rib,’’ J. Automot. Saf. Energy, vol. 2, no. 2, p. 122, 2011.
[12] C. Pezowicz and M. Głowacki, ‘‘The mechanical properties of human ribs
in young adult,’’ Acta Bioeng. Biomech., vol. 14, no. 2, pp. 53–60, 2012,
doi: 10.5277/abb120207.
[13] S. Ruiz de Gauna et al., ‘‘Characterization of mechanical properties of
adult chests during pre-hospital manual chest compressions through a simple viscoelastic model,’’ Comput. Methods Programs Biomed., vol. 242,
Dec. 2023, Art. no. 107847, doi: 10.1016/j.cmpb.2023.107847.
[14] S. Beger et al., ‘‘Chest compression release velocity factors during outof-hospital cardiac resuscitation,’’ Resuscitation, vol. 145, pp. 37–42,
Dec. 2019, doi: 10.1016/j.resuscitation.2019.09.024.
[15] J. K. Russell, M. Leturiondo, D. M. González-Otero, J. J. Gutiérrez,
M. R. Daya, and S. R. de Gauna, ‘‘Chest compression release
and
recoil
dynamics
in
prolonged
manual
cardiopulmonary
resuscitation,’’ Resuscitation, vol. 167, pp. 180–187, Oct. 2021, doi:
10.1016/j.resuscitation.2021.08.036.
[16] J. B. Nysaether, E. Dorph, I. Rafoss, and P. A. Steen, ‘‘Manikins with
human-like chest properties—A new tool for chest compression research,’’
IEEE Trans. Biomed. Eng., vol. 55, no. 11, pp. 2643–2650, Nov. 2008, doi:
10.1109/TBME.2008.2001289.
[17] A. A. Stanley, S. K. Healey, M. R. Maltese, and K. J. Kuchenbecker,
‘‘Recreating the feel of the human chest in a CPR manikin via
programmable pneumatic damping,’’ in Proc. IEEE Haptics Symp.
(HAPTICS),
Mar.
2012,
pp. 37–44,
doi:
10.1109/HAPTIC.2012.
6183767.
[18] S. Eichhorn et al., ‘‘Development and validation of an improved
mechanical thorax for simulating cardiopulmonary resuscitation with
adjustable chest stiffness and simulated blood flow,’’ Med. Eng.
Phys., vol. 43, pp. 64–70, May 2017, doi: 10.1016/j.medengphy.2017.
02.005.
[19] K.
Kanakapriya
and
M.
Manivannan,
‘‘CPR
module
with
variable
chest
stiffness
in
high
fidelity
mannequins,’’
in
Proc.
CIRP
Design,
2013,
pp. 159–167,
doi:
10.1007/978-1-44714507-3_16.
[20] M. Thielen, R. Joshi, F. Delbressine, S. Bambang Oetomo, and L. Feijs,
‘‘An innovative design for cardiopulmonary resuscitation manikins based
on a human-like thorax and embedded flow sensors,’’ Proc. Inst. Mech.
Eng., H, J. Eng. Med., vol. 231, no. 3, pp. 243–249, Mar. 2017, doi:
10.1177/0954411917691555.
[21] A. Neurauter et al., ‘‘Comparison of mechanical characteristics of
the human and porcine chest during cardiopulmonary resuscitation,’’
Resuscitation,
vol.
80,
no.
4,
pp. 463–469,
Apr.
2009,
doi:
10.1016/j.resuscitation.2008.12.014.
[22] J. Diani, B. Fayolle, and P. Gilormini, ‘‘A review on the mullins
effect,’’ Eur. Polym. J., vol. 45, no. 3, pp. 601–612, Mar. 2009, doi:
10.1016/j.eurpolymj.2008.11.017.
VOLUME 12, 2024
549
