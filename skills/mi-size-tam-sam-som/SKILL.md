---
name: mi-size-tam-sam-som
description: Build a bottom-up TAM, SAM, and SOM from a cited denominator and a FININT-derived capture rate, expressed in both currency and customers, with sensitivity. Use before a business case meets finance.
license: CC-BY-NC-SA-4.0
argument-hint: "[market] [denominator and capture rate]"
intent: >-
  Turn a cited denominator and a real capture rate into a sizing model that
  survives finance. Exists because "1% of a $50B market" is not a model, it is a
  wish with arithmetic, and because the sensitivity is the deliverable while the
  point estimate is decoration.
type: analysis
theme: market-competitive-intelligence
stage: act
discipline: GEOINT/DEMOINT
status: active
operating-level:
  - initiative
  - executive
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - Finance Business Partner
  - Strategy and Corporate Development
best-for:
  - "Building a bottom-up market size that survives a CFO's questions"
  - "Deriving a capture rate from a competitor's actual economics rather than from optimism"
  - "Producing the sensitivity that makes a business case decision-ready"
scenarios:
  - "Finance asked where our market size number came from and we do not have an answer"
  - "Our business case says one percent of a large number"
  - "Two analyst reports disagree by three times and the deck picked one"
  - "We need a SOM we can defend over a three-year horizon"
evidence-required:
  - "The denominator — establishment or population counts with vintage"
  - "A capture rate basis, ideally a competitor's revenue over claimed customers"
  - "The real eligibility constraints that turn TAM into SAM"
produces:
  - "TAM, SAM, SOM in both currency and number of customers"
  - "Every input with a source, a vintage, and a label"
  - "Best, base, and worst cases with the assumption that moves each"
  - "Method declared as bottom-up-built or top-down-validated"
estimated-time: "60-120 min"
group-size: "1-6"
consumes:
  - mi-collect-geoint-demoint
  - mi-collect-finint
combine-with:
  - mi-analyze-ansoff
  - mi-scan-market-landscape
  - mi-fuse-all-source
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, the TAM/SAM/SOM recipe"
  - "Regional Source Overlays: EU and MENA, statistics sections"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.census.gov/programs-surveys/cbp.html
interface:
  display_name: "TAM, SAM, and SOM"
  short_description: "Bottom-up sizing that survives finance"
  brand_color: "#00E874"
  default_prompt: "Use $mi-size-tam-sam-som to build a bottom-up TAM, SAM, and SOM from the cited denominator and capture rate, express each in currency and customers, and end on the sensitivity rather than a point estimate."
  allow_implicit_invocation: true
---

# TAM, SAM, and SOM

## Purpose

Build a market size that survives contact with finance.

Bottom-up, cited, and expressed in **both currency and number of customers** — because the customer count is what exposes an unbelievable model fastest. A $400M SOM sounds fine until it implies signing eleven hundred customers in three years with a sales team of nine.

The **sensitivity is the deliverable**. The point estimate is decoration. Business cases do not die because a number was wrong; they die because nobody could say what would have to be true for it to be right.

This skill consumes a denominator and a capture rate. Where an input has no source, the honest entry is **"no evidence found"** and the layer it feeds is not computed.

## When to Use It

Use it before a business case meets finance, before an entry decision, and whenever a sizing number is being quoted that nobody can trace.

Do not use it when:

- **You do not have a denominator.** Run `mi-collect-geoint-demoint` first. Sizing without a count of the eligible population is arithmetic on a guess.
- **You do not have a capture-rate basis.** Run `mi-collect-finint` on a comparable — revenue over claimed customer count is a deal-size reality check that optimism cannot supply.
- **The category is too new to be counted.** Say so, size against the nearest adjacent code with the substitution declared, and label the whole model an Assumption.
- **The question is where to grow rather than how big it is.** That is `mi-analyze-ansoff`.

## Input

Require:

- the **denominator** — establishment or population counts, with vintage
- a **capture-rate basis** — ideally a comparable company's revenue divided by claimed customer count
- the real eligibility constraints that turn TAM into SAM: geography, segment, compliance requirements, technical prerequisites, vendor-registration eligibility

Anything supplied in the invocation, attachments, a GEOINT sweep, a FININT sweep, or earlier conversation counts as context already given.

**Sizing runs get a four-question budget** rather than three, because the constraint set is wider.

**Example invocation:** `Use $mi-size-tam-sam-som using the GEOINT denominator and the FININT capture rate in this thread. US only. Decision: whether the segment funds a dedicated team.`

## Key Concepts

**Every input carries a source, a vintage, and a label** — Numbers without provenance are the single most common way a business case dies in front of finance. Not because they are wrong, but because they cannot be defended when asked, and the inability to answer discredits the numbers that *were* sourced. Vintage matters as much as source: a 2019 establishment count answering a 2026 question is a Fact about 2019 and an Assumption about now.

*Violation signal:* A figure appears in the model with no citation, or with a publication date standing in for the period the data describes.

**Both currency and customers, at every layer** — Express TAM, SAM, and SOM in money *and* in number of organizations. The customer count is the reality check: it converts an abstract revenue figure into a number of logos someone has to sign, at a cadence someone has to staff. Most implausible models are implausible in the customer column and invisible in the currency column.

*Violation signal:* The model is expressed entirely in currency, so nobody can tell how many customers the SOM implies.

**Capture rate comes from FININT, not from optimism** — A comparable company's revenue divided by their claimed customer count gives an implied deal size, and that is the reality check on your own. The capture rate itself needs **a horizon of three to five years and a named comparable**. A percentage with neither is a number chosen to make the model work.

*Violation signal:* A SOM carries a capture rate with no comparable company named and no horizon stated.

**Refuse "1% of a large market"** — This is not a model. It is a wish with arithmetic, and it inverts the work: a real model builds up from countable things and *derives* a percentage, which may turn out to be 0.3% or 4%. Starting from the percentage means the answer was chosen first. Refuse it explicitly rather than quietly building something better, because the phrase will otherwise reappear in the deck.

*Violation signal:* A share assumption appears before a count, anywhere in the model.

**Conflicting estimates are reported, never averaged** — Where two independent analyst reports disagree by threefold, report both, explain the gap (usually category definition), and adopt neither. Averaging produces a number that describes no market and that nobody can defend, and picking the flattering one guarantees that the person who found the other one is the CFO.

*Violation signal:* A single external market size is cited where several exist, or a midpoint appears with no source.

**The sensitivity is the deliverable** — Best, base, and worst, each with the *specific assumption that moves it*. Not three numbers 20% apart, but three scenarios distinguished by a named belief. The value is in showing which assumption the case actually hinges on, so the room can argue about that one thing instead of about the total.

*Violation signal:* Best and worst cases are the base case scaled up and down by a round percentage.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a bottom-up sizing run — TAM, SAM, SOM in both currency and customers, every input sourced with its vintage, ending on the sensitivity. One to two hours. Sizing gets four setup questions rather than three, because the constraint set is wider. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, cap of four:

1. `Sizing Setup Q1/4` — Do you have a denominator, or should I take it from a GEOINT sweep?
2. `Sizing Setup Q2/4` — What are the real eligibility constraints that turn TAM into SAM: geography, segment, compliance, technical prerequisites?
3. `Sizing Setup Q3/4` — What is our pricing, and over what horizon should SOM be modelled?
4. `Sizing Setup Q4/4` — Which comparable companies should anchor the capture rate?

In **Context dump** mode, extract supplied figures, attach vintages, flag stale inputs, and compute only what is sourced. In **Best guess** mode, use the most recent complete vintage, a three-year horizon, and the nearest comparable, naming every assumption. On silence: three-year horizon, US only, most recent vintage. Proceed.

## What It Produces

Complete the [TAM/SAM/SOM Model](template.md):

- executive summary: three numbers in currency and customers
- TAM, SAM, SOM breakdown with every input sourced, dated, and labeled
- method declared: **bottom-up-built** or **top-down-validated**, never blended silently
- key assumptions, each labeled
- **best / base / worst with the assumption that moves each**
- conflicting external estimates, reported as conflicts
- sources, Final Step block

## Workflow

1. **State web access in one line,** and state that this run consumes a denominator rather than producing one.
2. **Refuse the percentage-first framing** if it appears, and say why.
3. **Establish the denominator** with its source and vintage. If it is stale against the decision horizon, say so before computing anything on top of it.
4. **Build TAM:** eligible establishment or population counts times a spend or employment benchmark. Cite both.
5. **Validate TAM against two independent external estimates.** If they disagree by threefold, report both and explain the gap. Do not pick.
6. **Build SAM** by applying real constraints: geography, segment, compliance, technical prerequisites, vendor eligibility. Each constraint gets a stated basis.
7. **Build SOM** as SAM times a capture rate derived from FININT, over a three-to-five-year horizon, against a named comparable.
8. **Express every layer in currency and customers.** Check the customer column for plausibility against your actual sales capacity, and say so if it fails.
9. **Declare the method:** bottom-up-built or top-down-validated. Never blend without saying so.
10. **Write the sensitivity:** best, base, worst, each distinguished by a named assumption rather than by a percentage. Then stop.

## Human Decision Gate

Present the sensitivity first, then the model. Highlight:

- the assumption the case actually hinges on
- the customer count implied by SOM, against current sales capacity
- the oldest vintage in the model
- where external estimates conflict, and by how much

Use an Adaptive Decision Ladder: `Take the base case into the business case`, `Reduce the hinge assumption's uncertainty first`, `Re-run with different eligibility constraints`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every input **Fact** (published statistic or filing), **Inference** (derived, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** establishment counts, market sizes, growth rates, pricing benchmarks, adoption rates, capture rates, or competitor revenue. This model becomes a budget, and every number in it will eventually be checked by someone with an incentive to check it.
- State vintage separately from publication date on every statistic.
- Distinguish audited competitor revenue from company-reported customer counts.
- Report conflicting external estimates. Never average.
- If a layer cannot be computed from sourced inputs, say so rather than estimating it.

## Common Failure Modes

- Starting from a percentage of somebody else's headline number
- Expressing the model only in currency, hiding an implausible customer count
- Using a capture rate with no comparable and no horizon
- Averaging two conflicting analyst estimates
- Blending top-down and bottom-up silently
- Treating a publication date as a vintage
- Producing a point estimate with a decorative sensitivity band
- Summing counts across countries that use different units — establishments versus enterprises

## Assets and Examples

- [TAM/SAM/SOM Model template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Take the base case into the business case (Recommended)
2. Reduce the hinge assumption's uncertainty before presenting
3. Schedule an annual refresh, since sizing rot is slow but real
4. Run Ansoff to choose which slice of the SAM to pursue first

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: the TAM/SAM/SOM recipe under GEOINT/DEMOINT](../../reference/disciplines.md)
- [The act layer: sizing discipline rules](../../reference/frameworks.md)
- [Regional overlays: statistics bureaus](../../reference/regional-overlays.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [US Census County Business Patterns](https://www.census.gov/programs-surveys/cbp.html)
