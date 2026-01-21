# EL-PRESS Pressure Sensor

Bronkhorst EL-PRESS P-502C for airway pressure measurement during manikin ventilation characterization.

## Hardware

| Parameter | Value |
|-----------|-------|
| Model | EL-PRESS P-502C |
| Type | Gauge pressure (relative to atmosphere) |
| Range | 0-100 mbar |
| Interface | RS232 via USB adapter |
| Protocol | PROPAR |

## Connection

| Parameter | Value |
|-----------|-------|
| Port | `/dev/cu.usbserial-AQ00Z5CQ` |
| Node address | 4 |
| Baud rate | 38400 |

## Usage

### Setup
```bash
cd software/elpress
source venv/bin/activate
```

### Read pressure
```bash
# Single reading
python read_elpress.py

# Continuous reading (10 seconds, 100ms interval)
python read_elpress.py -c 10 -i 0.1

# Scan for sensor on different nodes
python read_elpress.py --scan
```

### Tare (zero) the sensor
```bash
# Show current offset
python tare_elpress.py

# Set new tare offset
python tare_elpress.py --tare
```

### Diagnostics
```bash
python diagnose_elpress.py
```

## Calibration Notes

- **Warm-up time:** 30 minutes recommended before measurements
- **Baseline offset:** ~45 mbar observed at rest (use tare to zero)
- **Drift:** ~2 mbar/min during warm-up, stabilizes after warm-up
- **Tare procedure:** Run `tare_elpress.py --tare` after warm-up

## PROPAR Parameters

### Measurement Values

| Param | Name | Example | Description |
|-------|------|---------|-------------|
| 8 | fmeasure | 23 | Gauge pressure (mbar) - same as `measure` |
| 153 | delta-p | 1.013 | Atmospheric reference (bar) |
| 250 | (absolute?) | 1006.6 | Possibly absolute pressure (mbar) |

### Device Information

| Param | Name | Example | Description |
|-------|------|---------|-------------|
| 1 | serial | SNM15211829B | Serial number string |
| 90 | type | DEPC | Device type (Digital Electronic Pressure Controller) |
| 91 | model | P-502C-350R-RGD-33-V | Full model number |
| 92 | serial_alt | M15211829B | Alternative serial |
| 94 | cal_date | 25,11,2015 | Calibration date |
| 105 | firmware | V1.21d | Firmware version |
| 129 | unit | mbar(g) | Measurement unit |
| 175 | ident | 9 | Device identification (9 = DEPC) |

### Configuration

| Param | Name | Example | Description |
|-------|------|---------|-------------|
| 21 | capacity | 200.0 | Capacity setting |
| 25 | fluid | AiR | Configured fluid/gas |
| 139 | full_scale | 100.0 | Full scale range (mbar) |
| 167 | capacity_100 | 100.0 | 100% capacity value |
| 246 | baro_press | 1.013 | Barometer pressure (bar) |

### Setpoint (Controller Mode)

| Param | Name | Example | Description |
|-------|------|---------|-------------|
| 9 | fsetpoint | 0 | Flow/pressure setpoint |
| setpoint | - | 0 | Setpoint attribute |

## Files

| File | Purpose |
|------|---------|
| `read_elpress.py` | Main reader script |
| `tare_elpress.py` | Tare/zero utility |
| `diagnose_elpress.py` | Diagnostic script |
| `elpress_offset.json` | Stored tare offset (auto-generated) |
| `venv/` | Python virtual environment |
| `propar/` | Local propar library |
| `testing_debug/` | Previous debug scripts (FLEXI-FLOW) |

## Dependencies

```bash
pip install propar pyserial
```

Or use the included venv:
```bash
source venv/bin/activate
```

---

## Sensor Specifications (from device)

| Parameter | Value |
|-----------|-------|
| Model | P-502C-350R-RGD-33-V |
| Type | DEPC (Digital Electronic Pressure Controller) |
| Range | 0-100 mbar (gauge) |
| Unit | mbar(g) |
| Fluid | Air |
| Firmware | V1.21d |
| Factory calibration | 25 Nov 2015 |

## Troubleshooting

### Serial errors (Bad file descriptor)
- USB cable may have disconnected
- Another process may be using the port
- Solution: Reconnect USB, restart script

### No response on any node
- Check power (24V required)
- Check RS232 adapter connection
- Try different baud rates (default 38400)

### Readings drift
- Allow 30 min warm-up
- Re-tare after warm-up
- Check for temperature changes

---

*Last updated: 2026-01-21*
