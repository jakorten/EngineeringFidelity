# Ventilation Measurement Apparatus

## Airway Tubing Sizes

| ID | Typical use |
|----|-------------|
| 4 mm | Small infant, neonatal |
| 6 mm | Infant |
| 8 mm | Pediatric |
| 22 mm | Adult (ISO standard) |

**Physiological reference:**
- Term neonate trachea: ~4-5 mm diameter
- Neonatal ETT (endotracheal tube): 3.0-3.5 mm ID

### Trade-off: 4 mm vs 6 mm

| Tubing | Pros | Cons |
|--------|------|------|
| 4 mm ID | Realistic airway resistance | Fewer T-connector options, may need adapters for EL-PRESS |
| 6 mm ID | Easy to source T-connectors, matches EL-PRESS fittings | Slightly lower resistance than real infant airway |

**Recommendation:** Keep 4 mm for the manikin connection (physiological), use a short 4→6 mm adapter where you connect the sensors. This way:
- Manikin side: realistic resistance
- Sensor side: standard 6 mm fittings

---

## Sensors

| Sensor | Type | Range | Purpose |
|--------|------|-------|---------|
| Bronkhorst EL-PRESS P-502C | Gauge pressure | 0-100 mbar (0-10 kPa) | Primary Paw measurement |
| MPXV5010GP ×2 | Gauge pressure | 0-10 kPa | Backup / blocked airway detection |
| SDP810 | Differential pressure | ±500 Pa | Flow measurement |

**Sensor port sizes:**
- EL-PRESS P-502C: 11 mm OD barbed fitting (needs ~10-11 mm ID tubing)
- MPXV5010GP: ~3 mm barbed port (2.8 mm nominal)

---

## T-Connectors Required

For tapping pressure from the airway circuit.

**Current tubing:** 4 mm ID (6 mm OD)

**Options:**
- Barbed T-connector, 4 mm ID
- 4→6 mm stepped adapter (to match EL-PRESS fittings)
- Luer-lock T-connectors (flexible, medical-grade)

**Suppliers:** Festo, SMC, RS Components, medical suppliers

---

## Suggested Measurement Setup

```
Manikin airway (4 mm ID)
      │
      ▼
   ┌──┴──┐
   │  T  │──── short tubing ──── EL-PRESS P-502C (primary Paw)
   └──┬──┘
      │
      ▼
   ┌──┴──┐
   │  T  │──── short tubing ──── MPXV5010GP (backup)
   └──┬──┘
      │
      ▼
  SDP810 (flow)
      │
      ▼
   Test lung / open
```

**Recommendation:** Keep 4 mm tubing at manikin connection (physiologically appropriate), use 4→6 mm adapter at sensor connections for easier fitting.

---

## To Order / Source

| Item | Qty | Purpose |
|------|-----|---------|
| T-connector, 4 mm barbed | 2 | Tap pressure from airway |
| Reducer 4→10 mm (stepped adapter) | 1 | Adapt to EL-PRESS |
| Silicone tubing, 10-11 mm ID | ~10 cm | EL-PRESS connection |
| Reducer 4→3 mm | 1-2 | Adapt to MPXV5010GP |
| Silicone tubing, 4 mm ID | ~50 cm | Main airway |
| Silicone tubing, 3 mm ID | ~20 cm | MPXV5010GP connection |

**Alternative:** Luer-lock system with adapters for more flexibility.

---

*Last updated: 2026-01-21*
