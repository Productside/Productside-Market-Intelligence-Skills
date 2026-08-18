# Weak Example: The Roadmap That Chased One Angry Reviewer

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It reviews a real corpus, quotes customers, counts mentions, clusters themes, and ends with clear priorities. It is more rigorous than most VoC work. It would pass a quick review, and its top theme reached a roadmap discussion.

Same fictional Cartelane case, mined by a different analyst.

## The Artifact

### Sources

134 posts reviewed across the review platform, Cartelane's community forum, and a public RevOps forum. Twelve months.

### Top Customer Themes

| # | Theme | Mentions | Representative quote |
|---|---|---|---|
| 1 | Needs field-level audit logging | 9 | "We need proper audit trails. Screenshots aren't good enough when the auditors come." |
| 2 | Wants Slack alerting on sync failures | 12 | "Just tell me in Slack when it breaks." |
| 3 | Needs bulk CSV export | 11 | "Export everything, let me work in Excel." |
| 4 | Connector reliability issues | 22 | "Sync problems again." |
| 5 | Support response times | 8 | "Slow to respond." |

### Competitor Weak Points

Cartelane's biggest weakness is connector reliability, mentioned 22 times. Support responsiveness is a secondary weakness.

### Recommendations

1. Prioritize field-level audit logging — this is a clear unmet need with strong customer demand.
2. Add Slack alerting.
3. Lead with reliability in competitive positioning.

## Why It Passes a Quick Read

- A real corpus of 134 posts across three genuinely different platforms.
- Themes are counted, which most VoC work does not bother to do.
- Every theme carries a quote, so it reads as grounded in customer language.
- The corpus spans twelve months rather than a snapshot.
- Recommendations are specific and immediately actionable.
- Nothing is obviously fabricated.

## Why It Fails

**Every theme is a feature request.** "Needs field-level audit logging," "wants Slack alerting," "needs bulk CSV export" — three solutions, zero needs. *This is the solution-free violation signal three times over.* The jobs underneath are: prove the number to someone who does not trust it; find out a connector broke before close rather than during it; reconcile by hand when the tool cannot. Building all three requested features produces a tool with logs, alerts, and exports that still cannot tell an analyst which system to trust — which is the actual recurring theme, and it appears nowhere in this document.

**Mentions were counted; sources were not.** 22 mentions of connector reliability sounds decisive. The correctly-run version counts *independent posters*, and the picture changes: 14 of 31 on the review platform, plus corroboration in the loyal community forum. Meanwhile theme 1's "9 mentions" collapses to **two posts by one person on one platform**. It is ranked first, and it was ranked first because the quote is the most compelling sentence in the corpus.

*This is the frequency violation signal exactly:* themes ordered by how compelling the quote was. And it worked — it reached a roadmap discussion as a priority.

**No frequency labels at all.** Nothing distinguishes recurring-across-sources from concentrated-in-one from isolated. A raw count cannot make that distinction, because twelve posts by four people in one forum produces a larger number than six posts by six people across three platforms — while being much weaker evidence.

**Source skew is never stated, and one source is systematically misread.** Cartelane's own community forum skews loyal: the unhappy have already left, so complaints there are *understated* and therefore more significant per mention. This document weights all three platforms identically and, by pooling counts, lets the largest corpus dominate — which happens to be the vendor's own forum.

**The quotes are suspiciously clean.** "We need proper audit trails. Screenshots aren't good enough when the auditors come." reads like a product requirement, not like a person typing on a review site. No platform, no date, and prose that matches the report's own register. Whether composed outright or tidied into shape, it fails the same test: a quote that cannot be located is not evidence, and quotes are precisely what gets pasted into a slide and read aloud.

**There are no switching triggers.** Not one. The document has a complaints section and nothing naming what actually made anyone leave. The correctly-run version finds four — a failed audit, a bad quarter-close at renewal, a price increase, and an analyst departure that brings customers *in* — and they reframe everything. The most-complained-about thing turns out not to be the thing that makes people leave, which is the single most useful finding this method can produce, and it requires searching departure language rather than reading complaints.

**"Lead with reliability in competitive positioning"** turns a review corpus into a field instruction with no check on whether reliability decides deals. Reviews are written by people who already bought.

**The structural gap goes unmentioned.** Everyone in this corpus is a Cartelane customer. The people who evaluated Cartelane and chose someone else — the population a competitive decision most needs — are invisible to this method, and nothing says so.

## What Makes This Hard to Catch

The counts are the disguise. A number next to a theme reads as measurement, and 22 feels more decisive than a frequency label. Nobody asks what the denominator is, because the column is called "Mentions" and mentions were, in fact, counted.

Theme 1 is the deepest trap. Two posts by one person, ranked first, on the strength of a quote so articulate it sounds like a category insight. Vivid isolated complaints are memorable *because* they are vivid, and the correctly-run version has to actively demote it — which feels like discarding the best material in the corpus. It is, and it should be, because one person is one person.

And the feature-request framing is genuinely convenient. Requests are easy to write down, easy to prioritize, and easy to hand to engineering. Needs require inference and arrive as sentences nobody asked for.

## Repair

Rewrite every theme solution-free: what was this person trying to accomplish. Keep the requests in a separate table with the job named beside each, so the roadmap sees both the guess and the problem.

Recount by independent source rather than by post, and add frequency labels. Theme 1 becomes isolated — two posts, one person — and drops out of the priority list. Theme 4 becomes recurring across all three sources and gains strength from appearing in the loyal forum at all.

State each platform's skew where its evidence is used, and stop pooling counts across sources with opposite biases.

Locate every quote or drop it: platform, date, verbatim. Compose nothing, including quotes that would be nearly identical to a real one.

Then go and find the switching triggers, which requires a different search — departure language, renewal language, migration language — and is where the run's actual value was sitting the whole time. Finally, add the structural gap in plain words: everyone here bought Cartelane, and only win/loss reaches the people who did not.
