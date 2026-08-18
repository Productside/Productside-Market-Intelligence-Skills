# Worked Example: The Market Was Mostly Spreadsheets

**Synthetic teaching case.** Every company name, quote, figure, and source below is invented for teaching. Nothing here is a claim about a real market or a real vendor.

**Decision supported:** Whether to enter mid-market revenue operations tooling.
**Buyer whose model defines the segments:** VP RevOps, with Finance running evaluation.

## 1. Scope and Category Language

| Who | What they call this market | Source |
|---|---|---|
| Vendors | "Revenue operations platform" | `example.invalid/vendor-a`, 2026-08 |
| Analysts | "Revenue intelligence and orchestration" | `example.invalid/analyst-note`, 2026-05 |
| **Buyers** | "getting finance and sales to agree on the same number" | 14 review and forum posts, `example.invalid/g2`, `example.invalid/reddit`, 2026-02 to 2026-08 |

**Where they diverge:** Vendors and analysts both describe a *platform*. Buyers describe a *reconciliation problem between two departments*. Nobody in the vendor set uses the buyers' framing, and it is the framing that appears in fourteen independent posts. That divergence is the most valuable line in this scan — it names a category nobody is claiming.

## 2. Segmentation (buyer-side)

| Segment | The job the buyer is doing | How they group alternatives | Evidence |
|---|---|---|---|
| Reconcilers | Make finance's number and sales' number match before the board meeting | Compares tools against "how our analyst does it now" | 9 forum posts, `example.invalid/reddit`, 2026 |
| Forecasters | Produce a defensible forecast leadership will not overrule | Compares tools against each other, and against the CRM's native forecasting | 6 reviews, `example.invalid/g2` |
| Process owners | Stop deals from stalling in handoffs between teams | Compares tools against workflow and ticketing systems | 4 posts |

Note what the buyer-side segmentation did *not* produce: segments by company size or vertical, which is how every vendor in this category segments. Buyers group by the job. Vendors group by the invoice.

## 3. Player Map (12 of ~40 identified)

**Selection rule:** appearance in buyer-side discussion threads and review comparisons, not by funding or size. Twenty-eight vendors were found and excluded; a list of forty changes no decision.

### Direct

| Player | What they sell | To whom | Source |
|---|---|---|---|
| Cartelane | Revenue ops platform, integration-led | Mid-market RevOps | `example.invalid/cartelane` |
| Meridian | Revenue systems, enterprise-down | Enterprise finance | `example.invalid/meridian` |
| Northwind | Forecasting-first | Sales leadership | `example.invalid/northwind` |

### Adjacent — one product decision from entering

| Player | Current position | What entry would take | Source |
|---|---|---|---|
| Two major CRM vendors | Own the sales data already | Shipping reconciliation, which both have signaled | `example.invalid/crm-roadmap`, 2026-06 |
| Two accounting platforms | Own the finance side | Shipping the sales-side connectors | `example.invalid/accounting-partner-page` |

The adjacent bucket is where the real threat sits in this category, and it is the bucket a vendor-list scan never produces.

### Substitutes and non-consumption

| Alternative | Who uses it | Why it persists | Source |
|---|---|---|---|
| **A spreadsheet maintained by one analyst** | Most of the mid-market | It works, it is free, and it is owned by someone who understands the business | Named as the incumbent in 11 of 19 relevant threads |
| Outsourced RevOps services firms | Companies under ~200 employees | Cheaper than tooling plus headcount | `example.invalid/services-directory` |
| In-house build on the data warehouse | Companies with a data team | Already own the warehouse; marginal cost is low | 3 forum threads |
| **Doing nothing — living with two numbers** | A large share | The pain is quarterly, not daily | Inferred from thread framing |

**Estimated share of the problem currently solved this way:** 60-80%, labeled **Inference**. Basis: eleven of nineteen threads name a spreadsheet as the current state, and no vendor in this category claims more than low-single-digit penetration of the eligible population. The range is wide on purpose.

This bucket is the market leader. It appears on no competitive slide anywhere, and it is the thing an entrant would actually have to displace.

### Emerging

| Player | Funding or hiring signal | Source |
|---|---|---|
| Two seed-stage entrants | Both funded 2026, both hiring integration engineers | `example.invalid/funding-db` |

## 4. Dynamics

1. **Where the money is:** enterprise, not mid-market. The three largest vendors all report enterprise as their growth segment, and two have raised their published floor in the past year. — `example.invalid/pricing-archive`, 2026-08
2. **Where the momentum is:** integration depth, not analytics. Every direct player's last three releases were connectors. — changelogs, 2026
3. **Consolidating or fragmenting:** **fragmenting at the low end, consolidating at the top.** Two acquisitions of enterprise players in 18 months, while seed funding into mid-market entrants continues. — `example.invalid/ma-tracker`
4. **Technology and regulatory shifts:** a ledger-interchange standard entered working-group stage in 2026, which would lower integration switching costs across the category if adopted. — `example.invalid/standards-wg`

Four reads, four citations. Not "the market is evolving rapidly."

## 5. Whitespace and Dead Zones

| Gap | Judgment | Why | What would settle it |
|---|---|---|---|
| Tooling for the reconciliation job as buyers describe it | **Whitespace** | Fourteen independent buyer posts name it; no vendor's language matches it | Ten buyer interviews confirming they would pay for it framed that way |
| Sub-50-employee segment | **Dead zone** | Three funded entrants tried between 2021 and 2024; all three moved upmarket or shut down. The spreadsheet is genuinely adequate below that size. | Evidence that the pain became daily rather than quarterly at that size |
| Vertical-specific compliance reconciliation | **Unknown, leaning whitespace** | Two buyer mentions only; too thin to call | Whether regulated buyers appear in the forum data at all |

Naming a dead zone is the harder half. The sub-50 segment is empty *because* three companies already died there, and an empty segment is attractive precisely for the reason it is empty.

## 6. Collection Gaps

> **No signal found.** Market share data returned nothing usable. Sources swept: three analyst summary pages, two funding databases. What the absence suggests: the category is too fragmented and too young for share to be measured, which is itself consistent with the non-consumption finding — you cannot have meaningful share of a market that mostly has not bought anything. What would close it: nothing publicly.

> **Thin.** The vertical-compliance gap rests on two posts. Treated as unknown rather than promoted.

## Assumptions to Validate

1. **The buyer-side segmentation rests on nineteen public posts.** Public voice skews toward the vocal and the frustrated. Ten interviews would either confirm the reconciliation framing or dissolve it, and everything downstream depends on which.
2. **The 60-80% non-consumption estimate is an Inference from thread framing**, not a measurement. It is the single most consequential number in this scan and the least precise.
3. **The adjacent CRM threat is read from roadmap signals.** Signaling and shipping are different, and both vendors have signaled things they did not ship.

This scan does not recommend entry. It produces the map that an entry decision needs, and the map's central finding is that the incumbent is a spreadsheet.

## Handoffs

- **Snapshot:** Cartelane, Meridian, and the larger of the two CRM vendors — the last because adjacent is where the threat sits
- **Sizing:** count establishments in the buyer-side segments, not in the vendor categories
- **Positioning:** the buyer-versus-vendor divergence is the raw material

## Final Step

1. Snapshot Cartelane, Meridian, and the adjacent CRM vendor (Recommended)
2. Take the buyer-side segments into sizing and count what they named
3. Schedule an annual re-scan, since category boundaries move slowly
4. Run ten buyer interviews against the reconciliation framing before anything else

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
