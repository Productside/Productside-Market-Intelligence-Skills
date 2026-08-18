# MASINT Collection: [TARGET]

**As-of date:** [today]
**Decision supported:** [what this changes]
**Prior sweep:** [date and filename, or "first run"]
**Window covered:** [date range]
**Physical goods:** [yes — full sweep / no — running the ops-capacity variant, and saying so here rather than in a footnote]
**Web access:** [yes, researching live / no, running from training data with vintage stated]

## Search Plan

- **Sweep order:** scale proxies → trend direction with windows → supply chain and trade records → facilities, permits, land, utilities → certification and notified-body registries → ops capacity → anomalies with candidate explanations
- **Date window:** [range]
- **Sampling method:** [how any measured proxy was sampled: how many observations, over what period, from where]
- **Noise filter:** [same-name entities excluded; seasonal effects noted; platform-specific biases stated]

## 1. Signal Inventory (fusion-ready)

Every anomaly names the discipline that would resolve it. A MASINT signal without a disambiguation path is a Rorschach test.

| Signal | Source (URL, date) | Label | Disambiguate via | Inference chain | Feeds |
|---|---|---|---|---|---|
| [What was measured or observed] | [URL, date] | [F/I/A] | [FININT / HUMINT / TECHINT / n/a — unambiguous] | [What it implies] | [Threat / Roadmap / Battle card / ...] |

## 2. Scale Proxies

Proxies bracket scale. They are not headcounts and not revenue. State the window and the method or the number is an impression.

| Proxy | Value | Window | Method | Trend | Platform bias to note |
|---|---|---|---|---|---|
| [review velocity / community size / downloads / integration count / app rank / forum volume] | [figure or range] | [period] | [how sampled] | [up / flat / down, with magnitude] | [what this proxy over- or under-counts] |

**Conversion assumptions:** [if any proxy is used to estimate scale, state the assumption explicitly and label it Assumption — or state that no conversion was attempted]

## 3. Anomalies and Candidate Explanations

At least two explanations per anomaly. If only one comes to mind, it is not an anomaly, it is a conclusion.

### Anomaly: [what is abnormal]

- **Observed:** [measurement, source, date]
- **Baseline:** [what normal was, and how that was established]
- **Explanation A:** [reading, and what would be true if it holds]
- **Explanation B:** [opposite reading, and what would be true if it holds]
- **Disambiguate via:** [named discipline, and the specific signal that separates A from B]
- **Which way the money would point:** [if FININT is the disambiguator, what to look for]

## 4. Facilities, Permits, and Commitment

| Record | Source (URL, date) | Lead time | Commitment level |
|---|---|---|---|
| [land, lease, permit, utility approval, EPC award, consolidation] | [URL, date] | [6-36 mo] | [Announced / Funded / Procured / Staffed / Built] |

An announced facility with no permit, lease, or utility record behind it sits at Announced. Say so.

## 5. Certifications and Regulated Entry

| Registry entry | Status | Source (URL, date) | Runway | Read |
|---|---|---|---|---|
| [ISO / SOC 2 / FedRAMP / CE / notified body / sector registry] | [held / in process / body selected] | [URL, date] | [12-36 mo] | [which regulated segment this opens] |

## 6. Ops Capacity

| Measure | Now | Prior | Window | Method | Read |
|---|---|---|---|---|---|
| [support first-response median / incident frequency / severity mix] | [figure] | [figure] | [period] | [sample size and how drawn] | [labeled Inference, with disambiguator] |

## 7. Strongest Inference Chains (max 5, ranked)

1. **[Signal cluster]** → [inference, labeled] → [artifact it should change] — *disambiguate via: [discipline]*
2. …

## 8. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 9. Collection Gaps and Handoffs

> **No signal found.** [Channel] returned nothing on [what was sought]. Sources swept: [list]. What the absence itself suggests: [read — including whether this channel can ever inform on this target]. What would close it: [the specific record or registry].

- **Handoffs:** anomaly disambiguation → `mi-collect-finint` or `mi-collect-humint`; everything → `mi-fuse-all-source`

## Assumptions to Validate

1. [The assumption that most changes the read if wrong]
2. [Second]
3. [Third]

## Final Step

1. Hand this to fusion and run FININT to disambiguate the anomalies (Recommended)
2. Re-sample the ops proxies in thirty days to establish a real trend
3. Schedule a quarterly MASINT pass so the next run is a diff
4. Turn the certification finding into a dated threat-assessment entry

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
