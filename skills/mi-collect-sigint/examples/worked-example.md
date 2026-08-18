# Worked Example: A Certificate, a Missing Tier, and a Brand Bid

**Synthetic teaching case.** Cartelane is fictional, and every price, tier name, subdomain, certificate date, and keyword below is invented for teaching. Nothing here is a claim about a real company. In a live run every capture would carry a real URL and a real capture date.

**Decision supported:** Whether to refresh the battle card now or wait for their announcement.
**Prior capture:** `cartelane-sigint-2026-05-14.md`
**Window:** 2026-05-14 to 2026-08-18.

## Search Plan

- **Sweep order:** pricing → messaging diffs via archive → docs and status page → certificates → app metadata → paid search including our brand terms → posting deltas → certifications
- **Date window:** 96 days since prior capture; archive snapshots at 2026-05-19, 2026-06-30, 2026-08-11
- **Noise filter:** the June site refresh relocated the pricing table and the footer without changing wording — treated as a redesign, not a change; excluded Cartelane Logistics entirely

## 1. Signal Inventory

| Signal | Before | After | Source (URL, capture date) | Label | Staleness | Feeds |
|---|---|---|---|---|---|---|
| Entry tier removed from pricing page | "Starter — $49/user/mo, 3 connectors" | Tier absent; page now opens at Growth | `example.invalid/cartelane-pricing`, 2026-08-18 vs 2026-05-14 | Fact | weeks | Pricing, Battle card |
| Lowest published price rose | $49/user/mo | $119/user/mo | same | Fact | weeks | Pricing, Battle card |
| Annual discount widened | 10% | 20% | same | Fact | weeks | Pricing |
| New certificate issued for `ledger.cartelane.example` | No such subdomain | Certificate issued 2026-07-02; subdomain resolves, returns a login page | `example.invalid/crt-log`, 2026-08-18 | Fact | point event | Roadmap, Battle card |
| API docs gained a `/v2/ledger-sync/` section | Absent | 11 endpoints documented | `example.invalid/cartelane-api`, 2026-08-12 vs 2026-05-14 | Fact | weeks | Roadmap |
| Paid search on two of our brand terms | No bidding observed | Bidding on both, ad copy references "migration" | `example.invalid/serp-capture`, 2026-08-16 | Fact | weeks | Battle card, Positioning |
| Homepage hero rewritten twice in the window | "Close your books faster" | "One system of record for revenue" (via "Integrated revenue operations" in June) | Archive snapshots 2026-05-19, 2026-06-30, 2026-08-11 | Fact | a quarter | Positioning |
| Case-study page added two German logos | US and UK only | US, UK, Germany | `example.invalid/cartelane-customers`, 2026-08-18 | Fact | a quarter | Threat assessment |

## 2. Baseline Captures (no prior state available)

| Item | Current state | Source (URL, capture date) | Why no prior state |
|---|---|---|---|
| Status page incident history | 4 incidents in 90 days, 2 rated major | `example.invalid/status`, 2026-08-18 | Page has no archive coverage; first reading |
| Partner directory | 31 listed partners, banner reads "not accepting new partners" | `example.invalid/partners`, 2026-08-18 | Not captured in the May run |

Both are genuinely interesting and neither is a change. Keeping them out of the inventory is what prevents "31 partners" from being read next quarter as a movement from some number nobody recorded.

## 3. Verbatim Capture — Pricing and Packaging

| Tier name | List price | Billing period | Unit | Included | Limits | Add-ons | Minimum |
|---|---|---|---|---|---|---|---|
| Growth | $119 | per user / month | seat | 10 connectors, standard support | 250K records/mo | Premium support $--- | 10 seats |
| Scale | $189 | per user / month | seat | Unlimited connectors, SSO | 2M records/mo | Sandbox $--- | 25 seats |
| Enterprise | Contact us | — | — | — | — | — | — |

- **Free tier or trial terms:** 14-day trial, no card required (unchanged)
- **"Contact us" boundary:** moved down one tier — previously only Enterprise, now Scale add-ons are unpriced
- **Page URL and capture date:** `example.invalid/cartelane-pricing`, 2026-08-18

Captured verbatim before interpretation. Next quarter's question will be more specific than this quarter's read, and only this table can answer it.

## 4. Verbatim Capture — Messaging

| Surface | Current wording | Prior wording | Rewrites in window |
|---|---|---|---|
| Homepage hero | "One system of record for revenue" | "Close your books faster" | **2** |
| Category line | "Revenue operations platform" | "Financial close software" | 1 |

Two rewrites in 96 days on the hero. That is positioning uncertainty, and it is visible only because three archive snapshots were pulled rather than one.

## 5. Strongest Inference Chains (ranked, 4 shown)

1. **New `ledger.` certificate + 11 undocumented API endpoints** → Inference: launch staging for the integration capability, running now. *Stale after: this is a point event; if no launch by 2026-Q1, the read was wrong.* → Battle card and roadmap: the decision date is before their announcement, not after.
2. **Entry tier removed + floor price up 144% + "contact us" moved down a tier** → Inference: packaging overhaul toward enterprise; they are firing the bottom of their market. *Stale after weeks.* → Battle card: an entire segment of their installed base was just repriced and is now addressable.
3. **Brand-term bidding with "migration" ad copy** → Inference: they consider us the threat, and they are targeting our installed base specifically. *Stale after weeks.* → Positioning and field response.
4. **Hero rewritten twice + category line changed** → Inference: positioning not settled. *Stale after a quarter.* → Positioning: this is the wound; the message they keep discarding is the one they cannot defend.

Chain 5 was cut. The German logos are real but chain 2 and the EMEA question belong together in fusion, not here.

## 6. Attention Signals

- **Bidding on our brand terms:** Yes — two terms, first observed 2026-08-16, ad copy references migration
- **Case-study pattern shift:** Germany appearing for the first time
- **App-store keyword changes:** No mobile listing; channel does not apply

## 7. Watch Items

- Annual discount widening from 10% to 20% — escalates if it widens again, which would read as cash or retention pressure rather than packaging
- Two major status-page incidents — no baseline, so escalates only if the next capture shows the rate holding

## 8. Collection Gaps and Handoffs

> **No signal found.** App-store metadata returned nothing. Sources swept: both major app stores under three name variants. What the absence suggests: no mobile product, which is consistent with their buyer being desk-bound finance and RevOps staff. What would close it: nothing; the channel does not apply to this target.

> **Partial coverage.** Archive snapshots exist at 96-, 49-, and 7-day intervals. The June wording is a snapshot, not continuous evidence — the hero may have changed more than twice.

- **Handoffs:** the pricing table → `mi-monitor-pricing-packaging` for a real time series; everything → `mi-fuse-all-source`, where the certificate should be paired with the TECHINT cluster

## Storage

Stored as `cartelane-sigint-2026-08-18.md`. Next run diffs against this file.

## Assumptions to Validate

1. **The `ledger.` subdomain is read as launch staging.** It could be an internal tool. It returns a login page rather than a marketing page, which is consistent with either.
2. **Two hero rewrites are counted from three snapshots.** The true count may be higher; archive coverage is not continuous.
3. **The removed Starter tier is read as segment abandonment.** It may have moved to an unlisted or sales-gated offer, which the pricing page would not show.

This sweep does not conclude that the integration launch is real. A certificate is one discipline. The TECHINT cluster and the HUMINT surge are what make it a story, and that stacking is fusion's job.

## Final Step

1. Hand this to fusion, pairing the certificate with the TECHINT cluster (Recommended)
2. Promote the pricing capture into a tracked time series
3. Set this up as a weekly watch so the next run is a diff
4. Push the pricing and brand-bidding lines into the battle card now

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
