# Ventilation Data Acquisition Requirements

## Hardware Configuration

| Component | Specification |
|-----------|---------------|
| **Sensor** | Bronkhorst FLEXI-FLOW Compact FF-M11 |
| **Type** | Mass flow and pressure meter |
| **Flow ranges** | 0.5 / 2 / 5 / 20 ln/min (selectable) |
| **Current config** | 2 ln/min (TBC) |
| **Pressure range** | 0-17 bar(a) |

## Sensor Specifications (from datasheet)

| Parameter | Value |
|-----------|-------|
| Accuracy | ±0.5% Rd + ±0.1% FS |
| Repeatability | < ±0.2% Rd |
| Turndown ratio | up to 1:1000 |
| Response time | < 30 ms (T63) |
| Warm-up time | 30 minutes |

## Communication Interfaces

| Interface | Specification |
|-----------|---------------|
| Digital | Modbus-RTU, Modbus-ASCII, FLOW-BUS |
| Ethernet | EtherCAT, EtherNet/IP, Modbus-TCP, PROFINET, POWERLINK |
| Service | USB-C, Bluetooth |
| Connector | 9-pin D-sub (RS485) or 2x RJ45 (Ethernet) |

## Power Requirements

| Parameter | Value |
|-----------|-------|
| Supply voltage | +24 Vdc ±10% |
| Power consumption | 0.5 W typical (+0.9 W for Ethernet) |

---

## Application Context

- **Use case:** Infant manikin ventilation characterization
- **Target parameters:** Compliance (mL/kPa), Resistance (kPa/L/s)
- **Reference:** Huang 2016 infant ventilation mechanics

### Infant Ventilation Reference Values

| Parameter | Infant (1-24 wks) | Infant (73-96 wks) |
|-----------|-------------------|-------------------|
| Compliance | ~80 mL/kPa | ~170 mL/kPa |
| Resistance | ~6 kPa/L/s | ~4 kPa/L/s |

### Typical Test Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Tidal volume | 5-7 mL/kg | ~17-25 mL for 3.5 kg infant |
| Ventilation rate | 40-60/min | Neonatal range |
| Peak inspiratory pressure | 20-25 cmH2O | Initial breaths may be higher |

---

## Functional Requirements

### FR-01: Flow Measurement
- **FR-01.1:** Measure inspiratory and expiratory flow
- **FR-01.2:** Calculate tidal volume by flow integration
- **FR-01.3:** Support bidirectional flow (inspiration/expiration)

### FR-02: Pressure Measurement
- **FR-02.1:** Measure airway pressure during ventilation
- **FR-02.2:** Resolution sufficient for infant pressures (0-40 cmH2O)

### FR-03: Sampling Rate
- **FR-03.1:** Sample flow and pressure at minimum 100 Hz
- **FR-03.2:** Timestamp each sample with millisecond resolution

### FR-04: Data Output
- **FR-04.1:** Output timestamped flow and pressure values
- **FR-04.2:** Format: CSV-compatible (`timestamp_ms, flow_ln_min, pressure_mbar`)
- **FR-04.3:** Support streaming mode for real-time acquisition

### FR-05: Derived Parameters
- **FR-05.1:** Calculate tidal volume (integral of flow)
- **FR-05.2:** Calculate compliance (ΔV / ΔP)
- **FR-05.3:** Calculate resistance (ΔP / flow)

---

## Interface Requirements

### IR-01: Communication Protocol
- **IR-01.1:** Use Modbus-RTU or FLOW-BUS for data acquisition
- **IR-01.2:** Alternatively USB-C for direct connection
- **IR-01.3:** Configure via Bronkhorst FlowSuite software

### IR-02: Gas Configuration
- **IR-02.1:** Configure for Air (default) or appropriate test gas
- **IR-02.2:** Embedded gas data available for 22 gases + mixtures

---

## Implementation Notes

### FLEXI-FLOW Considerations
- 30-minute warm-up required for rated accuracy
- Sensor response < 30 ms sufficient for ventilation dynamics
- Built-in pressure correction available

### Integration Options
1. **Direct USB-C:** Simplest, use FlowSuite for configuration and logging
2. **Modbus-RTU:** Via RS485 to MCU for synchronized acquisition
3. **Ethernet:** For networked/remote data collection

---

## References

- Bronkhorst FLEXI-FLOW Compact FF-M11 datasheet (6264-ff-m11-en)
- Bronkhorst FLEXI-FLOW manual (917158)
- Huang J et al. (2016). Reference values for resistance and compliance in healthy infants

---

*Created: 2026-01-20*
