# Worked Example: The Price Held and the Limit Halved

**Synthetic teaching case.** All companies, prices, limits, and dates below are invented for teaching. Nothing here is a claim about a real vendor's pricing.

## Run Header

~~~
As-of date:      2026-08-18
Prior capture:   cartelane-meridian-pricing-2026-05-14.md
Window:          96 days
Competitors:     Cartelane, Meridian
Capture URLs:    example.invalid/cartelane-pricing,
                 example.invalid/meridian-pricing
Runs with no change: 0
Stored as:       cartelane-meridian-pricing-2026-08-18.md
~~~

## Verbatim Capture — Cartelane

**Captured from:** `example.invalid/cartelane-pricing` on 2026-08-18.

| Tier name | List price | Billing period | Unit | Included | Limits | Add-ons | Minimum | Overage |
|---|---|---|---|---|---|---|---|---|
| Growth | $119 | per user / month | seat | "10 connectors, standard support, standard reporting" | "250,000 records / month" | "Premium support — contact us" | 10 seats | "$0.004 per additional record" |
| Scale | $189 | per user / month | seat | "Unlimited connectors, SSO, advanced reporting, sandbox" | "2,000,000 records / month" | "Dedicated environment — contact us" | 25 seats | "$0.003 per additional record" |
| Enterprise | "Contact us" | not published | not published | not published | not published | not published | not published | not published |

- **Free tier or trial terms:** "14-day trial, no credit card required"
- **Published discounts:** "Save 20% with annual billing"
- **"Contact us" boundary:** Enterprise entirely, plus add-ons at both published tiers
- **Regional notes:** USD only; page does not vary by geography

## Verbatim Capture — Meridian

| Tier name | List price | Billing period | Unit | Included | Limits | Add-ons | Minimum | Overage |
|---|---|---|---|---|---|---|---|---|
| — | "Contact us" | not published | not published | not published | not published | not published | not published | not published |

- **"Contact us" boundary:** everything. Meridian publishes no pricing at all.
- Recording this rather than skipping Meridian matters: "not published" on 2026-05-14 and again on 2026-08-18 establishes that their posture is *stable*, which is itself a data point in a series.

## Delta Against Prior Capture

| Competitor | Field | Was | Now | Interval |
|---|---|---|---|---|
| Cartelane | Tier: Starter | "Starter — $49/user/month, 3 connectors, 50,000 records/month, 5-seat minimum" (2026-05-14) | **Absent** (2026-08-18) | 96 days |
| Cartelane | Lowest published price | $49 (2026-05-14) | $119 (2026-08-18) | 96 days |
| Cartelane | Growth: included connectors | "5 connectors" (2026-05-14) | "10 connectors" (2026-08-18) | 96 days |
| Cartelane | **Growth: record limit** | **"500,000 records / month"** (2026-05-14) | **"250,000 records / month"** (2026-08-18) | 96 days |
| Cartelane | Annual discount | "Save 10% with annual billing" (2026-05-14) | "Save 20% with annual billing" (2026-08-18) | 96 days |
| Cartelane | Premium support | "$29/user/month" (2026-05-14) | "Contact us" (2026-08-18) | 96 days |
| Meridian | *(all fields)* | not published | not published | 96 days — **no change** |

**The fourth row is the one that matters most and would have been missed by anyone tracking headline prices.** Growth held at $119 while its record limit was cut in half. Doubling the connector count is the visible half of that trade; halving the throughput is the invisible half, and for a customer at 400,000 records a month it is a forced upgrade to Scale — a 59% increase disguised as a feature improvement.

Nothing in a "pricing simplified, more connectors included" note would have preserved this. It is only visible because the limits column existed in the prior capture.

## Packaging Signals

| Signal | Present? | Evidence from the capture | Read |
|---|---|---|---|
| A tier disappeared | **Yes** | Starter removed | Packaging overhaul toward the upper mid-market *(source doctrine)* |
| A feature moved up a tier | **Yes** | Throughput above 250K records now requires Scale | Monetizing what was previously included *(source doctrine)* |
| Usage pricing added alongside seats | No | Overage existed in both captures | — |
| "Contact us" replacing a published price | **Yes** | Premium support went from $29 to unpriced | Discount flexibility wanted, or an increase tested quietly *(working read)* |
| A new floor or minimum | **Yes** | Effective floor $49 → $119; seat minimum 5 → 10 | Firing the bottom of the market *(working read)* |
| Annual discount widening | **Yes** | 10% → 20% | Cash or retention pressure *(working read)* |

Five of six present, and that is unusual — this is a genuine repackaging, not a routine adjustment. In most runs two or three rows read "No," and leaving them empty is what keeps the tracker from becoming a horoscope.

## Ambiguous Reads

| Change | Explanation A | Explanation B | Disambiguate via |
|---|---|---|---|
| Annual discount 10% → 20% | Cash or retention pressure — they need committed revenue | A retention play ahead of the repricing, locking customers in before the increase bites | **FININT** — margin language and deferred revenue in the next filing |
| Premium support to "contact us" | Testing a higher price quietly | Bundling it into Scale and retiring it as a line item | **Next capture** — if it reappears inside Scale's inclusions, it was B |

Two changes, four explanations, none chosen. The first pair point in opposite directions about Cartelane's health, and picking the pessimistic one would have put an unsupported claim on a battle card.

## Update Flags

| Artifact | Flag | Why | Owner |
|---|---|---|---|
| Battle card: Cartelane | **Update now** | The card's pricing table still shows the $49 Starter tier. A rep quoting it is quoting a tier that no longer exists to a buyer looking at the live page. | Product Marketing |
| Deal desk guidance | **Review** | Their annual discount doubled; our standard annual counter may no longer hold | Sales Ops |
| Named-account campaign | **Review** | Their sub-$119 base was repriced and is now addressable — the throughput cut widens that population beyond just the Starter customers | Demand Gen |
| Battle card: Meridian | Hold | No change; "contact us" posture stable across two captures | — |

## Final Step

1. Update the Cartelane battle card pricing table today (Recommended)
2. Run FININT on the next filing to resolve the annual-discount ambiguity
3. Move Cartelane to weekly capture — two structural changes in one quarter
4. Build the named-account list from the repriced population

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
