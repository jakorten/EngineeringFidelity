# Hardware Components

## Compression Actuator Extension

**File:** `Compression Actuator extension.stl`

**Purpose:** Extension piece mounted on load cell for chest compression testing

**Dimensions:**
| Parameter | Value |
|-----------|-------|
| Contact diameter | ~20 mm |
| Extension height | ~23.3 mm |
| Contact shape | Flat/disc |

**Rationale:**

The 20mm contact diameter matches the **overlapping thumbs technique** recommended in current guidelines:

> *"Use the two-thumb-hands-encircling-technique with overlapping or adjacent thumbs to deliver chest compressions."*
> — ERC Guidelines 2025, Newborn Resuscitation

| Thumb Position | Contact Width | Our Actuator |
|----------------|---------------|--------------|
| Adjacent thumbs | ~30-40 mm | - |
| **Overlapping thumbs** | **~15-20 mm** | **~20 mm ✓** |

**Guidelines references:**
- ERC 2025: Two-thumb-hands-encircling with overlapping or adjacent thumbs
- Lim JS et al.: Comparison of overlapping (OP) and adjacent thumb positions (AP)
- Schmölzer 2023: Mechanical CC device with similar contact design

**Conclusion:** The 20mm actuator is appropriate for characterizing manikin response to the **overlapping thumbs technique** per ERC 2025 guidelines.

**Mounting:**
- Attaches to DYMH-103 load cell
- Load cell mounted on CNC linear actuator (BlackBox X32)

---

## Load Cell

**Model:** DYMH-103
**Range:** 0-5 kg (0-49 N)
**Application:** Infant compression (target force ~14-30 N)

**ADC:** HX711 (Sparkfun, 24-bit)
**MCU:** STM32F405

---

## Reference: Schmölzer 2023 Setup

From O'Reilly/Schmölzer (Pediatric Research, 2024):
- Mechanical CC device with flat contact point
- Target depth: 33% AP chest diameter
- CC rate: 90/min
- Acceleration: 500 cm/s²
- Recoil speed: 50 cm/s

Our actuator design is compatible with this approach.
