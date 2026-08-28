---
name: mi-collect-sigint
description: Diff what a company changed on the public internet — pricing pages, messaging, docs, SSL certs, app metadata, SEM terms. Use for the freshest competitive layer, the one that keeps battle cards alive.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company] [prior capture date]"
intent: >-
  Run the wiretap you are allowed to have. Companies broadcast constantly through
  what they change on the public internet, and most competitors never listen.
  Exists because the SIGINT layer is what keeps a battle card from going stale,
  and because a change without a before-state is not a change.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: SIGINT
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
  - "Catching a launch during staging, weeks before it is announced"
  - "Detecting a packaging overhaul the moment a pricing tier disappears"
  - "Refreshing the layer of a battle card that decays fastest"
scenarios:
  - "Their pricing page changed and nobody can remember what it said before"
  - "A new subdomain certificate appeared with a capability name on it"
  - "They started bidding on our brand terms"
  - "Their homepage messaging has been rewritten twice this quarter"
evidence-required:
  - "The target company and its public web properties"
  - "A prior capture or archive snapshot to diff against"
  - "The decision this collection feeds"
produces:
  - "Fusion-ready signal inventory with a mandatory before-to-after column"
  - "Verbatim captures of pricing and messaging for the next diff"
  - "Ranked inference chains with staleness horizons"
  - "Baseline captures where no prior state exists"
estimated-time: "20-45 min"
group-size: "1-3"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
  - mi-monitor-pricing-packaging
  - mi-watch-competitors
source-basis:
  - "Competitive Research on Steroids: A Category Compendium, SIGINT discipline"
  - "Public web archives and certificate transparency logs as primary sources"
sources:
  - https://github.com/Productside/Productside-Market-Intelligence-Skills
  - https://crt.sh/
interface:
  display_name: "SIGINT Collection Sweep"
  short_description: "Diff what they changed in public"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-sigint to diff this company's pricing, messaging, docs, certificates, app metadata, and search terms against their prior state, capture verbatim for the next run, and stop before rating confidence."
  allow_implicit_invocation: true
---

# SIGINT Collection Sweep

## Purpose

The wiretap you are allowed to have.

Companies broadcast constantly through what they change on the public internet — a tier removed from a pricing page, a hero paragraph rewritten, an SSL certificate issued for a subdomain that does not exist yet, an app listing quietly gaining a keyword. Most competitors never listen. The signals are free, they are legal, and they arrive weeks ahead of the announcement.

This is the freshest layer in competitive intelligence and therefore the one that decays fastest. It is what keeps a battle card from going stale, and it is the layer a card is wrong about first.

The sweep produces a labeled inventory, not a verdict. **Collection is not fusion.**

## When to Use It

Use it when something changed and nobody can say what it was before. Use it weekly, on a schedule, as the cheapest recurring intelligence available — thirty minutes buys the pricing, messaging, and posting layer. Use it when a launch is suspected and you want to know whether it is staged.

Do not use it when:

- **You need the pricing time series rather than this week's diff.** That is `mi-monitor-pricing-packaging`, which stores verbatim captures so next quarter's question is answerable.
- **You want a full multi-competitor delta report.** That is `mi-watch-competitors`, which applies a materiality bar across a watchlist.
- **No prior state exists anywhere.** Then this run is a *baseline capture*, not a diff, and it must say so — a first snapshot presented as a change report tells the reader everything moved.
- **The question is what they are building.** SIGINT sees the launch being wheeled out; TECHINT sees what is inside it.

## Input

Require:

- `[TARGET]` and its public web properties, including docs and status pages
- a prior capture, archive snapshot, or stored run to diff against
- the `[DECISION]` this feeds

Anything supplied in the invocation, attachments, a prior run, or earlier conversation counts as context already given. Never ask the user what a competitor's pricing page used to say; recovering that is the run.

**Example invocation:** `Use $mi-collect-sigint on Cartelane, diffing against our capture from 2026-05-14.`

## Key Concepts

**Before-to-after is mandatory** — A change without a before-state is an observation, not a diff, and the inventory has a required column for it. "Their pricing page shows three tiers" is a fact about today. "Their pricing page went from four tiers to three, and the removed tier was the entry point" is intelligence. If the prior state cannot be established, say so and log the row as a **baseline capture** rather than a change.

*Violation signal:* A row describes the current state of a page with nothing in the prior-state column, and is nonetheless read as a movement.

**Verbatim before interpretation** — Capture the actual words, tier names, prices, units, and limits before writing what they mean. A tracker that stores only your read of a page cannot answer next quarter's question, and next quarter's question is always more specific than this quarter's read. This is the discipline where note-taking discipline *is* the tradecraft.

*Violation signal:* The record says "pricing simplified" and nowhere preserves what the tiers were called or cost.

**Staging leaks before launch** — Certificate transparency logs are public. A new certificate for a capability-shaped subdomain is launch staging, often weeks ahead of any announcement, and it is one of the earliest signals available anywhere in this library. Its counterpart is API and documentation changes, which show the same launch from the inside.

*Violation signal:* A launch is reported from the press release when the certificate was public a month earlier.

**Every signal has a staleness horizon** — SIGINT signals expire. A pricing capture is authoritative for weeks; a messaging diff for a quarter; a certificate observation is a point event that either matures into a launch or does not. State the horizon with the signal, because a battle card built on this layer needs to know which lines rot first.

*Violation signal:* A SIGINT finding is written into a durable artifact with no date-stamp and no decay note.

**Attention is a signal too** — Sudden search-engine bidding on your brand terms means they now consider you the threat. Case-study pages shifting toward a new vertical or geography is a segment push. App-store keyword changes are positioning tests run in public. These are cheap to check and almost never checked.

*Violation signal:* The sweep covers the target's own pages and never checks what they are doing in the spaces around your brand.

**Messaging churn is uncertainty** — A homepage rewritten twice in a quarter is a company that has not settled its positioning. That is an opening, and it is visible only through archive diffs. A stable message repeated for a year is defended ground and should be left alone.

*Violation signal:* Messaging is reported as "updated" without saying how many times, or from what, or over what period.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Open with: "This is a SIGINT sweep — pricing, messaging, docs, certificates, app metadata, search terms, posting deltas — ending in a fusion-ready inventory where every row carries a before-to-after. Twenty to forty-five minutes. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**."

In Guided mode, ask one at a time, hard cap of three:

1. `SIGINT Setup Q1/3` — Which company, and is there a prior capture or stored run I should diff against?
2. `SIGINT Setup Q2/3` — What decision does this feed: a battle card refresh, a pricing response, or a launch-timing read?
3. `SIGINT Setup Q3/3` — Which of your own brand terms should I check their search bidding against?

In **Context dump** mode, treat a pasted prior capture as the baseline and diff against it directly. In **Best guess** mode, use web archive snapshots as the prior state, diff against the most recent one older than ninety days, and name the snapshot dates as assumptions. On silence: archive-based baseline, ninety-day comparison, Just Enough Mode. Proceed.

## What It Produces

Complete the [SIGINT Collection Sweep](template.md), written to the single-discipline schema in `reference/output-schemas.md`:

- signal inventory with a **mandatory before-to-after column**, plus URL, date, and F/I/A label
- verbatim captures of pricing and messaging, stored for the next run
- ranked inference chains with staleness horizons
- baseline captures, clearly separated from changes
- watch items, collection gaps, assumptions to validate, Final Step block

## Workflow

1. **State web access in one line.** Without it this discipline barely functions — say so plainly, and do not reconstruct a pricing page from memory. Fabricated prices reach customers.
2. **Show the search plan.** Sweep order, date window, noise filter — including how you will distinguish a real change from a site redesign that moves the same words. Continue unless revised.
3. **Establish the prior state first.** Stored capture, archive snapshot, or nothing. If nothing, declare the run a baseline capture in the header, not in a footnote.
4. **Sweep in this fixed order.** Pricing page against its last snapshot → site and messaging diffs via archive → documentation and status-page history → new certificates and subdomains → app-store metadata and version notes → search and paid-term movement, including bids on your brand → job posting deltas since the last observable window → certifications listed.
5. **Capture verbatim before interpreting.** Tier names, prices, billing periods, units, inclusions, limits, add-ons, minimums, trial terms, and the page URL with a capture date.
6. **Log every signal with its before-to-after.** One observation per row.
7. **Run the discipline's inference chains explicitly.** New capability-shaped subdomain certificate → launch staging, often weeks ahead. Pricing tier removed → packaging overhaul, usually toward enterprise. Bidding on your brand terms → they consider you the threat. Case-study pattern shift → segment push. Messaging A/B visible in archive diffs → positioning uncertainty, so hit the wound.
8. **Attach a staleness horizon to every chain.**
9. **Report what returned nothing** in one line, naming what was swept. A site with no archive coverage is a real constraint, not a failure.
10. **Store the captures** under the naming convention so the next run is a diff, then stop before rating confidence.

## Human Decision Gate

Present the inventory and the captures. Highlight:

- which rows are genuine changes and which are baseline captures with no prior state
- what the shortest staleness horizon is, because it dates the whole run
- whether a certificate or docs change suggests a launch inside the next quarter
- which stored artifact the next run should diff against

Use an Adaptive Decision Ladder: `Hand this to fusion`, `Promote the pricing capture into a tracked time series`, `Set this up as a weekly watch`, or `Other (specify)`.

## Evidence and Attribution Rules

- Label every line **Fact** (observed on a live or archived page), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated).
- **Do not invent:** prices, tier names, feature inclusions, usage limits, certificate issue dates, subdomain names, app version numbers, keyword rankings, or outage dates. A fabricated competitor price will be quoted to a customer within a week.
- An archive snapshot is evidence of what a page said on the snapshot date, not of what it said continuously. Gaps in archive coverage are gaps in evidence.
- Distinguish a change from a redesign that relocated identical wording.
- Every capture carries a URL and a capture date.
- Stay inside the guardrails: publicly served pages and public logs only. Do not scrape in violation of terms you agreed to, and do not access anything behind an authentication boundary.

## Common Failure Modes

- Reporting a current state as a change because the prior state was never established
- Storing your interpretation instead of the verbatim capture
- Missing a launch that was visible in certificate logs a month earlier
- Reading a site redesign as a messaging shift
- Omitting the staleness horizon, so a decaying signal enters a durable artifact
- Never checking whether they bid on your brand terms
- Treating a single archive snapshot as continuous coverage
- Rating the threat, which is fusion's job
- Running this once instead of weekly, which is where its value actually lives

## Assets and Examples

- [SIGINT Collection Sweep template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Final Step

```text
## Final Step

1. Hand this to fusion (Recommended)
2. Promote the pricing capture into a tracked time series
3. Set this up as a weekly watch so the next run is a diff
4. Push the changed lines into the battle card that just went stale

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
```

## Sources

- [The disciplines: SIGINT](../../reference/disciplines.md)
- [Sweep playbooks: SIGINT sweep and the before-to-after column](../../reference/sweep-playbooks.md)
- [Monitors: the diff layer](../../reference/monitors.md)
- [Competitive research compendium and runnable prompts](https://github.com/Productside/Productside-Market-Intelligence-Skills)
- [Certificate transparency search](https://crt.sh/)
