# PESTEL Delta: [MARKET]

## Run Header

~~~
As-of date:        [today]
Prior baseline:    [filename and date]
Window covered:    [date range since prior run]
Scope:             [market, countries at country level]
Sources swept:     [list]
Factors with no material movement: [count of 6]
Stored as:         [filename the next run will diff against]
~~~

> **Stop rule.** If no prior PESTEL exists in session or on file, stop here. Say so, and offer to run a baseline first. Do not run a first pass and label it a delta — a baseline wearing a delta's headers tells the reader everything moved when in fact nothing was compared.

## Materiality Threshold

Movement is material when it crosses a threshold that matters to a **named artifact**. "Interest rates rose" is news. "Rates crossed the level at which our buyers' capex needs board sign-off" is a finding.

## Factor Deltas

Each factor gets exactly one of two entry types.

### Political — [moved / no material movement]

**If moved:**
- **Was:** [prior state] — [prior source, prior date]
- **Now:** [current state] — [current source, current date]
- **Threshold crossed:** [what makes this material]
- **Read:** [labeled Inference]
- **What it changes:** [artifact]

**If not:** *No material movement.* [one line, done]

### Economic — [moved / no material movement]

### Social — [moved / no material movement]

### Technological — [moved / no material movement]

### Environmental — [moved / no material movement]

### Legal — [moved / no material movement]

*Distinguish a regulation **proposed** from **in consultation**, **adopted**, and **in force**. Four states, four timelines, routinely collapsed into "coming."*

## Broken Assumptions (the section that earns the run)

| Prior artifact | The assumption inside it | What is now true | Severity |
|---|---|---|---|
| [sizing model / entry case / pricing corridor / roadmap bet, with its date] | [the macro belief it rests on] | [current state, with source] | [invalidates / weakens / worth noting] |

A macro scan that names no affected artifact has produced background reading.

## New to the Frame

Factors that did not apply last quarter and do now.

| Factor | What changed | Why it now applies | What to watch |
|---|---|---|---|
| [factor] | [the development] | [the threshold it crossed] | [escalation trigger] |

## So What

- **Most consequential movement:** [and the artifact it touches]
- **Nothing changed for:** [the factors that held, named — silence about a factor is indistinguishable from not checking it]

## Assumptions to Validate

1. [The read most likely to be wrong]
2. [Second]
3. [Third]

## Final Step

1. Revisit the artifacts with broken assumptions (Recommended)
2. Add the new factor to the standing monitoring scope
3. Keep the quarterly cadence so the next run is a diff
4. Re-baseline if too much has changed to diff meaningfully

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
