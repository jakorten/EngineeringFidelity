# Ventilation Reference Model: Literature Sources

**Purpose:** Consolidated reference data for infant ventilation fidelity model
**Last Updated:** 2026-01-30
**Model Variables:** Compliance (C) and Resistance (R)

---

## Primary Source: Huang et al. 2016

**Citation:** Huang J, Zhang H, Zhang M, Zhang X, Wang L. Reference values for resistance and compliance based on the single occlusion technique in healthy infants from Southeast China. *J Thorac Dis.* 2016;8(3):513-519. doi:10.21037/jtd.2016.02.69

**Population:**
- n = 205 healthy term infants (GA ≥37 weeks)
- Age: **Postnatal** 1–96 weeks (confirmed from Methods: "gestational age of less than 37 weeks" was exclusion criterion)
- Location: Southeast China (Children's Hospital of FuDan University)

**Method:** Single Occlusion Technique (SOT) using Jaeger MasterScreen BabyBody

### Data (Table 2)

| Postnatal Age | n | Crs (mL/kPa) | Rrs (kPa/L/s) |
|---------------|---|--------------|---------------|
| 1–24 weeks | 84 | 77.95 ± 46.16 | 6.39 (5.00–8.15)* |
| 25–48 weeks | 35 | 123.51 ± 50.64 | 5.11 (3.88–6.97)* |
| 49–72 weeks | 36 | 141.17 ± 44.75 | 4.20 (3.17–6.11)* |
| 73–96 weeks | 50 | 170.58 ± 50.14 | 3.74 (2.78–4.72)* |

*Rrs reported as median (P25–P75); Crs reported as mean ± SD

### Overall Statistics
- Median Rrs: 5.04 kPa/L/s (range 3.73–6.82)
- Mean Crs: 119.52 ± 60.47 mL/kPa

### Regression Equations (Table 4)

**Female infants:**
- Resistance: Rrs = 7.509 − 0.046 × week (R² = 0.240)
- Compliance: Crs = 57.942 + 1.345 × week (R² = 0.552)

**Male infants:**
- Resistance: Rrs = 5.87 − 5.489×10⁻⁶ × e^weight
- Compliance: Crs = −44.705 + 0.026 × cm² + 0.13 × BMI²

### Key Findings
1. Compliance **increases** with age (lung elastic fiber network development)
2. Resistance **decreases** with age (airway diameter increases)
3. Dispersion in resistance decreases with age (respiratory rhythm stabilizes)

### Relevance to Model
- **Primary reference** for term infant C and R values
- Provides age-stratified data for envelope definition
- Both C and R available (only source with both)

---

## Supporting Source: Stoecklin et al. 2024

**Citation:** Stoecklin B, Veneroni C, Choi YJ, Pillow JJ, Dellacà RL. Respiratory and chest wall mechanics in very preterm infants. *J Appl Physiol.* 2024;136(6):1499-1506. doi:10.1152/japplphysiol.00561.2023

**Population:**
- n = 23 very preterm infants
- Birth GA: 27.2 ± 2.0 weeks
- Tested at: 36.6 ± 0.6 weeks PMA (postmenstrual age)

**Method:** Hering-Breuer reflex apnea technique with esophageal pressure

### Data (median, IQR)

| Parameter | All Infants | No BPD (n=12) | BPD (n=11) |
|-----------|-------------|---------------|------------|
| Crs/kg (mL/cmH₂O/kg) | 0.69 (0.6) | Higher | Lower (P=0.013) |
| CL/kg (mL/cmH₂O/kg) | 0.95 (1.0) | Higher | Lower (P=0.019) |
| Ccw/kg (mL/cmH₂O/kg) | 3.0 (2.4) | Higher | Lower (P=0.027) |

### Key Findings
1. **Ccw is ~3× CL** in preterm infants at 36 weeks PMA
2. Ccw/CL ratio is **equal** between BPD and non-BPD infants (2.95 vs 2.93)
3. BPD reduces all compliances proportionally

### Relevance to Model
- Confirms Ccw/CL ~3:1 ratio for preterm/early term
- Provides weight-normalized compliance data
- **Does NOT provide resistance data**

---

## Supporting Source: Papastamelos et al. 1995

**Citation:** Papastamelos C, Panitch HB, England SE, Allen JL. Developmental changes in chest wall compliance in infancy and early childhood. *J Appl Physiol.* 1995;78(1):179-184. PMID: 7713809

**Population:**
- n = 40 sedated infants/children
- Age: 2 weeks to 3.5 years (postnatal)
- Mixed lung disease (but Cw unaffected by lung disease status)

**Method:** Mead-Whittenberger technique with manual ventilation

### Data

| Age Group | n | Cw/kg (mL·cmH₂O⁻¹·kg⁻¹) | Cw/CL Ratio |
|-----------|---|-------------------------|-------------|
| < 1 year | — | 2.80 ± 0.87 | 2.86 ± 1.06 |
| > 1 year | — | 2.04 ± 0.51 | 1.33 ± 0.36 |

P = 0.002 for Cw/kg; P = 0.005 for Cw/CL ratio

### Key Findings
1. Chest wall is **~3× more compliant** than lung in infancy
2. By 2nd year, chest wall and lung are **nearly equally compliant** (~1:1)
3. Linear inverse relationship: Cw/kg decreases with age (r = -0.495, slope = -0.037)

### Relevance to Model
- Defines **developmental trajectory** of Ccw/CL ratio
- Explains why age categories matter for reference model

---

## Supporting Source: Diedericks et al. 2025 (Review)

**Citation:** Diedericks C, Crossley KJ, Davies IM, Blank DA, Cramer SJE, Wallace MJ, **te Pas AB**, Kitchen MJ, Hooper SB. Role of the Chest Wall in Newborn Respiratory Function at Birth. *FASEB J.* 2025;39:e71064. doi:10.1096/fj.202502372R

**Note:** Arjen te Pas (LUMC) is co-author — direct connection to potential collaborator

**Type:** Review article synthesizing neonatal chest wall mechanics

### Key Data (from cited primary sources)

| Population | Ccw/CL Ratio | Source |
|------------|--------------|--------|
| Preterm (<28 wks GA) | ~5:1 | Gerhardt & Bancalari 1980 |
| Term | ~3:1 | Gerhardt & Bancalari 1980 |
| Adults | ~1:1 | — |

### Ccw by Gestational Age

| Population | CCW (mL/cmH₂O/kg) |
|------------|-------------------|
| Preterm | ~7.2 |
| Term | ~4.2 |

### Key Points
1. High Ccw at birth is **functionally necessary** (accommodates lung liquid clearance)
2. Ccw decreases rapidly in first 2 weeks (rib ossification)
3. Trade-off: High Ccw reduces breathing efficiency

### Relevance to Model
- Authoritative review from Hooper lab (Monash) + te Pas (LUMC)
- Contextualizes why Ccw/CL ratio matters clinically

---

## Consolidated Reference Table

### Compliance by Age/Population

| Population | Age Basis | Crs (mL/kPa) | Source |
|------------|-----------|--------------|--------|
| Term infant | 1–24 wks postnatal | 78 ± 46 | Huang 2016 |
| Term infant | 25–48 wks postnatal | 124 ± 51 | Huang 2016 |
| Term infant | 49–72 wks postnatal | 141 ± 45 | Huang 2016 |
| Term infant | 73–96 wks postnatal | 171 ± 50 | Huang 2016 |
| Preterm | 36 wks PMA | 0.69 mL/cmH₂O/kg* | Stoecklin 2024 |

*Different units — weight-normalized

### Resistance by Age/Population

| Population | Age Basis | Rrs (kPa/L/s) | Source |
|------------|-----------|---------------|--------|
| Term infant | 1–24 wks postnatal | 6.39 (5.00–8.15) | Huang 2016 |
| Term infant | 25–48 wks postnatal | 5.11 (3.88–6.97) | Huang 2016 |
| Term infant | 49–72 wks postnatal | 4.20 (3.17–6.11) | Huang 2016 |
| Term infant | 73–96 wks postnatal | 3.74 (2.78–4.72) | Huang 2016 |

### Ccw/CL Ratio Trajectory

| Age/Population | Ccw/CL Ratio | Source |
|----------------|--------------|--------|
| Preterm (<28 wks GA) | ~5:1 | Diedericks 2025 |
| Term (newborn) | ~3:1 | Diedericks 2025, Stoecklin 2024 |
| Infant < 1 year | 2.86 ± 1.06 | Papastamelos 1995 |
| Child > 1 year | 1.33 ± 0.36 | Papastamelos 1995 |
| Adult | ~1:1 | — |

---

## Gaps and Limitations

1. **Huang 2016 is term-only** — excludes preterm infants (GA <37 weeks)
2. **Stoecklin 2024 has no resistance data** — only compliance
3. **No single source covers preterm C + R** — may need to combine sources
4. **Geographic limitation** — Huang 2016 is Southeast China only
5. **Unit inconsistency** — some sources report per kg, others absolute

---

## Implications for Manikin Fidelity Model

### Age Category Matching

| Manikin Target | Reference Data |
|----------------|----------------|
| Preterm/NICU | Stoecklin 2024 (C only), Diedericks 2025 (Ccw/CL) |
| Term newborn (0–6 mo) | Huang 2016 (1–24 weeks) |
| Older infant (6–12 mo) | Huang 2016 (25–48 weeks) |
| Toddler (1–2 yr) | Huang 2016 (49–96 weeks), Papastamelos 1995 |

### Fidelity Envelope Definition

For term infant manikins, use Huang 2016:
- **Compliance envelope:** mean ± 1 SD (or use P25–P75)
- **Resistance envelope:** median with IQR (P25–P75)

Example for 1–24 week term infant:
- C: 78 ± 46 mL/kPa → envelope 32–124 mL/kPa (mean ± 1 SD)
- R: 6.39 kPa/L/s (5.00–8.15) → envelope 5.0–8.2 kPa/L/s (IQR)

---

## References

1. Huang J, et al. J Thorac Dis. 2016;8(3):513-519.
2. Stoecklin B, et al. J Appl Physiol. 2024;136(6):1499-1506.
3. Papastamelos C, et al. J Appl Physiol. 1995;78(1):179-184.
4. Diedericks C, et al. FASEB J. 2025;39:e71064.
5. Gerhardt T, Bancalari E. Acta Paediatr Scand. 1980;69:359-364.

---

*Document created: 2026-01-30*
*For: MST Paper — Mechanical Fidelity of Infant CPR Manikins*
