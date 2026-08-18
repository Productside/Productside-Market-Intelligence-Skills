# Worked Example: The Supplier Nobody Called a Supplier

**Synthetic teaching case.** All companies, figures, and sources below are invented for teaching. Nothing here is a claim about a real industry or vendor.

**Industry:** Mid-market revenue operations tooling — software sold to a RevOps or finance function to reconcile sales and finance data.
**Excluded:** Enterprise financial close suites (different buyer, different switching costs) and CRM platforms (different structure entirely). Both compete, and neither shares this structure.
**Decision supported:** Whether to keep investing here at current levels.

## 1. Competitive Rivalry — **Moderate**

| Structural factor | Evidence | Source | Label |
|---|---|---|---|
| Exit barriers | Low. Two vendors exited to adjacent categories in 24 months with no distress signals | M&A tracker, 2026-06 | Fact |
| Differentiation | Low and falling. Every direct player's last three releases were connectors | Changelogs across 3 vendors, 2026 | Fact |
| Industry growth | Moderate; buyer population +7% over 3 years | Occupation statistics, vintage 2025 | Fact |
| Fixed-cost profile | Low. Software economics, no volume imperative | — | Inference |

**Rating rationale:** Rivalry is moderate rather than strong because exit barriers are low — vendors leave rather than fight to the bottom. Differentiation is falling, which pushes toward strong, but nothing structurally traps anyone here.

Note what did not enter the rating: there are eleven vendors in this category. Count is not structure.

## 2. Threat of New Entrants — **Strong**

| Structural factor | Evidence | Source | Label |
|---|---|---|---|
| Capital requirements | Low. Two seed-funded entrants shipped in 2026 | Funding database, 2026 | Fact |
| Regulatory gates | None at mid-market. SOC 2 is a buyer requirement, not a regulatory one — 12-18 months and modest cost | Trust registries | Fact |
| Switching costs | Low and falling. An interchange standard entered working-group stage in 2026 | Standards WG roster, 2026-04 | Fact |
| Distribution access | Open. Published pricing and self-serve trials are category norms | Competitive snapshot, 2026-08 | Fact |
| What entrants actually spent | Both 2026 entrants shipped on seed rounds | Funding database | Fact |

**Rating rationale:** Strong on every factor, and the interchange standard makes it worse over time.

## 3. Threat of Substitutes — **Strong**

### Non-consumption and manual alternatives

| Alternative | Who uses it | Why it persists | Source |
|---|---|---|---|
| **A spreadsheet maintained by one analyst** | Most of the mid-market | Free, works, and owned by someone who understands the business | Named as current state in 11 of 19 buyer threads |
| Outsourced services firms | Under ~200 employees | Cheaper than tooling plus headcount | Services directory |
| Doing nothing | A large share | The pain is quarterly, not daily | Inference from thread framing |

Estimated 60-80% of the problem is solved this way, labeled **Inference**. Non-consumption is the market leader and appears on no competitive slide in this category.

### AI-driven substitution

| Question | Assessment | Evidence | Label |
|---|---|---|---|
| What could a general-purpose model do adequately today? | The reconciliation *reasoning* — given two exports, identify mismatches and propose which side is wrong. This is the core job. | 4 forum posts describing exactly this workflow | Fact |
| Is there evidence buyers are already doing it? | Yes, at small scale. Four independent posters describe pasting exports into a model as their current process. | Public forum, 2026-03 to 2026-07 | Fact |
| What still requires the product? | Scheduled data access, write-back, audit lineage, and someone accountable when the number is wrong | Inference | Inference |

**Materiality: emerging, and moving.** The model does not have the data access or the liability position. Both are addressable, and neither is a moat anyone would choose to defend. Four posters is thin evidence and it is the *direction* that matters: the substitute is improving on its own schedule, without a competitor deciding anything.

This assessment is why the substitutes rating is strong rather than moderate, and it would have been absent entirely from a forces read written against the pre-2023 version of this framework.

### Other substitutes

| Substitute | Evidence | Source |
|---|---|---|
| CRM-native reconciliation | Two CRM vendors have signaled it on public roadmaps | Roadmap pages, 2026-06 |

**Rating rationale:** Strong. Non-consumption holds most of the market, AI substitution is emerging in the core job, and two adjacent platform vendors have signaled entry.

## 4. Buyer Power — **Strong**

| Structural factor | Evidence | Source | Label |
|---|---|---|---|
| Concentration | Low — fragmented buyers | Establishment counts, vintage 2024 | Fact |
| Bake-off frequency | High — 4 of 4 observed RFPs ran competitive evaluations | Our RFP records, 2026 | Fact |
| Switching costs | Low, falling with the interchange standard | Standards WG | Fact |
| Price transparency | High — two of three direct players publish | Pricing pages, 2026-08 | Fact |
| Who signs | Finance, who has a credible alternative: keep the spreadsheet | VoC mining, 2026-08 | Inference |

**Rating rationale:** Strong. The last row does most of the work — a buyer whose alternative is "keep doing what we do" has enormous power, and it is invisible if you only compare vendors.

## 5. Supplier Power — **Moderate, and structurally underappreciated**

| Dependency | Concentration | Unilateral terms? | Evidence | Label |
|---|---|---|---|---|
| Cloud infrastructure | Single provider, no multi-cloud | Yes — published pricing, changes with notice | Our own architecture | Fact |
| **Model / inference provider** | **Single provider for the reconciliation feature** | **Yes — pricing, rate limits, and model deprecation all unilateral** | Our own contracts | Fact |
| App store | n/a — no mobile product | — | — | — |
| Data source APIs | Two ERP vendors whose API terms permit unilateral change | Yes | Published API terms, 2026 | Fact |
| Talent | Moderate; the specialty is scarce but not unique | Hiring data | Inference |

**Rating rationale:** Moderate rather than weak, and the reason is the second and fourth rows. The instinct in a software category is to rate supplier power weak because nobody ships a physical good. But a single inference provider that can change pricing, deprecate a model, or alter rate limits with notice and no negotiation is textbook supplier concentration — and so are two ERP vendors whose API terms we do not control and whose product we integrate into.

This is the force most likely to be rated weak by default, and rating it honestly changes the profit-pool read below.

## Withheld Ratings

None withheld. All five carry at least one cited signal. Had the AI-substitution evidence been absent rather than thin, that rating would have been withheld rather than guessed — four posters is thin but real, and it is labeled as such.

## The Profit Pool

- **Where the money accumulates:** not with the tooling vendors. Entrants are cheap, buyers bake off, switching costs are falling, and most of the problem is currently solved for free. The money accumulates with **the platforms that own the underlying data** — the ERP and CRM vendors, who charge for the systems being reconciled and can absorb reconciliation as a feature — and with **services firms**, who are paid for the outcome rather than the tool.
- **Does the structure let us reach it?** Only partially. Our audit-lineage and liability position is the one thing the spreadsheet, the general-purpose model, and a fast-follow CRM feature all lack. That is a real pocket of the pool and it is narrower than the category we currently describe ourselves as being in.
- **What would flip this:** if the interchange standard is adopted, switching costs fall further and the answer worsens. If a regulator makes reconciliation lineage mandatory in our buyers' industries, the pocket widens sharply and becomes defensible.

Four of five forces are strong or moderate against us. That is the finding, and it does not say *exit* — it says the durable position is narrower and more specific than "revenue operations tooling."

## Assumptions to Validate

1. **The AI-substitution assessment rests on four forum posters.** Direction over magnitude, and it is the assumption most likely to be understated rather than overstated.
2. **The 60-80% non-consumption estimate is an Inference** from thread framing, not a measurement, and it drives the substitutes rating.
3. **Supplier power assumes our single-provider model dependency persists.** A second provider would move this rating, and that is a decision we control.

## Final Step

1. Act on the profit-pool read — narrow the durable position to audit lineage and liability (Recommended)
2. Get a second inference provider and re-rate supplier power
3. Schedule an annual refresh, since structure moves slowly but decisively
4. Run Ansoff to choose the growth path this structure permits

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
