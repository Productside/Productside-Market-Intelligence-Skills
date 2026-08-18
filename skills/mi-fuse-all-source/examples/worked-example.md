# Worked Example: Seven Sources, Four Disciplines, One Story

**Synthetic teaching case.** Cartelane is fictional, and every signal, source, and date below is invented for teaching. Nothing here is a claim about a real company. The reasoning is the transferable part.

**Decision supported:** Accelerate or concede our integration roadmap this quarter.
**Win/loss status:** Unverified — last round eight months ago.
**Prior brief:** First run.
**This run does not collect.**

## 1. Signal Inventory (excerpt)

| Signal | Discipline | Source (URL, date) | Label |
|---|---|---|---|
| ERP integration platform announced | OSINT | `example.invalid/newsroom`, 2026-03-04 | Fact |
| CEO posted 7x in 6 weeks on ERP reconciliation | OSINT | `example.invalid/ceo-posts`, 2026-05 to 06 | Fact |
| 9-filing patent cluster, ledger reconciliation, under acquired entity | TECHINT | `example.invalid/patents`, 2025-03 to 2026-01 | Fact |
| 11 API endpoints under `/v2/ledger-sync/`, absent from product | TECHINT | `example.invalid/api`, 2026-08-12 | Fact |
| 22 integration engineering roles open against a baseline of 3 | HUMINT | `example.invalid/careers`, 2026-08-15 | Fact |
| Partner-connector program moved to "maintenance only" | TECHINT | `example.invalid/partner-docs`, 2026-07-01 | Fact |
| VP of Partnerships departed 5 months after partner-program launch | HUMINT | `example.invalid/role-change`, 2026-06 | Inference |
| New certificate for `ledger.cartelane.example` | SIGINT | `example.invalid/crt`, 2026-07-02 | Fact |
| Entry pricing tier removed; floor rose $49 → $119 | SIGINT | `example.invalid/pricing`, 2026-08-18 | Fact |
| Support first-response median 4h → 19h | MASINT | `example.invalid/forum-sample`, 2026-08-15 | Inference |
| Support postings fell 7 → 2 | HUMINT | `example.invalid/careers`, 2026-08-15 | Fact |
| "Partner ecosystem is central to our integration strategy" | OSINT | `example.invalid/blog`, 2026-01 | Fact |

### Same-Source Collapses

| Apparent sources | Collapsed to | Shared origin |
|---|---|---|
| Newsroom post, 5 trade articles, 1 analyst summary, CEO announcement post | **1 row** | The 2026-03-04 press release |
| Investor update and the webinar reciting it | **1 row** | The investor update |

**Net effect:** 15 apparent sources reduced to **8 independent origins**. The seven-way collapse is the single most important line in this brief. Reported as "seven sources agree," the platform story would have looked overwhelming on OSINT alone.

### Discipline Coverage (post-collapse)

| Discipline | Signals held |
|---|---|
| OSINT | 3 |
| FININT | **none** |
| GEOINT/DEMOINT | **none** |
| TECHINT | 3 |
| HUMINT | 3 |
| SIGINT | 2 |
| MASINT | 1 |

**Disciplines holding signals: 5 of 7.** Enough to fuse. FININT's absence is material and is named in the gaps.

## 2. Fusion Stories (ranked by confidence then consequence)

### Story 1: Cartelane is replacing its partner-built connectors with a native integration layer

- **Disciplines in agreement:** **4** — TECHINT (patent cluster, API endpoints, partner deprecation), HUMINT (22-vs-3 hiring surge, VP departure), SIGINT (staging certificate), OSINT (announcement, CEO posts). Post-collapse; the OSINT contribution is one origin, not seven.
- **The story:** A nine-filing patent cluster under an acquired entity, twenty-two integration roles against a baseline of three, eleven undocumented API endpoints, and a staging certificate all point at a native integration layer being built now. The partner program moving to maintenance-only and the partnership VP's departure say what it replaces. *Inference.*
- **Verdict:** **Actionable.** Four independent disciplines, and critically the two strongest are independent of each other — a patent cluster and a hiring surge in the same specialty would have to fail differently to both be wrong.
- **Commitment level:** **Staffed, verging on Built.** Hiring and a live staging endpoint are past announcement; only customer availability is missing.
- **Response:** Roadmap — set the accelerate-or-concede decision at **2026-Q4**, before their announcement window opens, not after. Owner: Director of Product. Battle card — add the partner-displacement angle for accounts on their connector program, with the deprecation notice cited.

### Story 2: They are firing the bottom of their market

- **Disciplines in agreement:** **2** — SIGINT (entry tier removed, floor +144%, annual discount widened), HUMINT (support postings 7 → 2).
- **The story:** The $49 entry tier disappeared, the published floor rose to $119, and support hiring contracted while engineering hiring surged. *Inference:* a deliberate move upmarket with service cost taken out of the segment being abandoned.
- **Verdict:** **Working hypothesis.** Two disciplines. FININT would settle it — margin-defense language in a filing or call would confirm, and there is no FININT in this brief.
- **Commitment level:** **Built.** The pricing page is live; this has already happened.
- **Response:** Assign a probe — run `mi-collect-finint` on the last two quarters, due in two weeks. Owner: Product Marketing. If confirmed, an entire segment of their installed base is addressable and that is a campaign, not a card line.

### Story 3: Support capacity has degraded

- **Disciplines in agreement:** **2** — MASINT (response median 4h → 19h), HUMINT (support postings 7 → 2).
- **The story:** Measured first-response times nearly quintupled over ninety days while support hiring contracted. *Inference*, and an ambiguous one: cost constraint or growth overwhelm produce the same signature.
- **Verdict:** **Working hypothesis, capped.** Two disciplines, and **win/loss is unverified this cycle**, so an org-instability story may not rate higher. Public signals cannot establish that support quality decides deals in this market; only interviews can.
- **Commitment level:** n/a — a condition, not a move.
- **Response:** Probe via the next win/loss round — question already drafted. **Do not put this on a battle card yet.** A rep who claims a support advantage against a prospect who is a happy Cartelane customer loses the room.

Three stories, not five. There were not five worth writing, and padding to the cap is how fusion starts inventing.

## 3. Conflicts

### Conflict: the partner ecosystem

- **Signal A implies:** Their January blog states the partner ecosystem is "central to our integration strategy." Partners remain a positioning pillar.
- **Signal B implies:** The partner program is closed to new partners, the program docs say maintenance-only, the partnership VP left, and twenty-two in-house integration engineers are being hired.
- **Which one the money supports:** B, decisively. Twenty-two salaries and a nine-filing prosecution budget against one blog post.
- **What would settle it:** Their next partner-summit agenda, or the absence of one. Also any FININT commentary on partner-sourced revenue.

Not averaged into "they are evolving their partner strategy." That sentence would be technically defensible, would satisfy everyone, and would tell the reader nothing. The disagreement between what Cartelane says and what Cartelane funds *is* the finding.

## 4. Watch Items

| Signal | Discipline | What would escalate it |
|---|---|---|
| SOC 2 Type II in process | MASINT | A compliance-specific hire, or a regulated-segment customer logo |
| Brand-term bidding with migration ad copy | SIGINT | Sustained spend across a second quarter |
| Two-floor lease expansion | MASINT | FININT capex confirmation |

Each is one discipline. Logged, not acted on. That is the whole discipline of a watch item.

## 5. Collection Gaps

| Discipline with no signals | Which sweep fills it | Why it matters here |
|---|---|---|
| FININT | `mi-collect-finint` | Story 2 cannot rise above working hypothesis without it, and the commitment reading on Story 1 would firm up |
| GEOINT/DEMOINT | `mi-collect-geoint-demoint` | Nothing in this brief establishes whether the segment they are moving toward is large enough to justify the investment |

The GEOINT gap is the quieter of the two and possibly the more important: five disciplines agree Cartelane is building something, and none of them says whether the market rewards it.

## Assumptions to Validate

1. **The OSINT collapse is treated as complete.** If any of the five trade articles did independent reporting, OSINT contributes more than one origin and Story 1 strengthens slightly. It would not change the verdict.
2. **The patent cluster and the hiring surge are treated as independent.** They are the same *strategy*, but they are different bureaucracies producing different records, and both would have to be misread for the story to be wrong.
3. **Win/loss unverified is treated as capping Story 3.** If interviews are run and integration breadth turns out not to decide deals, Story 1's *response* changes even though its verdict does not.

## Final Step

1. Set the Q4 accelerate-or-concede date and assign the FININT probe (Recommended)
2. Turn Story 1 into a battle card with the partner-displacement angle
3. Schedule the fusion cadence so the next brief is a delta
4. Fill the GEOINT gap — nobody has checked whether the segment justifies their investment

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
