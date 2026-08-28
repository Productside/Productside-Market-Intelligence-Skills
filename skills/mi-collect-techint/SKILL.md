---
name: mi-collect-techint
description: Sweep patents, trademarks, changelogs, API diffs, repos, standards bodies, and preprints for what a company is building. Use when a roadmap bet depends on what ships in 12 to 18 months.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company] [suspected capability]"
intent: >-
  Run the patent-examiner discipline on one company. R&D leaves fingerprints 12 to
  18 months before products ship, in registries that are free and almost never
  read. Exists because a roadmap bet made on a competitor's press release is made
  a year late.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: TECHINT
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Technical Product Manager
  - Business Analyst
  - Competitive Intelligence Analyst
  - Engineering Leadership
best-for:
  - "Deciding whether to accelerate or concede a capability before a competitor announces it"
  - "Distinguishing a committed R&D bet from exploratory filing noise"
  - "Putting a clock on a roadmap implication rather than just a direction"
scenarios:
  - "They keep filing in one patent classification and I want to know what it means"
  - "Their API docs grew endpoints for something that is not in the product"
  - "A trademark appeared that looks like a product name"
  - "Their staff are publishing preprints in a specialty we do not staff"
evidence-required:
  - "The target company and its assignee names"
  - "The suspected capability, specific enough to be wrong"
  - "The roadmap decision this collection feeds"
produces:
  - "Fusion-ready signal inventory with a mandatory lead-time column"
  - "Built-versus-shipped read, including deprecations"
  - "Ranked inference chains with clocks attached"
  - "Collection gaps and named handoffs"
estimated-time: "45-90 min"
group-size: "1-4"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
  - mi-collect-humint
  - mi-build-battle-card
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, TECHINT discipline"
  - "Public patent, trademark, and standards registries as primary sources"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://patents.google.com/
interface:
  display_name: "TECHINT Collection Sweep"
  short_description: "Read the fingerprints R&D leaves behind"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-techint to sweep patents, trademarks, changelogs, API diffs, repos, standards bodies, and preprints on this company, attach a lead time to every signal, and stop before rating confidence."
  allow_implicit_invocation: true
---

# TECHINT Collection Sweep

## Purpose

Read the fingerprints. R&D leaves them twelve to eighteen months before products ship.

TECHINT is the discipline that makes roadmap decisions early enough to matter. A patent cluster, a trademark filing, an API endpoint for a capability that is not in the product, a preprint by a staff researcher — each carries a typical lead time, and together they let you decide whether to accelerate or concede *before* a competitor's launch, which is the only time that decision is cheap.

The sweep produces a labeled inventory, not a verdict. **Collection is not fusion.** A sweep gathers and labels; rating confidence across disciplines belongs to `mi-fuse-all-source`. TECHINT's strongest pairing lives there: a paper or patent cluster next to a hiring surge in the same specialty is one of the most reliable signals available, and neither half establishes it alone.

## When to Use It

Use it when a roadmap bet turns on what a competitor is building rather than what they are selling. Use it when you suspect a specific capability and need to know whether it is staffed exploration or a committed program. Use it when a battle card needs a countdown clock instead of a feature checkbox.

Do not use it when:

- **The question is whether the bet is staffed.** Filings show intent to build; job postings show someone hired to do it. Run `mi-collect-humint` and pair them in fusion.
- **The question is when it launches to customers.** Launch staging shows up in SIGINT — new subdomains, certs, app-store metadata. TECHINT tells you what exists; SIGINT tells you when it is being wheeled out.
- **The target files nothing.** Small private companies often hold no patents and publish nothing. That is a finding about the channel, not a reason to infer from silence.
- **You want a feature comparison.** Building a card from feature parity is the failure this discipline most often enables. Build it from which customer problem each side solves.

## Input

Require:

- `[TARGET]`, and the assignee names it files under — these frequently differ from the trading name and from each other after acquisitions
- `[CAPABILITY]`, specific enough to be falsifiable. "Platform expansion" fits any company in any quarter; "native ERP connectors replacing partner-built ones" can be wrong.
- the roadmap `[DECISION]` this feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given. Never ask the user for patent numbers or repo names; finding them is the run.

**Example invocation:** `Use $mi-collect-techint on Cartelane. Suspected capability: native ERP integration replacing their partner-built connectors. Decision: accelerate or concede our own integration work this quarter.`

## Key Concepts

**Built versus shipped** — The signature output. What the registries and repos show them constructing, set against what customers can actually buy today. The gap in one direction is a countdown clock; the gap in the other is abandonment. **Deprecations are the most informative half and the most skipped**, because a removed endpoint or a sunset SDK says what a company has given up on — and giving up is a decision they will never announce.

*Violation signal:* The sweep lists what a company is building and never says what it stopped building.

**Clusters, not filings** — A single patent is noise. Five or more filings in one classification within twelve months is a committed bet on a capability, because patent prosecution costs real money and companies do not cluster by accident. The unit of analysis is the cluster; a report organized as a list of individual patents has not done the analysis, only the retrieval.

*Violation signal:* The inventory enumerates patents by number without ever naming a classification concentration.

**Lead time is mandatory** — Every signal in this discipline carries a clock, and the inventory has a required column for it. Patents run twelve to eighteen months ahead of product; trademarks six to twelve, because they are cheap and companies file close to launch; preprints six to twenty-four; funded consortia twelve to forty-eight; API endpoints weeks. A roadmap implication without a clock is a direction without a deadline, and a direction cannot be scheduled against.

*Violation signal:* An inference chain says a competitor is building something, and the reader cannot tell whether to worry this quarter or next year.

**Inventors and authors are the team** — Names repeating across filings identify the actual product team behind an initiative, which is far more actionable than the filings themselves. Their conference talks, public profiles, and prior employers describe the approach being taken. Author affiliations shifting from a university to the target across successive papers means they hired the lab, not just the idea.

*Violation signal:* A patent cluster is reported with no attempt to identify who is behind it.

**Standards participation is rule-writing** — A company chairing a standards committee intends to shape the rules of the market, not merely play by them. This is a slow, high-conviction signal with a long horizon, and it is invisible to anyone reading only the product press.

*Violation signal:* Standards and consortium activity is omitted entirely, so a long-range structural bet reads as absent.

**Trademarks are the closest clock** — Trademarks are cheap and companies file near launch, so a product-sounding name entering the register is one of the tightest lead times available: six to twelve months. A trademark filed shortly after a funded research project completes signals commercialization underway, which is a different and stronger read than either signal alone.

*Violation signal:* A trademark filing is reported as branding trivia rather than as a launch clock.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a TECHINT sweep — patents, trademarks, changelogs, API diffs, repos, standards, preprints — ending in a fusion-ready signal inventory where every row carries a lead time. Forty-five to ninety minutes. I will stop before rating confidence. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `TECHINT Setup Q1/3` — Which company, and what capability do you suspect? Specific enough to be wrong is better than broad enough to be safe.
2. `TECHINT Setup Q2/3` — What roadmap decision does this feed, and by when?
3. `TECHINT Setup Q3/3` — Are there prior assignee names, acquisitions, or research partnerships I should sweep alongside the obvious one?

In **Context dump** mode, extract supplied filings and changelog notes into the inventory, attach lead times, and ask only about gaps. In **Best guess** mode, sweep the obvious assignee plus known acquisitions, use a twenty-four-month window for patents and twelve for changelogs, and name each assumption. On silence: twenty-four-month patent window, no suspected capability, report clusters as found. Proceed.

## What It Produces

Complete the [TECHINT Collection Sweep](template.md), written to the single-discipline schema in `reference/output-schemas.md`:

- signal inventory with a **mandatory lead-time column**, plus source URL, date, and F/I/A label
- classification clusters with filing counts and windows
- built-versus-shipped read, including deprecations
- ranked inference chains, capped at five, each with a clock
- watch items, collection gaps, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption with its vintage, and invent no patent numbers under any circumstances.
2. **Show the search plan.** Sweep order, date window, noise filter — including which assignee-name variants and acquired entities you are including, and which same-name assignees you are excluding. Continue unless revised.
3. **Sweep in this fixed order.** Patent search by assignee and classification, looking for clusters → inventor names repeating → trademark filings → public changelogs, release notes, and deprecations → API documentation diffs → repo and SDK activity → standards committee participation → funded research consortia → preprints and conference papers by affiliated authors.
4. **Log every signal immediately** with source URL, date, F/I/A label, and **lead time**. One observation per row.
5. **Cluster before interpreting.** Count filings per classification per twelve months. Name the concentration, then read it.
6. **Identify the people.** Repeating inventor and author names, and where they came from.
7. **Run the discipline's inference chains explicitly.** Patent cluster → committed bet, not exploration. Trademark → launch inside six to twelve months. Trademark after a funded project completes → commercialization underway. Repeated appearance in funded consortia → long-range bet with twelve to forty-eight months of lead time. Named pilot sites → likely launch customers. Standards chairmanship → intent to shape the rules. Preprint cluster → R&D direction six to twenty-four months ahead. Affiliation shifts → they hired the lab. New API endpoints for unreleased capability → beta running now. Public SDK scaffolding → developer platform play.
8. **Write the built-versus-shipped read,** and give deprecations equal space.
9. **Report what returned nothing** in one line, naming what was swept. A company with no patents is telling you their moat is not legal, which is worth knowing.
10. **Stop before rating confidence.** Hand the inventory to `mi-fuse-all-source`, and flag the HUMINT pairing explicitly.

## Human Decision Gate

Present the inventory and the built-versus-shipped read. Highlight:

- which clusters are large enough to be commitments and which are single filings
- the shortest lead time in the set, because that is the one that sets the deadline
- whether the suspected `[CAPABILITY]` was corroborated, contradicted, or simply not addressed by the evidence
- that no story here can rate above working hypothesis without a second discipline

Use an Adaptive Decision Ladder: `Hand this to fusion and run HUMINT next`, `Go deeper on one cluster`, `Turn the shortest clock into a roadmap decision date`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every line **Fact** (in a registry, repo, or published document), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** patent numbers, application or grant dates, classification codes, inventor names, trademark serial numbers, paper titles, author names, repository names, endpoint names, or version numbers. These are checkable in seconds and fabricating one destroys the credibility of the entire brief.
- A filing establishes what was filed, not what works. A patent is a claim staked, not a product delivered.
- Distinguish a granted patent from a published application. The second is far more common and far less committal.
- Every signal carries a real, checkable URL and a date.
- Stay inside the guardrails: published registries, public repos, and published papers only.

## Common Failure Modes

- Listing patents instead of finding clusters
- Reporting what is being built and omitting what was deprecated
- Omitting the lead-time column, which turns a scheduling signal into trivia
- Reading a single patent as a strategy
- Treating a published application as though it were granted
- Sweeping only the obvious assignee and missing the acquired entity that holds the filings
- Building a feature-parity comparison instead of a capability read
- Concluding the bet is real without HUMINT, which is fusion's call and needs a second discipline
- Padding the standards section for a company that participates in none

## Assets and Examples

- [TECHINT Collection Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Hand this to fusion and run HUMINT next to test whether the bet is staffed (Recommended)
2. Go deeper on the largest classification cluster
3. Schedule a quarterly TECHINT pass so the next run is a diff
4. Turn the shortest lead time into a dated roadmap decision

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: TECHINT](../../reference/disciplines.md)
- [Sweep playbooks: TECHINT sweep](../../reference/sweep-playbooks.md)
- [Output schemas: the lead-time column](../../reference/output-schemas.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [Google Patents](https://patents.google.com/)
