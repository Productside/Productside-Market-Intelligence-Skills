---
name: mi-analyze-five-forces
description: Rate the five forces from cited signals, name AI substitution and platform dependencies explicitly, and end on the profit pool. Use to judge whether an industry is worth being in.
license: CC-BY-NC-SA-4.0
argument-hint: "[industry] [fused evidence]"
intent: >-
  Read industry structure rather than compare companies. Five ratings, each with a
  documented signal, ending on where the money in this industry actually
  accumulates and whether the structure lets you reach it. Exists because a force
  rating without a cited signal is a mood.
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
  - Business Analyst
  - Strategy and Corporate Development
  - Executive Leadership
  - Investor Relations
best-for:
  - "Deciding whether an industry's structure permits durable margin"
  - "Assessing AI-driven substitution as a first-class threat rather than a footnote"
  - "Naming cloud, model, and platform dependencies as supplier power"
scenarios:
  - "We are considering entering a category and need to know if it can be profitable"
  - "Our margins are compressing and nobody can say structurally why"
  - "The board asked whether AI changes this industry's economics"
  - "We depend on one inference provider and nobody has called that supplier power"
evidence-required:
  - "The industry, defined at a level where structure is comparable"
  - "Fused evidence or sweep outputs with sources"
  - "The decision this supports"
produces:
  - "Five forces rated weak, moderate, or strong, each with cited signals"
  - "An explicit AI-substitution assessment"
  - "Supplier power including platform and model dependencies"
  - "The profit pool read — where the money accumulates and whether you can reach it"
estimated-time: "60-120 min"
group-size: "1-8"
consumes:
  - mi-fuse-all-source
  - mi-scan-market-landscape
combine-with:
  - mi-analyze-ansoff
  - mi-analyze-swot
  - mi-size-tam-sam-som
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, the act layer"
  - "Porter's five forces, as adapted in the Productside market-intelligence prompts"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Five Forces From Evidence"
  short_description: "Industry structure with cited signals"
  brand_color: "#00E874"
  default_prompt: "Use $mi-analyze-five-forces to rate the five forces from cited evidence, assess AI substitution explicitly, include platform and model dependencies in supplier power, and end on the profit pool."
  allow_implicit_invocation: true
---

# Five Forces From Evidence

## Purpose

Read industry structure, not company comparison.

Five Forces answers one question: **is this industry worth being in, and does its structure let you reach the money?** It is not a competitive analysis of named rivals — that is a snapshot — and it is not a position statement — that is a SWOT.

The five ratings are the work. **The profit pool is the output.** A forces analysis that ends with five ratings has stopped one step short of the only thing anyone needed.

This skill consumes evidence. Where a force has no cited signal behind its rating, the honest entry is **"no evidence found"**, and the rating is withheld. "Buyer power: strong" with nothing behind it is a mood in a table.

## When to Use It

Use it before entering a category, when margins are compressing for reasons nobody can name structurally, or when a board question turns on whether an industry's economics still hold. Use it after fusion, so the ratings rest on collected evidence.

Do not use it when:

- **The question is about named competitors.** That is `mi-snapshot-competitors`.
- **The question is your own position.** That is `mi-analyze-swot`.
- **The question is where to grow.** That is `mi-analyze-ansoff`, which reads better after this.
- **You have no evidence yet.** Run sweeps and `mi-fuse-all-source` first. Five ratings derived from a workshop are five opinions in a recognizable shape.

## Input

Require:

- the industry, defined at a level where structure is actually comparable — "software" is not an industry for this purpose
- fused evidence or sweep outputs with sources
- the decision this supports

Anything supplied in the invocation, attachments, a fusion brief, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-analyze-five-forces on mid-market revenue operations tooling, using the fusion brief and landscape scan in this thread. Decision: whether to keep investing here.`

## Key Concepts

**A rating without a cited signal is a mood** — "Buyer power: strong" means nothing. "Buyer power: strong — three of five named buyers ran competitive bake-offs in the last cycle, per [source]" means something, and can be argued with. The citation is what converts a framework into an analysis, and it is what lets someone disagree productively rather than by asserting a different mood.

*Violation signal:* A force carries a rating and a paragraph of reasoning with no source anywhere in it.

**Substitutes must name AI substitution explicitly** — In most knowledge industries, AI-driven substitution is now *the* substitute threat. A five forces read that omits it is describing 2015. Assess it directly: what part of the job a customer currently pays for could be done adequately by a general-purpose model, and what evidence exists that buyers are already doing so. Then rate it honestly, including the honest answer that it is not yet material here.

*Violation signal:* The substitutes force discusses adjacent products and legacy alternatives, and never mentions general-purpose AI.

**Supplier power includes platform and model dependencies** — Supplier concentration in this decade looks like a single inference provider, a single cloud, a single app store, or a single data source with unilateral terms — not a single parts vendor. These suppliers can change pricing, terms, or availability with little notice and no negotiation, which is the textbook definition of supplier power and is routinely omitted because it does not look like procurement.

*Violation signal:* Supplier power is rated weak on the grounds that the company has no physical supply chain.

**Rivalry is structural, not emotional** — Rivalry is strong when exit barriers are high, differentiation is low, growth is slow, or fixed costs push volume. It is not strong because competitors are annoying or marketing is loud. Rate the structure, and cite the structural evidence: switching costs, concentration, growth rate, cost profile.

*Violation signal:* Rivalry is rated strong because there are many competitors, with no reference to exit barriers, differentiation, or growth.

**Non-consumption sits inside substitutes** — In most emerging categories the largest substitute is doing nothing, or a spreadsheet, or an existing employee's manual process. It never appears on a competitive slide and it usually holds most of the market. Omitting it produces a substitutes rating about vendors, which is the wrong analysis.

*Violation signal:* The substitutes force lists only products a customer could buy.

**End on the profit pool** — Where does the money in this industry actually accumulate — vendors, channel, platform owners, services firms, incumbents — and does the structure let you reach it? This is the deliverable. Five ratings and no profit-pool read is a completed exercise with the conclusion missing, and the conclusion is the only part that changes an investment decision.

*Violation signal:* The analysis ends at the fifth force.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a five forces read on industry structure — five ratings, each with cited signals, ending on the profit pool. One to two hours. Where evidence is missing I will write 'no evidence found' and withhold the rating. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Forces Setup Q1/3` — Which industry, defined narrowly enough that structure is comparable across its players?
2. `Forces Setup Q2/3` — What decision does this support: entry, continued investment, exit, or pricing?
3. `Forces Setup Q3/3` — Which platform, cloud, model, or data suppliers do you depend on? That is supplier power, and only you know your stack.

**Context dump is the expected mode.** Extract evidence, map it onto the five forces, and ask only about gaps. In **Best guess** mode, rate from available evidence, withhold ratings where evidence is absent, and name each assumption. On silence: continued-investment framing, ratings withheld where unsupported. Proceed.

## What It Produces

Complete the [Five Forces Analysis](template.md):

- five forces, each rated weak / moderate / strong, with at least one cited signal per rating
- an explicit **AI substitution** assessment inside substitutes
- **non-consumption** named inside substitutes
- supplier power covering **cloud, model, and platform dependencies**
- ratings withheld and marked "no evidence found" where unsupported
- **the profit pool read** — where the money accumulates and whether you can reach it
- assumptions to validate, Final Step block

## Workflow

1. **State web access in one line,** and state that this run consumes evidence rather than collecting it.
2. **Define the industry narrowly** enough that structure is comparable. Say what you excluded.
3. **Rate competitive rivalry** on structure: exit barriers, differentiation, growth rate, fixed-cost profile. Cite each.
4. **Rate threat of new entrants:** capital requirements, regulatory gates, switching costs, distribution access, and what recent entrants actually had to spend. Funded entrants in the landscape scan are evidence here.
5. **Rate threat of substitutes,** and inside it: name **non-consumption** and assess **AI-driven substitution** directly. What part of the paid-for job could a general-purpose model do adequately, and is there evidence buyers are doing it.
6. **Rate buyer power:** concentration, bake-off frequency, switching costs, price transparency, and who signs.
7. **Rate supplier power,** including cloud, model, app-store, and data dependencies with unilateral terms. A single inference provider is supplier concentration.
8. **Withhold any rating you cannot cite,** and write "no evidence found" with what would close it.
9. **Write the profit pool read.** Where the money accumulates, and whether the structure lets you reach it.
10. **Name the assumptions** that would most change the read, and stop.

## Human Decision Gate

Present the profit pool first, then the ratings. Highlight:

- which ratings rest on a single signal
- the AI substitution assessment, and whether it is currently material
- any supplier dependency that could change terms unilaterally
- which force, if it moved, would most change the investment case

Use an Adaptive Decision Ladder: `Act on the profit-pool read`, `Collect evidence for the withheld rating`, `Run Ansoff to choose the growth path`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every rating rationale **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** switching costs, market concentration figures, entrant funding, supplier terms, buyer behavior, or margin data. A structural claim gets repeated in investment memos, where it is durable and consequential.
- Every rating carries at least one cited signal, or it is withheld.
- Distinguish a supplier's *published* terms from terms you have negotiated.
- Do not rate a force by analogy to another industry.

## Common Failure Modes

- Rating forces with reasoning and no citations
- Omitting AI substitution, so the analysis describes a decade ago
- Rating supplier power weak because there is no physical supply chain
- Rating rivalry strong because there are many competitors
- Listing only purchasable substitutes, so non-consumption disappears
- Defining the industry so broadly that structure is not comparable
- Comparing named companies instead of reading structure
- Ending at the fifth force with no profit-pool read

## Assets and Examples

- [Five Forces Analysis template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Act on the profit-pool read (Recommended)
2. Collect evidence for the withheld rating before this goes to the board
3. Schedule an annual refresh, since structure moves slowly but decisively
4. Run Ansoff to choose the growth path this structure permits

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The act layer: five forces discipline rules](../../reference/frameworks.md)
- [Fusion: what feeds this framework](../../reference/fusion.md)
- [The disciplines](../../reference/disciplines.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
