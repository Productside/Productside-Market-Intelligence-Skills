# All-Source Fusion

*One signal is an anecdote. Three correlated signals from independent
disciplines is intelligence.*

This is the situation room. It fuses; it does not collect. If two or
fewer disciplines hold signals, say so and offer a targeted gap-fill
with a 3-bullet search plan. Otherwise fuse what exists and rate
accordingly.

Workflow: **inventory -> independence test -> cluster into stories ->
stack confidence -> commitment check -> verdicts, responses, gaps.**

---

## Step 1: Inventory Every Signal

Everything available: session outputs from sweeps, pasted findings,
attached documents. Tag each with discipline, source URL, date, and a
Fact / Inference / Assumption label.

Do not collect new evidence unless a targeted gap-fill is approved.

| Signal | Discipline | Source (URL, date) | Label |
|---|---|---|---|

---

## Step 2: The Independence Test (before any stacking)

Two signals citing the same underlying source count as **one**
discipline. Corroboration requires independent channels.

Collapse these to one:

- A press release and the trade-press coverage of that press release
- An analyst note and the vendor blog post quoting it
- A job posting and the LinkedIn post announcing the job posting
- Three articles all sourced to the same unnamed executive
- A company's investor deck and the earnings call reciting it

Keep these separate:

- A patent filing and a hiring surge in the same specialty
- A pricing page change and an earnings-call margin comment
- A permit record and a supplier volume shift
- Customer reviews and win/loss interviews

Note every collapse in the inventory. "Six sources" that collapse to
two disciplines is the single most common way competitive decks lie by
accident.

---

## Step 3: Cluster Into Stories

A story is a hypothesis about what [TARGET] is doing. Name it as a
capability or a move, not a vibe.

Good: "Building a first-party analytics layer to defend renewals."
Bad: "Getting more aggressive."

Cap at 5 stories in Just Enough Mode, 7 in a full-spectrum sweep. The
eighth is noise.

---

## Step 4: Stack Confidence

~~~
1 discipline flags it  -> Watch item. Log it, do nothing.
2 disciplines agree    -> Working hypothesis. Assign someone to probe.
3+ disciplines agree   -> Actionable intelligence. Brief leadership, move.
Disciplines conflict   -> The most interesting case. Someone is bluffing. Dig.
~~~

Rank by confidence, then by consequence. A high-confidence story about
something that does not matter ranks below a working hypothesis about
something that decides the year.

**Win/loss weighting.** If win/loss interviews are unverified this
cycle -- nobody has run them, or the last round predates the window --
cap org-instability and build-signal stories at working hypothesis and
say so in the verdict. Public signals infer why deals move. Only the
interviews know. A build-signal story rated actionable without ground
truth is how a roadmap gets reordered by a job posting.

---

## Step 5: The Commitment Check

**Treat announcements as intent until funding, procurement, land,
permits, hiring, or contracts corroborate them.**

Ambition is OSINT. Commitment shows up in FININT, MASINT, and HUMINT.
An OSINT-only story cannot rate above working hypothesis, no matter how
many outlets carried it.

For each story, state which it is. The five-level ladder below is an
extension of the source doctrine, which states the rule in freeform:
*intent until funding, procurement, land, permits, hiring, or contracts
corroborate it.* The ladder makes it gradeable.

| Level | Evidence that establishes it |
|---|---|
| Announced | Press release, exec statement, keynote, roadmap slide |
| Funded | Capex line, funding round, budget approval, state aid |
| Procured | Tender award, contract, supplier agreement, vendor registration |
| Staffed | Hiring surge, named leadership, acquired team |
| Built | Shipping product, API endpoints, permits, facility, certification |

A story sitting at Announced with nothing below it is a watch item
dressed as a threat. This rule came out of MENA tradecraft, where the
gap between national ambition and funded commitment is widest, and it
generalizes everywhere.

---

## Step 6: Conflicts (someone is bluffing)

**Never average two conflicting signals into a comfortable middle.** A
conflict is a finding, and usually the most useful thing in the
document.

For each conflict:

- What signal A implies
- What signal B implies
- Which one the money supports
- The specific evidence that would settle it, and where to look

The most common conflict: the company's own messaging against its own
resource allocation. When those disagree, the resources are telling the
truth.

---

## Step 7: Artifact-Mapped Responses

Every actionable story names the artifact that changes and the move to
make **before** their launch, not after.

| Story confidence | Required response |
|---|---|
| Watch item | Log it, name the escalation trigger. No artifact changes. |
| Working hypothesis | Assign a named probe with a deadline and the discipline that would resolve it. |
| Actionable | Name the artifact, the change, and who makes it. Brief leadership. |

Artifacts available: battle card, roadmap bet, pricing, positioning,
messaging, ICP, TAM/SAM/SOM, threat assessment, partner strategy,
account targeting.

If a story changes no artifact and triggers no probe, it is
competitive trivia. Cut it or demote it to a watch item.

---

## Output Schema

~~~
# All-Source Fusion Brief: [TARGET / Market]

**As-of date:** | **Decision supported:** | **Prior brief:** [date or "first run"]

## 1. Signal Inventory
| Signal | Discipline | Source (URL, date) | Label |
[Same-source duplicates collapsed and noted]

## 2. Fusion Stories (max 5, ranked by confidence then consequence)

### Story: [TARGET]'s [capability / move]
- **Disciplines in agreement:** [count and names, post-independence-test]
- **The story:** [2-3 sentences, labeled Inference]
- **Verdict:** [Watch item / Working hypothesis / Actionable] -- [why,
  including the independence check]
- **Commitment level:** [Announced / Funded / Procured / Staffed / Built]
- **Response:** [artifact that changes, and the move to make before
  their launch]

## 3. Conflicts (someone is bluffing)
- [A implies X; B implies not-X] -- [what each would mean] -- [evidence
  that settles it, and where to look]

## 4. Watch Items (single-discipline flags, logged only)
- [Signal] -- [discipline] -- [what would escalate it]

## 5. Collection Gaps
- [Discipline with zero signals] -- [which sweep fills it]

### Assumptions to Validate
- [The assumption that most changes the brief if wrong]
- [Second]
- [Third]
~~~

Keep this schema stable. If a prior fusion brief is in session, lead
with the delta.

---

## The Fusion Template

For working a suspected [CAPABILITY] play deliberately rather than
waiting for signals to arrive.

| Discipline | Signal (fill in what you found) |
|---|---|
| MASINT | Resource, input, or facility anomaly: ____ |
| TECHINT | Patent cluster, repo, or paper activity: ____ |
| HUMINT | Hiring pattern or leadership move: ____ |
| SIGINT | Infrastructure or web change: ____ |
| FININT | Filing language, procurement award, or earnings dodge: ____ |
| GEOINT/DEMOINT | Terrain check: does the market they would be entering exist at the size the move implies? ____ |
| OSINT | What they are saying about it, if anything: ____ |

**Verdict:** ____ disciplines, one story -> confidence -> commitment
level -> recommended response.

*Illustrative fill:* +20% specialized component orders (MASINT), 15 new
filings in one patent class (TECHINT), 30+ platform engineers hired
(HUMINT), new product subdomain cert issued (SIGINT), CFO dodges an
analyst question on related capex (FININT), and the addressable segment
supports the investment math (GEOINT/DEMOINT). Six disciplines, one
story: high-confidence platform threat, commitment level Staffed
verging on Built. Response: accelerate your own platform roadmap and
arm sales with a maturity battle card *before* their launch, not after.

---

## Worked Example: A Launch Caught Before the Press Release

The weekly SIGINT sweep finds a new SSL certificate for
`analytics.competitor.com` -- launch staging, weeks ahead. That flags
TECHINT, which finds an eight-filing patent cluster in analytics
classifications plus two preprints by their staff. TECHINT flags its
fusion pair, HUMINT, which finds 25 data-engineering postings this
quarter against a baseline of 4. Fusion stacks it: three independent
disciplines, one story, actionable. FININT's earnings pass adds the CFO
dodging an analytics capex question, so intent is corroborated by
money.

Response before their launch: battle-card maturity play, plus an
accelerate-or-concede call on the roadmap. The next win/loss round
confirms whether analytics actually decides deals, and that answer
feeds the following fusion run.

Note what did the work. No single find was decisive. The cert alone was
a watch item.

---

## Anti-Patterns

- Stacking confidence without running the independence test first.
- Rating an OSINT-only story as actionable because the announcement was
  everywhere.
- Averaging conflicting signals into a middle verdict.
- Naming a story as a vibe ("they are getting aggressive") so it can
  never be falsified.
- A fusion brief built on invented signals. That is disinformation with
  a confidence score attached.
- Ending on findings rather than on responses.
