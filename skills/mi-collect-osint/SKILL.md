---
name: mi-collect-osint
description: Sweep a company's public record — press, analysts, exec social, reviews, events, prediction markets — into a fusion-ready signal inventory. Use to learn what they say and what is said about them.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company] [market and buyer]"
intent: >-
  Run the journalist's-desk discipline on one company: everything published,
  posted, rated, or presented in public, landed in a labeled inventory with a URL
  and a date. Exists because the say-versus-said-about gap is the cheapest
  positioning intelligence available and almost nobody collects it deliberately.
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
  - Content and Demand Marketing
best-for:
  - "Finding the gap between a competitor's positioning language and their customers' language"
  - "Catching a positioning pivot three to six months before the launch it precedes"
  - "Building the objection-handling layer of a battle card from cited review evidence"
scenarios:
  - "Their exec keeps posting about a problem space they have never sold into"
  - "They jumped two sponsor tiers at the conference our buyers attend"
  - "Analysts started describing them with a category name that did not exist last year"
  - "We need to know what customers actually complain about before we write the card"
evidence-required:
  - "The target company, and the market it is being read inside"
  - "The buyer, which determines which review sites and events matter"
  - "The decision this collection feeds"
produces:
  - "Fusion-ready signal inventory with URLs, dates, and evidence labels"
  - "Ranked inference chains, capped at five"
  - "The say-versus-said-about gap"
  - "Collection gaps and named handoffs"
estimated-time: "30-60 min"
group-size: "1-4"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
  - mi-mine-voice-of-customer
  - mi-build-battle-card
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, OSINT discipline"
  - "SCIP Code of Ethics, the industry reference for ethical collection"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "OSINT Collection Sweep"
  short_description: "Sweep the public record on one company"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-osint to sweep press, analysts, exec social, reviews, events, and prediction markets on this company, land every signal with a URL and a label, and stop before rating confidence."
  allow_implicit_invocation: true
---

# OSINT Collection Sweep

## Purpose

Run the journalist's desk: what a good beat reporter knows before the press release drops.

OSINT is everything published, posted, rated, filed as a talk, or priced by a crowd. It is the discipline everyone thinks they already run, and the one almost nobody runs *deliberately* — because reading the news is not the same as sweeping a defined source set in a fixed order and writing down what was not there.

The sweep produces a labeled inventory, not a verdict. **Collection is not fusion.** A sweep gathers and labels; rating confidence across disciplines belongs to `mi-fuse-all-source`. This matters more in OSINT than anywhere else, because OSINT is the discipline most likely to hand you a vivid, quotable, entirely uncorroborated story.

## When to Use It

Use it when you need to know what a company is saying, what is being said about it, and where those two diverge. Use it when a positioning question is live, when a battle card needs its objection-handling layer, or when something in the public record changed and nobody can say what.

Do not use it when:

- **You need review-level depth on customer pain.** This sweep flags the clusters; `mi-mine-voice-of-customer` mines them with quoted evidence.
- **You need the full competitor set mapped.** Run `mi-scan-market-landscape` first — sweeping one company in a market you cannot name produces a profile with no denominator.
- **You ran this recently.** Run `mi-watch-competitors` and diff instead of re-collecting.
- **The question is whether a move is funded.** OSINT is where ambition lives. Commitment shows up in FININT, MASINT, and HUMINT.

## Input

Require:

- `[TARGET]`, and the `[MARKET]` it is being read inside
- `[BUYER]`, which determines which review sites, job titles, conferences, and analysts are worth sweeping at all
- the `[DECISION]` this collection feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given. Do not ask for it again, and never ask for facts a search would return in ninety seconds.

If `[TARGET]` and `[MARKET]` are unclear, route back to `mi-router-market-intelligence` rather than sweeping a name.

**Example invocation:** `Use $mi-collect-osint on Cartelane. Mid-market revenue ops, buyer is VP RevOps with Finance running the evaluation.`

## Key Concepts

**The say-versus-said-about gap** — Their positioning language minus their customers' language. Where the two match, that is defended ground and attacking it wastes a quarter. Where they diverge, that is the exposed flank. Where customer language exists with no vendor claiming it, that is whitespace worth naming. This gap is the signature output of the discipline and the reason it is worth running as a sweep rather than as reading.

*Violation signal:* The sweep reports what the company says and what customers say in separate sections, and never subtracts one from the other.

**Ambition versus commitment** — OSINT collects intent. A press release, a keynote, a roadmap slide, and an exec's LinkedIn post are all the same evidence: the company would like this to be true. Treat announcements as intent until funding, procurement, land, permits, hiring, or contracts corroborate them elsewhere. An OSINT-only story cannot rate above working hypothesis no matter how many outlets carried it.

*Violation signal:* An inference chain concludes that a capability exists, sourced entirely to the company describing it.

**Source independence** — A press release and the six trade articles reporting it are one source, not seven. Three articles all sourced to the same unnamed executive are one source. An analyst note and the vendor blog quoting it are one source. Aggregators recycle press releases into what looks like corroboration, and OSINT is where this deception is easiest to fall for because the recycling is invisible unless you follow each link to its origin.

*Violation signal:* The inventory contains several rows whose "source" URLs all trace back to the same newsroom post on the same day.

**Leading indicators with known lead times** — OSINT signals carry clocks. Execs test messaging on social three to six months before launch. Webinar topics show what a company is about to sell. A sponsor-tier jump signals market entry or doubling down. Sudden silence on a product line is a sunset in progress. A signal without its typical lead time gives a direction and no deadline, which a roadmap cannot act on.

*Violation signal:* A positioning-pivot inference is reported without saying when the pivot would surface.

**Prediction markets as consensus, not truth** — Where a regulation, approval, or milestone gates `[MARKET]`, crowd-priced odds are a real signal about expectations. They are not ground truth, and a thin market is a number three people invented. Check liquidity before citing, and label the read as consensus rather than as forecast.

*Violation signal:* A market odd is quoted as a probability with no volume, no date, and no hedge.

**Review clusters as pressure points, not requirements** — Complaints clustering on one feature identify where the competitor's roadmap is under pressure, which is battle-card ammunition. They do not identify what your product should build. Public voice skews toward the angry and the vocal; a cluster is a hypothesis about *their* weak flank, not a mandate for *your* backlog.

*Violation signal:* A review cluster arrives in the output as a feature recommendation.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is an OSINT sweep — press, analysts, exec social, reviews, events, prediction markets — ending in a fusion-ready signal inventory and the say-versus-said-about gap. Thirty to sixty minutes. I will stop before rating confidence across disciplines. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `OSINT Setup Q1/3` — Which company, and in which market?
2. `OSINT Setup Q2/3` — What decision should this collection feed?
3. `OSINT Setup Q3/3` — Who signs the check? That decides which review sites, events, and analysts are worth sweeping — G2 and a vertical trade show are different worlds.

In **Context dump** mode, extract every supplied signal into the inventory schema, account for it as found / inferred / still missing, tag anything without a checkable URL as an Assumption, and ask only about gaps. In **Best guess** mode, assume the largest general review site for the category, the two best-known industry events, and a twelve-month window; name each assumption. On silence: twelve-month window, competitor framing, Just Enough Mode. Proceed.

## What It Produces

Complete the [OSINT Collection Sweep](template.md), written to the single-discipline schema in `reference/output-schemas.md`:

- signal inventory: one observation per row, with source URL, date, and F/I/A label
- strongest inference chains, ranked, capped at five
- the say-versus-said-about gap
- watch items — single signals, logged only
- collection gaps and handoffs, using the gap language rather than padding
- assumptions to validate
- the four-option Final Step block

No confidence ratings. No verdicts. Those belong to fusion.

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark every finding as an Assumption with its knowledge vintage, and invent nothing.
2. **Show the search plan.** Three bullets: sweep order, date window, noise filter. Name the same-name companies and the stale acquisitions you are excluding — a filter that names nothing has been mentioned, not applied. Continue unless revised.
3. **Sweep in this fixed order.** Newsroom and press output → analyst coverage and briefing chatter → exec and company social → review-site clusters on the `[BUYER]`'s sites → conference and webinar footprint → prediction markets where a regulation or milestone gates `[MARKET]`. Do not reorder because one channel looks juicier. The order is the defensibility.
4. **Log every signal immediately** into the inventory: what was observed, source URL with date, F/I/A label, the inference chain it supports, and the artifact it feeds. One observation per row — if a row needs the word "and," it is two rows.
5. **Collapse recycled sources as you go.** Follow each item to its origin. A press release and its coverage collapse to one row with the collapse noted.
6. **Run the discipline's inference chains explicitly.** Exec posting on a new problem space → positioning pivot forming. Sponsor-tier jump → market entry or doubling down. Review complaints clustering → their roadmap pressure point. Webinar topic shifts → what they will sell next. Sudden silence on a product line → sunset in progress. Prediction-market movement → crowd-priced expectations. State the lead time with each.
7. **Compute the say-versus-said-about gap.** Their language, the customers' language, and the subtraction. Name defended ground, exposed flank, and unclaimed whitespace.
8. **Rank and cut to five chains.** A sweep that reports everything found has not done the ranking that makes it useful.
9. **Report what returned nothing,** in one line, naming what was swept and what the absence itself suggests. Empty sections are findings.
10. **Stop before rating confidence.** Hand the inventory to `mi-fuse-all-source`.

## Human Decision Gate

Present the inventory and the gap. Highlight:

- which rows rest on the company's own words
- which apparent corroborations collapsed to a single origin, and how many
- which review clusters are recurring across sources versus concentrated in one
- what the sweep could not reach, and which run would close it

Use an Adaptive Decision Ladder: `Hand this to fusion`, `Mine the review clusters properly with voice-of-customer`, `Go deeper on one channel that looked thin`, or `Other (specify)`. Say in one sentence what each buys and what it gives up.

## Evidence and Attribution Rules

- Label every line **Fact** (documented in a checkable source), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated).
- A company's own words are a claim, not a fact about the market. "Cartelane says X" is a Fact about what Cartelane said; "Cartelane does X" is not established by it.
- **Do not invent:** press quotes, analyst ratings or rankings, review counts, star averages, event sponsorships, sponsor tiers, speaker rosters, webinar titles, or prediction-market odds. These are the specific fabrication risks of this discipline, and every one of them is the kind of detail a Product Manager will repeat out loud in a meeting.
- Every signal carries a real, checkable URL and a date. A signal you cannot source is an Assumption regardless of how plausible it reads.
- Quote reviews verbatim with platform and date, or describe the pattern and label it Inference. Never compose a representative quote.
- Stay inside the guardrails: published, posted, or publicly observable only. No pretexting, no soliciting NDA-protected information, no scraping in violation of terms you agreed to.

## Common Failure Modes

- Counting a press release and its three coverage articles as four signals
- Treating the company's own product page as a Fact about the market
- Letting one vivid find set the tone for the whole sweep
- Reporting review complaints as a feature backlog for your own product
- Sweeping the review sites you know instead of the ones the `[BUYER]` reads
- Quoting a prediction market with no liquidity check
- Padding a channel that returned nothing so the document looks symmetrical
- Rating the threat, which is fusion's job and not this run's
- Collecting past the point where the `[DECISION]` would change

## Assets and Examples

- [OSINT Collection Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Hand this inventory to all-source fusion (Recommended)
2. Mine the review clusters properly with voice-of-customer
3. Schedule this as a monthly OSINT digest so the next run is a diff
4. Turn the say-versus-said-about gap into positioning input

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: OSINT](../../reference/disciplines.md)
- [Sweep playbooks: OSINT sweep](../../reference/sweep-playbooks.md)
- [Output schemas: single-discipline sweep](../../reference/output-schemas.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
