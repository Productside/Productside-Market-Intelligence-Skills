---
name: mi-collect-finint
description: Follow the money on a company — filings, Risk Factors diffs, earnings dodges, procurement awards, entity registrations, state capital. Use to separate a funded move from a narrated one.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company] [geography] [decision]"
intent: >-
  Run the forensic-accountant discipline on one company. Companies lie in press
  releases and lie less in filings, because lying there is a felony. Exists
  because money is the least deniable signal a company emits, and because most
  competitive briefs never open a single filing.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: FININT
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
  - "Testing whether an announced strategy is funded or merely narrated"
  - "Finding what genuinely scares a competitor, in the section they are legally required to write"
  - "Deriving a realistic deal size and capture rate for a sizing model"
scenarios:
  - "They announced a platform play and I need to know if anyone is paying for it"
  - "We keep losing to an incumbent whose procurement scope quietly keeps expanding"
  - "Our SOM assumption is a guess and finance is going to ask where it came from"
  - "A sovereign or state-linked investor turned up on their cap table"
evidence-required:
  - "The target company and its filing jurisdictions"
  - "The geography in scope, at country level"
  - "The decision this collection feeds"
produces:
  - "Fusion-ready signal inventory with URLs, dates, and evidence labels"
  - "Risk Factors year-over-year diff"
  - "Money-versus-message read"
  - "Capture-rate inputs for sizing, and collection gaps"
estimated-time: "45-90 min"
group-size: "1-4"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
  - mi-size-tam-sam-som
  - mi-refresh-earnings-signals
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, FININT discipline"
  - "Regional Source Overlays: EU and MENA, procurement and company-registry sections"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.sec.gov/edgar/search/
interface:
  display_name: "FININT Collection Sweep"
  short_description: "Follow the money through the filings"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-finint to sweep filings, Risk Factors diffs, earnings Q&A, procurement awards, and entity registrations on this company, land every figure with a source and a date, and stop before rating confidence."
  allow_implicit_invocation: true
---

# FININT Collection Sweep

## Purpose

Follow the money.

Companies lie in press releases. They lie less in filings, because lying there is a felony. FININT is the discipline that reads what a company was legally compelled to write down, and it is the fastest way to separate a strategy that is funded from a strategy that is narrated.

It is also the discipline most Product Managers skip, on the theory that filings are finance's job. They are not. The Risk Factors section is a competitor telling you, under penalty, what genuinely frightens them — and it is free.

The sweep produces a labeled inventory, not a verdict. **Collection is not fusion.** A sweep gathers and labels; rating confidence across disciplines belongs to `mi-fuse-all-source`.

## When to Use It

Use it when the question is whether something is real. An announcement plus a capex line is a different object from an announcement alone. Use it when a sizing model needs a defensible capture rate, when an incumbent keeps winning accounts you cannot see into, or when you need to know how much runway a competitor actually has before you plan a price fight.

Do not use it when:

- **The target is private and pre-revenue.** Say so early. A seed-stage company generates incorporation records and little else, and the honest output is a short list of what cannot be known — not four paragraphs of inference from a Crunchbase page.
- **You want a quarterly language diff on a company you already profiled.** That is `mi-refresh-earnings-signals`, which diffs rather than rebuilds.
- **The question is what customers think.** Money says what a company committed to, never why a deal closed.
- **You need the market's size rather than one company's economics.** The denominator is GEOINT/DEMOINT; FININT supplies only the capture rate on top of it.

## Input

Require:

- `[TARGET]`, and its filing jurisdictions if already known
- `[GEOGRAPHY]` at country level — it determines which registries, procurement portals, and competition authorities apply
- the `[DECISION]` this collection feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given. Never ask the user for revenue, funding history, or ownership structure; finding those is the run.

If `[GEOGRAPHY]` is outside the US, load `reference/regional-overlays.md` before collecting. EU procurement lives in TED and national portals; MENA commitment evidence lives in Etimad, Monaqasat, and country platforms, in Arabic as well as English.

**Example invocation:** `Use $mi-collect-finint on Cartelane, US and Canada. Decision: whether their integration platform announcement is funded.`

## Key Concepts

**Money versus message** — The signature output. What the filings, awards, and capital structure say, set against what the press releases say. When a company's messaging and its resource allocation disagree, the resources are telling the truth. This is the single most reliable read in competitive intelligence and it requires no cleverness, only the willingness to open the document.

*Violation signal:* The sweep summarizes the company's stated strategy without ever setting it against a number.

**The Risk Factors diff** — Not the Risk Factors section: the *change* in it, year over year. Companies must disclose what threatens them, and they revise that list deliberately and defensively. A risk that appeared this year was added by lawyers who thought it now had to be there. A risk that disappeared was argued away. Reading the section once tells you what a large company is generically worried about; diffing it tells you what changed inside the building.

*Violation signal:* Risk Factors are quoted rather than compared, so every large company sounds equally worried about the same six things.

**The commitment ladder** — Announced, Funded, Procured, Staffed, Built. FININT is the discipline that establishes the middle three, and its whole value is refusing to let the first one masquerade as them. Treat announcements as intent until funding, procurement, land, permits, hiring, or contracts corroborate them. A capex line, a tender award, or a new subsidiary registration moves a story up the ladder; a keynote does not.

*Violation signal:* A story is described as committed on evidence that is entirely an announcement.

**The earnings dodge** — Analysts ask; executives deflect. The deflection is the signal, and it is more informative than any answer given, because a prepared non-answer marks a topic the company has decided not to discuss. Track which question got the longest non-answer, and track it across quarters. Dropped language matters as much as added language: a phrase repeated in four consecutive calls and absent in the fifth records a decision already made internally.

*Violation signal:* The earnings section quotes what executives said and never notes what they were asked and did not answer.

**Capture rate as arithmetic, not optimism** — Revenue divided by claimed customer count is a deal-size reality check, and it is where a SOM stops being a wish. A capture rate needs a horizon of three to five years and a named comparable company, because a percentage with neither is a number chosen to make the model work.

*Violation signal:* A SOM appears with a capture rate and no comparable, or with the phrase "1% of the market."

**Scope creep in procurement** — Contract modifications expanding an incumbent's scope are a locked-in account announcing itself in public, months before anyone in sales notices. Prior Information Notices and expressions of interest telegraph tenders three to twenty-four months out. This channel is invisible to competitors who only read the press, and it is entirely free.

*Violation signal:* An account is described as contestable with no check of whether its incumbent's contract was recently extended.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a FININT sweep — filings, Risk Factors diffs, earnings Q&A, procurement, entity registrations, capital structure — ending in a fusion-ready signal inventory and a money-versus-message read. Forty-five to ninety minutes. I will stop before rating confidence. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `FININT Setup Q1/3` — Which company, and in which countries do you need the money traced?
2. `FININT Setup Q2/3` — What decision should this feed: a sizing model, a pricing posture, a threat read, or an account strategy?
3. `FININT Setup Q3/3` — Is there a specific claim you want tested against the money — an announcement, a capability, a market entry?

In **Context dump** mode, extract every figure into the inventory, tag anything without a filing or portal link as an Assumption regardless of how confidently it was pasted, and ask only about gaps. In **Best guess** mode, assume the most recent annual and quarterly filings, a three-year Risk Factors window, and the primary listing jurisdiction; name each assumption. On silence: three-year window, US sources unless the geography says otherwise, Just Enough Mode. Proceed.

## What It Produces

Complete the [FININT Collection Sweep](template.md), written to the single-discipline schema in `reference/output-schemas.md`:

- signal inventory with source URL, date, and F/I/A label on every figure
- Risk Factors year-over-year diff: added, removed, materially reworded
- ranked inference chains, capped at five
- money-versus-message read
- capture-rate inputs, if sizing is downstream
- watch items, collection gaps, assumptions to validate, Final Step block

For a private target, the honest deliverable is often mostly gaps. Say so in the header rather than at the end.

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption with its vintage, and invent no figures whatsoever. Fabricated financials are the most dangerous output this library can produce.
2. **Show the search plan.** Sweep order, date window, noise filter — naming the same-name entities and the closed acquisitions being excluded. Continue unless revised.
3. **Establish the filing perimeter.** Legal entity, ownership status, tickers, exchanges, filing jurisdictions, subsidiaries. If the answer is "private, no filings," say it here and reset expectations before collecting.
4. **Sweep in this fixed order.** Latest annual and quarterly filings, **Risk Factors first and diffed against last year** → segment reporting structure → earnings call Q&A, specifically the dodges → funding, debt, and ownership structure → entity and subsidiary registrations in `[GEOGRAPHY]` → procurement awards and contract modifications → competition and state-aid cases.
5. **Log every figure immediately** with its source URL and date. One observation per row.
6. **Run the discipline's inference chains explicitly.** Risk Factors changes → what genuinely scares them. Segment restructure → which segment got promoted. Earnings dodges → the soft spot to probe in positioning. New entity registrations → market entry before announcement. Deferred revenue trend → real momentum versus stated momentum. Merger filings → market definitions and named competitors, from their own lawyers. Contract modifications → locked-in accounts. Sovereign or state-aid backing → their runway math changed, and discount pressure will not work.
7. **Place each story on the commitment ladder** and say which evidence put it there.
8. **Write the money-versus-message read.** Their stated strategy, their capital allocation, and the gap.
9. **Report what returned nothing** in one line, naming what was swept and what the absence suggests. A private company with no filings is telling you how much you will ever know through this channel.
10. **Stop before rating confidence.** Hand the inventory to `mi-fuse-all-source`.

## Human Decision Gate

Present the inventory and the money-versus-message read. Highlight:

- which figures are audited, which are company-reported, and which are estimates from third parties
- where the commitment ladder stops for each story
- whether the filing perimeter left material entities unswept
- what a paid data source would add, and whether the decision justifies it

Use an Adaptive Decision Ladder: `Hand this to fusion`, `Take the capture rate into sizing`, `Set up a quarterly earnings diff`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every line **Fact** (in a filing, award notice, or registry record), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** revenue, margins, funding amounts, valuations, deferred revenue, customer counts, contract values, award dates, ownership percentages, or executive quotes from earnings calls. A fabricated financial figure will be repeated to a CFO, and it will be checked.
- Distinguish audited figures from company-reported figures from third-party estimates. Crunchbase is not a filing.
- Record whether an amount is an announced budget, an approved budget, committed financing, a tender value, or an awarded contract. Those are five different numbers that routinely wear the same headline.
- Every figure carries a real, checkable URL and a date. An unsourced number is an Assumption.
- Stay inside the guardrails: filed, published, or publicly observable only.

## Common Failure Modes

- Quoting Risk Factors instead of diffing them
- Treating an announcement as commitment because the number attached to it was large
- Blending audited revenue and a press-reported estimate in the same table without saying which is which
- Reporting a headline budget as though it were an awarded contract
- Concluding "well capitalized" or "under pressure" without the figures that establish it
- Skipping procurement because the target sells commercially, and missing the public-sector accounts it quietly holds
- Deriving a capture rate with no horizon and no comparable
- Rating the threat, which is fusion's job
- Padding a section for a private company that simply does not file

## Assets and Examples

- [FININT Collection Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Hand this inventory to all-source fusion (Recommended)
2. Take the capture rate and deal-size read into sizing
3. Schedule a quarterly earnings and executive signal refresh
4. Turn the money-versus-message gap into positioning input

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: FININT](../../reference/disciplines.md)
- [Sweep playbooks: FININT sweep](../../reference/sweep-playbooks.md)
- [Regional overlays: procurement and company registries](../../reference/regional-overlays.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SEC EDGAR full-text search](https://www.sec.gov/edgar/search/)
