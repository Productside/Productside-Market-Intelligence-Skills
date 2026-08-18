# Worked Example: The Customer Column Broke the Model

**Synthetic teaching case.** Every count, price, revenue figure, and analyst estimate below is invented for teaching. Nothing here is a claim about a real market or company.

**Decision supported:** Whether the US mid-market segment funds a dedicated go-to-market team.
**Decision horizon:** 3 years. **Method:** bottom-up-built, top-down-validated against two external estimates.
**Evidence base:** GEOINT sweep 2026-08-18, FININT sweep 2026-08-18.

## Executive Summary

| Layer | Currency | Customers | Confidence |
|---|---|---|---|
| TAM | $1.02B | 38,400 establishments | Inference |
| SAM | $412M | 15,400 establishments | Inference |
| SOM (3-year) | $23.8M | **890 customers** | Inference |

**The customer column is the reality check, and here it fails.** 890 customers in three years is roughly 297 per year, or about 25 per month. Our current team closes 11 per month at a 31% win rate. The SOM as modelled requires more than doubling monthly close volume and sustaining it for thirty-six months.

Stating that in the summary rather than in a footnote is the point of expressing both columns. The currency figure, $23.8M, looked entirely reasonable to everyone who saw it.

## TAM

| Input | Value | Source | **Vintage** | Label |
|---|---|---|---|---|
| Eligible US establishments, 50-999 employees, NAICS 541511 + 511210, deduplicated | 38,400 | `example.invalid/cbp` | **2024** | Fact |
| Annual spend benchmark per establishment on this category | $26,600 | Derived: our median ACV against comparable pricing | — | Inference |
| **TAM** | **$1.02B** | derived | — | Inference |

The benchmark is an Inference, not a Fact, and it is the weakest input in the TAM line. It is derived from our own ACV and two competitors' published pricing, not from a spend survey.

### External Validation

| Estimate | Source | Vintage | Method | Difference |
|---|---|---|---|---|
| $4.1B global | Analyst A | 2025 | Top-down, method undisclosed | — |
| $12.6B global | Analyst B | 2025 | Top-down, includes adjacent CRM tooling | **3.1x** |

**What explains the gap:** category definition. Analyst B folds in adjacent CRM functionality our product does not replace. Our $1.02B is US-only against a global figure, so the comparison is directional at best — a US share of roughly 25% of Analyst A's global number is plausible; against Analyst B's it would be 8%, which is also plausible. **Neither is adopted and neither is averaged.** A $8.35B midpoint would describe no market.

## SAM

| Constraint applied | Effect | Basis | Label |
|---|---|---|---|
| Geography: US only | 38,400 | Decision scope | Fact |
| Segment: 100-999 employees | 24,100 | Below 100, buyers keep the spreadsheet — landscape scan finding | Inference |
| Technical prerequisite: runs one of two ERPs we connect to | 16,900 | Technographic estimate, TECHINT sweep | Inference |
| Compliance: none required at mid-market | 16,900 | No regulatory gate below enterprise | Fact |
| Buying-center exists: a named RevOps or equivalent function | 15,400 | Occupation prevalence, vintage 2025 | Inference |
| **SAM** | **15,400 / $412M** | derived | Inference |

Each constraint has a basis. The size-band cut is the largest single reduction and rests on a landscape-scan finding about non-consumption, which is an Inference — if the sub-100 segment is actually addressable, SAM rises by roughly 60%.

## SOM

| Input | Value | Source | Label |
|---|---|---|---|
| Comparable revenue (Meridian) | $412M | 10-K FY2026 | Fact (audited) |
| Comparable's claimed customer count | "over 1,900" | IR page | Fact (company-reported, **unaudited**) |
| **Implied deal size** | ~$217K ACV | derived | Inference |
| Our own median ACV | $26,600 | Our data | Fact |
| Named comparables | Meridian (enterprise-weighted), Cartelane (mid-market) | — | — |
| Horizon | 3 years | — | — |
| Capture rate | **5.8% of SAM** | Derived from comparable trajectories at similar scale, not chosen | Inference |
| **SOM** | **$23.8M / 890 customers** | derived | Inference |

Meridian's $217K implied ACV is eight times ours, which tells us they are enterprise-weighted and that their capture rate is not directly transferable. Cartelane's mid-market trajectory is the closer comparable, and the 5.8% is anchored there.

Note the derivation direction: the capture rate came *out* of comparable trajectories. It was not chosen and then multiplied. Had we started with "1% of a $50B market," the number would have been chosen first and the model built backwards to justify it — which is the framing this run refuses outright.

## Key Assumptions

| Assumption | Label | Rests on | If wrong |
|---|---|---|---|
| $26,600 spend benchmark | Inference | Our ACV plus two published price lists | TAM moves proportionally; SOM moves with it |
| Sub-100 segment is non-addressable | Inference | Landscape scan, non-consumption finding | SAM rises ~60% |
| Technographic ERP estimate | Inference | Sample-based, not a census | SAM moves ±20% |
| 5.8% three-year capture | Inference | Cartelane's trajectory at comparable scale | The whole SOM |

## Sensitivity

| Scenario | SOM (currency) | SOM (customers) | The assumption that moves it |
|---|---|---|---|
| **Best** | $38.1M | 1,430 | Sub-100 segment proves addressable after all, lifting SAM ~60%. Would require the spreadsheet to stop being adequate at that size — a specific, checkable belief. |
| **Base** | $23.8M | 890 | Capture rate tracks Cartelane's mid-market trajectory at 5.8% over three years |
| **Worst** | $9.4M | 350 | Capture rate halves because a CRM vendor ships native reconciliation in year two, compressing the window to eighteen months |

Three scenarios, three named beliefs. Not the base case scaled by ±40% — each scenario is distinguished by something that could be true or false, and each could be checked before the money is spent.

**The hinge:** the three-year capture rate. Everything else moves the model by tens of percent; this moves it by a factor of four between best and worst. It is also the assumption most reducible with cheap work — Cartelane's own trajectory is partly observable in their public customer count over time.

## Stale Inputs

- **Establishment counts:** vintage **2024** against a three-year decision horizon reaching into 2029. A Fact about 2024 and an Assumption about 2029. The 2025 release lands in spring and should update this.
- **Occupation prevalence:** vintage **2025**. Current enough.

## Where a Layer Could Not Be Computed

> **No evidence found.** A spend-per-establishment survey for this category does not exist. Sources checked: two industry associations, three analyst summary pages, federal expenditure data. What would close it: nothing publicly. The $26,600 benchmark is therefore an Inference from our own pricing and two competitors', and it is labeled as such wherever it appears — including in the TAM line, which is the number most likely to be quoted without its label.

## The Finding

The model is defensible. The conclusion it supports is not the one anyone expected: **the segment does not fund a dedicated team at the base case**, because 890 customers in three years is not reachable at current capacity. The useful next question is not "is the market big enough" — it is $412M of SAM, which is plenty — but "what would have to change about our close rate or motion," which is a different investment discussion entirely.

That reframing came from the customer column. In currency alone, $23.8M against a $412M SAM looks like a straightforwardly fundable opportunity.

## Final Step

1. Take the base case to the business case, with the capacity constraint stated plainly (Recommended)
2. Reduce the capture-rate uncertainty by tracking Cartelane's public customer count over four quarters
3. Schedule an annual refresh when the 2025 establishment data lands
4. Run Ansoff to choose which slice of the SAM to pursue first

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
