# Weak Example: The Sweep Where Seven Sources Agreed

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It has a search plan, a correct inventory schema, real evidence labels, dated sources, ranked chains, a gap section, and a stop before fusion. It is not lazy work. It would pass a quick review, and the chain at the top of it reached a roadmap discussion three days later.

Same fictional Cartelane case, swept by a different analyst.

## The Artifact

### Search Plan

- **Sweep order:** newsroom → analysts → social → reviews → events
- **Date window:** last 12 months
- **Noise filter:** excluded unrelated companies with similar names; deduplicated coverage

### 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| Cartelane announced an ERP integration platform | `example.invalid/cartelane-newsroom`, 2026-03-04 | Fact | Platform strategy confirmed | Roadmap |
| TechRevOps Weekly: "Cartelane bets big on integrations" | `example.invalid/techrevops`, 2026-03-05 | Fact | Industry sees this as a major move | Roadmap |
| RevOpsDaily coverage of the platform announcement | `example.invalid/revopsdaily`, 2026-03-05 | Fact | Confirms scale of the bet | Roadmap |
| Analyst summary calls it "a credible platform entry" | `example.invalid/analyst-brief`, 2026-03-11 | Fact | Third-party validation | Positioning |
| CEO LinkedIn post announcing the platform | `example.invalid/ceo-post`, 2026-03-04 | Fact | Executive commitment | Roadmap |
| Cartelane product page describes 40+ native connectors | `example.invalid/cartelane-product`, 2026-08-15 | Fact | Broad integration coverage shipped | Battle card |
| G2 rating 4.4 stars | `example.invalid/g2-cartelane`, 2026-08-15 | Fact | Well regarded by customers | Battle card |

### 2. Strongest Inference Chains

1. **Seven independent sources confirm the ERP platform strategy** → Inference: this is a committed, funded platform bet, not exploration → Roadmap: accelerate our integration work this quarter.
2. **40+ native connectors shipped** → Inference: they are ahead of us on integration breadth → Battle card: avoid integration comparisons.
3. **4.4 stars on G2** → Inference: customer satisfaction is not a weak point → Battle card: do not lead with quality.

### 5. Collection Gaps

- Prediction markets: no information available.

## Why It Passes a Quick Read

- The schema is correct: one observation per row, source, date, label, chain, artifact.
- Every URL is real and dated. Nothing is fabricated.
- Evidence labels appear on every line and are used consistently.
- The chains are ranked and tied to named artifacts with concrete moves.
- It stops before rating confidence, exactly as the discipline requires.
- The recommendation it produces is specific and actionable, which is what reviewers reward.

## Why It Fails

**Five of the seven rows are one source.** The newsroom post, both trade articles, the analyst summary, and the CEO's LinkedIn post all trace to Cartelane's press release of 2026-03-04. That is *one* origin wearing five hats. Chain 1 opens with the phrase "seven independent sources," which is the exact sentence the independence test exists to prevent, and it is the most persuasive sentence in the document.

*This is the source-independence violation signal verbatim:* several rows whose URLs all trace back to the same newsroom post on the same day. Catching it requires clicking through to each article's own citation, which is five minutes of work that nobody does under deadline.

**Chain 1 confuses ambition with commitment.** Every signal behind it is OSINT, and OSINT collects intent. The announcement establishes that Cartelane *would like* a platform strategy to be true. Whether it is funded, staffed, or built is a FININT, HUMINT, and TECHINT question, and none of them were asked. The chain nonetheless concludes "committed, funded" — a word that appears nowhere in the evidence — and then recommends reprioritizing a quarter of engineering on it.

**The product page is treated as a fact about the market.** "40+ native connectors" is a Fact about what Cartelane's marketing page says. Whether those connectors exist, work, or cover the systems this buyer runs is unestablished. Meanwhile the actual customer signal on this exact topic — the connector-reliability complaints a careful sweep would have found in the reviews — was never surfaced, because the review channel was reduced to a star rating.

**The star average destroyed the review channel.** "4.4 stars" is the least informative thing a review corpus contains. The clusters are the signal: what recurs, on which feature, across how many independent sources. Chain 3 uses the average to conclude quality is not a weak point, and then *instructs the field not to look there* — which is precisely where the weak point was.

**There is no say-versus-said-about gap.** The signature output of the discipline is simply absent. Their language is collected; customer language is reduced to a number; the subtraction never happens. Nothing in the review checklist catches this, because the missing section leaves no empty box.

**The noise filter names nothing.** "Excluded unrelated companies with similar names" and "deduplicated coverage" describe intentions. Which companies? Deduplicated against what? The dedup claim is especially damning given what the inventory contains — it is asserted and demonstrably not performed.

**"No information available" is not gap language.** The gap section is supposed to say what was swept, what the absence suggests, and what would close it. One line saying nothing was found tells a reader nothing about whether the channel was empty or the analyst was tired.

## What Makes This Hard to Catch

Every failure here is a failure of *provenance*, and provenance is invisible in a finished table. The rows look independent because they have different URLs, different publishers, and different dates. Reviewers check that sources exist; they rarely check that sources are *different*. And the document's confidence is proportional to its error — the more sources appear to agree, the stronger chain 1 reads, so the deception scales with itself.

The star-rating substitution is subtler still. It is a real number from a real source, correctly labeled, feeding a plausible chain. It looks like the review channel was swept. What it actually is is the review channel being *skipped* in a way that produces a citation.

And the whole thing recommends action, which is what the discipline says to do. A reviewer looking for "does this end in an artifact that changes" will find that it does.

## Repair

Follow every source to its origin before it enters the inventory. Collapse the five press-release descendants into one row and write the collapse down — "seven sources, one origin" belongs in the document, because it is the finding. Then re-rank: chain 1 was carrying the run on a corroboration that does not exist.

Relabel the announcement as intent, and state its commitment level as **Announced** with nothing below it. Say plainly that an OSINT-only story cannot rate above working hypothesis, and route the funded/staffed/built question to FININT, HUMINT, and TECHINT rather than answering it here.

Replace the star average with the clusters: what recurs, across how many independent sources, on which feature. Then perform the subtraction that produces the say-versus-said-about gap, and name defended ground, exposed flank, and whitespace.

Name the excluded entities in the noise filter, or delete the bullet. And rewrite the gap section to say what was swept and what the silence means — including the possibility that this channel simply does not apply to this category, which is a finding worth one honest line.
