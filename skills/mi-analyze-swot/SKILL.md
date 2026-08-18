---
name: mi-analyze-swot
description: Build a SWOT from fused evidence with quadrant discipline, ranked entries, and the S-O and W-T crossings that make it a decision. Use when the evidence exists and a position must be stated.
license: CC-BY-NC-SA-4.0
argument-hint: "[company] [fused evidence]"
intent: >-
  Turn fused competitive evidence into a SWOT that survives a hostile read:
  quadrant discipline enforced, every entry sourced and ranked, and the crossings
  written. Exists because most SWOTs are four lists that change nothing, and
  because an opportunity requiring you to act is a strategy in the wrong box.
type: analysis
theme: market-competitive-intelligence
stage: act
discipline: All-Source Fusion
status: active
operating-level:
  - product-team
  - initiative
  - executive
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - Strategy and Corporate Development
  - Executive Leadership
best-for:
  - "Stating a position on one company from evidence that already exists"
  - "Catching the quadrant errors that make a SWOT a wish list"
  - "Producing the S-O and W-T crossings that turn four lists into a decision"
scenarios:
  - "Leadership wants a SWOT and we have three sweeps and a fusion brief"
  - "Our last SWOT had a competitor's product filed as a weakness"
  - "We need a position on ourselves that customer evidence actually supports"
  - "The SWOT deck lists twenty items per quadrant and decides nothing"
evidence-required:
  - "Fused evidence, or sweep outputs, with sources and dates"
  - "Whose SWOT this is — us, or a competitor"
  - "The decision it supports"
produces:
  - "Four quadrants, max five entries each, every entry sourced and labeled"
  - "Ranked entries with the stated ranking basis per quadrant"
  - "S-O and W-T crossings with a named move"
  - "Quadrant corrections made visible"
estimated-time: "45-90 min"
group-size: "1-8"
consumes:
  - mi-fuse-all-source
  - mi-snapshot-competitors
combine-with:
  - mi-analyze-five-forces
  - mi-analyze-ansoff
  - mi-build-battle-card
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, the act layer"
  - "SWOT discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "SWOT From Evidence"
  short_description: "SWOT with sources and the crossings"
  brand_color: "#00E874"
  default_prompt: "Use $mi-analyze-swot to build a SWOT from the evidence we already hold, enforce quadrant discipline, rank every entry on a stated basis, and write the S-O and W-T crossings."
  allow_implicit_invocation: true
---

# SWOT From Evidence

## Purpose

Turn fused evidence into a position that survives a hostile read.

A SWOT is not four lists. It is a claim about where you stand, and the part that makes it a decision is the **crossings**: which strength lets you take which opportunity this quarter, and which weakness gets exposed by which threat. Without those, a SWOT is a workshop artifact that gets photographed and never referenced.

This skill consumes evidence; it does not manufacture it. Where a quadrant has no cited signal behind an entry, the honest entry is **"no evidence found"** — not a plausible sentence. A quadrant filled to look complete is the failure mode that makes SWOT the most-mocked framework in product management, and it is entirely avoidable.

## When to Use It

Use it when the evidence exists and a position must be stated — a board question, a planning cycle, a positioning reset. Use it on a competitor as readily as on yourself.

Do not use it when:

- **You do not have the evidence yet.** Run the sweeps and `mi-fuse-all-source` first. A SWOT built from opinion is a record of the room's mood.
- **The question is industry structure.** That is `mi-analyze-five-forces` — SWOT reads one player's position, forces reads whether the industry is worth being in.
- **The question is where to grow.** That is `mi-analyze-ansoff`.
- **You want a facilitation exercise.** This produces an evidence-bound artifact; it does not run a workshop.

## Input

Require:

- fused evidence, or sweep outputs, with sources and dates
- whose SWOT this is — us, or a named competitor
- the decision it supports

Anything supplied in the invocation, attachments, a fusion brief, or earlier conversation counts as context already given. If the evidence is thin in one quadrant, that is a finding to report, not a gap to fill.

**Example invocation:** `Use $mi-analyze-swot on us, using the fusion brief in this thread. Decision: what we defend and what we concede in next year's plan.`

## Key Concepts

**Quadrant discipline is the whole game** — Strengths and weaknesses are **internal and current**. Opportunities and threats are **external and not controllable**. Almost every bad SWOT fails here, and the two failures are specific and nameable: a competitor's product filed as a weakness (it is a threat — it is theirs, not yours), and an "opportunity" that requires you to act. Making the corrections visible teaches the rule better than stating it.

*Violation signal:* An entry in strengths or weaknesses describes something another company does.

**An opportunity that requires you to act is a strategy** — "Expand into healthcare" is not an opportunity; it is a plan. The opportunity is the external condition that makes it viable: a regulation creating demand, a competitor exiting, a buyer population growing. Filing strategies as opportunities is the most common way a SWOT quietly becomes a wish list, and it is invisible because wish lists read as ambition.

*Violation signal:* An opportunity entry starts with a verb you control.

**Five per quadrant, ranked on a stated basis** — Rank strengths on **defensibility**, weaknesses on **exploitability**, opportunities on **fit to your strengths**, and threats on **likelihood times damage**. Say which basis you used. An unranked quadrant treats a durable moat and a temporary advantage as equivalent, and the ranking is where the judgment lives.

*Violation signal:* Entries appear in the order they were thought of, with no basis named.

**Customer voice weighs heaviest in weaknesses** — What your own users say about you outranks internal opinion about yourself. Teams are systematically wrong about their own weaknesses in a predictable direction: they list what they know they have not built, and omit what customers actually struggle with. A weakness with a customer quote behind it is worth five without.

*Violation signal:* The weaknesses quadrant is a roadmap backlog, with no customer evidence in it.

**The crossings are the so-what** — **S-O:** which strength lets you take which opportunity, and what to do this quarter. **W-T:** which weakness gets exposed by which threat, and what protects it. Optionally S-T (defend) and W-O (invest to qualify). A SWOT without crossings is a list; with them it is a plan with evidence attached.

*Violation signal:* The document ends at the fourth quadrant.

**"No evidence found" is a valid entry** — A quadrant with two well-sourced entries beats one with five, three of which are plausible sentences. Empty space in a SWOT is informative: it says where you are not looking, or where nothing is currently true.

*Violation signal:* All four quadrants contain exactly five entries.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a SWOT built from evidence you already hold. Four quadrants, max five entries each, every entry sourced and ranked, ending with the S-O and W-T crossings. Forty-five to ninety minutes. Where evidence is missing I will write 'no evidence found' rather than fill the box. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `SWOT Setup Q1/3` — Whose SWOT is this: ours, or a named competitor's?
2. `SWOT Setup Q2/3` — What decision does it support?
3. `SWOT Setup Q3/3` — Is there customer evidence about weaknesses — reviews, win/loss, support themes — that I should weight above internal opinion?

**Context dump is the expected mode**, since this skill normally begins with a fusion brief or sweep outputs. Extract entries, sort them into quadrants, show the corrections you made, and ask only about gaps. In **Best guess** mode, build from available evidence, mark unsupported entries as "no evidence found," and name each assumption. On silence: our own SWOT, planning-cycle framing, customer evidence weighted first. Proceed.

## What It Produces

Complete the [SWOT](template.md):

- four quadrants, max five entries each, every entry with a source, date, and F/I/A label
- ranking within each quadrant on the stated basis
- **quadrant corrections made visible** — what was moved, and why
- S-O and W-T crossings, each with a named move and an owner
- entries marked "no evidence found" where they belong
- assumptions to validate, Final Step block

## Workflow

1. **State web access in one line,** and state that this run consumes evidence rather than collecting it.
2. **Establish whose SWOT this is.** The same evidence produces different quadrants for us and for a competitor.
3. **Sort candidate entries into quadrants, applying discipline as you go.** Internal and current on the left; external and uncontrollable on the right.
4. **Show your corrections.** When you move a competitor's product from weaknesses to threats, or a strategy from opportunities out entirely, say so. The corrections teach the rule.
5. **Attach a source, date, and label to every entry.** Anything unsupported becomes "no evidence found," and the quadrant stays short.
6. **Weight customer voice heaviest in weaknesses.** Reviews, win/loss, support themes outrank internal opinion.
7. **Cap at five per quadrant and rank** on the stated basis: defensibility, exploitability, fit to strengths, likelihood times damage.
8. **Write the S-O crossings:** which strength takes which opportunity, and the move this quarter.
9. **Write the W-T crossings:** which weakness meets which threat, and what protects it.
10. **Name the assumptions** that would most change the picture, and stop.

## Human Decision Gate

Present the crossings first, then the quadrants. Highlight:

- which entries were moved between quadrants, and why
- which quadrants are short because evidence was missing
- the W-T crossing with the highest likelihood-times-damage
- whether the weaknesses quadrant reflects customers or internal opinion

Use an Adaptive Decision Ladder: `Act on the top S-O and W-T crossings`, `Collect evidence for the thin quadrant first`, `Run the same SWOT on the competitor for contrast`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every entry **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** competitor capabilities, market conditions, customer sentiment, regulatory changes, or internal metrics. A SWOT is presented to leadership as a considered position, which makes an invented entry uniquely durable — it will be repeated for a year.
- Every entry carries a source and a date, or reads "no evidence found."
- An internal opinion about your own weakness is an Assumption unless customer evidence supports it.
- Threats must be external and outside your control; if you can decide it, it is not a threat.
- Do not average conflicting evidence into a moderate entry.

## Common Failure Modes

- Filing a competitor's product as a weakness rather than a threat
- Filing a strategy as an opportunity
- Filling all four quadrants to five because the template has five rows
- Listing the roadmap backlog as weaknesses, with no customer evidence
- Ranking nothing, so a moat and a temporary edge look equivalent
- Ending at the fourth quadrant with no crossings
- Building the SWOT from the room's opinion rather than from fused evidence
- Writing plausible entries where evidence is absent

## Assets and Examples

- [SWOT template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Act on the top S-O and W-T crossings (Recommended)
2. Collect evidence for the thin quadrant before presenting this
3. Schedule a semi-annual refresh so the position is tracked
4. Run the same SWOT on the competitor for contrast

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The act layer: SWOT discipline rules](../../reference/frameworks.md)
- [Fusion: what feeds this framework](../../reference/fusion.md)
- [The disciplines](../../reference/disciplines.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
