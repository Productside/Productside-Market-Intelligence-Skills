---
name: mi-analyze-ansoff
description: Lay out growth options across the four Ansoff quadrants with evidence per move, the risk gradient respected, and a recommended sequence. Use when the question is where to grow next.
license: CC-BY-NC-ND-4.0
argument-hint: "[company] [fused evidence]"
intent: >-
  Turn fused evidence into growth options that respect the risk gradient, then
  recommend a sequence rather than a ranked list. Exists because inventing a
  diversification play to fill an empty box is how a growth plan acquires a
  liability, and because sequence implies dependency, which is what a plan is.
type: analysis
theme: market-competitive-intelligence
stage: act
discipline: All-Source Fusion
status: active
operating-level:
  - initiative
  - executive
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - Strategy and Corporate Development
  - Executive Leadership
best-for:
  - "Laying out growth options with evidence rather than ambition behind each"
  - "Testing whether penetration is genuinely exhausted before reaching for new markets"
  - "Producing a sequence with dependencies rather than a ranked wish list"
scenarios:
  - "Leadership wants a growth plan and the default answer is a new vertical"
  - "Our roadmap has three diversification bets and no penetration work"
  - "We need to decide where next year's investment goes"
  - "Someone proposed entering a new market and nobody asked whether the current one is finished"
evidence-required:
  - "Fused evidence or sweep outputs with sources"
  - "Current market and product boundaries, stated"
  - "The investment decision this supports"
produces:
  - "Two to three candidate moves per quadrant, each with evidence and a risk rating"
  - "Empty quadrants left empty where the evidence is empty"
  - "A recommended sequence with dependencies"
  - "The 'not yet' move and the assumption that breaks the sequence"
estimated-time: "45-90 min"
group-size: "1-8"
consumes:
  - mi-fuse-all-source
  - mi-analyze-five-forces
combine-with:
  - mi-size-tam-sam-som
  - mi-analyze-swot
  - mi-scan-market-landscape
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, the act layer"
  - "Ansoff growth matrix, as adapted in the Productside market-intelligence prompts"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Ansoff Growth Options"
  short_description: "Growth options with a real sequence"
  brand_color: "#00E874"
  default_prompt: "Use $mi-analyze-ansoff to lay out growth options across the four quadrants with evidence per move, leave empty quadrants empty, and end on a recommended sequence with its breaking assumption."
  allow_implicit_invocation: true
---

# Ansoff Growth Options

## Purpose

Lay out where growth could come from, with evidence behind each option and the risk gradient respected.

Four quadrants, ordered by risk: **market penetration** (existing product, existing market), **market development** (existing product, new market), **product development** (new product, existing market), **diversification** (new product, new market). The gradient is not decorative — a recommendation that leads with diversification needs to explain why penetration is exhausted, with evidence that it is.

The output is a **sequence**, not a ranked list. Sequence implies dependency, and dependency is what makes something a plan rather than a menu.

This skill consumes evidence. Where a quadrant has no evidenced move, the honest entry is **"no evidence found"** and the quadrant stays empty. Inventing a diversification play to fill the box is how a growth plan acquires a liability.

## When to Use It

Use it when the question is where to grow next and the evidence exists. Use it especially when the room's default answer is a new market — this framework's main service is asking whether the current one is finished.

Do not use it when:

- **You do not know the market's structure.** Run `mi-analyze-five-forces` first; the structure determines which quadrants are even viable.
- **You need the market's size.** That is `mi-size-tam-sam-som`, which this should consume rather than estimate.
- **The question is your position rather than your direction.** That is `mi-analyze-swot`.
- **You have no evidence.** A quadrant grid filled from a workshop is a record of enthusiasm.

## Input

Require:

- fused evidence or sweep outputs with sources
- your current market and product boundaries, stated — the quadrants are defined relative to them, and a vague boundary makes every quadrant assignment arbitrary
- the investment decision this supports

Anything supplied in the invocation, attachments, a fusion brief, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-analyze-ansoff using the fusion brief and forces read in this thread. Current market: mid-market RevOps, US and Canada. Decision: where next year's investment goes.`

## Key Concepts

**The risk gradient is load-bearing** — Penetration is lowest risk because both the product and the market are known. Diversification is highest because neither is. A plan that starts at the far corner is not automatically wrong, but it carries a burden of proof: show that penetration is exhausted, with evidence. Skipping that burden is how organizations spend a year learning a new market while a competitor takes the one they already had.

*Violation signal:* Diversification is recommended first and no evidence is offered that the current market is saturated.

**An empty quadrant is an acceptable answer** — And it is usually diversification. A quadrant with no evidenced move should be left empty and marked "no evidence found," because a fabricated entry there is not merely padding — it is a proposal that someone may fund. This is the one framework where filling the boxes creates direct financial exposure.

*Violation signal:* All four quadrants contain the same number of moves.

**Penetration is checked with numbers, not with feelings** — "We've saturated our market" is nearly always false in a fragmented category. Test it: current customers against the addressable denominator, win rate against the served segment, share of the non-consumption alternative. The correctly-checked penetration quadrant is usually the fullest one, and it is usually the least popular in the room, because expansion is more exciting than finishing.

*Violation signal:* Penetration is dismissed in a sentence with no denominator anywhere in the document.

**Every move carries a risk rating and its justification** — "High risk" without a reason is a hedge. The rating comes from what is unknown: an unknown buyer, an unknown regulatory regime, an unknown channel, an unproven technology. Naming *which* unknown drives the rating is what lets someone reduce it cheaply — often with research rather than with investment.

*Violation signal:* Risk ratings appear as labels with no statement of what is actually unknown.

**Sequence, not ranking** — A ranked list says which move is best. A sequence says which move must happen before another can, and why. "Penetration through Q2 funds the market-development pilot in Q3" is a plan. "1. Penetration 2. Market development" is a preference. Sequence is where dependencies, funding, and learning order become visible.

*Violation signal:* The recommendation is a numbered list with no dependency stated between items.

**Name the "not yet" and the breaking assumption** — Two closing lines earn the document. **Not yet:** the tempting move, and why the evidence says wait — this is what stops the same proposal returning every quarter. **The assumption that breaks this sequence:** the single belief that, if wrong, invalidates the order. Naming it turns a plan into something that can be monitored.

*Violation signal:* The plan ends on a recommendation with no stated condition that would invalidate it.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is an Ansoff read — growth options across four quadrants with evidence per move, empty quadrants left empty, ending in a recommended sequence and the assumption that would break it. Forty-five to ninety minutes. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Ansoff Setup Q1/3` — What are your current market and product boundaries? The quadrants are defined relative to them.
2. `Ansoff Setup Q2/3` — What investment decision does this support, and over what horizon?
3. `Ansoff Setup Q3/3` — Is there a move already being proposed internally? I will assess it in place rather than pretending the room is empty.

**Context dump is the expected mode.** Extract evidence, sort candidate moves into quadrants, and ask only about gaps. In **Best guess** mode, build from available evidence, leave unsupported quadrants empty, and name each assumption. On silence: annual investment horizon, no pre-proposed move, penetration checked first. Proceed.

## What It Produces

Complete the [Ansoff Growth Options](template.md):

- current boundaries, stated
- two to three candidate moves per quadrant where evidence supports them, each with evidence and a risk rating with its justification
- **empty quadrants left empty**, marked "no evidence found"
- the penetration check, with numbers
- a **recommended sequence** with dependencies
- **not yet**, and **the assumption that breaks this sequence**
- Final Step block

## Workflow

1. **State web access in one line,** and state that this run consumes evidence rather than collecting it.
2. **State current market and product boundaries.** Every quadrant assignment depends on them.
3. **Run the penetration check first, with numbers.** Customers against the denominator, win rate in the served segment, share against non-consumption. Report the numbers even if they are uncomfortable.
4. **Populate market penetration** with two to three evidenced moves. This quadrant is usually the fullest and usually the least popular.
5. **Populate market development,** naming what is unknown about the new market — buyer, regulation, channel, or title prevalence.
6. **Populate product development,** naming what is unproven about the new product.
7. **Assess diversification honestly.** If nothing is evidenced, leave it empty and say so. Do not invent a move here.
8. **Rate each move and justify the rating** by naming the specific unknown that drives it.
9. **Write the recommended sequence with dependencies:** what funds what, what teaches what, what must complete before what begins.
10. **Write "not yet"** — the tempting move and why the evidence says wait — and **the assumption that breaks this sequence.** Then stop.

## Human Decision Gate

Present the sequence first, then the quadrants. Highlight:

- the penetration numbers, especially if they contradict the room's assumption
- which quadrant is empty and why
- the "not yet" move, since it is usually someone's proposal
- the breaking assumption, and how it would be monitored

Use an Adaptive Decision Ladder: `Commit to the sequence`, `Fund research to reduce the top risk before committing`, `Re-run with different market boundaries`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every move **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** market sizes, buyer populations, regulatory conditions, channel economics, or competitor withdrawal. A growth plan is funded, which makes a fabricated premise into a budget line.
- Every move carries at least one cited signal, or it does not go in a quadrant.
- The penetration check requires a real denominator, sourced. Without one, say the check could not be run.
- A risk rating requires a named unknown.
- Do not present an untested market-development move as lower risk than an evidenced product-development move merely because the matrix orders them that way.

## Common Failure Modes

- Recommending diversification without showing penetration is exhausted
- Filling the diversification quadrant so the grid looks complete
- Dismissing penetration in a sentence with no denominator
- Rating risk without naming the unknown behind it
- Producing a ranked list and calling it a sequence
- Omitting "not yet," so the same proposal returns next quarter
- Ending with no breaking assumption, so the plan cannot be monitored
- Assigning quadrants against vague boundaries, making every assignment arbitrary

## Assets and Examples

- [Ansoff Growth Options template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Commit to the recommended sequence (Recommended)
2. Fund research to reduce the top-rated risk before committing
3. Set a quarterly review against the breaking assumption
4. Size the market-development move before it starts

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The act layer: Ansoff discipline rules](../../reference/frameworks.md)
- [Fusion: what feeds this framework](../../reference/fusion.md)
- [The disciplines: GEOINT/DEMOINT for the denominator](../../reference/disciplines.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
