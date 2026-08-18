# FININT Collection: [TARGET]

**As-of date:** [today]
**Decision supported:** [what this changes]
**Prior sweep:** [date and filename, or "first run"]
**Window covered:** [date range]
**Filing posture:** [public, files in X jurisdictions / private, incorporation records only / PE-held / state-linked]
**Web access:** [yes, researching live / no, running from training data with vintage stated]

## Search Plan

- **Sweep order:** annual and quarterly filings (Risk Factors first, diffed) → segment reporting → earnings Q&A dodges → funding, debt, ownership → entity and subsidiary registrations in [GEOGRAPHY] → procurement awards and modifications → competition and state-aid cases
- **Date window:** [range; three years for Risk Factors diffing]
- **Noise filter:** [same-name entities excluded by name; acquisitions already closed; announced budgets separated from awarded contracts]

## Filing Perimeter

| Item | Value |
|---|---|
| Legal entity and trading names | [names] |
| Ownership status | [public / private / PE-held / subsidiary / state-linked] |
| Tickers and exchanges | [list, or "none"] |
| Filing jurisdictions | [list] |
| Material subsidiaries | [list] |
| Registries swept | [EDGAR / Companies House / BRIS / national portal] |

## 1. Signal Inventory (fusion-ready)

One observation per row. Every figure carries its source and date.

| Signal | Source (URL, date) | Label | Figure type | Inference chain | Feeds |
|---|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [audited / company-reported / third-party estimate / announced budget / awarded contract] | [What it implies] | [Sizing / Battle card / Positioning / ...] |

**Collapses applied:** [rows merged because an investor deck and the call reciting it are one origin]

## 2. Risk Factors Diff

| Change | Risk language | Prior year | Read |
|---|---|---|---|
| **Added** | [new risk, quoted briefly with citation] | absent | [what changed inside the building, labeled Inference] |
| **Removed** | absent | [prior language with citation] | [what they argued away] |
| **Reworded** | [now] | [was] | [direction of the shift] |

Quoting the section is not diffing it. If only one year is available, say so and log this as a baseline capture.

## 3. Strongest Inference Chains (max 5, ranked)

1. **[Signal cluster]** → [inference, labeled] → [artifact it should change, and the move] — *commitment level: [Announced / Funded / Procured / Staffed / Built]*
2. …

## 4. Money Versus Message

| What they say | What the money says | Gap |
|---|---|---|
| [stated strategy, with source] | [capital allocation, award, or filing language, with source] | [aligned / diverging — and which one the resources support] |

When messaging and resource allocation disagree, the resources are telling the truth.

## 5. Capture-Rate Inputs (if sizing is downstream)

- **Revenue basis:** [figure, source, date, and whether audited]
- **Claimed customer count:** [figure, source, date]
- **Implied deal size:** [arithmetic shown]
- **Horizon and comparable:** [3-5 years, benchmarked against named companies]
- **What this does not establish:** [the market's size — that is the GEOINT/DEMOINT denominator]

## 6. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 7. Collection Gaps and Handoffs

> **No signal found.** [Channel] returned nothing on [what was sought]. Sources swept: [list]. What the absence itself suggests: [read]. What would close it: [the specific filing, registry, or paid source].

- **Handoffs:** capture rate → `mi-size-tam-sam-som`; executive language shifts → `mi-refresh-earnings-signals`; everything → `mi-fuse-all-source`

## Assumptions to Validate

1. [The assumption that most changes the read if wrong]
2. [Second]
3. [Third]

## Final Step

1. Hand this inventory to all-source fusion (Recommended)
2. Take the capture rate and deal-size read into sizing
3. Schedule a quarterly earnings and executive signal refresh
4. Turn the money-versus-message gap into positioning input

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
