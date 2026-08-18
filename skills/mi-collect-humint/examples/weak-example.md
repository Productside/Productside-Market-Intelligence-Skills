# Weak Example: Thirty Postings and a Verdict

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It cites real listings with dates, labels its evidence, reports sentiment with frequencies, and reaches a specific, actionable conclusion. It respects the ethical line completely — nobody was contacted. It would pass a quick review, and the roadmap was reordered on the strength of it.

Same fictional Cartelane case, swept by a different analyst.

## The Artifact

### Search Plan

- **Sweep order:** job postings → leadership → reviews
- **Date window:** last 12 months
- **Noise filter:** duplicates removed

### 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| 30 engineering roles currently open | `example.invalid/cartelane-careers`, 2026-08-15 | Fact | Aggressive engineering expansion; they are building something significant | Roadmap |
| 9 account executive roles open | same | Fact | Sales expansion underway | Threat assessment |
| VP of Partnerships departed | `example.invalid/linkedin`, 2026-06 | Fact | Leadership instability | Battle card |
| Employee reviews mention "reorg" (6 of 19) | `example.invalid/reviews`, 2026 | Fact | Internal disruption | Threat assessment |
| Reviews mention "product feels rushed" (3 of 19) | same | Fact | Quality problems | Battle card |
| Glassdoor rating 3.4 | same | Fact | Below-average employee satisfaction | Threat assessment |

### 2. Strongest Inference Chains

1. **30 engineering roles open** → Inference: a major build is underway → Roadmap: we are behind and should accelerate integration work immediately.
2. **"Product feels rushed" in reviews + 3.4 rating** → Inference: quality is their weak point → Battle card: lead with reliability.
3. **VP departure + reorg mentions** → Inference: organizational instability → Threat assessment: they will be distracted; this is our window to take deals.

### Conclusion

Cartelane is scaling fast but struggling internally. Deals are likely being lost to them on integration breadth and won by us on reliability.

## Why It Passes a Quick Read

- Real listings, real dates, real review platform, all cited.
- Evidence labels present on every row.
- Sentiment reported with frequencies (6 of 19, 3 of 19) rather than as vague impressions.
- No employee was contacted, no confidential information solicited — the ethical line is fully respected.
- The chains are ranked, tied to named artifacts, and end in specific field actions.
- The conclusion is crisp and immediately usable, which is what a busy reader rewards.

## Why It Fails

**Thirty postings with no baseline.** The number does nothing. Thirty at a company that posted twenty-eight last year is normal; thirty against three is a program. The sweep never establishes which, and then chain 1 calls it "aggressive expansion" and recommends reordering a quarter of engineering. *This is the baseline violation signal verbatim:* a count described as a surge with no comparison period.

Worse, "30 engineering roles" is the wrong unit. The correctly-run version finds 22 of them concentrated in one specialty — which is the actual signal — while support postings *contracted* from seven to two. Aggregating to "engineering" destroys both findings and replaces them with a number.

**The postings were counted and never read.** Fourteen of them name two specific ERP products by name. That single fact settles an integration-targeting question the roadmap had been arguing about for a quarter, and it is free. This document has counts and not one technology name. Counting is the easy half; the named requirements are the intelligence.

**"Duplicates removed" is unverified and probably wrong.** Thirty-one apparent listings collapse to twenty-two distinct roles once reposts and agency listings are handled. A one-line claim with no method and no before/after number is an intention, not a deduplication — and the inflated count is the foundation of chain 1.

**Chain 2 uses employee sentiment as product evidence.** "Product feels rushed," written by three employees on a review platform, is evidence about how it feels to work there. It is not evidence about the product, and a 3.4 employer rating is evidence about neither. Chain 2 then instructs the field to lead with reliability against a competitor — a claim that will be made to a customer, in public, sourced to three anonymous employee reviews. That is the violation signal exactly, and it is the line item most likely to embarrass a rep.

**The departure has no antecedent.** "VP of Partnerships departed" is reported as generic instability. What makes it a signal is *what it followed*: a partner-program announcement five months earlier. Without that, it is one of the thousands of executive moves that happen every month, and chain 3 builds a threat assessment on it.

**The stated-strategy-versus-staffing read is missing entirely.** Cartelane publicly claims its partner ecosystem is central to its integration strategy while hiring integration engineers in-house and losing the partnership VP. That contradiction is the discipline's signature output and the most decision-relevant thing available here. It leaves no empty box, so nobody notices it is gone.

**The win/loss questions and the gap flag are both absent, and the conclusion states why deals are lost.** "Deals are likely being lost to them on integration breadth and won by us on reliability" is a claim about buyer behavior derived entirely from job postings and employee reviews. Only interviews know this. With no flag raised, fusion has no way to know the sweep is uncorroborated, and chains 1 through 3 will stack as though they were three findings rather than one discipline's inferences.

## What Makes This Hard to Catch

The ethical discipline is genuinely good, and that buys credibility for everything else. Reviewers of HUMINT work brace for the elicitation failure — someone messaging an employee, someone quoting a private conversation — and finding none, they relax.

The frequencies are the second disguise. "6 of 19" and "3 of 19" look like rigor. They are precise counts of the wrong denominator: nineteen self-selected reviewers, weighted toward the recently departed, being asked a question about employment and answered as though it were a question about software.

And the conclusion is the kind of sentence people want. It is specific, it names both a threat and an advantage, and it fits on a slide. Nothing in it is supportable, and none of that is visible in its phrasing.

## Repair

Establish the baseline before counting anything, and count by specialty rather than by function. Report 22-vs-3 in integration and 2-vs-7 in support as two separate findings, and say where the baseline came from.

Read the postings. Extract the named ERP products, the named standard, and the compliance requirements, and put them in their own table — that is where this sweep's best material was sitting the whole time.

Show the deduplication: 31 listings to 22 roles, and how. Delete chain 2 and rebuild the reliability question as one for win/loss, because employee sentiment cannot answer it. Give the VP departure its antecedent, and add the stated-strategy-versus-staffing table, which will carry the run.

Then write the three to five win/loss questions tied to specific signals, raise the gap flag verbatim, and delete the conclusion. Fusion decides what is actionable; a collection sweep that renders a verdict has taken a decision it was not holding the evidence for.
