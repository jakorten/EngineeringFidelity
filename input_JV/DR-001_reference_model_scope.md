---
status: DECIDED
date: 2026-01-15
decision: Option C - Infant Ventilation Focus
---

# Decision: Reference Model Scope

## Context

The paper needs to define what human reference data to include and what manikins to characterize.

**Constraints identified (2026-01-15):**
- Only infant manikins available
- Test equipment suitable for infant manikins only
- Deadline: March 31, 2026

## Available Options (given constraints)

| Option | Human Reference | Novelty | Feasibility |
|--------|-----------------|---------|-------------|
| Infant compression only | **None** (Babic 2017 used scaled adult) | Medium | Cannot validate |
| **Infant ventilation only** | **Huang 2016 (n=205)** | **High** | **Can validate** |
| Infant compression + ventilation | Partial (ventilation only) | High | Mixed validity |

## Decision

**Option C: Infant Ventilation Focus**

### Rationale

1. **Human reference exists:** Huang 2016 provides compliance (78-171 mL/kPa) and resistance (3.7-6.4 kPa/L/s) for infants aged 1-96 weeks (n=205)

2. **Strong novelty:** Verified (D2) - no systematic manikin ventilation benchmark exists. Reiss 2015 explicitly called for this work.

3. **Validation possible:** Can compare manikin C/R values against human reference envelope

4. **Equipment ready:** SDP810 + MFM operational; only need airway pressure sensor

5. **Infant compression excluded:** No human reference data exists to validate against (Babic 2017 confirms this gap)

### Scope Definition

| Include | Exclude |
|---------|---------|
| Infant manikin ventilation characterization | Adult manikins |
| Compliance (C) measurement | Adult ventilation |
| Resistance (R) measurement | Compression mechanics |
| Human reference envelope (Huang 2016) | — |
| Engineering fidelity index (ventilation) | — |

### Paper Positioning

**Title revision suggestion:**
"Engineering Fidelity of Infant CPR Manikin Ventilation: A Data-Driven Reference Model for Respiratory Mechanics"

**Key claims:**
- First systematic benchmark of infant manikin respiratory mechanics
- Quantitative comparison against human infant reference data
- Engineering fidelity index for ventilation compliance and resistance

## Implications

### Apparatus
- [x] Flow measurement (SDP810 + MFM) — ready
- [ ] Airway pressure sensor — pending Bronkhorst discussion
- ~~Load cell integration~~ — **not needed for this scope**

### Data Collection
- Infant manikins only
- Ventilation characterization: C and R at target tidal volumes
- Multiple replicates for unit-to-unit variation

### Claims Registry Update Needed
- Remove/deprioritize compression claims (C1-C5, RC1-RC2)
- Focus on ventilation claims (V1-V2, RV1-RV3)
- Update novelty claims (I2, I3, D1, D2) for ventilation focus

## Revisit If

- Adult manikins become available
- Human infant compression data published
- Co-authors request broader scope
