---
name: mi-collect-humint
description: Read a company through its people — hiring surges, leadership moves, departures, employee sentiment — and end by generating the win/loss questions only your own team can answer.
license: CC-BY-NC-ND-4.0
argument-hint: "[target company] [suspected capability]"
intent: >-
  Run the sports-scout discipline on one company. Organizations announce strategy
  through job boards long before press releases. Exists because a job posting is a
  roadmap with a salary band, and because public people-signals infer why deals
  move while only win/loss interviews know.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: HUMINT
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
  - "Testing whether an announced or suspected capability is actually staffed"
  - "Spotting a market entry through regional roles before any announcement"
  - "Finding the window created by a competitor's internal reorganization"
scenarios:
  - "They are hiring thirty people into a specialty they never staffed before"
  - "Their VP of Product left six months after the strategy announcement"
  - "Employee reviews suddenly all mention a reorg"
  - "Roles appeared for a country they have never sold into"
evidence-required:
  - "The target company and the capability in question"
  - "A baseline for what their normal hiring looks like"
  - "Whether win/loss interviews have been run this cycle"
produces:
  - "Fusion-ready signal inventory with counts against a stated baseline"
  - "Stated-strategy-versus-staffing read"
  - "Three to five win/loss questions tied to specific signals"
  - "The win/loss gap flag for fusion"
estimated-time: "30-60 min"
group-size: "1-4"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
  - mi-collect-techint
  - mi-build-battle-card
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, HUMINT discipline"
  - "SCIP Code of Ethics, which draws the line this discipline must not cross"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://www.scip.org/page/CodeofEthics
interface:
  display_name: "HUMINT Collection Sweep"
  short_description: "Read the strategy off the job board"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-humint to sweep hiring, leadership moves, departures, and sentiment on this company, count postings against a stated baseline, and end by generating the win/loss questions only our own team can answer."
  allow_implicit_invocation: true
---

# HUMINT Collection Sweep

## Purpose

Run the sports scout. People are the tell.

Organizations announce strategy through job boards long before press releases. A hiring surge in one specialty is a capability being built, not a feature being added. A regional specialist role is a market entry that has not been announced. A senior departure six months after a strategy launch says the strategy is in trouble. All of it is public, all of it is free, and almost none of it is read systematically.

This discipline has a boundary it must respect and a debt it must pay. The boundary: everything here is public observation, never pretexting or soliciting confidential information. The debt: **public HUMINT infers why deals move; only your team's interviews know.** So this sweep ends by generating the questions for the next win/loss round, and by raising a flag that tells fusion how much to trust it.

The sweep produces a labeled inventory, not a verdict. **Collection is not fusion.**

## When to Use It

Use it to test whether a capability is staffed. Use it when a competitor's internal turbulence might be your window, when regional roles hint at an expansion, or when a TECHINT cluster needs its strongest corroborator — a paper or patent cluster next to a hiring surge in the same specialty is one of the most reliable pairs available.

Do not use it when:

- **You want to know why deals were lost.** That is win/loss interviewing, which this sweep prepares for rather than replaces. No amount of public signal substitutes for asking the buyer.
- **The company is small enough that headcount noise swamps signal.** Four postings at a forty-person company means nothing without a baseline, and often no baseline exists.
- **You need the technical shape of what they are building.** That is TECHINT. HUMINT tells you it is staffed; TECHINT tells you what it is.
- **The temptation is to contact their employees.** That crosses the line this discipline draws. Observe what is published; do not elicit what is not.

## Input

Require:

- `[TARGET]`, and the `[CAPABILITY]` in question if one is suspected
- some sense of their normal — prior headcount, prior posting volume, anything that makes a count mean something
- whether win/loss interviews have been run this cycle, which is the one thing a search cannot tell you

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given. Never ask the user for headcounts or open roles; discovering those is the entire run, and asking for them teaches the user they should have known.

**Example invocation:** `Use $mi-collect-humint on Cartelane. Suspected capability: native ERP integration. Our last win/loss round was eight months ago.`

## Key Concepts

**Counts need a baseline** — Thirty postings is meaningless. Thirty postings against a trailing baseline of four is a program. A count without a denominator is the most common way this discipline manufactures alarm, and the baseline is usually available: the same company's posting volume a year earlier, or in an adjacent function today. If no baseline can be established, say so and label the count an observation rather than a surge.

*Violation signal:* A posting count appears with no comparison period and is described as a "surge."

**Stated strategy versus staffing** — The signature output. What leadership says they are doing, set against who they are actually hiring. A company that announced a platform strategy and is hiring only account executives has announced a sales motion. A company hiring thirty infrastructure engineers while saying nothing has a strategy it has not finished packaging. When words and staffing disagree, the payroll is the truthful one.

*Violation signal:* The sweep reports hiring activity without ever setting it against what the company claims to be doing.

**A job posting is a roadmap with a salary band** — Postings name technologies, integrations, compliance regimes, and customer segments, because they have to attract someone who can actually do the work. That specificity is the intelligence. A posting requiring experience with a named ERP is a confirmed integration target, stated more plainly than any press release would.

*Violation signal:* Postings are counted but never read, so the inventory has numbers and no technology names.

**Departure timing is the read, not the departure** — Executives leave constantly and most of it is noise. A senior product or technical leader leaving *within six months of a strategy announcement* is a different signal, because it dates the internal disagreement. Likewise, tenure concentration matters more than any single exit: three of five leaders departing in two quarters is an organization in trouble regardless of the stated reasons.

*Violation signal:* A departure is reported as a threat or an opportunity with no reference to what it followed.

**Sentiment is directional, never diagnostic** — Employee review platforms skew toward the recently departed and the currently frustrated. Themes mentioning pivot, reorg, or leadership churn are worth logging because they estimate *duration of distraction*, which is your window. They are not evidence about product quality, roadmap, or financial health.

*Violation signal:* An employee review is cited as evidence about the product rather than about the organization.

**The win/loss debt** — Every signal in this discipline is an inference about why deals move, made from outside. Your own interviews are the ground truth, and where they disagree with the sweep, **the interviews win**. A build-signal or org-instability story rated actionable without current interviews is how a roadmap gets reordered by a job posting. This is why the sweep ends with a gap flag rather than a conclusion.

*Violation signal:* The sweep concludes why deals are being lost.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a HUMINT sweep — hiring, leadership, departures, sentiment — ending in a fusion-ready inventory, win/loss questions for your next interview round, and a flag telling fusion how much to trust it. Thirty to sixty minutes. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `HUMINT Setup Q1/3` — Which company, and what capability do you suspect they are staffing?
2. `HUMINT Setup Q2/3` — Have win/loss or churned-customer interviews been run this cycle? This changes how much weight fusion may put on everything below, and nothing public tells me the answer.
3. `HUMINT Setup Q3/3` — What decision does this feed: a roadmap bet, a battle card, or a threat read?

Never ask for headcount or open roles. In **Context dump** mode, extract supplied signals into the inventory, establish a baseline from whatever is available, and ask only about gaps. In **Best guess** mode, assume a twelve-month window, use the prior year's posting volume as baseline where discoverable, and name each assumption. On silence: twelve-month window, win/loss assumed unverified, flag raised. Proceed.

## What It Produces

Complete the [HUMINT Collection Sweep](template.md):

- signal inventory with counts stated against a named baseline, plus URLs, dates, and F/I/A labels
- stated-strategy-versus-staffing read
- ranked inference chains, capped at five
- **three to five win/loss questions**, each tied to a specific signal this sweep collected
- **the gap flag for fusion**, stated verbatim
- watch items, collection gaps, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it, say so, run from training data, mark everything Assumption with its vintage, and invent no counts or names.
2. **Show the search plan.** Sweep order, date window, noise filter — including how you will avoid counting the same role reposted three times as three roles. Continue unless revised.
3. **Sweep in this fixed order.** Leadership roster and prior playbooks → open roles by function and geography, counted against a baseline → departures and tenure concentration → employee sentiment themes → public statements in interviews, talks, and podcasts → your own win/loss and churn debriefs if any exist.
4. **Establish the baseline before counting anything.** Say what normal looks like and where that number came from.
5. **Read the postings, do not just count them.** Extract named technologies, integrations, compliance regimes, regions, and customer segments.
6. **Log every signal immediately** with source URL, date, and F/I/A label. One observation per row.
7. **Run the discipline's inference chains explicitly.** Hiring surge in one specialty → building a capability, not a feature. Regional specialist roles → expansion pre-announcement. Named technologies → confirmed stack and integration targets. Senior exits within six months of a strategy announcement → the strategy is in trouble. Your own alumni landing there → assume they know your playbook. Sentiment mentioning pivot or reorg → two quarters of internal distraction, which is your window.
8. **Write the stated-strategy-versus-staffing read.**
9. **Generate three to five win/loss questions,** each tied to a specific signal collected here. This is a required output, not an optional flourish.
10. **Raise the gap flag** in the exact form below, then stop before rating confidence.

> **Gap flag for fusion:** win/loss unverified as of this run. Weight org-instability and build-signal stories accordingly.

If interviews *have* been run this cycle, say so instead — and note that where the interviews and this sweep disagree, the interviews win.

## Human Decision Gate

Present the inventory and the staffing read. Highlight:

- which counts rest on a real baseline and which do not
- which postings named technologies, because those are the hardest signals here
- whether win/loss is current, and what that caps
- that a build signal alone cannot move a roadmap

Use an Adaptive Decision Ladder: `Hand this to fusion with the flag attached`, `Pair it with TECHINT on the same specialty`, `Take the win/loss questions into the next interview round`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every line **Fact** (a posting, roster, filing, or published statement), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** headcounts, posting counts, employee names, titles, tenure dates, compensation figures, or quotes from reviews, interviews, or podcasts. A fabricated quote attributed to a named person is the most damaging output in this library.
- Reposted roles are one role. Say how you deduplicated.
- Employee sentiment is evidence about an organization, never about a product.
- Never contact, elicit from, or pretext an employee of the target. Observe what is published. If you would be uncomfortable explaining the method on stage at their user conference, do not use it.
- Do not solicit NDA-protected information, and do not hire someone to extract a former employer's material.

## Common Failure Modes

- Reporting a count with no baseline and calling it a surge
- Counting one reposted role three times
- Reading postings for volume and never for the technologies they name
- Treating any executive departure as a signal
- Citing Glassdoor as evidence about product quality
- Concluding why deals are being lost, which only interviews can establish
- Omitting the gap flag, which lets fusion over-rate everything here
- Skipping the win/loss questions because the inventory felt complete
- Crossing the line into elicitation because a public profile made it easy

## Assets and Examples

- [HUMINT Collection Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Hand this to fusion with the win/loss flag attached (Recommended)
2. Pair it with a TECHINT sweep on the same specialty
3. Schedule a monthly HUMINT digest so the next run is a diff
4. Take the win/loss questions into the next interview round

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: HUMINT](../../reference/disciplines.md)
- [Sweep playbooks: HUMINT sweep and the win/loss requirement](../../reference/sweep-playbooks.md)
- [Fusion: win/loss weighting](../../reference/fusion.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [SCIP Code of Ethics](https://www.scip.org/page/CodeofEthics)
