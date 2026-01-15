# Infant/Neonatal Chest Compression Reference Values

**Extracted:** 2026-01-15
**Purpose:** Human reference model for compression fidelity - MST paper Section 2.2

---

## Source 1: Japan Laser Study 2024 (Pediatr Crit Care Med) - **CRITICAL**

**Citation:** "Chest Compression Depth Targets in Critically Ill Infants and Children Measured With a Laser Distance Meter." Pediatr Crit Care Med. 2024.

**PMID:** [38602429](https://pubmed.ncbi.nlm.nih.gov/38602429/)
**DOI:** [10.1097/PCC.0000000000003509](https://doi.org/10.1097/PCC.0000000000003509)

### Sample
- **n = 555** critically ill patients <8 years
- **Setting:** Single-center PICU, Japan (May 2019 - May 2022)
- **Method:** Laser distance meter measured anterior-posterior chest diameter (APd)
- **Target:** 1/3 of APd (per guidelines)

### Age-Stratified Compression Depth Targets

| Age | Target Depth (cm) | IQR (cm) |
|-----|-------------------|----------|
| **0 months** | **2.7** | 2.5-2.9 |
| **2 months** | **2.9** | 2.7-3.2 |
| 3-5 months | 3.2 | 3.0-3.5 |
| 6-8 months | 3.4 | 3.2-3.6 |
| 9-11 months | 3.4 | 3.2-3.6 |
| 12-17 months | 3.6 | 3.4-3.8 |
| 18-23 months | 3.6 | 3.4-4.0 |
| 24-60 months | 4.0 | 3.5-4.2 |

### Critical Finding

**Current guidelines recommend 4 cm for infants** - but actual 1/3 APd measurements show:
- **49% of infants 0-2 months would be over-compressed** using 4cm target
- **45.5% of children 12-17 months would be over-compressed**

**Implication for manikin design:** Fixed 4cm depth target may not reflect physiological variation. Age-adjustable depth feedback needed.

---

## Source 2: 2025 AHA/AAP Neonatal Resuscitation Guidelines

**Citation:** "Part 5: Neonatal Resuscitation: 2025 American Heart Association and American Academy of Pediatrics Guidelines for CPR and ECC." Circulation. 2025.

**DOI:** [10.1161/CIR.0000000000001367](https://doi.org/10.1161/CIR.0000000000001367)
**Release Date:** October 22, 2025

### Compression Depth Recommendation

| Parameter | Recommendation |
|-----------|----------------|
| **Depth** | ~1/3 of chest AP diameter |
| **Absolute (infant)** | ~4 cm (1.5 inches) |
| **Rate** | 100-120 compressions/min |

### Key Changes from Previous Guidelines

1. **Two-finger technique ELIMINATED** - ineffective for achieving proper depth
2. **Approved techniques:**
   - Two thumbs-encircling hands (preferred)
   - One-hand technique (if cannot encircle chest)
3. **Ventilation rate:** 30-60 inflations/min (expanded from 40-60)
4. **Deferred cord clamping:** ≥60 seconds (increased from ≥30 sec)

### Compression Technique

> "The current international guidelines recommend neonatal resuscitation with the two thumb encircling method over the lower third of the sternum. Proper depth is approximately one-third of the anteroposterior diameter of the chest wall."

---

## Summary Table for MST Paper

### Infant Compression Reference Model

| Parameter | Value | Age | Source |
|-----------|-------|-----|--------|
| Target depth (0 mo) | 2.7 cm (2.5-2.9) | Newborn | Japan 2024 |
| Target depth (2 mo) | 2.9 cm (2.7-3.2) | 2 months | Japan 2024 |
| Target depth (6-11 mo) | 3.4 cm (3.2-3.6) | 6-11 months | Japan 2024 |
| Target depth (12-23 mo) | 3.6 cm (3.4-4.0) | 12-23 months | Japan 2024 |
| Guideline depth (infant) | ~4 cm | <1 year | AHA 2025 |
| Compression rate | 100-120/min | All ages | AHA 2025 |

### Key Observations for Manikin Design

1. **Guideline 4cm may overcompress young infants** - Japan data shows 2.7-2.9cm for 0-2 months
2. **Age-dependent targets** - significant variation from newborn (2.7cm) to toddler (4.0cm)
3. **Two-finger technique eliminated** - manikins should train two-thumb encircling method
4. **IQR shows individual variation** - ~0.4-0.6cm spread within age groups

---

## Source 3: SURV1VE Trial 2024 (Arch Dis Child Fetal Neonatal Ed)

**Citation:** "Sustained inflation and chest compression versus 3:1 compression:ventilation ratio during CPR of asphyxiated newborns." Arch Dis Child Fetal Neonatal Ed. 2024;109:608-615.

**DOI:** [10.1136/archdischild-2023-326383](https://doi.org/10.1136/archdischild-2023-326383)
**PMC:** [PMC11228189](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228189/)

### Study Design
- **Sample:** 27 newborns (12 CC+SI, 15 standard 3:1)
- **Setting:** 4 hospitals in Canada and Austria
- **Note:** Terminated early (target was 218) due to funding/regulatory issues

### Interventions Compared

| Parameter | CC+SI | Standard 3:1 |
|-----------|-------|--------------|
| Compressions | 90/min continuous | 3:1 ratio with ventilations |
| Inflation pressure | 25-30 cmH₂O sustained | Standard PPV |
| PEEP | 5-8 cmH₂O | Standard |

### Outcomes (Not statistically significant due to small n)

| Outcome | CC+SI | 3:1 C:V | p-value |
|---------|-------|---------|---------|
| Time to ROSC | 90 (60-270) s | 615 (174-780) s | 0.0502 |
| Mortality | 2/11 (18.2%) | 8/14 (57.1%) | NS |

### Relevance to Manikin Design
- Compression rate of 90/min for CC+SI differs from standard 100-120/min
- Continuous compressions (no pause for ventilation) is alternative approach
- **Note:** Authors caution against clinical use outside research settings

---

## Source 4: Novel CC Technique 2025 (Children)

**Citation:** "Evaluating Novel Chest Compression Technique in Infant CPR: Enhancing Efficacy and Reducing Rescuer Fatigue." Children. 2025;12(3):346.

**DOI:** [10.3390/children12030346](https://doi.org/10.3390/children12030346)
**PMC:** [PMC11940949](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940949/)

### Study Design
- **Sample:** 34 medical students
- **Design:** Randomized crossover trial
- **Duration:** 2-minute compression cycles with 15-min rest

### Technique Description
Novel technique (nT): Dominant hand with index finger flexed at proximal interphalangeal joint. External (dorsal) surface of middle phalanx contacts sternum, thumb supports from opposite side.

### Compression Adequacy Comparison

| Technique | Adequate Rate | Mean Depth (mm) |
|-----------|---------------|-----------------|
| **Novel (nT)** | **92.4%** | 42.9 |
| Two-Thumb (TTHT) | 78.6% | 44.2 |
| Two-Finger (TFT) | 65.2% | 38.6 |

### Rescuer Fatigue (Lower = Better)

| Measure | nT | TTHT | TFT |
|---------|-----|------|-----|
| Fatigue (RPE) | 3.63 | 4.06 | 6.63 |
| Hand Pain (NRS) | 3.48 | 4.36 | 6.93 |

### Key Finding
Novel technique "bridges the gap, offering TTHT-like depth with TFT-like adaptability" - promising for single-rescuer scenarios.

### Relevance to Manikin Design
- Target depth ~43mm for adequate compression on manikin
- Technique comparison data useful for training feedback design
- Fatigue metrics important for extended CPR scenarios

---

## Evidence Gap Identified

**No published data on:**
- Infant manikin chest stiffness values
- Force-depth relationship in infant manikins
- Comparison of manikin compression mechanics to human infant data

**MST paper contribution:** Characterize infant manikin compression mechanics and compare to Japan 2024 reference values.

---

## Sources

- [Japan Laser Study 2024 - PubMed](https://pubmed.ncbi.nlm.nih.gov/38602429/) **[WEB VERIFIED]**
- [2025 AHA Guidelines - Circulation](https://doi.org/10.1161/CIR.0000000000001367) **[WEB VERIFIED]**
- [AHA News Release](https://newsroom.heart.org/news/updated-cpr-guidelines-released-for-pediatric-and-neonatal-emergency-care-and-resuscitation)
- [SURV1VE Trial 2024 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228189/) **[WEB VERIFIED]**
- [Novel CC Technique 2025 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11940949/) **[WEB VERIFIED]**

---

*Extracted: 2026-01-15*
*Updated: 2026-01-15 - Added SURV1VE Trial and Novel CC Technique*
*Status: [WEB VERIFIED] - PDF download recommended for Japan study*
