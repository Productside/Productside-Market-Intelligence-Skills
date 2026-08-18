# TECHINT Collection: [TARGET]

**As-of date:** [today]
**Decision supported:** [the roadmap bet this changes]
**Prior sweep:** [date and filename, or "first run"]
**Window covered:** [range; 24 months for patents, 12 for changelogs]
**Suspected capability:** [specific enough to be wrong, or "none — reporting clusters as found"]
**Web access:** [yes, researching live / no, running from training data with vintage stated]

## Search Plan

- **Sweep order:** patents by assignee and classification → repeating inventors → trademarks → changelogs, release notes, deprecations → API doc diffs → repos and SDKs → standards committees → funded consortia → preprints and conference papers
- **Date window:** [range]
- **Noise filter:** [assignee-name variants and acquired entities included, listed; same-name assignees excluded, listed]

## Assignee Perimeter

| Name filed under | Relationship | Why included |
|---|---|---|
| [name] | [primary / acquired 20XX / research subsidiary] | [reason] |

Filings frequently sit under a name nobody uses in the market. Sweeping only the trading name is how a cluster goes missing.

## 1. Signal Inventory (fusion-ready)

Every row carries a lead time. A roadmap implication without a clock is a direction without a deadline.

| Signal | Source (URL, date) | Label | Lead time | Inference chain | Feeds |
|---|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [12-18 mo / 6-12 mo / weeks / ...] | [What it implies] | [Roadmap / Battle card / SAM / ...] |

## 2. Classification Clusters

| Classification | Filings in window | Window | Read |
|---|---|---|---|
| [code and plain-English description] | [count] | [12 months ending YYYY-MM] | [committed bet / exploratory / single filing, not a cluster] |

Five or more filings in one classification within twelve months is a commitment. Fewer is noise until something else corroborates it.

## 3. The People Behind It

- **Repeating inventors or authors:** [names, and how many filings or papers each appears on]
- **Where they came from:** [prior affiliation, and whether an affiliation shifted from a university to [TARGET]]
- **What they say in public:** [talks, papers, profiles — with links]

## 4. Built Versus Shipped

| What the registries and repos show | What customers can buy today | Read |
|---|---|---|
| [capability under construction, with source] | [shipped / partially shipped / absent] | [countdown clock — deadline: YYYY-QX] |

### Deprecations (equal space, always)

| Removed or sunset | Source (URL, date) | Read |
|---|---|---|
| [endpoint, SDK, product line, doc page] | [URL, date] | [what they have given up on, and what that frees] |

A company will announce what it is building and never announce what it stopped building. This table is where that shows up.

## 5. Strongest Inference Chains (max 5, ranked)

1. **[Signal cluster]** → [inference, labeled] → [roadmap move] — *lead time: [X], so the decision date is [YYYY-QX]*
2. …

## 6. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 7. Collection Gaps and Handoffs

> **No signal found.** [Channel] returned nothing on [what was sought]. Sources swept: [list]. What the absence itself suggests: [read]. What would close it: [the specific registry or deep sweep].

- **Fusion pairing flag:** this sweep establishes intent to build. Whether the bet is *staffed* is a HUMINT question. Run `mi-collect-humint` on the same specialty before any story here is rated.
- **Handoffs:** technographics → `mi-size-tam-sam-som` SAM refinement; feature gaps and clocks → `mi-build-battle-card`; everything → `mi-fuse-all-source`

## Assumptions to Validate

1. [The assumption that most changes the read if wrong]
2. [Second]
3. [Third]

## Final Step

1. Hand this to fusion and run HUMINT next to test whether the bet is staffed (Recommended)
2. Go deeper on the largest classification cluster
3. Schedule a quarterly TECHINT pass so the next run is a diff
4. Turn the shortest lead time into a dated roadmap decision

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
