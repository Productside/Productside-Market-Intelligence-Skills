# Worked Example: A Cluster, a Clock, and a Deprecation

**Synthetic teaching case.** Cartelane is fictional, and every patent count, classification, date, and endpoint name below is invented for teaching. Nothing here is a claim about a real company or a real filing. In a live run each row would carry a checkable registry link.

**Decision supported:** Accelerate or concede our own ERP integration work this quarter.
**Suspected capability:** Native ERP connectors replacing their partner-built ones.
**Window:** 24 months for patents, 12 for changelogs. **Prior sweep:** first run.

## Assignee Perimeter

| Name filed under | Relationship | Why included |
|---|---|---|
| Cartelane, Inc. | Primary | Obvious |
| Flowbridge Systems LLC | Acquired 2023, still the assignee of record on new filings | **The cluster is here, not under Cartelane** |
| Cartelane Logistics | Unrelated Ontario freight brokerage | Excluded by name |

Sweeping only the trading name would have returned two filings and a conclusion of "no meaningful R&D activity." The acquired entity holds nine.

## 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Lead time | Inference chain | Feeds |
|---|---|---|---|---|---|
| 9 published applications under Flowbridge Systems in one classification covering record reconciliation across heterogeneous ledgers | `example.invalid/patents-flowbridge`, filings dated 2025-03 to 2026-01 | Fact | 12-18 mo | Cluster = committed bet, not exploration; earliest filings mature H2 2026 | Roadmap |
| Same three inventor names on 7 of the 9 | same | Fact | — | A dedicated team exists; this is a program with staff, not a defensive filing | Roadmap |
| Two of those three list a prior affiliation at a university lab publishing on ledger reconciliation | `example.invalid/scholar-profile`, 2024-2026 | Inference | 6-24 mo | Affiliation shift = they hired the lab, not just the idea | Roadmap |
| Trademark application for "Cartelane Bridge," goods and services covering data integration software | `example.invalid/tm-register`, filed 2026-06-22 | Fact | 6-12 mo | Trademarks are cheap and filed near launch → announcement window Q4 2026 to Q2 2027 | Battle card |
| API docs added 11 endpoints under `/v2/ledger-sync/`, absent from the product UI and unmentioned in release notes | `example.invalid/cartelane-api`, diffed 2026-05-14 vs 2026-08-12 | Fact | weeks | Beta program running now | Roadmap, Battle card |
| Public SDK repo gained a connector scaffolding package, 40+ commits in 8 weeks | `example.invalid/repo`, 2026-06 to 2026-08 | Fact | weeks-months | Developer platform play, third-party connectors intended | Roadmap |
| Participation in a ledger-interchange standards working group, one seat, not chairing | `example.invalid/standards-wg`, roster 2026-04 | Fact | 12-48 mo | Present but not shaping; they intend to comply, not to write the rules | Watch |
| Deprecation notice: partner-connector program marked "maintenance only," no new partners accepted | `example.invalid/partner-docs`, 2026-07-01 | Fact | now | They are giving up on partner-built connectors — the strategy this cluster replaces | Battle card |

## 2. Classification Clusters

| Classification | Filings in window | Window | Read |
|---|---|---|---|
| Record reconciliation across heterogeneous ledgers | 9 | 24 months ending 2026-01 | **Committed bet.** Nine filings under a single assignee in one classification is not accidental; prosecution costs are real. |
| Report generation and formatting | 2 | same | Not a cluster. Logged, not read. |

## 3. The People Behind It

- **Repeating inventors:** three names on 7 of 9 filings
- **Where they came from:** two shifted affiliation from a university lab to Flowbridge across successive papers in 2024. They hired the lab.
- **What they say in public:** one gave a conference talk in March 2026 on reconciliation without canonical schemas — which describes the approach the filings claim

## 4. Built Versus Shipped

| Under construction | Buyable today | Read |
|---|---|---|
| Native ledger-sync integration layer, 11 endpoints live in docs | Absent from the product; partner connectors only | **Countdown clock.** Shortest signal is the API diff (weeks); tightest dated signal is the trademark. Decision date: **2026-Q4**, before their announcement window opens. |

### Deprecations

| Removed or sunset | Source (URL, date) | Read |
|---|---|---|
| Partner-connector program → "maintenance only," closed to new partners | `example.invalid/partner-docs`, 2026-07-01 | They have given up on the partner model. This is the strongest single signal in the sweep and it is the one nobody would have announced. It also strands their existing connector partners — a displacement angle. |

The deprecation is what converts this from "they are building something" to "they are replacing something." Half the sweeps that find the cluster miss this table entirely.

## 5. Strongest Inference Chains (ranked, 4 shown)

1. **9-filing cluster + 3 repeating inventors + partner-program deprecation** → Inference: native integration is a committed program replacing the partner model, staffed by a team they acquired. *Lead time 12-18 months from earliest filings → decision date **2026-Q4**.*
2. **11 undocumented API endpoints + SDK scaffolding commits** → Inference: beta running now. *Lead time: weeks. This is the shortest clock in the set and therefore the one that sets the deadline.*
3. **"Cartelane Bridge" trademark** → Inference: launch name chosen. *6-12 months → announcement window Q4 2026 to Q2 2027.*
4. **Standards seat without a chair** → Inference: they intend to comply, not to shape. *Long horizon, low urgency.* Logged, not acted on.

## 6. Watch Items

- Second classification (report generation, 2 filings) — escalates at 5 filings in 12 months
- Standards seat — escalates if they take a chair or editorship

## 7. Collection Gaps and Handoffs

> **No signal found.** Funded research consortia returned nothing. Sources swept: CORDIS, Horizon Europe participant database, NSF award search. What the absence suggests: this program is privately funded, which is consistent with an acquisition-plus-hire strategy rather than a long-horizon research bet. What would close it: nothing further; the channel does not apply.

> **Fusion pairing flag.** This sweep establishes intent to build and evidence of a team. Whether the bet is *staffed at scale* is a HUMINT question. The strongest available corroboration — a hiring surge in the same specialty — has not been checked. Run `mi-collect-humint` before any story here is rated above working hypothesis.

## Assumptions to Validate

1. **The nine filings are published applications, not grants.** Applications are far more common and far less committal. If several were abandoned, the cluster weakens considerably — and abandonment is checkable.
2. **The `/v2/ledger-sync/` endpoints are read as a live beta.** They could be internal scaffolding exposed by accident. A closed beta would have named customers somewhere.
3. **The partner deprecation is read as replacement.** It could be cost-cutting unrelated to the cluster. The timing argues against, but timing is not causation.

This sweep does not conclude that Cartelane will win the integration category. One discipline, however well corroborated internally, is still one discipline.

## Final Step

1. Hand this to fusion and run HUMINT next to test whether the bet is staffed (Recommended)
2. Go deeper on the nine-filing cluster: grant status, claims, and abandonment
3. Schedule a quarterly TECHINT pass so the next run is a diff
4. Set the 2026-Q4 accelerate-or-concede decision date on the roadmap now

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
