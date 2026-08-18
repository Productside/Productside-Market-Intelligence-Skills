# SIGINT Collection: [TARGET]

**As-of date:** [today]
**Decision supported:** [what this changes]
**Prior capture:** [date and filename, or "none — this run is a BASELINE CAPTURE, not a diff"]
**Window covered:** [date range between captures]
**Web access:** [yes / no — without it this discipline barely functions; say so rather than reconstructing pages from memory]

## Search Plan

- **Sweep order:** pricing page → site and messaging diffs via archive → docs and status-page history → new certificates and subdomains → app-store metadata → search and paid-term movement including bids on our brand → job posting deltas → certifications
- **Date window:** [range]
- **Noise filter:** [how a real change is distinguished from a redesign that moved identical wording; which archive snapshot dates are being used]

## 1. Signal Inventory (fusion-ready)

Every row carries a before-to-after. A change without a before-state is an observation, not a diff.

| Signal | Before | After | Source (URL, capture date) | Label | Staleness | Feeds |
|---|---|---|---|---|---|---|
| [What changed] | [prior state, with prior source and date] | [current state] | [URL, date] | [F/I/A] | [weeks / a quarter / point event] | [Battle card / Pricing / Positioning / ...] |

## 2. Baseline Captures (no prior state available)

Kept separate from changes on purpose. These are not movements; they are the first reading.

| Item | Current state | Source (URL, capture date) | Why no prior state |
|---|---|---|---|
| [item] | [verbatim] | [URL, date] | [no archive coverage / page is new / first run] |

## 3. Verbatim Capture — Pricing and Packaging

Capture before interpreting. A tracker that stores only your read cannot answer next quarter's question.

| Tier name | List price | Billing period | Unit | Included | Limits | Add-ons | Minimum |
|---|---|---|---|---|---|---|---|
| [verbatim] | [verbatim] | [verbatim] | [seat / usage / other] | [verbatim] | [verbatim] | [verbatim] | [verbatim] |

- **Free tier or trial terms:** [verbatim]
- **"Contact us" boundary:** [where published pricing stops]
- **Page URL and capture date:** [URL, date]

## 4. Verbatim Capture — Messaging

| Surface | Current wording | Prior wording | Rewrites in window |
|---|---|---|---|
| Homepage hero | [verbatim] | [verbatim, with snapshot date] | [count] |
| Category or positioning line | [verbatim] | [verbatim] | [count] |

Two rewrites in a quarter is positioning uncertainty. A line unchanged for a year is defended ground.

## 5. Strongest Inference Chains (max 5, ranked)

1. **[Signal cluster]** → [inference, labeled] → [artifact it should change, and the move] — *stale after: [horizon]*
2. …

## 6. Attention Signals

- **Bidding on our brand terms:** [yes, which terms, since when / no / not checkable]
- **Case-study pattern shift:** [new vertical or geography appearing]
- **App-store keyword changes:** [before → after]

## 7. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 8. Collection Gaps and Handoffs

> **No signal found.** [Channel] returned nothing on [what was sought]. Sources swept: [list]. What the absence itself suggests: [read]. What would close it: [the specific source].

- **Handoffs:** pricing capture → `mi-monitor-pricing-packaging`; multi-competitor delta → `mi-watch-competitors`; everything → `mi-fuse-all-source`

## Storage

Stored as `[target]-sigint-[YYYY-MM-DD].md`. The next run diffs against this file. A delta report that cannot name what it diffed against is a snapshot with ambition.

## Assumptions to Validate

1. [The assumption that most changes the read if wrong]
2. [Second]
3. [Third]

## Final Step

1. Hand this to fusion (Recommended)
2. Promote the pricing capture into a tracked time series
3. Set this up as a weekly watch so the next run is a diff
4. Push the changed lines into the battle card that just went stale

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
