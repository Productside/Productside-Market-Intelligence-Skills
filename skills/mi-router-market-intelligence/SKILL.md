---
name: mi-router-market-intelligence
description: Instantiate a market or competitor engagement on six variables and route it to the right run. Use when a company or market suddenly matters and you do not yet know which sweep to run.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company or market] [what changed]"
intent: >-
  Turn a vague competitive worry into a scoped engagement with a named decision
  behind it, then send it to the run that answers it. Exists because the most
  expensive error in intelligence work is not a bad sweep, it is a good sweep of
  the wrong thing, and that error is made in the first five minutes.
type: router
theme: market-competitive-intelligence
stage: instantiate
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
  - "Turning a vague competitive worry into a scoped engagement with a named decision"
  - "Choosing between a full sweep, a single discipline, a fusion pass, and a monitor"
  - "Catching a same-name company or a stale acquisition before the run, not after"
scenarios:
  - "A competitor turned up in three lost deals this month and my VP wants to know what is going on"
  - "We have a partner call this afternoon and I know almost nothing about them"
  - "Someone forwarded me a competitor announcement and asked what we should do"
  - "Our battle cards have gone stale and nobody trusts them"
evidence-required:
  - "The company or market that suddenly matters"
  - "The decision this research will change"
  - "Whatever is already known or already collected"
produces:
  - "Completed Instantiate block on the six variables"
  - "A named decision, or a stop"
  - "Routing recommendation with the reference files that run needs"
estimated-time: "5-15 min"
group-size: "1-8"
consumes: []
combine-with:
  - mi-sweep-full-spectrum
  - mi-fuse-all-source
  - mi-watch-competitors
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, Dean Peters"
  - "Regional Source Overlays: EU and MENA"
  - "SCIP Code of Ethics, the industry reference for competitive intelligence practice"
sources:
  - https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "Route a Market Intelligence Run"
  short_description: "Scope the engagement, then pick the sweep"
  brand_color: "#00E874"
  default_prompt: "Use $mi-router-market-intelligence to instantiate this engagement on the six variables, confirm the decision it will change, and route me to the right run without collecting anything yourself."
  allow_implicit_invocation: true
---

# Route a Market Intelligence Run

## Purpose

Act as the desk officer who scopes an engagement before anyone spends an afternoon on it.

The premise this library rests on: the intelligence community solved competitive research decades ago. They do not collect "data." They run collection disciplines, each with its own sources, tradecraft, and blind spots, then fuse them. Product teams should steal the whole playbook.

This skill runs the first five minutes of that playbook. It fills six variables, refuses to proceed without a decision, and routes to the run that answers the question actually being asked. It collects nothing itself.

The motion it opens: **instantiate → search plan → collect → fuse → act → schedule the next diff.**

## When to Use It

Use it when a company or market suddenly matters and being roughly right is not good enough — a competitor surfacing in lost deals, a partner call on the calendar, an announcement someone forwarded with "thoughts?" attached.

Use it especially when you are not sure which run you need. That is the condition it exists for.

Do not use it when:

- **You already know the run.** If you need OSINT on a named company, invoke `mi-collect-osint` directly. Routing a decision you have already made is ceremony.
- **You hold a framework question and its evidence.** The act-layer skills consume fused evidence; they do not need routing to find it.
- **The context lives in the user's head, not the world.** That is facilitation, not investigation. No amount of public collection will surface what only your team knows.
- **The subject is pre-public, pre-product, and pre-press.** Most disciplines return nothing, and the honest output is a short list of what cannot be known yet. Say that instead of routing.

## Input

Require only what a human uniquely holds:

- the company or market that suddenly matters, and which part of it
- what changed, or what prompted the question
- the decision this research will change
- anything already collected

Everything else — legal entity, tickers, ownership, market codes — is publicly discoverable and is the run's job to find, not the user's job to supply.

Anything supplied in the invocation, attachments, prior run output, or earlier conversation counts as context already given. Do not ask for it again.

**Example invocation:** `Use $mi-router-market-intelligence — Cartelane showed up in three lost deals this quarter and my VP wants a read before the QBR.`

## Key Concepts

**The six variables** — `[TARGET]`, `[MARKET]`, `[GEOGRAPHY]`, `[BUYER]`, `[CAPABILITY]`, `[DECISION]`. Fill them once and every discipline downstream becomes specific to this engagement. Leave them blank and the run produces a teaching artifact: correct, generic, and useless to the person holding the calendar invite. `[GEOGRAPHY]` is filled at country level, because it determines which registries, statistics bureaus, and procurement portals apply. "EMEA" is not a geography; it is a sales region wearing a map.

*Violation signal:* A downstream section could be pasted into a brief about a different company without editing.

**The decision gate** — If `[DECISION]` is blank, the run stops. Research without a decision is a hobby. This is the single most useful refusal in the library, and the one users most often want waived: "just get me smart on them" feels like a decision and is not, because nothing in the output can be wrong in a way anyone would notice. Naming the decision is also what lets the run stop collecting — you are done when the answer stops moving the decision.

*Violation signal:* The engagement is described entirely in terms of a company rather than in terms of a choice.

**Collection is not fusion** — Sweeps gather and label; they do not render verdicts. Rating confidence across disciplines is a separate act with its own rules, and merging the two is how a single vivid find sets the confidence level for a whole brief. The route table keeps them separate on purpose: a request to "reconcile what we already have" routes to fusion with no new fieldwork, and a request to "go deep on one channel" routes to a sweep that ends without a verdict.

*Violation signal:* A collection run is asked to conclude whether the threat is real.

**Identity and perimeter** — Legal entity, trading names, ownership status, tickers, subsidiaries, brands, and the same-name companies to exclude. Established before collecting, not during. This is cheap insurance with a brutal failure mode: catching the wrong company at the gate costs one line, and catching it in section eight costs the entire run plus whatever was said out loud in the meantime.

*Violation signal:* The noise filter says "exclude same-name companies" without naming one.

**Relationship framing** — Competitor, prospect, partner, acquirer, vendor, or unknown. The same company researched for a partnership and for a deal defense produces two different hours of work: the partner sweep spends its time on commercial model and dependency risk, the competitive sweep on pricing posture and exposed flank. Getting this wrong produces a thorough brief that answers a question nobody asked.

*Violation signal:* The brief contains a "what we do better" section for a run that was scoped as a partner evaluation.

**Depth as a budget, not an ambition** — Rapid, standard, or deep. Depth is chosen from the calendar, not from the interest of the subject. A rapid pass that lands before the call beats a deep pass that lands after it, and the most common routing failure is promising a research afternoon to someone who has forty minutes.

*Violation signal:* The estimated time exceeds the time until the meeting the run is for.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "I will scope this engagement on six variables and route it to the right run — I will not collect anything myself. Two or three questions, about five minutes. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `Setup Q1/3` — What decision will this research change? Offer three context-aware options plus `Other (specify)`. If the answer is genuinely "none," say so and stop.
2. `Setup Q2/3` — What is your relationship to them: competitor, prospect, partner, acquirer, vendor, or unknown?
3. `Setup Q3/3` — How much time do you have before this needs to be useful?

Skip any question the invocation already answered, and say "I have what I need" rather than spending the budget for its own sake. Never ask for the legal entity, the ticker, the market codes, or anything else a search would return — that is burden-shifting.

In **Context dump** mode, extract the six variables from whatever was pasted, show a `found / inferred / still missing` account, and ask only about gaps. In **Best guess** mode, fill the variables yourself, name each assumption, and route. On total silence: standard depth, competitor framing, general strategic briefing. Proceed.

## What It Produces

Complete the [Engagement Instantiation](template.md):

- the six variables, filled, with `[GEOGRAPHY]` at country level
- identity and perimeter, including the same-name companies to exclude by name
- the named decision, or an explicit stop
- a routing recommendation naming the skill, the depth, and the reference files that run needs
- the regional overlay to load, when `[GEOGRAPHY]` is outside the US

This skill produces no signals, no findings, and no verdicts. If it has started collecting, it has stopped routing.

## Workflow

1. **State web access in one line.** With access, the routed run researches live. Without it, say so plainly — the routed run will work from training data, mark everything Assumption with its knowledge vintage, and invent nothing.
2. **Fill the six variables.** Use what was supplied, infer what is inferable, ask only within the budget.
3. **Check the decision.** If `[DECISION]` is blank after the budget is spent, stop and say why. Offer to help name one; do not proceed without it.
4. **Establish identity and perimeter.** Legal entity, ownership, tickers, brands, subsidiaries, and the same-name confusions — named, not gestured at.
5. **Load the regional overlay if needed.** `[GEOGRAPHY]` outside the US means `reference/regional-overlays.md` before any collecting.
6. **Route from the table below.** Name the skill, the depth, and the reference files.
7. **Say what the run will not answer.** Every route has a blind spot. Naming it now prevents the brief from being read as more complete than it is.
8. **Hand off and stop.** Do not begin the run you just routed unless the user asks.

### Route Table

| The ask | The run | Skill | Read |
|---|---|---|---|
| "Get me smart on this company by 3pm" | Full-spectrum sweep, fused, call-ready brief | `mi-sweep-full-spectrum` | `sweep-playbooks.md`, `fusion.md`, `output-schemas.md` |
| "Go deep on one channel" | Single-discipline collection sweep | `mi-collect-osint` / `-finint` / `-geoint-demoint` / `-techint` / `-humint` / `-sigint` / `-masint` | `disciplines.md`, `sweep-playbooks.md` |
| "Map this market before we size it" | Landscape scan, then competitor snapshots | `mi-scan-market-landscape`, then `mi-snapshot-competitors` | `frameworks.md` |
| "What do customers actually complain about?" | Review and forum mining with quoted evidence | `mi-mine-voice-of-customer` | `frameworks.md` |
| "Is their announced move real?" | Commitment check: OSINT claim against FININT, HUMINT, MASINT | `mi-fuse-all-source` | `fusion.md`, `disciplines.md` |
| "Reconcile what we already collected" | All-source fusion, no new fieldwork | `mi-fuse-all-source` | `fusion.md` |
| "What changed since last time?" | Watch, pricing tracker, PESTEL delta, earnings refresh | `mi-watch-competitors`, `mi-monitor-pricing-packaging`, `mi-monitor-pestel-delta`, `mi-refresh-earnings-signals` | `monitors.md` |
| "Arm the field" | Battle card from cited evidence | `mi-build-battle-card` | `frameworks.md` |
| "Size it" | GEOINT/DEMOINT denominator, FININT capture rate | `mi-size-tam-sam-som` | `disciplines.md`, `frameworks.md` |
| "Read the industry or the position" | Fuse first, then the framework | `mi-analyze-five-forces`, `mi-analyze-swot`, `mi-analyze-ansoff` | `fusion.md`, `frameworks.md` |
| "Set up the rhythm" | Fusion cadence, scheduled diffs | `mi-watch-competitors` | `monitors.md` |

When two routes fit, prefer the narrower one and say what the wider one would add. A full-spectrum sweep run because nobody wanted to choose is an hour spent proving that seven channels exist.

## Human Decision Gate

Present the instantiated engagement and the recommended route. Highlight:

- any variable filled by inference rather than by the user
- the blind spot of the recommended route
- whether the depth fits the time available
- whether `[GEOGRAPHY]` requires an overlay that has not been built yet

Use an Adaptive Decision Ladder: `Run the recommended route`, `Run a narrower single-discipline sweep instead`, `Fix a variable first — the framing is wrong`, or `Other (specify)`. Say in one sentence what each choice buys and what it gives up.

Stop here. Do not run the route you recommended unless asked.

## Evidence and Attribution Rules

- Label every variable **Fact** (the user said it, or a source documents it), **Inference** (read from evidence, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** legal entity names, tickers, ownership structures, subsidiary relationships, market codes, or founding dates. If identity cannot be established, say so — a sweep pointed at the wrong entity is worse than no sweep, because it is confidently wrong.
- A company's own description of itself is a claim, not a fact about the market.
- Never fabricate a citation. In a briefing this is worse than an admitted gap, because the user will repeat it out loud.

## Common Failure Modes

- Routing without a decision, because "get smart on them" sounded like one
- Filling `[GEOGRAPHY]` with a sales region instead of a country
- Skipping identity and perimeter because the company name seemed unambiguous
- Recommending a full-spectrum sweep as a default, which is how the router becomes decoration
- Asking the user for facts the routed run will discover in ninety seconds
- Starting to collect during the routing conversation, so the scope is set by whatever turned up first
- Routing a partner evaluation to a competitive framing because the library's center of gravity is competitive
- Promising deep when the calendar says rapid

## Assets and Examples

- [Engagement Instantiation template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Run the recommended route now (Recommended)
2. Narrow to a single discipline first
3. Set this up as a scheduled series so run N+1 is a diff
4. Reframe the engagement — the decision is not the one we named

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines](../../reference/disciplines.md)
- [Sweep playbooks](../../reference/sweep-playbooks.md)
- [Guided context capture](../../reference/guided-context-capture.md)
- [Competitive research compendium and runnable prompts](https://github.com/deanpeters/product-manager-prompts/tree/main/market-intelligence)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
