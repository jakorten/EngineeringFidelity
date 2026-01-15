# Claim Registry

**Paper:** Engineering Fidelity of Infant CPR Manikin Ventilation (MST Special Issue)
**Last Updated:** 2026-01-15 (DR-001 scope decision)
**Thesis:** Data-driven reference model enables objective evaluation of infant manikin ventilation fidelity

**Scope:** Infant ventilation only (per DR-001)

---

## Coverage Summary

| Priority | Total | Verified | Needs Evidence | Coverage |
|----------|-------|----------|----------------|----------|
| P0 | 8 | 5 | 3 | 63% |
| P1 | 4 | 1 | 3 | 25% |
| P2 | 1 | 0 | 1 | 0% |
| **Total** | **13** | **6** | **7** | **46%** |

**Target:** >=85% overall, 100% P0

**Note:** Compression claims moved to out-of-scope per DR-001 (infant ventilation focus)

---

## Claim Registry (Section-Ordered)

### Section 1: Introduction

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| I1 | Engineering fidelity concept links to perspective paper | P1 | Proposition paper | [ ] |
| I2 | No systematic benchmark exists for infant manikin ventilation | P0 | Literature gap | [x] VERIFIED: Reiss 2015 calls for manikin C/R characterization but none exists |
| I3 | First data-driven reference model for infant manikin ventilation | P0 | Novelty claim | [x] VERIFIED: No infant manikin ventilation benchmark found in literature |

### Section 2: Human Reference Model -- Infant Ventilation Mechanics

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| V1 | Infant compliance ~78 mL/kPa (1-24 wks) to ~171 mL/kPa (73-96 wks) | P0 | Huang 2016 | [x] VERIFIED: Table 2, n=205, 77.95±46.16 to 170.58±50.14 mL/kPa |
| V2 | Infant resistance ~6.4 kPa/L/s (1-24 wks) to ~3.7 kPa/L/s (73-96 wks) | P0 | Huang 2016 | [x] VERIFIED: Table 2, n=205, median 6.39 to 3.74 kPa/L/s |
| V3 | Infant chest wall 3× more compliant than lungs (Ccw/CL ≈ 3:1) | P1 | Stoecklin 2024, Diedericks 2025 | [x] VERIFIED: Ccw/kg 3.0 vs CL/kg 0.95 mL/cmH₂O/kg (n=23) |

### Section 3: Uncertainty Envelope

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| U1 | Human data shows natural variability requiring range-based model | P1 | Inference | [ ] |
| U2 | Manikins within envelope = adequate engineering fidelity | P1 | Definition | [ ] |

### Section 4: Manikin Characterization Protocol

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| M1 | Protocol based on IEEE TIM methodology | P0 | [OWN WORK] | [ ] |
| M2 | Multiple infant manikin models tested | P0 | [OWN DATA] | [ ] |
| M3 | Unit-to-unit variation assessed | P1 | [OWN DATA] | [ ] |

### Section 5: Results -- Ventilation Fidelity

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| RV1 | Manikin compliance values (to be measured) | P0 | [OWN DATA] | [ ] |
| RV2 | Manikin resistance values (to be measured) | P0 | [OWN DATA] | [ ] |
| RV3 | Deviation from human reference (to be calculated) | P0 | [OWN DATA] | [ ] |

### Section 6: Engineering Fidelity Index

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| EF1 | Ventilation fidelity score formula | P1 | [OWN WORK] | [ ] |
| EF2 | Index enables procurement decisions | P2 | Inference | [ ] |

### Section 7: Discussion

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| D1 | First systematic infant manikin ventilation benchmark | P0 | Novelty claim | [x] VERIFIED: No multi-manikin infant ventilation benchmark found |
| D2 | Addresses gap identified by Reiss 2015 | P0 | Literature gap | [x] VERIFIED: Reiss 2015 explicitly calls for manikin C/R characterization |

---

## Out of Scope (per DR-001)

The following claims were verified but excluded due to infant ventilation focus. Preserved here for future reference:

### Compression Claims (Verified but Excluded)

| ID | Claim | Source | Verification |
|----|-------|--------|--------------|
| C1 | Adult chest stiffness 3-11 N/mm | Nysæther 2008 (n=59) | [x] Mean 270±150 N at 38mm → ~7 N/mm avg |
| C2 | Adult chest damping ~0.17 N·s/mm | Nysæther 2008 (n=59) | [x] 169±60 N·s/m |
| C3 | Force-displacement is non-linear | Tomlinson 2007 (n=91) | [x] Progressivity factor 1.41±0.25 |
| C4 | Stiffness decreases ~35% after 3000 compressions | Ruiz de Gauna 2023 (n=615) | [x] 34.6% (95% CI 33.0-36.1) |
| C5 | Infant chest properties uncharacterized | Babic 2017 | [x] "Little research performed..." |
| C7 | Infant compression depth age-dependent | Ikeyama 2024 (n=555) | [x] 0-2mo: 2.7cm, 49% over-compressed at 4cm |

**Reason excluded:** Only infant manikins available; no human reference for infant compression validation.

### Source Locations (for reference)

| Source | File |
|--------|------|
| Nysæther 2008 | `/research/articles/md_out/Manikins_With_Human_Like_Chest_Propertie.md` |
| Ikeyama 2024 | `/research/articles/md_out/Chest Compression Depth Targets...Japan, 2019–2022.md` |

---

## Priority Guide

### P0 (Critical) -- Must be 100% verified

These claims, if wrong, break the paper:

| ID | Risk if Wrong |
|----|---------------|
| V1-V2 | Human reference model invalid |
| I2-I3, D1-D2 | Novelty claim challenged |
| RV1-RV3 | Core results invalid |
| M1-M2 | Protocol credibility lost |

### P1 (Important) -- Target 90%

Strengthen but don't break argument:
- V3: Chest wall compliance context
- U1-U2: Envelope methodology
- M3: Variation analysis
- EF1: Fidelity formula

### P2 (Supporting) -- Target 70%

Nice to have:
- EF2: Procurement implication

---

## Source Verification Checklist

### Literature Sources (verify exact values)

| Source | Claims | What to Check | Status |
|--------|--------|---------------|--------|
| Huang 2016 | V1, V2 | Infant compliance 78-171 mL/kPa, resistance 3.7-6.4 kPa/L/s (n=205) | [x] VERIFIED |
| Stoecklin 2024 | V3 | Preterm Ccw/CL ratio ~3:1 | [x] VERIFIED |
| Reiss 2015 | I2, D2 | Call for manikin C/R characterization | [x] VERIFIED |

### Own Data (verify data files exist and analysis correct)

| Data Source | Claims | What to Check |
|-------------|--------|---------------|
| Ventilation tests | RV1, RV2, RV3 | Data files exist, analysis reproducible |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| [ ] | Not yet verified |
| [~] | In progress |
| [x] | Verified |
| [!] | Problem -- needs attention |

---

*Registry created: 2026-01-15*
*Scope change: 2026-01-15 — Infant ventilation focus (DR-001)*
*Last update: 2026-01-15 — Added compression claim details to out-of-scope section*
*Current: 6/13 claims verified (46%), 5/8 P0 verified (63%)*
*Remaining P0: M1, M2 (own work), RV1-RV3 (own data - pending experiments)*
