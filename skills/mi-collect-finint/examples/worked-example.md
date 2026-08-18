# Worked Example: A Public Incumbent, Diffed

**Synthetic teaching case.** "Meridian Revenue Systems" is fictional, and every figure, filing date, and award number below is invented for teaching. Nothing here is a claim about a real company. In a live run each row would carry a checkable EDGAR or portal link.

**Decision supported:** Whether to contest three public-sector accounts Meridian currently holds, or plan around them.
**Window:** FY2023 to FY2026 filings. **Prior sweep:** first run.

## Filing Perimeter

| Item | Value |
|---|---|
| Legal entity | Meridian Revenue Systems, Inc. (Delaware) |
| Ownership | Public |
| Tickers | MRSY (Nasdaq) |
| Filing jurisdictions | US (SEC), UK subsidiary files at Companies House |
| Material subsidiaries | Meridian Revenue Systems UK Ltd; Alto Close Inc. (acquired 2024) |
| Registries swept | EDGAR, Companies House, SAM.gov, USAspending.gov |

## 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Figure type | Inference chain | Feeds |
|---|---|---|---|---|---|
| Deferred revenue grew 4% YoY against 19% revenue growth | 10-K FY2026, `example.invalid/mrsy-10k`, 2026-02-18 | Fact | Audited | Bookings are decelerating ahead of recognized revenue; the growth story is trailing, not leading | Sizing, Battle card |
| Segment reporting restructured: "Public Sector" split out from "Enterprise" for the first time | 10-K FY2026, same | Fact | Audited | A segment gets its own line when management intends to be measured on it → public sector is being promoted, not harvested | Account strategy |
| Contract modification extending an existing federal award through 2029, scope expanded to two additional agencies | `example.invalid/usaspending-award`, modification dated 2026-05-30 | Fact | Awarded contract | Locked-in account, three more years; the expansion is the tell, not the extension | Account strategy |
| CFO deflected an analyst question on public-sector gross margin twice in one call | Q3 FY2026 transcript, `example.invalid/mrsy-q3`, 2026-11-04 | Fact | Company-reported transcript | Margin in the promoted segment is a topic they have decided not to discuss | Positioning |
| Phrase "land and expand" appeared in four consecutive calls, absent in Q3 FY2026 | Transcripts Q4 FY2025 - Q3 FY2026 | Inference | Company-reported | Dropped language records a decision already made internally; expansion motion likely being retired or renamed | Positioning |
| New UK subsidiary registered, SIC codes covering data processing | `example.invalid/companies-house`, incorporated 2026-06-12 | Fact | Registry record | Market entry ahead of any announcement | Threat assessment |
| Revenue $412M, claimed "over 1,900 customers" | 10-K FY2026 and IR page, 2026-02-18 | Fact | Audited revenue, company-reported count | Implied ACV ≈ $217K | Sizing |

**Collapses applied:** The investor deck and the earnings call reciting it were logged as **one** origin, not two.

## 2. Risk Factors Diff

| Change | Risk language | Prior year | Read |
|---|---|---|---|
| **Added** | "Our results may be adversely affected by changes in government appropriations cycles and procurement policy." | Absent in FY2025 | Inference: material public-sector exposure now exists that did not before, or did not previously rise to disclosure. Corroborates the segment split. |
| **Added** | "We may be unable to retain personnel with security clearances." | Absent | Inference: they are pursuing work that requires them — a higher tier of public contract than they previously held. |
| **Removed** | Absent | "Dependence on a single cloud infrastructure provider" (FY2024, FY2025) | Inference: multi-cloud achieved, or the risk was argued down. Cheap to check via TECHINT; do not resolve it here. |
| **Reworded** | "intense competition from both established vendors and well-funded new entrants" | "intense competition from established vendors" | Inference: new entrants entered their frame this year. Worth knowing who. |

Three years were available, so this is a real diff rather than a baseline capture. Two added risks point the same direction as the segment split, which is what makes them worth more than either alone.

## 3. Strongest Inference Chains (ranked, 4 shown)

1. **Segment split + two added Risk Factors + the scope-expanding award** → Inference: a deliberate public-sector push is underway and already producing contracted revenue. *Commitment level: **Procured*** — this is not an announcement, it is a modification with a dollar figure and a date.
2. **Deferred revenue at 4% against 19% revenue growth** → Inference: bookings momentum is behind the headline. *Commitment level: n/a — this is a condition, not a move.* Feeds a battle card quarter-end pressure play, but only if the trend holds one more quarter.
3. **CFO deflecting public-sector margin, twice** → Inference: the promoted segment is being won on price. *Probe it in positioning; do not assert it.*
4. **UK subsidiary registration** → Inference: UK entry ahead of announcement. *Commitment level: **Funded*** — incorporation costs money and signals intent, but no staff, premises, or contracts corroborate it yet.

## 4. Money Versus Message

| What they say | What the money says | Gap |
|---|---|---|
| "Balanced growth across all segments" (Q3 FY2026 call) | Public Sector split out and given its own reporting line; the only scope expansion in the window is federal | **Diverging** — the reporting structure names a priority the narrative smooths over. The resources are telling the truth. |
| "Land and expand remains our motion" (through Q2 FY2026) | Phrase dropped in Q3; deferred revenue growth at 4% | **Diverging** — the motion is being quietly retired, and the deferred revenue line is consistent with that. |

## 5. Capture-Rate Inputs

- **Revenue basis:** $412M, FY2026 10-K, audited
- **Claimed customer count:** "over 1,900," IR page, company-reported — note this is *not* audited and "over" is doing work
- **Implied deal size:** $412M ÷ 1,900 ≈ **$217K ACV**, which sets a realistic ceiling on what a comparable win is worth
- **Horizon and comparable:** 3-5 years, benchmarked against two named comparables in the same category at similar revenue scale
- **What this does not establish:** how many such customers exist. That denominator is GEOINT/DEMOINT's, and using this ACV without it produces a SOM with no market underneath it.

## 6. Watch Items

- Removed cloud-dependency risk — escalates if TECHINT finds no multi-cloud evidence, which would mean the risk was argued away rather than resolved
- New-entrant language in the competition risk — escalates when the entrants can be named

## 7. Collection Gaps and Handoffs

> **No signal found.** Competition and state-aid cases returned nothing. Sources swept: EC merger and antitrust databases, US DOJ and FTC actions. What the absence suggests: no regulatory friction at their current scale, which also means no merger filing exists to tell us how *their lawyers* define this market — a genuinely useful document we do not have. What would close it: any future filing; nothing available today.

> **Thin, not empty.** The UK subsidiary has filed no accounts yet — incorporated too recently. Revisit in twelve months.

- **Handoffs:** ACV → `mi-size-tam-sam-som`; dropped language and margin deflection → `mi-refresh-earnings-signals` quarterly; everything → `mi-fuse-all-source`

## Assumptions to Validate

1. **"Over 1,900 customers" is company-reported and unaudited.** If it counts free-tier or multi-entity accounts, the ACV is overstated and every downstream sizing number moves with it. This is the assumption most likely to be wrong and most likely to be repeated.
2. **The dropped "land and expand" phrase is read as a retired motion.** One absent quarter is thin; two would establish it.
3. **Deferred revenue deceleration is read as booking softness.** A billing-terms change produces the same signature. The Q4 filing settles it.

This sweep does not conclude that Meridian is in trouble, or that the public-sector accounts are uncontestable. It establishes that one story sits at **Procured** and another at **Funded**, and hands both to fusion.

## Final Step

1. Hand this inventory to all-source fusion, with HUMINT next on the clearance-hiring question (Recommended)
2. Take the $217K ACV into sizing, paired with a GEOINT denominator
3. Schedule a quarterly earnings and executive signal refresh
4. Turn the money-versus-message gap into positioning input

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
