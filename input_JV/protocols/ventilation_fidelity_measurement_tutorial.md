# Ventilation Fidelity Measurement Tutorial

**Purpose:** Step-by-step guide to measuring infant manikin ventilation mechanics and comparing against human reference data.

**Target Audience:** Researchers implementing the mechanical fidelity assessment protocol

**Last Updated:** 2026-01-30

---

## Table of Contents

1. [Overview](#1-overview)
2. [Equipment Required](#2-equipment-required)
3. [The Model](#3-the-model)
4. [Hardware Setup](#4-hardware-setup)
5. [Calibration](#5-calibration)
6. [Measurement Protocol](#6-measurement-protocol)
7. [Data Analysis](#7-data-analysis)
8. [Fidelity Scoring](#8-fidelity-scoring)
9. [Troubleshooting](#9-troubleshooting)
10. [Reference Data](#10-reference-data)

---

## 1. Overview

### What We're Measuring

We characterize infant CPR manikin "lungs" using two key parameters:

| Parameter | Symbol | Unit | What It Tells Us |
|-----------|--------|------|------------------|
| **Compliance** | C | mL/kPa | How easily the lung expands (volume per unit pressure) |
| **Resistance** | R | kPa/L/s | How hard it is to push air through the airway |

### The Goal

Compare manikin C and R values against human infant reference data (Huang 2016) to quantify **mechanical fidelity** — how closely the manikin mimics real infant respiratory mechanics.

### Why It Matters

- A manikin with wrong C/R teaches incorrect ventilation technique
- Too compliant → trainee uses too little pressure → underventilation in real infant
- Too stiff → trainee uses too much pressure → barotrauma risk in real infant

---

## 2. Equipment Required

### Primary Sensors

| Component | Model | Range | Purpose |
|-----------|-------|-------|---------|
| Pressure sensor | Bronkhorst EL-PRESS P-502C | 0–100 mbar | Airway pressure (Paw) |
| Flow sensor | Bronkhorst MFM | 0–2 ln/min* | Airflow (Q) |
| Backup pressure | MPXV5010GP | 0–10 kPa | Redundancy / blocked airway |

*Verify flow range is appropriate for infant tidal volumes (~20-50 mL at ~10-30 breaths/min)

### Pneumatic Supply (for Continuous Flow Method)

| Component | Model | Range | Purpose |
|-----------|-------|-------|---------|
| Supply regulator | Festo MS2-LFR-QS6-D6 | 0.5–7 bar | Reduce lab pressure, filter |
| Pressure controller | Bronkhorst EL-PRESS | 0–100 mbar | Precision mbar control |

**See Section 4.3 for complete pneumatic chain setup.**

### Manual Ventilation Source (Alternative)

| Option | Pros | Cons |
|--------|------|------|
| Calibrated syringe (50 mL) | Precise volume control | Manual, slower |
| Neopuff / T-piece | Realistic, pressure-controlled | Less volume precision |
| Self-inflating bag | Realistic training device | Variable delivery |

**Recommended:** Use continuous flow method (Section 6.5) for characterization, then validate with clinical devices.

### Data Acquisition

| Component | Purpose |
|-----------|---------|
| Microcontroller (STM32/Arduino) | Sensor interface |
| ADC (if needed) | Analog sensor digitization |
| PC with Python/MATLAB | Data logging and analysis |

### Consumables & Accessories

- Tubing (medical grade, ID ~4-6 mm for infant)
- Connectors / adapters for manikin airway
- Leak-test equipment (soap solution or electronic leak detector)
- Reference masses for pressure calibration (water column)

---

## 3. The Model

### Single-Compartment RC Model

The respiratory system behaves like an electrical RC circuit:

```
                    R (resistance)
    ┌───────────────/\/\/\───────────────┐
    │                                     │
    │                                     │
  P_aw                                   ─┴─
(pressure)                               ─┬─  C (compliance)
    │                                     │
    │                                     │
    └─────────────────────────────────────┘
                                         GND
```

### Equation of Motion

```
P_airway = P_elastic + P_resistive

P_airway = V/C + R·Q

Where:
  P_airway = pressure at airway opening (kPa)
  V        = volume in lung above FRC (mL)
  C        = compliance (mL/kPa)
  Q        = flow rate (L/s)
  R        = resistance (kPa/L/s)
```

### What This Means Practically

- **At zero flow (Q = 0):** P = V/C → measure compliance
- **During flow:** P increases by R·Q → measure resistance
- **Compliance** = how much the lung stretches per unit pressure
- **Resistance** = pressure needed to drive airflow

---

## 4. Hardware Setup

### 4.1 System Diagram

```
┌─────────────────┐
│  Ventilation    │
│  Source         │
│  (syringe/bag)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Flow Sensor    │──────► Flow signal (Q)
│  (MFM)          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Pressure Tap   │──────► Pressure signal (P)
│  (T-connector)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Manikin        │
│  Airway/Lung    │
└─────────────────┘
```

### 4.2 Connection Details

1. **Flow sensor placement:** Proximal to manikin (measure all delivered flow)
2. **Pressure tap:** Between flow sensor and manikin airway
3. **Leak check:** Critical — any leak invalidates compliance measurement

### 4.3 Pneumatic Supply Chain (for Continuous Flow Method)

For the continuous flow measurement method (Section 6.5), controlled low-pressure air delivery is required.

**System diagram:**

```
┌──────────────────┐
│  Compressed Air  │  (Lab supply, ~4-8 bar)
│  Source          │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  MS2-LFR-QS6-D6  │  Festo precision regulator
│  (0.5–7 bar out) │  → reduces to 1-2 bar working pressure
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  EL-PRESS P-502C │  Bronkhorst electronic pressure controller
│  (0–100 mbar)    │  → fine control for 10-50 mbar output
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  MFM             │  Bronkhorst mass flow meter
│  (0–2 ln/min)    │  → measures actual delivered flow
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Manikin Airway  │
└──────────────────┘
```

**Component specifications:**

| Component | Model | Range | Purpose |
|-----------|-------|-------|---------|
| Supply regulator | Festo MS2-LFR-QS6-D6 | 0.5–7 bar out | Clean, stable supply pressure |
| Pressure controller | Bronkhorst EL-PRESS P-502C | 0–100 mbar | Precision mbar-level control |
| Flow meter | Bronkhorst MFM | 0–2 ln/min | SI-traceable flow measurement |

**Pressure cascade:**
- Lab supply: ~5 bar
- After MS2-LFR: ~1 bar (reduces supply, filters)
- After EL-PRESS: 10–50 mbar (final output to manikin)

**Why two stages?**

The EL-PRESS requires stable upstream pressure to regulate accurately in the mbar range. The Festo MS2-LFR provides this by:
1. Reducing high supply pressure to manageable level
2. Filtering particulates (protects downstream components)
3. Damping pressure fluctuations from supply

**Important:** The MS2-LFR minimum output (500 mbar) is too high for direct manikin use — you need the EL-PRESS for final mbar-level control.

### 4.4 Sensor Wiring

**EL-PRESS P-502C:**
- Interface: RS232 or Modbus (check your unit)
- Power: Per Bronkhorst specs
- Output: Digital pressure reading in mbar
- Setpoint: Digital or analog (for continuous flow control)

**MFM (Mass Flow Meter):**
- Interface: RS232 or analog 0-5V
- Calibration: Factory calibrated, SI-traceable
- Output: Flow in ln/min (normalize to L/s)

### 4.5 Manikin Interface

Different manikins have different airway configurations:

| Manikin Type | Airway Interface | Notes |
|--------------|------------------|-------|
| Laerdal Baby Anne | 15 mm connector | Standard pediatric |
| Simulaids infant | Proprietary | May need adapter |
| Prestan infant | 15 mm connector | Check for leak points |

**Tip:** Create a universal adapter plate with sealed connections.

---

## 5. Calibration

### 5.1 Pressure Sensor Calibration

**Zero calibration:**
1. Open sensor to atmosphere
2. Record reading → should be 0 mbar (±0.1 mbar)
3. If offset, record and subtract in software

**Span calibration:**
1. Connect to water column manometer
2. Apply known pressures: 10, 20, 50, 100 cmH₂O
3. Record sensor output at each point
4. Fit linear calibration: P_true = a × P_sensor + b

**Conversion:** 1 cmH₂O = 0.981 mbar ≈ 0.098 kPa

### 5.2 Flow Sensor Calibration

**Volume verification:**
1. Connect calibrated syringe (50 mL) to flow sensor
2. Deliver full syringe volume at steady rate (~1-2 seconds)
3. Integrate flow signal: V = ∫Q dt
4. Compare integrated volume to syringe volume
5. Should match within ±5%

**If using SDP810 (differential pressure):**
- Requires orifice plate or venturi calibration
- Flow = k × √(ΔP) — calibrate k with known flows

### 5.3 System Leak Test

**Critical step — do before every measurement session:**

1. Seal manikin airway (plug or clamp)
2. Deliver 30 mL with syringe
3. Hold for 10 seconds
4. Monitor pressure — should remain stable (±5% drop max)
5. If pressure drops significantly → find and fix leak

---

## 6. Measurement Protocol

### 6.1 Preparation

- [ ] Calibrate all sensors (Section 5)
- [ ] Leak test system
- [ ] Record ambient conditions (temperature, humidity)
- [ ] Document manikin model, serial number, condition

### 6.2 Compliance Measurement (Quasi-Static Method)

This method minimizes resistance effects by using slow inflation.

**Procedure:**

1. **Connect** manikin to measurement system
2. **Zero** pressure sensor with airway open
3. **Deliver volume in steps:**

   | Step | Volume (mL) | Hold time (s) |
   |------|-------------|---------------|
   | 1 | 10 | 2 |
   | 2 | 20 | 2 |
   | 3 | 30 | 2 |
   | 4 | 40 | 2 |
   | 5 | 50 | 2 |

4. **Record** plateau pressure at each step (after ~1s stabilization)
5. **Release** volume, let pressure return to zero
6. **Repeat** 3 times for reproducibility

**Data recording format:**

```csv
trial,volume_mL,pressure_plateau_kPa,time_s
1,10,0.12,2.1
1,20,0.25,2.0
1,30,0.38,2.1
...
```

### 6.3 Resistance Measurement (Dynamic Method)

**Procedure:**

1. **Deliver** 30 mL at controlled rate (~0.5 seconds, Q ≈ 60 mL/s = 3.6 L/min)
2. **Record** continuously: P(t), Q(t)
3. **Identify:**
   - P_peak = maximum pressure during inflation
   - P_plateau = pressure 0.5s after flow stops
   - Q_mean = average flow during inflation

4. **Calculate:**
   ```
   R = (P_peak - P_plateau) / Q_mean
   ```

5. **Repeat** 5 times, report mean ± SD

### 6.4 Alternative: Single-Breath Analysis

If equipment supports high-speed acquisition (>100 Hz):

1. Deliver single tidal breath (~30 mL over 0.5s)
2. Record P, Q continuously
3. Compute V by integrating Q
4. Fit equation: P = V/C + R·Q using least squares
5. Extract C and R from fit parameters

**Python pseudocode:**
```python
from scipy.optimize import curve_fit

def model(X, C, R):
    V, Q = X
    return V/C + R*Q

# X = [volume_array, flow_array]
# P = pressure_array
popt, pcov = curve_fit(model, [V, Q], P)
C_fit, R_fit = popt
```

### 6.5 Continuous Flow Method (Recommended)

This method extracts both C and R from a single measurement by applying constant flow.

**Principle:**

With constant flow Q, the equation of motion becomes:
```
P(t) = V(t)/C + R·Q = (Q·t)/C + R·Q
```

This is a linear equation: **P(t) = (Q/C)·t + R·Q**

- **Slope** = Q/C → C = Q/slope
- **Intercept** = R·Q → R = intercept/Q

**Procedure:**

1. **Set constant flow** using EL-PRESS controlled regulator (see Section 4.3)
2. **Recommended flow rate:** 100–200 mL/min (1.7–3.3 mL/s)
   - Slow enough to avoid excessive R·Q pressure contribution
   - Fast enough to reach target volume in reasonable time
3. **Start flow** and record P(t) at ≥10 Hz
4. **Continue** until target volume reached (e.g., 30–50 mL)
5. **Stop flow** and record plateau pressure for verification
6. **Plot** P vs t during inflation phase
7. **Fit linear regression:** P = m·t + b

**Analysis:**

```
Given: Q = 0.003 L/s (180 mL/min)
       m = 0.04 kPa/s (slope from regression)
       b = 0.02 kPa (intercept)

Calculate:
  C = Q / m = 0.003 / 0.04 = 0.075 L/kPa = 75 mL/kPa
  R = b / Q = 0.02 / 0.003 = 6.7 kPa/L/s
```

**Python pseudocode:**
```python
import numpy as np
from scipy.stats import linregress

# Data from inflation phase
time = np.array([...])      # seconds
pressure = np.array([...])  # kPa
Q = 0.003                   # L/s (constant flow)

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(time, pressure)

# Extract parameters
C = Q / slope * 1000  # mL/kPa
R = intercept / Q     # kPa/L/s

print(f"Compliance: {C:.1f} mL/kPa")
print(f"Resistance: {R:.2f} kPa/L/s")
print(f"R² = {r_value**2:.3f}")
```

**Advantages:**
- Both C and R from single measurement
- Less sensitive to operator technique
- Continuous recording captures nonlinearities if present
- Automation-friendly (reproducible flow)

**Pressure range expected:**

For infant manikins with typical C = 50–150 mL/kPa and R = 4–8 kPa/L/s:
- At Q = 3 mL/s, R·Q = 4–8 × 0.003 = 0.012–0.024 kPa (1.2–2.4 mbar)
- At V = 50 mL, V/C = 50/50 to 50/150 = 0.33–1.0 kPa (33–100 mbar)
- **Total: ~10–50 mbar typical, max ~100 mbar**

---

## 7. Data Analysis

### 7.1 Compliance Calculation

**From quasi-static data:**

1. Plot Volume (y-axis) vs Pressure (x-axis)
2. Fit linear regression: V = C × P + b
3. **Compliance C = slope** (mL/kPa)
4. Intercept b should be ≈0 (if not, check for trapped gas)

**Example calculation:**

| V (mL) | P (kPa) |
|--------|---------|
| 10 | 0.12 |
| 20 | 0.24 |
| 30 | 0.37 |
| 40 | 0.49 |
| 50 | 0.61 |

Linear fit: V = 81.3 × P + 0.2

**C = 81.3 mL/kPa**

### 7.2 Resistance Calculation

**From dynamic data:**

```
R = (P_peak - P_plateau) / Q

Example:
  P_peak = 0.85 kPa
  P_plateau = 0.37 kPa
  Q = 0.060 L/s (60 mL/s)

  R = (0.85 - 0.37) / 0.060 = 8.0 kPa/L/s
```

### 7.3 Uncertainty Estimation

**For compliance:**
- Repeat measurement 3× → calculate SD
- Report: C = mean ± SD (mL/kPa)

**For resistance:**
- Repeat measurement 5× → calculate SD
- Report: R = mean ± SD (kPa/L/s)

**Combined uncertainty:**
```
u_C = √(u_V² + u_P²) × C
u_R = √(u_P² + u_Q²) × R
```

---

## 8. Fidelity Scoring

### 8.1 Reference Envelope (Huang 2016)

Select reference based on manikin's target population:

| Target Age | C (mL/kPa) | R (kPa/L/s) |
|------------|------------|-------------|
| **Term newborn (0-6 mo)** | 78 ± 46 | 6.4 (5.0–8.2) |
| **Infant (6-12 mo)** | 124 ± 51 | 5.1 (3.9–7.0) |
| **Infant (12-18 mo)** | 141 ± 45 | 4.2 (3.2–6.1) |
| **Toddler (18-24 mo)** | 171 ± 50 | 3.7 (2.8–4.7) |

### 8.2 Fidelity Index Calculation

**Method 1: Envelope inclusion (binary)**

```
Fidelity_C = 1 if (C_ref - SD) ≤ C_manikin ≤ (C_ref + SD), else 0
Fidelity_R = 1 if R_25th ≤ R_manikin ≤ R_75th, else 0
```

**Method 2: Normalized deviation**

```
δ_C = |C_manikin - C_ref| / C_ref
δ_R = |R_manikin - R_ref| / R_ref

Fidelity = 1 - (δ_C + δ_R) / 2

Where Fidelity ∈ [0, 1], higher = better
```

**Method 3: Z-score based**

```
Z_C = (C_manikin - C_mean) / C_SD
Z_R = (R_manikin - R_median) / (R_75th - R_25th)

Fidelity_C = max(0, 1 - |Z_C|/2)
Fidelity_R = max(0, 1 - |Z_R|/2)

Combined Fidelity = (Fidelity_C + Fidelity_R) / 2
```

### 8.3 Reporting Format

```
MANIKIN FIDELITY REPORT
=======================
Model: [Manikin name]
Serial: [S/N]
Target population: Term newborn (0-6 months)
Test date: 2026-XX-XX

MEASURED VALUES
---------------
Compliance (C): 65.2 ± 3.1 mL/kPa (n=3)
Resistance (R): 7.8 ± 0.4 kPa/L/s (n=5)

REFERENCE VALUES (Huang 2016)
-----------------------------
Compliance: 78 ± 46 mL/kPa
Resistance: 6.4 (5.0-8.2) kPa/L/s

FIDELITY ASSESSMENT
-------------------
Compliance: WITHIN envelope (Z = -0.28)
Resistance: WITHIN envelope (Z = +0.52)

Combined Fidelity Index: 0.80 / 1.00

INTERPRETATION
--------------
This manikin demonstrates acceptable mechanical fidelity
for term newborn ventilation training.
```

---

## 9. Troubleshooting

### Problem: Pressure doesn't stabilize

**Possible causes:**
- Leak in system → redo leak test
- Manikin lung still expanding → wait longer
- Temperature equilibration → let system settle

### Problem: Compliance too high (lung too soft)

**Check:**
- Is the manikin lung properly installed?
- Is there a hole or tear in the lung?
- Is the chest wall properly secured?

### Problem: Compliance too low (lung too stiff)

**Check:**
- Is the airway blocked?
- Is there water/debris in the lung?
- Is the manikin designed for a different age group?

### Problem: Resistance too high

**Check:**
- Airway obstruction (tongue, foreign body)
- Kinked tubing
- Narrow airway adapter

### Problem: Variable measurements

**Check:**
- Inconsistent syringe delivery technique
- Temperature fluctuations
- Sensor drift → recalibrate

---

## 10. Reference Data

### Human Infant Reference (Huang 2016)

**Population:** Term infants (GA ≥37 weeks), n=205, Southeast China

| Age (postnatal) | n | C (mL/kPa) | R (kPa/L/s) |
|-----------------|---|------------|-------------|
| 1–24 weeks | 84 | 77.95 ± 46.16 | 6.39 (5.00–8.15) |
| 25–48 weeks | 35 | 123.51 ± 50.64 | 5.11 (3.88–6.97) |
| 49–72 weeks | 36 | 141.17 ± 44.75 | 4.20 (3.17–6.11) |
| 73–96 weeks | 50 | 170.58 ± 50.14 | 3.74 (2.78–4.72) |

**Units:**
- C = compliance in mL/kPa (Crs from single occlusion technique)
- R = resistance in kPa/L/s (Rrs, median with P25-P75)

### Unit Conversions

| From | To | Multiply by |
|------|----|-------------|
| mbar | kPa | 0.1 |
| cmH₂O | kPa | 0.0981 |
| cmH₂O | mbar | 0.981 |
| L/min | L/s | 1/60 |
| mL/cmH₂O | mL/kPa | 10.2 |

### Key Literature

1. Huang J et al. (2016) J Thorac Dis 8(3):513-519
2. Stoecklin B et al. (2024) J Appl Physiol 136(6):1499-1506
3. Papastamelos C et al. (1995) J Appl Physiol 78(1):179-184

---

## Appendix A: Quick Reference Card

```
VENTILATION FIDELITY MEASUREMENT - QUICK REFERENCE
===================================================

SETUP CHECKLIST
□ Pressure sensor zeroed
□ Flow sensor calibrated (±5% volume)
□ System leak tested (<5% pressure drop in 10s)
□ Manikin documented (model, S/N)
□ Pneumatic chain: MS2-LFR → EL-PRESS → MFM → Manikin

METHOD 1: CONTINUOUS FLOW (Recommended)
1. Set constant flow 100-200 mL/min via EL-PRESS
2. Record P(t) during inflation
3. Plot P vs t → linear fit: P = m·t + b
4. C = Q/m, R = b/Q
5. Expect P range: 10-50 mbar typical

METHOD 2: QUASI-STATIC (Manual, C only)
1. Deliver 10, 20, 30, 40, 50 mL steps
2. Hold 2s each, record P_plateau
3. Plot V vs P → slope = C
4. Repeat 3×

METHOD 3: DYNAMIC (Manual, R only)
1. Deliver 30 mL in 0.5s
2. Record P_peak and P_plateau
3. R = (P_peak - P_plateau) / Q
4. Repeat 5×

TARGET VALUES (term newborn)
C: 78 ± 46 mL/kPa
R: 6.4 (5.0-8.2) kPa/L/s

PRESSURE RANGE (infant manikins)
Typical: 10-50 mbar
Maximum: ~100 mbar
```

---

*Document created: 2026-01-30*
*Author: Claude Code + JK*
*Project: MST Paper — Mechanical Fidelity of Infant CPR Manikins*
