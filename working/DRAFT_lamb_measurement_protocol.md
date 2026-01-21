# DRAFT: Lamb Chest Compression Measurement Protocol

**Status:** DRAFT - for discussion only
**Purpose:** Characterize infant-surrogate chest mechanical properties
**Collaborator:** Arjen ten Pas (LUMC)
**Created:** 2026-01-18

---

## Objective

Measure force-displacement characteristics of lamb chest to establish reference data for infant CPR manikin fidelity assessment.

**Target parameters:**
- Stiffness k (N/mm)
- Damping coefficient c (N·s/mm)
- Non-linearity
- Hysteresis

---

## Background: Animal Models

| Model | Primary use | Chest mechanics |
|-------|-------------|-----------------|
| **Piglet** | CPR/compression studies | Similar to infant |
| **Lamb** | Ventilation/fetal transition | Different geometry |

**Why lamb (not piglet)?**
- LUMC (Arjen ten Pas) has lamb infrastructure for neonatal resuscitation research
- Lambs used for fetal-to-neonatal transition studies
- ~3.5 kg weight matches term infant
- Opportunity for collaboration

**Caveat:** Piglet chest mechanics may be more directly comparable to human infant. Lamb chest geometry differs. Results should be interpreted with this in mind.

**Question for Arjen:** Are compression forces typically measured on lambs at LUMC, or only ventilation parameters?

---

## Animal Specifications

| Parameter | Target | Rationale |
|-----------|--------|-----------|
| Species | Lamb | Similar mass to term infant |
| Weight | 3-4 kg | Matches infant manikin target |
| Age | Newborn/perinatal | Chest compliance comparable |

---

## Equipment

### Available (home lab → transport to LUMC via trailer)
- CNC linear actuator (BlackBox X32)
- Load cell DYMH-103 (0-49 N)
- Displacement sensor VL53L4CD
- STM32F405 data acquisition

### To prepare
- ~~Compression plunger (~30 mm diameter, flat or slightly curved)~~ **AVAILABLE:** `Compression Actuator extension.stl` (20mm diameter, see `hardware/`)
- Positioning support/jig
- Calipers for chest measurement
- Power supply / extension cables for LUMC setup

**Actuator note:** 20mm diameter matches two-thumb contact area and Schmölzer 2023 mechanical CC design.

### Backup: Portable IMU setup (if CNC impractical)
- Bosch BHI360 IMU (6-axis + sensor fusion)
- Requires pre-validation against CNC reference
- Only if space/power constraints at LUMC

---

## Measurements to Record

### Per animal:
| Parameter | Unit | Method |
|-----------|------|--------|
| Weight | kg | Scale |
| Chest AP diameter | mm | Calipers |
| Age | days | Record |
| Post-mortem interval | hours | Record |
| Temperature | °C | Thermometer |

### Per compression test:
| Parameter | Unit | Rate |
|-----------|------|------|
| Force | N | 100 Hz |
| Displacement | mm | 100 Hz |
| Timestamp | ms | Synchronized |

---

## Test Protocol (Draft)

### Preparation
1. Position lamb supine
2. Measure chest AP diameter
3. Calculate target depth: 1/3 × AP diameter
4. Zero sensors

### Test 1: Quasi-static (stiffness)
- Compression rate: 2 mm/s
- Depth: 0 → target → 0
- Cycles: 3
- Rest: 30 s between cycles

### Test 2: Dynamic (damping)
- Compression rate: 100/min (~1.7 Hz)
- Depth: target depth
- Cycles: 10
- Rest: 60 s after

### Test 3: Repeat quasi-static
- Same as Test 1
- Check for tissue fatigue/change

---

## Data Analysis

### Stiffness (from quasi-static):
```
k = ΔF / Δd  (linear fit)
```
Or polynomial fit for non-linearity:
```
F = k₁d + k₂d² + k₃d³
```

### Damping (from dynamic):
```
c = loop_width / (2 × v_max)
```

### Hysteresis:
```
H = (loop_area / loading_area) × 100%
```

---

## Sample Size

| Phase | n | Purpose |
|-------|---|---------|
| Pilot | 2-3 | Verify setup, refine protocol |
| Main study | 8-10 | Reference data with CI |

---

## Considerations

### Ethical
- [ ] Animal research approval required
- [ ] LUMC protocol coverage?

### Practical
- [ ] Fresh tissue timing (<2h post-mortem ideal)
- [ ] Temperature control
- [ ] Equipment transport to LUMC?

### Scientific
- [ ] Live vs post-mortem differences (Arbogast: ~2× stiffer post-mortem)
- [ ] Lamb vs human infant validity

---

## Open Questions

1. Does LUMC have existing ethical approval for lamb mechanical testing?
2. Can we use animals from other studies (opportunistic)?
3. ~~Equipment at LUMC or transport from HAN?~~ **RESOLVED: Transport CNC to LUMC via trailer**
4. Fresh post-mortem or anesthetized?
5. Sample size for statistical validity?
6. Space/power requirements at LUMC for CNC setup?

---

## Next Steps (if proceeding)

1. [ ] Discuss feasibility with Arjen ten Pas
2. [ ] Clarify ethical/practical constraints
3. [ ] Pilot test (n=2-3)
4. [ ] Refine protocol based on pilot
5. [ ] Main study (n=8-10)

---

*DRAFT - not for execution without further review*
