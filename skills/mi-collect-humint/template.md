# HUMINT Collection: [TARGET]

**As-of date:** [today]
**Decision supported:** [what this changes]
**Prior sweep:** [date and filename, or "first run"]
**Window covered:** [date range]
**Win/loss status:** [run this cycle, date / unverified as of this run]
**Web access:** [yes, researching live / no, running from training data with vintage stated]

## Search Plan

- **Sweep order:** leadership roster and prior playbooks → open roles by function and geography, against a baseline → departures and tenure concentration → sentiment themes → public statements → our own win/loss and churn debriefs
- **Date window:** [range]
- **Noise filter:** [reposted roles deduplicated by title and location; contractor and agency listings separated; same-name companies excluded by name]

## Baseline

State what normal looks like before counting anything. A count with no denominator manufactures alarm.

| Function | Postings now | Baseline | Baseline source | Read |
|---|---|---|---|---|
| [specialty] | [count] | [count in comparison period] | [prior-year listings / adjacent function / careers page archive] | [surge / normal / contraction / no baseline available — observation only] |

## 1. Signal Inventory (fusion-ready)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [What it implies] | [Roadmap / Battle card / Threat / ...] |

**Deduplication applied:** [how many apparent postings collapsed to how many roles]

## 2. What the Postings Actually Say

Counting is the easy half. The named requirements are the intelligence.

| Named in postings | Where | Read |
|---|---|---|
| [technology, ERP, compliance regime, region, segment] | [role title, count] | [confirmed stack choice / integration target / market entry / regulated segment] |

## 3. Leadership and Departures

| Person or role | Event | Date | What it followed | Read |
|---|---|---|---|---|
| [role] | [joined / departed / changed scope] | [date] | [the announcement or event it came after] | [labeled Inference] |

- **Tenure concentration:** [how many of the senior team changed in how many quarters]
- **Prior playbooks:** [what this leadership did at their last company, and whether they are repeating it]

## 4. Sentiment Themes

Directional only. Evidence about the organization, never about the product.

| Theme | Frequency | Source and window | Read |
|---|---|---|---|
| [pivot / reorg / leadership churn / growth strain] | [recurring / concentrated / isolated] | [platform, date range] | [estimated duration of internal distraction] |

## 5. Stated Strategy Versus Staffing

| What leadership says | Who they are actually hiring | Gap |
|---|---|---|
| [claim, with source] | [functions and counts] | [aligned / diverging — and the payroll is the truthful one] |

## 6. Strongest Inference Chains (max 5, ranked)

1. **[Signal cluster]** → [inference, labeled] → [artifact it should change, and the move]
2. …

## 7. Win/Loss Questions for the Next Round

Required output. Three to five questions, each tied to a specific signal above. These are what convert public inference into ground truth.

1. [Question] — *tests: [the signal it would confirm or refute]*
2. [Question] — *tests: [signal]*
3. [Question] — *tests: [signal]*

## 8. The Gap Flag

> **Gap flag for fusion:** win/loss unverified as of this run. Weight org-instability and build-signal stories accordingly.

If interviews were run this cycle, replace with: *Win/loss current as of [date]. Where these interviews and this sweep disagree, the interviews win.*

## 9. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 10. Collection Gaps and Handoffs

> **No signal found.** [Channel] returned nothing on [what was sought]. Sources swept: [list]. What the absence itself suggests: [read]. What would close it: [the specific source].

- **Fusion pairing flag:** a hiring surge next to a TECHINT patent or paper cluster in the same specialty is the strongest pair available. Run `mi-collect-techint` if it has not been run.

## Assumptions to Validate

1. [The assumption that most changes the read if wrong]
2. [Second]
3. [Third]

## Final Step

1. Hand this to fusion with the win/loss flag attached (Recommended)
2. Pair it with a TECHINT sweep on the same specialty
3. Schedule a monthly HUMINT digest so the next run is a diff
4. Take the win/loss questions into the next interview round

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
