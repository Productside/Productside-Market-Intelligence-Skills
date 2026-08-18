# Weak Example: The Company That Was Definitely Collapsing

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It measures things, cites sources, uses evidence labels, and reaches a coherent story that explains every signal it found. It respects the ethical line entirely. It would pass a quick review — and its central claim went onto a battle card, where a customer contradicted it.

Same fictional Cartelane case, swept by a different analyst.

## The Artifact

### Search Plan

- **Sweep order:** support signals → status page → facilities → certifications
- **Date window:** recent
- **Noise filter:** obvious outliers removed

### 1. Signal Inventory

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| Support responses are noticeably slower than earlier this year | `example.invalid/forum`, 2026-08-15 | Fact | Support capacity is strained | Battle card |
| Support job postings dropped from 7 to 2 | `example.invalid/careers`, 2026-08-15 | Fact | They are cutting support costs | Battle card |
| 4 status-page incidents in 90 days, 2 major | `example.invalid/status`, 2026-08-18 | Fact | Reliability is degrading | Battle card |
| Community forum volume up 44% | `example.invalid/forum-stats`, 2026-08-18 | Fact | Customer frustration is rising | Threat |
| Package downloads up 31% | `example.invalid/registry`, 2026-08-18 | Fact | Roughly 31% more users, so ~14,000 total | Sizing |
| Leased two additional floors | `example.invalid/cre`, 2026-07-11 | Fact | Overextending on real estate while cutting service | Threat |

### 2. Strongest Inference Chains

1. **Slower support + fewer support hires + more incidents + more forum complaints** → Inference: Cartelane is under cash pressure and cutting service to protect margin → Battle card: lead with support quality and service commitment.
2. **Two floors leased during a cost squeeze** → Inference: poor capital discipline → Threat: they will need to raise or cut deeper within a year.
3. **Downloads up 31% → ~14,000 users** → Sizing input.

### Conclusion

Cartelane is growing on paper and deteriorating operationally. Expect service problems and pricing pressure over the next two quarters.

## Why It Passes a Quick Read

- Six real, cited signals with dates, drawn from genuinely good sources — the lease record and the posting deltas are both finds most sweeps miss.
- Evidence labels appear on every row.
- The chains are ranked and tied to named artifacts with concrete field actions.
- The story is internally coherent: every signal fits, which is exactly what a well-run investigation is supposed to produce.
- The ethical line is respected completely.

## Why It Fails

**Not one anomaly names a disambiguator, and the two central ones point opposite ways.** Support response times stretching means growth overwhelm *or* cost constraint. Support postings falling means cost cutting *or* automation. The sweep picks one reading for each — always the pessimistic one — and never names the discipline that would settle it. *This is the discipline's defining violation signal, present on every row that matters:* a single interpretation offered where two live ones exist.

The evidence inside this very document contradicts the chosen story. Forum volume up 44% is consistent with growth overwhelm, and postings down 7→2 with cost constraint. Those are the two explanations, sitting in adjacent rows, being read as one.

**Coherence was manufactured, and it is the tell.** Every signal fits the collapse narrative because each was interpreted after the narrative existed. A MASINT sweep that produces a story with no loose ends has almost certainly resolved its own ambiguity by choosing, and the discipline's whole design — the disambiguate-via column — exists to make that impossible.

**No measurement has a window, a sample, or a method.** "Noticeably slower than earlier this year" is an impression labeled Fact. The correctly-run version measures 4h → 19h across 34 threads with visible timestamps, excluding the conference fortnight when response times distort. That is a number a reviewer can contest. "Noticeably slower" is not.

**Chain 3 converts a proxy into users, silently.** Downloads up 31% becomes "~14,000 users" with no stated conversion assumption. Package downloads count machines, and a single customer's CI pipeline can move the figure. The number then enters a sizing model, where it will be treated as a measurement because it has a decimal-free precision to it.

**The status-page count has no baseline.** Four incidents in 90 days is compared to nothing — not their own history, not the category, not this company's own uptime page. It nonetheless becomes "reliability is degrading" and reaches a customer-facing card, where the customer, who reads the same status page, knows what last year looked like.

**The lease is read backwards.** Two floors leased is a **Procured** commitment — signed money — and the strongest evidence in the sweep that engineering is growing while support shrinks, which is a *targeted* reallocation rather than a general squeeze. Read as "poor capital discipline," it becomes further proof of collapse. Same record, opposite meaning, chosen to fit.

**The SOC 2 registry entry is missing entirely.** The longest-lead, least-contested signal available on this company — a twelve-to-thirty-six month runway into regulated segments — is absent, because the sweep was looking for evidence of decline and a compliance registry does not look like decline.

**"Recent" is not a window, and "obvious outliers removed" is not a filter.** Neither can be checked or reproduced.

## What Makes This Hard to Catch

The story is good. That is the problem. Reviewers assess investigations by whether the findings hang together, and these hang together perfectly — which in this discipline is evidence of interpretation, not of truth. Ambiguity is MASINT's normal state; a MASINT brief with no unresolved anomaly has usually removed the ambiguity rather than resolved it.

The sources are also genuinely strong. A commercial lease filing and a support-posting delta are sophisticated finds. Their quality lends credibility to the readings placed on top of them, and the readings are where the whole failure lives.

And the conclusion is the kind that gets forwarded. "Growing on paper, deteriorating operationally" is memorable, quotable, and fits a slide. It reached a card, and a prospect who was a happy Cartelane customer corrected a rep in a live call.

## Repair

Add the disambiguate-via column and populate it on every anomaly. For each, write two candidate explanations that point in opposite directions, state what would be true under each, and name the discipline that separates them — HUMINT sentiment for both of the central ones here. Then stop, because that is where a collection sweep ends.

Measure rather than characterize: sample size, window, method, and the periods excluded and why. Establish a baseline for the status-page count or keep it out of the chains. State the download-to-user conversion as an Assumption or, better, decline the conversion.

Re-read the lease as a commitment record and set it beside the integration hiring surge, where it argues for targeted reallocation rather than collapse. Sweep the certification registries that were skipped. And delete the conclusion — a sweep that has not disambiguated its own anomalies has not earned one.
