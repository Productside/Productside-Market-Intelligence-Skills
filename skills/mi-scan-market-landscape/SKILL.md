---
name: mi-scan-market-landscape
description: Map a market before sizing or positioning it — segments as buyers see them, players including substitutes and non-consumption, dynamics, and whitespace. Use when you are new to a category.
license: CC-BY-NC-ND-4.0
argument-hint: "[market or category] [buyer]"
intent: >-
  Map a market you do not yet know: how it segments from the buyer's side, who is
  in it including the substitutes nobody puts on slides, what is actually moving,
  and where the gaps are. Exists because sizing or positioning a market you have
  not mapped produces a confident number about the wrong category.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: OSINT
status: active
operating-level:
  - initiative
  - executive
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - Market Research Analyst
  - Strategy and Corporate Development
best-for:
  - "Mapping a category before sizing, positioning, or entering it"
  - "Surfacing substitutes and non-consumption that competitive slides omit"
  - "Distinguishing a whitespace worth entering from a graveyard with fresh paint"
scenarios:
  - "We are considering a new market and nobody here can name who is in it"
  - "Our competitive set is three logos and I suspect that is not the real picture"
  - "Analysts describe this category one way and our buyers describe it another"
  - "Leadership wants a market size and we have not established what the market is"
evidence-required:
  - "The market or category, in whatever words are currently used for it"
  - "The buyer whose mental model should define the segmentation"
  - "The decision this scan feeds"
produces:
  - "Buyer-side segmentation, with vendor-category divergence named"
  - "Player map in four buckets, capped at twelve"
  - "Four named dynamics reads"
  - "Whitespace and dead zones, distinguished"
estimated-time: "60-120 min"
group-size: "1-6"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-snapshot-competitors
  - mi-size-tam-sam-som
  - mi-analyze-five-forces
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, OSINT and the act layer"
  - "Market landscape scan discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Market Landscape Scan"
  short_description: "Map the category before sizing it"
  brand_color: "#00E874"
  default_prompt: "Use $mi-scan-market-landscape to map this category: segment it as buyers see it, map direct, adjacent, substitute, and emerging players, name four dynamics, and distinguish whitespace from dead zones."
  allow_implicit_invocation: true
---

# Market Landscape Scan

## Purpose

Map the market before sizing or positioning it.

Run this when you are new to a category and do not yet know who is in it. The output is a map: how the market segments *from the buyer's side*, who competes including the substitutes nobody puts on slides, what is actually moving, and where the gaps are — with an honest judgment about whether each gap is an opportunity or a graveyard.

This is a collection run. It gathers and labels; it does not rate a threat. **Collection is not fusion.** Sizing, forces analysis, and positioning all consume this map rather than being produced by it.

## When to Use It

Use it before sizing, before positioning, before market entry, and before a competitive snapshot — the scan tells the snapshot which players are worth profiling. Use it when your competitive set is three logos and you suspect the real picture is wider.

Do not use it when:

- **You already know the market and need depth on named players.** That is `mi-snapshot-competitors`.
- **You need the numbers.** The scan names what to count; `mi-collect-geoint-demoint` counts it and `mi-size-tam-sam-som` models it.
- **You need the industry's structural economics.** That is `mi-analyze-five-forces`, which consumes this map.
- **The category is one you have sold into for years.** A scan will confirm what your sales team already knows and cost an afternoon.

## Input

Require:

- the market or category, in whatever words are currently used for it — including a vendor category name, if that is all that exists
- the `[BUYER]` whose mental model should define the segmentation
- the `[DECISION]` this feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-scan-market-landscape on mid-market revenue operations tooling. Buyer is VP RevOps with Finance running evaluation. Decision: whether to enter.`

## Key Concepts

**Segment as buyers see it, not as vendors sell it** — An analyst quadrant is a map someone else drew for their own purposes, and vendor categories are drawn to make particular vendors look central. Segment by the problem the buyer is solving and the way they group alternatives in their own head. Where the buyer's model and the vendor category diverge, **that divergence is itself a finding** — usually the most valuable one in the scan, because it names a category nobody is currently claiming.

*Violation signal:* The segmentation reproduces an analyst quadrant's axes, or a vendor's own category page.

**Non-consumption is usually the market leader** — The player map has four buckets, and skipping the last three is the standard failure. Direct players sell the same thing to the same buyer. Adjacent players are one product decision away from entering. **Substitutes and non-consumption** are spreadsheets, services firms, in-house builds, and doing nothing — and doing nothing almost always holds more share than any vendor, while appearing on no competitive slide anywhere. Emerging entrants are funded, hiring, and pre-revenue.

*Violation signal:* The player map contains only vendors, so the largest incumbent in the category — the status quo — is invisible.

**Twelve is the cap** — Beyond twelve players you are cataloguing rather than mapping, and a map nobody can hold in their head changes no decision. Choose the twelve that matter to the buyer, and say what selection rule you used.

*Violation signal:* The map lists every vendor found, ranked by nothing in particular.

**Four dynamics, named** — Where the money is, where the momentum is, whether the market is consolidating or fragmenting, and which technology or regulatory shifts are in play. Four specific reads, each with evidence. A paragraph of atmosphere about how "the market is evolving rapidly" is the failure this rule exists to prevent, because it is true of every market in every year and therefore informs nothing.

*Violation signal:* The dynamics section is prose with no four named reads and no citations.

**Whitespace or graveyard** — A gap nobody serves is sometimes an opportunity and sometimes a market that has already killed three companies. Name both kinds, say which you think each is, and give the reason. An unserved segment with no evidence of demand is a dead zone until proven otherwise, and dead zones are attractive precisely because they are empty.

*Violation signal:* Every named gap is described as an opportunity.

**A scan is a map, not a verdict** — This run does not rate threats, size the market, or choose a position. It produces the map those decisions need. Reaching a strategic recommendation here means the recommendation was made on a category that had not yet been mapped, which is the error the scan exists to prevent.

*Violation signal:* The scan ends with an entry recommendation.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a market landscape scan — buyer-side segmentation, a four-bucket player map capped at twelve, four dynamics reads, and whitespace versus dead zones. One to two hours. I will produce the map, not the size or the position. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Scan Setup Q1/3` — Which market, in whatever words are used for it today?
2. `Scan Setup Q2/3` — Whose mental model should define the segments — which buyer?
3. `Scan Setup Q3/3` — What decision does this feed: entry, sizing, positioning, or a competitive set refresh?

In **Context dump** mode, extract supplied player names and category language, sort them into the four buckets, and ask only about gaps. In **Best guess** mode, segment from the buyer language found in reviews and forums, and name each assumption. On silence: buyer-side segmentation from public review language, twelve-player cap, entry framing. Proceed.

## What It Produces

Complete the [Market Landscape Scan](template.md):

- scope and the category language currently in use
- buyer-side segmentation, with the vendor-category divergence named
- player map in four buckets, capped at twelve, each entry sourced
- four dynamics reads with evidence
- whitespace and dead zones, distinguished with reasons
- collection gaps, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption with its vintage, and invent no companies, funding rounds, or market shares.
2. **Show the search plan.** Sweep order, date window, noise filter. Continue unless revised.
3. **Scope the market.** Record the category names currently in use — the vendors', the analysts', and the buyers'. Note where they disagree.
4. **Segment from the buyer's side.** Use the language buyers use in reviews, forums, and job postings. Then set it against the vendor category and name the divergence.
5. **Map the players into four buckets.** Direct, adjacent, substitutes and non-consumption, emerging. Cap at twelve and state the selection rule.
6. **Find the non-consumption.** Ask explicitly: what do people who have this problem and buy nothing do instead? Spreadsheets, agencies, an analyst's manual process, or living with it. This bucket is usually the largest and is the one that requires deliberate effort to see.
7. **Write four dynamics reads,** each with evidence: where the money is, where the momentum is, consolidating or fragmenting, and technology or regulatory shifts in play.
8. **Name whitespace and dead zones separately,** with a judgment and a reason for each.
9. **Report gaps** in one line each, naming what was swept.
10. **Stop at the map.** Hand it to `mi-snapshot-competitors`, `mi-size-tam-sam-som`, or `mi-analyze-five-forces`.

## Human Decision Gate

Present the map. Highlight:

- where buyer segmentation and vendor categories diverge
- what sits in the substitutes and non-consumption bucket, and how large it looks
- which gaps you judge to be dead zones, and why
- which players are worth a full snapshot

Use an Adaptive Decision Ladder: `Snapshot the top three players`, `Take the map into sizing`, `Re-segment — the buyer model is wrong`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every key line **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** company names, funding rounds, customer counts, market shares, growth rates, or analyst rankings. An invented competitor in a landscape scan propagates into every downstream artifact.
- Buyer language must be quoted from real sources with platform and date, or described as a pattern and labeled Inference.
- A vendor's own category claim is a Fact about their marketing, not about the market.
- Market share figures require a source and a definition of the denominator, or they are Assumptions.
- Every player entry carries at least one checkable URL.

## Common Failure Modes

- Reproducing an analyst quadrant and calling it segmentation
- Mapping only direct competitors, so non-consumption stays invisible
- Listing thirty players because thirty were found
- Writing atmosphere instead of four named dynamics
- Describing every gap as an opportunity
- Treating a vendor category page as evidence about buyer behavior
- Reaching an entry recommendation from a map
- Sizing the market here instead of naming what to count

## Assets and Examples

- [Market Landscape Scan template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Snapshot the three players that matter most (Recommended)
2. Take the map into sizing and count what it named
3. Schedule an annual re-scan, since category boundaries move slowly
4. Hand the buyer-versus-vendor divergence to positioning

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The act layer: market landscape scan discipline rules](../../reference/frameworks.md)
- [The disciplines: OSINT](../../reference/disciplines.md)
- [Sweep playbooks](../../reference/sweep-playbooks.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
