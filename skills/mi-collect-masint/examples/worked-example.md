# Worked Example: Two Anomalies, Four Explanations

**Synthetic teaching case.** Cartelane is fictional, and every measurement, registry entry, incident count, and download figure below is invented for teaching. Nothing here is a claim about a real company. In a live run each row would carry a real record and a real capture date.

**Decision supported:** Is Cartelane's operational strain real enough to put on a battle card?
**Physical goods:** No. Running the ops-capacity variant, stated here rather than buried at the end.
**Window:** 2026-05-18 to 2026-08-18. **Prior sweep:** first run.

## Search Plan

- **Sweep order:** scale proxies → trend with windows → *(supply chain skipped, no physical goods — see gaps)* → facilities and leases → certification registries → ops capacity → anomalies
- **Date window:** 90 days
- **Sampling method:** support first-response measured from 34 publicly visible community-forum threads where a vendor employee replied and both timestamps were visible; status-page incidents counted from the published history
- **Noise filter:** August sampling excludes the two-week period around a major industry conference, when response times distort in both directions; Cartelane Logistics excluded by name

## 1. Signal Inventory

| Signal | Source (URL, date) | Label | Disambiguate via | Inference chain | Feeds |
|---|---|---|---|---|---|
| Support first-response median moved from 4h to 19h | `example.invalid/forum-sample`, sampled 2026-08-15 | Inference (measured proxy, not their SLA) | HUMINT sentiment | Cash constraint or growth overwhelm — two opposite stories, one signature | Battle card, Threat |
| Support job postings fell from 7 to 2 | `example.invalid/careers`, 2026-08-15 | Fact | HUMINT | Cost compression or automation | Threat |
| Status-page incidents: 4 in 90 days, 2 rated major | `example.invalid/status`, 2026-08-18 | Fact | n/a — but no baseline exists | Capacity strain, *unestablished without a prior period* | Watch |
| SOC 2 Type II listed as "in process" with a named auditor | `example.invalid/trust-registry`, 2026-06-04 | Fact | n/a — unambiguous | 12-36 month runway into regulated segments they do not currently sell into | Threat, Roadmap |
| Office lease filed for 2 additional floors, same building | `example.invalid/cre-record`, 2026-07-11 | Fact | FININT | Headcount growth committed with real money — Procured, not Announced | Threat |
| Package downloads up 31% over 90 days | `example.invalid/registry-stats`, 2026-08-18 | Fact | n/a | Adoption or CI churn; see conversion note | Sizing (weakly) |
| Community forum post volume up 44% | `example.invalid/forum-stats`, 2026-08-18 | Fact | HUMINT | Growth or trouble — volume alone does not say which | Watch |

## 2. Scale Proxies

| Proxy | Value | Window | Method | Trend | Platform bias to note |
|---|---|---|---|---|---|
| Package downloads | 31% increase | 90 days | Public registry statistics | Up | Counts CI pipeline pulls, not users; a single customer's build system can move this |
| Community forum posts | 44% increase | 90 days | Public post counts | Up | Rises with both adoption and dissatisfaction |
| Public integration count | 31 → 33 | 90 days | Their own directory | Flat | Self-reported; the directory now says "not accepting new partners" |
| App store rank | n/a | — | — | — | No mobile product; channel does not apply |

**Conversion assumptions:** None attempted. Downloads were not converted into users, and forum volume was not converted into customer count. Both conversions are available and both would be Assumptions dressed as measurements — the download figure in particular counts machines, not people.

## 3. Anomalies and Candidate Explanations

### Anomaly: support first-response median nearly 5x in 90 days

- **Observed:** 4h → 19h median, 34-thread sample, 2026-05 to 2026-08
- **Baseline:** the May figure from the same forum, same method. Established, not assumed.
- **Explanation A — growth overwhelm:** volume arrived faster than staffing. If so, forum volume should be up (it is, 44%), sentiment should mention workload, and support hiring should be *rising*.
- **Explanation B — cash or cost constraint:** support was deliberately shrunk. If so, support postings should be *falling* (they are, 7 → 2), sentiment should mention cost discipline or a freeze, and other cost signals should appear.
- **Disambiguate via:** HUMINT employee sentiment. The postings evidence currently points to B, and the forum-volume evidence to A. **They point opposite ways and this sweep does not resolve it.**
- **Which way the money would point:** if FININT shows margin-defense language or a widening annual discount, B strengthens.

Naming both explanations is the entire value here. A sweep that picked one would be 50% likely to put a false claim on a customer-facing card.

### Anomaly: two additional floors leased during an apparent cost squeeze

- **Observed:** lease filed 2026-07-11, two floors, same building
- **Baseline:** prior footprint, one floor
- **Explanation A — the squeeze is targeted, not general:** support is being cut while engineering grows. Consistent with the 22-vs-3 integration hiring surge found separately.
- **Explanation B — the lease predates a decision that has since changed:** commercial leases are signed months ahead of occupancy.
- **Disambiguate via:** FININT (capex and commitment language) and HUMINT (which functions are actually growing).
- Explanation A currently looks stronger, and "currently looks stronger" is as far as a collection sweep may go.

## 4. Facilities, Permits, and Commitment

| Record | Source (URL, date) | Lead time | Commitment level |
|---|---|---|---|
| Two-floor lease expansion | `example.invalid/cre-record`, 2026-07-11 | 6-12 mo to occupancy | **Procured** — a signed lease is money, not intent |

## 5. Certifications and Regulated Entry

| Registry entry | Status | Source (URL, date) | Runway | Read |
|---|---|---|---|---|
| SOC 2 Type II | In process, auditor named | `example.invalid/trust-registry`, 2026-06-04 | 12-18 mo | Opens regulated buyers they do not sell to today. This is the longest-lead signal in the sweep and the one nobody would have found in the press. |

## 6. Ops Capacity

| Measure | Now | Prior | Window | Method | Read |
|---|---|---|---|---|---|
| Support first response (median) | 19h | 4h | 2026-05 to 2026-08 | 34 public forum threads, both timestamps visible, conference fortnight excluded | Inference: material degradation. Disambiguator: HUMINT. |
| Status incidents | 4 (2 major) | Unknown | 90 days | Published history | **No baseline.** Logged as a first reading, not as a trend. |

## 7. Strongest Inference Chains (ranked, 3 shown)

1. **Response time 5x + support postings down 7→2** → Inference: support capacity has been reduced or outstripped. *Disambiguate via HUMINT sentiment before this touches a card.*
2. **SOC 2 in process + two-floor lease** → Inference: they are investing to enter regulated segments. *Commitment: Procured. Lead time 12-18 months.* → Threat assessment with a date.
3. **Downloads +31% + forum volume +44% + integrations flat** → Inference: usage is growing faster than the ecosystem around it. *Weak; both proxies are ambiguous by construction.*

Only three chains. There were not five worth writing, and padding to five is how a sweep starts inventing.

## 8. Watch Items

- Status-page incident rate — escalates once a second reading establishes whether 4-in-90 is normal for them
- Forum volume — escalates if it keeps climbing while response times stay stretched

## 9. Collection Gaps and Handoffs

> **No signal found — and this channel never will.** Supply chain, import/export, trade codes, and country-of-origin records returned nothing. Sources swept: UN Comtrade, import-record aggregators under three name variants. What the absence suggests: Cartelane ships no physical goods, so this half of the discipline is permanently unavailable for this target. The ops-capacity substitute above is thinner and more ambiguous, and every read built on it should be weighted accordingly. What would close it: nothing.

> **No baseline.** Status-page history has no prior reading. The incident count is a first measurement, not a trend, and it is kept out of the inference chains for that reason.

- **Handoffs:** both anomalies → `mi-collect-humint` for sentiment, then `mi-collect-finint` for the money read; everything → `mi-fuse-all-source`

## Assumptions to Validate

1. **The response-time proxy measures public forum replies, not their contracted SLA.** Enterprise customers may have entirely different experience. This is the assumption most likely to make the battle card wrong.
2. **The 34-thread sample is small.** It is enough to notice a 5x move and not enough to characterize the distribution.
3. **Downloads are treated as adoption.** A single customer's CI pipeline could produce the entire 31%.

This sweep does not conclude that Cartelane is in trouble. It found two anomalies, gave each two live explanations, and named who resolves them.

## Final Step

1. Hand this to fusion and run HUMINT sentiment to disambiguate both anomalies (Recommended)
2. Re-sample response times in thirty days to establish whether the trend holds
3. Schedule a quarterly MASINT pass so the next run is a diff
4. Turn the SOC 2 finding into a dated threat-assessment entry

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
