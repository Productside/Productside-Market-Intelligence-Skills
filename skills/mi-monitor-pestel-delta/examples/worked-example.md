# Worked Example: One Factor Moved, Four Held, One Arrived

**Synthetic teaching case.** All regulations, figures, dates, and sources below are invented for teaching. Nothing here is a claim about any real policy, jurisdiction, or economic condition.

## Run Header

~~~
As-of date:        2026-08-18
Prior baseline:    revops-pestel-2026-05-12.md
Window covered:    2026-05-12 to 2026-08-18 (98 days)
Scope:             Mid-market revenue operations tooling; United States, Germany
Sources swept:     Federal register equivalents (US, DE), EU consultation
                   register, central bank rate publications, occupation and wage
                   releases, standards working-group rosters
Factors with no material movement: 4 of 6
Stored as:         revops-pestel-2026-08-18.md
~~~

Four of six held. That is what a filtered quarter looks like, and reporting it that way is what makes the two that moved worth reading.

## Materiality Threshold

Movement is material when it crosses a threshold that matters to a named artifact: the US market sizing model (2026-08-18), the German entry case (2026-08-18), or the pricing corridor (2026-06).

## Factor Deltas

### Political — *No material movement.*

Trade and procurement policy affecting this category unchanged in both jurisdictions this window.

### Economic — **Moved**

- **Was:** Buyer-role median wage growth at 11% over three years, supporting a $200-400/seat/month corridor — occupation wage release, vintage 2025, cited in `revops-pestel-2026-05-12.md`
- **Now:** Latest release shows the three-year figure revised down to 6% — `example.invalid/wage-release`, published 2026-07-30, vintage 2025 revised
- **Threshold crossed:** The pricing corridor was built on a 2-4% of loaded salary heuristic against the 11% growth trend. At 6%, the top of the corridor moves from roughly $400 to roughly $355.
- **Read:** The willingness-to-pay ceiling is lower than the corridor assumed, and the corridor's upper half is now unsupported. *Inference.*
- **What it changes:** Pricing corridor (2026-06), and the sizing model's spend benchmark downstream of it.

Note the shape of this entry. The wage figure did not fall — it was *revised*, in a statistical release, and the number itself moved by five percentage points on a metric nobody was watching. It was found because the factor was checked, not because anyone noticed news.

### Social — *No material movement.*

Buyer population and role-adoption trends unchanged.

### Technological — *No material movement.*

The ledger-interchange standard remains at working-group stage, as at baseline. It has not advanced; it has not stalled. Reported explicitly so silence is not mistaken for not checking.

### Environmental — *No material movement.*

No disclosure regime reached this buyer's size band in either jurisdiction.

### Legal — *No material movement, with a watch item.*

The German financial-reporting amendment noted at baseline as **proposed** remains **proposed**. It has not entered consultation. Distinguishing this from "coming" matters: proposed is not a timeline, and at baseline this was already being described internally as though a date existed.

## Broken Assumptions

| Prior artifact | The assumption inside it | What is now true | Severity |
|---|---|---|---|
| Pricing corridor (2026-06) | Buyer-role wages growing 11% over three years, supporting the corridor's top at ~$400/seat/month | Revised to 6%; corridor top is ~$355 | **Invalidates** the upper half of the corridor |
| US sizing model (2026-08-18) | $26,600 annual spend benchmark per establishment, derived partly from that corridor | Benchmark is overstated by roughly 8-11% | **Weakens** — TAM and SOM both move down proportionally |
| German entry case (2026-08-18) | Regulatory amendment would create demand within 18 months | Amendment still only proposed; no consultation stage entered | **Weakens** — the demand catalyst has no timeline |

Three artifacts, one genuinely invalidated. This section is the run: without it, "wage growth was revised down" is a fact about a statistical release that nobody would act on.

## New to the Frame

| Factor | What changed | Why it now applies | What to watch |
|---|---|---|---|
| **Environmental (EU)** | A sustainability-disclosure regime that previously applied only above 750 employees entered consultation on lowering the threshold to 250 | Our German SAM is concentrated in the 100-999 band. At 250, roughly 40% of that SAM acquires a reporting obligation with a reconciliation component. | Whether the threshold change is adopted, and at what number |

This factor was rated irrelevant at baseline and correctly so — it did not apply. It applies now because a threshold moved toward our buyers rather than because anything about our market changed. That is exactly the kind of arrival "new to the frame" exists to catch, and re-examining only the baseline's existing factors would have missed it entirely.

## So What

- **Most consequential movement:** the wage revision, which invalidates the top half of the pricing corridor and moves the sizing model down with it. The pricing decision scheduled for Q4 should not proceed on the current corridor.
- **Most consequential arrival:** the EU disclosure threshold consultation, which could turn a compliance requirement into a demand driver for roughly 40% of the German SAM — the entry case's original catalyst was the wrong regulation.
- **Nothing changed for:** political, social, technological, and environmental-US. Named explicitly, because silence about a factor is indistinguishable from not checking it.

## Assumptions to Validate

1. **The 2-4% of loaded salary heuristic** connecting wages to the corridor is convention, not evidence. It was an unlabeled assumption in the original corridor and it is doing all the work in this quarter's finding.
2. **The wage revision is treated as a correction rather than a trend change.** A revised series and a declining series have different implications and the release does not distinguish them.
3. **The 40% SAM figure** for the disclosure threshold is derived from a 2023-vintage German enterprise count by size band.

## Final Step

1. Rebuild the pricing corridor before the Q4 pricing decision (Recommended)
2. Add the EU disclosure consultation to the standing monitoring scope
3. Keep the quarterly cadence so the next run is a diff
4. Revisit the German entry case — its stated catalyst has no timeline and a better one may have just arrived

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
