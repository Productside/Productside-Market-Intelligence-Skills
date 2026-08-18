# Worked Example: Two Changes, Nine Things Seen and Discarded

**Synthetic teaching case.** All companies, prices, dates, and sources below are invented for teaching. Nothing here is a claim about a real vendor.

## Run Header

~~~
As-of date:         2026-08-18
Prior run:          analytics-market-watch-2026-07-14.md
Window covered:     2026-07-14 to 2026-08-18 (35 days)
Scope:              Cartelane, Meridian, Northwind — pricing, messaging,
                    changelog, postings, filings, certifications, announcements
Sources swept:      pricing pages, Wayback snapshots (3 dates), changelogs,
                    careers pages, EDGAR, trust registries, newsrooms
Runs with no material change: 0 (prior run was also material)
Stored as:          analytics-market-watch-2026-08-18.md
~~~

## Materiality Bar Applied

**Observed but below the bar** — listed so the reader knows they were seen and judged, not missed:

- Cartelane added two customer logos to the wall
- Cartelane rewrote a hero paragraph without changing any claim
- Meridian published four blog posts (normal cadence)
- Meridian's leadership page reordered photographs
- Northwind attended two conferences
- Northwind posted one engineering role (baseline is 1-3)
- All three refreshed footer copyright years
- Cartelane's docs site changed navigation without changing content
- Meridian announced a partner integration already listed in their directory since 2024

Nine observations, none material. The two logo additions and the partner "announcement" are the ones most likely to get reported by a monitor that has stopped filtering — both look like news and neither changes what a rep would say.

## Changelog (material shifts only)

### Cartelane — entry tier removed, floor up 144%

- **Was:** "Starter — $49/user/mo, 3 connectors, 50K records/mo" — `example.invalid/cartelane-pricing`, captured 2026-07-14
- **Now:** Tier absent; page opens at Growth, $119/user/mo, 10 connectors — same URL, captured 2026-08-18
- **Read:** Packaging overhaul toward the upper mid-market. Their entire sub-$119 installed base was repriced at renewal. *Inference.*
- **Commitment level:** **Built** — the page is live; this has already happened
- **Artifact affected:** Battle card (pricing section), and a named-account campaign opportunity

### Cartelane — annual discount widened 10% to 20%

- **Was:** "Save 10% with annual billing" — same page, 2026-07-14
- **Now:** "Save 20% with annual billing" — same page, 2026-08-18
- **Read:** Cash or retention pressure, or an attempt to lock in customers ahead of the repricing. *Inference*, and the two readings point opposite ways about their health — worth a FININT check rather than a guess.
- **Commitment level:** Built
- **Artifact affected:** Battle card (pricing), deal desk guidance

## Update Flags

| Artifact | Flag | Why | Owner |
|---|---|---|---|
| Battle card: Cartelane | **Update now** | The pricing table currently says $49 entry. A rep quoting it tomorrow is quoting a price that no longer exists, to a prospect who can see the page. | Product Marketing |
| Deal desk discount guidance | **Review** | Their annual discount doubled; our standard counter may no longer hold | Sales Ops |
| Positioning brief | **Hold** | Nothing in this window touched positioning | — |
| Battle cards: Meridian, Northwind | **Hold** | No material change | — |

One "update now," and it earns it: the specific failure is a rep quoting a dead price to a buyer looking at the live page. Two "update now" flags a month would teach the field to ignore both.

## Watchlist for Next Run

| Check first | Why | Escalation trigger |
|---|---|---|
| Cartelane pricing page | Two changes in 35 days; packaging is actively in motion | Any further tier change, or "contact us" moving down another tier |
| Cartelane SOC 2 status | Listed in process since 2026-06; completion erases our certification advantage | Status flips to complete |
| Cartelane `/v2/ledger-sync/` endpoints | 11 documented, none GA; launch would move a battle card claim | Endpoints appear in the product or in release notes |
| Northwind — anything at all | Three consecutive quiet runs on a competitor that appeared in three lost deals | Any observable change; silence itself is now the signal |

The Northwind row is the one worth studying. Three quiet runs on a company we cannot characterize is not reassurance — it is a gap the watch cannot close, and naming it here is what eventually gets win/loss funded.

## Assumptions to Validate

1. **The annual-discount widening is read two ways** and this run does not resolve it. Cash pressure and pre-repricing lock-in produce the same signature; FININT would separate them.
2. **The removed Starter tier is read as segment abandonment.** It may have moved to an unlisted sales-gated offer, which the pricing page would not show.
3. **Wayback coverage is 3 snapshots in 35 days**, so messaging may have moved more than observed. The "below the bar" hero rewrite is a floor, not a total.

## Final Step

1. Update the Cartelane battle card pricing section today (Recommended)
2. Run FININT to resolve the discount-widening ambiguity
3. Keep the weekly cadence on Cartelane pricing; monthly is now too slow for them
4. Fund win/loss on Northwind — the watch cannot close that gap

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
