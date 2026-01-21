# O'Reilly et al. 2024 - Machine vs Human Chest Compression

**Full Citation:** O'Reilly M, Lee T-F, Cheung P-Y, Schmölzer GM. Comparison of hemodynamic effects of chest compression delivered via machine or human in asphyxiated piglets. *Pediatric Research*. 2024;95:156-159. doi:10.1038/s41390-023-02827-4

**PDF:** `input_JV/literature/pdfs/oreilly_2024_machine_vs_human_cc.pdf`

**Extracted:** 2026-01-21

---

## Summary

Randomized animal study comparing automated mechanical CC device vs two-thumb encircling technique in asphyxiated neonatal piglets. Machine CC produced superior hemodynamic outcomes (stroke volume, LV contractility) despite *shallower* compression depth than human CC.

**Key finding:** Force application characteristics matter more than depth alone.

---

## Study Design

| Parameter | Value |
|-----------|-------|
| Model | Neonatal piglets (mixed breed) |
| Age | 0-3 days |
| Weight | 2.12 ± 0.17 kg |
| n | 12 (6 machine, 6 human) |
| Arrest type | Asphyxia-induced asystole |
| Ventilation | CC + sustained inflation (30 cmH₂O, 30s) |
| Outcome | Non-surviving (hemodynamic comparison only) |

---

## Intervention Parameters

### Machine CC
| Parameter | Setting |
|-----------|---------|
| Target depth | 33% AP diameter |
| Actual depth | 32 ± 2% |
| Rate | 90/min |
| Acceleration | 500 cm/s² |
| Recoil speed | 50 cm/s |

### Human CC (two-thumb encircling)
| Parameter | Setting |
|-----------|---------|
| Target depth | 33% AP diameter |
| Actual depth | 38 ± 2% |
| Rate | 90/min (metronome) |
| Operator | Single experienced operator (GMS) |

---

## Results

### Baseline (no differences between groups)

| Parameter | Machine | Human | p |
|-----------|---------|-------|---|
| Arterial pH | 7.48 (0.03) | 7.47 (0.05) | 0.68 |
| Carotid blood flow (mL/min) | 81 (22) | 69 (26) | 0.41 |
| MAP (mmHg) | 67 (9) | 55 (13) | 0.09 |
| Stroke volume (mL/kg) | 1.5 (0.6) | 1.4 (0.3) | 0.72 |
| dp/dt_max (mmHg) | 2823 (590) | 2801 (550) | 0.95 |
| dp/dt_min (mmHg) | -3552 (870) | -3401 (1163) | 0.80 |

### End of Asphyxia (machine group had worse acidosis)

| Parameter | Machine | Human | p |
|-----------|---------|-------|---|
| Arterial pH | 6.61 (0.10) | 6.82 (0.07) | **0.001** |
| Base excess (mmol/L) | -27.9 (2.9) | -21.8 (2.6) | **0.003** |

### During Chest Compressions (machine superior despite worse starting point)

| Parameter | Machine | Human | p |
|-----------|---------|-------|---|
| Carotid blood flow (mL/min) | 10 (7) | 11 (6) | 0.79 |
| MAP (mmHg) | 26 (12) | 15 (10) | 0.11 |
| Diastolic BP (mmHg) | 12 (2) | 8 (4) | 0.05 |
| **Stroke volume (mL/kg)** | **1.4 (0.3)** | **0.9 (0.3)** | **0.02** |
| End diastolic volume (mL/kg) | 3.9 (1.3) | 2.6 (1.4) | 0.13 |
| **dp/dt_max (mmHg)** | **2324 (854)** | **1096 (434)** | **0.01** |
| **dp/dt_min (mmHg)** | **-5389 (2036)** | **-1002 (377)** | **<0.001** |

---

## Machine Specifications

Custom-designed mechanical CC machine with programmable parameters:

| Parameter | Range |
|-----------|-------|
| CC rate | 50-200 /min |
| AP depth | 10-70% |
| Acceleration | 100-1000 cm/s² |
| Recoil speed | 1-100 cm/s |
| Steps/revolution | 400-1200 |
| Duty cycle | Variable |

**Depth measurement:** Infrared transmitter/receiver (Gikfun), sampled at 200 Hz via Arduino.

---

## Key Quotes

### On force vs depth (Discussion, p.158)
> "These results challenge the role of CC depth in CPR and lead us to speculate that **the force used to compress the chest contributes significantly to the stroke volume and left ventricular function during CC**."

### On depth paradox (Discussion, p.158)
> "Interestingly, **despite higher CC depth during human-delivered CC, the stroke volume and the left ventricular function were significantly lower** than those of machine-delivered CC."

### On consistency (Discussion, p.158)
> "This indicates that our automated CC machine can deliver **consistent high-quality CC** that directly impacts hemodynamic parameters."

### On depth feedback gap (Discussion, p.158)
> "Currently, there are **no feedback mechanism to assure optimal CC depth** during real-life CPR and it might be possible that healthcare providers compress the chest deeper than the recommended 33%."

---

## Relevance to MST Paper

### HIGH Relevance

1. **Supports mechanical fidelity concept:** Demonstrates that *how* force is applied (acceleration, recoil, waveform) matters more than depth alone. This directly supports the argument that manikins need mechanical fidelity, not just correct static depth targets.

2. **Force profile hypothesis:** The machine delivered shallower compressions but achieved better hemodynamics. This suggests the force-time profile (acceleration, release characteristics) is biomechanically important — something current manikins don't replicate.

3. **Quotable evidence:** The "challenge the role of CC depth" quote is highly relevant for arguing that current depth-focused training may miss critical force dynamics.

### MODERATE Relevance

4. **Neonatal model:** Piglets (2 kg) are reasonable infant analogues for chest mechanics, though not identical to humans.

5. **Machine specs:** The CC machine parameters (acceleration range, depth range, rate range) could inform what a "high mechanical fidelity" manikin should be able to produce or respond to.

### Limitations for MST Paper

- Animal model (piglets), not human data
- Hemodynamic outcomes, not mechanical characterization
- No stiffness/compliance measurements of chest wall
- Single operator for human CC

---

## References of Interest

From this paper's reference list:

| Ref | Citation | Potential Use |
|-----|----------|---------------|
| 5 | Bruckner et al. 2021, ADFNE 106:553-556 | CC depth effects on hemodynamics |
| 6 | Bruckner et al. 2022, ADFNE 107:262-268 | Optimal CC depth RCT |
| 7 | Bruckner et al. 2023, ADFNE 108:200-203 | CC rate effects |
| 3 | Enriquez et al. 2018, Am J Perinat 35:796-800 | Fatigue during neonatal CC simulation |

---

## Cross-Reference

- Related extraction: `infant_compression_reference_values.md`
- Claim registry: Consider adding claim about force profile importance

---

*Extracted: 2026-01-21*
