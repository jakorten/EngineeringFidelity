# McGraw-Hill-Cardiorespiratory-OCR

## Page 1

; 7
MODELING and SIMULATION
IN BIOMEDICAL ENGINEERING
Applications in
Cardiorespiratory Physiology
Willem van Meurs

## Page 2

Contents at a Glance
TWUOCMCHOR, 205 1mes coms news ea pens ewe Heme Cem « 1
Theory
Model Requirements ........
0.0... cece cece eee 17
Conceptual Models... 0.0.0...
cece cee eesme ioe 31
Mathematical Models .........
0... cence eee ones 45
Software Implementation .........
60. e seen eee 81
Simulation Results and Model Validation ........ 95
Applications
A Model of the Cardiorespiratory System ....... 107
Cineulation, sane ase gm 7 am + sok age 2 me 3 ome 3 Re 415
Respiration cess sews es 4 oes cease Wes vows» ewG st 133
Virgstologie Control sexs s ne. sues wea s oa 5 een wes 155
Advanced Topics
Sensitivity Analysis of a Cardiovascular Model .. 169
lesign of Model-Driven Acute Care
‘Ivaining Simulators ........
2... c eee eee ee 175
WS «age See tees Sete: Set eee now ee F Stes oe oe 187

## Page 3

Part! Theory
Contents
Foreword 6... cece
teen nes XV
PERS oussanenanaconesesaedbvededusnusseease xvii
Acknowledgments ow... eee
ee eee nee X1x
| Introduction ...... TTT TTITTTTT TTT civeneund
es ee |
1.1 Signalsand Systems .................. Prrrre 3
1.2 System Properties .................0.,. ae 5
ES a) MIEN) ca eceovsesneaesawveaaes 5
Continuous-lIime and Discrete-Time ..... 5
Staticand Dynamic ................--.- 6
Linearand Nonlinear .................. 6
Time-Invariant and Time-Variant ........ 6
1.3 Modeling and Simulation ................... 7
14 Applications in Biomedical Engineering ..... 10
1.5 Symbolic Notation ...........
0... cece ee. 11
Review Problems ..... 0.0...
ce cece eee ee 9
References and Further Reading ............ 12
2 Model Requirements ................. sPeeccess 17
2.1 Qualitative Aspects ........
2. eee eee ee 19
= Quantitative ASPECIS 1. c.cneaeuraeueonavace a
2.3 Implementation and Interfacing ............ 24
Model Code Implementation’ ........... 24
Interfacing ....... 2... eee eee eee 24
General Program Requirements ........ ae
“1 ‘Target Response Data...
eee ee ee ee 7
evi Preble nena penemase
eure beeeane 28
Keferences and Further Reading ............ ae
4 Conceptual Models ........ TOUTTITTTEIT Tree 31
ND Block Diagrams oo. eee 34
S20 Component Diagrams... 0.000 ea 30

## Page 4

Part {Applications
VURIGATR
3.3 General Observations on Conception) Mocdel
Review Problems ......
References and Further Readiny,
4 Mathematical Models ..........
0... - cece eee eeee
41 A Model of Two Physical Systems ...........
4.2 State Variable Models ............ 00.00.0405.
4.3 Units and Numerical Values ................
44 Direct Representation of Fluid Circuits ......
45 Direct Representation of Gas Uptake
ANGDIStHbULOR, = vane wien nappy dep ete 2 EER |
4.6 Direct Representation of Simple Transfers
in the Nervous System... 0... 0. cece cece ee
4.7 Electrical Analogs and State Variable
Models of Circuits 0... eee eee
4.8 General Observations on Mathematical
Models and Parameter Estimation ...........
ROVE PRONG na + wis + mas yes owe Bem
References and Further Reading ............
5 Software Implementation .............02
00 eee
5.1 Discretization of the Continuous-Time
SIRISBQUSHON: ig coun sume anes een come Sm 22
5.2. Basic Algorithms for Implementation of the
Discrete-Time State Variable Model ..........
5.3 Model Code Verification .............00000e
54 Connecting State Variable Models ...........
a ee ee ee ee ee
References and Further Reading ............
6 Simulation Results and Model Validation ........
6.1 Definitions and Overall Procedure ..........
6.2 Quantitative and Qualitative Methods for
Establishing Accuracy ...........0.000005.
6.3 Range of Validity, Target Data, and
Experimental Conditions ...............4.
Review Problems... 1.0.6...
0. cence ences
7 A Model of the Cardiorespiratory System .......
71 Model Requirements ...................-.
5e.
84
86
87
2
iS]
94
95
97
100
102
103
103
ti
Part il
To ConeepitlMadel eee (1)
Rederence and Purther Reading 00.0... 0000. 13
CUCU a ccc cena cee etter oon wae mene y 115
KL Model Requirements 0........0000
0c ee 117
K' Conceptual Models. 2.0... 119
KV Mathematical Models... 00.00.0000.
0. cee 22:
References and Further Reading ........... 131
ISGAPUTALIGH — s.cus ceva. sener sores sion peep sere eee te 133
“1 Model Requirements .......... 00.00. 0c ee 135
“2 Multiple Models oo... cece
cee aes 137
"Conceptual Models... 6.0... eee eee 141
“4 Mathematical Models ..........0......004. 145
References and Further Reading ........... 154
Physiologic Control... ............
ccc cee eee ee 155
10.1 Model Requirements ..........00..0000005 158
10.2 Conceptual Models o.oo... eee 160
10.3 Mathematical Models ..........0.00.0000045 162
References and Further Reading ........... 166
Advanced Topics
Sensitivity Analysis 169
{Lf Method .....:ee
ee ee ee 171
11.2. Application toa Hemodynamic Model ....,. 172
References and Further Reading ........... 174
Design of Model-Driven Acute Care
Training Simulators 2.2.0.0...
0.000. cee eee es 175
I2.1 Training Program Design ................. 178
12.2 Simulator Design ............0
000. cece eee 180
12.3 Model Requirements ........0.
0c. cece eee 182
References and Further Reading ........... 185
ides ae sense caus gemwmeg AA ERR TE eiecunser cain 187

## Page 5

CHAPTER 1
Introduction

## Page 6

11
vocabulary underlying modeling and simulation. Signals are
defined and used to distinguish systems from their environment.
System properties that play an important role in selecting mathematical formalisms for system modeling, analysis, and simulation are
presented. Modeling and simulation are powerful ways of studying
systems when direct interaction with the actual system is limited or
undesirable. Empirical models can be used to represent input-output
behavior. If we also want to represent internal system structure and
functioning, an explanatory model is required. Depending on our
interest in past or future system behavior, descriptive or predictive
models are used. Two examples of modeling and simulation in
hiomedical engineering are presented. A brief introduction of the
symbolic notation used in this book concludes the chapter.
[: this chapter we review or introduce the. basic concepts and
Signals and Systems
Physical, biological, and social phenomena can be described as events
or processes. Events are characterized by occurrence and time of
oveurrence. Breaking a bone, for example, is an event. Processes involve
more gradually evolving entities such as time, length, and temperature.
I‘racture healing is an example of a process. We can use our own senses
to evaluate an entity, for example, temperature as hot or cold, or use a
Measurement instrument, which, in combination with a unit and a
scaly, transforms the entity into a quantity with a specific value. For
exumple, the body temperature of this person (quantity) is 36.5 (value)
“ (unil), A constant is a quantity that has a specific fixed value. For
esample, Avogadro's constant is equal to 6,02 x 10 mol”. A variable is
«quantity that may assume any one of a specified set of values. A
continuous variable (CV) can take on an—in principle—infinite
number of values ina finite interval, whereas a discrete variable (DV)
vin only take on a finite number of specific values in a finite interval.
‘These value may be equidistant or nol, A special case of a discrete
variable is a binary varlable, which only taker on the values 0 and 1. A
Variable can take on valuew ax function of, for example, Hime or apace,
A Ume dependent variable ia often called a signal, even if no mennages

## Page 7

4
Introduction
are transmitted. The time variable can also be continuous or discrete,
leading to continuous-time (CT) and discrete-time (DT) signals,
respectively. Figure 1.1 shows several types of signals and common
conversions between them. Familiar, but not always rigorously defined
designations are included between brackets.
In many phenomena we can distinguish structured ensembles of
objects’ joined in regular interaction or systems. A system can be
natural or manmade and can be further delineated and described in
terms of the signals or variables via which it interacts with the
environment. A variable from the environment that influences the
evolution of a system is called an independent or input variable. We
sometimes distinguish control inputs and disturbances, depending
on whether these independent variables are under our control or not.
Disturbances can be measurable or not. Any dependent system variable
that we are interested in constitutes an output variable, whether it
influences the environment or not. A system and its input and output
variables can be represented in a block diagram (Fig. 1.2).
cM4 (Sequence, time series) (Digital signal)
om DAC cr di
Hs 2
A = —>»
| ADC
DT
Reconstruction | Sampling
ev {Analog signal) by
Acr
Ficure 1.1 Signals and common conversions. ADC, analog to digital
conversion, involving quantization; DAC, digital to analog conversion. See main
text for other abbreviations.
Input variable(s} ——»| System f—> Output variable(s)
Fiaure 1.2 System block dlagram.
* We will Juni our consideration of autonomous subjedia te human machine intertaces,
Introduction
For example, if we consider a car as the system, then the positions
of the accelerator and the steering wheel are control inputs, and the
position of the car is an output variable. But we could also be
interested in its speed and acceleration, or the fuel level, which would
then be added to the list of output variables. For a more precise
description, we would have to take into account the measurable
disturbance: wind velocity.
In this section, we defined a variable as a physical quantity that
may assume any one of a specified set of values, In subsequent
chapters, we will encounter the use of the same term to designate a
symbol in a mathematical formula representing a time-varying
physical quantity (Chap. 4), a symbol in software code representing a
variable or a (constant) parameter in an equation (Chap. 5), and a
symbol on the axis of a graph of simulation results (Chap. 6). These
are quite different concepts, yet their designation by a single term is
at the core of the modeling and simulation process. For example, we
can talk about the blood pressure in a graph of simulation results as
if it were the original physical quantity, “forgetting” the successive
abstractions between the physical phenomenon and the plot.
System Properties
Once we have defined a system and its boundaries, we can start
studying its properties. The first set of system properties are based
on input-output variables and play a role in selecting mathematical
formalisms for system modeling, analysis, and simulation.
SISO and MIMO
According to the number of input and output variables, we classify
systems as single-input, single-output (SISO), multiple-input,
multiple-output (MIMO) (Fig. 1.3), or combinations of those: SIMO
und MISO.
Continuous-Time and Discrete-Time
We classify systems as continuous-time or discrete-time according to
(heir input and output variables (Fig. 1.1). A system that has a mix of
continuous and discrete-time inputs and outputs is called a hybrid
uystem. Systems that involve events, rather than processes are often
——_——_
Input variable 1 ———p:
Input varlable 2 ——» System
Input variable @ ———p
p—ea Output variable
Fausi.8 brook dlagram of a MI@O

## Page 8

called discrete-event aystentn (Law, 2000; Cammandran, 2008), In thix
book we will focus on modeling and simulation of process type
systems.
A second set of system properties is based on aystem behavior,
and once established, plays a primary role in predicting that behavior.
These properties also play a rolein selecting mathematical formalisms
for system modeling, analysis, and simulation. In the definitions
below y(f) is the output or response of the system at rest to the input
u(t). We will limit ourselves to causal systems, for which y(t,), the
output at a specific time t,, depends only on the past or present input:
u(t) with ¢ <t,, for all u(f) and ¢,. This introductory text is also limited
to deterministic systems for which future outputs are completely
determined by the current state of the system and future inputs?
Static and Dynamic
If for all inputs and times £, the output of a system at time t depends
on the input at time f only (and not on the input at any other time) we
call the system static. If not, we call the system dynamic (Fig. 1.4).
Linear and Nonlinear
Let C be a constant. If the response of the system to the input C*u() is
C*y() for all u() and C, we call the system homogeneous. Let y,(#) be
the response to input w,(#) and y,(#) the response to the input u,(é). If
the response of the system at rest to the input 4,2) + u,@ is y,Q +y(
for all u,(/) and u,(1), we call the system additive. A system that is both
homogeneous and additive is called linear (L). If not, the system is
nonlinear (NL) (Fig. 1.5).
Time-Invariant and Time-Variant
The input u(t) delayed by a time t = i,is ut ~ ¢,). If the response to
u(t ~ t,) is y(t -t,) for all u(f) and i, the system is time-invariant (TI), if
not it is time-variant (TV) (Fig. 1.6).
Ficure 1.4 Response of a dynamic system.
? Note that we frequently encounter deterasinistle systema, kuch as filters, processing
random signals.
u(t) y(t)
J, t lm t
2u LSy(t)
System ——pe
Fiaure 1.5 Responses of a noniinear system.
u(t) y(t)
Ji, t — t
u(t-tg) —>| System p—> 0.5y{t-to)
tna.
to
Systems may be LTI for a subset of inputs, for example, over a
certain amplitude range of the input variable(s), or for a limited
time. Modeling techniques such as the impulse response and
transfer function [see for example Roberts (2003)] are well suited for
analysis and design of SISO, LTI systems. But to use these techniques,
the input variable needs to be known beforehand, sometimes even
in a specific analytical form. This does not make their use very
convenient in real-time simulations. Moreover, many physiological
systems are MIMO, NL, and TV. In Chap. 4, we will introduce a
mathematical description that applies to modeling and simulation
of this broader category of systems. This introductory text is limited
to finite dimensional dynamic systems that can be described by
differential equations or difference equations as opposed to systems
that are described by partial differential equations.
1,,
to
Figure 1.6 Responses of a time-variant system.
1.3
Modeling and Simulation
There are various ways to study a system [also see Law (2000)]. “To
study” is used here in a broad sense, including gaining a better
understanding, system optimization, and training in use or operation.
Experimenting with the actual system is acceptable if nobody will get

## Page 9

Introduotion
hurt, or if no significant damage is caused if we make a mistake. It is
generally not acceptable if the real system is, for example, a nuclear
power plant, an airplane, or a patient. In those cases we construct a
model? For some systems and experiments, we may be able to
construct a physical model, for example, an anatomical model to train
needle insertion. For other systems, physical models may be difficult
and expensive to construct. Physical models are also difficult to adapt
to different situations. In those cases, and if the envisioned application
is served by it, we may be able to construct a mathematical model, that
is, a mathematical representation of the relationships between system
variables that are of interest to us. A “good” mathematical model
contains a lot of information about the system, but to use it to study
system behavior, we need either an analytical solution, or, if that is not
available, a software implementation and a simulation. Before
selecting or designing a mathematical model for the response of a
dynamic system to an input; two fundamental questions about our
interest in the behavior of the system should be asked:
1. Are we merely interested in externally observable behavior,
or do we want to understand internal structure and
functioning?
The answer to this question determines the type of model at a very
basic conceptual level: An interest in internal functioning requires
an explanatory, white-box, or knowledge-based model that reflects
the structure and functioning of the underlying system (down to a
certain depth). An interest limited to external aspects of system
behavior may be served effectively and efficiently by an empirical or
black-box model, reflecting only essential aspects of response
dynamics.
A second fundamental question is:
2. Are we interested in past, present, or future system
behavior?
The answer to this question may also influence the type of a model,
especially its mathematical formulation, which may reflect a
descriptive, real time, or predictive use, even if the underlying
conceptual model is the same. Figure 1.7 summarizes these interests
and associated model types and uses.
A third, somewhat less fundamental question, but of particular
importance in biology and medicine, is if we are interested in the
behavior of one or more particular individuals, or in typical behavior
for a class or population. The answer to this question may also
influence the choice of conceptual or mathematical model, and has
an impact on the associated parameter estimation procedure.
3 In Chapter 6 we will come back to the use of animal models.
(a) fixterna! {b) Umpirieal
Paat Future Dosorlptive Pradiotive
Internal Explanatory
Fiaure 1.7 Interest in system behavior (a) and model type and use (b).
For example, based on data for the planet Mars gathered by ‘lychu
Brahe (1546-1601), Johannes Kepler (1571-1630) formulated empirical
laws that turned out to apply to the movements of all visible planety
in the solar system. The first two are:
1. All planets move in elliptical orbits, with the Sun at one
focus.
2. A line that connects a planet to the Sun sweeps out equal
areas in the plane of the planet's orbit in equal times (Halliday,
2001).
These were first used to describe past movement, and then ly
predict future planetary motion. Isaac Newton (1643~1727) was ably
to provide an explanatory model for the same phenomena, based on
his law of universal gravitation and his laws of motion. Alber|
Einstein (1879-1955) provided an alternative explanatory moddl,
based. on general relativity and the curvature of space under thy
influence of the mass of the Sun.
The distinctions in response to the above questions are generally
not binary oppositions, but may involve several levels. For example,
the deepest level of representation of an explanatory model of an
organism may include systems such as the cardiovascular ani
respiratory.systems and corresponding organs, or it may go further
and represent tissues, cells, molecules, atoms, etc. Many models used
in biomedical engineering are “gray-box” models and combine some
level of representation of internal structure and function with
empirical, black-box models based exclusively on input-output data,
Another example of levels on the axes of Fig. 1.7 is that meteorological
and climate models involve similar variables, but descriptions and
predictions involve very different time scales. A physical model is
also a system, and stretching the meaning of the word “objects” in
the definition ec. 1.1) a bit, we can even consider a mathematical
model a system. Therefore, the system properties introduced in See.
1.2 can also be used to further describe models. For example, we can
talk about an explanatory deterministic MIMO model
cardiorespiratory dynamics.

## Page 10

1.4 Applications in Biomedical Engineering
Areas in medicine that benefit from modeling and simulation include
research, therapy, training, equipment design, and control of devices
Many types of models are used to represent a multitude of
physiological systems in very diverse simulation applications. The
purpose of this section is to present two examples, rather than to give
a systematic review. We will use the terminology introduced in this
chapter. SA Couto et al. (2010) presented a model for use in a training
simulator for obstetricians and neonatal intensive care physicians
(Fig. 1.8).
The changes in the circulation during and shortly after birth are
complex and quite spectacular: Perfusion of the lungs goes from
almost nothing to the full cardiac output, the placental circulation is
removed, and the ductus arteriosus, a communication between the
pulmonary and systemic circulation, necessary for intrauterine life,
but potentially fatal to a newborn, closes. Figure 1.9 shows some of
the input and output variables of the continuous-time dynamic
model representing these hemodynamic phenomena.
The input variables of this MIMO model are set by a discrete
event system. A gray-box model explicitly reflects several of the
Ficure 1.8 Prototype delivery simulator. (Picture Dr. Luisa Bastos.)
pee
Umbilical cord resistance ———»|
Lung perfusion
Pulmonary vascular resistance ——>| Wiodel ,
+——» Ductus arteriosus flow rate
Ductus arteriosus resistance ——
Ficure 1.9 Block diagram of a model for educational simulation of
hemodynamic transitions at birth,
1,5
anatomical structures ineluced in the tetalneonatal cireulation, such
ae the umbilical cord and the ductus The system and
mathematical model contain several nonlinearities, for example
those resulting from the cardiac valves, The envisioned model use is
real time (neither descriptive nor predictive, Fig. 1.7), and the patient
population considered in the article is an average, normal, term
fetus,
Intracranial pressure (ICP) is an important variable in the
intensive care unit. Increased ICP can result in compression of blood
vessels and impede perfusion and oxygenation of the brain. ICP
depends on multiple factors, including cerebrospinal fluid dynamics,
intracranial compliance, and cerebral hemodynamics. Ursino et al.
(1995) presented a mathematical model for the ICP response to a
typical clinical test: injection and withdrawal of a few milliliters of
saline in the craniospinal space. The primary goal of this continuoustime mathematical model is to understand and explain the complex
ICP dynamics. Work carried out using Ursino’s publication targets
therapeutic and educational applications.
Hardman and Ross (2006) conclude that modeling and simulation
are now a stand-alone methodology of similar value to laboratory
investigations and clinical trials. The purpose of Part I of this book is
to introduce the reader to the modeling and simulation process and
to the basic techniques required to implement it, but first we present
symbolic notation.
on snienttsorennee
eadnninn SAiieaeinivan tea SE Ce
Symbolic Notation
In a text spanning the clinical world, physiology, physics, chemistry,
mathematics, anc computer engineering, it is impossible to define a
standard symbolic notation for involved quantities that is accepted
by all. We propose to optimize notation from an educational, modelbuilding perspective, and retain the following conventions:
e Froma mathematical perspective, continuous time is denoted
by #, and discrete time by 1. We distinguish variables from
(constant) parameters by using lower case and capitals,
respectively, and by explicitly including time dependency,
for example, flow rate f(#), resistance R.
° From the perspective of physics, we use the same symbol for
the same quantity. For example, volume, pressure, and flow
rate will be designated by v(t), p(}), and f(), respectively.
e From an anatomo-physiological perspective, we use
subscripts to designate a particular location or process. For
example, the blood pressure in the aorta is designated by
P(t). When considering both a gas and a blood phase, we use
capital subscripts for gases, and lower case subscripts for

## Page 11

blood, ane append a particular gas i necessary, Vor example
the partial pressures of oxygen in alveolar gas and arterial
blood are designated by p,O,(t), and p.O,(), respectively,
We recommend keeping symbols meaningful, consistent, anc
compact. For critical model quantities, such as input and output
variables, it is often useful to establish a table including full variable
names, symbols, and units. This notation follows several, but not all,
of the conventions of a frequently used standard in cardiorespiratory
physiology (Nunn, 1993). For example, the primary symbol in our
notation represents the physical quantity flow rate without
distinguishing between gas and blood.’ Units and their symbolic
notation will be introduced in Chap. 4.
Review Problems
11 Define the terms signal, system, model, and simulation.
1.2 Let y(/) be the output of a system at rest to the input w(). The graphs below
show two input-output pairs. Is the system nonlinear or time-variant?
u(t) y(t)
\
7 |
2u(t~to) ay System p——p 41.5y(t-to)
to wy t
Fieure 1.10 Graphs for review probiem 1.2.
1.3. Search the web for a mathematical model of ung mechanics. What are
the main input and output variables?
References and Further Reading
Cassandras CG, Lafortune S. Introduction to discrete event systems, 2°¢ ed. New York:
Springer; 2008.
Halliday D, Resnick R, Walker J. Fundamentals of physics. 6 ed. New York: John
Wiley & Sons; 2001.
Hardman JG, Ross JJ. Modelling: a core technique in anaesthesia and critical care
research. Br J Anaesth. 2006 Nov; 97(5):589-92.
4 The mentioned standard represents these quantities by Vand Q, respectively.
Law AM, Kelton WI). Simulation modeling and analyale, OY ed. Boston: MeGraw
PHIL 2000
Nunn JP, Nun's applied reapiratory physiology. 4" ed, Oxtord: Butterworth
Heinemann; 1993
Roberts MI, Signals and systems: Analysis of signals through linear systems. Boston:
MeGraw Fill; 2003,
fa Couto CD, Andriessen P, van Meurs WL, S4 Couto PM, Ayres-de-Campos D. A
model for educational simulation of hemodynamic transitions at birth, Pediatr
Kes, 2010; 67(2):158-165.
Ursino M, lezzi M, Stocchetti N. Intracranial pressure dynamics in patients with
acute brain damage: a critical analysis with the aid of a mathematical model
IEEE Trans Biomed Eng, 1995 Jun; 42(6):529--40.

## Page 12

PART
Theory
Chapter 2 Chapter5
Model Requirements Software Implementation
Chapter 3 Cuarten6
Conceptual Models Simulation Results and Model
Validati
Chapter 4 eenes
Mathematical Models

## Page 13

~ CHAPTER 2
Model
Requirements
U

## Page 14

chapter we introduce a stepwise approach to the modeling
simulation process and present the first step: How to set
jiivements for a model of the system under study. Qualitative
of model design include the input-output variables,
wr to be represented, structures and functions to be included,
He ype of model to be used. Quantitative aspects include ranges,
ony, and bandwidths of input and output variables. Additional
lrements address how a model needs to be implemented, and
pul and output variables need to be imteriaced to the
‘oiiment, Target response data play a central role in validation of
before its use to explore certain aspects of system behavior.
requirements presented in this chapter provide input to all
juent steps of the modeling and simulation process, and are
ther specified in an iterative manner (Fig. 2.1).
(he model development phase, all major steps are executed, up
iilation results and validation. One or more of the steps may be
dl, depending on the results of the validation. Other phases
Jollow and lead to further iterations, for example, validation by
spendent experts, comments by model users, expansion of the
ie|, ancl so on. Model requirements may evolve from one phase to
puther,
‘The novice modeler may want to read this key chapter twice: one
inmory initial consideration, followed by a second in-depth reading
»» (he concepts underlying the subsequent steps of the modeling
simulation process are assimilated.
jualitative Aspects
‘Jel requirements are often set in dialog with clinical investigators
+) hanle life scientists. At the onset of a modeling and simulation
jject It is usually clear which organ(s) or global physiological
win(y) will be considered. A modeler who does not have a
\jyound in these fields may first have to refresh his or her
1g

## Page 15

2. Model requirements
® 2.1 Qualitative aspects
{ 3. Conceptual models
|
» 2.2 Quantitative aspects ——————_——+
4, Mathematical models
> 2.3 Implemertation and interfacing
——» 5. Software implementation
!
Fieure 2.1 The modeling and simulation process.
knowledge of relevant physiology (Berne, 2004; Guyton, 2006), and
possibly of the health care environment, for example, via a visit to the
hospital guided by a clinician. Qualitative choices with potential
quantitative implications are those of the population, the physiological
state(s) of the subject, and the pathologies to be represented. The
population is specified in terms of species, age, gender, height, and
weight. A model may be designed for an (hypothetical) average
member of the selected population. The “population” may be a
specific individual, in which case the model should be designed so
that it is possible to estimate model parameters from available data.
A special physiological state that almost always requires simulation
is the normal resting state of a subject. Body position can be specified
as, for example, supine: lying down, face up. Other physiological
states are, for example, hypovolemia or hypoxemia. Examples of
pathologies are cardiac valve insufficiency and congenital
diaphragmatic hernia. The possibly dynamically evolving state of
the patient is observed via clinical signs and monitored variables.
Clinical signs, such as a palpable pulse, can be evaluated without
dedicated medical devices. Monitored variables, such as an invasive
blood pressure, do require medical devices for their measurement.
Clinical signs and monitored variables that need to be simulated
constitute the output variables of the model. Qualitative choices that
influence simulation dynamics are those of critical incidents and
interventions to be simulated. Examples of critical incidents are acute
blood ioss and pneumothorax. Interventions such as exercise or the
Vaisalva maneuver may be carried out by a healthy volunteer.
Therapeutic interventions such as chest compression or provision of
additions Geygen ean be carried out by a health care provider on
patients, Home interventions require mecical devices, others don't
An overall Hoek diagram with model input (independent) and model
output (pendent) variables can now be established (see Fig, 1.9 for
an example) Lf representation of internal structures and functions is
not requiled, and i sufficient input-output data are available, thena
black-boy Model may suffice, In its simplest form this model may
take the (orm Of a database or a set of look-up tables for the values of
the dependent variables, They may also take the form of difference
equation) OF Neural networks with parameters that are estimated
based on {ipul-output data (Ljung, 1999). Note that—in principle—
detailed physiological knowledge is not required to establish a blackbox model, li the remainder of this book we will focus on white-box
and grayhox models, For example, it is difficult to imagine that lung
perfusion
ane ductus arteriosus flow rate (Fig. 1.9) can be modeled as
a function Of all possible combinations of the continuous input
variables, merely based on input-output data and without
represeniiis, internal structures and functions. Therefore, we used 4
gray-box model, All previous choices may influence the internal
structure and functions to be incorporated. For example, to represent
fetal hemodynamics, specific structures that are not part of the
postpartum circulation, such as the umbilical cord and placenta,
need tobeineluded. Qualitativemodels requirements are summarized
in Table 2.1,
Many modeling and simulation projects require only setting a
subset of the requirements listed in Table 2.1. For example, not all
projects involve pathologies or critical incidents. Conversely,
requirements may have to be combined, for example, a critical
incident occurring in a patient with an underlying pathology. We
repeat the comment made in the introduction to this chapter that
model requirements may evolve depending on the phase of a
Organ or physiological system |
Population
Physiological states i
dh
2i
Ey
4, Pathologies
5,
6
Clinical signs and monitored variables
Critical incidents
Interventions
Overall block diagram
8.
9, Internal structures and functions (if applicable)
TaBLe 2.1 Qualitative Model Requirements

## Page 16

modeling and simulation project, Given that these requirement)
guide all subsequent steps of the modeling and simulation process,
they should be set with utmost care; adding, a eritical qualitative
requirement toward the end of the process may lead to invalidation
of much previous work.
The review problem at the end of this chapter provides detailed
examples of questions involved in specifying model requirements,
setting the stage for the first review problem in each of the subsequent
chapters of Part| of the book.
Based on the qualitative requirements we can continue the
modeling and simulation process (see Fig. 2.1) by designing a
corresponding conceptual model (Chap. 3). Alternatively, we can
complete the requirements as outlined in the subsequent sections,
before setting up a conceptual model. In our experience this second
approach provides more structure to the overall process.
Quantitative Aspects
In this section, we elaborate on one of the main qualitative
requirements—the model block diagram—and specify quantitative
aspects of input and output variables. These requirements and
observations will play a role in interface design and model code
implementation (Sec. 2.3 and Chap. 5) and in mathematical modeling
(Chap. 4). We also consider quantitative aspects of system behavior
that have to be included in the mathematical model. For the model
input and output variables we:
¢ Select a symbol, also see Sec. L5.
« Assign a unit and use it to specify typical ranges and
resolutions.
© Specify bandwidths.
Table 2.2 describes the input variables of the model of Fig. 1.9 in
more detail.
The resistances of the umbilical cord and ductus arteriosus (DA)
go to infinity on simulation of cord clamping and progressive closure
of the DA respectively. For that reason, we use conductance, the
inverse of resistance, instead. The electrical engineering symbol for
conductance is G. Because these are input variables, rather than
parameters, we use g(f). There are no such constraints on the
pulmonary vascular resistance. Subscripts indicate the three
anatomical structures. These variables are not routinely measured in
clinical practice, so we use units that are convenient for modeling
purposes right away. The range for the umbilical cord conductance
represents complete closure, and a typical term fetal value,
respectively (SA Couto, 2010). The resolution indicates that we want to
input
Symbol (ih Range | Resolution
variables Bandwidth |
Umbilical cord | 4,,(0 mmbkeimis' |} O0°027 | 0.04 | LHz |
conductance | | . |
Pulmonary | ri (t) jmmHgmlts | 2.0-12.0 | 0.4 | O.1 Hz
| |
Ductus & y(t) mm Hg* mis | 0-8.3 | 0.4 | 0.01 Hz
arteriosus \ | |
| conductance
Tasue 2.2 Input Variables of the Model for Educational Simulation of Hemodynamic
Transitions at Birth
be able to simulate incomplete and progressive closure of the
umbilical cord, for example, via partial compression of the cord by
the fetus, or partial clamping by the health care provider. Similar
considerations hold for the ranges and resolutions of the other two
input values. The bandwidth indicates that the umbilical cord
conductance can change rather rapidly, but we don’t expect the signa!
to have any frequency components above 1 Hz. The changes in
pulmonary vascular resistance take place over minutes, and the
changes in DA resistance over hours and days, which is reflected in
decreasing bandwidths.
Depending on the use of the model, it may be convenient to
specify input and output variables in clinical units and establish only
a consistent set of standard units, and convert variables to them, in
the mathematical modeling phase—see Chap. 4.
It will be clear from the above example that the ranges, resolution,
and bandwidth are indicative, rather than highly precise values.
They play a role in displaying and storing data, and can be further
specified if a simulator design requires it. Bandwidth is used here in
the sense that the variable or signal has no frequency components
outside that frequency range. Theoretically, we can reconstruct a
signal from its samples if the sampling frequency is at least twice the
bandwidth (in this sense). Note that this value is usually larger than
the -3 dB definition used in signal processing. The bandwidth of
input and output signals also gives an indication of system dynamics,
which is of particular importance if real time performance is required;
also see the next section and Chap. 5.
The intended use of the model for hemodynamic transitions at
birth is real time and predictive, rather than descriptive. For example,
trainees will be manipulating the position of the fetus, influencing
umbilical cord conductance, and observing the consequences, in real
time. The phenomena to be modeled are mainly continuous processes,

## Page 17

2.3 Implementation and Interfacing
so the basic mathematical model will be continuous-time, We have
already seen that the simulation requires a MIMO representation of
the system (Fig. 1.9). The cardiovascularsystem contains nonlinearities
such as unidirectional cardiac valves. These nonlinearities will most
likely become apparent in the relationship between input and output
variables. The main hemodynamic transitions at birth are represented
via the input variables. For the duration of a delivery simulation
exercise, the remaining hemodynamic system can be considered
time invariant.
Implementation of physical models, Sec. 1.3, involves electromechanical hardware and engineering design.1 Interfaces to the environment are often an integral part of a physical model. In this book we
will focus on mathematical models and implementation in software.
These models require interfaces that need to be explicitly designed.
We will consider requirements in the categories: model code
implementation, interfacing, and general program requirements. In
each one of these categories, requirements depend on the intended
model application and on the phase of model development and use.
Model Code implementation
General requirements for code implementation of a mathematical
model are that the equations are calculated in the correct order and
that a simple, accurate, and efficient numerical integration method is
used. Especially when coupling multiple dynamic models, the
sequence of equations is critical. In Chap. 5 we will present methods
that allow us to meet these requirements. Efficiency of code
implementation may be more important in final use than in the
design and validation phases, especially if real time or acceleratedtime performance is required.
Interfacing
An interface is a layer between a model and the environment that
processes input data from the environment and presents output data
to it. We further distinguish run-time and off-line interfaces.
Examples of simple interfaces are keyboard entry of a numerical
value, or a graph of simulation results. More elaborate interfaces
involve emulation of medical devices, such as a clinical monitor, to
enter or display data.
In the model development phase, interfaces should be flexible,
but don’t have to have a highly standardized form. We want to be
1! Which may include design via relatively low cost and flexible mathematical
prototyping.
i
able to initialize the model, change parameter values, sel inpul
variables, display output values in numerical or graphical displays,
and so on (Hig, . For model validation, including documentation
and scientific publication, data should be presented more carefully,
and an appropriate corresponding interface, including scales and
units that match the target data, should be chosen (Fig. 2.3). This can
be accomplished as an extension to the model development program
or off-line, based on saved data and using a specific graphing
program.*
ina research application or in a model development phase, it may
be perfectly acceptable, and even desirable, to “administer” fluid via
the keyboard, have the model execute 10 times faster than real time,
and present effects, for example, on blood pressure and heart rate, as
a graph at the end of a simulation run. In an immersive acute care
training simulation, however, the resulting differences with clinical
reality would greatly distract the trainees, and thereby most likely
reduce both the quality of learning and transfer of learned skills
from the simulated to the real environment. In such an application,
we would want to use real fluids, and automatically detect their
administration, run the model in real time, and present, for example,
heart rate continuously as a palpable pulse on a mannequin
(Fig. 2.4).
The success of such modeling and simulation projects often
stands or falls based on the quality of the interfaces. In the remainder
of this book, we will focus on software implementation of
WE ae
an
ye
cokia
Figure 2.2 Model development interface.

## Page 18

200
180
160
140
120
100
80
Pressure (in mm Hg)
60
40
20
Volume (in ml)
Figure 2.3 Model validation interface. (Adapted from Goodwin, 2004.)
Figure 2.4 Palpable pulse for acute care simulation. (Photo courtesy of
Medical Education Technologies, inc.)
mathematical models, Only in Chap, 12 will we briefly return to
interface design
General Program Requirements
General program requirements involve the choice of programming
language, the need for real-time or accelerated-time (“fast-forward”)
simulations, and specification of the global program flow. In our
opinion, an environment like Matlab (The MathWorks) is a good tool
for mathematical model design and validation because of the
relatively simple, direct implementation of equations, and its
interfacing capabilities. In the design phase, real time behavior is
often not a requirement, and for demonstrations approximate real
time behavior can easily be accomplished; see the next chapter. A
potential shortcoming is that Matlab allows for programming
without much preliminary reflection on an algorithm. In our
experience, the explicit formulation of an algorithm (see Chap. 5)
facilitates debugging, documentation, reuse, and sharing and
transferring of developed code. Visually oriented modeling and
simulation tools aliow for rapid prototyping, but address the
conceptual and mathematical modeling and code implementation
phases all at once, which can be confusing, and can jeopardize reuse
and transfer of code. If a model is incorporated in a simulator that
involves other functional units, for example, other models, user
interfaces, communication with hardware, then a more general highlevel programming language such as Java or C needs to be used. The
model algorithm needs to fit the overall program flow. True real-time
programming, ifrequired, isa highly specialized task for professional
software engineers. The modeler needs to verify that real time is
accomplished, and pay close attention to sequencing of model
equations, especially if closed-loop systems, which are potentially
sensitive to oscillations, are involved.
RR me EE On PTS RS SNM NNN AS
Target Response Data
Target data should be established for baseline simulation results and
for dynamic responses to changes in input variables. They may take
the form of tables or graphs of numerical data, or waveforms. These
data should not be used for parameter estimation, part of establishing
the mathematical model, also see Chap. 4. The target data should
match the modeled population, pathologies, and conditions as closely
as possible (also see Sec. 2.1). Population sizes, standard deviations,
and ranges should be reported whenever available. Table 2.3 shows
an example of target data for fetal hemodynamics from (Treitel, 1987)
as used in (SA Couto, 2010). :
2 In Chap. 6 we will come back to the use oftarget data from animal experiments.

## Page 19

LO iheory
i Flow rate, in% of combined |
| Anatomical structure ventricular output
| Right ventricle i
| Leftventricle |
| Ductus arteriosus
ica: cn
Pulmonary circulation
Foramen ovale |
Placenta
Note: Values expressed as mean + standard deviation, measurements in 16 term fetal lambs.
Taste 2.3 Example of Target Data
There are advantages to establishing target data at the onset, rather
than during or toward the end of a modeling and simulation project;
they provide concrete examples for how the model should respond in
a few specific cases. Additional target data may be needed wher
expanding the range of validity of the models, also see Chap. 6.
Review Problems
2.1 Clinical instructors want to develop a simulation-based class for
teaching hemodynamic? principles and monitoring. Their request is for a
simulator of acute hypotension (low arterial blood pressure) and tachycardia
(high heart rate) due to three different possible causes: (1) Low blood volume,
(2) decreased systemic vascular resistance, and (3) low myocardial contractility
(a weak heart). The goal is for trainees to interact with the simulator and make
a differential diagnosis of the underlying cause. To be able to do so, they
need access to other monitored hemodynamic variables besides arterial blood
pressure and heart rate
© Refresh your knowledge of relevant physiology. Gather background
information on how central venous pressure and cardiac output are
measured and on how the three causes for hypotension influence
these hemodynamic variables.
The clinical instructors further specify that they would like to manipulate
the severity of the underlying causes of hypotension, and that these causes
can appear in combination. The simulated arterial blood pressure signal
should be available as a noninvasive reading of systolic and diastolic blood
3 Hemodynamic is defined as pertaining
to the (uid dynanien af blood in the cardiovas
References and Further Reading
Mode! Requirements
pressures, and on request, take the form of a
L : pulsatile continuous-ti i
corresponding to an invasive measurement. ilies
© Select model input-output variables and establish a block diagram.
It is unlikely that there are enough input-
— a black-box model for this MIMO system. Moreover, manipulati
© model to reflect different clinical conditions and ae different
patients is almost impossible in a black-box m i i
structure reflecting anatomy and physiology. a
output data on human subjects to
ew i
hich structures and functions need to be incorporated in the
hypotensi —atri i
: yp ierision, model atria, ventricles, systemic circulation pulmonary circulation, baroreflex, chemoreflex, or other? ‘
The ins i
nstructors would like to be able to simulate other patients and
conditions in the future, but for now are satisfied with a single, representative
ingle, represent “
* Speci . a
+ as i ss taking into considerations educational objec-
, for example, a typical hospital po i
; pulation, and access to d
estimate model parameters and validate its response. “ees
Other model requirements will be a
odie ddressed in subsequent review
conan
Berne RM, Levy MN, Koe
: Paildephe Aes eppen BM, Stanton BA, eds., Physiology. 5th ed.
eaeis fan Meute WE, me CD, Beneken JEW, Graves SA. A model
ion of i i ar physi F
. 2004 Deo oo(etees
ct infant cardiovascular physiology. Anest Analg
uyton AC, Hall JE. Textbook i i
, ce ae ook of medical physiology. 1th ed. Philadelphia: W.B.
Ljung L. System identification, theory for the 5
ioe ee Hie ion, theory for the user, 2° ed. Upper Saddle River, NJ:
Couto CD, Andriessen P, van Meurs WL, S4 Couto PM Ayres-de-Campos D.
A model for educational si i
os Psi Re ee oe en of hemodynamic transitions at birth.
eitel DE, Iwamoto HS, Rudolph AM. Eff i
blood flow patterns. Pediat? Res. 1987; LS ———

## Page 20

CHAPTER 3
Conceptual Models

## Page 21

f we need a model with an internal structure and processes we
can understand, manipulate, and possibly expand, then it is
convenient to specify these qualitative aspects first, before we
formalize them and add quantitative aspects in a mathematical
model. This step in the modeling process is accomplished via a
conceptual model. In this chapter we introduce two predominantly
visual representations of internal system structure and function:
block diagrams and component diagrams.
In the previous chapter, we specified what we require from a
model in terms of input-output behavior and in terms of structures
and processes that need to be included. Our goal is to get to a
mathematical model that meets these requirements, which can then
be transformed into computer code and used to obtain simulation
results. We can now carry out a literature search to see if an existing
model meets all our requirements. If this is the case, we canimplement
a mathematical model in code or a physical model in hardware. In
many cases, however, published models only partially meet our
requirements. In such cases they need to be adapted or combined. If
no model can be found, a completely new model needs to be designed.
If we are satisfied with an empirical model, then we can choose the
type and order of a mathematical model, for example, a second-order
linear ordinary differential equation or a neural network, and
parameter estimation completes the modeling process. Note that
sufficient input-output data should be available to estimate the
parameters of sucha model. If, on the contrary, weneed an explanatory
model we need to set up a conceptual model that reflects the internal
structure of the system in terms of subsystems and networks of
idealized system components. That is relatively straightforward for
manmade engineering systems, which are often designed that way.
Physiological systems, however, frequently do not have clearly
distinguishable subsystems, and do not consist of close-to-ideal
components in a simple network. Yet, engineering-type analytical
techniques can be used as an intermediate step between model
requirements and explanatory mathematical.-models. The involved
simplifications constitute a delicate balancing act: too few
simplifications, and the model may take too long to establish, it may
33

## Page 22

oF
3.1
be difficult to maintain, and its software inplementation may run
too slow for the envisioned application; too many simplifications
and the model may not have a realistic response in all required
situations.
Block Diagrams
Let us assume we want to set up a basic model of the normal
cardiorespiratory system. Following the steps listed in Table 2.1, we
turn to the standard physiology text books for background
information on the cardiorespiratory system. We specifically want to
study the effect of oxygen metabolism in body tissues on spontaneous
breathing and systemic arterial and venous blood gases, leading
to the input and output variables reflected in the block diagram
(Fig. 3.1).
We further specify that the model should include spontaneously
breathing lungs, distribution of respiratory gases by the circulation,
metabolism in body tissues, and control of breathing, which
maintains arterial blood gases at appropriate values by adjusting
respiratory muscle activity. An intuitive graphical representation of
these structures and processes is included in Fig. 3.2.
Spontaneous
one lism Cardiorespiratory [-—TM breathing
m lis!
sysiem Lp Arterial and
| __ venous blood
gases
Ficure 3.1 Block diagram for a basic model of the cardiorespiratory system.
| Ventilation
~—
Control of
“Sioa
/
[ /
\
4 Circulation y
\ dy tissues
KY Metabolism
Ficure 3.2 Graphical representation of the cardiorespiratory system.
A final qualitative requirement is to represent the carcdioresp!
ratory system of an average young, healthy adult) females
population for which we have explicit target data
To get to a mathematical model, we need to separate structures
and processes more carefully than in Fig. 3.2. The lungs and upper
airway are anatomically separate from the overall system. Blood
reaches the lungs via the pulmonary arteries and leaves via the
pulmonary veins. The partial pressures of the respiratory gases
oxygen and carbon dioxide in those vessels are P,, On), PC OAH),
Pp QD, and p,,CO,(), respectively. These are not quite our intended
output variables (Fig. 3.1), but in normal circulation the partial
pressures of respiratory gases in the pulmonary arteries are very
close to those in systemic veins. Similarly, the partial pressures of
respiratory gases in the pulmonary veins have values that are very
close to those in systemic arteries. The input variable, oxygen
metabolism (Fig. 3.1), is represented by mO,(t). Let us further assume
that the respiratory muscles responsible for spontaneous breathing
receive nervous activity with a firing frequency /,,,,()- Breathing and
ventilation are reflected in the time-varying alveolar volume u,(),
another output variable in Fig. 3.1, The block diagram in Fig. 3.3 divides
this system into subsystems, and makes key variables and causal
interactions between subsystems explicit. Note that control of
breathing is not yet included.
Block diagrams are the basis of a modular approach to modeling
and simulation. We can now focus our attention on a single block, or
a block can be reused in another model. In Fig. 3.3 we used a
structural or anatomical criterion for separating the system into
subsystems. Anatomical hierarchies (see Fig. 3.4 for an example)
often provide a first basis for identifying subsystems.
fragt) i va(t)
Distribution to Lungs and airways
| body tissues PpaDal(t) |]
(a a--7
[ PpaCOn(t) ml
PyyCO(t)
mO.(t)} ——>|
Figure 3.3 Biock diagram of the cardiorespiratory system.
Vessels
[ : |
Systemic vessels Pulmonary vessels
=] -——
1
Systemic arteries Systemic veins — Pulmonary arteries Pulmonary veins
Figure 3.4 Basic hierarchy of biood vessels.

## Page 23

A second criterion for separating systems into subsysteme ip
based on function, rather than structure, or on physiology rather
than anatomy. Examples of physiological processes include formation, transport, transformation, and absorption of substances and
generation, transmission, and processing of signals. The physiological]
criterion refers to the type of quantity involved in the modeled
process. In an adaptation of work presented by Rideout (1991), we
distinguish the following basic types of quantities:
1. Volume. Processes: bulk mass transport, formation and
absorption of substances. Examples: respiratory gas flow,
blood flow, cerebrospinal fluid production and absorption.
2. Concentration. Processes: dissolved mass (solute) transport in
a fluid carrier or via diffusion, transformation of substances.
Examples: distribution and metabolism of respiratory gases,
hormones, and drugs in blood or plasma, heat (under certain
conditions).
3. Action potential. Processes: transmission and processing of
predominantly electrical signals by a fixed carrier. Examples:
electrical activity of the heart, transmission of baroreceptor
signals via the vagus nerve, and processing of those signals
by the brain stem.
A few comments on this classification: transport of respiratory or
anesthetic gases in a gas mixture is an intermediate case between
bulk and dissolved mass transport; in this case the contribution of
solute volume to carrier volume cannot be ignored. Partial pressure is
a concept (and variable) that is frequently used alongside concentration
in modeling of solute transport. “Information” can be carried by both
solutes and signals. At the microscopic level, transmission and
processing of signals involve movement of neurotransmitters and
electrical charge in the form of electrons or ions.
The lungs in Fig. 3.3 represent a single anatomical structure, but
can be further divided into lung mechanics involving volume
transport, and pulmonary gas exchange involving solute transport
in the volume carrier and diffusion between gas and blood (Fig. 3.5),
The main factors that determine the partial pressures of gases in the
pulmonary veins are the supply via the pulmonary arteries and
ventilation reflected in the time varying alveolar volume v,(f)2
Anatomical and physiological criteria concur to separate the
cardiorespiratory system from control influences. The partial
pressure of carbon dioxide in systemic arterial blood p,CO,() plays a
primary role in the control of breathing by the autonomic nervous
system. Respiratory centers in the brain stem are sensitive to p,CO,0),
' Composition of inspired gases is considered constant, for now.
wWeuRvePrPee
ee? wee ete
PpaOa(t)y PpypGOo(t)
——) — Pulmonary gas PpvOa(t)
{nuolt) —| Lung mechanics exchange PpyCOn(t)
Va(t)
Figure 3.5 Block diagram of the lungs and airways. To simplify the
representation, a single arrow now represents partial pressures of both gases.
1
Control frnustt) Cardiorespiratory
md q i system Co,‘t)
breathing Ns PalO2
Figure 3.6 Block diagram of the cardiorespiratory system and control of
breathing.
transforming the partial pressure into time-varying nervous activity
sent to the respiratory muscles, the above-mentioned f,,.(f) (Fig. 3.6).
A third criterion for separating systems into subsystems is
measurability of input and output variables. Measurability facilitates
interpretation and system identification, but meaningful subsystems
may sometimes rely on input-output variables that are difficult or
impossible to measure directly. Most of the variables in the presented
example can be measured directly or indirectly. We already observed
that, in a normal circulation, the partial pressures in the pulmonary
arteries are very close to those in easily accessible systemic veins.
The partial pressures in the pulmonary veins are very close to those
in systemic arteries, or can be approximated by partial pressures in
alveolar or exhaled gases, with which they are in equilibrium. The
nervous activity stimulating respiratory muscles could be measured
at the phrenic nerve providing motor supply to the diaphragm
muscle, but it may be easier to obtain derived signals such as an
electromyogram of certain respiratory muscles. ;
In summary, we have used criteria to separate systems into
subsystems based on:
e Anatomy (structure), involving anatomical hierarchies.
¢ Physiology (function), involving the basic type of quantities:
volume, concentration, and action potential.
® Measurability of input and output variables.
The notions of system and subsystem naturally expand into a
hierarchy of superiors and subordinates. When applied to block
ve

## Page 24

38
Theory
diagrams, input-output configurations have to match across levels.
For example, the block diagrams of Figs. 3.3, 3.5, and 3.6 fit the
hierarchy shown in Fig. 3.7.
In many modeling and simulation projects, a block diagram
hierarchy will be established in a “top-down” approach: starting
from the single overall block part of the requirements, we work our
way down until it is no longer necessary or practical to distinguish
further subsystems. At the bottom of the hierarchy there may bea
simple equation describing the relationship between input and
output variables, or we may choose to include a black box for the
particular subsystem, and estimate parameters based on inputoutput data. A third possibility is that the subsystem can be further
described in terms of a network of interacting components reflecting
basic system properties. We will explore this form of conceptual
modeling in the next section. For relatively complex conceptual
models, maintaining the hierarchy may be useful to keep oversight.
For the relatively simple model of Fig. 3.7, after establishing the
hierarchy as part of the conceptual modeling process, we can
substitute the lower blocks into the superior levels, leading to the
more compact representation of Fig. 3.8.
Note how the overall system is divided into subsystems along
anatomical lines and according to type of quantities. Comparing
Figs. 3.8 and 3.1, we have indeed formalized a lot of qualitative
frnus(t) Cardio-
, :
Control! respiratory p.CO»(t)
system
T
A
ed
t t
1 mOzai(t) 1
frnus(t) —3 ——> p,CO.(t)
Lungs Distribution
PpyOait) PpaValt)
T PoyCOo(t) | PpeCOz(t)
IT PpaOalt), PpeCOa(t) I
Lung Ly Gas
mechanics rT exchange
va(t)
foruslt) ———>}
Fiaure 3.7 Hierarehy of block diagramsof the cardioreapiiatar alien. The
bloake
of Fig. 4.4 arere-arranged to HiMNHMNL The Tt WIL Lie @uperiar level
3.2.
Conceptual Models
Nervous system
Action potential
betes
'
1
1
'
t
'
'
'
'
1
'
1
1
!
ee ee
'
'
'
'
'
'
'
'
fl
i
i Concentration
valt! mOz(t) 4C09(t)
ti : ,
ee | oat ii Distribution Control
r| | L.
mechanics | ri Post) |
PpaOalt), PpgCOatt) fraug(t)
|
| | PovCOa(t)
Ficure 3.8 Integrated (single-level) block diagram of the cardiorespiratory
system. Anatomical structures and types of quantities involved in the
subsystems are shown above the blocks.
information about the system. For some modeling tasks the
“hierarchy” may only be one level deep, in which case we do not
distinguish subsystems, and immediately formulate mathematical
models or use conceptual models in the form of component diagrams.
In large and relatively unconstrained modeling projects, the process
of establishing a block diagram hierarchy may be turned around,
and anatomy and types of quantities may be used to build a model
from the “bottom-up,” taking measurability of variables into account
only at higher levels.
Note that the block diagrams in this section are presented to
illustrate concepts; they contain many simplifications, most notably
concerning the limited representation of the circulation and its
control, which will be covered in more detail in Part IL.
tot sisanousseaauusiesmironaoanenrnenaurrninenueit:
Component Diagrams
Even if meaningful causally connected subsystems can no longer be
distinguished, we may be able to describe the internal structure and
functioning of a system further in terms of interacting components
connected in a network. Overall system behavior depends on the
properties of the components and on how they are connected. Figure
3.9 gives an example of a component diagram for an electrical
circuit.
The components in this diagram are an external voltage source, a
capacitor, a resistor, and an inductor. These may be actual physical
components, or represent genera lized system properties, for example,
when modeling the resonant properties of a cable. In the next chapter,
we will see how a mathematical model describing, for example, the
relationship between the variables voltage .e(f) and charge on the
capacitor q(t) ean be derived from component descriptions and the
laws governing connection ol components Generally speaking,
pliyelologieal systems do not econalat of diserete components
38

## Page 25

40‘ Theory
connected in a network. However, component diagrams and derived
mathematical models may represent system properties and behavior
in a reasonable approximation. Figure 3.10 shows examples of
components and networks for systems involving the different types
of quantities introduced in the previous section.
Setting up a conceptual model of a physiological svstem in the
form of a component diagram is an inductive, creative process, where
TOIT
Ficure 3.9 Electrical circuit diagram. See the main text for a description of
variables and components.
(a Pulmonary Pulmonary
Right ventricle arteries veins
RENE Left
atrial = >< I<] atrial
pressure pressure
Tricuspid valve Pulmonic valve Pulmonary Atrial
vascular inflow
resistance resistance
Left lung
, Dead
( space rt Oxygen uptake
Inspired Ventilation |
oxygen
fraction
L Oxygen uptake
Right lung
(c
i
oy u-y .
dt t
Time constant Saturation
Fisure 3.10 Conceptual models of physiological systems in the form of
component diagrams: (a) Volume: fluid circuit diagram of the right ventricle and
pulmonary circulation, (b) Concentration: compartment model of oxygen mixing
in the lungs. (c) Action potential elementary transfers in the aympathetk
nervous system
Conceptual Models
simplifying assumptions need to be balanced against anticipated
model performance. For example, the succession of tricuspid valve,
right ventricle, and pulmonic valve in Fig. 3.10(a) closely reflects basic
anatomy and will be appropriate for a broad range of model
applications. However, representing the whole pulmonary vascular
bed by only three hydraulic components may be appropriate for a
model representing the basic relationships between volume, pressure,
and flow rate, but not for a model for the study of blood flow
distribution in the lungs. The component diagram (of Fig. 3.10(b))
reflects the assumption that oxygen exchange in the lungs can be
represented by three distinct spaces with a homogeneous gas
concentration in each space, two with oxygen uptake, and one dead
space compartment without oxygen exchange. This particular
conceptual model further reflects that ventilation of these spaces is
bidirectional and that the parallel lung compartments are connected
in series with the dead space compartment. Note that for a number of
applications, a model based on continuous, unidirectional ventilation
of a single homogenous space (Fig. 3.11; also see Riley, 1949) is
sufficiently accurate.
If we split the oxygen uptake in the model of Fig. 3.10(b) into
uptake by the arterial blood and delivery to the lungs by the venous
blood, it becomes a conceptual model for oxygen exchange, part of
the gas exchange block of Fig. 3.8, illustrating how block and
component diagrams can be used in conjunction. The transfers of
Fig. 3.10@ reflect elementary mathematical operations. These
operations are combined in a block diagram.
Conceptual models in the form of component diagrams take on
their full meaning in conjunction with the quantitative relationships
between the involved variables and the laws governing component
connections. These will be introduced formally and systematically in
the next chapter, providing a new perspective on what may now
seem like rather intuitive, but somewhat ambiguous drawings. In
Chap. 4 we will also make the distinction between component
diagrams in the same physical domain as the modeled process, and
Inspired
ee en
Ventilation ed
fraction
Oxygen uptake
Piavee 240 Sinplified oxygen exchange model
4

## Page 26

42
33
Theory
analog representations in another physical domain. We will develop
the fluid volume-electrical charge analogy, which implies that
network techniques developed in electrical engineering can also be
applied to modeling fluid mechanics. Part Il of the book provides
further detailed examples of conceptual and mathematical model
design.
General Observations o1on Conceptual Models
The traditional engineering disciplines have well-established
standard symbols for component diagrams. Wherever appropriate,
we will use those. However, in modeling of physiological systems,
we often encounter a number of different physicochemical systems
simultaneously, and in the scientific literature a number of rather
loose conventions are used. Our choice of symbols is a personal one,
as much as possible inspired by standard symbols, but with the
additional requirement of maintaining the distinction between
systems with different basic types of variables. An example of such a
choiceis the use of circular rather than rectangular representations
of compartments, to avoid mistaking them for block diagrams and
misinterpreting represented connections: an arrow in a block
diagram represents a causal connection, but in a compartment model
it represents positive flow of fluid and solute, or metabolism. The
(nonstandard) use of parallel lines for flow conduction in fluid circuit
diagrams such as Fig. 3.10(a) results from similar considerations.
Block diagrams and component diagrams are powerful
complementary conceptual modeling tools for continuous-time
dynamic systems, but not the only ones. Any representation that
links system structure and processes to a mathematical model, anc
that is convenient for both the modeler and model user, can be applied
for conceptual modeling and more general discussions and
presentations of the model.
In modeling of physiological systems, conceptual modeling is a
step in which a lot of domain knowledge (anatomy, physiology,
physics, etc.) and several critical assumptions are incorporated.
Typically, it is the step in which the dialog between life scientists and
modelers, which started with transfer of background knowledge and
requirement formulation, is most pronounced. Simplifications at this
stage have consequences in all subsequent phases, but may only
become apparent in the final stages of development or even during
practical use of a model. This constitutes one of the major challenges
in physiologic modeling and simulation. A common vocabulary and
a combination of knowledge and experience will guide the modeler
and model user in distinguishing useful simplifications from
detrimental oversimplifications. A rigorously documented modeling,
process allows revisiting, simplifications, if necessary
Conceptual Models
eviewy Problems —
3.1 Consider the requirements formulated as part of review problem 2.1.
Divide the overall system into two subsystems, one for the baroreflex and
the other for the “uncontrolled cardiovascular system.” Carefully identify the
input and output variables of each subsystem. Which criteria did you use?
3.2. Consider the electromechanical properties of the heart and the
transmission of electrical activity to the chest wall, where it results in polarity
changes that can be seen in an electrocardiogram (ECG). Design a conceptual
model in the form of a block diagram that separates the intrinsic electrical
activity of the heart from the transmission to the chest wall and from the
mechanical activity resulting in a time-varying contraction. What are the
key variables?
3.3. How does the block diagram from Problem 3.2 need to be modified to
represent mechanical and electrical activity involved in third-degree heart
block, which is a disorder of the cardiac conduction system where there is no
conduction through the atrioventricular node and complete dissociation of
the atrial and ventricular activity, the ventricles beating at their intrinsic rate
of approximately 40 beats per minute?
References and Further Reading
Berne RM, Levy MN, Koeppen BM, Stanton BA, eds. Physiology. 5th ed. Philadelphia:
Mosby; 2004.
Guyton AC, Hall JE. Textbook of medical physiology. 11th ed. Philadelphia: W.B.
Saunders; 2006. :
Rideout VC. Mathematical and computer modeling of physiological systems. Madison,
Prentice Hall, 1991.
Riley RL, Cournand A. ‘Ideal’ alveolar air and the analysis of ventilationperfusion relationships in the lungs. J Appl Physiol. Jul 1949; 1(12):825-847.
43

## Page 27

CHAPTER 4
Mathematical
Models

## Page 28

hie
41
n this chapter we present a method for modeling causal,
continuous-time, finite-dimensional, dynamic systems. A mathematical model, corresponding to two conceptual models in the
form of component diagrams, is derived based on component
descriptions and natural or empirical laws. The state variable
representation, in its most general formulation, captures the behavior
of SISO and MIMO systems, and of static and dynamic, linear and
nonlinear, and time-invariant and time-variant systems. Numerical
integration and simulation of state variable models is straightforward,
and state variable models can be derived from conceptual models of
biomedical systems in the form of component diagrams. After a brief
reminder of numerical] values and units, we present fluid circuit
elements that can be used to model circulation and ventilation;
homogeneous compartments that can be used to model solute
exchange, transport, and metabolism in the respiratory system; and
elementary transfers that can be used to model the nervous system.
We introduce the analog and its applications, and elaborate on the
analogy between fluid and electrical circuits, presenting network
reduction techniques for parallel and in series elements, and an
extensive example of deriving a state variable model of fluid
circuits.
A Model of Two Physical Systems
In this section we will see how a mathematical model is derived from
a conceptual model in the form of a component diagram. This step
involves formulating and combining natural or empirical laws
describing components and connections. To highlight the general
applicability of modeling and simulation, we introduce this step with
two examples from mechanical and electrical engineering,
respectively, Mathematical models for specific biomedical systems
will be introduced in the second half of this chapter. Consider the
(ranelational mechanical system of Tig. a1

## Page 29

Theory
Figure 4.1 Translational mechanical system. See the main text for a
description of components, variables, and parameters.
The components in this diagram are a spring, a mass, and a
frictional element. Their behavior can be depicted in terms of
relationships between variables such as forces and displacements.
For example, Fig. 4.2 shows the relationship between the force on a
spring and its deflection.
These relationships can often be described by equations. Over a
limited range of the variables, a linear equation characterized by a
single constant or parameter may be an acceptable approximation.
For example, let /(f) be the force exerted by the spring on the mass.
For small deviations, this force and the extension x(t) are
proportional.
f,t)=—Kx(t) 41)
where K is the spring constant. The minus sign indicates that the
force operates in the opposite direction of positive x(f). Let f,(f) be the
force caused bv friction of the mass on the surface. If we ignore
breakaway forces, necessary to get the object moving, then, in a first
approximation, this force is proportional to the velocity v(f) of the
frictional element with respect to the surface.
felt) =-Folt) 4.2)
where F is the friction constant. The velocity of the mass is equal to
the derivative of its position x(t).
fl) =—Fottr= a0 43)
The net force on the mass f,(f) and its acceleration a(!) are linked via
Newton's second law.’
' For more information
on (his
anc other natural lawe mentioned 1h ie ehapter
we point to standard phyaioe texte books (ey, Cutnell, 190)
he
Mathematical Models
Deflection “7262
Linear range er TUT
1 ft
ame Force
i
Figure 4.2 Spring characteristic.
d’x(t)
fy (b= Mat) = M ee 44)
Let us further assume that an external force f(t) is applied. The vector
sum of the forces on the mass is the sum of the external force and
those exerted by friction and spring.
fat)= fis f+ £0 (4.5)
Substituting the component descriptions in Eq. (4.5) and rearranging
the terms, we find:
d-x(t) LF dx(t)
M ar dt
+Kx(t) =f) 4.6)
Equation (4.6) constitutes a mathematical model of the
translational mechanical system represented in Fig. 4.1. This ordinary
differential equation (ODE) relates the dependent variable, position
x(t), to the independent variable, external force f(f). The other
dependent variables velocity and acceleration can be derived from
x(t). The specific time profile of x(t) depends on the initial values x(t,)
and v(t,), on the time profile of the external force f(f) for t > f,, and on
the numerical values of the constants or parameters M, F, and K,
describing the components. The ODE is a convenient model
formulation for mathematical analysis of system behavior. We can
derive homogeneous and nonhomogeneous solutions of Eq. (4.6) or
because the coefficients M, F, and K, are constant, use the Laplace
transform to compute the transfer function and the nonhomogeneous
solution, (see for example Roberts, 2003). In the next section we will
present a formulation that is more convenient for numerical
integration anc simulation, But first consider the electrical system of
Hig, 9 repeated in Tig. 4.3 below with a number
of specific variables
Wa parameters
iwieleneoe
4§
O
&Tech
LIBRARY
University of Engg
Karachi-75300
Sir Syed

## Page 30

50
Theory
i(t)
2
et) ]) R
Fieure 4.3 Electrical system.
The components in this diagram are an external voltage source, a
capacitor, a resistor, and an inductor. Their behavior, this time in
terms of the relationship between variable charges, voltages, and
currents, can also be described by equations. When in a linear form,
those relationships can also be characterized by a single constant.
For example, let v,(f) be the voltage across the capacitor and q(t) its
charge. Voltage and charge are proportional over a wide range.
1
v(t)
= q(t) (4.7)
0 ct
where C is the capacitance. The currents through the three componenis in series / (1), 7,(t), and i), are all the same.
LW=i, =i =i) (4.8)
Using conservation ot charge, we find that this current i(t) is equal to
the change in charge on the capacitor.
(4.9)
«=
dt
(4.10)
v,(t) = Ri,(t) = Ri(t) = pa
dt
where K is the resistance. The relationship between voltage across
oft) and current through an inductor i,(4) is:
/ di _, di) dg)
dt dt dl
(41)
4.2
Mathematical Models
Considering the externally applied voltage e(t) and using Kirchhoff’s
voltage law, which states that the sum of all directed voltages in a
closed circuit is zero, we find:
e(t)= v(t) +0, + oF) (4.12)
and substituting the previously found voltages in terms of charge,
we find a mathematical model of the electrical system of Fig. 4.3.
aq(t) | aq) 1 7
L 7B +R ae cai e(t) (4.13)
This ODE relates the dependent variable charge on the capacitor q(t)
to the independent variable, the externally applied voltage e(¢). Other
dependent variables of interest, such as the current i(f) or voltages
across the components, can be derived from q(t) using the above
equations. The specific time profile of q(t) depends on the initial
values q(t,) and i(t,) = dq(t)/dt for t = i, on the time profile of the
externally applied voltage e(¢) for t > t,, and on the numerical values
of parameters R, L, and C. It will not have escaped the attentive reader
that Eq. (4.13) is very similar to Eq. (4.6), repeated below.
M nes 4F dx(t)
dt" dt
+ Kx(t) = fe) 4.14)
The two systems are called analogs. Despite their different nature,
and the different component descriptions and laws used in derivation,
their mathematical models reflect a deep similarity in dynamic
behavior. Consequences and uses of such similarities will be explored
in Sec. 4.7.
Summarizing: Based on a conceptual model in the form of a
component diagram, domain specific component descriptions, and
natural or empirical laws, we derived mathematical models relating
variables of interest. In the next section we will present a model
formulation that is applicable to a broad range of systems and more
convenient for numerical integration and simulation.
State Variable Models
In this section we put one of the mathematical models derived in
See, 4.1 in the torm of a set of algebraic equations for first-order
derivatives of the so-called state variables. We then generalize these
state variable models and show that they can represent a broad class
Of systems
\n alternative formulation of the mathematical model of the
electyical ayatem of Mig. 4.3 can be found by considering: the voltage
SL
Sie Sunes

## Page 31

Theory
across the capacitor v(t) and the current through the inductor i).
Using relationships listed in the previous section, we find their firstorder derivatives.
dv(t) 1,
ao Sit (4.15
dt ci) an)
and
di(t) 1 R. 1
-. = pe - Ti+ rele) 4.16)
Let us assume we are interested in the dependent variable voltage
across the inductor.
2(f) = ae =~v,(t)— Ri(t)+ el?) 4.17)
Introducing the variable vector:
o,(t)|
S| OO :
x(t ea (4.18)
and the scalar variables:
u(t) = e(t) (4.19
yt) = 0, (f) (4.20)
we can write the model of the electrical system, Eqs. (4.15) - (4.17), in
the compact form:
a = Ax(t)+ bu) 4.21)
y(t)= c7 x(t)+ dutt) (4.22
with the constant matrix:
A 0 A/C 7
“|-VL =-R/I (4.2)
Mathematical Models
the constant vectors:
b pes 0
“HyL (4.24)
c= -R| (4.25)
and the scalar constant d = 1. Simplifying the notation of the
derivative, and allowing u(t) and y(t) to be vectors, and b, c, and d
matrices, Eqs. (4.21) and (4.22) can be generalized to:
X(t) = Ax(t) + Bult) . (4.26)
y(t) = Cx(t) + Dutt) (4.27)
Equations (4.26) and (4.27) can be further generalized to:
XE) = fC), ut), £) (4.28)
y(t) = g(x), u(t),£) (4.29)
where f() and g(.) are algebraic or transcendental functions? of the
state variable x(t), the input variable u(t), and time t; y(f) is the output
variable. Equation (4.28) is called the state equation, and Eq. (4.29) is
called the output equation. For now, we will assume that our models
are pure white-box models (Chap. 1) and that the numerical values of
parameters (the constants that appear in the state and output equations)
are given, or can be derived via simple one point measurements, for
example, a resistance from pressure and flow data. Let x(f,) be the
initial value of the state variable at time t,. A block diagram of this
model is given in Fig. 4.4.
Let us consider Eq. (4.28) in more detail. If we know x(f,) and u()
for f 2 {,, then we can predict the evolution of x(t), and via Eq. (4.29), of
u(t). In the next chapter, we will present a practical implementation of
this prediction in the form of numerical integration. Numerical
integration is facilitated by the fact that the constituent equations of
hq, (4.28) only contain a single, first-order derivative. Because no past
\ljebraic funetions can be formed by the algebraic operations: addition, multiplication, division, and talking ann root, A transcendental function cannot be
expreaied in terme of a finite sequence of these algebraic operations. Examples
OF Lranecendental finetions inchide exponential, logarithmic,
and trigonometrie Tune tion
53

## Page 32

(ty)
u(t) ——> Model ———p it
Figure 4.4 Block diagram of a state variable model
information is necessary to predict the evolution of the system, we
say that x(t) contains the “memory” of the system.
As state variables we often choose variables that, in physical
terms, represent temporary energy storage. This is the case for the
voltage across the capacitor and the current through the inductor in
the previous section, and in review problem 4.2 we will derive a state
variable model for the translational mechanical system of Fig. 4.1,
using the extension of the spring x(f), and velocity of the mass v(t) as
state variables. The frictional element dissipates mechanical energy,
but does not store it. To avoid confusion about notation, we introduce
the state variable vector:
_ pol
X(t) = 4 (4.30)
The evolution of this system depends on the present values of the
state variables (extension of the spring and the velocity of the mass)
and on the present and future values of the input variable (the
external force acting om the system). How the present state was
achieved has no influence on the evolution of the system. We again
find that the memory of the system is stored in the state variables.
To simplify modeling and make numerical integration more
efficient, we like to keep the set of state variables as small as possible
This is achieved by selecting independent state variables, that is, state
variables that cannot be expressed in terms of one or more of the
other state variables. For electrical circuits, there are systematic
approaches for selecting a set of independent state variables and
deriving the corresponding state variable model (Athans, 1974).
However, these methods are quite elaborate, and we will see in the
subsequent sections and in Part II that in many practical cases in
biomedical engineering, independent state variables can be selected,
and models derived, by using simple rules of thumb.
We saw in Sec. 1.2 that knowing system properties such as
linearity and time invariance is important because certain analysis
techniques apply only to, for example, linear, time-invariant (LTI)
svatemie In the modeling anc simulation context, knowing, system
and model properties also has several practical consequences, For
example, we know the response from zero initial conditions
y(f) of
a linear system to the input u(f), then we no longer need to derive
or
compute the zero state response to input 2u(t), as, by the system
properties, it is simply 2y(). Another example: A static system has no
state variables and, therefore, no initia! values have to be set to
simulate the model. The properties of a model in state variable
notation can be recognized by inspection of the equations. Table 4.1
provides the key to such connections. Proof of these associations can
be provided based on definitions of system properties, Sec. 2.2. Note
that the properties of the model equations do not automatically carry
over to the real system it represents. For example, a nonlinear system
can have a linear model for a limited range of the input and state
variables.
The last property in Table 4.1 is added here for later reference.
When notations in Table 4.1 are combined, then so are model
properties. For example, when we combine the notations of the third
and fourth models in Table 4.1, we obtain Eqs. (4.26) and (4.27), with
constant rather than time-dependent matrices A, B, C, and D.
Combining the properties, we find that this model is LT1.
In Sec. 4.8 we will come back to some potential concerns with
state variables models, but note that the above demonstrates how
versatile the state variable representation is: In its most genera!
formulation, Eqs. (4.28) and (4.29), it captures the behavior of SISO
and MIMO systems, and of static and dynamic, linear and nonlinear,
X(t) = F(x(t),u(t),t u(t) and y(t) scalars | Single-input
| | single-output
| y(t) = g(x(t),u(t),t) (SISO)
“yty)=guult)t) —«=«=‘ét@ State equaation == Static
fence Sy poi oe ie ee
A(t), BQ), C(t), and Dit) Linear
time-dependent
| matrices
x(t) = A(t)x(t)+ B(tyu(t)
C(t)x(t)+ D(t)u(t)
bs
ii}
X(t) = f(x(t),u(t)) 10) and gl) are not | Time-invariant
(direct) functions of t
X(t) = f(x(t), u(t), t) ! | No immediate
i | throughput from
y(t) = g(x(t),t) ) input
to output |
Taste 4. Equations and Properties of State Variable Models

## Page 33

56
Theory
as well as time-invariant and time-variant systems. In the next
chapter, we will see that numerical integration and simulation of
state variable models is straightforward. In the remainder of this
chapter and in Part II of the book we will see how state variables
models can be derived from conceptual models of biomedical systems
in the form of component diagrams, but first we provide the reader
with a brief reminder of units and numerical values.
3 Units and Numerical Values
So far, we have been discussing physical systems and models without
referring to specific numerical values. This is a fruitful abstraction,
but if we want to obtain specific analytical solutions or numerically
integrate the state equation, we need to assign numerical values to
the involved quantities: variables, parameters, and the special
variable time. This implies the use of a consistent set of units, which
is especially challenging in the biomedical field, where a number of
nonstandard units are still in use. For smaller modeling and
simulation projects, it may be simpler to work with clinical units
whenever possible, paying close attention to consistency. For more
complex models, and especially when combining models of different
systems, we propose to use the SI (from the French Systeme
International) units and then convert input and output variables from
and to clinically applied units whenever necessary. As a reminder,
Tables 4.2, 4.3, and 4.4 list the SI base units, selected SI derived units,
and SI prefixes, respectively. The latter help keep numerical values
within convenient ranges. Frequently used clinical units for time,
volume, and pressure, and their conversions to SI units are listed in
Table 4.5. See the literature on physics for the conditions such as
pressure and temperature, which are sometimes involved in these
conversions. Clinical units for derived quantities, such as flow rate
and resistance, will be listed in subsequent sections.
Quantity Name | Symbol |
Length |_meter Lm |
Time ' second | S$
_ Temperature / kelvin [kK ~
| Amount of substance mole | mol
- | ampere | A |
, | candela cd
Tasie 4.2 SI Base Units
Mathematical Models 57
i Quantity Name Symbol and derivation |
Area square meter e
| Volume _. ‘cubic meter _
4 Nelocity ce | “meter per second -—
Acceleration | meter per second -
_ pron SABES |
Force | newton - : 7
Work, Energy _ joule
. Frequency — “hertz —_
| Electric potential volt a
| Charge F coulomb |
Resistance ohm |
Capacitance “Farad _
| Inductance. — | henry
Tape 4.3 Selected SI Derived Units
[ Factor Prefix Symbol
“10%
© 10%
| 10°
10°
410-8
10” | pico |p
Tame 4.4 Profixos

## Page 34

58 Theory
Quantity | Unit Symbol and derivation |
l time ‘minute ; dmin=60s
“Lhr = 36005
|
il
t04.3kPa
| atmosphere
_ millimeter mercur
datm=401.3kKPa
1000 om H,0 = $
cme=0.000LKPaCid
UV
P,(t) — Pott)
1 dyne/
if v(t)
| Mathematical description
| centimeter
Taste 4.5 Frequently Used Clinical Units and Conversions to SI! Units
py(t) ~ Polt)
1c
t
p(t) ~ pplt)
a/R
4.4 Direct Representation of Fluid Circuits
We have already seen the basics of mathematical modeling of
physical systems: how to go from a conceptual to a mathematical
model, the versatile and easy-to-use state variable representation,
and numerical vaiues and units. In the remaining sections of this |
chapter, we will expand those tools for use in modeling of
physiological systems. We will call graphical representations such
as Figs. 4.1 and 4.3 direct representations of the respective mechanica.
and electrical systems. We will reserve the term analog for a graphica- _
representation in a different physical domain from that of the j te
| Relationship
af
dt
po{t)
—-
f)
pp{t)
(t)
(f)
~ Pa(t)
2
original system. In Sec. 4.7 we will come back to analogs and their {
use in modeling of physiological systems. |
Fluids include both liquids and gases. Basic concepts for the =
description of the behavior of fluids, such as density, pressure, and | a nel
continuity, can be found in many introductory texts on physics (e.g.
Haliday, 2001). Direct representations of fluid circuit elements that
are frequently used in modeling of systems involving volume type '
quantities such as the circulation and lung mechanics are listed in j
Table 4.6, together with idealized linear or piecewise linear
p,(t)
—
F(t)
uit
©:
Dp. °
—
f(t)
ations of Fluid Circuit Elements
p=
npliance
Direc
relationships and mathematical descriptions. Table 4.7 lists the
involved basic quantities.
Basic passive fluid circuit elements listed in ‘Table 4.6 include
a resistor, compliance, inductor, and valve The relationship and
wets
Inductor
Valve
Tanie 46
|
no

## Page 35

Mathematical Models
Name | Symbol | Si unit Frequently used
clinical units
Volume v(t) Lem’ L, m! |
er \ Pressure p(t) | Pa (=N/m?) mm Hg,cmH,O
5 Flow rate f(t) |_m*/s _U/min, mi/s ——
3 ' 3 | Resistance R | Pam's | dyns cm, cm H,OL*S
$ 8 ie Compliance ic _ m/Pa / mi/mm Hg, ml/em H,0
S| 1S Sl Fluid Pal | Pa ms? =
gi i Bs | inductance i i
a = \ Oo SS - oe oe Heenan a a
Be, ° |g 2 |
§| ce 1 i Taste 4.7 Basic Variables and Parameters in Fluid Circuits
=| 5 eo &
z| ¢ oe a ;
es mathematical description of the resistance reflect Ohm’s law for
fluid circuits.’ For this, as well as for the other elements, the direction
of the arrow corresponds to a positive flow rate. In the later
paragraphs, we will come back to the physics behind this law, and in
Sec. 4.7 we will revisit the equivalencies with other electrical circuit
elements. The second element contains a nonlinearity, reflecting that
below an unstressed volume UY, the vessel (or airway) segment is in
a collapsed state, without generating pressure. Imagine a balloon
that requires a certain volume, before pressure starts building up.
Above this volume, the compliance, which is equal to the ratio
between change of volume and change of pressure, is assumed to be
constant. UV is an additional parameter, required to characterize
this relationship. In the transmural pressure of the compliance 7,()
- p,(t), p,() is often assigned a zero value, representing a reference
pressure, for example, ambient pressure. Note that only positive
volumes and pressures are taken into consideration for this element.
Besides the description of this elastic behavior, the mathematical
description of the compliance contains a second equation reflecting
conservation of mass: The change of volume is equal to the inflow
rate minus the outflow rate. Note that the compliance may also be
connected to a single, possibly bidirectional flow rate. The inductor
Relationshi
Symbol
—
Facile 4.6 Direct Representations of Fluid Circuit Elements (continued)
compliances (Beneken, 1967;Suga, 1973). Themathematical description
of this element is identical to the passive compliance, with the
eS represents inertial phenomena: it takes a pressure difference and a
& certain amount of time to change flow rate. An open valve has an
| 2 internal resistance R. The valve closes when the pressure across the
1g valve is negative and there is no reverse flow. Two basic active
= | Be | components are also included in Table 4.6. An (ideal) compressor
g = | maintains a specified pressure difference regardless of the flow rate
ais i | through it. Heart chambers can be represented by time-varying
‘ All depleted relationalipe
are atatic; alvo see Table dl, buat we maintain
the note
tion e0) fora variable to clearly diatinpiieh i from a parameter 2

## Page 36

Theory
exception of a time varying c(f). Often, the mathematical description
uses the inverse of compliance: elastance:
p(t) = e(t)[v(t) -UV| (4.31)
where p(f) is the transmural pressure p,(t) — p,(t), and with, for
example,
+ (Emax ~Emin)Sin(at/T,,) for 0<t<T,,
Ein
e(t)= 4.32)
‘min (otherwise )
Figure 4.5 shows e(), repeated with heart period HP. The other
parameters of this curve are the duration of ventricular systole, T,,
and the minimum and maximum elastances, E,,, aid, Bis
respectively.
From a general modeling perspective, we observe that the
relationships and mathematical descriptions may introduce
assumptions and simplifications in addition to those already
included in the conceptual model.
The mathematical relationships for the compliances and for the
inductor contain derivatives of volume in and flow rate through the
element, respectively. When the elements are included in a network,
these are good choices of state variables, and equations of the type of
Eq. (4.28) can often be derived. Rules for combining these elements
are analogous to the rules for combining electrical elements in
circuits, and will be discussed further in Sec. 4.7. There we will aiso
demonstrate how a mathematical model for a complete circuit is
derived. In Part II of the book we will use these elements to build
conceptual models, such as Fig. 3.10(a), and derive mathematical
models from them. Differences between hydraulics and pneumatics
Fiaure 4.5 Simple cardiac elastance funotion
Mathematical Models
will be discussed there too. We verify that only the mentioned state
variables contain information about the past of the system.
A deeper understanding of the circuit elements, depicted
relationships, mathematical descriptions, and implicit simplifications
can be gained both from further study of physics and “real world”
experiential learning. The mathematical description of the resistor,
for example, is a form of Poiseuille’s law for laminar fluid flow
through a uniform straight pipe of radius r and length /
Ue
= At OP)
(f)
f 87
(4.33)
where 7 is the dynamic viscosity. Propelling air or water through
tubes of different diameter and length will make you experience this
law. Studying Young’s modulus and blowing air into more or less
compliant balloons will improve understanding of compliance
Newton’s second law of motion (see Sec. 4.1) and trying to lift a bucket
of water slowly vs. instantaneously (df(t)/di — ~) provides insight
into the fluid inductor. :
Direct Representation of Gas Uptake
and Distribution
Basic concepts for the description of a gas in a gaS mixture or a gas
dissolved in a liquid, such as partial pressure, solubility, diffusion,
and the ideal gas law, can be found in many introductory texts on
chemistry and physics (¢.g., Brady, 2000; Haliday, 2001). References to
the rather complex binding of the respiratory gases oxygen and
carbon dioxide to other molecules in blood will be given in Part II. A
direct representation that is fundamental in the modeling of
physiological systems involving concentration-type variables is the
homogeneous compartment. A number of elementary homogeneous
compartments that are frequently used in modeling of gas uptake in
the lungs and distribution via the circulation are listed in Table 4.8,
together with their mathematical descriptions. The relationships
between variables in these compartments are more complex than for
fluid circuit elements; therefore, a simple graphical representation
cannot be given here. Table 4.9 lists the involved quantities.
Table 4.8 reflects the use of partial pressure, rather than
content, as a state variable. This represents expansion of work on
inert gases by, for example, Mapleson (1963) and Zwart (1972),
rather than a traditional content-based approach to modeling of
respiratory gases such as that presented by, for example, Grodins
(1967) and Chiari (1997). The advantages of this approach are that
it facilitates deseription of diffusion phenomena and allows for a
more unified representation of mixing phenomena in gases and
63

## Page 37

Mathematical Models
a eee eee er Name Symbol | SI unit Frequently used
| | | g clinical units
| i ve Partial pressure | p(t) Pa (= Nm?) mm Hg
/ z | Ee a\_8 | Concentration c(t) | mol m, kg Lor ml of gas at STP or
} a = |=)e | -3
g oss | 3 s 3 _ im L BTPS/L or di of blood -
I al= eS Sle | Gas volume om? | LormlatSTP or BTPS
| i 38 | S cs mt s i | Blood volume m : L, ml
| | Et i = | é > | ce = \ Tissue volume _ _mé imi ;
S| clic + fl iq t 4 | mene
A | =_& Sls = = | = ~ | Gas flow rate : ms s* | Lat STP or BTPS min®, ml
Bas = | 2 = ae & = | S e i \ | at STP or BTPS s*
Ss, S | 8 sje Sil 1S S i Ae | ase | Blood flowrate F, | mest | Lmin+, mis*
o| | a 22 eae | Se | | . - neal. es
S| =f | = | gis =2 u2| : {
3 a Es { <Zl-8. S fs i, ee .
o <¥ s SR = = A | See main text for STP and BTPS.
sf | & & / = |
3) | | wise pu || = jul [ _
i Ly \ fl i i Taste 4.9 Variables, Parameters, and Units in Homogeneous Compartments
o it i | Eat H S Pay
\ | z| S a|S {
s \
fluids, and of inert gases and gases with binding. It brings with it
some additional complexity in the form of the derivative of the
' | - | partial pressure—content relationships. In this chapter we consider
| 5 | | \ i that the involved carrier flow rates and volumes are constant and
ig | positive. In Chap. 9 we will lift those restrictions—with the
| 3 | exception of positive volumes—and discuss multiple models
| ls \ 9 combining dynamic fluid models with homogeneous comparti 6 ment models.
ig | 5 The SI units for concentration of a gas in a gas mixture or
5 2 | z | 3 dissolved in a liquid are mol/m’ or kg/m’. In medicine, for a gas in
3 Joe * | é a gas mixture, and by extension for a gas dissolved in a liquid,
| E | a & , € | a volume fractions are often used for example, milliliter of oxygen per
ka [= Be _ oe = deciliter of blood. These units are often taken over in physiologic
| i | \ | | &, models. They suffer from the following ambiguity: how much gas
| | vo ' ‘< | | 12 (in moles or kilogram) a particular volume (milliliter or liter)
| ls ; 13 | | |g contains, depends on temperature, pressure, and the amount of
| \s \ = | o is | |S water vapor in the gas. As long as the units are carefully specified,
| | & \£ \ 5 E | 2 ] 2g this does not constitute a problem. The following conversions from
| g | a | = = g | \s mole to liter apply. For a gas that obeys the ideal gas law:
,£ OD lo | 13
|e ee 2 | 8 12 3 | |8 PV =nRT 434)
5 & rs 2 = \8 | 8 with pressure P in Pa, volume V in m%, the number of moles , the
E i = le |g 8 5 5 z universal gas constant R & 8.31 Pa m* mol x, and temperature Tin
5 2 18 \8 |s \2 § |" f ~ Kk, 1 mol at the standard temperature T = 0 °C = 273 K and standard
3 2 ° \8 3 | oo i be pressure! [© 100 kPa occupies approximately
AES 3 2 \€ ef EI i
Older lexthbooke vee the standard pressure Latin e Ed RPA

## Page 38

66
Theory
_nRT, _1x8.31x273 = 0.0227m° = 22.7LatSTP (4.35)
P 10°
Vv,
Applying the ideal gas law, we find that at body temperature
T = 37 °C = 310 K, but otherwise identical conditions, the same
amount of gas occupies approximately
Bo. 310
Vy = 2V, = 22.7 = 25.8LatBTPD
ae (4.36)
where D stands for dry gas. The vapor pressure of water at body
temperature is approximately 47 torr = 0.06 10° Pa (Brady, 2001). If the
gas is saturated with water vapor, its pressure decreases from the
standard pressure to a partial pressure
Prag = P- Py. = (1.00 ~ 0.06) 10° = 0.94 x10°Pa (4.37)
Again applying the ideal gas law, the same amount of gas, now
mixed with water vapor, occupies approximately
P 10°
Vn= Vy =—————
25.8 = 27 ALat BTPS
3D 2 0.94x10° (38)
gas
where S stands for saturated with water vapor. For precise models
involving inspired gases, ambient temperature, pressure, and relative
humidity have to be taken into account.
We will derive the mathematical description of the perfused
blood-tissue compartment with metabolism, and then show how it
can be simplified to obtain the description of the perfused
compartment with inert gas. The amount of gas in the blood-tissue
compartment consists of gas dissolved in blood and gas dissolved in
tissue. Both forms are at the same partial pressure, but have different
and potentially nonlinear binding characteristics:
a(t) = V,c, [pb] + Vics [pO] (4.39)
Mass transport is equal to the product of carrier (blood) flow rate
and solute concentration. For example, in the compartment inflow:
Fico [pin (4.40)
Mathematical Models
The change of amount depends on inflow, outflow, and
metabolism, formalized in the mass balance:
a = F.cs[ Pin] — Fico [PO]-V 4.41)
To write this mass balance in terms of partial pressures, we first take
the derivative of Eq. (4.39):
dp(t)
ptt) at
datt) _ vy, dey(p)| apt), , dep)
dt "ap | dp
=| sa
dp
Combining Eqs. (4.41) and (4.42) and reorganizing terms, we find the
mathematical description included in Table 4.8:
vy dese] ae
oP Le | at
(4.42)
dp) _ F,{co[Pin(®)|—5[POH-V
= 7 (4.43)
a E dev'p)| —, dex(p)
p(t)
aP he) ap
For the perfused compartment with inert gas, tissue volume and
metabolism are zero, and content is found via Henry’s law, for
example, in blood:
cp [pee)]= apt) (4.44)
where a, is the solubility coefficient for the considered gas in blood.”
For inert gases, the derivative of the partial pressure—content
relationship is simply:
de, (p) =e
dp b (4.45)
Mass transport simplifies to:
F,Qpp, (8) (4.46)
Hore we follow the standard notation of the parameter o.in lower case
67

## Page 39

Theory Mathematica! Models 69
The solubility coefficients cancel out and Eq. (4.43) can be simplified
to the result listed in Table 4.8:
|
|
dpt) _&,
aE
= lp. (DH - plE 7 i
a = y; PnP )] 4.47) | |
For the derivation of mathematical descriptions of ventilated | |
=
=
e
I
compartments, we need to take into account that the amount of gas SI s
ina gas mixture is equal to: | | Fi
i | Ser rel
| ; wg i
(t) a | H js '
a(t) = Ve = (4.48) = | | =e Ss
: a | ' =
s} = | ie
S 2 eres
, 2 rs or i
where P., represents the total pressure. The mass transport of gas in 8 aE | op | =
a gas mixture is equal to, for example: S Ces | = S
( = uw & a ey us ut S |
F, Pi (4.49) +l eS ee ce i &
Pr uw ol i (wes putt yo li
1 S S14 a oS: ee ~ S
spur Ff Pi F our BF
In the description of the ventilated compartment, Table 4.8, the | voanell nel
parameter P, cancels out, but we do find it back in the description of
the ventilated and perfused compartment, which is a simple lung
model. Binding characteristics of specific respiratory gases will be
presented in Chap. 9. Conceptual modeis of concentration-type
models often include several connected homogeneous compartments
[see, for example, Fig. 3.10(b)]. Table 4.10 lists several of those
connections and their mathematical descriptions.
Concatenation and multiple outflows have straightforward
descriptions. The mathematical description of the volumeiess
confluent reflects conservation of mass of the carrier fluid,
polt)
Fy
n
ic
oO
5
GQ
&
°
Oo
®
instantaneous mixing and conservation of solute mass (the equation i 3
reflects blood carrying gas with binding), and computation of the i &
inverse of the partial pressure—content relationship. The latter is only s = | | 2
computed if partial pressure is explicitly required. The derivation of | ia < 1s
the mathematical description of a compartment with multiple (blood) i ~ | wo
inflows is very similar to the derivation for the perfused blood-tissue | o \ 8
compartment with metabolism. It is equivalent to a confluent = g zZ | pe
followed by a compartment. In Part II of the book we will use these S HS = 1 ts
elements and connections to build conceptual models [such as 5 5 . le | bs
Fig. 3.10(b)] and derive mathematical models from them, Models for e i a ial | 7
important respiratory phenomena such as dead space and shunt will hi | & | 5 [3 | i
) oO 4 le Cs)
Ey
ra
be introduced there.

## Page 40

10
4.6 Direct Representation of Simple Transfers
4.7
Theory
in the Nervous System
The central and peripheral nervous systems process many
physiological variables. For example, the firing frequency of afferent
neurons from peripheral chemoreceptors to the brain stem cA)
depends on the partial pressure of oxygen in arterial blood p,O,().
The brain stem processes this signal, resulting in the firing frequency
of efferent neurons f(f) influencing, for example, heart rate hr(é)
(Fig. 4.6).
The processing going on in each individual block can often be
described by one or more simple mathematical operations. A number
of elementary operations that are frequently used in modeling of
transfers in the nervous systems are shown in Table 4.11, together
with their graphical representation. The involved quantities can be
quite diverse, and are therefore represented by generic input u(f) and
output (f) variables and generic parameters, such as an offset Y, and
time constant 7.°
The first five elementary operations are static, and their
mathematical representation is in the form of Eq. (4.29). The last
operation is dynamic and its mathematical representation is in the
form of Eq. (4.28). The output equation for this element would simply
be y() = x(#). Although special symbols exist for some simple
functions, such as a sum or integrator element, we chose here to
represent all these relationships by a simple block with input and
output variables. The relationship or the mathematical description
can be included in the block [see Fig. 3.10(0)]. The signal processing
and control engineering literature provide more elaborate system
transfers (Roberts, 2003). Connecting rules are simple and identical
to those of general block diagrams. An input has to have a welldefined, single origin. Outputs can be sent to one or more other
blocks, resulting in series or parallel combinations. The sum block
combines two or more inputs. In Part Il of the book we will use these
elements and connecting rules to build conceptual models of systems
(such as in Fig. 4.6).
Electrical Analogs and State Variable Models
of Circuits
For a representation to be qualified as an analog of a given system
the underlying mathematical models should be the same. In
that sense, and after demonstrating that the two systems have
identical underlying mathematica] models, Fig, 4.1 is a mechanical
6 Here we follow the standard notation
of the parameter CN lower cane
Mathematical Models 7]
Peripheral f(t) | felt) | |
P202lt) —> chemoreceptors Brain stem | 275, oa pam LL» hrit)
| ode
Figure 4.6 Block diagram of processes involved in chemoreceptor control of
heart rate. See main text for symbols.
Name | Relationship
Mathematical description
Sum
y(t)
ag Up(t)
¥(t) = Uy (t) + Up(t)
Gu(t)
| |
i }
i |
Gain with offset y(t) | y(t) = Gu(t) + ¥, oo |
) Ms 0
i | i
EA
¥ G
ZZ / u(t) |
Piecewise linear vey - t Bathe - q
function oo | SONS
i Y(t) = Vy
Yy LAS else if u(t) < U,
a i
j . \ Yo~- Yj {
U, U. ‘ = 2 1 }
5 Uy ult) | W(t) = V4 + U,2u,
aT (u(t)-U,) |
else
Y(t) = Yo
gmoid curve i () | u(t)’ i
| y(t)= er
u(t)’ + UY). |
first order NA _
transfer oxe) = et)
=xit)
at es
Tape 4.44
Hepresentations of Simple System Transfers

## Page 41

22
Theory
analog for the electrical system of Fig. 4.3, and Fig. 4.3 is an
electrical analog for the mechanical system of Fig. 4.1. In the past,
electrical analogs were often used to represent hemodynamics
and ventilatory mechanics, and even gas exchange, but we
recommend the use of direct representations to establish
conceptual models. This greatly facilitates the dialog between life
scientists and modelers, and avoids a number of problems related
to equivalencies between variables and parameters and associated
unit conversions. Analogs nevertheless still have useful
applications in physiologic modeling. In the first place, they may
provide additional insights in a given system. Consider, for
example, the equivalencies between the spring in Fig. 4.1 (Eq. 4.1),
the capacitor in Fig. 4.3 (Eq. 4.7), and the compliance in Table 4.5.
What we learn about one system is extended to an understanding
of the other system. However, when making such extensions, we
need to be aware of the simplifications underlying idealized
components. For example, there is no equivalent phenomenon to
the mentioned breakaway forces for the frictional element in Fig.
4.1 for current flow through a resistor. A somewhat related
application of an analog is that it may be in a domain that the
modeler is more familiar with. A mechanical, or mechanically
oriented, engineer may prefer to work with Fig. 4.1 as a
representation of the electrical system, once it is established as an
analog. Similarly, a transformation into another domain may
provide a convenient and more intuitive visualization of a system,
or of its mathematical model, that would otherwise remain
difficult to understand. For example, Nikkelen et al. (1998) used a
hydraulic analog of the dynamic, nonlinear processes of drug
distribution and drug effect on muscle relaxation. An accelerated
time simulation of this analog was used in teaching
pharmacokinetics and pharmacodynamics to anesthesia residents.
A special form of direct representation, sometimes also calied an
analog, is a linear equivalent circuit. For example, an electrical
equivalent circuit for the electrode-skin interface may provide
useful insights in the main dynamics of this system. A final
application of analogs is based on the fact that, in some physical
domains, certain techniques are worked out further than in others.
Here we will present network reduction techniques for parallel
and in series electrical circuit elements, and a more extensive
electrical circuit example. Via analogy, the same concepts also
apply to direct representations of hydraulic and pneumatic
circuits. In preparation of that, and to facilitate access to older
biomedical modeling literature, Tables 4.12 and 4,13 present
electrical circuit elements and quantities in the order of
equivalencies to Tables 4.6 and 4.7.
Mathematical Models 73
[Name
| | —
|Symbo! Relationship | Mathematical description 4
Resistor jy,tHAA AVX volt) | it i v,(t) v(t)
i i(t) oR i
| V4(t)-vo(t) |
Capacitor | a(t) | val -v9(t _ oo q(t) 7 :
ed ae [ee
i a i ve | ‘
a) 7 a) | ie) = 0 =o atti)
Inductor iyo OO v(t) le (t)-vo(t) a 7
2 AND i
| ae va(t)—vo(t) =L 22
i(t) | Wt at
i dit) |
Diode (in ly ( vot) it) 7 ‘ a
les | A prov A | if v,(t)-Vo(t)>0
witha | iit) i wR ‘(ty = ave)
resistor) ¥,(t)=Vo(t) R
else
i(t)=0
Volta e j - (t + " —_
ta | et) | volt=vg(t) Vo(t) = vq (t) + ett)
hoe ——
Ke) |
Tote 4.12 — Electrical Analogs to the First Five Fluid Circuit Elements of Table 4.6
Resistance
Capacitance
Inductance
[ Name | Symbol | Stunit
| Charge q(t) C (=As) ;
Voltage _ M(t) - VeNmA*s*)
| Current
Tamir 4,13
Basic Variables and Parameters in Electrical Circuits

## Page 42

4
Theory
Unlike the equivalent compliance, the capacitor has a linear
model, and allows for negative charges. The most commonly used
state variable is voltage, equivalent to pressure, rather than charge,
equivalent to volume.
In modeling physiological and other systems we frequently
encounter in series and parallel circuit elements, for example, in
series upper airway and bronchial resistances to gas flow, or parallel
left and right lung compliances. If volumes or flow rates (charges or
currents) on or through the individual elements are not of interest,
then these elements can be combined, simplifying the model without
loss of generality. Table 4.14 shows several rules for combining linear
electrical resistors and capacitors.
These equivalencies can be derived using component descriptions and the Kirchhoff laws. Kirchhoff’s voltage law (KVL) was
introduced in Sec. 4.1. Kirchhoff’s current law (KCL) specifies that
the sum of the currents flowing into a node is equal to the sum of
currents flowing out of a node. For example, assuming initially
uncharged capacitors in series, if a charge q(t) is injected in capacitor
C,, then by KCL, the same current and charge enter C,. Using KVL
and the component description, Table 4.12, we find the voltage across
the two capacitors
4)
U,(t)— v2 (t)= a +e
1 2
(4.50)
$
°
Ry + Ro
:
C,Cy
C, + Cy
dit
HI
L
Tante 4.14 1h Series and Parallel Resistors and Capauital
Mathematica! Models
or
ov) 1 1 _ G+C
gt) = C, CC
(4.51)
and the total capacitance is
at) GG,
2 (—v9lt)
Cy +Cy
(4.52)
Figure 4.7 shows a fluid circuit, part of an elementary vascular
model, and its electrical analog.
We will derive a state varble model! for this nemo in the
domain of the analog. Remember that the goal of a state variable
model is to express the change of the state variables, which we will
choose to be the charges on the capacitors, as a function of the same
state variables, and of the input voltage e(t). At a specific time f, the
voltages across the capacitors can be expressed as a function of their
charges, using the component description in Table 4.12.
ne)
t
a= CG (4.53)
Gait)
hb=_Boe
ag (F) Cy (4.54)
(t)
(t= (4.55)
3
C3
HH
IH
KAA
Piawwe 4.7 Tluld oiroult ‘and its alec trot analog,
6

## Page 43

76 02 «Theory
The currents through the resistors R, and R, depend on the voltages
according to Ohm’s jaw, also included in Table 4.12.
oy (t) - v(t)
Re
‘1
i(t)= (4.56)
_ U9(t)— v5 (t)
in(t) a
(4.57)
We find an expression for the current i,(f) = i,(f) through the resistors
R, and R, via the KVL for the closed circuit: ground, C,, R,, source,
R, C,, and back to ground, taking into account the directed
oY
voltages.
aa(t)— Rais (#) + e(t) — Ryig(t)
— 2, (1) = 0 (4.58)
or
v(t) + e(t) — 0, (t)
iz(t) = ig(t) = R+ks
(4.59)
The change in charge on each capacitor is equal to the difference
between incoming and outgoing currents.
dq,
(t)
MH = ig(t) 110 (4.60)
BHD 500) —~ig() (4.60)
di 2
Hast) 83) ig) (4.62)
By substituting the voltage equations in the current equations, and
the current equations in the charge equations, we find:
dqy(t) _ qalt)/Ca+elt)—qy(t)/C, aul) /C, - qn (t)/Co
dt Rot Ry
(4.63)
g(t) _ qylt)/Cy—qalt)/Cy _ qylt)/
Co —aalt)/Ca on
di R R
dag(t) — qa(t)/Cy qx) /Cy galt)/Cy eC = gy (D/ ey
(1.05)
dt Ry Kya ,
Mathematical Models
or
dq,(t)
is
q(t) =
dt |
dq, |
L dt
a eS 1 11 a(t) 1
CU Rot+R, Ry CR, C3 Ro +R, Ro +R;
1 1 2 1 b
—— ->|—+— t)|+ 0 t
GR, G, [Z z] CRs 2 ae
44 1 Aft, 1 Ve] [a
Cy Ro +R CoR> Cg\ Ry Ry t+R3 % Rot Rs
(4.66)
which is indeed a state equation of the form of Eq. (4.26)
X(t) = Ax(t) + Bult) (4.67)
4.8
Using the equivalencies between electrical and hydraulic
quantities as listed in Tables 4.13 and 4.7, respectively, and substituting
the external voltage by an externally applied pressure, we can
transform this model into a model for the analog hydraulic circuit.
For this relatively simple circuit, we could also have derived the
mathematical model directly from the fluid circuit and its component
equations. If we choose to include nonlinear compliances, the
resulting model will be of the form of Eq. (4.28). Note that the state
variables in this example are dependent: the sum of the charges on
the capacitors or of the volumes in the compliances is constant. The
model could therefore be simplified. However, if a leakage current
or blood loss is included, this would no longer be the case, and the
same systematic model derivation applies.
General Observations on Mathematical Models
and Parameter Estimation
The mathematical model has obvious advantages for system ana-
», and by being unambiguous, concise (yet complete), and selftent (Khoo, 1999) itis the best form to archive knowledge about
the syatem, A mathematical model in state variable notation is fully

## Page 44

rt}
Theory
characterized by input and output variables, state and output
equations, and numerical values of parameters and initial state
variables. A code implementation is necessary to obtain simulation
results, but does not have the properties of a mathematical model
that make it convenient for analysis and archiving knowledge. We
do not advocate the use of techniques, however convenient, that skip
the mathematical model and code implementation steps, and go
directly from “drag-and-drop” diagrams of system structure and
function to simulation results; the overall block diagram, conceptual
model, mathematical model, and simulation results provide
complementary perspectives on system behavior, which are most
insightful when established separately and then considered in
conjunction.
For white-box models, the parameters are known, and involve
physical constants or measurable quantities, for example, the
universal gas constant or total blood volume. For gray-box models,
some of the parameters may have to be estimated. The methods to
do so can be divided into two broad categories. One approach is to
search the scientific literature for numerical values of model
parameters for specific structures or processes. These parameters
may have to be scaled from different human or even animal
populations. See Goodwin et al. (2004) for an example of this process
applied to a cardiovascular model. An alternative method is to treat
a model with a few remaining unknown parameters as a black-box
model, and apply standard parameter estimation techniques (Ljung,
1999). If only a single model parameter remains to be estimated,
and if resulting limited accuracy is acceptable, a point estimate
based on a single observable response may be sufficient. See Van
Meurs et al. (1998) for an example of this process applied to a
pharmacological model.
A possible concern with state variable models is that the set of
independent state variables may not be unique. For example, we
could have used the voltages across the capacitors in Fig. 4.7 instead
of their charges as state variables. Therefore, there may be several
valid state variable models for the same system. A second concern
has to do with the time-domain character of state variable models.
There is no equivalent to the simple multiplication of transfer
functions for calculation of the response of two systems in series.
This is a concern for system analysis and design, but not for
simulation. For simulation purposes, two state variable models can
easily be connected by specifying:
Un(t) = yy (f) (4,68)
where y,(#) is the output of the first system, and (ie The input ot the
second system, This puts some conatrainiy on the order i whieh
Review Problems
Mathematical Models
equations have to be computed. We will investigate this topic further
in the next chapter.
In Secs. 4.1 and 4.2 we showed in a simple example how the same
system can be represented by an ordinary differential equation and
a state variable model, respectively. For a more formal treatment of
the relationships between these mathematical models, and the
relationships with models in the form of the impulse response,
frequency response function, and transfer function, we again point
to Ljung (1999).
4.1 Design a conceptual model for the uncontrolled cardiovascular
subsystem of Review Problem 3.1 in the form of a fluid circuit diagram.
Take into account the requirements formulated as part of Review Problem
2.1. Derive a mathematical model assuming linear fluid circuit elements
and a simple time-varying elastance, as introduced in Sec. 4.4. Search
the scientific literature for numerical values of model parameters for the
selected patient population. See Goodwin et al. (2004) for an example of
this process.
4.2 Derive a state variable model for the translational mechanical system
of Fig. 4.1 with the state variables extension of the spring x(1), and velocity of
the mass v(f).
4.3 The figure below shows a left ventricular pressure-volume curve,
simulated with an elastance function similar to the one of Eq. (4.31) and
Fig. 4.5 Goodwin, 2004)
Ventricular
pressure
a
a EMIN
# > Ventricular
uy volume
Figure 4.8 Graph for review problem 4.3.
identify the phases of the cardiac cycle in this diagram: filling, isovolumetric
contraction, ejection, and isovolumetric relaxation
79

## Page 45

80
Theory
References and Further Reading
Athans M. Systems, networks and computations: Multivariable methods. New York:
McGraw-Hill, 1974.
Beneken JEW, DeWit B. A physical approach to hemodynamic aspects of the
human cardiovascular system. In: Reeve EB, Guyton AC, eds. Physical
bases of circulatory transport: regulation and exchange. Philadelphia: Saunders;
1967:1-45.
Brady JE, Russell JW, Holum JR. Chemistry: Matter and its changes. 3" ed. New York:
John Wiley & Sons; 2001.
Chiari L, Avanzolini G, Ursino M. A comprehensive simulator of the human respiratory system: validation with experimental and simulated data. Ann Biomed
Eng. Nov-Dec 1997; 25(6):985-99.
Cutnell JD, Johnson KW. Physics, 4th ed. New York: John Wiley & Sons; 1998.
Goodwin JA, van Meurs WL, $4 Couto CD, Beneken JEW, Graves SA. A model for
educational simulation of infant cardiovascular physiology. Anest Analg. Dec
2004; 99(6):1655-64.
Grodins FS, Buell J, Bart AJ. Mathematical analysis and digital simulation of the
respiratory control system. J Appl Physiol. Feb 1967; 22(2):260-76.
Halliday D, Resnick R, Walker J. Fundamentals of physics. 6 ed. New York: John
Wiley & Sons; 2001.
Khoo MCK. Physiologic control systems, analysis, simulation, and estimation.
Piscataway: Wiley-IEEE Press; 1999,
Ljung L. System identification, theory for the user. 2°4 ed. Upper Saddle River, NJ:
Prentice Hall; 1999.
Mapleson WW. An electric analogue for uptake and exchange of inert gases and
other agents. Appl Physiol. Jan 1963; 18:197-204.
Nikkelen E, van Meurs WL, Ohrn MAK. Hydraulic analog for simultaneous
representation of pharmacokinetics and pharmacodynamics: Application to
vecuronium. } Clin Monit Comput. Jul 1998; 14 (5):329-37.
Roberts MJ. Signais and systems: Analysis of signals through linear systems. Boston:
McGraw Hill; 2003.
Suga H, Sagawa K, Shoukas AA. Load independence of the instantaneous pressure-volume ratio of the canine left ventricle and effects of epinephrine and
heart rate on the ratio. Cire Res. 1973; 2:314 -22.
Van Meurs WL, Nikkelen E, Good ML. Pharmacokinetic-pharmacodynamic
1 for educational simulations. IEEE Trans Biomed Eng. May 1998
5(5):582-90.
Zwart A, Smith NT, Beneken JE. Multiple model approach to uptake and distribution of halothane: the use of an analog computer. Comput Biomed Res. Jun
1972; 5(3):228-38.
CHAPTER 5
Software
Implementation

## Page 46

of the continuous-time state equation, based on the definition of
the derivative. Algorithms for off-line and (pseudo) real time
software implementation of a state variable model are given.
Grouping and sequencing of model equations is of particular
importance when connecting state variable models. To avoid circular
references when feedback occurs, at least one of the models should
not have immediate throughput from the input to the output.
Different integration step sizes in two connected models can be
accommodated via separate branches in an algorithm.
Input-output requirements are formulated in the form of an
overall model block diagram, and an explicit list of input and output
variables (see Chap. 2). Internal system structure and functions to be
included in the model are reflected in a conceptual model, which can
take the form of a block diagram of subsystems and/or of component
diagrams (Fig. 3.10). For the subsystems, a mathematical model in the
form of a continuous-time state variable formulation can often be
formulated (Chap. 4).
[: this chapter we present a simple discrete-time approximation
a(t) = f(t), ult), £) (5.1)
u(t) = g(a(t), ut), £) 62)
in this chapter we will see how these equations can be
implemented in software on a digital (discrete-time) computer, and
how subsystems can be combined. We will only make programming
lang uage-independent observations.
5.1 Discretization of the Continuous-Time State Equation
The output equation (5.2) can be implemented “as is.” A simple
dincreto-time code implementation of the state equation (6.1) is based
oo

## Page 47

84
5.2
Theory
on the definition of the derivative:
c(t) = li 5.3
x(t) lim 7; 6.3)
Combining Eqs. (5.1) and (5.3) we find
x(t +T) = x(t) +T f (x(t), u@),t) (54)
In its definite form Eq. (6.4) can be initiated with x(f,) and applied
iteratively fort =f), t,+ TZ ty* 21,...ort=t,+ nT, where 11 is the discrete
time and T the integration step size. T should be small as compared to
the fastest system dynamics to lead to a good approximation of the
derivative and to precise integration, but not so small that the
simulation time becomes prohibitively long or that the accuracy of
the increments of the state or time variables is limited by word length.
This basic method of integration is called the Euler forward method.
Textbooks on numerical integration discuss this method, as well as
more accurate and efficient methods (see, for example, Chapra, 2010).
For certain models, if the input u(t) is constant over the time interval
T, an exact prediction can be computed (see Ljung, 1999).
Throughout this chapter we will assume that the sampling interval
of u(f) is identical to the integration step size. Reconstruction of y(f) from
its samples, again assumed to be spaced at intervals that are identical to
the integration step size, will involve interpolation. Interpolation
routines, for example, zero-order hold or linear interpolation, are often
implicit to hardware implementations or plotting routines, and will
greatly affect the frequency content and appearance of a signal
Basic Algorithms for Implementation of the
Discrete-Time State Variable Model
We first consider a simple algorithm for off-line or non-real time
simulation of a state variable model. At the start of the program, a
number of quantities need to be set or initialized: the integration step
size T, the simulation start and stop times f = f, and t,, the model
parameters, and the initial state x(/,) (Fig. 51).
We assume that input u(t) is available for f 2 t,, either as an array
of values, or in the form of an analytical function. Then the output
equation (5.2) can be computed for time f = #,. Note the use of “=” to
indicate an assignment. It is possible that t, = {,, in which case the
simulation is over, and simulation results can be plotted. In this case
the “plot” would be reduced to a single value for all variables of
interest. An alternative to plotting data inside the program is to save
them, and plot them later with another program If the simulation
time is not over, the state prediction
yb Te (Dt TPO),
HD (8,5)
Software Implementation
Start
Initializations
Pl
X(t4T)= x(t)-+TA(x(t)
u(t) ,t) AA
X(t):= x(t+T)
t= t4+T End
[|
Fieure 5.1 Flow diagram for off-line sof i
ee nod ‘tware implementation of a state
can be computed. Here, the assignment takes its full meaning: For a
vector of state variables, x(t + T) is a different (code) variable from x(t)
Otherwise, for example, for a second-order system, the computation
of x,(f + T) would be based on x, and x,(), and the computation of
x,(E+ T) on x, + T) and x,(f). In preparation for the next iteration, the
state variable and time need to be updated: ‘
x(t) = x(t+T) (6.6)
t=t+T (5.7)
In this simple algorithm there is no specific assignment for discrete
time 1. However, in practical code implementations, branching and
storage and retrieval of data may be facilitated by maintaining
We will continue to refer to continuous time ¢ in the BasloramenEs
ae note that Eqs. (5.2), (5.5), (5.6), and (5.7) are often written as
OHOWS;:
VOD i @OVOD, MD, ID) (5.8)
85

## Page 48

86
5.3
Theory
x(n + 1) = x(0) + T f(x), un), 1) (69)
x(1) = x(n +1) (6.10)
n=nt+l (5.11)
Unlike what is suggested by this notation, in the algebraic functions f
is substituted by nT, not by n
With the above algorithm, the simulation will run as fast as the
model, the integration step size, the structure of the code, the
programming language, and the computer hardware allow for.
However, several simulation applications require a model to run in
real time, or in a specified acceleration or deceleration of real time.
For demonstrations, pseudo-real time, a reasonable approximation
of real time on a specific computer, may be sufficient. The algorithm
of Fig. 5.1 can be expanded as indicated in Fig. 5.2 to meet such
requirements. After initializations, the computer “waits” for
continuous time to be an integer multiple of the integration step
size. This can be implemented via interrupts or scheduling
algorithms, or in pseudo-real time via a computer specific cycle in
the False branch that takes a time T - T,.to run, where T,, is the
average computation time for the remainder of the loop. Real time
input and output should be grouped around the output equation,
and the ensemble should occur immediately after the timing routine
to minimize potentially variable time lag with respect to time ft. The
end of the simulation may now depend on specific user commands.
Based on simulation requirements, these algorithms may be
expanded with file, user interface, or peripheral device input and
output
Model Code Ver ication
The above algorithms, when correctly implemented in software,
should avoid problems due to incorrect sequencing of model
equations. But when writing software to implement a mathematical
model, several other errors can occur: The equations may not be
implemented correctly, the numerical values for parameters or the
initial state may be incorrect, or the integration step size may be
inadequate. Basic precautions include matching names of quantities
between the mathematical model and the software, and careful
verification by a qualified, preferably independent, person. Some
differences in symbols are to be expected, as the mathematical model
uses compact, standard mathematical and physiological notation,
whereas longer names may have to be used in programming
languages, which usually do not have the possibility to use subseripts
or superscripts. Remaining errors may be detected when verifying,
model code functionality via selected simulation reaulie, Por apeettic
5.4
Software Implementation
| Start
Initializations
; gf Input u(t) PA
iets
tL False
X(t+T)= x(t) + TF(x(t),U(t).0) i
X(t)!= x(t+T) | End
t= t+T
Figure 5.2 Flow diagram for (pseudo) real-time software impiementation of a
state variable model.
inputs, steady state or dynamic responses may have analytical
solutions. Simulated numerical values or curves can be compared to
those. If the model code is part of a larger, more complex software
project, an effort should be made to keep it modular, so that it can be
tested independently. In the next chapter we will come back to mode!
code verification as part of the more encompassing model verification
and validation.
Connecting State Variable Models
Now assume two models that interact, with part of the input to the
second model coming from the first (Hig, §,3)

## Page 49

88
Theory
Yzolt) — Ug oft)
Model 2 yo(t)
Ficure 5.3 Block diagram of two connected models.
For example, consider lung mechanics driving pulmonary gas
exchange (Fig. 3.5). To simplify the discussion of grouping and
sequencing model equations, we will assume that all output from
Model 1 goes to Model 2, and that Model 2 does not have other inputs,
leading to the block diagram (of Fig. 5.4).
Let us further assume that for the two systems we want to
maintain separate mathematical models and code in distinct
segments.! Initially, we assume that the integration step sizes for the
two models are identical:
T=h=T (6.12)
We assume that input u,(/) is available. Let the output equation
for the first model be:
yl) = gy @),t44) (6.13)
For notational compactness we drop the time-variant notation from
here on. The models are connected via the equation:
u(t) = y(t) (6.14)
and the output equation for the second model is:
yo(t) = go (xp (4), uo) (5.15)
These three equations can be computed in the presented order, which
closely reflects the block diagram. The reader can verify that any
other order would lead to forward references. For an off-line software
implementation, we elaborate on Fig. 5.1, resulting in Fig. 5.5. As in
Fig. 5.1, computation of the state prediction needs to precede the state
and time updates. This represents the only constraint on the order of
these equations, which can be grouped per model (as in Fig. 5.5) or
per equation type.
1 Otherwise a new single model with a state variable vector PewHliing Fran the
coneatenation of Y (0and x () ¢ ould be derived
Software Implementation
v x9(0)
3 ya(t) Ualt)
u(t) ——» Model 1 >» Wiodel 2 -H—p yoit)
Figure 5.4 Simplified block diagram of two connectec models.
Start
Initializations
ya (t)s= 84 (X1(t),U4(t))
Us(t):= y(t}
Yalt):= Bo(Xo(t),Uo(t))
a
Plot graphs
+7)
Xolt)+ Tho(Xo(t),Ualt))
Xo(t+T}
IGURE 5. ow diagram for off-line software im| ti n nse €
Fi 55 &F d for off. if e impiem
f plementation of i ies stat
; This algorithm can easily be generalized to more than two models
in series. Now let us assume that there is feedback from Model 2 to
Model 1, maintaining the simplification concerning the absence of
external input or output (Fig. 5.6).
For example, consider the cardiorespiratory system and control
of breathing (Fig. 3.6). We add the connecting equation
y(t) = Yo(t) (5.16)
89

## Page 50

x4(0) X20)
| yatt) a(t) |
U,(t) Model 4 Model 2 Yolt)
Figure 5.6 Simplified block diagram of two connected models with feedback.
Equations (5.13)—-(5.16) cannot be computed in the presented (or any
other) order, because of a circular reference. For example, substituting
Eq. (5.16) in Eq. (5.13), Eq. (6.13) in Eq. (5.14), and Eq. (5.14) in Eq. (5.15),
we find
Y(t) = Bo (X(t),
By(%4 (1), Yo) (5.17)
with a circular reference to y,(t). If such circular references occur,
they are often the result of a modeling error. To avoid them in the
presented example, at least one of the models should not have
immediate throughput from the input u(f) to the output y(t), for
example, Model 1:
y(t) = g(a (8) 6.18)
Output and connecting equations can now be computed in an
order that avoids forward and circular references and that still closely
reflects the block diagram (Fig. 5.7). The state predictions and state
and time updates are the same as those in Fig. 5.5.
Elaborating on the feedback example, we now consider the case
in which Model 2 uses an integration step size T,, which is an integer
multiple of T,; that is, the equations of Model 2 can {and should) be
computed at a lower frequency than those of Modei 1. This would be
the case for the chosen example: the cardiorespiratory system and
control of breathing (Fig. 3.6), where the control of breathing model
would only have to execute once per respiratory cycle. Note that T,
can be variable. The algorithm needs to verify whether t —t, = nT, is
a multiple of T,, before computing Model 2 equations (Fig. 5.8).
Going from the high-frequency output y,(f) to the low-frequency
input u,(f) involves sampling or averaging. Going from the lowfrequency output y,(f) to the high-frequency input w,(f) involves
interpolation, for example, zero-order hold or linear interpolation.
Also note the use of T, in the state prediction tor Model 2. In this
algorithm there is no specific f= f+ T, assignment and the incre
times1 and mare not explicitly maintained, We Lirther observe that
Software Implementation
Start
Initiatizations
False
Xq(t):= X4(t+T)
Xo(t#T) = Xolt)+Tfo(xo(t),Uo(t})
Xo(t) = Xo(t+T)
fo Plot graphs F
betty
End
Figure 5.7 Flow diagram for off-line software implementation
? of sti
modeis with feedback. : severable
| Xy(tFT)= xq (CTH
(x4 (t), U4 (t))
l
the change from identical to different sampling intervals is not
visible in the block diagram (Fig. 5.6) but has a considerable effect on
the flow diagrams (Figs. 5.7 and 5.8). In the algorithm of Fig. 5.8
code for the two models is divided over five distinct segments,
which is not conducive to modularity. This algorithm may be
simplified in several situations. For example, when Model 2 is static
there is no state prediction for that model, and the second t.
branching disappears. :
We remind the reader of two simplifying assumptions applied in
this section: the absence of external inputs and outputs in all three
considered cases, and the absence of immediate throughput in Model
1 for the last two. Absence of immediate throughput in Model 2 leads
to fairly trivial changes in the equations and algorithms.
Generalization to the case including exterhal inputs and outputs
requires careful writing out of the continuous-time equations
corresponding to the block diagram of Bip, 59.
91

## Page 51

2
Theory
Start
Initializations
x
yalt)= 84(x4(t))
True
t-to =mT2? 1
Ua(t)= ya(t)* |
Yalt)= Eo(Xp(t),Ug(t))
False
tate? True
False
“SS True
t-ig=mTg? -
Xo(t+Tali= Xo(t)+Tofo(xo(t) Ualt)))
False | Xo(t):= xalt+T2)
J
Xq(t+T4):= X4(t)+T
Fy (x q(t) Ug (t))
X4(t)= X4(t+T4)
= t4+T,
Ld
Ficure 5.8 Flow diagram for off-line software implementation of state
variable models with feedback and different integration step sizes. Plot graphs
and algorithm end as in Fig. 5.4. *see main text.
Software Implementation
x4(0) x2(0)
Uy oft) Yzolt) — Ug,o(t) Yo,olt)
> > > >
Model 2 Model 2
Uz a(t) [" Ya alt) Up, 1(t) | Yoalt)
Figure 5.9 Block diagram of two connected models with feedback.
For example, for Model 1:
HO = fy), ) 6.19)
where:
{M0 =
w= (5.20)
and:
Yi ob) = %0(@),
4 ()) (6.21)
Y42(b) = S204), (6) (5.22)
paying close attention to potential immediate throughput from
the u, ,(f) part of u,(f) to y, ,(). Then the corresponding discrete-time
equations need to be added to appropriate locations in the algorithm,
in terms of references and calling frequencies.
Review Problems
5.1 Select an algorithm for a code implementation for validation of the
mathematical model of the uncontrolled cardiovascular subsystem, derived
as part of Review Problem 4.1. Does the software have to run in real time?
Make sure that the user interface allows you to reproduce experiments and
present data reflecting the validation data. Implement this algorithm in @
programming language of your choice. Verify the code and its operation.
5.2 Discretize, program, and simulate the state variable model of Sec. 4.2,
using the algorithm of Fig. 5.1, Parameters: R=1,L=1H,C=1 F Initial
state variables: v(t.) = i(¢,) = 0. Input: e(f) = 1 V for 0 <# < 20s, 0 V otherwise.
Plot the output variable v,(f). How did you select the integration step size
T? Experiment with parameter variations; predict the expected changes in
response first,

## Page 52

QL Theory
mini SP Mb RR a oa
References and Further Reading
Chapra SC, Canale RP. Numerical Methods for Engineers, 6" ed. New York:
McGraw-Hill; 2010.
Ljung L. System identification, theory for the user, 2" ed. Upper Saddle River, NI:
Prentice Hall; 1999.
CHAPTER 6
Simulation Results
and Model Validation

## Page 53

Honinmnoneie
6.1
odel verification targets several, relatively simple aspects
of model quality. A model is considered conceptually valid
if incorporated theories, assumptions, and data are
reasonable for the intended purpose. A model is considered
operationally valid for a set of experimental conditions if its accuracy
is acceptable for the intended purpose. Measures of accuracy can be
based on comparison of time or frequency domain features of system
and model outputs. Operational validity can be based on target data
obtained on human subjects or from animal experiments, or by
presenting simulation results to clinical experts. The used evaluation
method depends greatly on the intended purpose and. available
resources.
Definitions and Overall Procedure
In this chapter we consider the quality of a model used in simulation.
Model is used here in a generic sense, including conceptual and
mathematical models, code implementation, and simulation results.
We distinguish between to verify—“Conclusively demonstrate by
presentation of facts or by sound reasoning or argument”—and to
validate—“Corroborate or support on a sound basis or authority”
(Webster's third new international dictionary, 2002). Model verification
targets several, relatively simple aspects of model quality, such as
inclusion of all required input and output variables, correct derivation
of model equations based on a conceptual model and physical laws,
and correct implementation of model equations in code. Verification
leads to unambiguous, factual results, often in the form of a yes or no
answer. Model validation targets other, more complex aspects of model
quality. For example, are the simplifying assumptions reflected in
the structure of a conceptual model justified in view of the intended
purpose? Validation often refers to more
or less subjective obyservations
by experts, anc is by nature a gradual notion; we may speak of
9]

## Page 54

O&§ Theery
degrees of validity. For mode] validation, we further distinguish the
quality of what was put into a model and the quality of its behavior:
¢ A model is considered conceptually valid if incorporated
theories, assumptions, and data are reasonable for the
intended purpose.
A model is considered operationally valid for a set of
experimental conditions if its accuracy is acceptable for the
intended purpose.
A central role in all considerations on verification and validation
is played by the “intended purpose” as reflected in the model
requirements. In these definitions, the subjective aspect of validity
becomes apparent in the use of the words “considered,” “reasonable,”
and “acceptable” (by whom, to whom, according to which criteria’).
Both definitions refer to a single model; multiple coupled models
should, as much as possible, be validated in isolation first. Conceptual
validity mainly concerns the conceptual and mathematical models,
whereas operational validity refers to simulation results and target
data. Therefore, the basis for conceptual validity is jaid during the
modeling process, while operational validity is established at the
end of the modeling process, with a completed model, before it is
used in practical simulations. Conceptual validity is often established
by model developers, whereas operational validity is increased when
carried out (or at least verified) by independent evaluators or mode!
users. Input from physiologists and clinicians may be of use in
establishing both conceptual and operational validity, but a natural
focus would be that of physiologists on conceptual ‘matters and of
clinicians on operational matters. Model verification and conceptual!
validity involve meeting requirements, as presented in the previous
chapters. The focus of this chapter is on simulation results and
operational validity. In subsequent sections we elaborate on
“accuracy,” which refers to a quantitative or qualitative comparison
between target data and simulation results, and on the “set of
experimental conditions,” which points to a necessarily limited,
range of model validity. :
Documentation is central to model verification and validation. If
models are evaluated by professionals who are not part of the
development team, and possibly do not havea modeling background,
then a summary of model attributes and a critical assessment of
those with respect to the model requirements, as formulated in Chap.
“r greatly contributes to model verification and validation, Table 6.1
lists anumber of questions that can be addressed in such a summary,
Some questions on operational validation will be further elarified in
subsequent sections. This list refers toa newly devi loped model, tha
pres iously developed moclel is reused, for exaripile, far a clifferent
patient population several verification ahd Valilaliad qieetionia may
|
L.
Simulation Results and Model Validation gg
f
| Verification
_—_——
| Were all required input and output variables included?
| Do they have appropriate units, r.
|
_ resolution, and bandwidth?
: Are the required anatomical structures and physiological processes includec
i e conceptual model?
correct derivation and implementation of model equations verified?
|
| Was adequacy of integration method and step size verified? This may invoive
| a range of parameter values.
| De simulation results match known analytical solutions or steady-state
1
| results?
L Does the model code run fast enough for the envisioned application?
\ Was the model adequately verified?
Conceptual validation
fia
What simplifying assumptions were made concerning structure, and what was
their justification?
| What simplifying assumptions were made concerning function, and what was
| their justification?
Does the level of representation detail match the objectives?
: What underlying laws and principles were used, and was their use
appropriate?
What assumptions were made in deriving the mathematical model, and what
was their justification?
What assumptions were made for parameter estimation, and what was their
justification?
| What data were used in parameter estimation, and were the data appropriate
in view of the objectives?
Are the resulting parameter values physiologically plausible?
i Were physiologists knowledgeable in the domain of the model consulted?
What was their opinion’?
conceptually valid? Ol
is the model considered
Operational validation
What are the patients, pathologies, conditions, incidents, and interventions
the model needs to be validated for?
Are target data on human subjects available for these situations?
If not: are target data on animal subjects available for these situations, and
can the data be scaled?
Were clinical experts who have been exposed to these situations consulted?
What was thelr opinion?
Tanie G4 Oueatlone Gone arming Physiologic Model Verification and Validation

## Page 55

WY
Do experimental conditions of the model reflect those of the larzet data’
_ What measure of accuracy was used’i
“Are the results considered acceptable inin viewv of the project objectives?
Is the model considered operationally valid for the listed situations”?
Was model behavior explored beyond the available target data? Was it
considered plausible? oO
Taste 6.1 Questions Concerning Physiologic Model Verification and Validation
(continued)
have already been answered. In general, the list should be amended
based on specific project needs.
This rather extensive list shows that validity has a cost. Depending
on the phase of model development or use, increasing levels of validity
may be required, and certain elements of the list may be revisited, or
the range of validity may be expanded, for example, via model
modifications enhancing conceptual validity, or inclusion of additional experimental conditions broadening the range of operational
validity. A cost-benefit analysis could consider development or
evaluation costs and the value of a sought-after increment in validity.
A physiologic model is rarely designed and evaluated in isolation;
its requirements are embedded in more general project goals, and
evaluation of conceptual and operational validity refers back to these
requirements. Additional quality questions arise around the use of a
model in a simulator. For example, modularity and interaction with
other functional units, such as other models or simulator hardware and
user interfaces, become important. As argued in Chap. 2, the quality of
such interfaces will influence the overall impact of a model-driven
simulator. In Chap. 12 we will explore this broader perspective further.
With time and use of a simulator, model applications may evolve
beyond the originally intended purpose, and model and simulator
validation in new experimental conditions may be necessary and can
lead to modifications. A dramatic illustration of this observation is
the use of a model-driven simulator, designed and developed
between 1986 and 1996 for training of anesthesia residents, for totally
unanticipated post 9/11 disaster medicine drills. For additional
information on verification and validation of simulation models we
point to Sargent (2007).
6.2 | Quantitative and Qualitative Methods for
Establishing Accuracy
The principle of establishing operational validity is visualized in
Fig. 6.1.
cs) 8 BE Baa SB Oe Be A BE Oe 2 eee 2S 8 Bee Se 2 eee
Vall)
— |
u(t) ———— X(t) (> th
> Model ——
Ym(t)
Figure 6.1 Principle of establishing operational validity.
The system and its model are assumed to be in identical initia]
conditions. Then the same input is applied to both, the model output
y,,(£) is subtracted from the system output y, (f, and the residual r(f) is
seen The target data [u(#),y,(Q] should not have been used
previously for model parameter estimation. The analysis of the
residual can be quantitative of qualitative. The residual can be
processed to lead to a measure of accuracy A, for example, for a
continuous-time system with a single output
£
Ay = = | LY. (E) ~ Yon (EDIdt (6.1)
Cg
dp, = Fllw0-~ Yon(t)) at (6.2)
(6.3)
T5 on
(t)
representing, respectively, the integral of absolute residuals, th:
integral of squared residuals, and the integral of normalized absolute
residuals. T represents here the total record length of the evaluated
data. A, applies only if y,(f) does not have zero values. These measures
can easily be adapted to multivariable and discrete-time systems.
Other measures of accuracy can be based on comparison of overall
time or frequency domain features of system and model outputs,
’ We reserve the term “error” for use in feedback control. Note that “residual” is
used here in a deterministic sense.
awe

## Page 56

such as autocorrelation and frequency reajie, Spectie features of
the output signals, for example, amplitudiaseline, ime ot peal
effect, and bandwidth, can also be usel) aceuraey measures
Simulated waveforms are more casily evaliwcl visually, by domain
experts. Such evaluations are qualitative
ther than quantitative,
although semi-quantitative resemblance ths can be established,
with or without explicit comparison tot) system outputs. For
examples of the latter, see Bastos (2011). hget data can also be
obtained from a more complete, previou\validated model. The
used evaluation method depends greatly tthe intended purpose
and on available resources.
ea
Range of Validity, Target Data, anixperimental
Conditions
As mentioned in Sec. 6.1, the range of operinal validity of a model
is determined by the set of experimental wlitions for which it is
validated. These experimental conditi« should match the
population, pathologies, conditions, incidenand interventions part
of the requirements (Tables 2.1 and 6.1). (en, our purpose is to
reflect a plausible patient, within normal intyatient variability (also
see Table 2.3). Some of these target data il reflect steady states,
whereas others will involve dynamic exptnents. A fundamental!
paradox of modeling and simulation, andot only in biomedical
engineering, is that we often want to expleunknown and potentially extreme, rare, and dangerous systemlhavior. Target data for
those situations, obtained in carefully contiled conditions, are not
always available. Another paradox is thatroften use a model to
represent dynamic systems with one or monmtinuous and possibly
interacting independent variables, Sec. 2.1he number of possible
combinations of input variables and respow is very large and not
all combinations can be expected to be valitkd.
If our model is for human subjects, aiif no target data are
available for that population, then data fromaimal experiments are
sometimes used. There are ethical concernsih carrying out animal
experiments, and even with using data im such experiments.
Moreover, validation is complicated by thict that model inputs
and outputs have to be scaled between spes, or two sets of model
parameters are required: one for the modeleluman, and one for the
species of the target data. Model validity isiestablished as clearly
as when using human target data. A third ojin for model validation
is to present simulation results, combined ti carefully formulated
questions, to clinical experts (also see theevious section). They
may not have had much exposure to rare, erme situations, and do
not always agree. We frequently use combi strategies for model
validation (see, for example, SA Couto, 200!kstos, 2011). As briefly
mentioned in the previous section, data usior validation need to
be independent from those used in parameter estimation, otherwise
we could aliinply be verifying that these data were correctly
incorporated into the model. We can distinguish an identification set
and a validation set.
The experimental conditions of the simulation model need to be
matched with those of the system yielding the target data. For
example, an initial state involving hypovolemia may a the
response of a patient to mechanical ventilation. Model ie . “e
be explored beyond the available target data, and may yiel use u
validity information. One example isa sensitivity analysis, where
one input or one parameter is varied at a time, and the effect on
output variables is observed. A sensitivity analysis im0 ee :
information about linearity, assist in parameter estimation, an
provide general indicators on model behavior. We will explore oe
method further in Chap. 11. It is also useful to evaluate the mo
response in extreme conditions, even if no target data are — e.
This helps in assuring that the model correctly implements boundary
conditions, for example, blood volume should not become negative
on blood loss.
Review Probiems
6.4 Compare the simulation results obtained with the code developed as
part of Review Problem 5.1 to validation data. Which comparison method(s)
did you use? What are the ranges of the input variables for which you have
reliable validation data? Comment on conceptual and operational validity
of the developed model. Does the model need to be improved? How ee
that be accomplished? What are the steps required to complete the mo “
and the code, and to transform it into a practical simulator for use in medica!
education?
6.2 Canamodel be conceptually valid, but not operationally valid, and vice
versa? What would cause such discrepancies?
References and Further Reading — a
Bastos ML. Mathematical models for educational simulation of uterine contrac
tions during labor [thesis]. Po xtugal: University of Porto; a —
S4 Couto PM, van Meurs WL, Bernardes JF, Marques de Sa JP, Goo a
Mathematical model for a of the oxygen delivery to
etus. Control Eng Practice. 2002; 1059-66.
_— RG. ectination and valictation of simulation models, in aoa i
‘et al. (eds): Proceedings of the 2007 Winter Simulation Conference, Pp - i
Zijlmans M, $4-Couto CD, van Meurs WL, Goodwin JA, Andriessen P. Correc
and improved model for educational simulation of neonatal men ar
pathophysiology [technical report}. Simul Healthc, Spring 2009; 4(1):49-53.

## Page 57

PART
Applications
CHAPTER 7 CHAPTER9
A Model of the Respiration
di irat te
Cardiorespiratory System CHAPTER 10
CHAPTER 8 Physiologic Control
Circulation

## Page 58

cardiorespiratory physiology. Qualitative requirements for our
model of the whole cardiorespiratory system include simulation
of a number of clinically monitored physiologic variables, and
simulation of appropriate reactions to the administration of fluid and
to re-breathing of carbon dioxide. We derive an overall conceptual
model in the form of a block diagram of the subsystems:
hemodynamics, lung mechanics, uptake and distribution, control of
circulation, and control of breathing.
In this part of the book we apply the theory introduced in Part I.
The goals of Part II are to further illustrate and expand presented
concepts and procedures and to provide the reader with a consistent
library of conceptual and mathematical models of the normal
cardiorespiratory system. As mentioned in the foreword, they
represent a simplified version of the cardiorespiratory models used in
the Human Patient Simulator (HPS®) and derived products (van
Meurs, 1997, www.meti.com). These models will be of intermediate
complexity, so that they can be either simplified or expanded for other
applications. We follow the top-down, goal-oriented approach to
modeling presented in Part L In the subsequent sections, we formulate
qualitative requirements for a model of the whole cardiorespiratory
system and derive an overall conceptual model in the form of a block
diagram of subsystems, following the procedures outlined in Sees. 2.1
and 3.1, respectively. This approach highlights the interconnectedness
of the cardiorespiratory system and will give the reader a framework
for future modeling projects in this area. In the subsequent chapters,
lE this chapter we present a framework for modeling projects in
the conceptual model of the cardiorespiratory system is deepened by
modeling the circulation via fluid circuit elements representing the
heart anc vessels, followed by a model for fluid mechanics of lungs
and alywaya, Addition of compartment models of respiratory gas
rit

## Page 59

ii0
Applications
transport and transfer functions representing control of circulation
and spontaneous breathing completes this process. Mathematical
models corresponding to these conceptual models are derived. These
models are all in state variable notation, so software implementation
can be based on the algorithms presented in Chap. 5. Most of the
presented models are referenced to the scientific literature; we point
to this for validation of individual models. Full integration of all seven
presented mathematical models in software and validation of
integrated operation are beyond the scope of this introductory text.
74
Model Requirements
For information on basic cardiorespiratory physiology we point to
the references in Chap. 2. Our main focus will be on normal
physiology, and we expect our model to react appropriately to
administration of fluid, for example, to evaluate the Frank-Starling
curve of the heart, and to re-breathing of carbon dioxide to test the
ventilatory response. We would like for our model to simulate a
number of key physiological variables that are also monitored
clinically, such as heart rate, pulsatile systemic and pulmonary blood
pressure waveforms, and cardiac output. On the respiratory side, it
should simulate tidal volume, respiratory rate, oxygen saturation in
systemic arterial blood, and the partial pressures of oxygen and
carbon dioxide in systemic arterial and venous blood. Table 7.1 and
Fig. 7.1 list and complete these requirements.
These requirements contain several simplifying assumptions.
Fo: example, the electrocardiogram (ECG), the plethysmogram,
airway pressures, blood pH, and hematocrit? are not considered
output variables and do not have to be modeled as such. In some
cases this means that the underlying structures and functions do not
have to be represented in the model, for example, electrophysiology
underlying the ECG. In other cases, it only means that variables are
assumed constant or that their evolution will not be displayed as an
output variable.
To be able to simulate the interaction between these variables,
internal structures and functions that should be incorporated include
the basic fluid dynamics of the heart and systemic and pulmonary
vessels; basic airway, lung, and chest wall mechanics; pulmonary
uptake and distribution of the respiratory gases oxygen and carbon
dioxide; and basic representations of the physiologic contro!
mechanisms of circulation and spontaneous breathing. We will focus
on short-term phenomena, roughly on a time scale from 2 to 300s,
ruling out, on the one hand, fast phenomena like beat-to-beat heart
' ‘The plothysmograny
ix the waveform
of the pulie Geli
2 Hematoerit
in the fractionof whole blood that la ceeupied ly fed tied gall
A Medel of the Cardiorespiratory System
Population
3, Physiological state of the
simulate subject
PA. Pathologies _ None
|ea ves
5. Monitored variables and
clinical si
Critical incidents
Is
| 7. Interventions
“Fluid administration, re-breathing_ |
of CO,
8. Overall block diagram | Fig. TL
| 9. Internal structures ana See main text
| functions
Taste 7.1 Qualitative Model Requirements
ete Heart rate
t———-» Systemic blood pressures
|» Pulmonary blood pressures
Fluid administration
——>| Model of the t+—— Cardiac output
cardiorespiratory t——> Tidal volume
Insp. carbon dioxide ——>; system +——» Respiratory rate
+» Arterial oxygen saturation
}+-——-» Partial pressures of oxygen
i aad Partial pressures of carbon dioxide
Figure 7.4 Overall block diagram of the cardiorespiratory model.
1.2
rate variability, and on the other, slower dynamics of fluid balance
and endocrine aspects of physiologic control mechanisms.
Conceptual Model
To come to a conceptual model of this rather complex system, we take
as our starting point the graphical representation of the
cardiorespiratory system (Fig. 3.2), to which we add the control of
cireulation.® We observe that the system involves volume, concentration, and action-potential-type variables. Respiratory gases are
transported by both blood and gas. Control systems affect the
Al (Hin etage of mioceling, a search for published models would be warranted,
vnc level to rang Peeulis, but for dicaetic reasons we will build the conceptual
iocel Geom Hie peeund ap
il

## Page 60

112
Blood
Applications
circulatory and respiratory systems. Using these criteria, the identified
internal structures and functions can be divided in causally connected
subsystems as in the block diagram of Fig. 7.2. The circulation of blood
is influenced by ventilation via the intrapleural or intrathoracic
pressure. Control of breathing mainly depends on blood gases.
Control of circulation depends on those, as well as on blood pressures.
However, the influences of blood gases on the circulation only play a
minor role in the interventions that we would like to simulate, so they
will not be considered further. For this system, and at this level of
conceptual modeling, separation along anatomical lines, also indicated
in the block diagram, plays a more limited. role. To keep oversight,
only connecting variables are indicated in the diagram, and are given
generic names. Table 7.2 associates the input and output variables of
Fig. 7.1 with the subsystems of Fig. 7.2
By considering fluid administration as an input to the
hemodynamic model, we make the simplifying assumption that the
fluid does not affect the oxygen carrying capacity of the blood, part
of the uptake and distribution model. The input and output variables
of the overall block diagram are measurable by design, per the
requirement on clinically monitored variables. Specific instantiations
of the generic variables included in the block diagram may not always
be measureable. For example, depending on the choice of a specific
structure for the uptake and distribution model, the blood flow rates
and volumes may not be directly measurable. Activities of the
sympathetic and parasympathetic nervous systems are useful
concepts when discussing cardiorespiratory control, and their
Volume : Concentration ; Action potential
ventilatory control effectors
i} Gas flow rates Systemic arterial |
ras umes
LJ Lung and volumes Tyetake and [bloodgases [ Gontrolof | |
| mechanics distribution Hi breathing
| Senin '
] ‘ Respiration
intrathoracic pressure 1
' fo sateen eeece reno cnt eeeanneenn
ace
\ '
| ‘ Circulation
Blood flow rates H
and volumes s Control of
IHemodynamics| circulation
Systemic biood pressures
Cardiovascular control effectors
Nervous ayaten
Heart and vessels
Fiaure 7.2 Block diagram of the carciorespiratory syaleny ald subayelen) Beparation
criteria (dashed lines)
A Model of the Cardiorespiratory System
Overall inputs | To
Fiuid administration _ HD
Inspired carbon dioxide | UD : ~
Overall outputs From
Heart rate . a CC, together with other control effectors i
Systemic blood pressures HD
Pulmonary blood pressures. CHD oo
Cardiac output HD, together with other blood flow rates
|_ Tidal volume LM, implicit in gas flow rates and volumes
CB, together with other control effector
Respiratory rate
Arterial oxygen saturation UD
Partial pressures of oxygen uD
Partial pressures of carbon dioxide UD. :
HD, hemodynamics; UD, uptake and distribution; CC, control of circulation; LM, lung
mechanics; CB, control of breathing.
Taste 7.2 Overall Input-Output Variables and Associated Subsystems
representation is essential when modeling relatively fast phenomena
like beat-to-beat heart rate variability, but this is not a requirement
for the present model. The block diagram clearly divides the
circulatory and respiratory loops, and shows the main connection
between them, namely, hemodynamics driving pulmonary uptake
of respiratory gases and their distribution via the circulation. It also
shows secondary connections, withintrathoracic pressure influencing
the circulation and arterial blood gases influencing control of
circulation. Structures and functions that are not included in the
block diagram, besides the already mentioned electrophysiology of
the heart, are, for example, a fluid balance, the effect of lung stretch
receptors on control of breathing, a myocardial oxygen balance, and
local control of vascular beds. If, however, inclusion of such systems
were part of the requirements, the block diagram could easily be
expanded to accommodate that. A quite similar conceptual model
(van Meurs, 1997) needed only minor adaptations to also model drug
influences on the cardiorespiratory system. In the subsequent
chapters we will present conceptual and mathematical models for all
five blocks of Fig, 7.2.
Reference and Further Reading
Van Moura WE, Good ML, Lampotang8, Functional anatomy of full-scale patient
Hato | Ol Monit Beploor, (VS) aL%-24
1B

## Page 61

CHAPTER 8
Circulation

## Page 62

n this chapter we further specify the requirements of the pulsatile
hemodynamic model. We introduce a conceptual model consisting
of an elastance generator and a model for basic hemodynamics.
The latter is represented by a hydraulic component diagram.
Complete mathematical models for both subsystems are presented.
The model for the basic hemodynamics is shown to have a state
variable form.
8.1
Model Requirements .
From Fig. 7.2 and Table 7.2 we obtain the overall block diagram of the
hemodynamic model shown in Fig. 8.1.
Table 8.1 further specifies the input and output variables. In this
part of the book, we focus on conceptual and mathematical models.
Therefore, indications of range, resolution, and bandwidth, which
play an important role in code implementation and interfacing, are
omitted.
Fluid administration and intrathoracic pressure are given in
typical units used in clinical practice and modeling of lung mechanics,
respectively. We model control of circulation via four effector
variables: heart rate, myocardial contractility, systemic arteriolar
resistance, and venous unstressed volume. This choice includes the
assumption that, for the intended purpose, control of circulation can
be represented via relatively easily observable physiologic variables,
without a more detailed representation of the autonomic nervous
system. Myocardial contractility is given in (maximum) elastance
units (also see Sec. 4.4). Heart rate and myocardial contractility,
as defined above, only have a value once per cardiac cycle. This is
not the case for the two additional control effectors, which are
Fluid administration ——>} }—» Systemic and pulmonary blood
intrathoracic pressure ——p| Hemodynamics pressures
Cardiovascular control effectors ——»| t-—+> Blood flow rates, incl. cardiac
output, and blood volumes
Faun 8 Overall blogk diagram of the hemodynamic model.
WW

## Page 63

118 Applications
_ contractility
Input variable | Symbol | Unit | Origin |
Fluid administration | fA) | mi/min External input
Intrathoracic pressure | p,At) _ | “cm H,0 ~Lungmmechanics
“Heart rate. 7 | Bean ~t min _ _ Control of circulation
“Myocardie me(n) mm He/mi Control of circulation
" Systemic arteriolar
|
mm Hg External
| Central venous blood mm Hg External
pressure
Pulmonary arterial P,
» (0) mm Hg » External
blo pressure L
Pulmonary capillary newt) » mm He / External
wedge pressure : |
_Cardiac output co(k) L/min : External
“Pulmonary tissues ml/s “Uptake and distribution
blood flow rate L
| Arteriai pool blood : ey ( : mi/s “Uptake and distribution
_flow rate |
Systemic tissues FAO | mi/s Uptake and distribution
blood flow rate |
_fesistance |
| “Venous unstressed vA} mi Control of circulation
» volume
Output variable Symbol | Unit Destination |
Mean arterial blood map(n) ; mm Hg | Control of circulation
i. | i
| Venous pool blood | St) / mi/s Uptake and distribution
_fiow rate * \
Ar terial pool blood ' Veplt) mi Uptake and distribution
volume i
Systemic tissues | vi) i omt t Uptake and distribution
blood volume | |
Venous pool blood | v(t) mi | Uptaxe and distribution
[ volume
Here n represents the cardiac cycle, and k intermittent sampling to obtain cardiac
output
Tasle 8.2 Input and Output Variables of the Hemodynamle Modal
Circulation
continuous-time variables, but defining them as discrete-time
variables avoids a hybrid formalism of the control of circulation
model, also facilitating software implementation. We further assume
that the only hemodynamic variable that affects control of circulation
is mean arterial blood pressure, which is also available once per
cardiac cycle. In Chap. 10 we will come back to these assumptions,
and provide references to the control of circulation model. The output
pressures correspond to clinically monitored waveforms. Central
venous pressure can be measured in various locations, but is defined
as right atrial pressure. Pulmonary capillary wedge pressure is
measured via inflation of a small balloon at the tip of a catheter
blocking one of the pulmonary arteries. Via a static fluid column, the
pressure in the pulmonary veins is measured. Cardiac output is
sampled intermittently, forexample, viameasuring blood temperature
in the pulmonary arteries, after upstream injection of a bolus of cold
fluid. The thermodilution gives an indication of flow rate. It is given
inclinical units. Anticipating the design of the uptake and distribution
model (Chap. 9), we consider that, for the purpose of our model,
respiratory gas exchange can be adequately reflected via four
perfused homogeneous compartments: pulmonary tissues and
alveolar space, arterial pool, systemic tissues, and venous pool. Gas
content in pulmonary blood will be ignored. These considerations
result in the listed output variables. These flow rates and volumes
are rarely monitored as such, so we assign units that are convenient
for modeling. In Chap. 9 we will come back to the use of pulsatile
versus average flow rates and volumes.
Only compound pulmonary and systemic flow rates are required;
these blood flows are not divided over separate left and right lungs,
or over different organs or tissue groups. This requirement makes it
likely that the model will not be designed to include such flow rates
either. If flow rates and blood volumes in specific organs or tissue
groups can be considered a fixed fraction of total flow rate and
volume, then they can be computed as such. If not, for example, when
modeling local control of coronary or brain circulation, the
requirements need to be expanded, and additional organs or tissue
groups need to be added.
Conceptual Models
A relatively simple pulsatile hemodynamic model that meets most of
the input-output requirements was among several conceptual and
mathematical models presented by Beneken (1965). More recently it
was described and used in a new application by Goodwin et al.
(2004), This model separates the electromechanical processes, which
are responsible tor the generation of the time-varying elastances of
the heart chambers, from the basic hemodynamics (Fig. 8.2).
119

## Page 64

120
Applications
fralt) +—> mapin)
p(t) > —>
sart(") '
Yuin) Basic '
hemodynamics
hr(n) ——> Elastance :
eho generator >| a be
vp\t!
Cialt), Cip{t), Cpalt), ert)
Fieure 8.2 Block diagram of the hemodynamic model. See Table 8.1 for
output variables.
An empirical elastance generator uses the input variables heart
rate and myocardial contractility, which are available once per cardiac
cycle, to parameterize the continuous-time elastances for all four heart
chambers (also see Sec. 4.4). Figure 8.3 shows a component diagram for
the basic hemodynamics, with some minor adaptations with respect to
the Beneken model, using the circuit elements of Table 4.6.
The adaptations concern the separation of the systemic tissue
resistance in a variable arteriolar and a fixed venular part, and the
addition of a compliance containing blood volume in the systemic
tissues. The first adaptation provides an explicit element for the input
variable: systemic arteriolar resistance. The second adaptation
facilitates coupling the hemodynamic model with the uptake anc
distribution model described in the next chapter. Other input variables
affect this model as follows: Fluid can be administered intravenoush
via a catheter in the extrathoracic systemic veins. The intrathoracic
pressure is considered an external pressure for all compliances, with
the exception of the systemic arteries, systemic tissues, and extrathoracic
systemic veins. Venous unstressed volume is distributed over the
extrathoracic and intrathoracic veins. Output variables include the
mean arterial blood pressure, which is the average of the pressure in
the aorta’ The other blood pressure waveforms are also associated
with specific compliances in the conceptual model. Cardiac output is
the average of the flow rate in the pulmonary arteries, or can be
computed as the product of heart rate and stroke volume. Table .2 lists
the homogeneous compartments of the uptake and distribution model
and the corresponding compliances of the hemodynamic model.
A compartment volume output of the hemodynamic model is
simply the sum of compliance volumes corresponding to each
* We have argued in Goodwin (2004) and Zijlmans (2009) that i is more correct to con
sider the elements named aorta and systemic arteries 1m Heneken(1%05) & loweorder
empirical approximation
of the whole systemic arterial bed. WIL) a aliple arterial pres
sure waveform output py (0)
Circulation
* Pulmonary tissues
Pulmonary Pulmonary
arteries veins
. Left atrium
Puimonic valve
Mitral valve
Right ventricle Left ventricle
Tricuspid valve
Right atrium
intrathoracic
systemic
Extrathoracic Systemic
systemic arteries
Fieure 8.3 Conceptual model of basic hemodynamics.
Compartment Compliances
Pulmonary tissues None
Arterial pool Pulmonary veins, left atrium, left ventricle. i
"aorta, systemic arteries i
Systemic tissues
Systemic tissues
| Extrathoracic veins, intrathoracic veins, right
| atrium. right ventricle, pulmonary arteries
Venous poo!
Taste 8.2 Homogenous Compariments of the Uptake and Distribution Model
and Compliances in the Hemodynamic Model
compartment. The compartment flow rate outputs of the
hemodynamic model correspond to the inflow rates of each
compartment. For example, the arterial pool blood flow rate is the
flow rate into the pulmonary veins.
Simplifying, assumptions of this conceptual model are that
inertial phenomena are only represented in the aorta (where the
121

## Page 65

122
Applications
acceleration of blood is the highest). Simplifying assumptions made
at an earlier stage, for example, concerning the undivided systemic
and pulmonary blood flow rates, become more visible in the
component diagram.
Mathematical Models
Elaborating on the parameterized elastance curve presented in Eq.
(4.32), the time-varying elastances of the four heart chambers can be
represented as follows:
é sintat/T,,) for O<t<T,. et
a, (t) =
a 0 (otherwise ) 61)
€iq(£) = Evemin + Etomax ~ Etamin) at) (8.2)
Cg E) = Evans + Eparaas ~ Etamin a8) 6.3)
n[ mt —Typ Tao) / Tos] for Tas + Tay <t<Tas + Tro * a
(otherwise )
(8.4)
Cpt) = Exenin + Etomax ~ Etomin 40) (8.5)
Cpe (t) = Evins + Etomas ~ Exomin Molt) (8.6)
where a (f) and a,(f) are the atrial and ventricular activation functions,
respectively. The timing parameters ae ae and T,, represent the
durations of atrial systole, atrioventricular (AV) node conduction,
and ventricular systole, respectively. The ventricular activation
function is delayed by a time T., + T,,, with respect to the atrial
activation function. Each heart chamber has its own elastance
function, with distinct minimum and maximum elastances. The
elastance functions are repeated with heart period HP. The time in
the cardiac cycle needs to be maintained in a state variable. This can
take place inside the elastance generator (Fig. 8.2) or ata higher level
(Gig. 72). In the latter case, the time in the cardiac cycle becomes an
input variable to the generator. The generator has no other state
variables.
2 Goodwin et al. (2004) present a slightly skewed ventricular melivalion Hanetion, which.
somewhat improves the simulate
* Strictly speaking, conduction in the AV node stirty before The enh ar abenin wyatole
temic arterial blood preamire wavelorn
Thin can be compensatedby a amalier value of)
Circulation
Using the mathematical descriptions of the components listed in
Table 4.6, and following the same procedure as for the electrical
analog in Sec. 4.7, we derive a mathematical model corresponding to
the conceptual model of Fig. 8.3. Considering that all volumes in the
compliances are above the unstressed volumes, the transmural
pressures across the compliances are:
Pir) = ey DOC) — UV| 7)
Paolt)= Egg [Ugo (t) — UV ag | (8.8)
Daa (t) = Egg | Vo f) UVa,] 9)
Pop
(t) = Exs[05(t) UVa] (8.10)
PasyE) = Eso [Deso(#) UV| @1D
Piso
(E) = Ejgy [Vigo (E) — UVign| (12)
Prat) = Cm (D)[Vq(t)-UV,, | (8.13)
Prot) = e,n(#)[0,,(t)- UV, | (14)
Pet!) = Epa 29 (FU 8.15)
Ppp) = Epp | pp EUV pe | 6.16)
Pint) = Ca) (t) -UV;,| 617)
Using the unit step function u(x) = 0, for x < 0, u(x) = 1 for x 2 0, to
describe the valves‘ and the differences in resistance to forward and
reverse flow at the atrial inlets, we find the flow rates:
fio) = ue piel) — Pro | Piaf) — Pro O]/ Bore (8.18)
The original Heneken model allows for backflow across the aortic valve, which only
Hen The promure difference inequalto— timm tg, resulting ina small dicrotic
HOLN TH Ce AHTATEG Aveeno Arterial prowmure signal
123

## Page 66

CHAPTER {
A Model of the
Cardiorespiratory
System
107

## Page 67

Applications
fot) =ufpre(E)— Pao | [Pie= Pao O}/ Raw (8.19)
Hal pt) + Pp ~ Rafal) Pol] (6.20)
fer6t) =[ProaC€) — Pr (B)|/ Root (2D
feso(t) =[Pot(#) ~ Peso #)|/ Reven (6.22)
fist) os [Peso(t) = Piset) a P,\/ Ro (8.23)
fra (t)= [Piso E) Pra Ol [Pin — Pre @)]/ Re (8.24)
= Uf Pe (t)— Piso E)|[Pro(l) ~ Piso D|/ 10 X Ryn) —
rot) = [Pig — Pro] Prat) — Pro OV/
Ree (8.25)
fat) = tf Prot) Pow ][Pret Poe ® |/ Rpop 8.26)
fot) =[ Ppa (t) = Ppo(t) |/ Ry 6.27)
fiat) = | Ppt) — Pin)
I] Pye ~ Prat)|/ Ri
= ufpint) — Pot)
J] Pat) — Pp)
|/ (0 xR) (8.28)
Eq. (8.20) results from application of the fluid mechanics
equivalent of Kirchhoff’s voltage law to the loop: reference pressure,
intrathoracic pressure, transmural pressure aortic compliance,
systemic arterial fluid inductor, systemic arterial resistance,
transmural pressure systemic arteries compliance, and back to
reference pressure:
Py Patt) + Lag Hi + Rafal B+ Pel =0 629
The flow rates are based on absolute pressures. To compute
absolute pressures in intrathoracic compliances, average intrathoracic
pressure P, is added to the transmural pressures, If the flow rate is
between two intrathoracic compliances, such ay the left ventricle and
the aorta, P,, cancels out. To avoid confusion between pulmonary
Circulation
veins and pulmonic valve, the resistance of the latter is represented
by Ror also indicating that, in fact, it represents the lumped
resistances of the valve and the pulmonary arteries. The mathematical
model is completed by the volume balances:
oe = fio) fog
(B) (8.30)
a = fill)
~ fall) (831)
dal) _ ¢wf) (6.32)
di
eet = fult)—f eo (t) (8.33)
cet = fey t= fig) (8.34)
ae = fio)
— fal) (8.35)
a = fil) f(b (8.36)
onal = feolD~f pat) (8.37)
ae =f, -fnb (8.38)
rt al ll~ il 6.39)
a = fal)
— fig) (8.40)
Simplifying assumptions included in this mathematical model
involve use of the idealized component descriptions in Table 4.6. The
presented mathematical model only applies to compliance volumes
above the unstressed volumes.
Numerical values of parameters (Table 8.3) are given in the same
Humber of siynifleant digits as presented in Beneken (1965), or in
125

## Page 68

1907
suajeWBled[apostUeUAPOWAaHEgATaVE
+S,{ua8}ywUTeupure‘sjw34UTEUFseoUe}sIsal‘PULUTsauN|Oaposaysun‘jui/S_{WwUrsaueysea‘SpytuUFaunsaidoieroYjesqut’sUrsraqureyojavaySuTUry“UTUTUTayerjrvay:aresymap]
- “an SUIaA Aino tre |
H | - sansh Areuowing
- | - sto |
— coe ‘a | oe “An 00. it) ioe
i 7 ost “an | t8t00 “a
— - gO. ae Sst “AN sonssy o1uiersis |
aa _ OovTt 7,1 rs 2 _ euoV |
i aoeds o19e40Y}2/]U]

## Page 69

128
Applications
three significant digits when computed based on a given parameter,
for example, certain elastance values from given compliances.
The sum of R,,, and R,,,, is equal to the resistance of the systemic
peripheral vessels as given by Beneken. Their ratio reflects the
distribution over arterioles and venules, and is consistent with a
functional capillary pressure of approximately 17 mm Hg (Guyton,
2006). The values of E,, and LIV,, were chosen to be consistent with
that pressure, and with a total volume in tissue capillaries of 250 ml.
The units of parameters listed in Table 8.3 are consistent with the
variables: time in seconds, cardiac elastances in millimeter of mercury
per milliliter, pressures in millimeter of mercury, flow rates in
milliliter per second, and volumes in milliliter.
Considering the input vector from the elastance generator
(Fig, 8.2)
ult) = [ea B) epg CE) erCE) Cyn (t)]” (841)
and the state vector
xi) = [ f(t) Vpy(E) Tyo (E) Ogg (E) Dep (ED Cpge
CE) Vig
(£) Oyq (E) Op E) Opa (E) Opp (ED a],
(8.42)
we observe that Eqs. (8.7) through (8.40) can be put in the form of the
(vector) state equation
EE) = f(x), ud) (8.43)
To achieve this, the pressure equations (8.7) through (8.17) need
to be substituted in the flow rate equations (8.18) through (8.28). Eo.
(8.20) is one of the state equations. By substituting the resulting flow
rate equations (8.18) and (8.19), and (8.21) through (8.28) into the
volume balances (8.30) through (8.40) we find the other eleven state
equations. In general, we will not use such a formulation for software
implementation; it would reduce the model to only twelve equations,
but they would be quite complex. Such a formulation would not be
easy to verify or modify, nor would it necessarily lead to more
efficient code. The interest of this observation lies in its consequences
for the subsequent step in the modeling and simulation process:
Software implementation can be based on the algorithms presented
in Chap. 55 and only the state variables need to be initialized before
the start of a simulation, or saved at the end of a run, to be able to
recover the state of the system at the exact same point. Another
consequence of this observation is that, using Table 4,1, we see that
5 An Buler method with integration
step ive T= O00) 6 hve Rata Rietary remit:
greulation
the state equation is nonlinear and time invariant, Ap «ample of
nonlinearity is the multiplication of the input variable i!) and the
state variable v,,(f) in Eq. (8.7). Therefore, multiplying teimput by a
factor will, in general, not result in multiplication, of thesle by the
same factor. However, a delayed input will result ina qgiyed—but
otherwise unmodified—staie.
To complete the model description we would have tog" aset of
initial values for the state variables. In this partioyjay qs We Can
simply put all state variables to 0, with the exception of yevolume in
the extrathoracic systemic veins v,, (1), which we initialize! the total
blood volume of 4990 ml. In a few simulated cardiac cyelts the blood
volume will distribute across the circulation, anq the sistem will
settle into a steady state. -
We now consider the general input and out ut gtiables as
specified in Table 8.1. The repeat of the elastance functionsi# governed
by the heart period hp(n) = 60/hr(n) in seconds. Beneken ptvides the
following empirical relationships between hp(n) anq the systole
durations used in Eggs. (8.1) through (8.6):
tag (11) = 0.03 + 0.09 hp(2) (8.44)
tyg(2) = 0.16 + 0.20 hp(ni (8.45)
t(n) and t,,(n) are intermediate variables of the elastance generator
(Fig. 8.2), and they do not constitute new, independent inpot Variables.
Myocardial contractility is given as the maximum ‘elastae of the
left ventricle, and we substitute E,,,_,, in Eq. (8.5) by
Ctomax
(1) = mein) (8.46)
The contractility of the other heart chambers js made t© change
proportionally by introducing the intermediate variables
Comey = OME wail Epreae (8.47)
Saray HL) = G(T)
E rasa! Eni (8.48)
C roma (1) = MCN) Erman! Eta (8.49)
To take into account fluid administration, Fall) becomes 2% input
variable to the basic hemodynamic model, and Eg. (8.34) 8 updated
as follows: be
tt as f(t) f ign (ED fin (1) /60.0 (8.50)
128

## Page 70

130
Applications
The factor 60.0 represents the unit conversion from milliliter per
minute to milliliter per second, which is used in the model equations.
To take into account a time varying intrathoracic pressure, the
parameter P,, in Eqs. (8.20) and (8.23) is substituted by the input
variable 0.760 p,(i). The factor 0.760 represents the conversion from
centimeter of water to millimeter of mercury. To take into account the
cardiovascular control effector systemic arteriolar resistance, the
parameter R,,, in Eqs. (8.21) is substituted by the input variable r,,,(n),
with a constant value over the duration of the cardiac cycle. Variable
venous unstressed volume is distributed over the extra- and
intrathoracic compartments via the intermediate variables:
Wen = Tv, (n) (8.51)
nlite 5
Wie i, Pout) (8.52)
used in Egs. (8.11) and (8.12), respectively. This completes the
adaptation of the model to the input variables listed in Table 8.1.
Table 8.4 lists the relationships between basic hemodynamic model
variables and output variables of the overall model. Unit conversions
or averaging over the cardiac cycle may apply, and all output
Overall model output variable Basic hemodynamic model variable
» map(n) | average (Paot)*P,(t))
| plt)*P,(t)
Pyalt)*P,,(t) a —
Pplt)+P,()
average 0.060 Ff,.(t)
py e rt ase
st mannii
Va fC*V CV (OFY, (tv, (0)
v(t)
igh Lh
Vo (LEY, At EY, (OEY, (EY, (0)
Taste 8.4 Overall Model Output Variable
Circulation
pressures are absolute rather than transmural pressures. Owing to
the absence of a compliance in the pulmonary circulation, the inflow
rate of the pulmonary veins and the arterial pool is equal to the
inflow rate of the pulmonary tissues. This makes one of these two
output variables redundant, but both are maintained to increase
readability and facilitate evolution of the model.
For documentation of a mathematical model, we often provide a
summary of input, output, and state variables, equations, and
numerical values of parameters and initial state.
References and Further Reading
Beneken JEW. A mathematical approach to cardiovascular function. The uncontrolled human system [thesis]. The Netherlands: University of Utrecht; 1965
Goodwin JA, van Meurs WL, SA Couto CD, Beneken JEW, Graves SA. A model for
educational simulation of infant cardiovascular physiology. Anest Analg. Dec
2004; 99(6):1655~1664.
Guyton AC, Hall JE. Textbook of medical physiology, lith ed. Philadelphia: W.B.
Saunders; 2006.
Van Meurs WL, Neto P, Azevedo H, SA Couto CD. “Sian Vintage”: A baseline
patient for the Human Patient SimulatorTM with hemodynamic parameters
from the scientific literature [abstract]. Simul Healthcare. Fall 2006; 1(3):183.
Zijlmans M, S4-Couto CD, van Meurs WL, Goodwin JA, Andriessen P. Corrected
and improved model for educational simulation of neonatal cardiovascular
pathophysiology [technical report]. Siu] Healthc. Spring 2009; 4(1):49-53
131

## Page 71

CHAPTER 9
Respiration

## Page 72

mechanics and uptake and distribution models. We introduce a
conceptual model consisting of a muscle pressure generator and
a model for basic lung mechanics. Lung mechanics are represented
via a pneumatic component diagram. We also introduce a conceptual
model for uptake and distribution, based on homogenous
compartments. The latter takes the form of a multiple model with
time-varying fluid volumes and flow rates generated by separate
models driving the uptake and distribution model. Complete
mathematical models for both subsystems are presented and are
shown to have a state variable form.
In this chapter we present models for lung mechanics and uptake
and distribution. In the latter model, gas and blood flow rates and
volumes may be variable. In Sec. 9.2 we therefore expand the theory
presented in Sec. 4.5, introducing the concept of multiple models.
lE this chapter we further specify the requirements of the lung
eprsciinactoat nenpasee
Model Requirements
From Fig. 7.2 and Table 7.2 we obtain the following overall block
diagrams of the lung mechanics and uptake and distribution models
(Fig. 9.1).
Tables 9.1 and 9.2 further specify the input and output variables.
We model control of spontaneous breathing via two effector
variables: respiratory rate and respiratory muscle pressure amplitude.
As for control of circulation, this choice includes the assumption that,
for the intended purpose, control of breathing can modeled without
a more detailed representation of the autonomic nervous system!
Respiratory rate and respiratory muscle pressure have a value once
per respiratory cycle. The outputs are continuous-time variables. In
‘Table 7.2 we noted that the overall output variable, tidal volume, is
implicit in the gas flow rates and volumes.
With the exception of the partial pressure of inspired carbon
dioxide, necessary to simulate re-breathing of CO, all input variables
' Aino note the role af the voluntary nervous system, which has a more direct influence
OH a pOnteneHie Heat Chan on the elreulation:

## Page 73

136 0«=- Applications
7 i Lung
Ventilatory control effectors ——» enone
Gas flow rates and volumes ——pl Uptake
Blood flow rates and volumes ——» and
Inspired carbon dioxide ——> distribution
ane eernieee |
t—— intrathoracic pressure
+—+> Blood gases
Figure 9.2 Overall bock diagrams of the respiratory models.
{ input variable Symbol | Unit | Origin
| Respiratory rate mm) min” Control of breathing
Muscle pressure amplitude | mpa(m) | cm H,0 Control of breathing
Output variable | Symbol | Unit | Destination
| intrathoracic pressure pdt) / em H,0 | Hemodynamics —
Alveolar flow rate F(t) - mi s* i Uptake and distribution
| Alveolar volume - v(t) . i mi Uptake and distribution
Here m represents the respiratory cycle.
Taste 9.1 Input and Output Variables of the Lung Mechanics Model
Systemic tissues blood volume
| Venous pool blood volume
st
Vp(t)
mi
Input variable Symbol | Unit | Origin
Partial pressure of inspired p,COo,(t) | mmHg | Exterior
carbon dioxide .
| alveolar gas flow rate f(t) | mis Lung mechanics
Alveolar gas volume - ; v,(t) ; ; mi i Lung mechanics
Pulmonary tissues blood flow rate Ft) ) mist Hemodynamics
Arterial pool blood flow rate to mis* Hemodynamics
Systemic tissues blood flow rate Flt) mis? Hemodynamics
Venous poo! blood flow rate tfo mist Hemodynamics
Arterial pool blood volume Vip(t) jm Hemodynamics
v_(t) [mi Hemodynamics
Hamodynamies
Taare 9.2 Input and Output Variables of the Uptake and Distibutian Model
Respiration
‘ [ Output variabie Symbol Unit Destination
| Partial pressure of oxygen in p,0,(m) | mmHg Exterior and
arterial blood contro! of
| breathing
Partial pressure of carbon dioxide | p,CO,(m) mm Hg i Exterior and
in arterial blood | control of |
breathing '
Partial pressure of oxygen in _ p,0,(m) / mm Hg Exterior /
venous blood ' | :
Partial pressure of carbon dioxide p,CO,(m) mm Hg ' Exterior |
in venous blood |
Oxygen saturation in arterial bloo $,0,(m) % Exterior |
Here, depending on the variable and the destination, m represents intermittent blood
gas sampling or sampling by the control of breathing model of continuous-time
variables,
4 Tasie 9.2 Input and Output Variables of the Uptake and Distribution Model
(continued)
were presented previously. For the blood gases, “arterial” and
“venous” refer to the systemic circulation. The effects of ambient
temperature and relative humidity of inspired gas will be ignored.
Other respiratory model requirements, already mentioned in Sec. 7.1,
include representation of basic airway, lung, and chest wall mechanics, and pulmonary uptake and distribution of the respiratory gases
oxygen and carbon dioxide.
} 9.2 Multiple Models
In Sec. 4.5 we derived a number of elementary mathematical models
for homogeneous compartments. In these models, gas or blood flow
rates and volumes were assumed constant. For a number of modeling
and simulation purposes, including the one developed here, this may
not be a realistic assumption. Consider, for example, the influence of
the normal respiratory cycle on alveolar gas composition, or critical
incidents such as apnea or significant blood loss. In this chapter we
will therefore lift those restrictions. For example, the amount of gas
with binding in a perfused blood-tissue compartment with
metabolism (Fig, 9.2) now reflects the time-varying blood volume.
AL) Oy (Dep [pC]+ Vic,
[ pO] (9.1)
137

## Page 74

138 Applications
FigurE9.2 Homogeneous compartment with time-varying volume and
flow rates.
The evolution of this volume depends on the fluid inflow and
outflow rates.
FH 5 (8) fu (9.2)
The mass balance of the gas also reflects the variable fluid inflow
and outflow rates.
BA float) foe PO]-V
<S
02
The derivative of the amount now takes into account the timevarying volume.
da(t) ud dv, (t)
dt dt
dsp] ap), deep)! dplt)
a" dp - dt 4)
cp |p)
| +7,
ptt)
Substituting Eq. (9.2) in Eq. 9.4) we find:
(9.5)
ine +v, 4) je
SA = [foil fou ® Jeol]+ f 7) a te
ap ) Lae
_ Equating the right hand sides of Eqs. (9.3) and (9.5), the terms
(f)c,[p(6)] cancel out, and we find:
Fal
dptt) _feinlt){colPat]-co[PO]}-V
(9.6)
dt 0,1) cu) a de,(p)|
p(t) | pC)
This equation is quite similar to Hq, (hat) but now refleets the
time-varying blood volume and flow rate, Moreover Hapecition that
Respiration
the considered flow rate is the inflow rate; outflow affects the
amount, but not the partial pressure. Similar changes apply to the
mathematical descriptions of other elementary homogeneous
compartments. The time-varying fluid volumes and flow rates may
be generated by a separate model, for example, a hemodynamic
model (Fig. 9.3). .
Beneken and Rideout (1968) presented a generic combined
model consisting of coupled hemodynamic and distribution models.
This multiple model has matching hemodynamic compliances
and homogeneous distribution compartments. Figure 9.4 shows a
conceptual multiple model using the symbols introduced in Chap. 4.
For modularity, the mathematical models constituting a multiple
model are often kept separate. Note, for example, the similarity
between Eq. (9.2) and the volume updates, part of the hemodynamic
model described in the previous chapter. If the flow rate is
bidirectional, or can be reversed under specific conditions, then the
mathematical uptake and distribution model has to be adapted to
reflect the changes in supply and evacuation of the transported
substance. For example, the mass balance of the first compartment in
Fig. 9.4 is adapted as follows, using the unit step function, introduced
in Sec. 8.3, as a switch to select the upstream compartment:
aun =fAO{u| AO] [pn O]+u[-AO]e[pO]}
~ ht {u[oO]e, [a ]+u[-fO]e, [p.®]} Q.7)
Uptake and
——» Hemodynamics }+————————_»
distribution
Blood flow rates
and volumes
Ficure 9.3 Block diagram of coupled hemodynamic and uptake anc
distribution models.
anne
aon>
v4(t) fo(t) Volt) fa(t)
Se EE
Foun ®4 Haale conceptual multiple model
138

## Page 75

140
Applications
As for the derivation of Eq. (9.6), only the terms reflecting the
upstream compartments are maintained in the partial pressure
equation.
There are several variations on the basic multiple model. In the
next section, we will see an example of perfusion with a variable flow
rate, but at a fixed volume. In that case, the compliance can be
eliminated. The variations in uptake and distribution variables
caused by cardiac or respiratory cycle fluctuations in carrier volumes
and flow rates may be very small, or not of interest, in a particular
modeling and simulation project. In such cases, the flow rates and
volumes can be averaged before their use in uptake and distribution
computations, resulting in a larger integration step size and more
efficient code for these equations. Concentrations or partial pressures
in sites corresponding to fluid dynamic compliances may be very
similar, or their differences may not be of interest. For example, the
partial pressure of oxygen in the left ventricle only has a minute
delay with respect to the partial pressure in the left atrium. The
volumes of these two compliances can be lumped into a single
homogeneous compartment (Fig. 9.5).
The compartment volume is equal to the sum of compliance
volumes and the compartment inflow rate corresponds to the inflow
rate of the first compliance. This leads to a simplification of the uptake
and distribution model and more efficient code. In Sec. 8.1 we
observed that if flow rates and blood volumes in specific organs or
tissue groups can be considered a fixed fraction of total flow rate and
volume, then they can be computed as such. In a multiple model this
results in a single hemodynamic element (resistance or compliance)
corresponding to several distribution compartments. If parallel
organs or tissue groups have different hemodynamic characteristics,
or if incorporation of local control mechanisms depending on
compartment partial pressures is required, such a scheme cannot be
used, and parallel hemodynamic and distribution elements are
required, for example (Fig. 9.6).
4 4
1 3 i
H A Se 1
i : : \
1 Pe ey 1
Fx(t) Volt) fa(t)
— >
im ( Jeb
Fiaure 9.5 Multiple model with lumped companinent
Respiration
Figure 9.6 Multiple model with parallel tissue groups and autoregulation in
one.
; An example of such autoregulation would be the coronary
circulation where, according to one hypothesis, a decrease in oxygen
concentration leads to the release of a vasodilator substance affecting
the arterioles (Guyton, 2006; also see Fig. 9.6). This also constitutes an
example of feedback from the distribution model to the carrier model.
A multiple model may involve several carriers (the fluids, gas or
blood), even for a single compartment, for example, the elementary
ventilated and perfused compartment in Table 4.8. It may also involve
several substances (a particular gas, drug, hormone, heat) using the
same underlying carrier model(s) (Fig. 9.7). °
9.3
Conceptual Models
Mecklenburgh et al. (1992) proposed a lung model with direct tepresentation of respiratory muscle activity. Similar to hemodynamics
(Sec. 8.2) the electromechanical processes that are responsible for
the generation of the time-varying respiratory muscle pressure
Puust) can be separated from the pneumatic aspects of lung
mechanics (Fig. 9.8). i.
In the next section we will present an empirical muscle pressure
generator that uses the input variables respiratory rate and muscle
pressure amplitude, available once per respiratory cycle, to
parameterize the continuous-time respiratory muscle pressure
wavelorm presented by Mecklenburgh et al. (1992). Their model for
basic lung, mechanics consists of a resistance in series with a
compliance, The
re
anee K reflects resistance to flow in the airways,
an Well ae energy losses in moving lung ane chest wall tissues. As
1

## Page 76

142
Applications
Lung Gas flow rates and volumes
— Uptake and
mechanics p
distribution —
substance nh
Uptake and
distribution —>
substance 2
Uptake and
distribution == -——>
—»>| Hemodynamics - substance 1
Blood flow rates and volumes
Fieure 9.7 Block diagram of a multiple model with two carriers and n
substances.
% ————> v(t}
remy >| Muscle pressure Pwus(t) Basic lung be
mechanics ts
‘apatral generator y(t)
Figure 9.8 Block diagram of the lung mechanics model.
simulating the intrathoracic pressure is part of the requirements, we
expand this model by dividing the compliance into lung compliance
C, and chest wall compliance C,,,. Figure 9.9 shows the corresponding
component diagram, already in the form of a multiple model
including gas mixing in the airways.
During spontaneous inspiration, respiratory muscle pressure
contributes to the transmural pressure of the chest wall compliance,
resulting in a negative intrapieural pressure, which we will consider
to be equal to the intrathoracic pressure. This negative pressure
contributes to the transmural pressure of the lung compliance,
resulting in a negative alveolar pressure and gas flow across the
airway resistance. On expiration, the muscle pressure is removec|
and the volume accumulated in the compliances creates a positive
alveolar pressure and passive exhalation.
The pulmonary uptake and distribution model consists of two
homogeneous compartments coupled to this model: alveolar space,
where gas exchange e(f) takes place, and dead space, without gas
exchange. Ventilation is bidirectional; the arrow above the resistance
defines positive flow rate. The dead space is consicered to have a
fixed volume V,,, hence the absence of a corresponeling compliance:
in the lung mechanics model, The alveolar apace hae a Hineevary in,
Respiration
Cow
Figure 9.9 Multiple model of lung ventilation and gas uptake.
volume corresponding to the volume of the compliance. Gas exchange
is considered variable, depending on pulmonary perfusion, venous
blood gas content, and alveolar partial pressure. The partial pressures
in blood leaving the alveolar capillaries are modified by admixture
of blood coming directly from the pulmonary arteries (Fig. 9.10).
Normally this admixture is a small fraction of total flow rate, in
the order of 2 percent, but in certain critical incidents or pathologies
it can increase significantly. The shunt flow rate and the flow rate
through the compartment are equal to SF fil) and (1 — SF) FO:
respectively.
The concept of lumping hemodynamic compliances into a single
distribution compartment is presented in Fig. 9.5. For modeling
distribution of respiratory gases, hemodynamic compliances can be
lumped as listed in Table 8.2. Figure 9.11 shows these compartments
in association with the compliances of the hemodynamic model
(Fig. 8.3) and of the model of lung ventilation (Fig. 9.9).
Figure 9.12 shows the resulting uptake and distribution model,
using the homogeneous compartments introduced in Sec. 4.5 and
adding the pulmonary shunt of Fig. 9.10.
A simplifying assumption included in this model is that the
amount of gas dissolved in pulmonary blood and lung tissue can be
ignored with respect to the amount of gas in the alveolar gas mixture;
the homogenous compartment has no tissues, and the separation
between gas and blood included in the model in Table 4.8 is removed.
For the same reason, there is no compliance corresponding to a timevarying pulmonary blood volume (Figs. 9.10 and 9.11). The main
simplifying assumption included in the lung ventilation and gas
uptake model (Fig. 9.9) is that such a simple model can indeed
represent the essential aspects of spontaneous breathing and gas
mixing in the airways. The absence of representation of separate left
ancl right lungs is consistent with the requirements, which do not
include simulation of unilateral incidents, such as pneumothorax.
143

## Page 77

44 = Applications
(4-SF)fpy(t)
‘ ’
os
Pulmonary veins
Ces
Pulmonary arteries ><
Fieure 9.10 Multiple model of lung perfusion including a simple shunt with
shunt fraction SF, O<SF <i.
Ficure 9.12 Multiple model of ventilation, circulation, and uptake and
distribution of respiratory gases.
The effect of gas warming and humidification during inspiration on
alveolar volume is ignored, but could be incorporated using the
concepts presented in Sec. 4.5. Simulation of mechanical uel edi
is not part of the requirements, bul would rebut in an adeitiona
input to the basic lung mechanics model iy Hig WA
Respiration 145
Dead space
Alveolar space
Venous pool Arterial pool
Systemic tissues
Figure 9.12 Uptake and distribution model.
9.4 Mathematical Models
The muscle pressure curve presented by Meckienburgh et al. (1992)
can be parameterized empirically asa piece-wise continuous function
consisting of a ramp and a decaying exponential with amplitude
mpa(m), Eq. (9.8).
on SHOP at isn censor mannan
t
i Oxbet
mipa(m) ae <t)(m)
i tt, (mn)
paus) = “EO ey (9.8)
mpa(m) : _ ty(m) St <t)(m) +tp(m)
j-e4
The inspiratory and expiratory times are defined with respect to
the muscle pressure waveform, rather than with respect to flow rate.
They are considered fixed fractions of the respiratory period in
seconds: 60/rr(@m), Eqs. (9.9) and (9.10).
1 60
t)(m) = ~
srr(n)
(99)

## Page 78

Applications
te(m) == 9.10)
. 3 rr(m) (9.10)
Tt can be verified that this waveform is continuous in the knots
t=0,t=8, andt=t,+t,= RP, wheret is the time in the respiratory
cycle and RP the respiratory period. The muscle pressure waveform
is repeated with RP. The basic lung mechanics model takes this
waveform as an input (Fig. 9.8). Following the same procedure as for
the hemodynamic model Gec. 8.3), we derive a mathematical model
corresponding to the conceptual model of Fig. 9.9. Considering the
state variable v,(f) and the functional residual capacity (FRC), the
transmural pressure of the lung compliance is:
CG
pt) =—Prre + 1)
This represents a minor adaptation of the mathematical
description of the compliance listed in Table 4.6. The nonlinearities of
this relationship are not considered here. The parameter P,,. indicates
the intrathoracic or intrapleural pressure at the end of a passive
expiration with 0,() = ERC. At that point, the alveolar pressure is
equal to atmospheric pressure, which we will take as our reference
pressure, and the lungs are kept open by a positive transmural
pressure, due to a slightly negative pressure in the intrapleural space.
Assuming that the intrapleural volume canbe ignored, the transmura!
pressure of the chest wall compliance is:
Cow
Pins (9.12)
Pew
At the end of a passive expiration the chest wall has a slightly
negative transmural pressure, and is pulled inward due to the
pressure in the intrapleural space. Compressibility of respiratory
gases is included in these compliances. The pressure in the alveolar
space is the sum of the muscle pressure and the two transmural
pressures [respecting the sign Of Prag:
palt)= py 6+ Pow — Pas (9.13)
Flow rate through the linear resistance is equal to:
(9.14)
pat) - apt) — pew)+ Pmus!)
f,@Q=-
& R k
A form
of Kirehhott’s voltage law
—e
Respiration
Substituting the transmural pressures
fl) = BAD ERC_wal#)—FRC , prs
RC, Rss R (9.15)
and reordering terms, the flow r j i
i , ‘ate can be written in
state and input variables: terms of the
Cr+,
()=-— =" To) - :
fa CiCowR [ea FRC]+ 5 Panustt) 9.16)
Note that this equation includ
> es the formula for in seri
compliances, Table 4.14. The volume balance is simply: _
doa) ;
-~ =f, (0.17)
Per the requirements, this equation does not contain compenae for differences between ambient and body temperature, or
‘or differences in humidity between inspired and expired gases
Substituting the flow rate we find: ,
do(t)_ — C, + Cow
y — ie
dt CiCouR PAP FRC} + Pinus (2.18)
The state variable v,(f) is one of ti i
. at (f) 3 he output variables. The flow
rate f,()), given by Eq. (9.16), is another. The output variable p,,(t) is the
it Bs
sum of the muscle pressure ¢
_ p and the transmural pressure of the chest
Pi) = Pow) — Paus(t)
(9.19)
Substituting the transmural pressure, we find:
va(t)~ FRC
py) = Pepe +A— past)
a Pmus (9.20)
Considering the input u(/) =
z = Pyys(t), the state x(f) = v,(f) - FRC, and
the output vector y(t) = [v,(4) - FRC f,0) p,@) - Pil, we observe that:
dxf) _ dv,
(t)
dl dt (9-21)
147

## Page 79

Applications
and Eq. (9.18) is a state equation of the form
= = ax(x)+ bu(t) (9.22)
with scalar constants a and b that can be read from the equation. The
transmission of the state variable to the output, and Eqs. (9.16) and
(9.20) can be written as
4 Po)
va(t)— FRC
gt) (=| -2ASW |To,-FRC]+] = Ips 9.28)
s : CCR R
pelt) — Pore ) 1 es
Cow
which is an output equation of the form
y(t) = ox(x) + dult) (9.24)
with vector constants c and d that can be read from the equation.
Numerical values of model parameters are given in Table 9.3, in a
consistent set of units.
| Name Symbol Value ‘Unit
| Respiratory muscle pressure MPA | 45 i cm H,0
i amplitude a '
; — | i
| Respiratory period RP \ a 7 s -
i 3 Eat
Airways and lung tissue R b Bi IO em H,0 mis
| resistance _ _—--
l Functional residual capacity FRC 2300 _ mi
| Lung compliance | 200 i mifom H,0
| if
\ End-expiratory pressure in -4 com H,0
the intrapleural space | _ xs
| Chest wall compliance Cow i aes mi/em H.O
Taste 9.3 Lung Mechanics Model Parameters
Respiration
Mecklenburgh et al. (1992) present numerical values of model
parameters for only three individual subjects. Guyton and Hall
(2006) give numerical values for most parameters, reflecting a
normal adult male. The value of Coy is derived from a total lung
and chest wall compliance of 110 ml/cm H,O and the value of ae
The timing and amplitude of the muscle pressure waveform are
governed by the input variables mpa(n) and rr(n). Table 9.3 lists
corresponding baseline values for the muscle pressure amplitude
MPA and the respiratory period RP. For the given set of parameters
the value of MPA results in a steady-state volume increase of 500
ml, which is the typical value for tidal volume given by Guyton
and Hall. The value of RP corresponds to a typical respiratory rate
of 12 minTM. Guyton and Hall provide two values for Pye, Ppp,= —4
cm H,O is retained here. This value and a negative deflection of
approximately 2 cm H,O, caused by MPA divided over the two in
series compliances, areconsistent with the hemodynamic parameter
P,, = -4mm Hg ~ -5 cm HO, which indicates the average value of
the intrathoracic pressure. Patterson et al. (1968) give a value for
the resistance R reflecting airways and lung tissues. Resistive
losses in the chest wall are therefore ignored. This value is an
average value for patients undergoing open heart surgery, with
access to the intrapleural space, but not for a typical healthy adult
male. A few parameters are included as numerical values in
equations (9.8) through (9.10). For some applications, it could be
useful to represent those via symbols and list them in a table,
similar to Table 9.3. The end-expiratory situation is a convenient
initial state: v,(0) = FRC.
The conceptual model of uptake and distribution is given in
Fig. 9.12. The mathematical model is derived based on the descriptions
of the homogeneous compartments in Table 4.8, and their timevarying equivalents, derived in Sec. 9.2. Considering the bidirectional
flow rate/,(f) (Fig. 9.9), we observe that u[f,()]= 1 on inspiration and
ulf,(}= 0 on expiration. Conversely, u[--f,(Q] = 0 on inspiration and
ul-7,(0 = 1 on expiration. This is used to switch upstream
compartments, as in Eq. (9.7). The description of the ventilated
compartment in Table 4.8 can be adapted for the dead space, with a
fixed vorume but a variable flow rate.
apy
(t) _ 4 f,O)faOpin®)—ul-fxO]fy Op.) -|f, Opp) ier
ai Vp Beas
This, and all subsequent, equations have specific instantiations
for the respiratory gases oxygen O, and carbon dioxide CO,. For
oxygen, when breathing room air, the partial pressure of inspired
M4

## Page 80

150 «= Applications
gas is constant: p,,(f) = P,O,, for carbon dioxide p,,(f) = p,CO,(#). The
amount of gas in the alveolar space is equal to:
ag) =,(0) a (0.26)
Tr
where P, represents the total pressure, ignoring the respiratory cycle
variations in this quantity. The derivative of the amount is:
dat) _ {vs @ baat _ dog pa , va dpa
dt dt 7 dt PP, Pr dt
pat) , ta® dpa
= f,p4—+4 4 (9.27)
Ae’ Pp Re dt
The mass balance reflects ventilatory supply and evacuation of
gas, from and to the dead space, and perfusion coming from the
venous poo! with a flow rate (1 - SFI (also see Fig. 9.10).
da ,(t)
dt
= fx} ul fos uf- p02}
Pr Py
# -SFrtDfoa[ rg }-aalrntO)} (9.28)
An assumption included in the last term of this equation is that
there is perfect equilibration of partial pressures between the alveolar
space and pulmonary venous blooc The relationships between
partial pressure and blood gas content for oxygen and carbon dioxide
will be discussed as part of the model parameters. Using:
{b= {uf f,O]+ul-fO]} LO 9.29:
in Eq. (9.27) and combining Eqs. (9.27) and (9.28), the expiratory terms
cancel out, and we find:
dp alt) _ j.dul f,O]{pp®-p,W}+ Ppa SP if 0 o4[ Py, “ep [p 4o]}
dt vat)
(9.30)
The confluent, Table 4.10, in the pulmonary veins combines the
mass flow rates from the alveolar space and the venous pool.
= SE) fy Dey [P| SE
(De 1} Pont |
/,(
(9.31)
Respiration
The dynamic equations for the partial pressures in the arterial
i the systemic tissues, and the venous pool result from adaptations
of Eq. (9.6) . -
dp_p(t) fn) Pat]
= (9.32)
nytt
Pap (t)
apatt) 1 {eo[ Pa ]-caleatt}1
dt me (9.33)
xt pve) |
pa(t) ap iw]
dpypit) feo) {e [palt)}-co[ Poptt y}
dt de,(p)) os
Vp (|
ap Spy lt)
Only the systemic tissues compartment contains tissue volume and
has metabolism. For oxygen, metabolism is positive, indicating
consumption, for carbon dioxide it is negative, indicating production.
Considering the input vector
ult) =| pCO fall) On) fon fap fu) fap CE) Byp lf) 2a (8) Pan ]” (0,38)
and the state vector
1) =[PoCO2( p4CO2( PyCO 218) PCO) PyCO2] 0.36)
ae (9.25), (9.30) through (9.34) constitute a state equation of the
orm
CE) = fx), ub) (9.37)
For oxygen, the input p,CO,(4) is replaced by the parameter P,O,.
The partial pressure output variables correspond to state variables.
For carbon dioxide:
ened
(° 010
pCO)
0
00 0 0 ano (286)
51

## Page 81

152
Applications
which is an output equation of the form
y(t) = Ax(t) (9.39)
The output variable oxygen saturation in arterial blood s,O,(é) is
a nonlinear function, presented below, of the state variable partial
pressure of oxygen in arterial blood. Discrete-time versions of these
output variables (Table 9.2) are obtained via sampling of the
continuous-time equivalents. Table 94 lists the uptake and
distributions parameters that appear in the state equations.
The first two parameters indicate conditions of the environment,
the latter four are patient specific. Volume of perfused tissues is
estimated for a 70 kg subject. Oxygen consumption and carbon
dioxide production are considered at BTPS, and are related via a
respiratory quotient RQ = 0.8. Values for these parameters can be
found in Guyton and Hall (2006), or other physiology textbooks.
Additional parameters are included in the functions that relate
content to partial pressure. The content of oxygen in blood as a
function of its partial pressure c,O,[pO,] is computed as follows.
Severinghaus (1979) gives an accurate approximation of the
relationship between pO, in mm Hg and the dimensionless fraction
of hemoglobin saturated with oxygen S.
\-1
5 =( 23400 (pO? +150p0,) +1 (9.40)
Oxygen content results from a combination of oxygen bound to
hemoglobin and dissolved oxygen. The content in milliliter of oxygen
Name Value | Unit
Atmospheric pressure _ 760 mm Hg
Partial pressure of oxygen if "160 | mm Hg
inspired air i
[Shuntfraction 0.02
_ Volume of perfused tissues 60000 | mi
Oxygen metabolism _ one | 250 ml min+
| VO,
Carbon dioxide production / 2 200 ) mi min
VCO,
Lcxiintinaismteaesytantae lle lia parr
Taste 9.4 Uptake and Distribution Model Parameters
Respiration
oe per milliliter of blood (see Sec. 4.5) is given by Severinghaus
1979): :
[O,], = 0.0134 Hb $+ 0.000031 pO, (9.41)
where Hb is the hemoglobin concentration in grams per deciliter.
Typical hemoglobin concentrations for males and females are 16 and
14 g/dl, respectively (Guyton, 2006). As we have seen in Sec. 4.5, to
obtain content in milliliter of oxygen at BTPS per milliliter of blood,
this result needs to be multiplied by a factor 1.21.
c4O2 = 1.21[ 05], (9.42)
The amount of gas in the alveolar space, Eq. (9.26), is at BIPS
conditions. The alveolar mass balance Eq. (9.28) and resulting state
equation (9.30) also assume use of BIPS content units. The output
variable oxygen saturation in arterial blood s O.(n) in percentage can
be derived from the continuous-time partial pressure of oxygen in
arterial blood, and Eq. (9.40).
r . 7 =
5,0,(#) = 100 ( 23400 (p,0,(8) +150p,0,(0) + 1] (0.43)
In the tissues, outside of the circulation, there is no hemoglobin,
and considering Eq. (9.33), the amount of dissolved oxygen can be
ignorec.
0, =0 (9.44)
Carbon dioxide is transported by the blood in many forms: the
dissolved state (7%), as bicarbonate ions HCO,- (70%), and bound to
hemoglobin (23%). Kelman (1967) gives a procedure to compute the
content of carbon dioxide in blood as a function of its partial pressure
c,CO,{[pCO,]. For our application, this procedure can be approximated
by a linear relation ship, which gives the content in milliliter of carbon
dioxide at STP per milliliter of blood.
(CO,
], = 0.0066 pCO. +0.23 (9.45)
Content in milliliter of carbon dioxide at BTPS per milliliter of
biood is given by:
cyCO2 = 1.21[CO, |, (9.46)
153

## Page 82

164
Applications
The tissues do not contain hemoglobin, but carbon dioxide is
present in the other forms. At the same partial pressure:
¢CO, =0.77 ¢CO, (9.47)
The derivatives of the partial pressure-content relationships can
be computed analytically, or empirically using small changes in
partial pressure, for example, 1 mm Hg. Dependency of these
relationships on other blood gases (Bohr and Haldane effects) is not
considered here, but more information can be found in the references
and further reading. A more complete analysis of pulmonary gas
uptake could also take into account water vapor and nitrogen (N,). In
that case, the sum of partial pressures has to add up to the total
pressure in the lung mechanics model, and net uptake has to be taken
into account by that model.
References and Further Reading
Barton SA, Black AM, Hahn CE.: Dynamic models and solutions for evaluating
ventilation, perfusion, and mass transfer in the lung - Part I: The models. IEEE
Trans Biomed Eng. Jun 1988, 35(6):450-7.
Beneken JE, Rideout VC. The use of multiple models in cardiovascular system
studies: transport and perturbation methods. IEEE Trans Biomed Eng. Oct 1968;
15(4):281-9.
Chiari L, Avanzolini G, Ursino M. A comprehensive simulator of the human respiratory system: validation with experimental and simulated data. Ann Biomed
Eng. Nov-Dec 1997; 25(6):985-98.
Fincham WE, Tehrani FT. A mathematical model of the human respiratory system.
J Biomed Eng. Apr 1983, 5(2):125-33.
Grodins FS, Buell J, Bart AJ. Mathematical analysis and digital simulation of the
respiratory control system. } Appl Physiol. Feb 1967; 22(2):260-70.
Guyton AC, Hall JE. Textbook of medical physiology, 1th ed. Philadelphia: W.B.
Saunders; 2006.
Kellman GR. Digital computer subroutine for the conversion of PCO2 into blood
CO2 content. Respiration Physiol. 1967; 3:111-15.
Mapieson WW. An electric analogue for uptake and exchange of inert gases and
other agents. Appl Physiol. Jan 1963; 18:197-204.
Mecklenburgh JS, Al-Obaidi TAA, Mapleson WW. A model jung with direct representation of respiratory muscle activity. Br. J. Anaesth. 1992; 68:603-12.
Patterson RW, Sullivan SB. interrelation between Paco2 and PAco2 in the control of the mechanics of breathing in man. Bull N Y Acad Med. Oct 1968;
44(10):1265-72.
Riley RL, Cournand A. ‘Ideal’ alveolar air and the analysis of ventilation-perfusion
relationships in the lungs. J App! Pirysiol. Jul 1949; 1(12):825-47,
Severinghaus JW. Simple, accurate equations for human blood O2 dissociation
computations. ]. Appl. Physiol. 1979; 46(3):599-602.
CHAPTER 10
Physiologic Control
lao

## Page 83

econsider that an operating pointin physiological feedback
results from the equilibrium between a system and its
control. The models for control of circulation and
spontaneous breathing, presented in this chapter, are based on
linearization of the relationship between the controlled variable (e.g.,
mean arterial pressure) and the control effector (e.g., heart rate) in the
operating point. The static models consist of piecewise linear receptor
functions, control gains, and saturations on the control effectors.
Complete mathematical models for both control systems are
presented.
One of the benefits of feedback control is that it allows for
maintaining variables within narrow ranges, despite changes in
system characteristics or environmental conditions. Thus, feedback
is at the center of many homeostatic mechanisms, including control
of blood pressure and control of blood gases. We consider that an
operating point in physiological feedback results from the equilibrium
between a system and its control. This situation is unlike manmade
control systems with an explicit setpoint for the controlled variable
(see for example van de Vegte, 1994). Figure 10.1 gives an example in
cardiovascular control.
A rise in heart rate causes a rise in blood pressure in the
uncontrolled cardiovascular system. In the baroreflex control system,
a drop in blood pressure causes a rise in heart rate. Coupling the two
systems results in the operating point as indicated in Fig. 10.1. Heart
rate acts as a control effector. We will call the value of a control
effector in the operating point a reference (REF). Mean arterial blood
pressure is the controlled variable. We will also call the value in the
operating point a setpoint (SP), despite the fact that it results from the
equilibrium between the two systems. A perturbation, for example,
acute blood loss, will cause the characteristics of the uncontrolled
system to change, as illustrated in Fig. 10.1. Without feedback, heart
rate would remain equal to the REF value, and a significant blood
pressure drop would result! With feedback, a new equilibrium
' A precine analysis would have to take into account the sympathovagal balance
in Lhe operaling point
157

## Page 84

158 Applications
Perturbation ———>/_ Uncontrolled Heart rate (ce)
system a Perturbed
| . system
Control Controlled Sen
effector (ce) variable (cv) REF j->~ . -.. Operating
; i point
‘ Control
Control
SP Mean arterial
pressure (cv)
Figure 10.1 Simplified block diagram of a physiologic control system and
steady-state relationships in baroreflex control.
between the perturbed system and its control is established, resulting
in a much smaller decrease in blood pressure. A more intuitive way
of looking at this feedback is that, in the coupled systems, a drop in
blood pressure results in a rise in heart rate, partially counteracting
the original blood pressure drop. In the subsequent sections we will
introduce simple empirical models of control of circulation anc
control of spontaneous breathing.
10.1 Model Requirements
From Fig. 7.2 we obtain the overall block diagrams of the control
models as shown in Fig. 10.2.
Table 10.1 defines the input and output variables of the control of
circulation model, explicitly listing the control effectors, including
the overall output heart rate (Table 7.2). These variables are a subset
of the variables of the uncontrolled model, listed in Table 8.1,
switching input and output variables.
These are essentially the same input and output variables as for
the model presented by Wesseling and Settels (1985). A minor
difference is that the directly measurable control effector total
peripheral resistance (TPR) is replaced by systemic arteriolar
resistance 1,4, which is the physiological variable in the Beneken
model (Chap. 8), causing a TPR change. A simplifying assumption
included in this input-output configuration is that control of
circulation only depends on systemic mean arterial blood pressure.
Table 10.2 defines the input and output variables of the control of
breathing model, explicitly listing the control effectors, including the
overall output respiratory rate (Table 7.2). The input variables are a
subset of the output variables of the uptake and distribution model
(Table 9.2). The output variables are the input variables of the lung,
mechanics model (Table 9.1).
Simplifying assumptions included in this input-output
configuration are that the control of spontaneour breathing, only
Physiologic Control! 159
. Controt
Systemic arterial blood gases ——p| of
breathing
t-—> Ventilatory controt effectors
aa
tic
Control
Systemic blood pressures ——>| of + Cardiovascular contro! effectors
circulation
Figure 10.2 Block diagrams of physiologic control systems.
Input variable | Symbol | Unit | Origin |
Mean arterial blood pressure map(n) mm Hg
Output variable Symbol Unit |_ Destination |
Hemodynamics
| Heart rate © Arn)
Myocardiai contractility me(n)
Hemodynamics
| _ Hemodynamics
Systemic arteri i ' in) i
y: c arteriolar resistance Peart) Hemodynamics
Venous unstressed volume
__ Hemodynamics
Here n represents the cardiac cycle.
Taste 10.4 input and Output Variables of the Control of Circulation Model
Fi T
Input variable | Symbol Unit | Origin
Partial pressure of oxygen = p,0,(m) | mmHg | Uptake and distribution
in arterial blood i
Partial pressure of carbon
| dioxide in arterial blood
p,CO,(m) mmHg | Uptake and distribution
Output variable Symbol Unit Destination |
Respiratory rate rim) — min | Lung mechanics
Muscle pressure amplitude | mpa(m)
Here m indicates the respiratory cycle
Tan 10.2
Inpul and Output Variables oi the Control of Breathing Model

## Page 85

160 Applications
depends on the partial pressures of oxygen and carbon dioxide in
arterial blood, ignoring the effect of these blood gases in other
locations, and the effect of other blood components, such as pH, and
the lung stretch receptors (Guyton, 2006).
10.2 Conceptual Models
The basic principle underlying the models presented in this chapter
is linearization of the empirical relationship between the controlled
variable and the control effector in the operating point (Fig. 10.1).
This results in a “gain with offset” model (Table 4.11). A piecewise
linear function (PLE) (also see Table 4.11) and limits are included to
expand the range of validity of the model. The PLF represents
receptor activation and saturation as a function of the controlled
variable. Overall physiological limits are imposed on the control
effector. Figure 10.3 gives an example of these relationships in
baroreflex control of heart rate.
In this model, both saturations of the hr(map) curve [Fig. 10.3]
result from the saturation of the receptor [Fig. 10.3(a)], not from the
limits on the control effector. The baroreceptor activation function is
common to all four cardiovascular control effectors, but the gains
and control effector saturations are distinct.
Control of breathing is based on two receptor activation
functions, one for each of the controlled variables p,O,, and p,CO,,.
Oxygen has a stimulating effect on spontaneous breathing for p,O, <
100 mm Hg, but no effect for higher values. High carbon dioxide,
p,CO, > 40 mm. Hg, has a stimulating effect; low carbon dioxide has
a depressing effect. The parameters governing these effects will be
presented in the next section. We assume that the main effects of the
controlled variables on spontaneous breathing are on minute
ventilation, the product of tidal volume and respiratory rate, leaving
the ratio between the two intact. These effects are governed by two
gains and are considered additional. Physiological limits are applied
to tidal volume and respiratory rate. For a particular set of lung
mechanics parameters, and in the approximation of the lung
mechanics model presented in the previous chapter, tidal volume is
linearly related to the output variable muscle pressure amplitude.
Simplifying assumptions included in these conceptual models
are that for the intended purpose, the relationships between
controlled variables and control effectors can indeed be represented
by static, piecewise linear relationships. The additive nature of the
effect of pO, and p,CO, on minute ventilation is another simplifying,
assumption. More elaborate conceptual and mathematical models
of control of circulation, control of respiration, and their interaction
can be found in, for example, the work by Ursino (1998), and Khoo
(1999).
Physiologic Control 161
a(map) in mm Hg
MAP, = 92 mm Hg .”
(a)
as
2g erste
| ! ~1.4 bpm/mm Hg = Ghrymap
{b) Sasa tee > map inmm
Hg
50 100!
$28 procon ec ee nsec ee ec eee ——
| hr(map) in bpm
fi
200 f 200 = HRinay.
|
:
i
150
i
t
|
(ce) ; 724+28
4 72 bpm = HRyer
t a 72-28
! a 40 = HRimin
| tot '
| a
aracme Se ee ee ee
50 100 mapinmm Hg
Figure 10.3 Relationships in baroreflex control of heart rate. (a) Baroreceptor
activation function a(map). (b) Baroreflex-mediated heart rate change Ahr(map)
= Gmap * a(Map). (c) MAP-dependent heart rate hr(map) = HRrer + Ahr(map)
and saturations. Numerical values as in Tables 10.3, 10.4, and 10.5.

## Page 86

162 Applications Physiologic Control! 63
Name | Symbol | Value | Unit Table 8.3 |
L -
10.3 Mathematical Models oni Heart rate reference ABs 1% min | 60/HP
For notational compactness, we drop the (discrete) time notation in see . rei i : : ss
the static relationships between controlled variables and control Myocardial contractility MC, ., 4 :
effectors. The distinction between variables and parameters is reference . 4 |
maintained
via lower and upper case symbols. The receptor activation Systemic arteriolar SAR, O28 |
function of control of circulation [Fig. 10.3(a)] can be described as resistance reference |
follows: Venous unstressed UV, ., 2190 | mi | UY, FUV,, |
volume reference |
BRypin — MAP 5p if maps BRyrin Mean arterial pressure = MAP, = 92, mm Hg
ap (map) = 4 BRax — MAP.» if map 2 BRyar (10.1) |_ setpoint ae aS -
map — MAP,,, otherwise
Taste 10.3 Operating Point of the Unperturbed Hemodynamic Model in Open-Loop
with the mean arterial pressure setpoint MAP., the threshold below
which decrease in map has no further efiect on the baroreceptor BR,,,,,
and the saturation point of baroreceptor activation BR,,,,. This
function is multiplied by the gain from map to heart rate G9, also
effectors. Physiologically speaking, the autonomic nervous system
may be active, even in the operating point. The table also lists
see Fig, 10.3(b). a parameters and numerical values included in
Gains from map to the control effectors of the Wesseling and
Altt = Gig / map%may MAP) (10.2) Settels model, as penned by Ten Voorde (1992), and a in
Goodwin et al. (2004), are listed in Table 10.4.
Addition of the heart rate reference HR,,, and control effector As all the change in total peripheral resistance are assumed to be
saturation [Fig. 10.3(0)] is accomplished as follows: concentrated in the systemic arterioles, the gain G.,,,,,, is equal to the
Bain Crop mag’ With the — as defined by Eqs. (10.1) through (10.3),
if the control loop is closed on an unperturbed system, the controlled
AR nin if Rye + Mtr s AR in variable ate ea in its area, and the control effectors
Shr (FIR oe + Ahir j= AR nox if HRyp+ Al 2 AR yx (10.3) should keep their reference values.’ Parameters of the receptor
| HRyep + Ar otherwise activation function and control effector saturations are listed in
"3 Table 10.5.
The baroreceptor thresholds are set so that, in combination with
Other control effectors are computed in a similar way, based on the gain G,,,,,,,. they result ina reasonable baroreflex mediated change
the same receptor activation function a,,,,(map), but with different in heart rate. The range of mean arterial pressures with an infiuence
references MC,,, SAR,,, and VUV,,,; gains Copa —iinasl i on the firing frequency of nerves coming from the baroreceptors is
and control effector saturation functions §,,); S4,(), and Sq) The larger, but nonlinear (Guyton, 2006). The limits imposed on the
parameters of these saturation functions are MC... MC yeu SAR pin control effectors are empirically set general physiological limits for a
SAR yee VUViy and VUV,,,. respectively. This relatively simple healthy adult male, not only reflecting the influence of the
empirical model has many parameters, which can be grouped as baroreflex.
follows. Table 10.3 lists the parameters of the operating point. The Control of breathing is modeled analogously, via oxygen and
first four are in fact parameters of the hemodynamic model, anc carbon dioxide receptor activation functions causing changes in
MAP. is the value of the hemodynamic output map(n) for ar (exhaled) minute ventilation via dedicated gains.
unperturbed system in open-loop. “Open-loop” is interpreted here
in the sense of the defined control model: There is 10 feedback ol Ave m Gye noa na Pir)* Guay pacer! acon PxCO2) ay
deviations in the controlled variable from its setpoint to the control
Tigh) ates ated eyatenn tine conatante could result in sustained oseiations

## Page 87

164 Applications
“Name Symbol | Value | Unit |
Map-heart rate gain men | -14 min mm Hg
Map-myocardial contractility gain “| a " =0.016 mi ;
Map-systemic arteriolar —_ -0.027 | smit
resistance gain |
i
|
|
I
“Map-venous unstressed volume gain © ices QE ml mm Hg+ :
Taste 10.4 Gains of the Control of Circulation Model
Name Symbol | Value | Unit
Baroreceptor lower threshold BR an 1 #2 mm Hg |
Baroreceptor saturation BR ax 112 mm Hg
Minimum heart rate HR in 40 min* |
Maximum heart rate HR. 200 min*
Minimum myocardial contractility MC, nin 0 mm Hg mit
Maximum myocardial contractility : MC. ox 12 mm Hg m+ 7
Minimum systemic arteriolar resistance SART in O;2 7 mm Hg mits” |
Maximum systemic arteriolar resistance SART..,, “2.4 mm Hg mi s
Minimum venous unstressed volume VUV nin 1000 ml -
Maximum venous unstressed volume VUV ay 4000 | mi
Taste 10.5 Activation and Saturation Function Parameters of the Control of
Circulation Model
Assuming a constant ratio between tidal volume and respiratory
rate of 500/12 = 41.7 ml min, tidal volume and respiratory rate can be
computed from minute ventilation.
500
UpS. 7 (VE + Ave) (10.5)
} 12.
] re Boo Ext + Ave) (10,6)
Physiological limits are applied to these two variables, The
output variable muscle pressure amplitude tt computed from teal
Physislogic Control
volume via the inverse total lung and chest wall compliance
(Table 9.3).
i,
ipa 5 (10.7)
This computation ignores the dynamic nature of the breathing
cycle. Table 10.6 lists the parameters of the operating point of the
respiratory system. Via Eq. (10.7) the tidal volume reference
corresponds to the muscle pressure amplitude in Table 9.3. The rate
reference corresponds to the respiratory period in the same table.
The setpoints should correspond to the values of corresponding
outputs of the unperturbed lung mechanics and uptake and
distribution models in open-loop.’
Table 10.7 lists the gains of the control of breathing model. These
gains are set empirically with respect to the minute ventilation in the
operating point so that a decrease of 5 mm Hg in p,CO, leads to
apnea, The response to oxygen is half as strong as the carbon dioxide
response, and in the opposite direction (a drop in oxygen leads to
hyperventilation).
Table 10.8 lists the activation and saturation function parameters
of the control of breathing model. .
Name | Symbol Value Unit
Tidal volume reference | Vow _ 500 mi
Respiratory rate reference ; RR... ap mint
Partial pressure of oxygen in F Oo, 100 mm He "
arterial blood.
Partial pressure of carbon dioxide PCO). 40 mm Hg
in arterial blood. |
Taste 10.6 Operating Point of the Unperturbed Respiratory Modeis in Open-Loop
Name Symbol Value Unit
Oxygen-minute ventilation gain Gvejoaos «=| 700 mi min mm Hg
Carbon dioxide-minute | Greracos 1200.) mimintmm He
ventilation gain !
Taste 10.7 Gains of the Control of Breathing Model
’ Veriied tay alin tianiocdele in the MITIivan! software
165

## Page 88

166 Applications
Name Symbol _—- Value Unit
Oxygen receptor lower threshold
| 20 _omm Hg
| Oxygen receptor saturation
Carbon dioxide receptor lower threshold
Carbon dioxide receptor saturation
Minimum tidal volume
Maximum tidal volume b ET a
Minimum respiratory rate PRE
Maximum respiratory rate RR ay
Taste 10.8 Activation and Saturation Function Parameters of the Control of
Breathing Model
References and Further Reading
Unlike the baroreceptor activation function, the modeled p,O,
and p,CO, receptor activation functions are not symmetrical around
the setpoint. The lower threshold on the oxygen receptor is set equal
to the setpoint. This eliminates the oxygen response for p,O, > 100
mm Hg; high oxygen does not cause hypoventilation. The limits
imposed on the control effectors are again empirically set general
physiological limits for a healthy adult male, not only reflecting the
influence of control of breathing.
Chiari L, Avanzolini G, Ursino M. A comprehensive simulator of the human respiratory system: validation with experimental and simulated data. Ann Biomed
Eng. Nov-Dec 1997; 25(6):985-99.
Goodwin JA, van Meurs WL, $4 Couto CD, Beneken JEW, Graves SA. A mode!
for educational simulation of infant cardiovascular physiology. Anest Analg.
Dec 2004; 99(6):1655-64.
Guyton AC, Hall JE. Textbook of medical physiology. lth ed. Philadelphia:
WB. Saunders; 2006.
Khoo MCK. Physiological control systems, analysis simulation, and estimoation.,
New York: Wilev-IEEE Press; 1999.
Ursino M. Interaction between carotid baroregulation and the pulsating heart: a
mathematical model. Am J Physiol Heart Circ Physiol. 1998; 275: H1733-H174'
Ten Voorde B. Modeling the baroreflex: a system analysis approach |thes ).
Amsterdam, The Netherlands: Vakgroep Medische Fysica; 1992.
Van de Vegte J. Feedback control systems. 3° ed. Englewood Cliffs, NJ: Prentice Hall;
1994.
Wesseling KH, Settels JJ. Baromodulation explains short-term blood pressure vari
ability. In: Orlebeke JF, Mulder G, van Doornen LIP, eds. Psychophysiology 0/
cardiovascular control. New York: Plenum Press; 1985:69-97.
Zijimans M, S4-Couto CD, van Meurs WL, Goodwin JA, Andrionien 2. Corrected
and improved model for educational simulation of neonatal ¢ arcdlovaseular
pathophysiology [technical report}, Simul Healtic Spring 200% Ade os
parr UT
Advanced
Topics
CHAPTER 11 Cuapter 12
Sensitivity Analysis Design of Model-Driven Acute
Care Training Simulators

## Page 89

CHAPTER 11
Sensitivity Analysis
40

## Page 90

n this chapter we describe a method for establishing relative
sensitivity of model outputs to changes in model parameters,
and apply it to a selection of model Parameters and outputs
of the hemodynamic model introduced in Chap. 8. Physiological
consistency of the results is discussed.
A sensitivity analysis basically answers the questions: “What is
affected by what, and by how much?” We can consider the sensitivity
of output variables to input variables, parameters, and initial
conditions. Sensitivity analysis has been applied to physiological
models for evaluation of the relevance of a particular parameter to
the model response, for reduction of model complexity, and to assist
in parameter estimation. In Sec. 11.1 we introduce a method for
establishing relative sensitivity of model outputs to changes in model
parameters. In the subsequent section we apply this technique to the
uncontrolled hemodynamic model introduced in Chap. 8, with the
specific purpose to assist users of a model-driven training simulator
in programming new patients.
11.1 Method
Consider a mathematical model with M parameters PL cog ME
and N output variables v,j=1,2,...,N. Let P., be the baseline value
for parameter P,and Bq the baseline value for variable v . A variation
AP, in P, potentially causes variations Av, in all variables v, For a
dynamic model, steady-state conditions need to be considered. The
relative sensitivity of the output variable v, to the parameter P, is
defined as:
= Ao; [Pio
ij AB /P.y (1.1)
The values S, constitute an M x N matrix, called the relative sensitivity matrix, The elements of this matrix are easily interpreted as the
relative change in an output variable in response to a relative change
ia parameter, For example, the relative sensitivity of systolic blood

## Page 91

172
41.2 Application to a Hemodynamic Model
* =
Advanced Topics
pressure (SBP) to heart rate (HR) in the uncontrolled hemodynamic
model presented in Chap. 8 is 0.26. This means that a 10% increase in
HR will lead to an approximately 2.6% increase in SBP. The
normalized, dimensionless elements in the sensitivity matrix can be
compared among each other, even if the output variables have
different units. For example, the relative sensitivity of cardiac output
(CO) to HR in the same model is 0.41. In this model, CO is more
sensitive to HR than SBP.
For simple models, the sensitivity matrix may have an analytical
solution, obtained via differentiation. For nonlinear, dynamic modeis,
itis often determined via simulation experiments. The results presented
in the next section are obtained with AP,/P,,, = 0.01; that is, simulations
are carried out to evaluate the effect of a positive 1% change in each
parameter, one at a time. The size of this change has to be carefully
balanced: Too small a parameter change may result in truncation
errors in the subtractions involved in computing the changes in the
variables, whereas too big a parameter changes may result in nonlinear
effects. For a nonlinear model, the sensitivity matrix also depends on
the particular operating point. Additional information can be obtained
by modifying the magnitude of the parameter change, or its sign, and
by combining changes in parameters.
When interpreting relative sensitivities, it has to be noted that
typical changes in parameters may differ greatly. For example, the
sensitivities of flow rates and blood pressures to changes in systemic
vascular resistance (SVR) are much higher than the sensitivities to
changes in cardiac valve resistances; doubling SVR results in
considerable physiological changes, whereas doubling of the
resistance of a cardiac valve has no observable effects at all. Yet, in
valve disease, the increase in resistance may be as much as hundredfold, resulting in a significant effect. Another limit associated
with relative sensitivity is that it amplifies absolute changes in
variables with a low baseline value. For example, the relative
sensitivity of central venous pressure to parameter changes is
amplified by an average baseline value close to 0 mm Hg.
The sensitivity analysis introduced in the previous section is applied
io selected parameters and output variables of the hemodynamic
model introduced in Chap. 8. This analysis involves the unperturbed
model in its open-loop operating point (also see Chap. 10). We will
refer to this model as the Beneken model. This model was also the
basis of the cardiovascular model used in the Human Patient
Simulator (HPS®), developed at the University of Mlorida, and
commercialized by Medical Education ‘Technologies, Ine. In the
context of the development of a simulator-basect hemodynank
monitoring, classy (Ohrn, 1995) HPS" developers introduced eis
Sensitivity Analysis
normalized hemodynamic “factors” grouping selected model
parameters that can be used to adapt an existing baseline patient to
reflect a specific physiology or pathology. The relationship between
these factors and the corresponding parameters in the Beneken
model is reflected in Tables 11.la and b. These tables present the
quantitative results of a sensitivity analysis, as well as a condensed
view, indicating only the sign and the number of significant digits in
Beneken SBP ‘DBP SPAP | DPAP | CO HPS® factor
model
parameter
‘HR . 0.26 0.54 70.15 | _0.46 0.44 Heart rate
- 0.09 | 0.06 | -0.02, -0.16 | 0.07 Left ventricular
| contractility
Eos 015 | 015 019 | 0.23 | 0.46 | Right
| | ventricular
| i contractility
Ree | 044 | 0.67 | -0.10 | -0.05 _ -0.14 | SVR /
O8R, __-0.07 | -0.07 | 0.31 073 -0.07 | PVR |
UV, tUV,, “1.34 -1.33 | -4.53 -4.99 | -1.27 | Venous
= i capacity
SBP, systolic blood pressure; DBP, diastolic biood pressure; SPAF, systolic pulmonary
artery pressure; DPAP, diastolic pulmonary artery pressure; CO, cardiac output.
Taste 11.1a Sensitivity Analysis, Quantitative Results
Beneken SBP DBP | SPAP DPAP co HPS® factor ;
model |
parameter |
HR ++ ++ ce ++ ++ Heart rate
Emax 12 - i te + Left ventricular
{ _ contractility
E max he i pas ah ++ ++ Right ventricular
_ d ee contractility
Specie
sai je ee ee --__| SVR
0.8 R, | - | ++ ++ ase PVR
UV, + UV jae | a pe ae | Venous capacity
Tape LA4b Sensitivity Analysis, Condensed View ~
173

## Page 92

JJ Advanced Topics
the result, respectively. The results of this sensitivity analysis apply
most directly to the baseline patient called “Stan Vintage” (van
Meurs, 2006).
These results are consistent with a more extensive sensitivity
analysis of the same model presented by Sa Couto and van Meurs
(2009). Most of the sensitivities are fairly intuitive; increases in both
HR and SVR (&,,,) result in increases in SBP and DBP, but an increase
in HR results in an increase in CO, whereas an increase in SVR results
ina decrease in CO. The strong effect of venous capacity on the whole
circulation and the effect of right ventricular contractility on both
pulmonary and systemic pressures are noteworthy. The negative
sensitivity of SPAP to HR may be due to a redistribution of blood
volume between the pulmonary and systemic parts of the circulation,
and is consistent with a reduction in CVP following the increase in
HR. The results of the sensitivity analysis can also be interpreted in
the opposite direction: What are the parameters affecting a particular
variable? For example, CO is strongly depressed by an increase in
venous capacity (venodilation) and strongly stimulatedby an increase
in HR. In this model and this operating point, the effect of left
ventricular contractility on CO is rather limited.
References and Further Reading
Ohrn MAK, van Meurs WL, Good ML. Laboratory classes: replacing animals with
a patient simulator [abstract]. Anesthesiology. 1995; 83(3A):A1028.
S4 Couto CD, van Meurs WL. Sensitivity analysis of a hemodynamic mode! to
facilitate programming simulation patients. in: S4 Couto CD. Mathematical
models for educational simulation of cardiovascular pathophysiology [thesis].
Porto, Portugal: University of Porto College of Engineering; 2009.
Van Meurs WL, Neto P, Azevedo H, $4 Couto CD. “Stan Vintage”: A baseline
patient for the Human Patient Simulator with hemodynamic parameters from
the scientific literature [abstract]. Simul Healthc. 2006; 1@):183.
CHAPTER 12
Design of ModelDriven Acute Care
Training Simulators
M5

## Page 93

simulation-based training program is designed to meet
carefully specified training needs. In the case of full-mission
simulations for training high-performance tasks we strive
for a high level of functional fidelity, which pertains to the similarity
of trainee behavior in the simulated and real environments. Physical
fidelity is the extent to which the appearance and behavior of a
simulator match the appearance and behavior of the simulated
system. Sufficient physical fidelity is achieved if a designed simulator
allows meeting the specified training needs at the desired level of
functional fidelity. Model requirements are set, and operational!
validity established, based on the required simulator behavior.
Aphysiologic modelis rarely designed and evaluated in isolation;
its requirements are embedded in more general project goals, and
evaluation of conceptual and operational validity (Chap. 6) refers
back to these requirements. The purpose of this chapter is to illustrate
how model requirements can be derived from more general process
and device requirements. We will use simulation-based training in
anesthesia as an example.
Farmer et al. (1999) observe that the most critical skills acquired
with the aid of mil itary training simulators are skills required for the
performance of so-called high-performance tasks. These tasks are
defined as complex, time-critical tasks where the operator is in the
primary control loop. Farmer et al. further define a full-mission
simulator as a top-level training device that provides all the required
cues and facilities necessary for training complete missions (of a
specific weapon system). Many tasks in acute care medicine
(anesthesia, intensive care, emergency medicine, and labor and
delivery)
are high>performance tasks, and, starting with the specialty
Of aneathewla, several fullemission simulations and simulators were

## Page 94

178
Advanced Topics
developed (Denson, 1969; Gaba, 1988; Good, 1989; Chopra, 1994;
Rettedal, 1996).
Training in a simulated acute care environment has a number of
advantages over training in the clinical environment. First, the real
patient, or an animal model, is replaced by a simulator. Errors can be
made and learned from, without any other consequences; rare critical
events can be trained on demand; and the pace of training can be
adapted to the progress of the trainees. However, realism in the
simulated environment is necessarily limited, and often comes at a
cost. Some discrepancies between the simulated and real
environments may be acceptable, and can be overcome by soliciting
the imagination of trainees, who are capable of remarkable leaps of
faith, provided they buy into the simulation. Other discrepancies
could impede meeting the educational goals. The design of
simulation-based training programs and training simulators face:
the challenge of anticipating what needs to be included and what car
be left out, while keeping the design pedagogically coherent, anc
technically and economically feasible.
Two concepts can provide guidance in simulation and simulator
design. Functional fidelity pertains to the similarity of trainee behavior
in the simulated and real environments. Physical fidelity is the extent
to which the appearance and behavior of a simulator match the
appearance and behavior of the simulated system. Farmer et al.
present a detailed procedure for the design and evaluation of training
programs and simulators. In the next two sections we briefly present
this procedure and illustrate how it can be applied in health care
simulation, backtracking certain aspects of the design of full-mission
anesthesia simulations and simulators.’ Specification of model
requirements fits in this procedure, and is the topic of the final
section.
12.4 Training Program Design
The design of a training program is based on the results of a training
needs analysis (TNA).? Table 12.1 lists the main steps in TNA as
specified by Farmer et al. and provides a few examples of what is
subject to analysis for the target learners: anesthesia residents.
A training program can now be designed to meet the identified
training needs. Table 12.2 lists the main steps in training program
1 In many practical situations, simulation program design will follow, rather than
precede, simulator design, and be carried out by different (teams of) designers
using available training media. However, the principle of letting educational
considerations drive simulator evaluation and procurement also applies i
these situations.
2 In this chapter we will not consider the more global objectivesof (he heallh
care
svetem and overall cureedhiny
Design of Model-Driven Acute Care Training Simulators
= —
| - Examples
| Mission analysis Airway management
and mechanical ventilation
lor general anesthesia
Task analysis Machine check, preoxygenation, medication,
| laryngoscopy and tracheal intubation, ventilator
operation, weaning and extubation, troubleshooting: |
_ | difficult airway, breathing circuit problems i
| Trainee analysis Performance on an intubation part-task trainer f
__Training analysis | Formulation of skill tests 7 I
Taste 12.4 Main Steps in Training Needs Analysis
: | Examples
| |
|
| Specification of Briefing, normal intubation and mechanical
| training activities ; ventilation, airway complication, breathing
a . |_cirouit problem, debriefing
Scenario design
| Design of instr
Cannot intubate/cannot ventilate, breathing
_ circuit disconnect |
Prompting by a facilitator? ;
Taste 12.2 Main Steps in Training Program Design
design (TPD). Background information for TNA and TPD can be
found in Bready (2007), or in more traditional anesthesia textbooks
and guidelines.
In the case of iull-mission simulations for training highperformance tasks, we strive for a high level of functional fidelity,
under the assumption that this facilitates transfer of skills acquired
in the simulated environment to the real environment. Any TPD
decision that brings the (anticipated) behavior of the trainee in the
simulated environment closer to behavior in the real environment
increases functional fidelity. Other factors that contribute tc
functional fidelity include competent instructors using appropriate
training media, An important aspect of training media specification
(TMS), simulator design, is presented in the next section.
Functional fidelity is a useful simulation design concept, but has
limited application in training evaluation (TE), mainly because it
does not reflect endpoints, such as increased task performance or
improved patient outcome. Preimplementation evaluation of a
proposed training, program can be achieved by submitting the
content to domain experts, After implementation of a simulationbased Lalning program, TE ean focus on endpoints, for example, by
179

## Page 95

180
soionser noma cee
Advanced Topics
assessing the performance of trainees on standardized skill tests.
Sometimes improved health care in terms of patient outcomes can be
demonstrated, see, for example, Draycott et al. (2006). More subjective
forms of TE include check lists filled out by instructors and selfevaluation and satisfaction scores by trainees.
sate abanke SHIM STUN NETS
12.2 Simulator Design
Dieckmann et al. (2007) observed that it is not uniformly the case that
more physical fidelity means better attainment of educational goals.
However, the level of physical fidelity needs to be sufficient to meet
the specified training needs at the desired level of functional fidelity
in a majority of trainees. As observed in the previous section, in the
case of full-mission simulations for training high-performance tasks,
the desired level of functional fidelity is high. Simulators supporting
these objectives should therefore have a sufficiently high level of
sical fidelity.
ar aacaaiie simulator design, we briefly introduce the
functional units of acute-care simulators. All but one of the fullmission acute-care simulators listed in the introductory section to
this chapter, and many part-task trainers, are script-controlled,
model-driven devices (van Meurs, 1997). Figure 12.1 shows the main
functional units in such simulators.
The trainees interact with the simulator via a number of
interfaces for clinical signs, monitored signals, and therapeutic
interventions. The patient mannequin and medical devices can be
real, or emulated on a computer screen. The instructor, pOmennirs
assisted by an operator, has run-time, and possibly off-line control
over the simulation. The instructor can make the simulated patient
evolve or react to therapeutic interventions, but in that is often
assisted by a combination of time-and-event-based scenario
Airway
1 Clinical signs
Device emulators
be
initialization | | =
Patient selection : in Medica |
Scenario contrat | i device ? ‘
Tt model “
ua otk Trainee(s)
>| 7 State *)/ Patient) Ps
operator }
\machine, Anode! t
ss {Real)
Medical
devices
t
te
instructor/ —| t
f
| a
c
ie
-2 =
State of simulator Simulation:
Trainee performance
Simutator Physico-chemica
quantities
Fiaure 12.1 Functional units and run-time information flow in a serpt
controlled model-driven simulator (Adapted from van Maurs, 200; 3)
Design of Model-Driven Acute Care Training Simulators
Examples
| Interfaces | Trainee Mannequin Airway, breath sounds
| Interfaces | Monitors Capnograph :
| i Therapeutic Mechanical ventilator
_| devices |
| | Instructor | Run-time : Patient and scenario
interfaces | selection
Off-line : Log of trainee activities -
Simulation Models | Patient Respiratory system
engine | l” Devices | Gas mixing in ventilator
- Scripts wcilh | Triggering airway occluder |
TasLe 12.3 Functional Units in an Acute Care Training Simulator
scripts, running on a finite state machine, and continuous-time
models. Table 12.3 further divides these functional units and
provides examples of what needs to be incorporated to create a
simulator implementing the training program outlined in the
previous section.
Appearance and behavior of the trainee interfaces are subject to
design and directly influence physical fidelity. For example, to
optimize physical and functional fidelity we decide that a full-body
mannequin and a real mechanical ventilator and real monitoring
equipment will be used. This implies that the simulator needs to
interface with these devices. It also implies that a device model for
gas mixing in the ventilator is not required. Another example is
that breath sounds need to appear in appropriate locations, and
need to be bilateral so that endobronchial intubation’ can be
diagnosed.
Appearance and behavior of the instructor-operator interface are
also subject to design, but only indirectly influence physical fidelity.
However, careful design can enhance ease of operation, and inclusion
of learning management tools can increase the impact of a simulation.
Examples of off-line instructor interface tools include patient and
scenario editors. Both run-time and off-line instructor interfaces may
interact with physiologic models, and specific model requirements
may result. The concept of hemodynamic factors, described in Sec.
11.2, constitutes an example.
The simulation engine is the main determinant of simulator
behavior, and an important factor in physical fidelity. For example, to
Ponitioning of the tip ofan endotracheal tube beyond the split of the trachea in
one ofthe mainatem bronchi leads to ventilation of a aingle hing
181

## Page 96

Advanced Topics
simulate airway management and mechanical ventilation, alveolar
oxygen and carbon dioxide should depend in a realistic fashion on
the timing and precision of tracheal intubation, and on tidal volume
and respiratory rate set on a mechanical ventilator. Some of the
dynamic aspects of patient evolution and responses to therapy can be
taken into account by a script. For example, an airway occluder,
actuated by the instructor or by a scenario script, is required to
implement the cannot ventilate/cannot jntubate scenario. However, a
scripted simulation cannot be designed to anticipate all possible
management options, nor generate all desired output signals,
especially in the case of multiple, continuous independent and
dependent variables. Therefore, this requirement leads to the
adoption of an at least partially model-driven simulation engine.
Model requirements will be discussed further in the next section.
In many cases, the extent to which the appearance and behavior
of a simulator match the appearance and behavior of the simulated
system is a subjective notion, and can only be evaluated qualitatively.
Another design challenge results from the interdependence of
interface and simulation engine design. For example, for realistic
simulation of endotracheal intubation, the anatomy of the airway
needs to be correct, breath sounds need to appear in the right locations
and be triggered appropriately, and physiologic responses need to be
suitable.
Other considerations in simulator design include economic and
technological feasibility, and safety, cost, and ease of operation and
maintenance. The effect of any remaining discrepancies between the
appearanceand behavior of simulated and real patients and equipment
can be mitigated by addressing them in a simulation briefing.
Elaborating on our comment in the previous section, functional and
physical fidelity are useful concepts in the simulation and simulator
design, but do not reflect endpoints in the effect of training. Training
evaluation (TE) following simulator development and training
program implementation remains the primary tool to demonstrate
adequacy (or insufficiency) of simulations and simulators.
Model Requirements
Many acute-care simulation projects have in common therequirement
to provide realistic and consistent evolution of clinical signs and
monitored signals, and of their response to therapeutic interventions
(Zijlmans, 2009). A simulation engine can generate these variables
automatically and in real time. For complex systems this simulation
engine needs to include models. Realistic reactions require
appropriate interactions between physiological subsystems, For
example, in the case of mee hanical ventilation with higher airway
pressures, the circulation
should become pro rrossively compromised
is ny
This requirement leads to a pray box moceling approach where tht
Design of Model-Driven Acute Care Training Simulators
resulting models reflect structure and function, facilitating coupling
of models of physiological subsystems. In educational sonata it as
often required to adapt the physiology of the patient to simulate
pathologies or critical incidents. This requirement further reinforces
the preference for a gray-box modeling approach, so that models can
be manipulated in a logical fashion to achieve the desired goals
Following the format of Table 2.1, qualitative requirements a a
gray-box model, part of a simulator for training airway management
a ee ventilation for general anesthesia, are listed in
The specific examples listed in Table 12.4 can all be traced back to
simulator or simulation scenario requirements presented in the
previous sections. Although the main training objectives are airway
management and mechanical ventilation, simulation of induction of
anesthesia also requires a reasonably realistic response of both the
cardiovascular and respiratory systems to anesthetic agents. An
Examples
or physiological Lung mechanics, uptake and distribution of
_ Subsystem — respiratory gases, effect of anesthetic agents
Population | ASAPS 1, 2,* patient with a difficult airway.
__ Physiological states _ Normal
| Pathologies ~ None
Clinical signs and
monitored variables
Breath sounds, capnogram, pulse oximetry
Critical incidents
' Cannot intubate/cannot ventilate, breathing
circuit disconnect
interventions
Preoxygenation, medication, ventilator settings
Overall biock diagram
J See main text
Internal structures and
functions
To be determined
*American Society of Anesthesiologists (ASA) i
n ; . s gists ) Physical Status (PS) reflecti
healthy patients and patients with mild systemic disease. iii
Taste 12.4 Qualitative Model Requirements
Insp. oxygen fraction ——p}
Anesthetic agents ——p}
Airway preagure ———!
AINWAY OOOIUAOE =
Piaune 28
Model of the
system
cardiorespiratory
+» Arterial oxygen saturation
+—— Arterial blood pressure
>» Electrocardiogram
}-_—» Expired gas composition
Overall blook diagram
of the cardiorespiratory model,
183

## Page 97

184
Advanced Topics
overall block diagram of the cardiorespiratory model is given in
Fig. 12.2.
The output variables include signals shown on standard monitors
for induction of anesthesia. The model requirements can be met
using a mathematical model and model development can follow the
process outlined in this book. Alternatively, models can be
implemented using both mathematical and physical components.
Such hybrid models are difficult to design, but have the advantage
that the interaction with, for example, a real ventilator and gas
analyzer takes place via physical quantities, rather than via computer
generated variables. For example, a hybrid lung mechanics model,
using real gas flows and an anatomically correct airway (Sajan, 1993),
can easily detect endobronchial intubation or insufficient sealing of
the airway, thus increasing physical fidelity. Note that these
phenomena are difficult to observe otherwise.
In the previous sections we observed that in the case of fullmission simulations for training high-performance tasks we strive
for a high level of functional fidelity. The level of physical fidelity of
a simulator needs to be sufficient to meet the specified training
needs at the desired level of functional fidelity. The simulation
engine is the main determinant of simulator behavior, and an
important factor in physical fidelity. We recall from Chap. 6 that a
model is considered operationally valid for a set of experimental
conditions if its accuracy is acceptable for the intended purpose.
This is a slightly more formal way of looking at one of the components of physical fidelity: The extent to which the behavior of a
simulator matches the behavior of the simulated system. Target data
for a representative set of clinical situations, likely to be encountered
in a simulation-based training exercise, form the basis of model
validation. What is acceptable in view of the educational objectives
may remain a matter of informed opinion. We also recall from Chap.
6 that target data for the rare and dangerous situations which are
most interesting in simulations for training high-performance tasks,
obtained on humans in carefully controlled conditions, are often not
available. Conceptual validity refers to the acceptability of the
incorporated theories, assumptions, and data. High-quality graybox models used in training simulators facilitate coupling of models
of physiological subsystems and manipulation of models to achieve
the desired educational goals.
The extensive example treated in this chapter demonstrates that
a physiologic model is rarely designed and evaluated in isolation; it
also illustrates how model requirements can be derived from more
general process and device requirements. It should be noted that
existing full-mission healthcare simulators were designed in much
less structured,
more intuitive, ways, The presented top-down design
process has too many assumptions and interplaying, factors lo evolye
References and Further Reading
Design of Model-Driven Acute Gare Training Simulators
into a true “science of acute care simulator design.” However, it may
provide guidance to the design of new simulations, simulators, and
models, and to the adaptation of existing ones, and its application
should increase the traceability of design decisions at several levels
to educational objectives.
Bready LL, Dillman D, Noorily SH, eds. Clinical decision making in anesthesiology,
4" ed. Philadelphia: Mosby Elsevier; 2007. .
Chopra V, et al. The Leiden anaesthesia simulator. Br J Anaesth 1994; 73:287-92.
Denson JS, Abrahamson 8. A computer-controlled patient simulator. JAMA. 1969;
208:504-8,
Dieckmann P, Gaba D, Rall M. Deepening the theoretical foundations of patient
simulation as social practice. Simul Healthc. Fall 2007: 2(3):183-93.
Draycott T, Sibanda T, Owen L, Akande V, Winter C, Reading $, Whitelaw A.
Does training in obstetric emergencies improve neonatal outcome? BJOG.
Feb 2006; 113(2):177-82.
Farmer E, van Rooij J, Riemersma J, Jorna P, Moraal J. Handbook of simulator-based
training, Aldershot: Ashgate; 1999. .
Gaba DM, DeAnda A. A comprehensive anesthesia simulation environment:
re-creating the operating room for research and training. Anesthesiology. 1988;
69:387-94, :
Good ML, Gravenstein JS. Anesthesia simulators and training devices. Int
Anesthesiol Clin 1989; 27(3):161-8.
Maran NJ, Glavin RJ. Low- to high-fidelity simulation — a continuum of medical
education? Med Educ. Nov 2003; 37 Suppl 1:22-8
Rettedal A, Stale F, Ragna K, Petter L. PatSim — simulator for practicing anaesthesia
and intensive care, development and observation. In! ] Clin Monit Comput.
1996, 13:147-52
Sajan 1, van Meurs WL, Lampotang 8, Good ML, Principe JC. Computer controlled
mechanical lung model for an anesthesia simulator, abstracted. int J Clin Monit
Comput. 1993; 10:194-5.
Van Meurs WL, Good ML, Lampotang S. Functional anatomy of full-scale patient
simulators. J Clin Monit. 1997; 13 7-24.
Van Meurs WL, SA Couto PM, SA Coute CD, Bernardes JE. Ayres-de-Campos D.
Development of foetal and neonatal s:mulators at the University of Porto. Med
Educ. 2003; 37 Suppl 1:29-33 ‘
Zijlmans M, SA-Couto CD, van Meurs WL, Goodwin JA, Andriessen P. Corrected
and improved model for educational simulation of neonatal cardiovascular
pathophysiology [technical report]. Simul Healthc. Spring 2009; 4(1):49-53.
185

## Page 98

_[No extractable text found on this page.]_

## Page 99

age mers flo fi
a
securaey, 9-10, 18
Bein potential, 36
algerithes.
aller integration stop
sizes, 90-92,
feedback, 89-90
‘ostline, 8h
rl sie. 8-8
i series mele, S88
bien expert 66,137
analog to dig
conversion ADC),
sigs 8 88, 0-72
lectical,
72
hhyesnlic, 72
analytical sattions,
anesthesia
adrante analog, 72
rnin simi fo, 20,
Ts18
sual 4,102,178
sorts, 20-121
Bove vive, 2
espsctieiy
Tnaoree, ISE-I58, 1614, Se ws
‘atl
of circa
biomedical engineering 10
ack diagram, 3458
ardiorespiraary syste,
384 38, 39, 112
chemoreceptor contro, 7H
contro of eveathing,3
isemodnamic mute, 2
Ing mecha,
Tings
al area
RODS fori femperaure
pressure saamatel ce,
2152
eee
eapacitrs, 73
in parallel, in seis, 7
jorespiacor: See made
Fequiements;concenual
sels
Eero, 7
lectial 20-75
fbn, 869,75,
‘otelatos. Sa hemtalynamios
nea signs 20-25, 18

## Page 100

190
Inder
aM oting. 08-2
eels, evs
Vaio wal 132-143,
Ai, 148
tng 2-48, 146-18,
Mist
Seve atote vale
Iemedynamics
componestclageams. 9
rca eeu 50,
conven. exchange, 4UF
coaen sing 5
“
syieres
syste 8h
ne
Tepresentatone
Tralnespatoy S750
Wan
“tse
Tung mesos, 1-142
120
nplake an distin,
ar
Sez sho back dnp:
corte bo dion, 1-954
woe,
ale
Systems 5.10
os tathng,
12 186-60,
tenet
T-To8
ceca nee, 20-25, 98 1
cS
end
spa, eat 1,
Tous
deerminstionstems6
Sieutoshon,
o8
aiestetime
avaiable model 2-8
wipes 32.
“pout, 102-403
c:
cpt
oak
feta
0
oan, 187A
una t
fe
Tutonal olny prs
2
har. Se tem nauis
hhemeclyzamic factors,
hh
He in
etarchies
anatomical, 35
block dingram, 97-30,
highsperiormnayce tis, 177-18
hharaan pation slate
es,
‘rumeatace throughput, 55,90
“5
impulse respons 78
indepesdent
ste variables,
7s
ngs wales, 4
integration step se, 84, 99
sertaces,
2-27, 18-18
:nterpolrion 90
intracramiel pressere ICY,
:
inteapleuraz apace, 145, 142
Insratlarace pees, I
55
ir
K
ant
‘elle
he Mi
Ingex 198
i
Laplace anata.
teatro search,
LEU Gia nanan
satin,2
Tung means. 12%, 135-135,
TAA, M64, 15
ws Mo
tas balance, 138, 150. Se a
smathesatica! model8 7-20
contual af beating,
eae
contrat of cecuation
162-164
muscle
ie
il equations
ste vatabie mls
MIMO simlpiespat
raltiieopat systems,
sta eave. 31)
aed eequiresens
e100, 182-18
19.28,
ory system
eum, 183k
conte of breathing
15-150
oni of een,
158-1
hooynamies;
Hn eectanis. 13S
ist
cualative, 79.29, 182
uantativ, 2-24
‘ptakeand distrbution,
135-157, 2531
Sus aso inertia tae
twoaeling and simation,
Ine ape
Prdones He
Peng 2

## Page 101

192 Inder
device 180-38
empincal or ack-bow8,
33.3875
expintey witb,
icnowlaige Based 52
BA
gry 621,78 182088
obi 6
physi §24
multe mel
dla38 9,
1,1, 101788
smtp model 68 13-2
rer
ee N wei
neonatal incensive care
training sate fr 10
stv system
Sypeti, 222-919
Newlan
‘Sand J of ten
a0
snurserial ntegstion, 83,36 8
oes hee
ian
‘Onna 75
operating po
102-16, 16,
‘sustone CDE), 48
Secale 5051
soil
[parameter etiation,
8,20
72578, 9%, 10, 102, 108, 17
partes tener, 180
Davia! presse, 60-65
pathologies, 20-21, 27, 91,202
Physiological states, 20-21
physiological spats, 10,18,
238,42
Poise’
lav 68
pppolatians, 8, 20-21, 27, 102,
13
progr rguements 27
prog:aruming langages, 27
plmonscy ens exchange. See
‘avake nd istiguton
pulmonic valve, 121F
meee
‘sic pes a, 36
quautization 3
ff variables, 22-23, 96811
reo time, 27, 85-87, 152
receptor aetivarion fametin,
relive humic 137
relative sensitiv 17
masts,
17
residuais, 101
sistance, 58-6
‘airway, 74, Ll, 196,138
ue
sestemie aerials, 7,
120,183, 186189
esolition, 22-28, 991,117
espinaton.235 iv fas hang
sitution
sampling,4 90
imerval8
shun, Ws
Feaction, Lae
SL Sorte ea
nits
Signa 3-5
simatation, 11
‘engine, 189-14
Sera mesteing
simulation
sinwlsoes, Se
leaning simon
SISO fsngie-npat single
‘output systems, §
soteeane
implemestetion, 24, 83-95,
is
verifieation, 86-87
sob 6-€8
Sate variable mites, 5
4
onal units
comeing, 75, 87.98
itemstysamies, 123-229
hm mechansee, 146-145
Dropertis
af, 5456
‘uneake and station,
8-15),
tote varices $8.54 82465, 6
78, 128-126, o- 148
15-152,
STP anda emperatare
8 Take
Index 193
subyatems
titra to separate, 25-87
Suboic tation, 11-12, 23-23
systems 4?
aiscreteevent6 4
von
lange date 27-25, 98-905, 184
Uerapeuticimerventions, 2-3
94 102,10, 285,
training
evaluation, 770.750
sein, 179
ees, 178
Programs, 278159
Sirltor, 10-300, 178-382
transterémctions 48, 28-78
ransmural presse
134.530
lecospesaive, I
a Yo
ncntollenael orate,
18 Steals conte
"plake and astioutian, 11
15-137, Hast
elation,
concer tna 98-199, 181
fst 1
‘petational 98-103, 284
‘enous unsteseel wom, 17,
13, 158-158
vereation 6-87, 92-109,
