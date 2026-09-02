---
name: mi-build-battle-card
description: Build a one-page, seller-ready battle card — ranked weaknesses, ranked advantages, a call-and-response grid, do not say — every claim traced to a source. Arm sales without arming them wrongly.
license: CC-BY-NC-SA-4.0
argument-hint: "[competitor] [fused evidence]"
intent: >-
  Turn fused evidence into a card a salesperson will actually use: outcome
  language, trap questions you can evidence, honest acknowledgment of their real
  strengths, and a Do Not Say list. Exists because an assertion without a source
  and a date is an opinion wearing a badge.
type: analysis
theme: market-competitive-intelligence
stage: act
discipline: All-Source Fusion
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Marketing Manager
  - Product Manager
  - Sales Enablement
  - Competitive Intelligence Analyst
  - Business Analyst
best-for:
  - "Arming the field with claims that survive a customer who knows the competitor"
  - "Writing trap questions you can actually back up"
  - "Naming the claims a rep must not make, and why"
scenarios:
  - "Our battle cards have gone stale and nobody trusts them"
  - "A rep got corrected by a customer using our own card"
  - "We keep losing to one competitor and the field has nothing"
  - "The card is a feature matrix and reps do not open it"
evidence-required:
  - "Fused evidence or sweep outputs with sources and dates"
  - "The competitor, and which deals this card is for"
  - "Current pricing and packaging capture"
produces:
  - "One-page field summary a rep can use without opening the appendix"
  - "Thirty-second read as a framing wedge: who they are, when you win, when you lose"
  - "Top 5 ranked competitor weaknesses and top 5 ranked advantages, each with a stated basis"
  - "A call-and-response grid: if they say this, you say that"
  - "Ask this, watch out for, do not say"
  - "Pricing snapshot with a capture date"
  - "Evidence appendix where every claim traces to a source"
estimated-time: "45-90 min"
group-size: "1-4"
consumes:
  - mi-fuse-all-source
  - mi-mine-voice-of-customer
  - mi-snapshot-competitors
combine-with:
  - mi-watch-competitors
  - mi-monitor-pricing-packaging
  - mi-collect-sigint
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, the act layer"
  - "Battle card discipline rules, Productside market-intelligence prompts"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Battle Card From Evidence"
  short_description: "A card reps use and can defend"
  brand_color: "#00E874"
  default_prompt: "Use $mi-build-battle-card to build a one-page, seller-ready card from our fused evidence: a wedge-framed read, ranked weaknesses and advantages, a call-and-response grid, and do not say, with every claim traced to a dated source in the appendix."
  allow_implicit_invocation: true
---

# Battle Card From Evidence

## Purpose

Arm the field with claims that survive a customer who knows the competitor better than the rep does.

A battle card is not a feature matrix and not a research summary. It is a small set of things to say, ask, expect, and avoid — each traceable to a dated source. **A card salespeople will not use is a document, not a card**, and the fastest way to make one unusable is to fill it with claims that get a rep corrected in front of a buyer. Just as fatal, and easier to miss: a card that reads like an intelligence brief instead of a sales tool never gets opened at all, however well-sourced it is.

This skill consumes fused evidence. Where a claim has no cited source, the honest entry is **"no evidence found"** and the claim does not go on the card. The evidence appendix is not optional decoration; it is what lets a rep answer "where did you hear that?" — but the appendix is the backing, not the front door. The front door is the one-page field summary, and if a rep never gets past it, that is the card doing its job.

## When to Use It

Use it when the field needs current, defensible ammunition against a named competitor. Use it after fusion, and after a pricing capture, so the freshest layer is actually fresh.

Do not use it when:

- **You have not fused yet.** A card built from one discipline's signals will be confidently wrong in the direction that discipline is blind.
- **You need the full competitive picture.** That is `mi-snapshot-competitors`. A card is deliberately narrow.
- **You need to know why deals are lost.** Win/loss knows; a card built to answer it from public signals will mislead the field about the thing that matters most.
- **The competitor is unknown to you.** Say so. A card that pretends to knowledge is worse than no card, because a rep will trust it.

## Input

Require:

- fused evidence or sweep outputs, with sources and dates
- the competitor, and which deals this card is for
- a current pricing and packaging capture

Anything supplied in the invocation, attachments, a fusion brief, or earlier conversation counts as context already given.

**Example invocation:** `Use $mi-build-battle-card on Cartelane, using the fusion brief and the SIGINT pricing capture in this thread. For mid-market deals where Finance runs the evaluation.`

## Key Concepts

**Every claim traces to a row in the evidence table** — An assertion without a source and a date is an opinion wearing a badge. The appendix is what makes the card auditable, what lets a rep answer a challenge, and what lets the next refresh know which lines are stale. A card whose claims cannot be traced cannot be maintained either, because nobody knows what to re-check.

*Violation signal:* A claim on the card has no corresponding row in the evidence appendix.

**Outcome language, not feature lists** — "Top 5 Advantages" carries at most five points, phrased as customer outcomes rather than capabilities. "We have field-level audit lineage" is a feature. "Your auditors accept the number without a screenshot trail" is an outcome. Reps do not lose deals on feature counts; they lose them on failing to connect to what the buyer is trying to achieve.

*Violation signal:* The "top 5 advantages" section reads as a capability list with checkmarks implied.

**The read is a wedge, not a biography** — Describing the competitor accurately is not the job. The thirty-second read exists to name the tension their real strength creates for this specific buyer — cost, risk, or friction they will feel, not credit for how impressive the competitor is. A read that could be lifted and pasted onto the competitor's own about page has taught the rep nothing they can use.

*Violation signal:* The thirty-second read could be mistaken for a paragraph from the competitor's own marketing.

**Rankings need a stated basis, not vibes** — A "Top 5" list orders by something: deal frequency, dollar impact, how often it surfaces in review complaints. Name the basis once, at the top of the section. A ranking with no stated basis is not evidence-backed just because each row has a citation — the *order* is a claim too, and it needs its own justification.

*Violation signal:* A Top 5 list with no stated ranking basis, or one whose order shifts between runs with no new evidence to explain the reshuffle.

**Speak like a seller, not a sensor** — The card is read by someone about to say these words to a customer. Discipline vocabulary — OSINT, SIGINT, FININT, HUMINT, and the rest — belongs in this skill's own teaching prose, where it does real pedagogical work. It has no place in the card itself: a rep does not say "per our SIGINT sweep" to a buyer, and a card that talks like a briefing document instead of a person gets skimmed once and never opened again.

*Violation signal:* A discipline acronym appears anywhere in the one-page summary, the thirty-second read, the Top 5 lists, or the If They Say/You Say grid.

**Never ask what you cannot evidence** — Trap questions are at most three, aimed at what the competitor's architecture or pricing genuinely cannot answer well. **A trap question you cannot back up traps your own rep**, because the buyer will relay it to the competitor and return with an answer the rep cannot handle. Every trap question needs its evidence row and its expected counter.

*Violation signal:* A trap question exists with no evidence row and no anticipated response.

**Watch out for names their real strengths, honestly** — The competitor's strongest true claims, stated plainly, each with your response. Understating them is the most common way a card fails in the field: a rep who has been told the competitor is weak everywhere is unprepared for the place they are strong, and their surprise is visible to the buyer.

*Violation signal:* The "watch out for" section contains only their weaknesses reframed, and nothing they genuinely do better.

**Do Not Say is the section that saves the deal** — Claims that are tempting, plausible, and unsupported, each with the reason it does not hold. This is not modesty or legal padding. It is the paragraph that prevents a specific, foreseeable correction in front of a customer, and it is the first section a good rep reads.

*Violation signal:* The card has a competitive-advantage section and no Do Not Say section.

**Date-stamp the card and name its decay** — The SIGINT layer — pricing, packaging, messaging — goes stale in weeks. The positioning layer goes stale in quarters. A card without a date and a decay note will be used a year later with the same confidence it earned on the day it was written, which is how a rep quotes a price that changed two quarters ago.

*Violation signal:* The card carries no capture date, or carries one date for content with different half-lives.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a battle card built from evidence you already hold, led by a one-page field summary a rep can actually use — wedge-framed read, ranked weaknesses and advantages, a call-and-response grid, ask this, watch out for, do not say, pricing snapshot, and an evidence appendix behind it all where every claim traces to a dated source. Forty-five to ninety minutes. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Card Setup Q1/3` — Which competitor, and which deals is this card for? A card for enterprise evaluations and one for self-serve are different cards.
2. `Card Setup Q2/3` — What are reps currently saying about them? I will check each claim and put the unsupported ones in Do Not Say, which is usually the most useful part of this run.
3. `Card Setup Q3/3` — Are win/loss interviews current? If not, I will not put win-reason claims on the card.

**Context dump is the expected mode.** Extract evidence, build the card, and flag which existing rep claims failed the check. In **Best guess** mode, build from available evidence and mark unsupported sections "no evidence found." On silence: mid-market framing, win/loss assumed unverified. Proceed.

## What It Produces

Complete the [Battle Card](template.md):

- **one-page field summary** — the page a rep actually opens, built entirely from material earned in the sections below it, never from anything new
- thirty-second read, as a wedge: who they are, when you win, when you lose
- **top 5 competitor weaknesses**, ranked with a stated basis, each with evidence
- **top 5 advantages** — max 5, outcome language, evidence-anchored where it touches the competitor
- **ask this** — max 3 trap questions, each with evidence and an expected counter
- **watch out for** — their strongest true claims, with responses
- **if they say / you say** — a call-and-response grid for the room, each row evidenced
- pricing and packaging snapshot **with a capture date**
- **do not say** — with the reason each claim fails
- **evidence appendix** — every claim, source URL, date, and label
- decay note by layer

## Workflow

1. **State web access in one line,** and state that this run consumes evidence rather than collecting it.
2. **Establish scope.** Which deals, which buyer, which segment. A card that tries to serve every deal serves none.
3. **Check what reps are already saying.** Each claim either earns an evidence row or moves to Do Not Say. This step alone usually justifies the run.
4. **Write the thirty-second read as a wedge:** who they are, when you win, when you lose — framed as the tension their strength creates for this buyer, not a neutral description. When you lose is not optional — a card that never says it is fiction, and reps know it.
5. **Build "top 5 competitor weaknesses,"** ranked against a stated basis named at the top of the section, each with its evidence ref.
6. **Write "top 5 advantages,"** at most five points, in outcome language, each traceable where it touches the competitor and dated where it touches our own product.
7. **Write "ask this,"** at most three, each with the evidence behind it and the counter you expect. Discard any question you cannot evidence.
8. **Write "watch out for"** — their genuinely strongest claims, stated honestly, with your response.
9. **Build "if they say / you say,"** pulling the room-ready version of claims already surfaced above. An entry with no evidence ref does not make the grid.
10. **Capture pricing and packaging verbatim with a date.**
11. **Write "do not say,"** each entry with its reason.
12. **Build the evidence appendix,** and confirm every card claim has a row. Then date-stamp the card and name the decay by layer.
13. **Assemble the one-page field summary last,** entirely from material already written above. Nothing appears in the summary that isn't already earned and evidenced somewhere below it.

## Human Decision Gate

Present the card, then the appendix. Highlight:

- which rep claims failed the evidence check and moved to Do Not Say
- which lines decay first, and when the card needs re-running
- whether win/loss is current, and what that prevented you from claiming
- any trap question that was cut for lack of evidence
- which Top 5 items are well-corroborated versus resting on thin or single-source evidence

Use an Adaptive Decision Ladder: `Ship the card to the field`, `Fill the evidence gap before shipping`, `Set up the weekly SIGINT watch that keeps it fresh`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every claim **Fact**, **Inference** (chain shown), or **Assumption** (basis stated). **Assumptions do not go on the card** — they go in the appendix or nowhere.
- **Do not invent:** prices, tier names, feature availability, customer names, outage histories, review counts, quotes, a stated ranking basis for the Top 5 lists, or certainty in a call-and-response answer the evidence does not actually support. A fabricated line on a battle card is spoken to a customer by someone who trusts you, which is the worst delivery mechanism for an error in this library.
- Every claim traces to an appendix row with a URL and a date.
- Never claim a competitor lacks a capability without a documentation or pricing-page citation; absence from a marketing page is not absence from a product.
- Do not build claims about why deals are won or lost without current win/loss interviews.
- Stay inside the guardrails: published, filed, posted, or publicly observable only.

## Common Failure Modes

- Building the card from feature parity rather than from which customer problem each side solves
- Writing trap questions you cannot evidence
- Understating their real strengths, so the rep is surprised in the room
- Omitting Do Not Say
- Shipping without a capture date, so a stale price gets quoted
- Putting an Assumption on the card because it was persuasive
- Claiming win reasons with no win/loss behind them
- Writing one card for every deal type
- Letting the appendix drift out of sync with the card
- Padding the one-page summary with a claim the full card does not back
- Ranking weaknesses or advantages by vibes instead of a stated basis
- Letting discipline jargon (OSINT, SIGINT, FININT, and the rest) leak into the seller-facing sections instead of staying in this skill's own teaching prose

## Assets and Examples

- [Battle Card template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Ship the card to the field (Recommended)
2. Fill the named evidence gap before shipping
3. Set up the weekly pricing and packaging watch that keeps this layer fresh
4. Run win/loss so the win-reason claims can be made at all

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The act layer: battle card discipline rules](../../reference/frameworks.md)
- [Fusion: what feeds this card](../../reference/fusion.md)
- [Monitors: keeping the freshest layer fresh](../../reference/monitors.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
