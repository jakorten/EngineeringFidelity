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

| Parameter | ID | Description |
|-----------|-----|-------------|
| measure | - | Gauge pressure reading (mbar) |
| delta-p | 153 | Atmospheric reference (~1013 mbar) |
| capacity | 21 | Full scale range |
| ident | 175 | Device identification (9 = DEPC) |

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

*Last updated: 2026-01-21*
