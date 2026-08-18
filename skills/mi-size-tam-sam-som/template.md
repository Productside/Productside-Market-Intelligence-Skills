# Market Sizing: [MARKET]

**As-of date:** [today]
**Decision supported:** [what this funds or gates]
**Decision horizon:** [years — this is what "stale" is measured against]
**Method:** [bottom-up-built / top-down-validated] — never blended silently
**Evidence base:** [GEOINT sweep, FININT sweep — with dates]
**This run consumes a denominator; it does not produce one.**

## Executive Summary

| Layer | Currency | Customers | Confidence |
|---|---|---|---|
| TAM | [figure] | [count of organizations] | [F/I/A] |
| SAM | [figure] | [count] | [F/I/A] |
| SOM ([N]-year) | [figure] | [count] | [F/I/A] |

**The customer column is the reality check.** [State plainly whether the SOM customer count is achievable at current sales capacity, and if not, say so here rather than in a footnote.]

## TAM — total addressable

| Input | Value | Source (URL, published) | **Vintage** | Label |
|---|---|---|---|---|
| Eligible establishments / population | [count] | [URL] | [period described] | [F/I/A] |
| Spend or employment benchmark | [figure] | [URL] | [period] | [F/I/A] |
| **TAM** | [count x benchmark] | derived | — | Inference |

### External Validation (report both, adopt neither)

| Estimate | Source | Vintage | Method | Difference |
|---|---|---|---|---|
| [figure] | [analyst A] | [period] | [top-down / bottom-up / undisclosed] | — |
| [figure] | [analyst B] | [period] | [method] | [Nx] |

**What explains the gap:** [category definition, geography, or undisclosed method]

If they disagree by 3x, report both and say so. Do not pick the flattering one, and do not average — a midpoint describes no market.

## SAM — serviceable, after real constraints

| Constraint applied | Effect | Basis | Label |
|---|---|---|---|
| Geography | [count remaining] | [which countries, and why] | |
| Segment / size band | [count remaining] | [eligibility rule] | |
| Compliance requirement | [count remaining] | [which regime] | |
| Technical prerequisite | [count remaining] | [technographic basis] | |
| Vendor registration / local content | [count remaining] | [where applicable] | |
| **SAM** | [count] / [currency] | derived | Inference |

Each constraint gets a stated basis. A constraint applied without one is a percentage in disguise.

## SOM — realistically capturable

| Input | Value | Source | Label |
|---|---|---|---|
| Capture-rate basis: comparable revenue | [figure] | [filing, audited?] | Fact |
| Comparable's claimed customer count | [figure] | [source, company-reported?] | Fact |
| **Implied deal size** | [revenue / count] | derived | Inference |
| Named comparable(s) | [companies] | — | — |
| Horizon | [3-5 years] | — | — |
| Capture rate | [%] | [derived from the above, not chosen] | Inference |
| **SOM** | [currency] / [customers] | derived | Inference |

A capture rate with no comparable and no horizon is a wish. **"1% of a $50B market" is refused outright** — it is not a model, it is a wish with arithmetic, and it inverts the work by choosing the answer first.

## Key Assumptions

| Assumption | Label | What it rests on | What changes if it is wrong |
|---|---|---|---|
| Pricing | [F/I/A] | [benchmark] | |
| Adoption or penetration rate | [F/I/A] | [demand signals named] | |
| Deal size | [F/I/A] | [comparable] | |
| Eligibility interpretation | [F/I/A] | [constraint basis] | |

## Sensitivity (this is the deliverable)

Three scenarios distinguished by a **named assumption**, not by a round percentage.

| Scenario | SOM (currency) | SOM (customers) | **The assumption that moves it** |
|---|---|---|---|
| Best | | | [the specific belief, and why it might hold] |
| Base | | | [the belief in the base case] |
| Worst | | | [the specific belief, and why it might hold] |

**The hinge:** [the single assumption the case most depends on — this is what the room should argue about, instead of arguing about the total]

## Stale Inputs

- **[Input]:** vintage [period] against a [N]-year decision horizon. Fact about [period], Assumption about now.

## Where a Layer Could Not Be Computed

> **No evidence found.** [Layer or input] could not be sourced. Sources checked: [list]. What would close it: [the specific release or sweep]. This layer is left uncomputed rather than estimated.

## Final Step

1. Take the base case into the business case (Recommended)
2. Reduce the hinge assumption's uncertainty before presenting
3. Schedule an annual refresh, since sizing rot is slow but real
4. Run Ansoff to choose which slice of the SAM to pursue first

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
