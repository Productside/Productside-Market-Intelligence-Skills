# Output Schemas

These schemas are load-bearing. They are what makes run N+1 a diff
instead of a rebuild, which is what makes scheduled runs worth
scheduling.

Do not improve them mid-series. If a schema must change, say so in the
run header and note which sections are no longer comparable.

Conventions: ASCII only, no emojis. `F/I/A` means Fact / Inference /
Assumption. Every source is a real, checkable URL with a date.

---

## 1. Signal Inventory (fusion-ready, every collection sweep)

The atomic unit. Every sweep emits this, which is what lets any
combination of sweeps stack in fusion.

~~~
| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [What it implies] | [Battle card / Positioning / Sizing / Roadmap / ...] |
~~~

For a multi-discipline run, add a Discipline column between Signal and
Source.

**Per-discipline required column.** Four disciplines add one mandatory
column, and each column exists to enforce a rule that the discipline
fails without:

| Discipline | Added column | The rule it enforces |
|---|---|---|
| TECHINT | **Lead time** | Date every signal and state its typical lead time, so the roadmap implication carries a clock, not just a direction. |
| MASINT | **Disambiguate via** | Name the discipline that would resolve the anomaly. A MASINT signal without a disambiguation path is a Rorschach test, not intelligence. |
| SIGINT | **Before -> After** | A change without a before-state is an observation, not a diff. |
| GEOINT/DEMOINT | **Vintage** | Name the statistical vintage of every dataset and flag anything older than the decision's horizon. Statistics releases lag; sizing rot is slow but real. |

Rules: one observation per row. If a row needs the word "and," it is two
rows. A signal you cannot source is an Assumption regardless of how
plausible it reads.

---

## 2. Single-Discipline Collection Sweep

~~~
# [DISCIPLINE] Collection: [TARGET]

**As-of date:** | **Decision supported:** | **Prior sweep:** [date or "first run"]

## 1. Signal Inventory (fusion-ready)
[the table above]

## 2. Strongest Inference Chains (max 5, ranked)
- [Signal cluster] -> [inference, labeled] -> [artifact it should change, and the move]

## 3. [Discipline signature section]
[OSINT: say vs said-about gap. FININT: money vs message. TECHINT:
built vs shipped. HUMINT: stated strategy vs staffing. GEOINT: the
denominator. SIGINT: the freshest layer. MASINT: anomalies.]

## 4. Watch Items (single signals, logged only)
- [Signal] -- [what would escalate it]

## 5. Collection Gaps and Handoffs
- [Uncovered source type] -- [why it was out of reach this run]
- Deep dives: [where to go next]

### Assumptions to Validate
- [1] / [2] / [3]

## Final Step
[exactly 4 numbered options]
~~~

---

## 3. Full-Spectrum Company Sweep

~~~
# Full-Spectrum Company Sweep: [TARGET]

**As-of date:** | **Prepared for:** [the conversation] | **Depth:** [rapid / standard / deep] | **Relationship:** [competitor / prospect / partner / acquirer / vendor]

## 0. Identity and Perimeter
[legal entity, HQ, ownership status, tickers, founding year, brands and
subsidiaries, same-name confusions to avoid]

## 1. OSINT -- The Public Record
[positioning in their own words / what customers and analysts say /
say vs said-about gap / recent announcements, labeled intent]
| Signal | Source (URL, date) | Label |

## 2. FININT -- Money and Commitment
[financial posture / funding and ownership / pricing and packaging /
spend signals]
| Signal | Source (URL, date) | Label |

## 3. TECHINT -- What They Have Actually Built
[product surface / release cadence and deprecations / patents and
publications / architecture and dependency signals]
| Signal | Source (URL, date) | Label |

## 4. HUMINT -- People and Intent
[leadership and prior playbooks / hiring signals / departures and
tenure / public statements]
| Signal | Source (URL, date) | Label |

## 5. GEOINT / DEMOINT -- Terrain and Population
[footprint / market and segment coverage / customer firmographics /
expansion and retreat]
| Signal | Source (URL, date) | Label |

## 6. SIGINT -- Emissions and Digital Exhaust
[web and product telemetry / job posting deltas / certifications /
outages and incidents]
| Signal | Source (URL, date) | Label |

## 7. MASINT -- Measurable Signatures
[scale proxies / trend direction with window stated / anomalies with
candidate explanations]
| Signal | Source (URL, date) | Label |

## 8. Fusion -- Confidence Stacking
| # | Story | Disciplines supporting | Confidence | Commitment | So what |
[cap at 7 stories in standard depth]

### Contradictions Worth Naming
- [Claim from one discipline] versus [evidence from another] -- and
  which one the money supports

## 9. The Call-Ready Brief
[see schema 4 below]

## 10. Collection Gaps
- Disciplines that returned little or nothing: [list] -- and what the
  absence itself suggests
- Questions this sweep could not answer: [list]
- What would close each gap: [the specific source or deep sweep]

### Assumptions to Validate
- [The one that most changes the brief if wrong] / [second] / [third]

## Final Step
[exactly 4 numbered options]
~~~

---

## 4. The Call-Ready Brief

The deliverable. The research is the evidence behind it. Written to be
spoken, not read aloud verbatim.

~~~
### Sixty-Second Summary
One paragraph a Product Manager can say from memory: who this company
is, what they are doing right now, where they are strong, where they
are exposed, and the one thing that matters most for this conversation.

### The Three Things Worth Saying
1. [Point] -- [the evidence in one clause]
2. [Point] -- [the evidence in one clause]
3. [Point] -- [the evidence in one clause]

Each must be a Fact or a well-corroborated Inference. Nothing on this
list may rest on a single Assumption.

### Questions You Will Be Asked
| Likely question | Short answer | Confidence |
|---|---|---|
| [What they will ask] | [How to answer] | [Solid / Hedge / Do not know] |

Include at least one question you cannot answer, with the honest
response. "I do not know, I will find out" beats a confident guess
repeated by a customer.

### Do Not Say
Claims that are tempting, plausible, and not supported:
- [Claim] -- [why it does not hold up]

### If They Ask What We Do Better
Only when the relationship is competitor or prospect: the two or three
contrasts the evidence actually supports, phrased as outcomes rather
than feature lists, each traceable to a signal above.
~~~

---

## 5. Fusion Brief

Full schema in `fusion.md`. Sections: signal inventory (with collapses
noted) -> fusion stories -> conflicts -> watch items -> collection gaps
-> assumptions to validate -> final step.

---

## 6. Monitor and Delta Reports

Full schemas in `monitors.md`. Every monitor shares: run header ->
materiality bar applied -> changelog in was/now format -> update flags
-> watchlist for next run -> assumptions to validate -> final step.

---

## 7. The Final Step Block (every run)

Exactly four numbered options, the recommended one first and marked.
Then the reply invitation.

~~~
## Final Step

1. [Most likely next move] (Recommended)
2. [Turn this into the downstream artifact]
3. [Set up the recurring version so the next run is a diff]
4. [Reformat or repackage for a different audience]

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom
path.
~~~

Four is the cap. Two options is a false binary; six is a menu nobody
reads. Option 3 should almost always be the scheduling move, because
the compounding value of this work lives in the series, not in any
single run.

---

## Storage Convention for Diffable Series

For a run that will be repeated, name the artifact so the next run can
find it:

~~~
[target-or-market]-[run-type]-[YYYY-MM-DD].md

acme-corp-full-spectrum-2026-08-18.md
analytics-market-watch-2026-08-18.md
acme-corp-pricing-capture-2026-08-18.md
~~~

State the prior file's name in the run header. A delta report that
cannot name what it diffed against is a snapshot with ambition.
