# Weak Example: The Brief Where Everything Was Actionable

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It has a signal inventory, discipline labels, confidence ratings, commitment levels, artifact-mapped responses, and a conflicts section. It follows the schema closely. It would pass a quick review, and it did — leadership was briefed on all five stories.

Same fictional Cartelane case, fused by a different analyst.

## The Artifact

### 1. Signal Inventory (excerpt)

| Signal | Discipline | Source (URL, date) | Label |
|---|---|---|---|
| ERP integration platform announced | OSINT | `example.invalid/newsroom`, 2026-03-04 | Fact |
| TechRevOps: "Cartelane bets big on integrations" | OSINT | `example.invalid/techrevops`, 2026-03-05 | Fact |
| RevOpsDaily coverage of the announcement | OSINT | `example.invalid/revopsdaily`, 2026-03-05 | Fact |
| Analyst summary: "credible platform entry" | OSINT | `example.invalid/analyst`, 2026-03-11 | Fact |
| CEO post announcing the platform | OSINT | `example.invalid/ceo-post`, 2026-03-04 | Fact |
| 9-filing patent cluster | TECHINT | `example.invalid/patents`, 2026-01 | Fact |
| 22 integration roles open | HUMINT | `example.invalid/careers`, 2026-08-15 | Fact |
| Support response times slower | MASINT | `example.invalid/forum`, 2026-08-15 | Fact |
| Support postings down | HUMINT | `example.invalid/careers`, 2026-08-15 | Fact |
| Entry pricing tier removed | SIGINT | `example.invalid/pricing`, 2026-08-18 | Fact |

### 2. Fusion Stories

**Story 1: Platform strategy is real and funded.** Disciplines: 7 (OSINT x5, TECHINT, HUMINT). Verdict: **Actionable**. Commitment: **Funded**. Response: accelerate integration roadmap.

**Story 2: Moving upmarket.** Disciplines: 2 (SIGINT, HUMINT). Verdict: **Actionable**. Commitment: Built. Response: reposition against them at the low end.

**Story 3: Support is failing.** Disciplines: 2 (MASINT, HUMINT). Verdict: **Actionable**. Commitment: n/a. Response: battle card — lead with support quality.

**Story 4: They are becoming more aggressive competitively.** Disciplines: 3. Verdict: Working hypothesis. Response: monitor.

**Story 5: Partner strategy is evolving.** Disciplines: 2. Verdict: Working hypothesis. Response: monitor.

### 3. Conflicts

- Cartelane says partners are central; they are also hiring in-house. **Read:** they are pursuing a hybrid model, balancing partner and native integration.

### 5. Collection Gaps

- FININT signals were not available for this brief.

## Why It Passes a Quick Read

- The schema is followed: inventory, stories, conflicts, gaps, all in order.
- Every signal is real, sourced, and dated. Nothing is fabricated.
- Discipline labels are applied correctly to each signal.
- Confidence verdicts and commitment levels are both present — most briefs omit the second.
- Every story ends with a response, which is what the discipline demands.
- A conflict is named rather than ignored.

## Why It Fails

**The independence test never ran, and Story 1 is built on its absence.** Five of the ten inventory rows are the same 2026-03-04 press release: the newsroom post, two trade articles, an analyst summary, and the CEO's announcement post. Story 1 claims **seven disciplines**, which is not even arithmetically possible — there are only seven disciplines in total and this brief holds four. What it means is seven *sources*, five of which are one origin.

*This is the independence violation signal exactly:* confidence stated in number of sources rather than number of independent origins. Post-collapse, Story 1 rests on three disciplines, which still rates actionable — so the verdict happens to survive. The reasoning does not, and the next brief that makes this error will not be so lucky.

**Commitment is graded backwards on the strongest story.** Story 1 is marked **Funded**, and nothing in the inventory is a funding signal — there is no FININT at all. What the evidence actually supports is **Staffed**: twenty-two roles and a patent cluster. "Funded" was chosen because it sounds like commitment, and it is the one rung the evidence cannot reach.

**Three stories rated actionable, two of which are two-discipline stories.** The stacking rule is not a suggestion: two disciplines is a working hypothesis with a named probe, not a brief to leadership. Story 2 and Story 3 were both promoted, and nothing in the document explains the promotion.

**Story 3 ignores the win/loss cap entirely.** It is an org-instability story, win/loss is unverified this cycle, and it is rated actionable with the response "battle card — lead with support quality." That is a claim about why deals are won, derived from forum response times and job postings, going straight to a rep who will say it to a customer. The cap exists for precisely this line.

**Story 4 is a vibe.** "They are becoming more aggressive competitively" cannot be falsified, cannot be probed, and cannot be wrong. It also double-counts: the signals behind it are the same pricing and hiring signals already carried by Stories 1 and 2, appearing a second time under a name vague enough to accommodate them.

**Two stories respond with "monitor," which is not a response.** A watch item names its escalation trigger. A working hypothesis names a probe, an owner, and a deadline. "Monitor" assigns nothing to nobody by no date, and it is how a working hypothesis quietly becomes permanent.

**The conflict was averaged, in the exact words the rule warns about.** "Pursuing a hybrid model, balancing partner and native integration" reconciles two contradictory signals into a moderate statement neither supports. The partner program is closed to new partners and its VP has left; twenty-two in-house engineers are being hired. That is not a balance, it is a replacement, and the gap between what Cartelane says and what Cartelane funds was the most useful finding available. It has been smoothed into a sentence nobody can act on and nobody can dispute.

**Five stories because the cap is five.** Stories 4 and 5 add nothing that Stories 1 through 3 do not already carry. The cap is a ceiling, not a quota.

**"FININT signals were not available"** names no sweep, no consequence, and no reason. The consequential version says Story 2 cannot rise without it. And the GEOINT gap — nobody has checked whether the segment Cartelane is moving toward is large enough to matter — is not mentioned at all.

## What Makes This Hard to Catch

The schema is the disguise. Fusion briefs are reviewed for completeness of structure — is there an inventory, are there verdicts, are there responses — and every box is filled. The confidence ratings *look* like the rule being applied, because the vocabulary is correct.

The seven-source claim is persuasive in the direction of its own error: the more sources appear to agree, the stronger the story reads, so the deception scales with itself. And the number 7 is never questioned, because nobody counts disciplines while reading a number that large.

The averaged conflict is the subtlest failure of all. "Balancing partner and native integration" is the sentence everyone in the room can agree with. It is measured, it acknowledges both sources, and it sounds like judgment. What it actually is, is the analyst declining to say which source is lying.

## Repair

Run the independence test first and record the collapse: fifteen apparent sources, eight independent origins, five of them collapsing into one press release. Then recount every story's disciplines from the collapsed inventory, and state the count post-collapse everywhere a verdict appears.

Regrade Story 1's commitment to **Staffed** and say what evidence would move it to Funded — which is a FININT sweep, which is also the named gap. Demote Stories 2 and 3 to working hypothesis, and give each a probe with an owner and a deadline instead of "monitor." Apply the win/loss cap to Story 3 explicitly and pull it off the battle card until interviews confirm that support decides deals here.

Delete Stories 4 and 5. Three real stories beat five padded ones, and the signals in 4 and 5 already appear above.

Rewrite the conflict without averaging: A says partners are central, B says the program is closed and the VP is gone, the money supports B, and their next partner summit would settle it. Then rewrite the gaps to say what each absence costs this brief — starting with the GEOINT question nobody asked, which is whether the market Cartelane is building toward is worth the twenty-two engineers.
