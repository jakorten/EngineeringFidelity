# A New Physiological Manikin to Test and Compare Ventilation Devices During CPR

**Authors:** Morin F, Polard L, Fresnel E, Richard M, Schmit H, Martin-Houitte C, Cordioli RL, Lebret M, Mercat A, Beloncle F, Savary D, Richard JC, Lesimple A
**Venue:** Resuscitation Plus 19 (2024) 100663
**DOI:** 10.1016/j.resplu.2024.100663

---

## Abstract

A new physiological manikin (SAM - Sarthe Anjou Mayenne) was developed to evaluate ventilation devices during CPR. The manikin reproduces:
- Functional residual capacity (FRC)
- Intrathoracic airway closure (via Starling resistor)
- CO2 production simulation
- Realistic passive ventilation during chest compressions

Validated against tracings from 3 OHCA patients. Used to compare B-card (continuous flow insufflation) vs ITD (impedance threshold device).

---

## Key Design Features

### Lung Model
| Component | Specification |
|-----------|---------------|
| Bellow capacity | 3 L maximum |
| Equilibrium volume (FRC) | 1.5 L |
| Compliance | **25 mL/cmH₂O** |
| Resistance | **5 cmH₂O·s/L** |
| Spring | Mimics elastic recoil above/below FRC |

### Airway Closure Simulation
- Starling resistor (collapsible tube in pressurized chamber)
- Simulates intrathoracic airway closure (~30% of OHCA patients)
- Affects capnogram pattern

### CO2 Production
- Continuous CO2 flow (0.1 L/min) into bellow base
- Enables capnogram analysis

### Realistic Head
- Georges manikin head (KerNel Biomedical)
- Dead space: 152 mL
- Resistance: 2.4 cmH₂O·s/L
- Supports invasive (ETT) and non-invasive (mask) ventilation

---

## Validation Data

### Comparison: SAM Manikin vs OHCA Patients (n=3)

| Parameter | OHCA Patients | SAM Manikin |
|-----------|---------------|-------------|
| V_comp (passive) | 24 ± 11 mL | 22 ± 4 mL |
| V_decomp (passive) | 30 ± 10 mL | 22 ± 11 mL |
| Paw_mean | 7.6 ± 0.3 cmH₂O | 5.8 ± 0.1 cmH₂O |
| Vti (active) | 232 ± 26 mL | 173 ± 34 mL |
| EtCO2 max | 39 ± 3 mmHg | 40 ± 0 mmHg |

### Test Conditions
- Mechanical compressions: 100/min, 3 cm depth (Life Stat)
- Ventilator: Monnal T60, CPV mode
- Invasive configuration (ETT)

---

## Clinical Reference Values Cited

### Adult Respiratory Mechanics During CPR

| Parameter | Value | Source |
|-----------|-------|--------|
| Compliance | **37.3 ± 10.9 mL/cmH₂O** | Charbonney 2018 |
| Compliance | **40 ± 11 mL/cmH₂O** | Cordioli 2016 |
| Resistance | **20.2 ± 5.3 cmH₂O·s/L** | Charbonney 2018 |

### Passive Ventilation During Compression-Only CPR

| Study | Median Tidal Volume |
|-------|---------------------|
| McDannold 2018 | 7.5 mL |
| Deakin 2007 | 41.5 mL |
| Vanwulpen 2021 | 20 mL |
| Azcarate 2023 | 25.6 mL |

---

## Device Comparison Results

### B-card vs ITD on SAM Manikin

| Parameter | CC Only | B-card | ITD |
|-----------|---------|--------|-----|
| V_comp (mL) | 27 ± 1 | **47 ± 8** | 3 ± 1 |
| V_decomp (mL) | 27 ± 1 | **44 ± 9** | 4 ± 0 |
| P_intra mean (cmH₂O) | 0.0 | **6.3 ± 0.1** | -1.6 ± 0.0 |
| P_intra max (cmH₂O) | 8.8 ± 0.2 | 18.9 ± 1.1 | 5.7 ± 0.1 |
| P_intra min (cmH₂O) | -4.5 ± 0.1 | -0.3 ± 0.2 | **-4.8 ± 0.1** |

**Key finding:** B-card increases passive ventilation; ITD dramatically reduces it (by design, to increase venous return).

---

## Relevance to MST Paper

### Adult Ventilation Reference Values
Provides adult compliance/resistance values for comparison with infant data:

| Population | Compliance | Resistance |
|------------|------------|------------|
| Adult (Charbonney/Cordioli) | 37-40 mL/cmH₂O | 20 cmH₂O·s/L |
| Infant 1-24 wks (Huang 2016) | 78 mL/kPa (~8 mL/cmH₂O) | 6.4 kPa/L/s (~65 cmH₂O·s/L) |
| Infant 73-96 wks (Huang 2016) | 171 mL/kPa (~17 mL/cmH₂O) | 3.7 kPa/L/s (~38 cmH₂O·s/L) |

Note: Infant compliance is LOWER, resistance is HIGHER than adults (as expected).

### Bench Testing Methodology
- Validates use of physiological manikin for ventilation device testing
- Shows importance of FRC, compliance, resistance in bench setup
- Demonstrates intrathoracic airway closure simulation

### For Your Apparatus Design
- SAM uses compliance ~25 mL/cmH₂O — similar order of magnitude to clinical values
- Resistance 5 cmH₂O·s/L — lower than clinical (20 cmH₂O·s/L)
- Your infant manikin targets: compliance ~8-17 mL/cmH₂O, resistance ~38-65 cmH₂O·s/L

---

## Key Quotes

### On need for physiological bench model:
> "There is a lack of bench systems permitting to evaluate ventilation devices in the specific context of cardiac arrest."

### On FRC importance:
> "Lung volume is highly important to assess recoil and thoracic pressure changes as well as passive ventilation during chest compressions."

### On airway closure:
> "Reproducing intrathoracic airway closure in the SAM manikin is relevant as it has been observed in a significant proportion of cardiac arrest patients... approximately 30% of out-of-hospital cardiac arrest patients."

---

## References Cited (relevant)

- Charbonney 2018: Thiel cadaver CPR model (compliance, resistance)
- Cordioli 2016: Ventilation strategies during chest compression
- Grieco 2019: Intrathoracic airway closure and CO2 signal
- Beloncle 2022: CPR-associated lung edema

---

*Retrieved: 2026-01-15*
*Source: ScienceDirect / Resuscitation Plus*
*File: /Users/jakorten/research/articles/md_out/1-s2.0-S2666520424001140-main.md*
