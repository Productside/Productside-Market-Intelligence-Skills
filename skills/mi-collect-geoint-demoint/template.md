# GEOINT/DEMOINT Collection: [MARKET]

**As-of date:** [today]
**Decision supported:** [what this changes]
**Decision horizon:** [how far forward the decision reaches — this is what "stale" is measured against]
**Prior sweep:** [date and filename, or "first run"]
**Countries in scope:** [country level; "EMEA" is not a geography]
**Web access:** [yes, researching live / no, running from training data with vintage stated]

## Code Selection (disclosed, not assumed)

| Code | System | Description | Over-captures | Under-captures |
|---|---|---|---|---|
| [code] | [NAICS / SIC / NACE / local] | [official description] | [what it includes that is not our market] | [what our market includes that it misses] |

**Why these codes:** [the analyst judgment, stated plainly]
**Overlap handling:** [how establishments counted under two codes were deduplicated]

## Search Plan

- **Sweep order:** establishment counts by code and size band → regional concentration → occupation counts and growth → wage trends → firmographic distributions → buyer-title prevalence by country → trade flows → [TARGET]'s own footprint
- **Vintage window:** [the oldest vintage acceptable given the decision horizon]
- **Noise filter:** [overlapping-code double counting; establishment versus enterprise definitions; size-band boundary differences between agencies]

## 1. Signal Inventory (fusion-ready)

Every dataset carries its vintage, not just its publication date. A 2019 count answering a 2026 question is a Fact about 2019 and an Assumption about now.

| Signal | Source (URL, published) | **Vintage** | Label | Inference chain | Feeds |
|---|---|---|---|---|---|
| [figure observed] | [URL, publication date] | [period the data describes] | [F/I/A] | [what it implies] | [TAM / ICP / Persona / Pricing / ...] |

**Stale flags:** [any dataset whose vintage predates the decision horizon, named explicitly]

## 2. The Denominator — Establishment Counts

| Country | Code | Size band | Establishments | Vintage | Source |
|---|---|---|---|---|---|
| [country] | [code] | [employee band] | [count] | [period] | [URL] |

**Denominator total (eligible shape only):** [count] — [country], vintage [period]

This is the number every bottom-up size rests on. Without it, a market size is a percentage of somebody else's headline.

## 3. Regional Concentration

| Region | Share of establishments | Vintage | Read |
|---|---|---|---|
| [region] | [%] | [period] | [where SOM lives; where field sales should live] |

## 4. The Buying Population

| Role | Country | Occupation count | Growth | Median wage | Vintage | Read |
|---|---|---|---|---|---|---|
| [buyer or end-user role] | [country] | [count] | [trend] | [figure] | [period] | [population growing or shrinking; WTP ceiling implication] |

**Wage-based pricing corridor:** [what the buying population can plausibly fund, and the assumption connecting wage to budget — labeled Assumption]

## 5. Buyer-Title Prevalence by Country

| Country | Equivalent title | Prevalence | Source | Read |
|---|---|---|---|---|
| [country] | [local title] | [count or share] | [URL] | [persona localization note; or "this role does not meaningfully exist here"] |

## 6. Firmographics and ICP Boundaries

| Dimension | Distribution | Vintage | ICP boundary it supports |
|---|---|---|---|
| Size band | [distribution] | [period] | [boundary] |
| Legal form | [distribution] | [period] | [boundary] |
| Sector | [distribution] | [period] | [boundary] |

## 7. Trade Flows (where product codes apply)

| Product code | Flow | Change | Vintage | Read |
|---|---|---|---|---|
| [code] | [origin → destination] | [%] | [period] | [market entry or supply relocation, labeled Inference] |

## 8. Conflicting Estimates

Report both. Never average them into a comfortable middle.

| Estimate | Source | Vintage | Method | Difference |
|---|---|---|---|---|
| [figure] | [analyst A] | [period] | [top-down / bottom-up / undisclosed] | — |
| [figure] | [analyst B] | [period] | [method] | [Nx] |

**What explains the gap:** [code selection, geography, definition of the category, or undisclosed method]

## 9. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 10. Collection Gaps and Handoffs

> **No signal found.** [Dataset] returned nothing on [what was sought]. Sources swept: [list]. What the absence itself suggests: [read — including the honest case that the category is too new to be counted]. What would close it: [the specific release, or "nothing until the next census"].

- **Handoffs:** the denominator → `mi-size-tam-sam-som`; capture rate → `mi-collect-finint`; everything → `mi-fuse-all-source`

## Assumptions to Validate

1. [The assumption that most changes the denominator if wrong — usually the code selection]
2. [Second]
3. [Third]

## Final Step

1. Take this denominator into sizing (Recommended)
2. Widen or narrow the code selection and re-count
3. Schedule an annual refresh, since sizing rot is slow but real
4. Turn the firmographic distribution into ICP boundaries

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
