---
name: mi-collect-geoint-demoint
description: Pull the market's denominator from government statistics — establishment counts, occupations, wages, firmographics, trade flows. Use before sizing, ICP work, or persona localization.
license: CC-BY-NC-ND-4.0
argument-hint: "[market and codes] [countries in scope]"
intent: >-
  Run the cartographer's discipline. Government statistics are free intelligence
  most Product Managers never open, and they are the backbone of every ICP,
  persona, and TAM that survives scrutiny. Exists because a market sized without a
  denominator is a vibe with a dollar sign.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: GEOINT/DEMOINT
status: active
operating-level:
  - initiative
  - executive
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - Market Research Analyst
  - Strategy and Corporate Development
best-for:
  - "Establishing the establishment counts that a bottom-up TAM rests on"
  - "Drawing ICP boundaries from firmographic data rather than from vibes"
  - "Localizing personas when the buyer title changes across countries"
scenarios:
  - "Finance asked where our market size number came from and we do not have an answer"
  - "We are entering a second country and do not know if the buyer role exists there"
  - "Our ICP was drawn from our best twelve customers and nothing else"
  - "Two analyst reports disagree about this market by a factor of three"
evidence-required:
  - "The market and its NAICS, SIC, or NACE codes or nearest equivalent"
  - "Countries in scope, at country level"
  - "The buyer and end-user roles to count"
produces:
  - "Fusion-ready signal inventory with a mandatory vintage column"
  - "Establishment counts by code and size band — the denominator"
  - "Occupation, wage, and buyer-title prevalence by country"
  - "Firmographic ICP boundaries and trade-flow reads"
estimated-time: "60-120 min"
group-size: "1-4"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-size-tam-sam-som
  - mi-fuse-all-source
  - mi-collect-finint
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, GEOINT/DEMOINT discipline"
  - "Regional Source Overlays: EU and MENA, statistics and trade sections"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.census.gov/programs-surveys/cbp.html
interface:
  display_name: "GEOINT/DEMOINT Collection Sweep"
  short_description: "Find the denominator in public statistics"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-geoint-demoint to pull establishment counts, occupation and wage data, firmographics, and trade flows for this market, state the vintage of every dataset, and stop before building the sizing model."
  allow_implicit_invocation: true
---

# GEOINT/DEMOINT Collection Sweep

## Purpose

The cartographer's discipline. The terrain map, not troop movement.

Government statistics are free intelligence that most Product Managers never open, and they are the backbone of every ICP, persona, and TAM that survives scrutiny. Establishment counts by industry code and size band are the *denominator* — the number of things that could possibly buy you. Everything sized without one is a vibe with a dollar sign in front of it.

This is also the slowest-moving discipline, which cuts both ways: the data rots slowly, and it rots invisibly. Statistical releases lag, so every dataset here carries a **vintage**, not just a publication date.

The sweep produces a labeled inventory, not a model. **Collection is not fusion**, and it is not sizing either — this run gathers the counts; `mi-size-tam-sam-som` builds the model on top of them.

## When to Use It

Use it before any sizing exercise, before drawing ICP boundaries, and before localizing personas into a second country. Use it when two analyst reports disagree and you need a bottom-up number to referee them. Use it annually, because sizing rot is slow but real.

Do not use it when:

- **You need the model, not the counts.** This run produces the denominator; `mi-size-tam-sam-som` produces TAM, SAM, SOM, and sensitivity.
- **You need a capture rate.** That comes from FININT — a competitor's revenue divided by their claimed customer count — not from statistics.
- **The market is too new to have a code.** Emerging categories are not counted by statistical agencies. Say so honestly and size from an adjacent code with the substitution named, rather than pretending a code fits.
- **The geography is a sales region.** "EMEA" cannot be counted. Country level or nothing.

## Input

Require:

- `[MARKET]` and its NAICS, SIC, NACE, or nearest equivalent codes
- `[GEOGRAPHY]` at country level — this determines which statistical agency has jurisdiction, and there is no substitute
- `[BUYER]` and end-user roles, which is what makes occupation data usable

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given.

If `[GEOGRAPHY]` is outside the US, load `reference/regional-overlays.md` first. Eurostat and national statistical institutes for the EU; GCC-Stat, GASTAT, FCSC, CAPMAS, HCP and peers for MENA; World Bank, IMF, OECD.Stat, and UN Comtrade as global cross-checks.

**Example invocation:** `Use $mi-collect-geoint-demoint for mid-market revenue operations tooling, NAICS 541511 and 511210, United States and Germany. Buyer is VP RevOps.`

## Key Concepts

**Vintage, not publication date** — The mandatory column. A dataset published in 2026 may describe 2023. That distinction is the difference between a Fact about the past and an Assumption about now, and statistical agencies rarely make it prominent. Name the vintage of every dataset and flag anything older than the decision's horizon. A 2019 establishment count answering a 2026 sizing question is a Fact about 2019 and an Assumption about today.

*Violation signal:* A table cites publication years and never says which period the data describes.

**The denominator** — The signature output. Establishment counts by industry code and employee size band: how many organizations of the relevant shape exist at all. Every credible bottom-up size starts here, and every incredible one starts with a percentage of somebody else's headline number. The denominator is also what makes a sizing model *falsifiable*, which is why finance asks for it.

*Violation signal:* A market size appears with no count of the things being sized.

**Codes are a fit, not a fact** — NAICS, SIC, and NACE were designed for statistical reporting, not for your category. Most software markets map imperfectly onto them, and the mapping is a judgment you make and must disclose. Two defensible code selections can differ by a factor of three, which is often the entire disagreement between two analyst reports.

*Violation signal:* Codes are listed as though selected by the data rather than chosen by the analyst, with no note on what they over- or under-capture.

**Buyer titles do not survive borders** — The "VP of Product" you message in Boston is a "Head of Digital" in Frankfurt and may not exist in Riyadh. Occupation counts and title prevalence by country are how a persona gets localized, and skipping this step is how a market entry discovers, two quarters in, that it has been targeting a job that nobody holds.

*Violation signal:* A persona is carried into a new country with the buyer title unchanged and unchecked.

**Wages bound willingness to pay** — Wage trends in buyer and end-user roles set a ceiling on what a market can absorb, and they move slowly enough to be reliable. A pricing corridor validated against occupation wage data is defensible in a way that competitor-price benchmarking alone is not, because competitor prices reflect what vendors hope rather than what buyers can fund.

*Violation signal:* A pricing corridor is justified entirely by competitor prices, with no reference to what the buying population earns or budgets.

**Disagreement is a finding** — When two independent analyst reports differ by threefold, report both and say so. Picking the flattering one is the single most common way a business case dies in front of finance: not because the number was wrong, but because someone else found the other number.

*Violation signal:* One market-size estimate is cited where several exist, with no mention that others disagree.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a GEOINT/DEMOINT sweep — establishment counts, occupations, wages, firmographics, title prevalence, trade flows — ending in a fusion-ready inventory where every dataset carries its vintage. One to two hours. I will produce the denominator, not the sizing model. Up to four setup questions, because the constraint set here is wider. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, cap of four:

1. `GEO Setup Q1/4` — Which market, and do you already have codes, or should I select and disclose them?
2. `GEO Setup Q2/4` — Which countries, at country level?
3. `GEO Setup Q3/4` — Which buyer and end-user roles should I count occupations for?
4. `GEO Setup Q4/4` — What are your real eligibility constraints — size band, segment, compliance, tech prerequisites? Those turn a denominator into a serviceable one.

In **Context dump** mode, extract supplied figures, attach vintages, flag anything stale against the decision horizon, and ask only about gaps. In **Best guess** mode, select the closest codes, disclose what they over- and under-capture, use the most recent complete vintage, and name each assumption. On silence: US only, most recent complete vintage, codes selected and disclosed. Proceed.

## What It Produces

Complete the [GEOINT/DEMOINT Collection Sweep](template.md), written to the single-discipline schema in `reference/output-schemas.md`:

- signal inventory with a **mandatory vintage column**, plus source URL, date, and F/I/A label
- establishment counts by code and size band, per country — the denominator
- occupation counts, growth, and wage trends for buyer and end-user roles
- buyer-title prevalence by country
- firmographic distributions and the ICP boundaries they support
- trade-flow reads where product codes apply
- conflicting estimates, reported as conflicts
- watch items, collection gaps, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark every figure as an Assumption with its vintage, and invent no counts. A fabricated establishment count will be defended in front of finance.
2. **Select and disclose codes.** Name the NAICS, SIC, NACE, or local equivalents chosen, and say explicitly what each over-captures and under-captures. This is a judgment, and hiding it is how two credible models end up threefold apart.
3. **Show the search plan.** Sweep order, vintage window, and how you will avoid double-counting establishments across overlapping codes. Continue unless revised.
4. **Sweep in this fixed order.** Establishment counts by industry code and employee band → regional concentration → occupation counts and growth for the `[BUYER]` and end-user roles → wage trends in those roles → firmographic distributions by size band, legal form, and sector → buyer-title prevalence by country → trade flows in product-specific codes → the target's own physical footprint and regions served.
5. **Record the vintage of every dataset,** not just its publication date, and flag anything older than the decision's horizon.
6. **Log every figure immediately** with source URL, date, vintage, and F/I/A label.
7. **Run the discipline's inference chains explicitly.** Establishment counts → the bottom-up denominator. Regional concentration → where SOM lives and where field sales should live. Occupation growth → is the population you sell to growing or shrinking. Wage trends → willingness-to-pay ceiling and pricing corridor. Firmographic distributions → ICP boundaries from data. Title prevalence → persona localization. Trade-flow shifts → market entry or supply relocation ahead of announcement.
8. **Cross-check against two independent analyst estimates.** If they disagree by threefold, report both and say so. Do not pick.
9. **Report what returned nothing** in one line — including the honest case where a market is too new to be counted.
10. **Stop before building the model.** Hand the denominator to `mi-size-tam-sam-som`.

## Human Decision Gate

Present the counts and the code selection. Highlight:

- what the chosen codes over- and under-capture, in plain language
- the oldest vintage in the set, and whether it clears the decision's horizon
- where independent estimates conflict, and by how much
- which countries returned usable occupation data and which did not

Use an Adaptive Decision Ladder: `Take this denominator into sizing`, `Widen or narrow the code selection first`, `Add a country`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every line **Fact** (in a published statistical release), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** establishment counts, occupation counts, wage figures, employment totals, trade volumes, growth rates, or market size numbers. These are the figures a business case rests on, and every one of them is checkable.
- State the vintage separately from the publication date, always.
- Disclose the code selection as an analyst judgment, with what it misses.
- A statistic older than the decision's horizon is an Assumption about the present, regardless of how authoritative its source.
- Where two independent estimates disagree materially, report both. Never average them into a comfortable middle.
- Every figure carries a real, checkable URL.

## Common Failure Modes

- Reporting publication dates as though they were vintages
- Presenting a code selection as though the data chose it
- Double-counting establishments across overlapping codes
- Carrying a buyer title into a new country unchecked
- Justifying a pricing corridor entirely from competitor prices
- Citing one analyst estimate where several conflict
- Sizing an emerging category against a code that does not fit, without saying so
- Building the TAM here instead of handing over the denominator
- Treating "EMEA" as a geography

## Assets and Examples

- [GEOINT/DEMOINT Collection Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Take this denominator into sizing (Recommended)
2. Widen or narrow the code selection and re-count
3. Schedule an annual refresh, since sizing rot is slow but real
4. Turn the firmographic distribution into ICP boundaries

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: GEOINT/DEMOINT and the TAM/SAM/SOM recipe](../../reference/disciplines.md)
- [Sweep playbooks: GEOINT/DEMOINT sweep and the vintage column](../../reference/sweep-playbooks.md)
- [Regional overlays: statistics bureaus and trade data](../../reference/regional-overlays.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [US Census County Business Patterns](https://www.census.gov/programs-surveys/cbp.html)
