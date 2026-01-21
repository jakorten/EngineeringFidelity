# Load Cell Data Acquisition Requirements

## Hardware Configuration

| Component | Specification |
|-----------|---------------|
| **Load Cell** | DYMH-103 |
| **Range** | 0-5 kg (0-49 N) |
| **ADC** | HX711 (Sparkfun, 24-bit) |
| **MCU** | STM32F405 |

## Application Context

- **Use case:** Infant chest compression force measurement
- **Target force range:** 14-30 N (infant CPR)
- **Actuator:** 20mm diameter compression extension (see `hardware/`)

---

## Functional Requirements

### FR-01: Force Measurement
- **FR-01.1:** Measure compressive force with resolution ≤ 0.1 N
- **FR-01.2:** Support measurement range 0-49 N (full load cell range)
- **FR-01.3:** Handle both compression (positive) and release (negative/zero) phases

### FR-02: Sampling Rate
- **FR-02.1:** Sample force at ~80 Hz (HX711 hardware limit)
- **FR-02.2:** Timestamp each sample with millisecond resolution

### FR-03: Data Output
- **FR-03.1:** Output timestamped force values via serial (USB or UART)
- **FR-03.2:** Format: CSV-compatible (`timestamp_ms, force_N`)
- **FR-03.3:** Support streaming mode for real-time acquisition

### FR-04: Calibration
- **FR-04.1:** Support zero/tare function
- **FR-04.2:** Support two-point calibration (zero + known weight)
- **FR-04.3:** Calibration stored in RAM (re-calibrate each session)

---

## Non-Functional Requirements

### NFR-01: Accuracy
- **NFR-01.1:** Force measurement accuracy ≤ ±0.5 N within operating range
- **NFR-01.2:** Repeatability ≤ ±0.2 N

### NFR-02: Latency
- **NFR-02.1:** End-to-end latency (force applied → data available) < 20 ms

### NFR-03: Drift
- **NFR-03.1:** Zero drift < 0.1 N over 10-minute measurement session
- **NFR-03.2:** Temperature compensation if drift exceeds spec

---

## Interface Requirements

### IR-01: HX711 ADC Interface
- **IR-01.1:** Configure HX711 for 80 Hz sample rate (RATE pin HIGH)
- **IR-01.2:** Use Channel A, Gain 128 (default for load cells)
- **IR-01.3:** Implement proper timing for DOUT/SCK protocol

### IR-02: Serial Output
- **IR-02.1:** Baud rate: 115200
- **IR-02.2:** Protocol: ASCII, newline-terminated
- **IR-02.3:** Commands: `TARE`, `CAL`, `START`, `STOP`, `READ`, `RAW`, `STATUS`, `HELP`

---

## Test Protocol Integration

| Parameter | Unit | Rate |
|-----------|------|------|
| Force | N | ~80 Hz (HX711 limit) |
| Timestamp | ms | Per sample |

**Test modes to support:**
1. **Quasi-static:** 2 mm/s compression rate (stiffness measurement)
2. **Dynamic:** 100/min (~1.7 Hz) compression rate (damping measurement)

---

## Implementation Notes

### HX711 Considerations
- HX711 native rate is 10 Hz or 80 Hz (set by RATE pin)
- Current implementation: 80 Hz mode, ~83 Hz polling interval
- Tare/calibration uses 10-sample averaging for noise reduction

### STM32F405 Resources
- Polling-based sampling using `millis()`
- USB CDC for serial output

---

## References

- DYMH-103 load cell datasheet
- HX711 datasheet (Avia Semiconductor)
- Sparkfun HX711 breakout documentation
- STM32F405 reference manual

---

*Created: 2026-01-19*
