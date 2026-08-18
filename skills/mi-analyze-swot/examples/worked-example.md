# Worked Example: A SWOT With Three Corrections and One Empty Box

**Synthetic teaching case.** The company, competitors, quotes, and figures below are invented for teaching. Nothing here is a claim about a real organization.

**Whose SWOT:** Ours (a mid-market revenue operations vendor).
**Decision supported:** What we defend and what we concede in next year's plan.
**Evidence base:** Fusion brief 2026-08-18, competitive snapshot 2026-08-18, VoC mining 2026-08-18.

## Quadrant Corrections Made

| Candidate entry | Was filed as | Moved to | Why |
|---|---|---|---|
| "Cartelane's implementation is faster than ours" | Weakness | **Threat** — and a separate weakness written | It is their capability, not our deficiency. The weakness underneath is *our* six-week onboarding, which is a different sentence with different evidence. |
| "Expand into regulated verticals" | Opportunity | **Removed** — it is a strategy | An opportunity is an external condition. The real opportunity is the compliance regime creating demand; the expansion is what we might do about it. |
| "Our engineering team is strong" | Strength | **Removed** — no evidence | Every company says this. Nothing in the evidence base supports or refutes it, so it does not belong in a document that claims to be evidence-bound. |

Three corrections, and the first is the one worth studying. "Their thing is better than our thing" feels like a weakness because it feels bad. It is two facts: a threat that is theirs, and a weakness that is ours, and separating them is what lets each be acted on.

## Strengths — internal, current

**Ranked on: defensibility.**

| # | Strength | Source (URL, date) | Label | Why it is defensible |
|---|---|---|---|---|
| 1 | Full finance-side audit trail, certified | Our SOC 2 report, 2026-03 | Fact | Certification is a two-year moat; Cartelane's is in process and Northwind has none |
| 2 | Published pricing in a category that mostly hides it | Competitive snapshot, 2026-08-18 | Fact | Defensible only while competitors stay opaque; Cartelane also publishes, so this is a two-vendor advantage, not a unique one |
| 3 | Two native ERP connectors, shipped and referenceable | Our docs; customer references | Fact | Least defensible of the three — Cartelane has eleven staged endpoints |

Three, not five. Two further candidates were removed for lack of evidence.

## Weaknesses — internal, current

**Ranked on: exploitability.**

| # | Weakness | Customer evidence | Label | How exploitable |
|---|---|---|---|---|
| 1 | Six weeks to first reconciled report | "Three weeks with [competitor], six with you — that's a whole close cycle." — win/loss debrief, 2026-06 | Fact | **Highly.** It is an RFP criterion in 4 of 4 RFPs we have seen, and a competitor is twice as fast |
| 2 | Cannot tell a user which of two disagreeing systems is wrong | VoC mining: recurring across two independent sources, 2026-08 | Fact | Moderately — the whole category shares it, so nobody is currently exploiting it |
| 3 | Support response degrades above 40 concurrent implementations | Internal ops data, 2026-Q2 | Inference | Low today, high if we win the deals we are chasing |

The first entry came from win/loss, not from our backlog. Our internal weakness list had "connector coverage" first; customers never mentioned it.

## Opportunities — external, not controllable

**Ranked on: fit to our strengths.**

| # | Opportunity (external condition) | Source (URL, date) | Label | Which strength it fits |
|---|---|---|---|---|
| 1 | Cartelane vacated the sub-$119 segment, raising its floor 144% | SIGINT capture, 2026-08-18 vs 2026-05-14 | Fact | Published pricing — their former Starter customers are price-aware and now shopping |
| 2 | A ledger-interchange standard entered working-group stage, which would lower switching costs category-wide | Standards WG roster, 2026-04 | Fact | Audit trail — lower switching costs favor the vendor with the compliance story |
| 3 | Buyer population growing 7% over three years; wages up 11% | Occupation statistics, vintage 2025 | Fact | All three — a growing, better-funded buying population |

Note that none of these starts with a verb we control. "Expand into regulated verticals" was removed for exactly that reason.

## Threats — external, not controllable

**Ranked on: likelihood times damage.**

| # | Threat | Source (URL, date) | Label | Likelihood x damage |
|---|---|---|---|---|
| 1 | Cartelane's native integration layer lands within two quarters | Fusion brief: 4 disciplines, Staffed | Inference | **High x High.** It closes our only shipped-connector advantage |
| 2 | Cartelane's SOC 2 completes, erasing our certification moat | Trust registry: in process, 2026-06 | Fact | Medium x High. 12-18 month horizon |
| 3 | Cartelane's implementation speed, twice ours, in an RFP criterion | Competitive snapshot, 2026-08-18 | Fact | High x Medium |
| 4 | Adjacent CRM vendors own the sales-side data and have signaled reconciliation | Landscape scan, 2026-08 | Inference | Low x Very High. The category-ending scenario, and the one nobody is watching |

Threat 4 ranks fourth on likelihood-times-damage and is the one to re-read in six months. Ranking on a stated basis is what keeps it visible instead of letting it drop off a list ordered by urgency.

## The Crossings

### S-O

| Strength | Opportunity | The move this quarter | Owner |
|---|---|---|---|
| Published pricing | Cartelane vacated sub-$119 | Named-account campaign to their former Starter customers, leading with price transparency. The list is buildable from public case studies. | Product Marketing |
| Certified audit trail | Interchange standard lowering switching costs | Join the working group. Low cost, and it positions us where switching costs fall. | Product |

### W-T

| Weakness | Threat | What protects it | Owner |
|---|---|---|---|
| Six weeks to first report | Cartelane at three weeks, an RFP criterion | Cut onboarding to four weeks by Q1, or concede the speed criterion and compete on audit trail explicitly. **This is the plan's central choice.** | Product + Services |
| Two connectors shipped | Their integration layer landing in two quarters | Do not race to eleven. Deepen the two we have into the audit story, where they cannot follow before their SOC 2 completes. | Product |

The second W-T crossing is a *concession*, deliberately made and written down. A SWOT that produces only offensive moves has not taken its threats seriously.

## Where Evidence Was Missing

- **Threats:** no evidence found regarding Northwind. They appeared in three lost deals and we cannot characterize them at all. Sources checked: their site, three funding databases, two review platforms. What would close it: win/loss interviews on those three deals.

That empty space is doing real work. A fourth plausible threat entry about Northwind would have been easy to write and would have hidden the fact that we know nothing.

## Assumptions to Validate

1. **Threat 1's two-quarter timeline** comes from a lead-time heuristic, not from anything Cartelane announced. If they are slower, the onboarding decision has more room.
2. **Weakness 1's exploitability** rests on four RFPs. Whether implementation speed decides deals or merely appears in criteria is a win/loss question.
3. **Opportunity 1 assumes their former Starter customers are shopping** rather than absorbing the increase. Nothing here establishes that.

## Final Step

1. Make the W-T call on onboarding — cut to four weeks or concede the criterion (Recommended)
2. Run win/loss on the three Northwind deals and fill the empty box
3. Schedule a semi-annual refresh so the position is tracked
4. Run the same SWOT on Cartelane for contrast

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
