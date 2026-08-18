# Worked Example: What Cartelane Says, and What Is Said About It

**Synthetic teaching case.** Cartelane is fictional, and every URL, date, review count, and sponsor tier below is invented for teaching. Nothing here is a claim about a real company. In a live run every one of these cells would carry a checkable link — the shape is what to copy, not the contents.

**Decision supported:** Whether to reprioritize the integrations roadmap this quarter.
**Window:** 2025-08-18 to 2026-08-18. **Prior sweep:** first run.

## Search Plan

- **Sweep order:** newsroom → analysts → exec social → review clusters on G2 and the RevOps subreddit (the VP RevOps buyer reads both; Finance reads neither) → conference footprint at RevOps Summit and FinOps Exchange → prediction markets: none apply, no regulation gates this category
- **Date window:** 12 months, extended to 18 for the positioning language baseline
- **Noise filter:** excluding Cartelane Logistics (Ontario freight brokerage) and the "Cartlane" retail analytics vendor; collapsing the March funding announcement and its coverage to one origin

## 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| Homepage headline changed from "close the books faster" to "one system of record for revenue" | `example.invalid/cartelane-home` via Wayback, 2026-04-02 vs 2025-11-14 | Fact | Category-widening pivot; platform framing precedes platform packaging by 2-3 quarters | Positioning |
| CEO posted 7 times in 6 weeks about ERP data reconciliation, a topic absent from their prior 2 years of posts | `example.invalid/ceo-posts`, 2026-05 to 2026-06 | Fact | Execs test messaging on social 3-6 months before launch → expect an ERP-integration announcement Q4 | Roadmap, Battle card |
| Sponsor tier at RevOps Summit went Silver (2025) → Diamond (2026) | `example.invalid/revops-sponsors`, 2026-03-11 | Fact | Tier jump = market entry or doubling down; Diamond includes a keynote slot | Positioning |
| 14 of 31 G2 reviews in the window mention connector reliability unprompted | `example.invalid/g2-cartelane`, sampled 2026-08-15 | Fact | Recurring across sources (also present in 4 subreddit threads) → roadmap pressure point | Battle card |
| Two analyst notes describe them in a category that did not exist in the prior year's coverage | `example.invalid/analyst-a`, 2026-02-20; `example.invalid/analyst-b`, 2026-05-03 | Fact | Category-creation attempt underway; briefing cycle active | Positioning |
| Webinar series shifted from month-end close topics to "integration architecture" | `example.invalid/cartelane-events`, 2026-06-01 | Fact | What they teach is what they are about to sell | Roadmap |
| Product line "Cartelane Reconcile" absent from all 2026 materials; still has a live docs page | `example.invalid/reconcile-docs`, checked 2026-08-15 | Inference | Sudden silence = sunset in progress; docs still live means customers exist | Battle card |

**Collapses applied:** The March funding announcement appeared as a newsroom post plus five trade articles plus one analyst summary. All seven trace to the same press release. Collapsed to **one** row. Reported here because "seven sources" would have been the single most misleading number in this document.

## 2. Strongest Inference Chains (ranked, 4 of a possible 5)

1. **CEO posting cluster + webinar topic shift + homepage rewrite** → Inference: an ERP-integration platform play is being positioned now. *Lead time: 3-6 months from exec social, so expect announcement Q4 2026.* → Roadmap bet: decide accelerate-or-concede before their announcement, not after.
2. **Connector-reliability complaints, recurring across two independent sources** → Inference: their existing integration layer is their pressure point, which is exactly the ground they are about to claim. → Battle card: maturity play, cited.
3. **Sponsor tier jump to Diamond with keynote** → Inference: the announcement venue is likely RevOps Summit, March 2027. → Watch: agenda publication in December is the escalation trigger.
4. **"Cartelane Reconcile" silence with live docs** → Inference: sunset in progress, existing customers unmigrated. → Battle card: displacement angle for accounts on that product.

Chain 5 was cut. The analyst category-creation signal is real but changes no artifact this quarter; it is logged as a watch item instead.

## 3. The Say-Versus-Said-About Gap

| Their language | Customers' language | Read |
|---|---|---|
| "one system of record for revenue" | "we still export to a spreadsheet to reconcile" (4 reviews, 2 threads) | **Exposed flank** — the claim and the complaint are about the same workflow |
| "fast implementation" | "up in three weeks" (7 reviews, consistently positive) | **Defended ground** — do not attack this |
| — | "nobody owns the handoff between finance and revops" (recurring, no vendor language matches it) | **Unclaimed whitespace** |

The third row is the most valuable line in this sweep and the easiest to skip, because it required noticing what *nobody* was saying.

## 4. Watch Items

- Analyst category-creation attempt — escalates if a third analyst adopts the term, or if the term appears in Cartelane's own materials
- A single reviewer alleging a data-loss incident — isolated, uncorroborated, and explicitly **not** carried into any chain

## 5. Collection Gaps and Handoffs

> **No signal found.** Prediction markets returned nothing on this market. Sources swept: Polymarket, Kalshi, Metaculus. What the absence suggests: no regulation or approval milestone gates mid-market revenue tooling, which is itself worth knowing — scenario planning here has no crowd-priced anchor. What would close it: nothing. This channel does not apply to this category.

> **Thin, not empty.** Employee-facing OSINT (Glassdoor, Blind) was not swept — it belongs to HUMINT and would have been double-counted here.

- **Deep dive recommended:** the connector-reliability cluster deserves `mi-mine-voice-of-customer` with real quotes and dates before it goes on a card.

## Assumptions to Validate

1. **The Q4 announcement timing rests on the standard 3-6 month exec-social lead time**, not on anything Cartelane said. If their cycle is faster, the accelerate-or-concede decision is already late.
2. **G2 and the subreddit are treated as independent sources.** They may share a small vocal population; four overlapping usernames would collapse chain 2 to a single channel.
3. **"Reconcile" silence is read as a sunset.** It could equally be a rename. The live docs page argues against, but does not settle it.

Note what this sweep did not do: it did not conclude that the platform play is real. Six OSINT signals pointing the same direction is still **one discipline**. The story cannot rate above working hypothesis until TECHINT, HUMINT, or FININT corroborates it — which is fusion's job, not this run's.

## Final Step

1. Hand this inventory to all-source fusion, with HUMINT and TECHINT next (Recommended)
2. Mine the connector-reliability cluster properly with voice-of-customer
3. Schedule this as a monthly OSINT digest so the next run is a diff
4. Turn the say-versus-said-about gap into positioning input

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
