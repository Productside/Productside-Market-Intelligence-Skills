---
name: mi-watch-competitors
description: Diff a competitor watchlist against a prior snapshot, reporting material shifts only, with was/now changelogs and battle-card update flags. Use to make run N+1 a diff instead of a rebuild.
license: CC-BY-NC-SA-4.0
argument-hint: "[watchlist] [prior run file]"
intent: >-
  Run the scheduled delta against a stored prior snapshot: material shifts only,
  was/now format, update flags with owners. Exists because a monitor that
  re-derives everything each time produces a document nobody reads twice, and
  because "no material change" is a valid and valuable output.
type: monitor
theme: market-competitive-intelligence
stage: monitor
discipline: SIGINT
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Product Marketing Manager
  - Competitive Intelligence Analyst
  - Sales Enablement
  - Business Analyst
best-for:
  - "Running a scheduled competitive delta that survives having nobody watching"
  - "Keeping battle cards current without rebuilding them every month"
  - "Reporting 'no material change' honestly instead of manufacturing news"
scenarios:
  - "Our battle cards go stale and nobody notices until a rep is embarrassed"
  - "We need a competitive update every month and rebuilding it each time is not working"
  - "Leadership wants to know what changed, not what is true"
  - "We want this to run on a schedule without a human answering questions"
evidence-required:
  - "A prior snapshot or watch run to diff against"
  - "The watchlist — which competitors and which surfaces"
  - "The artifacts that would need updating"
produces:
  - "Run header with prior run, window, and sources swept"
  - "Changelog of material shifts only, in was/now format"
  - "Update flags with owners and urgency"
  - "Watchlist for the next run, with escalation triggers"
estimated-time: "20-45 min"
group-size: "1-3"
consumes:
  - mi-snapshot-competitors
  - mi-collect-sigint
combine-with:
  - mi-build-battle-card
  - mi-fuse-all-source
  - mi-monitor-pricing-packaging
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, the fusion cadence"
  - "Competitive intel watch discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Competitive Intel Watch"
  short_description: "Material shifts only, run over run"
  brand_color: "#00E874"
  default_prompt: "Use $mi-watch-competitors to diff the watchlist against our prior run, apply the materiality bar, report changes in was/now format with update flags, and say 'no material change' if that is the truth."
  allow_implicit_invocation: true
---

# Competitive Intel Watch

## Purpose

Make run N+1 a diff instead of a rebuild.

A monitor that re-derives everything each time produces a document nobody reads twice, because there is no way to see what changed. This run holds a prior snapshot, sweeps a fixed set of surfaces, applies a **materiality bar**, and reports only what cleared it — in was/now format, with flags naming which artifact needs updating and who owns it.

**"No material change" is a valid and valuable output.** Say it in one line and stop. A monitor that always finds something has stopped filtering, and the moment a reader learns that, every future run is discounted.

This run is built to execute without a human answering questions, which is what makes it schedulable.

## When to Use It

Use it monthly for a full pass and weekly for the fastest-moving surfaces. Use it after a snapshot has established a baseline. Use it as the scheduled job that keeps battle cards from rotting.

Do not use it when:

- **No prior run exists.** Then this is a baseline, not a delta, and it must say so. Run `mi-snapshot-competitors` first — a first snapshot presented as a change report tells the reader everything moved.
- **You need the pricing time series.** That is `mi-monitor-pricing-packaging`, which stores verbatim captures.
- **You need macro factors.** That is `mi-monitor-pestel-delta`.
- **Something material just happened and you need depth.** Run the sweep or `mi-fuse-all-source`; a delta report is the wrong shape for an event.

## Input

Require:

- **a prior snapshot or watch run to diff against**, named
- the watchlist — which competitors, which surfaces
- the artifacts that would need updating: battle cards, pricing, positioning, roadmap

Anything supplied in the invocation, attachments, a stored prior run, or earlier conversation counts as context already given. For a scheduled run, the prior output must be stored where this run can read it — a delta monitor with no access to its own history is a snapshot on a timer.

**Example invocation:** `Use $mi-watch-competitors against analytics-market-watch-2026-07-14.md. Watchlist: Cartelane, Meridian, Northwind.`

## Key Concepts

**The materiality bar is what separates a monitor from a newsfeed** — Report a change only if it clears one of these: it changes what a salesperson would say in a live deal; changes a price, tier, packaging boundary, or eligibility rule; changes who the buyer is or which segment is targeted; changes a stated strategy or removes language previously repeated; adds or removes a capability that appears in competitive evaluations; establishes commitment where there was only announcement; or breaks an assumption a prior artifact rests on.

*Violation signal:* The changelog contains a copy tweak, a new customer logo, or a site redesign that moved the same words.

**Was and now, or it is not a diff** — Every entry pairs the prior state with its prior source and date against the current state with its current source and date. The pairing is the whole trick: it forces you to have actually held the prior state, which is what keeps a "delta report" from being a fresh snapshot with the word delta on it.

*Violation signal:* An entry describes the current state and characterizes it as new, with no prior state recorded.

**A named prior run, always** — The header states which file this diffed against, the window covered, and the sources swept. "Recently" is not a window. A reader has to be able to tell whether silence means nothing happened or nobody looked, and only the header can answer that.

*Violation signal:* The report says what changed without naming the run it changed from.

**Three flag levels, and "update now" means now** — Update now, review, hold. **Update now** means a rep will say something wrong tomorrow if nobody acts. Reserving it for that case is what makes the flag mean anything; flagging four things urgent every month teaches the field to ignore all four.

*Violation signal:* Most entries in a run carry the highest urgency.

**Silence is a finding** — A run that reports one line and a date has done its job. Resist justifying the run's existence with volume, and track consecutive quiet runs in the header — a competitor with three silent months is itself a signal worth noticing, usually of internal focus elsewhere.

*Violation signal:* Every run produces roughly the same amount of content.

**The next-run watchlist is what compounds** — Close every run by naming the specific things to check first next time and the trigger that would escalate each. Without it, every run starts from zero and the series never gets cheaper or sharper.

*Violation signal:* The report ends at the update flags, so the next run has no memory.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a scheduled competitive watch — diffed against the prior run, material shifts only, was/now format, with update flags. Twenty to forty-five minutes. If nothing cleared the bar I will say so in one line. Up to three setup questions, and this run proceeds without answers if nobody is here. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Watch Setup Q1/3` — Which prior run should I diff against?
2. `Watch Setup Q2/3` — Has the watchlist changed since last run?
3. `Watch Setup Q3/3` — Which artifacts should update flags point at, and who owns them?

**Best guess is the expected mode for scheduled runs.** Use the most recent stored run as the baseline, the stored watchlist, the standard materiality bar, and the stored artifact owners. Name each assumption in the header and proceed without waiting. In **Context dump** mode, treat a pasted prior snapshot as the baseline. On silence: stored baseline, stored watchlist, standard bar. Proceed.

## What It Produces

Complete the [Competitive Watch Report](template.md), written to the schema in `reference/monitors.md`:

- run header: as-of date, **prior run named**, window covered, scope, sources swept, consecutive no-change runs
- changelog: material shifts only, in was/now format, each with a read and a commitment level
- update flags: artifact, flag level, why, owner
- **watchlist for next run**, with escalation triggers
- assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so and do not reconstruct prior states from memory.
2. **Load the prior run and name it in the header.** If none exists, declare this a baseline capture, not a delta, in the header rather than a footnote.
3. **State the window explicitly.** The date range since the prior run.
4. **Sweep the fixed surface set:** pricing pages → positioning and homepage messaging → product and changelog → job posting deltas → funding, filings, and leadership → certifications → notable customer or partner announcements.
5. **Apply the materiality bar to every observed change.** Below the bar: copy tweaks, blog cadence, new logos on a customer wall, conference attendance, headcount noise under the baseline, redesigns that move the same words.
6. **Write each surviving change in was/now format,** with both sources and both dates.
7. **Add a read and a commitment level** to each: Announced, Funded, Procured, Staffed, or Built.
8. **Set update flags** with owners. Reserve "update now" for a rep saying something wrong tomorrow.
9. **Write the next-run watchlist** with escalation triggers.
10. **Store the output** under the naming convention so the next run can read it, and name the storage location in the header.

If nothing cleared the bar, write one line, note the consecutive-quiet count, and stop.

## Human Decision Gate

Present the changelog and flags. Highlight:

- anything flagged update now, and what breaks if it waits
- changes that moved a story up the commitment ladder
- how many consecutive runs have been quiet
- what the next run should check first

Use an Adaptive Decision Ladder: `Act on the update-now flags`, `Fuse this with the other disciplines`, `Adjust the materiality bar — too much or too little is getting through`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every read **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** prior states, prices, dates, capabilities, headcounts, or certifications. A fabricated prior state is uniquely corrosive here — it manufactures a change that never happened and sends the field to correct something that was never wrong.
- Every was/now pair carries two sources and two dates.
- If a prior state cannot be established, log the item as a baseline capture rather than as a change.
- Distinguish a real change from a redesign that relocated identical wording.
- Report the absence of change explicitly; do not omit a quiet competitor silently.

## Common Failure Modes

- Reporting a current state as a change because the prior state was never held
- Manufacturing news to justify the run
- Flagging everything "update now"
- Running without naming the prior run, so nobody can tell what was compared
- Letting a site redesign read as a messaging shift
- Changing the schema between runs, which breaks every future diff
- Omitting the next-run watchlist, so the series never compounds
- Blocking on a question during a scheduled run

## Assets and Examples

- [Competitive Watch Report template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Act on the update-now flags (Recommended)
2. Fuse this with the other disciplines for a threat read
3. Keep the schedule, and check the next-run watchlist first
4. Adjust the materiality bar if too much or too little is getting through

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [Monitors: the diff layer, materiality bar, and cadence](../../reference/monitors.md)
- [Output schemas and the storage convention](../../reference/output-schemas.md)
- [The disciplines: SIGINT](../../reference/disciplines.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
