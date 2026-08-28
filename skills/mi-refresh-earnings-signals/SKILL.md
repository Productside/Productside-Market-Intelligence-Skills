---
name: mi-refresh-earnings-signals
description: Diff a company's strategy language quarter over quarter — shifted signals, dropped language, new deflections. Use when how a competitor talks is the leading indicator of what they do.
license: CC-BY-NC-SA-4.0
argument-hint: "[company] [prior profile file]"
intent: >-
  Diff executive language against a prior profile: what shifted, what disappeared,
  and which analyst question now gets the longest non-answer. Exists because
  dropped language is the most underused signal in competitive intelligence -- a
  phrase repeated four quarters and absent in the fifth records a decision already
  made.
type: monitor
theme: market-competitive-intelligence
stage: monitor
discipline: FININT
status: active
operating-level:
  - initiative
  - executive
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - Competitive Intelligence Analyst
  - Strategy and Corporate Development
best-for:
  - "Catching a strategy change in the language before it appears in the product"
  - "Tracking disappearance as carefully as appearance"
  - "Finding which analyst question now gets the longest non-answer"
scenarios:
  - "They stopped saying something they said in four consecutive calls"
  - "A segment got promoted in the reporting structure and nobody noticed"
  - "We need a quarterly read on a public competitor without rebuilding the profile"
  - "Their metrics changed and we want to know what stopped being flattering"
evidence-required:
  - "A prior profile or earnings refresh to diff against"
  - "The company and its filing and call cadence"
  - "The artifacts that rest on their stated strategy"
produces:
  - "Run header naming the prior profile and the quarters compared"
  - "Shifted signals: strategy language, segment emphasis, metric selection"
  - "Dropped language — tracked as carefully as new language"
  - "Deflection log and the so-what"
estimated-time: "45-90 min"
group-size: "1-3"
consumes:
  - mi-collect-finint
  - mi-sweep-full-spectrum
combine-with:
  - mi-fuse-all-source
  - mi-build-battle-card
  - mi-watch-competitors
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, FININT and the diff layer"
  - "Earnings and executive signal refresh discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.sec.gov/edgar/search/
interface:
  display_name: "Earnings and Executive Signal Refresh"
  short_description: "Diff how they talk, quarter over quarter"
  brand_color: "#00E874"
  default_prompt: "Use $mi-refresh-earnings-signals to diff this company's strategy language against the prior profile: shifted signals, dropped language, changed metrics, and the questions executives now deflect."
  allow_implicit_invocation: true
---

# Earnings and Executive Signal Refresh

## Purpose

Read what changed in how they talk, because it is a leading indicator of what changes in what they do.

Executives are careful with language on the record. When a phrase repeated in four consecutive calls is absent in the fifth, that absence is a decision already made internally, weeks or quarters before it appears in a product, a price, or an org chart. **Dropped language is the most underused signal in competitive intelligence**, precisely because it leaves nothing to notice.

This is a diff, not a profile. It holds a prior profile, compares the current quarter's language against it, and reports the shifts.

## When to Use It

Use it quarterly on a public competitor you have already profiled. Use it when a segment appears to have been promoted or folded. Use it when a battle card's positioning layer needs to know whether their story changed.

Do not use it when:

- **No prior profile exists.** Then this is a baseline. Run `mi-collect-finint` or `mi-sweep-full-spectrum` first — a first pass presented as a quarterly diff will read as though everything shifted.
- **The company is private and holds no calls.** Say so plainly; this discipline has almost no surface on a private target beyond occasional interviews and conference talks.
- **You need the financial position rather than the language.** That is `mi-collect-finint`.
- **You need competitor surface changes.** That is `mi-watch-competitors`.

## Input

Require:

- **a prior profile or earnings refresh to diff against**, named
- the company and its filing and call cadence
- the artifacts that rest on their stated strategy — battle cards, positioning briefs, threat assessments

Anything supplied in the invocation, attachments, a stored prior profile, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-refresh-earnings-signals on Meridian, diffing against meridian-earnings-refresh-2026-05-20.md.`

## Key Concepts

**Track disappearance as carefully as appearance** — New language is easy to notice and everyone reports it. Dropped language requires holding the prior text and looking for absence, which nothing prompts you to do. A phrase repeated in four consecutive calls and absent in the fifth is the strongest single signal this discipline produces, and it is invisible without the prior profile open beside the current transcript.

*Violation signal:* The report lists what executives said this quarter and never says what they stopped saying.

**The deflection is the signal** — Analysts ask; executives deflect. A prepared non-answer marks a topic the company has decided not to discuss, and it is more informative than any answer given. Track which question got the longest non-answer, and track it across quarters — a question deflected twice is a soft spot, and a question that was answered last quarter and deflected this quarter is a change.

*Violation signal:* The earnings section quotes executive statements and never records what they were asked and did not answer.

**A named prior profile and named quarters** — The header states which profile this diffed against and which quarters are being compared. Without it, a reader cannot tell whether a "shift" is a quarter-over-quarter change or a year-old condition being noticed for the first time.

*Violation signal:* A shift is reported with no prior quarter named and no prior text quoted.

**Metric selection is strategy** — Which metrics executives lead with, and which they stop reporting, is a choice made in advance by people who know what the numbers will look like. A metric that disappears from the opening remarks has usually stopped being flattering, and a new metric introduced with an explanation of why it is "the better measure" is nearly always replacing one that got worse.

*Violation signal:* The report notes a new metric without checking which one it displaced.

**Segment promotion and folding** — A segment getting its own reporting line means management intends to be measured on it. A segment folded into another means the opposite. These are structural, deliberate, and disclosed — and they say more about resource allocation than any strategy slide.

*Violation signal:* A reporting-structure change is reported as an accounting detail rather than as a priority signal.

**Rephrasing is not a shift** — The materiality bar for this run: report a language change only if it changes a stated strategy, removes language previously repeated, changes segment emphasis or metric selection, or breaks an assumption a prior artifact rests on. Executives rewrite sentences every quarter; a report that treats every rewrite as a signal is a newsfeed with quotation marks.

*Violation signal:* A "shift" is reported where the meaning is identical and only the wording moved.

**Language is intent, not commitment** — Everything here is what a company *says*, which sits at Announced on the commitment ladder. It is a leading indicator worth having early, and it is not evidence that anything is funded, procured, staffed, or built. Pair it with the money before rating a story.

*Violation signal:* A language shift is reported as an established strategic move.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a quarterly language diff — shifted signals, dropped language, metric changes, and deflections, against the prior profile. Forty-five to ninety minutes. Everything here is intent, not commitment. Up to three setup questions, and this run proceeds without answers. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Refresh Setup Q1/3` — Which prior profile should I diff against?
2. `Refresh Setup Q2/3` — Which artifacts rest on their stated strategy, so I can flag what needs updating?
3. `Refresh Setup Q3/3` — Is there a specific claim of theirs you want tracked across quarters?

**Best guess is the expected mode for scheduled runs.** Use the stored prior profile, the last four quarters of calls, and the stored artifact list; name each assumption and proceed. In **Context dump** mode, treat a pasted prior profile as the baseline. On silence: stored profile, four-quarter language window. Proceed.

## What It Produces

Complete the [Earnings and Executive Signal Refresh](template.md), written to the schema in `reference/monitors.md`:

- run header: **prior profile named**, quarters compared, sources
- **shifted signals**: strategy language, segment emphasis, metric selection
- **dropped language**, with the number of consecutive prior quarters it appeared in
- **deflection log**, tracked across quarters
- reporting-structure changes
- so-what and update flags, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so and quote nothing from memory — a fabricated executive quote is attributable, checkable, and damaging.
2. **Load the prior profile and name it in the header,** with the quarters being compared.
3. **Read the current call transcript and the current filing** alongside the prior text, not after it.
4. **Diff the strategy language.** What phrasing changed, and how.
5. **Find the dropped language.** Search the prior profile's repeated phrases against the current transcript, and record how many consecutive quarters each appeared in before disappearing. This step is the run's highest-value work and the one that requires the prior text.
6. **Diff the metrics.** Which are led with, which are new, which stopped being reported, and what each new one displaced.
7. **Check the reporting structure.** Segments split out, folded in, or renamed.
8. **Log the deflections.** Which analyst question got the longest non-answer, and whether it was deflected in a prior quarter too.
9. **Diff the Risk Factors** if an annual filing falls in the window.
10. **Write the so-what**, place every signal at **Announced** on the commitment ladder, set update flags, and store under the naming convention.

## Human Decision Gate

Present dropped language and deflections first — they are the least obvious and most valuable. Highlight:

- any phrase that ran four or more quarters and stopped
- any question deflected in two consecutive quarters
- reporting-structure changes and what they signal about priority
- that everything here is intent, and what would confirm commitment

Use an Adaptive Decision Ladder: `Update the positioning and battle card language`, `Pair this with a FININT sweep to test commitment`, `Track a specific claim across the next two quarters`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every read **Fact** (what was said or filed), **Inference** (what it implies, chain shown), or **Assumption** (basis stated).
- **Do not invent:** executive quotes, analyst questions, metric values, segment names, or call dates. A fabricated quote attributed to a named executive of a public company is the most damaging output in this library — it is attributable, checkable, and defamatory in the wrong hands.
- Quote from transcripts with the call date; paraphrase only when marked as paraphrase.
- State how many consecutive quarters a dropped phrase appeared in, or do not call it dropped.
- Distinguish a phrase absent from prepared remarks but present in Q&A — that is a demotion, not a disappearance.
- Everything in this run sits at **Announced**. Do not rate a story on language alone.

## Common Failure Modes

- Reporting new language and never checking what disappeared
- Calling a phrase dropped after one absent quarter
- Quoting statements without recording what was asked and dodged
- Treating a reporting-structure change as accounting rather than priority
- Reporting a new metric without identifying what it replaced
- Rating a language shift as an established strategic move
- Running without the prior profile open, which makes absence undetectable
- Paraphrasing a quote and presenting it as verbatim

## Assets and Examples

- [Earnings and Executive Signal Refresh template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Update the positioning and battle card language (Recommended)
2. Pair this with a FININT sweep to test whether the language is funded
3. Keep the quarterly cadence so the next run is a diff
4. Track the deflected question across the next two quarters

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [Monitors: the earnings and executive signal refresh](../../reference/monitors.md)
- [The disciplines: FININT](../../reference/disciplines.md)
- [Fusion: the commitment ladder](../../reference/fusion.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SEC EDGAR full-text search](https://www.sec.gov/edgar/search/)
