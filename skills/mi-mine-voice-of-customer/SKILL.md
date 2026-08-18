---
name: mi-mine-voice-of-customer
description: Mine reviews, app stores, forums, and communities for unmet needs, competitor weak points, and switching triggers, with quoted evidence and frequency labels. Use before a card or a roadmap bet.
license: CC-BY-NC-SA-4.0
argument-hint: "[market or competitor] [buyer]"
intent: >-
  Mine public customer voice for solution-free need themes, competitor weak
  points, and the specific events that make people switch. Exists because public
  voice is real evidence with a known skew, and treating it as either verdict or
  noise are the two ways teams get it wrong.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: OSINT
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - User Researcher
  - Sales Enablement
best-for:
  - "Finding switching triggers — the specific events that make someone leave"
  - "Turning review clusters into solution-free need themes with quoted evidence"
  - "Sourcing the objection-handling layer of a battle card from real customer words"
scenarios:
  - "We need to know what customers actually complain about before we write the card"
  - "Our roadmap is being argued from three anecdotes and one angry reviewer"
  - "A competitor's reviews cluster on something and we do not know what"
  - "We want to know what makes people leave, not just what they dislike"
evidence-required:
  - "The market or competitor whose customers are being mined"
  - "The buyer and end-user, which decides which platforms matter"
  - "The decision this feeds"
produces:
  - "Solution-free need themes with frequency labels"
  - "Competitor weak points with quoted, dated evidence"
  - "Switching triggers — the highest-value output"
  - "Per-source bias notes and collection gaps"
estimated-time: "45-90 min"
group-size: "1-4"
consumes:
  - mi-collect-osint
  - mi-router-market-intelligence
combine-with:
  - mi-build-battle-card
  - mi-fuse-all-source
  - mi-snapshot-competitors
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, OSINT review mining"
  - "Voice-of-customer mining discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Voice-of-Customer Miner"
  short_description: "Mine public reviews for real needs"
  brand_color: "#00E874"
  default_prompt: "Use $mi-mine-voice-of-customer to mine reviews, app stores, and forums for solution-free need themes, competitor weak points, and switching triggers, with real quotes, frequency labels, and per-source bias noted."
  allow_implicit_invocation: true
---

# Voice-of-Customer Miner

## Purpose

Mine what customers actually say, in their own words, at scale.

Reviews, app stores, forums, support communities, and social posts are the largest body of unsolicited customer evidence available, and it is free. It is also skewed — toward the angry, the vocal, and the recently disappointed — which is why the two common failures are opposite: treating it as verdict, and dismissing it as noise. It is neither. It is evidence with a known bias, and stating the bias is what makes it usable.

The highest-value output is not the complaint list. It is the **switching triggers**: the specific events that made someone leave. Those are your entry points and your own churn early-warning list.

This is a collection run. **Collection is not fusion** — it gathers themes and labels their frequency; it does not rate whether a theme decides deals.

## When to Use It

Use it before writing a battle card's objection-handling layer, before a roadmap bet that rests on customer pain, and after an OSINT sweep has flagged a review cluster worth mining properly.

Do not use it when:

- **You need to know why deals were lost.** Reviews are written by people who bought. Win/loss interviews reach the people who did not, and that population is the one you are missing.
- **You need frequencies you can trust as market-wide.** Public voice is self-selected. It reveals themes; it does not measure their prevalence.
- **The product has too few reviews to cluster.** Fewer than roughly twenty across all sources means you have anecdotes, and saying so is more useful than clustering them.
- **You want a feature list.** Requests are not needs; see below.

## Input

Require:

- the market or competitor whose customers are being mined
- the `[BUYER]` and end-user, which decides which platforms matter — a finance buyer and a developer end-user live in different places
- the `[DECISION]` this feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-mine-voice-of-customer on Cartelane. Buyer is VP RevOps, end users are ops analysts. Decision: what goes on the battle card.`

## Key Concepts

**Need themes must be solution-free** — Four to eight words describing what the person was trying to accomplish, not the feature they asked for. "Cannot reconcile numbers across two systems" is a need. "Wants a CSV export" is a request. The distinction matters because requests are one customer's guess at a solution, and a roadmap built from requests builds twelve versions of that guess instead of solving the problem underneath.

*Violation signal:* A theme is phrased as a feature that could be built, rather than as a situation someone is stuck in.

**Frequency labels, not counts** — Every theme is labeled **recurring across sources**, **concentrated in one source**, or **isolated**. A vivid isolated complaint and a recurring cross-source pattern are not the same evidence, and a theme list that does not distinguish them will send a roadmap chasing one angry reviewer — who is memorable precisely because they were vivid.

*Violation signal:* Themes are listed in order of how compelling the quote was.

**Every source has a stated bias** — Reviewers skew negative and toward the recently churned. Vendor communities skew loyal, because the unhappy leave. App-store ratings skew bimodal, since mild satisfaction does not motivate a rating. Incentivized review programs skew positive in ways that are usually disclosed if you look. State each source's skew where you use it, not in a footnote.

*Violation signal:* Evidence from a vendor's own community forum is weighted the same as evidence from an independent review site.

**Switching triggers are the prize** — Not "what do they dislike" but "what specific event made them leave." A renewal, an outage, a price increase, a reorg, a champion departing, a failed audit. These are the moments a competitor is displaceable and the moments your own customers are at risk, and they are far rarer in the data than complaints — which is why most mining runs miss them by not asking.

*Violation signal:* The output has a complaints section and no section naming the events that preceded departures.

**Quote discipline** — Real quotes, with the platform and the date. **Never compose a representative quote.** If a pattern cannot be quoted, describe it and label it Inference. A fabricated quote is the single most damaging output here, because quotes are exactly what gets pasted into a slide and read aloud.

*Violation signal:* A quote appears with no platform, no date, or in language suspiciously close to the report's own prose.

**Themes are hypotheses, not verdicts** — Public voice tells you what to go ask about. It does not tell you what decides purchases, what most customers experience, or what to build. Every theme leaving this run is a candidate for validation, and saying so is not hedging — it is the accurate description of what review data can support.

*Violation signal:* A theme arrives in a roadmap document as an established customer requirement.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a voice-of-customer mining run — solution-free need themes, competitor weak points, and switching triggers, with real quotes and frequency labels. Forty-five to ninety minutes. Themes leave here as hypotheses to validate, not as requirements. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `VoC Setup Q1/3` — Whose customers am I mining: a competitor's, the category's, or your own?
2. `VoC Setup Q2/3` — Who is the buyer and who is the end user? They are often different people on different platforms, and mining the wrong one produces themes nobody with budget cares about.
3. `VoC Setup Q3/3` — What decision does this feed: a battle card, a roadmap input, or a positioning refresh?

In **Context dump** mode, extract supplied reviews and transcripts, cluster them, label frequency, and mine only the gaps. In **Best guess** mode, assume the largest independent review platform for the category plus the two most active public forums, use a twelve-month window, and name each assumption. On silence: those defaults, competitor framing. Proceed.

## What It Produces

Complete the [Voice-of-Customer Mining Report](template.md):

- scope and sources, each with its stated bias
- need themes, solution-free, with frequency labels and quoted evidence
- competitor weak points with quoted, dated evidence
- **switching triggers**
- so-what, and what to validate before acting
- collection gaps, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption, and compose no quotes under any circumstances.
2. **Show the search plan.** Which platforms, which window, and how you will separate the target's customers from adjacent-product customers. Continue unless revised.
3. **Choose platforms from the buyer and end user,** not from familiarity. State the skew of each as you add it.
4. **Read for the job, not the request.** When someone asks for a feature, record what they were trying to accomplish.
5. **Cluster into solution-free themes,** four to eight words each.
6. **Label frequency:** recurring across sources, concentrated in one source, or isolated. Count sources, not posts — twelve posts by four people in one forum is concentrated, not recurring.
7. **Quote real evidence** with platform and date. Where a pattern cannot be quoted, describe it and label it Inference.
8. **Mine the switching triggers specifically.** Search for departure language — renewal, migration, "we moved to," "after the outage" — because triggers do not surface by reading complaints.
9. **Note each source's bias where it is used.**
10. **Close with what to validate,** and stop. Themes leave as hypotheses.

## Human Decision Gate

Present the themes and triggers. Highlight:

- which themes are recurring versus concentrated versus isolated
- which sources carry the heaviest skew, and how much of the evidence came from them
- the switching triggers, which are the highest-value output
- what would have to be true for a theme to justify a roadmap change

Use an Adaptive Decision Ladder: `Take the triggers into the battle card`, `Validate the top theme with interviews`, `Mine a second competitor for contrast`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every key line **Fact** (a real quote or a counted pattern), **Inference** (a read across posts, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** quotes, review counts, star ratings, usernames, dates, or platform names. Never compose a "representative" quote, even when a real one is nearly identical — composed quotes are the fabrication most likely to be read aloud verbatim.
- Attribute every quote to a platform and a date. Do not attribute quotes to named individuals or companies, even when the poster identifies themselves.
- Count independent sources, not posts.
- State the skew of each platform where its evidence is used.
- Stay inside the guardrails: publicly posted content only. No private groups, no scraping in violation of terms, no contacting reviewers.

## Common Failure Modes

- Recording feature requests as needs
- Ranking themes by how vivid the quote was
- Treating one forum's twelve posts as a cross-source pattern
- Weighting a vendor's own community equally with an independent site
- Composing a quote that "captures the sentiment"
- Producing complaints and never finding switching triggers
- Mining the end user's platforms when the buyer holds the budget, or the reverse
- Presenting themes as validated requirements
- Clustering twelve reviews and calling it a pattern

## Assets and Examples

- [Voice-of-Customer Mining Report template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Take the switching triggers into the battle card (Recommended)
2. Validate the top theme with ten customer interviews
3. Schedule a quarterly mining pass so themes are tracked over time
4. Mine a second competitor for contrast

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The act layer: voice-of-customer mining discipline rules](../../reference/frameworks.md)
- [The disciplines: OSINT](../../reference/disciplines.md)
- [Sweep playbooks](../../reference/sweep-playbooks.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
