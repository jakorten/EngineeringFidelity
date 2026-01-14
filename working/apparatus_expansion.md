# Apparatus Expansion: TIM → Engineering Fidelity

**Goal:** Expand current IEEE TIM sensor validation apparatus to enable manikin mechanical characterization for the Engineering Fidelity paper.

---

## 1. Current Capabilities vs. Requirements

### Compression Apparatus

| Capability | TIM Paper | Engineering Fidelity | Gap |
|------------|-----------|---------------------|-----|
| Displacement measurement | ✅ ToF sensor (±2mm) | ✅ Required | None |
| Automated actuation | ✅ CNC (±0.01mm) | ✅ Required | None |
| **Force measurement** | ❌ Not present | ✅ Required | **LOAD CELL NEEDED** |
| Thermal monitoring | ✅ SHT45 | ✅ Required | None |
| Data acquisition | ✅ STM32F405 | ✅ Required | None |

**Critical gap:** No load cell for force measurement. Without force, cannot calculate stiffness (k = F/x) or damping.

### Ventilation Apparatus

| Capability | TIM Paper | Engineering Fidelity | Gap |
|------------|-----------|---------------------|-----|
| Volume delivery | ✅ Syringe actuator | ✅ Required | None |
| Pressure measurement | ✅ DPS (±0.75%) | ✅ Required | None |
| Flow reference | ✅ MFM (±0.8%) | ✅ Required | None |
| **Compliance derivation** | ❌ Not calculated | ✅ Required | **SOFTWARE** |
| **Resistance derivation** | ❌ Not calculated | ✅ Required | **SOFTWARE** |

**Gap:** Software extension needed to calculate C and R from existing P/V data.

---

## 2. Compression Apparatus Expansion

### 2.1 Load Cell Integration

**Requirements:**
- Force range: 0–500 N (based on Tomlinson 2007: mean ~300 N, max ~500 N)
- Resolution: ≤1 N (for stiffness calculation at ~10 N/mm)
- Sampling rate: ≥50 Hz (synchronized with ToF)
- Interface: Compatible with STM32F405 (analog or I2C/SPI)

**Recommended Options:**

| Option | Model | Range | Resolution | Interface | Est. Cost |
|--------|-------|-------|------------|-----------|-----------|
| A | SparkFun HX711 + TAL220 | 0–50 kg (~500 N) | ~0.05 N | HX711 ADC | €20–30 |
| B | Futek LSB200 | 0–500 N | 0.1 N | Analog | €200–400 |
| C | TE FC22 | 0–445 N | 0.5 N | Analog | €50–100 |

**Recommendation:** Start with **Option A** (HX711 + TAL220 load cell) for rapid prototyping. Low cost, well-documented, Arduino-compatible. Upgrade to Option B/C if precision issues arise.

### 2.2 Mechanical Integration

**Mounting approach:**
```
                    CNC Actuator
                         │
                    ┌────┴────┐
                    │ Load    │  ← Force measurement
                    │ Cell    │
                    └────┬────┘
                         │
                    ┌────┴────┐
                    │ Piston  │  ← Compression surface
                    │ Plate   │
                    └─────────┘
                         │
                    ┌────┴────┐
                    │ Manikin │  ← ToF sensor inside
                    │ Chest   │     measures displacement
                    └─────────┘
```

**Key considerations:**
- Load cell in series between actuator and compression plate
- Rigid mounting to avoid compliance artifacts
- Calibrate with known weights before manikin testing

### 2.3 Software Updates

**New data fields (extend existing JSON structure):**
```json
{
  "timestamp": 0.025,
  "cnc_z_pos": -20.0,
  "distance_mm": 20.1,
  "force_N": 210.5,      // NEW
  "range_status": 0,
  "signal_strength": 5032
}
```

**New analysis functions:**
```python
def calculate_stiffness(force, displacement):
    """Linear regression: k = dF/dx [N/mm]"""
    return np.polyfit(displacement, force, 1)[0]

def calculate_damping(force, displacement, velocity, frequency):
    """Hysteresis loop analysis: d = W_loop / (2π f A²)"""
    loop_area = np.trapz(force, displacement)  # Signed area
    amplitude = np.max(displacement) - np.min(displacement)
    return loop_area / (2 * np.pi * frequency * amplitude**2)

def fit_gruben_model(force, displacement, velocity):
    """Fit F = k1*z + k2*z² + k3*z³ + k4*z⁴ + d0*ż + d1*z*ż"""
    # Construct feature matrix
    # Return coefficients [k1, k2, k3, k4, d0, d1]
    pass
```

### 2.4 Calibration Protocol

**Load cell calibration:**
1. Zero with no load
2. Apply known weights: 0, 100, 200, 300, 400, 500 N
3. Record raw ADC values
4. Fit linear calibration: F = a × ADC + b
5. Verify with intermediate weights
6. Document calibration coefficients and uncertainty

**Cross-validation:**
- Compare actuator force (from load cell) with expected force from manikin datasheet
- Verify stiffness calculation with known spring (if available)

---

## 3. Ventilation Apparatus Expansion

### 3.1 Compliance/Resistance Calculation

**No hardware changes needed** — derive from existing pressure and volume data.

**Compliance calculation:**
```python
def calculate_compliance(volume_ml, pressure_cmH2O):
    """
    C_rs = ΔV / ΔP [mL/cmH₂O]

    Use peak-to-baseline pressure difference
    """
    delta_V = np.max(volume_ml) - np.min(volume_ml)
    delta_P = np.max(pressure_cmH2O) - np.min(pressure_cmH2O)
    return delta_V / delta_P
```

**Resistance calculation:**
```python
def calculate_resistance(pressure_cmH2O, flow_Lps):
    """
    R_rs = ΔP / V̇_peak [cmH₂O·s/L]

    Use peak flow and corresponding pressure
    """
    # Find peak flow
    peak_flow_idx = np.argmax(np.abs(flow_Lps))
    peak_flow = flow_Lps[peak_flow_idx]

    # Pressure at peak flow (approximate)
    pressure_at_peak = pressure_cmH2O[peak_flow_idx]

    return pressure_at_peak / peak_flow
```

### 3.2 Enhanced Analysis

**New metrics to extract:**
- Peak inspiratory pressure (PIP)
- Plateau pressure (if inspiratory hold possible)
- Peak flow rate
- Time to peak flow
- Pressure-volume loop area (work of breathing)

**Visualization additions:**
- Pressure-volume loops
- Compliance vs. volume (nonlinearity assessment)
- Flow-volume loops

### 3.3 Unit Conversion

**Reference data uses different units — ensure consistency:**

| Parameter | Huang 2016 | Our measurement | Conversion |
|-----------|------------|-----------------|------------|
| Compliance | mL/kPa | mL/cmH₂O | 1 kPa = 10.2 cmH₂O |
| Resistance | kPa/L/s | cmH₂O/L/s | 1 kPa = 10.2 cmH₂O |

```python
def convert_compliance_to_kPa(C_cmH2O):
    """Convert mL/cmH₂O to mL/kPa"""
    return C_cmH2O * 10.2

def convert_resistance_to_kPa(R_cmH2O):
    """Convert cmH₂O/L/s to kPa/L/s"""
    return R_cmH2O / 10.2
```

---

## 4. Implementation Plan

### Phase 1: Load Cell Integration (Week 1)

| Day | Task |
|-----|------|
| 1 | Order HX711 + TAL220 load cell kit |
| 2–3 | Design mounting bracket (3D print or machine) |
| 4 | Wire load cell to STM32F405 |
| 5 | Write HX711 driver code |
| 6 | Calibrate with known weights |
| 7 | Verify against reference (bathroom scale as sanity check) |

**Deliverable:** Force measurement integrated into compression apparatus

### Phase 2: Software Updates (Week 1–2)

| Task | Priority |
|------|----------|
| Add force field to data acquisition | HIGH |
| Implement stiffness calculation | HIGH |
| Implement damping calculation | HIGH |
| Implement Gruben polynomial fitting | MEDIUM |
| Add C/R calculation to ventilation analysis | HIGH |
| Unit conversion functions | HIGH |
| Updated visualization (F-D curves, P-V loops) | MEDIUM |

**Deliverable:** Analysis scripts ready for mechanical characterization

### Phase 3: Validation (Week 2)

| Test | Success Criteria |
|------|-----------------|
| Load cell linearity | R² > 0.999 |
| Load cell repeatability | CV < 1% |
| Force-displacement on test spring | Stiffness within 5% of known value |
| Ventilation C/R on test lung | Values within expected range |

**Deliverable:** Validated apparatus ready for manikin testing

---

## 5. Bill of Materials

### New Components Required

| Item | Quantity | Est. Cost | Source |
|------|----------|-----------|--------|
| TAL220 load cell (50 kg) | 1 | €10 | SparkFun/AliExpress |
| HX711 ADC module | 1 | €5 | SparkFun/AliExpress |
| Mounting hardware | 1 set | €20 | Local hardware store |
| Calibration weights (if needed) | 1 set | €30 | Amazon |
| **Total** | | **~€65** | |

### Optional Upgrades

| Item | Purpose | Est. Cost |
|------|---------|-----------|
| Futek LSB200 load cell | Higher precision | €300 |
| Calibrated test spring | Stiffness validation | €50 |
| Test lung (calibrated) | Ventilation validation | €100 |

---

## 6. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Load cell noise | Medium | Medium | Averaging, filtering, shielding |
| Mechanical compliance in mounting | Medium | High | Rigid design, calibrate in-situ |
| HX711 sample rate too slow | Low | Medium | Can achieve 80 Hz; sufficient |
| Ventilation C/R calculation invalid | Low | High | Validate against test lung |

---

## 7. Quick Start Checklist

**Before ordering:**
- [ ] Confirm CNC actuator can accommodate load cell in series
- [ ] Measure available space for load cell mounting
- [ ] Verify STM32F405 has available GPIO/ADC pins

**After receiving components:**
- [ ] Assemble and calibrate load cell
- [ ] Update firmware for force data acquisition
- [ ] Update Python scripts for force analysis
- [ ] Validate on known reference (spring or weights)
- [ ] Test on one manikin before full data collection

---

## 8. Summary

**Hardware changes required:**
- Add load cell (HX711 + TAL220) to compression apparatus — ~€65, ~1 week

**Software changes required:**
- Force data acquisition and logging
- Stiffness, damping, Gruben fitting functions
- Compliance/resistance calculation for ventilation
- Unit conversions and updated visualizations

**No changes needed:**
- Ventilation hardware (DPS, MFM already sufficient)
- Displacement measurement (ToF already validated)
- Environmental monitoring (SHT45 already integrated)

**Estimated timeline:** 2 weeks from component arrival to validated apparatus

---

*Document created: January 2026*
