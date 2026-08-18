---
name: mi-fuse-all-source
description: Reconcile signals from multiple disciplines into confidence-rated stories with artifact-mapped responses. Use when evidence is already in hand and someone has to decide what is actionable.
license: CC-BY-NC-SA-4.0
argument-hint: "[collected signals or prior sweeps]"
intent: >-
  The situation room. One signal is an anecdote; three correlated signals from
  independent disciplines is intelligence. Exists to run the independence test
  before confidence stacking, because six sources that collapse to two disciplines
  is the single most common way a competitive deck lies by accident.
type: analysis
theme: market-competitive-intelligence
stage: fuse
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
  - Strategy and Corporate Development
best-for:
  - "Turning scattered signals into confidence-rated stories an executive can act on"
  - "Testing whether an announced move is funded, procured, staffed, or merely narrated"
  - "Finding the conflict that says someone is bluffing, instead of averaging it away"
scenarios:
  - "We have three sweeps and a spreadsheet and nobody can say what it means"
  - "Is their announced platform play real, or theater?"
  - "Two of our sources say opposite things and the deck says the average"
  - "Leadership wants a threat assessment and we have evidence but no verdict"
evidence-required:
  - "Signals from two or more disciplines, with sources and dates"
  - "The decision the fusion supports"
  - "Whether win/loss interviews are current"
produces:
  - "Signal inventory with same-source collapses noted"
  - "Confidence-rated fusion stories with commitment levels"
  - "Conflicts, kept as conflicts"
  - "Artifact-mapped responses and named collection gaps"
estimated-time: "45-90 min"
group-size: "1-8"
consumes:
  - mi-collect-osint
  - mi-collect-finint
  - mi-collect-techint
  - mi-collect-humint
  - mi-collect-sigint
  - mi-collect-masint
  - mi-collect-geoint-demoint
combine-with:
  - mi-build-battle-card
  - mi-analyze-swot
  - mi-watch-competitors
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, All-Source Fusion"
  - "Regional Source Overlays: MENA, on separating announced ambition from funded commitment"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "All-Source Fusion"
  short_description: "Stack the disciplines, rate the confidence"
  brand_color: "#00E874"
  default_prompt: "Use $mi-fuse-all-source to inventory the signals we already hold, run the independence test, stack confidence across disciplines, and end with artifact-mapped responses rather than findings."
  allow_implicit_invocation: true
---

# All-Source Fusion

## Purpose

The situation room. One signal is an anecdote. Three correlated signals from independent disciplines is intelligence.

This skill fuses; it does not collect. Its job is to take whatever evidence exists — sweep outputs, pasted findings, attached documents — run the independence test, stack confidence, check commitment, keep conflicts as conflicts, and end on *responses* rather than findings.

It exists because of one specific, common, expensive error: **six sources that collapse to two disciplines**. A press release and its coverage. An analyst note and the vendor blog quoting it. Three articles sourced to the same unnamed executive. Every one of those looks like corroboration in a table and is a single origin wearing several hats. Stacking confidence before collapsing them is how competitive decks lie by accident, with real citations attached.

Motion: **inventory → independence test → cluster into stories → stack confidence → commitment check → verdicts, responses, gaps.**

## When to Use It

Use it when evidence is already in hand and someone has to decide what is actionable. Use it to test whether an announced move is real. Use it on a quarterly cadence as the standing threat assessment. Use it when two sources disagree and someone is about to split the difference.

Do not use it when:

- **Only one discipline holds signals.** A single-discipline story cannot rate above a watch item, and running fusion on it produces ceremony. Say so and recommend the sweep that would make fusion worth doing.
- **You need new evidence.** This run does not collect. If two or fewer disciplines hold signals, say so and offer a *targeted* gap-fill with its own three-bullet search plan — do not quietly start sweeping.
- **The question is a framework question with its evidence attached.** Hand it to `mi-analyze-swot`, `mi-analyze-five-forces`, or `mi-analyze-ansoff`.
- **The real question is why deals close.** Public signals infer that. Win/loss interviews know it, and fusion's job here is to cap what the public signals may claim.

## Input

Require:

- signals from two or more disciplines, with sources and dates
- the `[DECISION]` this fusion supports
- whether win/loss interviews are current — the one input no search can supply

Anything supplied in the invocation, attachments, prior sweep outputs, or earlier conversation counts as context already given. If a prior fusion brief exists in session or on file, lead with the delta rather than rebuilding.

**Example invocation:** `Use $mi-fuse-all-source on the Cartelane sweeps — OSINT, TECHINT, HUMINT, SIGINT are all in this thread. Decision: accelerate or concede integration work.`

## Key Concepts

**The independence test comes first** — Before any stacking, collapse signals that trace to a shared origin. A press release and its trade coverage are one discipline. An investor deck and the earnings call reciting it are one. A job posting and the LinkedIn post announcing it are one. Kept separate: a patent filing and a hiring surge; a pricing change and an earnings margin comment; a permit record and a supplier volume shift; customer reviews and win/loss interviews. Two sources are independent when they would fail *differently*, not when they sit far apart.

*Violation signal:* A story's confidence is stated in number of sources rather than number of independent origins.

**Confidence stacking** — One discipline flags it: watch item, log it, do nothing. Two disciplines agree: working hypothesis, assign someone to probe. Three or more agree: actionable intelligence, brief leadership and move. Disciplines conflict: the most interesting case, because someone is bluffing. Rank by confidence, then by consequence — a high-confidence story about something that does not matter ranks below a working hypothesis about something that decides the year.

*Violation signal:* A verdict appears without the discipline count that produced it, post-collapse.

**Ambition versus commitment** — Treat announcements as intent until funding, procurement, land, permits, hiring, or contracts corroborate them. Ambition is OSINT. Commitment shows up in FININT, MASINT, and HUMINT. The five-level ladder — Announced, Funded, Procured, Staffed, Built — makes this gradeable, and a story sitting at Announced with nothing below it is a watch item dressed as a threat.

*Violation signal:* A story is rated actionable on evidence that is entirely announcement, however widely it was carried.

**Conflicts are findings, not noise** — Never average two conflicting signals into a comfortable middle. A conflict is usually the most useful thing in the document, because it means someone is bluffing and the bluff is discoverable. The most common conflict is a company's own messaging against its own resource allocation, and when those disagree, the resources are telling the truth.

*Violation signal:* Two contradictory sources are reconciled into a single moderate statement that neither source supports.

**Win/loss weighting** — If win/loss interviews are unverified this cycle, cap org-instability and build-signal stories at working hypothesis and say so in the verdict. Public signals infer why deals move; only the interviews know. A build-signal story rated actionable without ground truth is how a roadmap gets reordered by a job posting.

*Violation signal:* A story about why deals are being lost is rated actionable with no interview behind it.

**A story that changes no artifact is trivia** — Every actionable story names the artifact that changes, the move to make, and who makes it — *before* the competitor's launch, not after. Watch items name their escalation trigger. Working hypotheses name a probe with an owner and a deadline. A finding with none of these is competitive trivia and should be cut or demoted.

*Violation signal:* The brief ends on findings, with no artifact named and no owner assigned.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is all-source fusion. I will inventory what we already hold, collapse same-origin signals, stack confidence, check commitment, and end with responses — I will not collect new evidence unless we agree a targeted gap-fill. Forty-five to ninety minutes. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Fusion Setup Q1/3` — What decision does this brief support?
2. `Fusion Setup Q2/3` — Have win/loss or churned-customer interviews been run this cycle? Nothing public tells me, and it caps what several story types may claim.
3. `Fusion Setup Q3/3` — Is there a prior fusion brief I should diff against rather than rebuild?

**Context dump is the expected mode here**, since fusion normally begins with a paste. Extract every signal into the inventory schema, account for it as found / inferred / still missing, tag anything without a checkable source as an Assumption regardless of how confidently it was supplied, and show the discipline coverage before asking anything. In **Best guess** mode, assume win/loss unverified, no prior brief, and a general threat-assessment audience; name each assumption. On silence: those defaults, Just Enough Mode. Proceed.

## What It Produces

Complete the [All-Source Fusion Brief](template.md), written to the schema in `reference/fusion.md`:

- signal inventory with **same-source collapses noted and counted**
- fusion stories, capped at five, ranked by confidence then consequence
- per story: disciplines in agreement post-collapse, the story in two or three sentences, verdict, commitment level, and response
- conflicts, kept as conflicts, each with the evidence that would settle it
- watch items — single-discipline flags, logged only
- collection gaps, naming which sweep fills each
- assumptions to validate, Final Step block

If a prior brief exists, lead with the delta.

## Workflow

1. **State web access in one line,** and state plainly that this run does not collect.
2. **Inventory every signal.** Discipline, source URL, date, F/I/A label. Everything available: sweep outputs, pasted findings, attached documents.
3. **Run the independence test before anything else.** Follow each signal to its origin. Collapse shared origins to one row and **record the collapse** — "seven sources, one origin" belongs in the document, because it is a finding.
4. **Show discipline coverage.** How many disciplines hold signals, post-collapse. If two or fewer, say so now and offer a targeted gap-fill with a three-bullet plan rather than proceeding as though the evidence were richer than it is.
5. **Cluster into stories.** Name each as a capability or a move, not a vibe. "Building a first-party analytics layer to defend renewals" is a story. "Getting more aggressive" is unfalsifiable. Cap at five, seven in a full-spectrum sweep. The eighth is noise.
6. **Stack confidence** using the discipline count after collapsing. Rank by confidence, then by consequence.
7. **Apply win/loss weighting.** If interviews are unverified, cap org-instability and build-signal stories at working hypothesis and say why in the verdict.
8. **Run the commitment check.** Place each story on the ladder and name the evidence that put it there.
9. **Work the conflicts.** For each: what A implies, what B implies, which one the money supports, and the specific evidence that would settle it plus where to look. Never average.
10. **Map responses to artifacts.** Watch item → log it and name the escalation trigger. Working hypothesis → assign a named probe with a deadline and the discipline that resolves it. Actionable → name the artifact, the change, and who makes it. Any story with none of these is trivia; cut or demote it.
11. **Name the collection gaps** and which sweep fills each. Then stop.

## Human Decision Gate

Present the stories, ranked. Highlight:

- how many apparent sources collapsed, and which stories moved as a result
- any story rated on a single discipline, and why it is a watch item
- which stories are capped by unverified win/loss
- the conflict most worth resolving, and what would resolve it

Use an Adaptive Decision Ladder: `Act on the actionable stories`, `Fund the named probes on the working hypotheses`, `Fill the largest collection gap first`, or `Other (specify)`. Say what each buys and what it defers.

## Evidence and Attribution Rules

- Label every line **Fact**, **Inference** (chain shown), or **Assumption** (basis stated).
- **Do not invent:** signals, sources, dates, discipline counts, or corroboration. A fusion brief built on invented signals is disinformation with a confidence score attached — the most damaging artifact this library could produce.
- Never upgrade a confidence level to make a story more persuasive. The count after collapsing is the count.
- A signal whose source cannot be checked is an Assumption, no matter how confidently it was pasted.
- Where the sweep and the win/loss interviews disagree, the interviews win.
- Report the absence of a discipline as a gap, never as an implied zero.

## Common Failure Modes

- Stacking confidence without running the independence test first
- Rating an OSINT-only story as actionable because the announcement was everywhere
- Averaging conflicting signals into a middle verdict
- Naming a story as a vibe so it can never be falsified
- Quietly collecting new evidence in a run that was scoped to reconcile
- Producing eight stories because eight were available
- Ending on findings rather than on responses
- Omitting the win/loss cap, so a job posting reorders a roadmap
- Ranking purely by confidence and burying the working hypothesis that decides the year

## Assets and Examples

- [All-Source Fusion Brief template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Act on the actionable stories and assign the probes (Recommended)
2. Turn the top story into a battle card or roadmap decision
3. Schedule the fusion cadence so the next brief is a delta
4. Fill the largest collection gap with the named sweep

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [Fusion: independence test, stacking, commitment ladder, conflicts](../../reference/fusion.md)
- [The disciplines and their strongest pairs](../../reference/disciplines.md)
- [Output schemas: the fusion brief](../../reference/output-schemas.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
