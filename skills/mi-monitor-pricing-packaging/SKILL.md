---
name: mi-monitor-pricing-packaging
description: Track competitor pricing and packaging as a diffable time series, capturing tiers, units, and limits verbatim before interpreting them. Use when next quarter's pricing question must be answerable.
license: CC-BY-NC-ND-4.0
argument-hint: "[competitors] [prior capture file]"
intent: >-
  Build a pricing time series rather than a pricing opinion. Capture tiers,
  prices, units, inclusions, and limits verbatim, then diff. Exists because a
  tracker that stores only your read of a page cannot answer next quarter's
  question, and next quarter's question is always more specific.
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
  - Pricing and Packaging Lead
  - Sales Enablement
  - Business Analyst
best-for:
  - "Building a pricing time series that answers questions you have not thought of yet"
  - "Catching a packaging overhaul the quarter it happens, not the year after"
  - "Giving deal desk a dated, verbatim record instead of a recollection"
scenarios:
  - "A competitor changed pricing and nobody can remember what it was before"
  - "We need to know whether their record limits moved, and nobody captured them"
  - "Their entry tier disappeared and we want to know what that means"
  - "Deal desk is guessing at competitor discounting"
evidence-required:
  - "The competitors and their pricing pages"
  - "A prior capture to diff against, or an explicit baseline declaration"
  - "The decision this feeds"
produces:
  - "Verbatim capture of tiers, prices, units, inclusions, limits, minimums"
  - "Was/now delta against the prior capture"
  - "Named packaging signals where they appear"
  - "A stored artifact the next run diffs against"
estimated-time: "20-45 min"
group-size: "1-3"
consumes:
  - mi-collect-sigint
  - mi-snapshot-competitors
combine-with:
  - mi-build-battle-card
  - mi-watch-competitors
  - mi-collect-finint
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, SIGINT and the diff layer"
  - "Pricing and packaging tracker discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Pricing and Packaging Tracker"
  short_description: "Capture verbatim, then read the diff"
  brand_color: "#00E874"
  default_prompt: "Use $mi-monitor-pricing-packaging to capture competitor tiers, prices, units, inclusions, and limits verbatim, diff them against the prior capture, and name the packaging signals only where they appear."
  allow_implicit_invocation: true
---

# Pricing and Packaging Tracker

## Purpose

Build a pricing time series, not a pricing opinion.

This is the one monitor where the **raw capture matters as much as the read**. Tier names, list prices, billing periods, units, inclusions, limits, add-ons, minimums, published discounts, trial terms, and the "contact us" boundary — captured verbatim, with a URL and a date, before a word of interpretation.

The reason is simple and easy to underestimate: **next quarter's question is always more specific than this quarter's read.** "Did their record limit move?" cannot be answered by a note saying "pricing simplified." A tracker that stores only your interpretation has destroyed the data it was built to preserve.

## When to Use It

Use it weekly or monthly on a small set of competitors whose pricing actually affects your deals. Use it before a pricing decision of your own. Use it to give deal desk a dated record instead of a recollection.

Do not use it when:

- **You want the full competitive delta.** That is `mi-watch-competitors`, which covers messaging, product, hiring, and filings too.
- **The competitor publishes no pricing.** Capture the "contact us" boundary and what *is* published; say plainly that the rest is unobservable through this channel.
- **You need to know why they changed it.** The read is a hypothesis; FININT's margin language is what would confirm it.
- **You have no prior capture.** Then this run is a **baseline**, and it must say so — a first capture presented as a change report tells the reader everything moved.

## Input

Require:

- the competitors and their pricing pages
- **a prior capture to diff against**, or an explicit baseline declaration
- the decision this feeds

Anything supplied in the invocation, attachments, a stored prior capture, or earlier conversation counts as context already given. For a scheduled run, store the output where the next run can read it.

**Example invocation:** `Use $mi-monitor-pricing-packaging on Cartelane and Meridian, diffing against cartelane-pricing-capture-2026-05-14.md.`

## Key Concepts

**Capture verbatim before interpreting** — Record what the page says, in its words, then read it. This is the discipline's defining rule and the one most often skipped under time pressure, because interpretation feels like the valuable part. It is not: the interpretation is reproducible from the capture, and the capture is not reproducible from the interpretation. Once a page changes, an uncaptured prior state is gone permanently.

*Violation signal:* The record says "pricing simplified" or "moved upmarket" and nowhere preserves what the tiers were called or what they cost.

**Every field, not just the headline price** — Units (seat, usage, hybrid), inclusions, limits, add-ons, minimums, overage rates, trial terms, and the "contact us" boundary. Packaging changes hide in these fields far more often than in the headline number: a price that stays at $119 while the record limit halves is a price increase that no headline reports.

*Violation signal:* The capture has prices and tier names and nothing about what each tier includes or limits.

**A named prior capture and a stated window** — The header names the file this diffed against and the date range covered. Without it a reader cannot tell whether a field is unchanged or unchecked, and a time series with unlabeled gaps is not a series.

*Violation signal:* A change is reported with no prior capture named and no interval stated.

**Signals only where they appear** — A tier disappearing means a packaging overhaul, usually toward enterprise. A feature moving up a tier means monetizing what was previously bait. Usage pricing added alongside seats means hedging against seat compression. "Contact us" replacing a published price means discount flexibility wanted or a quiet increase being tested. A new floor or minimum means firing the bottom of the market. A widening annual discount means cash or retention pressure. **The first two are source doctrine; the rest are working reads offered as extensions.** Name a signal only when its pattern actually appears — attaching an interpretation to every field turns a tracker into a horoscope.

*Violation signal:* Every captured field arrives with a strategic interpretation attached.

**A read is a hypothesis, and often ambiguous** — A widening annual discount is cash pressure *or* a retention play ahead of a repricing. Those point opposite directions about a competitor's health. Say both, and name the discipline that would separate them, rather than choosing the one that fits the story.

*Violation signal:* A pricing change is reported with a single confident explanation of the competitor's motive.

**The series is the asset** — Any single capture is worth little; twelve are worth a great deal. Keep the schema stable, store under the naming convention, and resist improving the format mid-series. A tracker rebuilt in a new shape each quarter has no history, only a present.

*Violation signal:* This run's fields differ from last run's, so the columns cannot be compared.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a pricing and packaging capture — tiers, prices, units, inclusions, limits, and minimums recorded verbatim, then diffed against the prior capture. Twenty to forty-five minutes. If nothing changed I will say so in one line. Up to three setup questions, and this run proceeds without answers. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Pricing Setup Q1/3` — Which competitors, and is there a prior capture to diff against?
2. `Pricing Setup Q2/3` — Are there fields beyond the standard set that matter in your category — overage rates, implementation fees, regional pricing?
3. `Pricing Setup Q3/3` — What decision does this feed: a pricing change, deal desk guidance, or a battle card refresh?

**Best guess is the expected mode for scheduled runs.** Use the stored prior capture, the stored competitor set, and the standard field list; name each assumption in the header and proceed. In **Context dump** mode, treat a pasted prior capture as the baseline. On silence: stored baseline, stored set, standard fields. Proceed.

## What It Produces

Complete the [Pricing and Packaging Capture](template.md):

- run header: **prior capture named**, window, competitors, capture URLs
- **verbatim capture table per competitor** — every field
- was/now delta, per changed field
- named packaging signals, only where their pattern appears
- ambiguous reads flagged with their disambiguator
- a stored artifact under the naming convention

## Workflow

1. **State web access in one line.** Without it, do not reconstruct a pricing page from memory. Fabricated prices reach customers within days.
2. **Load the prior capture and name it in the header.** If none exists, declare this a baseline capture in the header.
3. **State the window** — the interval since the prior capture.
4. **Capture verbatim, field by field, per competitor:** tier names, list prices, billing period, unit, what is included, limits, add-ons, minimums, published discounts, free tier or trial terms, "contact us" boundary, and the page URL with capture date.
5. **Do not interpret while capturing.** Finish the table first.
6. **Diff every field** against the prior capture and write the changed ones in was/now format.
7. **Name a packaging signal only where its pattern appears.** Silence on a field is a valid outcome.
8. **Flag ambiguous reads** and name the discipline that would resolve them — usually FININT.
9. **Set update flags** for battle cards and deal desk guidance.
10. **Store under the naming convention** and name the file the next run should diff against.

If nothing changed, say so in one line with the window and stop.

## Human Decision Gate

Present the delta, then the full capture. Highlight:

- any change to floors, minimums, or the "contact us" boundary
- limits or inclusions that moved while the headline price held
- ambiguous reads and what would settle them
- whether a battle card is currently quoting a dead price

Use an Adaptive Decision Ladder: `Update the battle card and deal desk guidance`, `Run FININT to resolve the ambiguous read`, `Increase the capture frequency for this competitor`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every read **Fact** (what the page says), **Inference** (what it implies, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** prices, tier names, limits, inclusions, minimums, overage rates, discount percentages, or trial terms. A fabricated competitor price is quoted to a customer within a week and is trivially disproven.
- Capture the page's words, not a paraphrase.
- Distinguish list price from any negotiated or promotional price.
- If a field is absent from the page, record "not published" rather than inferring it.
- Note when a price is regional or currency-specific.

## Common Failure Modes

- Storing your read instead of the verbatim capture
- Capturing headline prices and skipping limits, inclusions, and minimums
- Reporting a change with no prior capture named
- Attaching a strategic signal to every field
- Choosing one explanation for an ambiguous change
- Improving the schema mid-series, destroying comparability
- Treating a promotional price as list
- Running this once instead of on a schedule, which is where the value lives

## Assets and Examples

- [Pricing and Packaging Capture template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Update the battle card and deal desk guidance (Recommended)
2. Run FININT to resolve the ambiguous read
3. Keep the schedule — the series is the asset, not any single capture
4. Increase capture frequency for the competitor that is moving

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [Monitors: the pricing tracker and the materiality bar](../../reference/monitors.md)
- [The disciplines: SIGINT](../../reference/disciplines.md)
- [Output schemas and the storage convention](../../reference/output-schemas.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
