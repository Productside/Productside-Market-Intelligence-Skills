---
name: mi-collect-masint
description: Measure a company's operational and physical exhaust — supply chain, facilities, permits, certifications, ops capacity, scale proxies. Use to catch a buildout or a strain before either is announced.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company] [suspected buildout or strain]"
intent: >-
  Run the satellite-photo discipline on one company. Abnormal resource allocation
  never lies, but it never explains itself either. Exists because operational
  exhaust reveals capacity decisions 6 to 36 months before announcements, and
  because every anomaly found here needs a named path to disambiguation.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: MASINT
status: active
operating-level:
  - product-team
  - initiative
  - executive
audience:
  - Product Manager
  - Business Analyst
  - Competitive Intelligence Analyst
  - Strategy and Corporate Development
  - Operations Leadership
best-for:
  - "Catching a facility, capacity, or certification buildout well before any announcement"
  - "Detecting operational strain that a competitor's messaging is covering"
  - "Estimating a private company's real scale from public operational proxies"
scenarios:
  - "Their support response times have been stretching for two months"
  - "A competitor reserved power capacity in an industrial zone"
  - "They appeared in a notified-body register for a product category they do not sell"
  - "Import volumes for their critical component jumped twenty percent"
evidence-required:
  - "The target company and whether it moves physical goods"
  - "The suspected buildout or strain, if any"
  - "The decision this collection feeds"
produces:
  - "Fusion-ready signal inventory with a mandatory disambiguate-via column"
  - "Scale proxies with trend direction and stated windows"
  - "Anomalies with candidate explanations, never with verdicts"
  - "Collection gaps and named handoffs"
estimated-time: "45-90 min"
group-size: "1-3"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
  - mi-collect-finint
  - mi-collect-humint
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, MASINT discipline"
  - "Regional Source Overlays: EU and MENA, facilities and certification sections"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://comtradeplus.un.org/
interface:
  display_name: "MASINT Collection Sweep"
  short_description: "Measure the operational exhaust"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-masint to sweep supply chain, facilities, permits, certifications, and ops capacity on this company, name a disambiguation path for every anomaly, and stop before rating confidence."
  allow_implicit_invocation: true
---

# MASINT Collection Sweep

## Purpose

The satellite photo. Measure the physical and operational exhaust.

Abnormal resource allocation never lies. A company reserving power capacity, selecting a notified body, changing supplier geographies, or letting support response times stretch is making a decision that costs money, and it is doing so in public records six to thirty-six months before anything gets announced.

MASINT also has the discipline's defining weakness: **an anomaly never explains itself.** Input volumes up twenty percent is pre-launch buildup or demand collapse, and only another discipline tells you which. So this sweep carries a mandatory column naming, for every anomaly, the discipline that would resolve it. A MASINT signal without a disambiguation path is a Rorschach test, not intelligence.

The sweep produces a labeled inventory, not a verdict. **Collection is not fusion.**

## When to Use It

Use it when the question is capacity: are they building for something, or straining under something. Use it when a competitor's messaging is confident and you suspect their operations are not. Use it to estimate a private company's real scale when no filings exist.

Do not use it when:

- **The target is pure software with no physical footprint** and you expect supply-chain findings. The software equivalent is ops capacity plus infrastructure-scale language, and it is thinner. Say so before collecting rather than after.
- **You need to know what they are building.** MASINT sees that capacity is being added; TECHINT sees what it is for.
- **You need the anomaly resolved.** This sweep names the disambiguation path; it does not walk it. That is fusion's job, with FININT or HUMINT.
- **You are tempted by imagery or observation of non-public property.** Everything here is published, filed, or observable from public sources. The line is not negotiable.

## Input

Require:

- `[TARGET]`, and whether it moves physical goods at all
- the suspected buildout or strain, if there is one
- the `[DECISION]` this feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given.

If `[GEOGRAPHY]` is outside the US, load `reference/regional-overlays.md` first. Facilities evidence in the EU runs through environmental permits and NANDO notified-body designations; in MENA through industrial-zone tenancy, utility-connection approvals, and EPC contract awards.

**Example invocation:** `Use $mi-collect-masint on Cartelane. Pure software, so focus on ops capacity. Decision: is their support strain real enough to put on a card?`

## Key Concepts

**Every anomaly names its disambiguator** — The mandatory column. Input volumes up twenty percent means pre-launch buildup *or* demand collapse; support times stretching means cash constraint *or* overwhelmed by growth; a hiring freeze in support means cost discipline *or* automation. Each of these is two opposite stories with one signature, and the sweep's job is to name which discipline settles it, not to guess. This is the rule that keeps MASINT from being the most confidently wrong discipline in the set.

*Violation signal:* An anomaly is reported with a single interpretation and no alternative named.

**Trend direction needs a window** — "Support response times are stretching" is not a measurement. "Median first response moved from 4 hours to 19 hours across sampled tickets between May and August" is. Every proxy carries the window it was measured over and the method used, because a proxy without a window is an impression with a number attached.

*Violation signal:* A trend is asserted with no period, no sample, and no method.

**Registries telegraph regulated entry** — A certification listed as "in process," or a company selecting a notified body for a product category it does not currently sell, is a twelve-to-thirty-six-month runway into a regulated segment, visible to anyone who checks. It is one of the longest-lead signals available and among the least contested, because almost nobody looks.

*Violation signal:* A regulated-market entry is discovered from the launch press release when the registry entry was public two years earlier.

**Commitment is physical** — Land allocation, utility capacity reservations, environmental permits, and engineering-design contracts precede equipment procurement, which precedes any announcement by six to thirty-six months. This is the discipline that most directly answers whether an announced ambition is funded and underway, and it is why MASINT sits alongside FININT on the commitment ladder.

*Violation signal:* An announced facility or expansion is accepted at face value with no check for a permit, a lease, or a utility approval.

**Scale proxies are estimates, and must read as estimates** — Review velocity, community size, support-forum volume, integration counts, package download counts, and app rankings can bracket a private company's scale. They are proxies: they carry platform bias, they can be gamed, and they measure attention as much as usage. Report them as a range with the proxy named, never as a headcount or a revenue figure.

*Violation signal:* A proxy is converted into a revenue or customer estimate without stating the conversion assumption.

**Absence is a finding, not a failure** — A software company with no supply chain has not produced a MASINT failure. It has produced a fact about which channels can ever inform you about them. Report it in one honest line and substitute ops capacity; do not pad the section to make the document symmetrical.

*Violation signal:* A supply-chain subsection exists for a company that ships no goods, filled with adjacent-sounding material.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a MASINT sweep — scale proxies, supply chain, facilities and permits, certifications, ops capacity — ending in a fusion-ready inventory where every anomaly names the discipline that would resolve it. Forty-five to ninety minutes. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `MASINT Setup Q1/3` — Which company, and do they move physical goods? If not, I will run the ops-capacity variant and say so up front.
2. `MASINT Setup Q2/3` — Is there a suspected buildout or strain, or should I report anomalies as found?
3. `MASINT Setup Q3/3` — What decision does this feed: a threat read, a launch-timing estimate, or a battle card?

In **Context dump** mode, extract supplied operational data into the inventory and attach disambiguation paths. In **Best guess** mode, assume ops-capacity focus for software targets, a ninety-day sampling window for response-time proxies, and name each assumption. On silence: ninety-day window, anomalies reported as found, no suspected capability. Proceed.

## What It Produces

Complete the [MASINT Collection Sweep](template.md), written to the single-discipline schema in `reference/output-schemas.md`:

- signal inventory with a **mandatory disambiguate-via column**, plus URL, date, and F/I/A label
- scale proxies with trend direction, window, and method
- anomalies with **candidate explanations**, at least two per anomaly
- ranked inference chains, capped at five
- watch items, collection gaps, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption with its vintage, and invent no volumes, permit records, or dates.
2. **Declare the physical-goods question up front.** If the target ships nothing, say so in the header and run the ops-capacity variant. This prevents a reader from mistaking a thin section for a thin company.
3. **Show the search plan.** Sweep order, date window, noise filter, and the sampling method for any proxy you intend to measure. Continue unless revised.
4. **Sweep in this fixed order.** Scale proxies (app ranks, review velocity, community size, support-forum volume, integration counts, package downloads) → trend direction on each with the window stated → supply chain and import/export records where physical goods exist → facilities, permits, land, utility connections → certification and notified-body registries → ops capacity via status pages and support-response sampling → anomalies with candidate explanations.
5. **Log every signal immediately** with source URL, date, F/I/A label, and **disambiguate-via**. One observation per row.
6. **State the window and method for every proxy.** How many observations, over what period, sampled how.
7. **Run the discipline's inference chains explicitly.** Twenty percent input volume change → pre-launch or demand collapse; check via FININT. New supplier geographies → entry, tariff hedging, or resilience. Certification in process → twelve to thirty-six months into a regulated segment. Recalls or safety alerts → quality strain, with a public citation. Land, power, or engineering contracts → buildout six to thirty-six months out. Support times stretching plus a support hiring freeze → cash constraint or growth overwhelm; disambiguate via HUMINT sentiment. Office consolidation → cost compression, expect pricing aggression.
8. **Give every anomaly at least two candidate explanations** and name which discipline separates them.
9. **Report what returned nothing** in one line, naming what was swept and what the absence means for this target permanently.
10. **Stop before rating confidence.** Hand the inventory to `mi-fuse-all-source`.

## Human Decision Gate

Present the inventory and the anomalies. Highlight:

- which anomalies have two live explanations pointing opposite directions
- which proxies were measured versus estimated, and their windows
- the longest-lead signal found, because that is the one worth scheduling against
- what a second discipline would resolve, and which one

Use an Adaptive Decision Ladder: `Hand this to fusion and run FININT to disambiguate`, `Sample the ops proxies again in thirty days to establish a trend`, `Go deeper on the certification registry`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every line **Fact** (in a record, registry, or measured sample), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** import or export volumes, download counts, review velocity, permit records, lease details, utility approvals, certification dates, notified-body designations, incident dates, or response-time measurements. Operational figures are the easiest to fabricate plausibly and the hardest for a reader to check.
- State the sampling method for anything measured. An unmeasured impression is an Assumption.
- Never convert a proxy into a revenue or headcount figure without stating the conversion assumption as an Assumption.
- Every signal carries a real, checkable URL and a date.
- Stay inside the guardrails: published records, public registries, and publicly observable operations only. No surveillance of private property, no access to anything behind an authentication boundary.

## Common Failure Modes

- Reporting an anomaly with one interpretation, when it has two opposite ones
- Asserting a trend with no window, sample size, or method
- Padding a supply-chain section for a company that ships nothing
- Converting downloads or community size into a revenue estimate silently
- Treating an announced facility as a buildout with no permit or lease behind it
- Skipping certification registries because they look like compliance paperwork
- Reading a single status-page incident as a capacity signal
- Rating the threat, which is fusion's job and doubly wrong here, because the evidence is ambiguous by construction

## Assets and Examples

- [MASINT Collection Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Hand this to fusion and run FININT to disambiguate the anomalies (Recommended)
2. Re-sample the ops proxies in thirty days to establish a real trend
3. Schedule a quarterly MASINT pass so the next run is a diff
4. Turn the certification finding into a dated threat-assessment entry

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: MASINT](../../reference/disciplines.md)
- [Sweep playbooks: MASINT sweep and the disambiguate-via column](../../reference/sweep-playbooks.md)
- [Regional overlays: facilities, permits, and certification registries](../../reference/regional-overlays.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [UN Comtrade trade statistics](https://comtradeplus.un.org/)
