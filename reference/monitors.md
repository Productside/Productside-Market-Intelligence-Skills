# The Diff Layer

The point of a stable schema is that run N+1 is a diff, not a rebuild.
A monitor that re-derives everything each time produces a document
nobody reads twice, because there is no way to see what changed.

Every monitor here shares three things: a run header, a materiality
bar, and a changelog of material shifts only.

---

## The Run Header (every monitor)

~~~
**As-of date:** [today]
**Prior run:** [date, or "first run -- this establishes the baseline"]
**Window covered:** [date range since prior run]
**Scope:** [competitors / factors / pages monitored]
**Sources swept:** [list]
**Runs with no material change:** [count, if applicable]
~~~

State the window explicitly. "Recently" is not a window. A reader has
to know whether silence means nothing happened or nobody looked.

---

## The Materiality Bar

This is what separates a monitor from a newsfeed. Report a change only
if it clears one of these:

- Changes what a salesperson would say in a live deal
- Changes a price, a tier, a packaging boundary, or an eligibility rule
- Changes who the buyer is, or which segment is targeted
- Changes a stated strategy, or removes language previously repeated
- Adds or removes a capability that appears in competitive evaluations
- Establishes commitment where there was only announcement (funding,
  procurement, hiring, permits, contracts)
- Breaks an assumption a prior artifact rests on

Below the bar and therefore not reported: copy tweaks, blog cadence,
new logos on a customer wall, conference attendance, headcount noise
under the baseline, and site redesigns that move the same words.

**"No material change" is a valid and valuable run output.** Say it in
one line and stop. A monitor that always finds something is a monitor
that has stopped filtering.

---

## Changelog Format (shared)

Per subject, per change:

~~~
### [Subject] -- [4 to 8 word change summary]

- **Was:** [prior state, with the prior source and date]
- **Now:** [current state, with the current source and date]
- **Read:** [what it implies, labeled Inference]
- **Commitment level:** [Announced / Funded / Procured / Staffed / Built]
- **Artifact affected:** [battle card / pricing / positioning / roadmap / sizing]
~~~

The was-and-now pairing is the whole trick. It forces you to have
actually held the prior state, which is what keeps a "delta report" from
being a fresh snapshot with the word delta on it.

---

## Update Flags

Close every monitor with a flag table. This is what makes the run
actionable rather than informative.

| Artifact | Flag | Why | Owner |
|---|---|---|---|
| [Battle card: X] | [Update now / Review / Hold] | [the change that triggered it] | [who] |

Three flag levels only. "Update now" means a rep will say something
wrong tomorrow if nobody acts.

---

## Competitive Intel Watch

Scheduled delta against a prior snapshot. Material shifts only.

Sweep: pricing pages -> positioning and homepage messaging -> product
and changelog -> job posting deltas -> funding, filings, and leadership
-> certifications -> notable customer or partner announcements.

Sections: run header -> changelog (material shifts only) -> update flags
-> watchlist for next run -> assumptions to validate.

**Watchlist for next run** is what makes the series compound: the
specific things you would check first next time, and the trigger that
would escalate each. Without it, every run starts from zero.

Cadence: weekly for the SIGINT layer, monthly for a full pass. See the
fusion cadence below.

---

## Pricing and Packaging Tracker

The one monitor where the raw capture matters as much as the read,
because it is a time series.

Per competitor, capture verbatim: tier names, list prices, billing
period, seat or usage units, what is included per tier, add-ons,
minimums, published discounts, free tier or trial terms, enterprise
"contact us" boundaries, and the page URL with a capture date.

Then the delta, using the was/now format.

**Signals worth naming when they appear.** The first two are source
doctrine; the rest are extensions, offered as working reads rather than
canon:

- A tier disappears -> packaging overhaul, usually toward enterprise
- A feature moves up a tier -> monetizing what was previously bait
- Usage pricing added alongside seats -> hedging against seat
  compression
- "Contact us" replacing a published price -> discount flexibility
  wanted, or price increase being tested quietly
- A new floor or minimum -> they are firing the bottom of their market
- Annual discount widening -> cash or retention pressure

Rule: capture verbatim before interpreting. A tracker that only stores
your read of the page cannot answer next quarter's question.

---

## PESTEL Delta Monitor

Quarterly re-scan of macro factors. What moved, what broke, what
entered the frame.

**Stop rule.** A delta needs a baseline. If no prior PESTEL exists in
session or on file, say so and offer to run a baseline PESTEL first
(`pestel-analysis`). Do not run a first pass and label it a delta. A
baseline wearing a delta's headers tells the reader everything moved
when in fact nothing was compared.

Sections: run header -> factor-by-factor delta -> broken assumptions ->
new to the frame -> so what.

Per factor, one of two entries:

- **[Factor]: moved** -- was / now / read / what it changes
- **[Factor]: no material movement** -- one line, done

**Broken assumptions** is the section that earns the run. Which prior
artifact rests on something that is no longer true? Name the artifact.

**New to the frame** catches factors that were not relevant last run
and are now. A regulation entering consultation, a currency moving past
a threshold, a technology becoming table stakes.

---

## Earnings and Executive Signal Refresh

Quarterly diff of one company's strategy language against a prior
profile. Reads what changed in how they talk, which is a leading
indicator of what changes in what they do.

Sections: run header -> shifted signals -> dropped language -> so what.

**Shifted signals:** strategy language, segment emphasis, metric
selection, and the questions executives now deflect versus the ones
they used to answer.

**Dropped language** is the most underused signal in competitive
intelligence. A phrase repeated in four consecutive calls and absent in
the fifth is a decision that has already been made internally. Track
disappearance as carefully as appearance.

Other things worth diffing quarter over quarter: the Risk Factors
section, which metrics they lead with, whether a segment got promoted or
folded, and which analyst question got the longest non-answer.

---

## The Fusion Cadence

The governed rhythm. Not every discipline needs the same clock, because
the sources refresh at different rates.

| Cadence | Run | Time |
|---|---|---|
| Weekly | SIGINT sweep: site diffs, pricing, job posts | 30 minutes |
| Monthly | OSINT + HUMINT digest: review mining, employee sentiment, conference intel | An hour or two |
| Quarterly | FININT + TECHINT deep pass: filings, patents, procurement awards | An afternoon |
| Quarterly | Fusion brief and threat assessment | An hour, on top of the above |
| Annual, plus every sizing refresh | GEOINT/DEMOINT pass | Statistics releases lag; sizing rot is slow but real |
| Event-driven | MASINT alerts, material filings, leadership exits | React within 48 hours |

**Event triggers that override the calendar:** a competitor
announcement, a funding round, an acquisition, a leadership exit, a
pricing change, a lost deal where the competitor did something new, a
regulation entering force.

---

## Scheduling Notes

These runs are built to execute without a human answering questions,
which is what makes them schedulable. Three properties make that safe:

1. **The question budget caps at 3 and then proceeds** on labeled
   assumptions. A scheduled run never blocks waiting for input.
2. **The search plan gate continues unless revised.** Nobody has to
   approve anything.
3. **The schema is stable,** so the run can diff against the stored
   prior output rather than needing context re-supplied.

For a scheduled run, store the output somewhere the next run can read
it, and name that location in the run header. A delta monitor with no
access to its own history is just a snapshot on a timer.

If a scheduled run finds nothing material, its output should be one
line and a date. Resist the urge to justify the run's existence with
volume.
