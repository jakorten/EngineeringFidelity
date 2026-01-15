# Manikins With Human-Like Chest Properties—A New Tool for Chest Compression Research

**Authors:** Nysæther JB, Dorph E, Rafoss I, Steen PA
**Venue:** IEEE Transactions on Biomedical Engineering, Vol. 55, No. 11, November 2008
**DOI:** 10.1109/TBME.2008.2001289

---

## Abstract

Commercially available CPR training manikins do not accurately mimic the mechanical properties of human chests. This paper presents manikins with chest properties matching those measured in 59 cardiac arrest patients during out-of-hospital CPR. Eight interchangeable chest force-depth profiles were constructed, representing the measured range of chest stiffness and average damping.

---

## Key Data (PRIMARY SOURCE for human chest mechanical properties)

### Study Population
- **n = 59** cardiac arrest patients
- Out-of-hospital CPR (Akershus Norway, Stockholm Sweden, London England)
- Data collected October 2004 - March 2005

### Equipment
- Philips Heartstart 4000 defibrillator with compression sensor
- Force sensor (HBM DF2S-LAD)
- Accelerometer (ADXL202e)
- Depth calculated from double integration of acceleration

### Mechanical Model
```
F_c ≈ k(x)·x + μ(x)·v

where:
  F_c = compression force from rescuer
  k(x) = chest stiffness (depth-dependent)
  x = chest displacement
  μ(x) = damping coefficient (depth-dependent)
  v = chest velocity
```

---

## Results: Human Chest Properties

### Stiffness (Spring Force)

| Metric | Value |
|--------|-------|
| Mean force for 38mm depth | **270 ± 150 N** |
| Force range for 38mm depth | 120 - 420 N (from SD) |
| Distribution | Lognormal |
| Calculated average stiffness | ~7 N/mm |
| Stiffness range | ~3 - 11 N/mm |

**Comparison to prior studies:**
| Study | Mean force at 38mm |
|-------|-------------------|
| Nysæther 2008 | 270 ± 150 N |
| Gruben 1993 | 430 ± 40 N |
| Tsitlik 1983 | 360 ± 150 N |

Note: Nysæther values are lower, possibly due to incomplete release compensation or surface compliance.

### Damping

| Metric | Value |
|--------|-------|
| Mean damping coefficient (10-30mm) | **169 ± 60 N·s/m** |
| Converted to mm units | **0.169 ± 0.06 N·s/mm** |
| Behavior | Increases with depth |

### Non-linearity

- Chest stiffness is **progressive** (non-linear)
- Force-depth relationship follows lognormal distribution
- Eight percentile-based profiles (S1-S8) span population range

---

## Manikin Design Based on Human Data

### Stiffness Profiles (S1-S8)
- Each profile represents 12.5% (one octile) of population
- S1 = softest, S8 = stiffest
- All profiles are non-linear/progressive
- Verified to match specification within ±30 N (30-50mm depth)

### Damping Mechanism
- Piston-cylinder with air slit
- Single damping profile (average of population)
- Verified: 167 ± 3 N·s/m (target: 169 N·s/m)

---

## Key Quotes for Paper

### On manikin limitations:
> "Commercially available training manikins for cardiopulmonary resuscitation (CPR) do not accurately mimic the mechanical properties of human chests."

### On linear vs non-linear:
> "While manikin chests have a predominantly linear force—depth relationship, a human chest shows a progressive, nonlinear stiffness."

### On damping importance:
> "The human chest is not only purely elastic, but also has a significant viscous damping component that is found to increase with compression depth."

### On variability:
> "Most available manikins use only one spring type to mimic the chest stiffness of the entire population, which does not account for the great variability in chest stiffness between patients."

---

## Relevance to MST Paper

### Primary source for C1, C2:
- **C1:** Human chest stiffness ~3-11 N/mm (derived from 270±150 N at 38mm)
- **C2:** Human chest damping ~0.17 N·s/mm (169±60 N·s/m)

### Key insight:
Nysæther is the **primary source** for human chest mechanical properties. Lim 2024 cites Nysæther for human reference values; Lim's own data (5.34-13.59 N/mm) describes their **manikin system range**, not human values.

### For reference model:
- Use Nysæther's lognormal distribution for uncertainty envelope
- Eight percentile profiles (S1-S8) could inform fidelity scoring
- Damping should be included in reference model (not just stiffness)

---

## References Cited (relevant)

- Gruben 1993: Sternal force-displacement during CPR (n=27)
- Tsitlik 1983: Elastic properties during CPR
- Tomlinson 2007: Force-depth relationship during OHCA CPR (n=91)
- Bankman 1990: Dynamic mechanical parameters identification

---

*Retrieved: 2026-01-15*
*Source: IEEE Xplore*
*File: /Users/jakorten/research/articles/md_out/Manikins_With_Human_Like_Chest_Propertie.md*
