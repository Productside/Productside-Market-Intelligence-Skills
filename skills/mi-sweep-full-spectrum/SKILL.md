---
name: mi-sweep-full-spectrum
description: Run all seven collection disciplines on one company in a single sitting, fuse them, and end in a call-ready brief. Use when a company suddenly matters and you have one hour.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company] [the conversation this is for]"
intent: >-
  The one-sitting sweep. Seven disciplines at collection-floor depth, fused with
  confidence stacking, ending in a brief a Product Manager can speak from memory.
  Exists because the most common intelligence need is not depth on one channel but
  defensible coverage before a meeting that is already on the calendar.
type: investigation
theme: market-competitive-intelligence
stage: collect
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
  - Competitive Intelligence Analyst
  - Sales Enablement
best-for:
  - "Getting comprehensively smart on one company before a call, review, or board question"
  - "Producing a brief that names what you must not say, as well as what you should"
  - "Establishing a baseline that every later run can diff against"
scenarios:
  - "We have a partner call this afternoon and I know almost nothing about them"
  - "A competitor turned up in three lost deals and my VP wants a read before the QBR"
  - "An acquirer approached us and nobody has profiled them"
  - "I have to answer board questions about this company on Thursday"
evidence-required:
  - "The company, and the conversation this is for"
  - "The relationship: competitor, prospect, partner, acquirer, vendor, unknown"
  - "How much time is available before it needs to be useful"
produces:
  - "Identity and perimeter block"
  - "Seven per-discipline sections with labeled signals"
  - "Fusion table with confidence and commitment"
  - "Call-ready brief, including a Do Not Say list"
estimated-time: "30 min rapid / 1-2 hr standard / half day deep"
group-size: "1-4"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
  - mi-build-battle-card
  - mi-watch-competitors
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, all eight disciplines"
  - "Regional Source Overlays: EU and MENA"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Full-Spectrum Company Sweep"
  short_description: "All seven disciplines, one sitting"
  brand_color: "#00E874"
  default_prompt: "Use $mi-sweep-full-spectrum on this company: identity first, then all seven disciplines in fixed order, fused with confidence stacking, ending in a call-ready brief with a Do Not Say list."
  allow_implicit_invocation: true
---

# Full-Spectrum Company Sweep

## Purpose

For when a company suddenly matters and there is one sitting to get smart.

All seven collection disciplines at collection-floor depth, run in a fixed order, fused with confidence stacking, ending in a brief a Product Manager can speak from memory. One run, no orchestration.

The deliverable is not the research. The deliverable is the **call-ready brief**: a sixty-second summary, the three things worth saying, the questions you will be asked with honest answers, and — the section that earns the run — the claims you must not make.

The sweep collects and labels per discipline. The fusion section rates. Keeping those separate is what lets a reader challenge one link instead of dismissing the whole brief, and it is why **collection is not fusion** even inside a run that does both.

## When to Use It

Use it when a company suddenly matters and you have one sitting. Use it for a first profile of a competitor, partner, prospect, or acquirer. Use it to establish the baseline that every later monitor diffs against.

Do not use it when:

- **Maximum rigor on one discipline is what you need.** Run that single sweep. This one trades depth for coverage on purpose.
- **The subject is a market or category, not a company.** Run `mi-scan-market-landscape` or `mi-size-tam-sam-som`; those answer different questions.
- **You already hold recent sweeps and only need them reconciled.** That is `mi-fuse-all-source`, with no new fieldwork.
- **You already ran this recently.** Run `mi-watch-competitors` and diff.
- **The company is pre-public, pre-product, and pre-press.** Most disciplines return nothing and the honest output is a short list of what cannot be known yet. Say that in the first two minutes, not the last.

## Input

Require:

- the company, and the conversation this is for
- the relationship — competitor, prospect, partner, acquirer, vendor, or unknown
- the time available

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given. Never ask for the legal entity, ticker, funding history, or headcount; finding all of it is the run.

If `[GEOGRAPHY]` is outside the US, load `reference/regional-overlays.md` before collecting.

**Example invocation:** `Use $mi-sweep-full-spectrum on Cartelane. Competitor, showed up in three lost deals, QBR is Thursday morning.`

## Key Concepts

**Identity before everything** — Legal entity, trading names, ownership status, tickers, filing jurisdictions, founding year, brands, subsidiaries, and the same-name companies to exclude *by name*. This block costs one minute and prevents the failure that costs the whole run. Catching the wrong company at the gate is a line; catching it in section eight is a rewrite, plus whatever was said out loud in between.

*Violation signal:* The perimeter section says "excluded unrelated companies" without naming one.

**The fixed order is the defensibility** — Identity, OSINT, FININT, TECHINT, HUMINT, GEOINT/DEMOINT, SIGINT, MASINT, fusion, brief, gaps. Do not reorder because one channel looks juicier. What you swept is defensible; what you stumbled across is not, and a sweep that follows the search engine's enthusiasm will report whatever ranked well.

*Violation signal:* Sections appear in the order the findings arrived, with the richest first.

**Per-discipline sections before fusion** — Every signal stays in the section of the channel that produced it. This is what makes provenance visible, and provenance is what lets a skeptical VP challenge one claim instead of dismissing the brief. A document that merges everything into "what we found" is unfalsifiable in the way that feels authoritative.

*Violation signal:* A finding appears in the brief with no discipline attached, so nobody can tell which channel produced it.

**Depth is a budget** — Rapid is the highest-value pass per discipline, enough to hold a conversation without embarrassing yourself. Standard is the collection floor and the default. Deep is a research afternoon. Depth is chosen from the calendar, not from how interesting the company is, and the most common failure here is promising deep to someone who has forty minutes.

*Violation signal:* The estimated time exceeds the time remaining before the meeting the sweep is for.

**Empty sections are findings** — A discipline that returns nothing gets one honest line naming what was swept and what the absence suggests. A private company with no filings is telling you how much you will ever know via FININT. A software company with no supply chain is not a MASINT failure. Padding an empty section to keep the document symmetrical is the most common way a sweep starts inventing.

*Violation signal:* Every one of the seven sections is roughly the same length.

**The Do Not Say list** — The section that keeps a Product Manager from being corrected in front of a customer or a board. Claims that are tempting, plausible, and unsupported, each with the reason it does not hold. It is not padding and it is not modesty; it is the highest-value paragraph in the document, because it is the one that prevents a specific, foreseeable embarrassment.

*Violation signal:* The brief contains a "what we do better" section and no "do not say" section.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a full-spectrum sweep — identity, then seven disciplines in fixed order, fused, ending in a call-ready brief. Standard depth is one to two hours. I will stop at the brief and a Final Step block. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Sweep Setup Q1/3` — Which company, and what conversation is this for?
2. `Sweep Setup Q2/3` — What is your relationship: competitor, prospect, partner, acquirer, vendor, or unknown? The same company researched for a partnership and for a deal defense is two different hours.
3. `Sweep Setup Q3/3` — How much time before this needs to be useful?

In **Context dump** mode, extract supplied material into the relevant discipline sections, account for it, and sweep only the gaps. In **Best guess** mode, assume standard depth, competitor framing, and a general strategic briefing; name each assumption. On silence: exactly those defaults. Proceed.

## What It Produces

Complete the [Full-Spectrum Company Sweep](template.md), written to the schema in `reference/output-schemas.md`:

- identity and perimeter
- seven per-discipline sections, each with its own labeled signal table
- fusion table: stories with disciplines supporting, confidence, commitment, and so-what — capped at seven
- contradictions worth naming
- the call-ready brief, including **Do Not Say**
- collection gaps and what the absences suggest
- assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption with its vintage, and invent nothing.
2. **Show a four-bullet search plan, identity first.** Identity and perimeter, sweep order, date window, noise filter. Four rather than three because catching the wrong company at the gate is the cheapest error prevention available. Continue unless revised.
3. **Establish identity and perimeter.** Name the same-name confusions explicitly.
4. **Announce each discipline as it starts**, then sweep in the fixed order: OSINT, FININT, TECHINT, HUMINT, GEOINT/DEMOINT, SIGINT, MASINT.
5. **Keep every signal in its own discipline's section**, with source URL, date, and F/I/A label.
6. **At collection-floor depth per discipline**, take the highest-value pass and move on. This run buys coverage, not depth; the single-discipline skills exist for depth.
7. **Fuse.** Run the independence test, collapse shared origins and record the collapse, stack confidence across disciplines, and place each story on the commitment ladder. Cap at seven stories in standard depth.
8. **Name the contradictions,** and which side the money supports.
9. **Write the call-ready brief.** Sixty-second summary, three things worth saying, questions you will be asked with honest answers including at least one you cannot answer, and Do Not Say.
10. **Report the gaps.** Which disciplines returned little, what the absence suggests, and what would close each.
11. **Store it** under the naming convention so the next run is a diff.

## Human Decision Gate

Present the brief first, then the evidence behind it. Highlight:

- how many apparent sources collapsed during fusion
- which stories rest on a single discipline
- the one question in the brief you cannot answer
- which disciplines were thinnest, and whether that reflects the company or the run

Use an Adaptive Decision Ladder: `Use the brief as-is`, `Go deep on the thinnest discipline first`, `Turn it into a battle card`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every key line **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** figures, quotes, headcounts, patent numbers, review counts, customer names, prices, funding amounts, or URLs. This brief will be spoken out loud, which makes fabrication here uniquely costly — a Product Manager will repeat it to the person best positioned to correct it.
- A company's own words are a claim, not a fact about the market.
- Nothing in "The Three Things Worth Saying" may rest on a single Assumption.
- Include at least one question you cannot answer, with the honest response. "I do not know, I will find out" beats a confident guess repeated by a customer.
- Stay inside the guardrails: published, filed, posted, or publicly observable only.

## Common Failure Modes

- Reordering the sweep because one channel looked more interesting
- Padding an empty discipline so the document looks symmetrical
- Letting a single vivid find set the confidence level for the run
- Merging findings so provenance disappears
- Skipping identity because the name seemed unambiguous
- Running deep when the calendar said rapid
- Producing seven stories because the cap is seven
- Omitting Do Not Say, which is the section that prevents the embarrassment
- Ending on research rather than on a brief someone can speak

## Assets and Examples

- [Full-Spectrum Company Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Use the brief for the conversation it was built for (Recommended)
2. Go deep on the thinnest discipline before the meeting
3. Schedule this as a monthly watch so the next run is a diff
4. Turn it into a battle card for the field

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [Sweep playbooks: the full-spectrum sweep and depth settings](../../reference/sweep-playbooks.md)
- [The disciplines](../../reference/disciplines.md)
- [Fusion: independence, stacking, commitment](../../reference/fusion.md)
- [Output schemas: full-spectrum sweep and call-ready brief](../../reference/output-schemas.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
