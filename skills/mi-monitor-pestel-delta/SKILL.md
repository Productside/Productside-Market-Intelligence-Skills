---
name: mi-monitor-pestel-delta
description: Re-scan macro factors quarterly against a prior baseline — what moved, what broke, what entered the frame. Use when an artifact may be resting on something that is no longer true.
license: CC-BY-NC-ND-4.0
argument-hint: "[market] [prior PESTEL file]"
intent: >-
  Diff political, economic, social, technological, environmental, and legal
  factors against a stored baseline. Exists because the value of PESTEL is in what
  moved, and because a first pass presented as a delta tells the reader everything
  changed when nothing was compared.
type: monitor
theme: market-competitive-intelligence
stage: monitor
discipline: All-Source Fusion
status: active
operating-level:
  - initiative
  - executive
audience:
  - Product Manager
  - Business Analyst
  - Strategy and Corporate Development
  - Risk and Compliance
  - Executive Leadership
best-for:
  - "Finding which prior artifact now rests on something that is no longer true"
  - "Catching a factor entering the frame that was irrelevant last quarter"
  - "Reporting 'no material movement' honestly instead of writing a horoscope"
scenarios:
  - "A regulation entered consultation and nobody has assessed what it touches"
  - "Our market entry case assumed conditions that may have changed"
  - "We do a PESTEL every year and nobody reads it twice"
  - "Leadership wants to know what moved outside our control this quarter"
evidence-required:
  - "A prior PESTEL baseline to diff against"
  - "The market and geography in scope"
  - "The artifacts that rest on macro assumptions"
produces:
  - "Run header naming the prior baseline and the window"
  - "Factor-by-factor delta: moved, or no material movement"
  - "Broken assumptions, with the artifact each one breaks"
  - "New to the frame, and the so-what"
estimated-time: "45-90 min"
group-size: "1-6"
consumes:
  - mi-fuse-all-source
  - mi-scan-market-landscape
combine-with:
  - mi-analyze-five-forces
  - mi-size-tam-sam-som
  - mi-watch-competitors
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, the diff layer"
  - "PESTEL delta discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "PESTEL Delta Monitor"
  short_description: "What moved outside our control"
  brand_color: "#00E874"
  default_prompt: "Use $mi-monitor-pestel-delta to diff macro factors against our prior baseline, report only material movement, name which prior artifacts now rest on broken assumptions, and stop."
  allow_implicit_invocation: true
---

# PESTEL Delta Monitor

## Purpose

Re-scan the macro frame and report what moved.

Political, economic, social, technological, environmental, legal — external forces only, none of them controllable. The first PESTEL is a baseline; **the value is entirely in the delta**. What moved, what broke, and what entered the frame that was not in it last quarter.

The section that earns the run is **broken assumptions**: which prior artifact — a sizing model, an entry case, a roadmap bet, a pricing corridor — now rests on something that is no longer true. A macro scan that names no affected artifact has produced background reading.

**A PESTEL where all six factors moved every quarter is not monitoring, it is horoscope writing.** "No material movement" is a valid and useful entry, and most quarters most factors will earn it.

## When to Use It

Use it quarterly, after a baseline exists. Use it when a regulation enters consultation, a currency crosses a threshold, or a technology becomes table stakes. Use it before re-committing to a business case whose macro assumptions are a year old.

Do not use it when:

- **No baseline exists.** **Stop and say so.** Offer to run a baseline PESTEL first. A first pass wearing a delta's headers tells the reader everything moved when in fact nothing was compared — and it is the single most common failure of this run.
- **The question is industry structure rather than macro conditions.** That is `mi-analyze-five-forces`.
- **The question is competitor behavior.** That is `mi-watch-competitors`.
- **You want a strategy.** PESTEL names external conditions. What to do about them belongs to Ansoff, sizing, or the roadmap.

## Input

Require:

- **a prior PESTEL baseline to diff against**, named — or an explicit acknowledgment that none exists
- the market and geography in scope, at country level
- the artifacts that rest on macro assumptions, so broken ones can be named

Anything supplied in the invocation, attachments, a stored prior baseline, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-monitor-pestel-delta on mid-market RevOps tooling, US and Germany, diffing against revops-pestel-2026-05-12.md.`

## Key Concepts

**A delta needs a baseline, and the stop rule is absolute** — If no prior PESTEL exists in session or on file, say so and offer to run a baseline first. Do not run a first pass and label it a delta. This is the discipline's hardest rule to follow, because producing *something* feels more useful than producing a refusal — and a baseline mislabeled as a delta will be read as "six factors moved this quarter," which is alarming, wrong, and unfalsifiable.

*Violation signal:* Every factor has a "was" state that appears nowhere in any prior document.

**Each factor either moved materially or it did not** — Two entry types, and no third. "Moved" gets was, now, read, and what it changes. "No material movement" gets one line and nothing else. The one-line entry is not laziness; it is the filter working, and a report where it never appears has stopped filtering.

*Violation signal:* Every factor entry is a paragraph, and none says a factor held steady.

**Broken assumptions is the section that earns the run** — Name the prior artifact, the assumption inside it, and what is now true instead. A sizing model built on a wage trend that reversed, an entry case built on a regulatory regime that changed, a pricing corridor built on an exchange rate that moved. Without this section a PESTEL is a current-affairs summary with headings.

*Violation signal:* The report describes macro movement and names no artifact affected by it.

**New to the frame catches what was previously irrelevant** — A factor that did not matter last quarter and does now: a regulation entering consultation, a currency crossing a threshold that changes a pricing corridor, a technology becoming table stakes, an environmental disclosure regime reaching your customers' size band. These arrive without warning precisely because nobody was watching a factor that did not apply.

*Violation signal:* The report only re-examines the factors the baseline already contained.

**External and uncontrollable only** — If you can decide it, it is not a PESTEL factor. Your own pricing, roadmap, and hiring belong elsewhere. Competitor behavior belongs in the competitive watch. Mixing controllables in produces a document where the reader cannot tell what is weather and what is a choice.

*Violation signal:* A factor entry describes something the company could change by deciding to.

**Movement needs a threshold, not a direction** — This is the run's materiality threshold, and it is what separates a monitor from a newsfeed. "Interest rates rose" is a fact about the world. "Interest rates crossed the level at which our buyers' capex approvals require board sign-off" is a finding about your market. Material movement is movement past a threshold that matters to a named artifact; everything else is news.

*Violation signal:* A factor is reported as moved because a number changed, with no threshold named.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a PESTEL delta — six factors diffed against the prior baseline, reporting only material movement, ending in broken assumptions and what is new to the frame. Forty-five to ninety minutes. If no baseline exists I will stop and offer to build one instead. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `PESTEL Setup Q1/3` — Is there a prior PESTEL to diff against? If not, I will stop rather than run a baseline in delta clothing.
2. `PESTEL Setup Q2/3` — Which market and countries, at country level?
3. `PESTEL Setup Q3/3` — Which artifacts rest on macro assumptions — a sizing model, an entry case, a pricing corridor?

**Best guess is the expected mode for scheduled runs.** Use the stored baseline, the stored scope, and the stored artifact list; name each assumption and proceed. In **Context dump** mode, treat a pasted prior PESTEL as the baseline. On silence: stored baseline, stored scope, quarterly window. If no baseline is found, stop and say so — that refusal is the correct scheduled output.

## What It Produces

Complete the [PESTEL Delta Report](template.md), written to the schema in `reference/monitors.md`:

- run header: **prior baseline named**, window covered, scope, sources swept
- factor-by-factor delta: each factor **moved** (was/now/read/what it changes) or **no material movement** (one line)
- **broken assumptions**, each naming the artifact it breaks
- **new to the frame**
- so-what, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so and do not reconstruct prior macro states from memory.
2. **Check for a baseline. If none exists, stop.** Say so plainly and offer to run a baseline PESTEL instead. Do not proceed.
3. **Name the baseline and the window in the header.**
4. **Take each factor in turn** — political, economic, social, technological, environmental, legal — and ask whether it moved past a threshold that matters to a named artifact.
5. **Write "moved" entries in was/now format** with both sources and dates, plus the read and what it changes.
6. **Write "no material movement" entries in one line** and move on. Expect most factors to be here most quarters.
7. **Work the broken assumptions.** For each artifact resting on macro conditions, check whether its assumption still holds. Name the artifact, the assumption, and what is now true.
8. **Scan for new to the frame** — factors that did not apply last quarter and do now.
9. **Write the so-what,** tied to artifacts rather than to themes.
10. **Store under the naming convention** so the next run can diff against this one.

## Human Decision Gate

Present the broken assumptions first, then the factor deltas. Highlight:

- which artifacts now rest on something untrue
- which factors are new to the frame
- how many factors reported no material movement — a healthy run has several
- what the next quarter should watch

Use an Adaptive Decision Ladder: `Revisit the artifacts with broken assumptions`, `Add the new factor to the standing scope`, `Re-baseline — too much has changed to diff`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every read **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** regulations, effective dates, consultation stages, economic figures, exchange rates, or policy positions. Macro claims reach investment memos and legal reviews, where they are checked by people who know.
- Every "moved" entry carries a prior source and a current source, both dated.
- Distinguish a regulation *proposed* from one *in consultation*, *adopted*, and *in force*. These are four different states with different timelines and are routinely collapsed.
- Name the threshold that makes movement material.
- Report factors that did not move. Silence about a factor is indistinguishable from not checking it.

## Common Failure Modes

- Running a baseline and labeling it a delta
- Reporting all six factors as moved every quarter
- Describing macro movement with no artifact named
- Collapsing "proposed" and "in force" into "coming"
- Including controllables — your own pricing, roadmap, or hiring
- Reporting a number changing with no threshold that matters
- Omitting "new to the frame," so a newly relevant factor stays invisible
- Failing to store the run, so the next quarter has nothing to diff

## Assets and Examples

- [PESTEL Delta Report template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Revisit the artifacts with broken assumptions (Recommended)
2. Add the new factor to the standing monitoring scope
3. Keep the quarterly cadence so the next run is a diff
4. Re-baseline if too much has changed to diff meaningfully

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [Monitors: the PESTEL delta and its stop rule](../../reference/monitors.md)
- [The act layer: PESTEL discipline rules](../../reference/frameworks.md)
- [Regional overlays: regulatory environments by geography](../../reference/regional-overlays.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
