# Extracted Data from Proposition Repository

**Source:** `C:\local_dev\Proposition\`
**Extracted:** 2026-01-15
**Purpose:** Reuse verified literature data for MST paper human reference model

---

## Human Chest Mechanics - Adults (Compressions)

### Stiffness Data

| Property | Value | Source | Clinical Context | Claim |
|----------|-------|--------|------------------|-------|
| **Stiffness at 50mm** | 4–10 N/mm | Lim et al. 2024 | Wide variation between patients | C1 |
| **Stiffness at 50mm** | 7.7–8.1 N/mm | Neurauter et al. 2009 | 90 cardiac arrest patients | - |
| **Stiffness (initial)** | 10.5 N/mm | Ruiz de Gauna et al. 2023 | 615 OHCA patients, 1.1M compressions | - |
| **Damping at 30mm** | 0.08–0.38 N·s/mm | Lim et al. 2024 | Viscoelastic response | C2 |
| **Force for 38mm depth** | 27.5 ± 13.6 kg | Tomlinson et al. 2007 | 91 OHCA patients | - |
| **Force-depth curve** | Non-linear | Tomlinson et al. 2007 | Stiffness increases with depth | C3 |

### Dynamic Stiffness Changes (Ruiz de Gauna et al., 2023)

**Dataset:** 1,156,608 chest compressions from 615 OHCA patients

| Property | At CPR Start | After 3000 Compressions | Change |
|----------|-------------|------------------------|--------|
| Stiffness (k) | 10.5 N/mm | ~6.9 N/mm | **-34.6%** |
| Compression damping | 2.87 N·s/cm | ~1.5 N·s/cm | **-48.8%** |
| Recoil damping | 4.89 N·s/cm | ~3.1 N·s/cm | **-37.2%** |

**Key Finding:** Human chests soften ~35% during prolonged CPR. Manikins don't simulate this.

---

## Human Ventilation Mechanics - Infants

| Property | Value | Source | Age Range | Claim |
|----------|-------|--------|-----------|-------|
| **Compliance** | ~80 mL/kPa | Huang et al. 2016 | 1-24 weeks | V1 |
| **Compliance** | ~170 mL/kPa | Huang et al. 2016 | 73-96 weeks | V1 |
| **Resistance** | ~6 kPa/L/s | Huang et al. 2016 | 1-24 weeks | V2 |
| **Resistance** | ~4 kPa/L/s | Huang et al. 2016 | 73-96 weeks | V2 |

---

## Key Quotes (Verified)

### Tomlinson et al. 2007 - Manikin Problem

> "Commonly used CPR training manikins...usually have spring loaded chests with a **linear relationship between force and depth**."

> "The elastic force in manikins is **higher than in humans at the onset of compression and lower at higher depths** of compression."

### Lim et al. 2024 - Manufacturer Gap

> "Mechanical properties of commercially available CPR training manikins remain constant and **no information on these properties is provided by the manufacturers**."

---

## Evidence Gaps Confirmed

### Well-Characterized (Strong Evidence)
- [x] Adult chest stiffness (Tomlinson, Neurauter, Lim, Ruiz de Gauna)
- [x] Adult chest damping (Lim 2024)
- [x] Adult dynamic stiffness changes (Ruiz de Gauna 2023)
- [x] Infant respiratory compliance (Huang 2016)

### Poorly Characterized (Weak Evidence)
- [ ] Infant chest compression mechanics
- [ ] Adult ventilation mechanics
- [ ] Manikin vs human systematic comparison
- [ ] Unit-to-unit manikin variation

### Evidence Landscape Summary (from Proposition Chapter 8.5)

| Dimension | Adult Compressions | Infant Compressions | Adult Ventilations | Infant Ventilations |
|-----------|-------------------|--------------------|--------------------|---------------------|
| Human clinical data | **Strong** | **Weak** | **Weak** | **Very weak** |
| Manikin vs human comparison | Partial (Lim 2024) | **None** | **None** | **None** |

**MST Paper Contribution:** Systematic manikin characterization to fill "Manikin vs human comparison" gaps.

---

## Training-Performance Gap Evidence

### Lund-Kordahl et al. 2019

| Metric | Basic Training | Advanced Training | Gap |
|--------|----------------|-------------------|-----|
| Effective ventilations | 16.4% | 85.7% | **5× difference** |
| Correct compression depth | 40.6% | 82.1% | 2× difference |

**Key Finding:** Ventilations show the largest training-performance gap.

---

## BibTeX Keys (from Proposition references.bib)

```bibtex
@article{lim2024variable,
  title={Variable Stiffness and Damping Mechanism for CPR Manikin...},
  author={Lim, Hyunwoo and Shin, Dong-Ah and Sim, Jaesoon and others},
  journal={IEEE J Transl Eng Health Med},
  year={2024}
}

@article{tomlinson2007force,
  title={Compression force-depth relationship during out-of-hospital CPR},
  author={Tomlinson, AE and Nysaether, J and Kramer-Johansen, J and others},
  journal={Resuscitation},
  volume={72},
  pages={364--370},
  year={2007}
}

@article{ruizdegauna2023characterization,
  title={Characterization of mechanical properties of adult chests...},
  author={Ruiz de Gauna, Sofía and Gutiérrez, JJ and Sandoval, CL and others},
  journal={Comput Methods Programs Biomed},
  volume={242},
  pages={107847},
  year={2023}
}

@article{neurauter2009comparison,
  title={Comparison of mechanical characteristics of the human and porcine chest...},
  author={Neurauter, A and Nysaether, J and Kramer-Johansen, J and others},
  journal={Resuscitation},
  year={2009}
}

@article{huang2016reference,
  title={Reference values for resistance and compliance in healthy infants},
  author={Huang, J and others},
  journal={J Thorac Dis},
  volume={8},
  number={3},
  pages={513--519},
  year={2016}
}

@article{lundkordahl2019training,
  title={Relationship between level of CPR training, self-reported skills...},
  author={Lund-Kordahl, I and Mathiassen, M and Melau, J and others},
  journal={BMC Emerg Med},
  year={2019}
}
```

---

## Files to Obtain for Verification

### Priority 1 - Core Reference Data
- [ ] Lim et al. 2024 (IEEE JTEHM) - stiffness/damping values
- [ ] Tomlinson et al. 2007 (Resuscitation) - force-depth curves
- [ ] Ruiz de Gauna et al. 2023 (Comput Methods Programs Biomed) - dynamic changes
- [ ] Huang et al. 2016 (J Thorac Dis) - infant ventilation reference

### Priority 2 - Supporting
- [ ] Neurauter et al. 2009 - cross-species comparison
- [ ] Papastamelos et al. 1995 - developmental changes

---

*Data extracted from Proposition repository chapter_engineering_fidelity.md, records_jk/literature_search_mechanical_fidelity.md, and records_jk/key_quotes.md*
