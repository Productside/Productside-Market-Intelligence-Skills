# Worked Example: Three Lost Deals and a QBR on Thursday

**Synthetic teaching case.** Cartelane, Northwind Analytics, and the lost-deal history are fictional. The routing reasoning and the source types named are real; no external fact is asserted here.

## The Ask

> "Cartelane showed up in three lost deals this quarter and my VP wants a read before the QBR Thursday."

Two questions asked, not three. The third was skipped because the answer was discoverable.

`Setup Q1/3` — What decision will this change? The user chose *"whether we reprioritize the integrations roadmap this quarter."*

`Setup Q2/3` — How much time before this needs to be useful? *"Thursday morning, so realistically Wednesday afternoon."*

Relationship was not asked. Three lost deals establishes it.

## The Six Variables

| Variable | Value | Label |
|---|---|---|
| `[TARGET]` | Cartelane, Inc. | Fact — user named them |
| `[MARKET]` | Mid-market revenue operations tooling; NAICS 541511 and 511210 both plausibly apply | Inference — the user's own category language, not a filed classification |
| `[GEOGRAPHY]` | United States and Canada | Inference — all three lost deals were North American; their expansion elsewhere is unverified |
| `[BUYER]` | VP of Revenue Operations, with Finance as economic buyer | Fact — user's own deal history |
| `[CAPABILITY]` | Suspected: native ERP integrations replacing the partner-built connectors both vendors rely on | Assumption — comes from one sales anecdote, and it is the assumption most likely to be wrong |
| `[DECISION]` | Whether to reprioritize the integrations roadmap this quarter | Fact — user stated it |

`[CAPABILITY]` is deliberately labeled Assumption. It came from a single seller's recollection of a single call. It is a useful hypothesis to sweep against and a terrible thing to brief as established.

## Identity and Perimeter

- **Legal entity:** Cartelane, Inc. (Delaware). Trades as "Cartelane."
- **Ownership:** Private, venture-backed. No filings expected beyond incorporation records — FININT will be thin, and that is a finding, not a failure.
- **Tickers:** None.
- **Subsidiaries and brands:** One product brand, "Cartelane Flow," acquired 2023.
- **Same-name confusions to exclude by name:** Cartelane Logistics (Ontario freight brokerage, unrelated), and "Cartlane" — a common misspelling that returns a retail analytics vendor.

Naming the Ontario freight brokerage cost one line here. Discovering it in the HUMINT section would have meant recounting job postings.

## Engagement Frame

- **Relationship:** Competitor
- **Depth:** Standard. Deep does not fit before Wednesday.
- **Regional overlay:** None — US and Canada
- **Already collected:** A battle card last refreshed 11 months ago, and three lost-deal notes of varying quality

## Routing Recommendation

**Recommended run:** `mi-sweep-full-spectrum` at standard depth, then `mi-build-battle-card` if the QBR goes the way the user expects.

**Why this route:** The decision is a roadmap reprioritization, and the suspected capability is a build signal. Build signals live in TECHINT and HUMINT, but a single-discipline sweep would answer "are they building it" without answering "does it matter" — which needs the terrain check and the money. The full sweep also refreshes the eleven-month-old battle card as a by-product, which is the second thing that will be asked on Thursday.

**Reference files:** `sweep-playbooks.md`, `fusion.md`, `output-schemas.md`

**What this run will not answer:** *Why those three deals were actually lost.* Public signals infer that; win/loss interviews know it. The sweep will produce a build-signal story, and that story cannot rate above working hypothesis without interviews, which have not been run this cycle. The brief will say so in the verdict rather than letting a job posting reorder a roadmap.

**The wider route considered and set aside:** `mi-scan-market-landscape` first. Set aside because the user is not new to this market — they have been losing deals in it — so a landscape scan would spend Wednesday confirming what the sales team already knows.

**The narrower route considered and set aside:** `mi-collect-techint` alone. It would have answered the patent and changelog question faster, but a roadmap reprioritization argued from TECHINT alone is one discipline dressed as a case.

## Assumptions to Validate

1. **The `[CAPABILITY]` hypothesis is a single seller's recollection.** If native ERP integrations are not what they are building, the sweep will still be useful but the QBR framing collapses. This is the one to check first.
2. **`[MARKET]` codes are inferred, not filed.** If Cartelane classifies itself differently, the GEOINT/DEMOINT denominator will be built on the wrong establishment counts.
3. **Three lost deals may not be a pattern.** Three is enough to warrant a sweep and not enough to establish a trend.

## Human Decision

- **Route approved:** `mi-sweep-full-spectrum`, standard depth
- **Variables corrected by the human:** `[BUYER]` — Finance is not merely the economic buyer, it now runs the evaluation. That moves which review sites and job titles matter.
- **Approved by:** Director of Product
- **Output will be stored as:** `cartelane-full-spectrum-2026-08-18.md`

## Final Step

1. Run the full-spectrum sweep now (Recommended)
2. Narrow to TECHINT plus HUMINT and accept the thinner case
3. Schedule this as a monthly watch so the next QBR starts from a diff
4. Reframe — the real question may be why those three deals were lost, which is a win/loss program, not a sweep

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
