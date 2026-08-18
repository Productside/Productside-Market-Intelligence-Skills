# Pricing and Packaging Capture: [COMPETITOR SET]

## Run Header

~~~
As-of date:      [today]
Prior capture:   [filename and date, or "none -- this is a BASELINE CAPTURE, not a delta"]
Window:          [interval since prior capture]
Competitors:     [list]
Capture URLs:    [one per competitor]
Runs with no change: [consecutive count]
Stored as:       [filename the next run will diff against]
~~~

## Verbatim Capture — [Competitor]

**Captured from:** [URL] on [date]. Words as the page has them, not paraphrased.

| Tier name | List price | Billing period | Unit | Included | Limits | Add-ons | Minimum | Overage |
|---|---|---|---|---|---|---|---|---|
| [verbatim] | [verbatim] | [verbatim] | [seat / usage / hybrid] | [verbatim] | [verbatim] | [verbatim] | [verbatim] | [verbatim] |

- **Free tier or trial terms:** [verbatim, or "not published"]
- **Published discounts:** [verbatim, e.g. annual billing terms]
- **"Contact us" boundary:** [where published pricing stops]
- **Regional or currency notes:** [if the page varies by geography]

*Fields absent from the page are recorded as "not published" — never inferred.*

*Repeat this block per competitor, with identical fields every run. A schema improved mid-series destroys the series.*

## Delta Against Prior Capture

| Competitor | Field | Was | Now | Interval |
|---|---|---|---|---|
| [name] | [tier / price / limit / inclusion / minimum] | [prior verbatim, prior date] | [current verbatim, current date] | [days] |

**Packaging changes hide in the non-price fields.** A price that holds at $119 while the record limit halves is an increase no headline reports.

## Packaging Signals (only where the pattern appears)

Name a signal only when its pattern is actually present. Attaching an interpretation to every field turns a tracker into a horoscope.

| Signal | Present? | Evidence from the capture | Read |
|---|---|---|---|
| A tier disappeared | | | Packaging overhaul, usually toward enterprise *(source doctrine)* |
| A feature moved up a tier | | | Monetizing what was previously bait *(source doctrine)* |
| Usage pricing added alongside seats | | | Hedging against seat compression *(working read)* |
| "Contact us" replacing a published price | | | Discount flexibility wanted, or an increase tested quietly *(working read)* |
| A new floor or minimum | | | Firing the bottom of the market *(working read)* |
| Annual discount widening | | | Cash or retention pressure *(working read)* |

## Ambiguous Reads

| Change | Explanation A | Explanation B | Disambiguate via |
|---|---|---|---|
| [change] | [reading] | [opposite reading] | [FININT margin language / HUMINT / next capture] |

Do not choose. A pricing change frequently has two explanations pointing opposite ways about a competitor's health.

## Update Flags

| Artifact | Flag | Why | Owner |
|---|---|---|---|
| [Battle card: X] | [Update now / Review / Hold] | [is a card currently quoting a dead price?] | [who] |

## If Nothing Changed

> **No pricing or packaging change this run.** Window: [interval]. Pages captured: [URLs]. Consecutive runs with no change: [count].

One line and stop.

## Final Step

1. Update the battle card and deal desk guidance (Recommended)
2. Run FININT to resolve the ambiguous read
3. Keep the schedule — the series is the asset, not any single capture
4. Increase capture frequency for the competitor that is moving

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
