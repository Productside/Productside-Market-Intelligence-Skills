---
name: mi-snapshot-competitors
description: Profile a named competitor set with cited snapshots, a buyer-dimension comparison matrix, and a so-what. Use when you know who matters and need just-enough depth on each.
license: CC-BY-NC-ND-4.0
argument-hint: "[up to three competitors] [buyer]"
intent: >-
  Produce just-enough profiles on the competitors who actually show up in deals,
  compared on the dimensions the buyer uses rather than the ones you win on.
  Exists because most competitive matrices are marketing with a grid around them,
  and because an inflated competitor set breaks every later diff.
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
  - Competitive Intelligence Analyst
  - Sales Enablement
best-for:
  - "Profiling the two or three competitors who actually appear in lost deals"
  - "Building a comparison matrix on buyer dimensions rather than favorable ones"
  - "Establishing the snapshot baseline that a competitive watch will diff against"
scenarios:
  - "Sales keeps naming the same three competitors and we have no current profile"
  - "Our comparison matrix has ten rows and we win on all of them"
  - "We need a baseline before setting up a competitive watch"
  - "Leadership asked who we are really up against"
evidence-required:
  - "The competitor set, or the lost-deal history that would identify it"
  - "The buyer, whose dimensions the matrix must use"
  - "The decision this feeds"
produces:
  - "Per-competitor snapshots with sources and dates"
  - "Comparison matrix on buyer dimensions, with an evidence-quality row"
  - "So-what with counted implications, risks, and opportunities"
  - "A diffable baseline for the next watch"
estimated-time: "45-90 min"
group-size: "1-4"
consumes:
  - mi-scan-market-landscape
  - mi-router-market-intelligence
combine-with:
  - mi-build-battle-card
  - mi-watch-competitors
  - mi-fuse-all-source
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, OSINT and the act layer"
  - "Competitive research snapshot discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Competitive Research Snapshot"
  short_description: "Just-enough profiles on who matters"
  brand_color: "#00E874"
  default_prompt: "Use $mi-snapshot-competitors to profile up to three competitors with cited snapshots, compare them on the dimensions our buyer uses, include an evidence-quality row, and end with a counted so-what."
  allow_implicit_invocation: true
---

# Competitive Research Snapshot

## Purpose

Just-enough profiles on the competitors who actually matter, plus a comparison matrix and a so-what.

The discipline here is restraint. Three competitors profiled well beats eight profiled thinly, because the matrix schema assumes three columns and an inflated set breaks every diff that follows. And the matrix compares on **dimensions the buyer uses**, not dimensions you win on — a matrix where every row favors you is marketing with a grid around it.

This is a collection run. It gathers and labels; it does not rate threats or fuse disciplines. **Collection is not fusion.**

## When to Use It

Use it when you already know who matters and need current, cited depth on each. Use it to establish the baseline a competitive watch will diff against. Use it after a landscape scan has told you which players are worth profiling.

Do not use it when:

- **You do not yet know who is in the market.** Run `mi-scan-market-landscape` first, or you will profile the three vendors with the best SEO.
- **You need one company in depth across all seven disciplines.** That is `mi-sweep-full-spectrum`.
- **You need field-ready talk tracks.** That is `mi-build-battle-card`, which consumes this.
- **You ran this recently.** Run `mi-watch-competitors` and diff.

## Input

Require:

- the competitor set — or the lost-deal history that would identify it
- the `[BUYER]`, whose dimensions the matrix must use
- the `[DECISION]` this feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-snapshot-competitors on Cartelane, Meridian, and Northwind. Buyer is VP RevOps with Finance evaluating.`

## Key Concepts

**Three, chosen by deal appearance** — Use the competitors the user provides. If none are provided, identify the top three; use four only if clearly needed. If more than four are named, ask which three appear most often in lost deals and profile those. **Pick by who shows up in deals, not by who is largest** — the biggest company in a category is frequently not the one taking your revenue, and profiling them instead is how a competitive program spends a year watching the wrong door.

*Violation signal:* The competitor set was chosen by market share or brand recognition rather than by appearance in real deals.

**Buyer dimensions, not favorable ones** — The matrix rows come from what the buyer evaluates: the criteria in their RFP, the questions in their discovery calls, the language in their reviews. Rows chosen from where you are strong produce a document that is true, useless, and actively misleading to a rep who believes it. **If every row favors you, the matrix is marketing, not intelligence.**

*Violation signal:* Every row in the matrix has your column winning.

**The evidence-quality row** — For each competitor, how good is the sourcing behind their column: documented, inferred, or guessed. A matrix that hides which column is guesswork is worse than no matrix, because it launders an assumption into a comparison. This row is the difference between a grid a rep can trust and a grid that makes them confident about the wrong thing.

*Violation signal:* Two competitors are compared cell-for-cell when one was researched from filings and the other from a homepage.

**Just enough, per competitor** — What they sell, to whom, positioning in their own words, pricing posture, notable strengths, notable exposure, and the last material thing they did with a date. Seven items. More than that is a sweep, and a sweep is a different skill with a different budget.

*Violation signal:* A profile runs to two pages and still does not say what the competitor's pricing posture is.

**The so-what is counted** — Three implications, two risks, two opportunities, three assumptions to validate. The counts are the discipline: they force ranking, and ranking is the work. An uncounted "key takeaways" section grows until it contains everything found, which means it prioritizes nothing.

*Violation signal:* The closing section is a bulleted list of observations with no counts and no ranking.

**A snapshot is a baseline** — This artifact exists to be diffed. Keep the schema stable, date every claim, and store it under the naming convention. A snapshot rewritten in a new shape each quarter cannot be compared to itself, which quietly destroys the entire value of running it repeatedly.

*Violation signal:* The second run has different matrix rows than the first, so nothing can be compared.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a competitive snapshot — up to three competitors, cited profiles, a matrix on your buyer's dimensions, and a counted so-what. Forty-five to ninety minutes. It becomes the baseline a watch can diff against. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Snapshot Setup Q1/3` — Which competitors? If you name more than four, which three appear most often in lost deals?
2. `Snapshot Setup Q2/3` — Who is the buyer, and what do they actually evaluate on? Those are the matrix rows.
3. `Snapshot Setup Q3/3` — What decision does this feed: a battle card, a roadmap input, or a positioning refresh?

In **Context dump** mode, extract supplied profiles and deal notes, identify what is already covered, and research only the gaps. In **Best guess** mode, select the top three by appearance in buyer-side discussion, derive matrix rows from review language, and name each assumption. On silence: top three by buyer mentions, review-derived dimensions, battle-card framing. Proceed.

## What It Produces

Complete the [Competitive Research Snapshot](template.md):

- competitor selection rule, stated
- per-competitor profiles: seven items each, sourced and dated
- comparison matrix on buyer dimensions, including the **evidence-quality row**
- so-what: 3 implications, 2 risks, 2 opportunities, 3 assumptions
- collection gaps, Final Step block
- stored under the naming convention as a diffable baseline

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption with its vintage, and invent no prices, features, or customer names.
2. **Apply the selection rule and state it.** Three competitors, chosen by deal appearance. If the user named more, ask which three show up in lost deals.
3. **Show the search plan.** Sweep order, date window, noise filter including same-name exclusions by name. Continue unless revised.
4. **Profile each competitor on the same seven items,** in the same order, with a source and date on each.
5. **Derive matrix rows from the buyer,** not from your product. Use RFP criteria, discovery questions, and review language.
6. **Fill the matrix, then fill the evidence-quality row.** Documented, inferred, or guessed, per competitor.
7. **Check the matrix for self-flattery.** If every row favors you, the rows are wrong. Rebuild them from buyer language and try again.
8. **Write the counted so-what:** 3 implications, 2 risks, 2 opportunities, 3 assumptions to validate.
9. **Report gaps** in one line each, naming what was swept.
10. **Store it** under the naming convention so the next run is a diff.

## Human Decision Gate

Present the matrix first, then the profiles. Highlight:

- how the three were selected, and who was excluded
- which columns rest on weak sourcing
- any row where you do not win, stated plainly
- what the next run should diff against

Use an Adaptive Decision Ladder: `Turn this into a battle card`, `Set up the watch that diffs against it`, `Re-derive the matrix rows from buyer language`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every key line **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** prices, tier names, feature availability, customer names, headcounts, funding, or review counts. Competitor feature claims are the most commonly fabricated content in competitive work and the most easily disproven in a live deal.
- A competitor's own positioning language is a Fact about their marketing, not about their product.
- Feature availability requires a documentation, pricing-page, or changelog citation. "Their site implies it" is an Inference.
- Date every claim. A snapshot with undated claims cannot be diffed.
- Stay inside the guardrails: published, filed, posted, or publicly observable only.

## Common Failure Modes

- Profiling the largest players instead of the ones in lost deals
- Profiling eight competitors, which breaks the matrix and the diff
- Choosing matrix rows where you win
- Omitting the evidence-quality row, so guesswork and filings look identical
- Comparing a competitor researched from filings against one researched from a homepage
- Writing an uncounted takeaways section
- Changing the schema between runs
- Rating threats, which is fusion's job

## Assets and Examples

- [Competitive Research Snapshot template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Turn this into a battle card for the field (Recommended)
2. Set up the competitive watch that diffs against this baseline
3. Schedule a quarterly refresh so the snapshot stays current
4. Take the matrix into positioning

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The act layer: competitive snapshot discipline rules](../../reference/frameworks.md)
- [The disciplines: OSINT](../../reference/disciplines.md)
- [Output schemas and the storage convention](../../reference/output-schemas.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
