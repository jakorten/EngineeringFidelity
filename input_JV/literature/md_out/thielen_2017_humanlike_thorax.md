# Thielen et al. 2017 - Human-Like Thorax CPR Manikin

**Full Citation:** Thielen M, Joshi R, Delbressine F, Bambang Oetomo S, Feijs L. An innovative design for cardiopulmonary resuscitation manikins based on a human-like thorax and embedded flow sensors. *Proc IMechE Part H: J Engineering in Medicine*. 2017;1-7. doi:10.1177/0954411917691555

**PDF:** `input_JV/literature/pdfs/thielen_2017_humanlike_thorax.pdf`

**Extracted:** 2026-01-21

---

## Summary

Design paper from TU Eindhoven presenting a novel CPR manikin with anatomically realistic thorax, embedded cardiovascular/respiratory systems, and flow sensors. Key contribution: demonstrates that classical manikins have linear force-displacement while humans (and their design) show nonlinear behavior.

**Core argument:** Improving physical/anatomical fidelity → increases functional/physiological fidelity.

---

## The Problem with Classical Manikins

### Single Spring-Damper Configuration (Figure 1)

Classical manikins use a single spring-damper system where:
- Displacement is **independent of compression location** (unrealistic)
- Sternum is stiff and does not tilt
- Force-displacement is essentially **linear**

> "like other classical designs, these manikins consist of a single spring–damper configuration... This displacement is independent of the axial location of the applied force since the manikin sternum is stiff and does not tilt, a behaviour unrealistic when compared to the human body."

### Even Advanced Manikins Fail

> "Despite the aforementioned recommendations and a clinical desire for physiologically and anatomically high-fidelity manikin designs, even the technologically most advanced manikins such as the **SimMan 3G** (Laerdal) and **Apollo** (CAE healthcare) **do not fulfil all these requirements**."

---

## Force-Displacement Model

### Gruben et al. Polynomial Model (Refs 7-9)

The compression force F consists of elastic (Fe) and damping (Fd) components:

```
F = Fe + Fd

Fe = k(z) · z
k(z) = k₁ + k₂·z + k₃·z² + k₄·z³

Fd = μ(z) · ż
μ(z) = d₀ + d₁·z
```

**Combined equation:**
```
F = k₁·z + k₂·z² + k₃·z³ + k₄·z⁴ + d₀·ż + d₁·z·ż
```

### Nonlinearity Comparison

| System | Higher-order coefficients | Behavior |
|--------|--------------------------|----------|
| Classical manikin | Only k₂ ≠ 0 | Near-linear |
| Human thorax | k₂, k₃, k₄ ≠ 0 | Nonlinear |
| Thielen manikin | k₂, k₃, k₄ ≠ 0 | Nonlinear (human-like) |

> "Our manikin, unlike typical manikins, shows a greater nonlinear relationship since the polynomial estimate of the force–displacement relationship has **three non-zero higher order components (k₂, k₃ and k₄)** while the typical manikin has only one higher order component (k₂)."

---

## Results (Figure 8)

Force-displacement curves at 5 cm depth (AHA guideline target):

| System | Force at 5 cm | Shape |
|--------|---------------|-------|
| Human thorax | ~700 N | Nonlinear, progressive |
| Classical manikin | ~600 N | Near-linear |
| Thielen manikin | ~200 N | Nonlinear but too soft |

**Key finding:** Their manikin achieves the correct nonlinear *shape* but with insufficient *stiffness*.

---

## Design Details

### Rib Cage
- Material: Polyoxymethylene (POM), 4mm thick
- Cut via laser engraver, heat-shaped
- Bolted to T1-T10 vertebrae of anatomical spine model
- Rationale: High stiffness, abrasion resistance, resilience to repeated load

### Respiratory System
| Component | Material | Specs |
|-----------|----------|-------|
| Lungs | PU memory foam | ρ = 45 kg/m³, silicone-coated |
| Bronchi | PVC | - |
| Trachea | Latex tube | ID = 2 cm |
| Airflow sensor | Honeywell AMW720P1 | In trachea |

### Cardiovascular System
| Component | Material | Specs |
|-----------|----------|-------|
| Ventricles | Latex balloons | 75 mL each (female reference) |
| Arteries | Latex tubing | ID = 1 cm |
| Heart wall | PE foam | ρ = 25 kg/m³ |
| Blood | Life/form simulation blood | - |
| Flow sensors | B.I.O-TECH Vision 2000 | In aortic & pulmonary arteries |

### Data Acquisition
- Arduino Uno microcontroller
- Processing software for real-time display
- Philips Q-CPR for force-displacement measurement

---

## Cardiac Output Results

At 120 CPM (AHA guideline):
- Total cardiac output: 1.65 L/min
- Left ventricle: 0.92 L/min
- Right ventricle: 0.73 L/min
- Air displacement: 2.7 L/min

Comparison:
- 48% lower than Fodden et al. (human Doppler measurement)
- 150% higher than Koeken et al. (physiological model, after scaling)

---

## Key Quotes

### On clinical need (p.2)
> "There is a key clinical demand for CPR manikins to **mimic human physiology** and monitor cardiac output, artificial ventilation and oxygen saturation in order to **provide feedback data for assessing CPR performance**."

### On fidelity relationship (p.6)
> "The novelty of this design is the anatomical design and construction of the manikin with the expectation that **improving physical fidelity increases functional fidelity** as showcased by Sawyer et al. in training simulators for intubation."

### On stiffness limitation (p.6)
> "However, the force required to achieve similar compression depths in humans is considerably higher. This indicates that **the stiffness of our manikin is low**."

### On material challenges (p.6)
> "The challenge herein is that the materials not only need to have **suitable material properties** but should also be **amiable to the rigours of manufacturing processes** such as laser cutting, heat shaping and injection moulding."

---

## Limitations (Stated)

1. Stiffness too low (less force needed than human thorax)
2. No valves in cardiovascular system
3. No connection between pulmonary and systemic circulations
4. Manufacturing constraints limited rib cage thickness
5. Higher density foams mimicking lung tissue unavailable

---

## Relevance to MST Paper

### VERY HIGH Relevance

1. **Directly supports mechanical fidelity concept:** Paper explicitly argues that anatomical/physical fidelity → functional/physiological fidelity

2. **Documents the linear vs nonlinear gap:** Classical manikins have linear F-D, humans have nonlinear F-D - this is exactly the "mechanical fidelity gap" we're characterizing

3. **Provides force-displacement model:** Gruben polynomial model could be used for our characterization methodology

4. **Names specific manikins as inadequate:** SimMan 3G and Apollo explicitly called out as not meeting fidelity requirements

5. **Dutch connection:** TU Eindhoven + Máxima Medisch Centrum - potential collaboration/citation network

### Quotable for Introduction

> "even the technologically most advanced manikins such as the SimMan 3G (Laerdal) and Apollo (CAE healthcare) do not fulfil all these requirements"

This directly supports I2 (no systematic benchmark exists) and the mechanical fidelity gap argument.

---

## References of Interest

| Ref | Citation | Potential Use |
|-----|----------|---------------|
| 7 | Bankman et al. 1990, IEEE Trans Biomed Eng | Human chest mechanical parameters during CPR |
| 8 | Gruben et al. 1990, IEEE Trans Biomed Eng | Mechanical measurement system during CPR |
| 9 | Gruben et al. 1999, IEEE Trans Biomed Eng | Canine sternal F-D relationship |
| 18 | Tomlinson et al. 2007 | Compression force-depth (already have) |
| 15 | Martin et al. 2013 | "Physiological" infant manikin design |

---

## Cross-Reference

- Related: Tomlinson 2007 (nonlinearity), Nysæther 2008 (human stiffness)
- Claim registry: Supports I2, potentially new claim on linear vs nonlinear gap

---

*Extracted: 2026-01-21*
