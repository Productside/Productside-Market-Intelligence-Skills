# Skill Index

Every skill in this Project, with the stage it belongs to, the collection discipline it speaks for, and what triggers it.

The authoritative registry lives in `scripts/validate-skills.py`. This index is written from the skills' own frontmatter and should match it.

## Instantiate

Scope the engagement and route the run. Stops if you cannot name the decision.

### `mintel:mi-router-market-intelligence`

**Route a Market Intelligence Run** — Scope the engagement, then pick the sweep

- **Discipline:** All-Source Fusion
- **Type:** router
- **Time:** 5-15 min · **Group:** 1-8
- **Argument hint:** `[target company or market] [what changed]`
- **Consumes:** nothing — this run can start cold
- **Combine with:** `mi-sweep-full-spectrum`, `mi-fuse-all-source`, `mi-watch-competitors`

Instantiate a market or competitor engagement on six variables and route it to the right run. Use when a company or market suddenly matters and you do not yet know which sweep to run.

**Reach for it when:**

- A competitor turned up in three lost deals this month and my VP wants to know what is going on
- We have a partner call this afternoon and I know almost nothing about them
- Someone forwarded me a competitor announcement and asked what we should do
- Our battle cards have gone stale and nobody trusts them

**It produces:**

- Completed Instantiate block on the six variables
- A named decision, or a stop
- Routing recommendation with the reference files that run needs

## Collect

Gather and label signals in a defensible sweep order. These runs do not render verdicts.

### `mintel:mi-collect-finint`

**FININT Collection Sweep** — Follow the money through the filings

- **Discipline:** FININT
- **Type:** investigation
- **Time:** 45-90 min · **Group:** 1-4
- **Argument hint:** `[target company] [geography] [decision]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-fuse-all-source`, `mi-size-tam-sam-som`, `mi-refresh-earnings-signals`

Follow the money on a company — filings, Risk Factors diffs, earnings dodges, procurement awards, entity registrations, state capital. Use to separate a funded move from a narrated one.

**Reach for it when:**

- They announced a platform play and I need to know if anyone is paying for it
- We keep losing to an incumbent whose procurement scope quietly keeps expanding
- Our SOM assumption is a guess and finance is going to ask where it came from
- A sovereign or state-linked investor turned up on their cap table

**It produces:**

- Fusion-ready signal inventory with URLs, dates, and evidence labels
- Risk Factors year-over-year diff
- Money-versus-message read
- Capture-rate inputs for sizing, and collection gaps

### `mintel:mi-collect-geoint-demoint`

**GEOINT/DEMOINT Collection Sweep** — Find the denominator in public statistics

- **Discipline:** GEOINT/DEMOINT
- **Type:** investigation
- **Time:** 60-120 min · **Group:** 1-4
- **Argument hint:** `[market and codes] [countries in scope]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-size-tam-sam-som`, `mi-fuse-all-source`, `mi-collect-finint`

Pull the market's denominator from government statistics — establishment counts, occupations, wages, firmographics, trade flows. Use before sizing, ICP work, or persona localization.

**Reach for it when:**

- Finance asked where our market size number came from and we do not have an answer
- We are entering a second country and do not know if the buyer role exists there
- Our ICP was drawn from our best twelve customers and nothing else
- Two analyst reports disagree about this market by a factor of three

**It produces:**

- Fusion-ready signal inventory with a mandatory vintage column
- Establishment counts by code and size band — the denominator
- Occupation, wage, and buyer-title prevalence by country
- Firmographic ICP boundaries and trade-flow reads

### `mintel:mi-collect-humint`

**HUMINT Collection Sweep** — Read the strategy off the job board

- **Discipline:** HUMINT
- **Type:** investigation
- **Time:** 30-60 min · **Group:** 1-4
- **Argument hint:** `[target company] [suspected capability]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-fuse-all-source`, `mi-collect-techint`, `mi-build-battle-card`

Read a company through its people — hiring surges, leadership moves, departures, employee sentiment — and end by generating the win/loss questions only your own team can answer.

**Reach for it when:**

- They are hiring thirty people into a specialty they never staffed before
- Their VP of Product left six months after the strategy announcement
- Employee reviews suddenly all mention a reorg
- Roles appeared for a country they have never sold into

**It produces:**

- Fusion-ready signal inventory with counts against a stated baseline
- Stated-strategy-versus-staffing read
- Three to five win/loss questions tied to specific signals
- The win/loss gap flag for fusion

### `mintel:mi-collect-masint`

**MASINT Collection Sweep** — Measure the operational exhaust

- **Discipline:** MASINT
- **Type:** investigation
- **Time:** 45-90 min · **Group:** 1-3
- **Argument hint:** `[target company] [suspected buildout or strain]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-fuse-all-source`, `mi-collect-finint`, `mi-collect-humint`

Measure a company's operational and physical exhaust — supply chain, facilities, permits, certifications, ops capacity, scale proxies. Use to catch a buildout or a strain before either is announced.

**Reach for it when:**

- Their support response times have been stretching for two months
- A competitor reserved power capacity in an industrial zone
- They appeared in a notified-body register for a product category they do not sell
- Import volumes for their critical component jumped twenty percent

**It produces:**

- Fusion-ready signal inventory with a mandatory disambiguate-via column
- Scale proxies with trend direction and stated windows
- Anomalies with candidate explanations, never with verdicts
- Collection gaps and named handoffs

### `mintel:mi-collect-osint`

**OSINT Collection Sweep** — Sweep the public record on one company

- **Discipline:** OSINT
- **Type:** investigation
- **Time:** 30-60 min · **Group:** 1-4
- **Argument hint:** `[target company] [market and buyer]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-fuse-all-source`, `mi-mine-voice-of-customer`, `mi-build-battle-card`

Sweep a company's public record — press, analysts, exec social, reviews, events, prediction markets — into a fusion-ready signal inventory. Use to learn what they say and what is said about them.

**Reach for it when:**

- Their exec keeps posting about a problem space they have never sold into
- They jumped two sponsor tiers at the conference our buyers attend
- Analysts started describing them with a category name that did not exist last year
- We need to know what customers actually complain about before we write the card

**It produces:**

- Fusion-ready signal inventory with URLs, dates, and evidence labels
- Ranked inference chains, capped at five
- The say-versus-said-about gap
- Collection gaps and named handoffs

### `mintel:mi-collect-sigint`

**SIGINT Collection Sweep** — Diff what they changed in public

- **Discipline:** SIGINT
- **Type:** investigation
- **Time:** 20-45 min · **Group:** 1-3
- **Argument hint:** `[target company] [prior capture date]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-fuse-all-source`, `mi-monitor-pricing-packaging`, `mi-watch-competitors`

Diff what a company changed on the public internet — pricing pages, messaging, docs, SSL certs, app metadata, SEM terms. Use for the freshest competitive layer, the one that keeps battle cards alive.

**Reach for it when:**

- Their pricing page changed and nobody can remember what it said before
- A new subdomain certificate appeared with a capability name on it
- They started bidding on our brand terms
- Their homepage messaging has been rewritten twice this quarter

**It produces:**

- Fusion-ready signal inventory with a mandatory before-to-after column
- Verbatim captures of pricing and messaging for the next diff
- Ranked inference chains with staleness horizons
- Baseline captures where no prior state exists

### `mintel:mi-collect-techint`

**TECHINT Collection Sweep** — Read the fingerprints R&D leaves behind

- **Discipline:** TECHINT
- **Type:** investigation
- **Time:** 45-90 min · **Group:** 1-4
- **Argument hint:** `[target company] [suspected capability]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-fuse-all-source`, `mi-collect-humint`, `mi-build-battle-card`

Sweep patents, trademarks, changelogs, API diffs, repos, standards bodies, and preprints for what a company is building. Use when a roadmap bet depends on what ships in 12 to 18 months.

**Reach for it when:**

- They keep filing in one patent classification and I want to know what it means
- Their API docs grew endpoints for something that is not in the product
- A trademark appeared that looks like a product name
- Their staff are publishing preprints in a specialty we do not staff

**It produces:**

- Fusion-ready signal inventory with a mandatory lead-time column
- Built-versus-shipped read, including deprecations
- Ranked inference chains with clocks attached
- Collection gaps and named handoffs

### `mintel:mi-mine-voice-of-customer`

**Voice-of-Customer Miner** — Mine public reviews for real needs

- **Discipline:** OSINT
- **Type:** investigation
- **Time:** 45-90 min · **Group:** 1-4
- **Argument hint:** `[market or competitor] [buyer]`
- **Consumes:** `mi-collect-osint`, `mi-router-market-intelligence`
- **Combine with:** `mi-build-battle-card`, `mi-fuse-all-source`, `mi-snapshot-competitors`

Mine reviews, app stores, forums, and communities for unmet needs, competitor weak points, and switching triggers, with quoted evidence and frequency labels. Use before a card or a roadmap bet.

**Reach for it when:**

- We need to know what customers actually complain about before we write the card
- Our roadmap is being argued from three anecdotes and one angry reviewer
- A competitor's reviews cluster on something and we do not know what
- We want to know what makes people leave, not just what they dislike

**It produces:**

- Solution-free need themes with frequency labels
- Competitor weak points with quoted, dated evidence
- Switching triggers — the highest-value output
- Per-source bias notes and collection gaps

### `mintel:mi-scan-market-landscape`

**Market Landscape Scan** — Map the category before sizing it

- **Discipline:** OSINT
- **Type:** investigation
- **Time:** 60-120 min · **Group:** 1-6
- **Argument hint:** `[market or category] [buyer]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-snapshot-competitors`, `mi-size-tam-sam-som`, `mi-analyze-five-forces`

Map a market before sizing or positioning it — segments as buyers see them, players including substitutes and non-consumption, dynamics, and whitespace. Use when you are new to a category.

**Reach for it when:**

- We are considering a new market and nobody here can name who is in it
- Our competitive set is three logos and I suspect that is not the real picture
- Analysts describe this category one way and our buyers describe it another
- Leadership wants a market size and we have not established what the market is

**It produces:**

- Buyer-side segmentation, with vendor-category divergence named
- Player map in four buckets, capped at twelve
- Four named dynamics reads
- Whitespace and dead zones, distinguished

### `mintel:mi-snapshot-competitors`

**Competitive Research Snapshot** — Just-enough profiles on who matters

- **Discipline:** OSINT
- **Type:** investigation
- **Time:** 45-90 min · **Group:** 1-4
- **Argument hint:** `[up to three competitors] [buyer]`
- **Consumes:** `mi-scan-market-landscape`, `mi-router-market-intelligence`
- **Combine with:** `mi-build-battle-card`, `mi-watch-competitors`, `mi-fuse-all-source`

Profile a named competitor set with cited snapshots, a buyer-dimension comparison matrix, and a so-what. Use when you know who matters and need just-enough depth on each.

**Reach for it when:**

- Sales keeps naming the same three competitors and we have no current profile
- Our comparison matrix has ten rows and we win on all of them
- We need a baseline before setting up a competitive watch
- Leadership asked who we are really up against

**It produces:**

- Per-competitor snapshots with sources and dates
- Comparison matrix on buyer dimensions, with an evidence-quality row
- So-what with counted implications, risks, and opportunities
- A diffable baseline for the next watch

### `mintel:mi-sweep-full-spectrum`

**Full-Spectrum Company Sweep** — All seven disciplines, one sitting

- **Discipline:** All-Source Fusion
- **Type:** investigation
- **Time:** 30 min rapid / 1-2 hr standard / half day deep · **Group:** 1-4
- **Argument hint:** `[target company] [the conversation this is for]`
- **Consumes:** `mi-router-market-intelligence`
- **Combine with:** `mi-fuse-all-source`, `mi-build-battle-card`, `mi-watch-competitors`

Run all seven collection disciplines on one company in a single sitting, fuse them, and end in a call-ready brief. Use when a company suddenly matters and you have one hour.

**Reach for it when:**

- We have a partner call this afternoon and I know almost nothing about them
- A competitor turned up in three lost deals and my VP wants a read before the QBR
- An acquirer approached us and nobody has profiled them
- I have to answer board questions about this company on Thursday

**It produces:**

- Identity and perimeter block
- Seven per-discipline sections with labeled signals
- Fusion table with confidence and commitment
- Call-ready brief, including a Do Not Say list

## Fuse

Collapse shared origins, stack confidence across independent disciplines, map responses to artifacts.

### `mintel:mi-fuse-all-source`

**All-Source Fusion** — Stack the disciplines, rate the confidence

- **Discipline:** All-Source Fusion
- **Type:** analysis
- **Time:** 45-90 min · **Group:** 1-8
- **Argument hint:** `[collected signals or prior sweeps]`
- **Consumes:** `mi-collect-osint`, `mi-collect-finint`, `mi-collect-techint`, `mi-collect-humint`, `mi-collect-sigint`, `mi-collect-masint`, `mi-collect-geoint-demoint`
- **Combine with:** `mi-build-battle-card`, `mi-analyze-swot`, `mi-watch-competitors`

Reconcile signals from multiple disciplines into confidence-rated stories with artifact-mapped responses. Use when evidence is already in hand and someone has to decide what is actionable.

**Reach for it when:**

- We have three sweeps and a spreadsheet and nobody can say what it means
- Is their announced platform play real, or theater?
- Two of our sources say opposite things and the deck says the average
- Leadership wants a threat assessment and we have evidence but no verdict

**It produces:**

- Signal inventory with same-source collapses noted
- Confidence-rated fusion stories with commitment levels
- Conflicts, kept as conflicts
- Artifact-mapped responses and named collection gaps

## Act

Consume fused evidence into a decision artifact. An unevidenced cell reads "no evidence found."

### `mintel:mi-analyze-ansoff`

**Ansoff Growth Options** — Growth options with a real sequence

- **Discipline:** All-Source Fusion
- **Type:** analysis
- **Time:** 45-90 min · **Group:** 1-8
- **Argument hint:** `[company] [fused evidence]`
- **Consumes:** `mi-fuse-all-source`, `mi-analyze-five-forces`
- **Combine with:** `mi-size-tam-sam-som`, `mi-analyze-swot`, `mi-scan-market-landscape`

Lay out growth options across the four Ansoff quadrants with evidence per move, the risk gradient respected, and a recommended sequence. Use when the question is where to grow next.

**Reach for it when:**

- Leadership wants a growth plan and the default answer is a new vertical
- Our roadmap has three diversification bets and no penetration work
- We need to decide where next year's investment goes
- Someone proposed entering a new market and nobody asked whether the current one is finished

**It produces:**

- Two to three candidate moves per quadrant, each with evidence and a risk rating
- Empty quadrants left empty where the evidence is empty
- A recommended sequence with dependencies
- The 'not yet' move and the assumption that breaks the sequence

### `mintel:mi-analyze-five-forces`

**Five Forces From Evidence** — Industry structure with cited signals

- **Discipline:** All-Source Fusion
- **Type:** analysis
- **Time:** 60-120 min · **Group:** 1-8
- **Argument hint:** `[industry] [fused evidence]`
- **Consumes:** `mi-fuse-all-source`, `mi-scan-market-landscape`
- **Combine with:** `mi-analyze-ansoff`, `mi-analyze-swot`, `mi-size-tam-sam-som`

Rate the five forces from cited signals, name AI substitution and platform dependencies explicitly, and end on the profit pool. Use to judge whether an industry is worth being in.

**Reach for it when:**

- We are considering entering a category and need to know if it can be profitable
- Our margins are compressing and nobody can say structurally why
- The board asked whether AI changes this industry's economics
- We depend on one inference provider and nobody has called that supplier power

**It produces:**

- Five forces rated weak, moderate, or strong, each with cited signals
- An explicit AI-substitution assessment
- Supplier power including platform and model dependencies
- The profit pool read — where the money accumulates and whether you can reach it

### `mintel:mi-analyze-swot`

**SWOT From Evidence** — SWOT with sources and the crossings

- **Discipline:** All-Source Fusion
- **Type:** analysis
- **Time:** 45-90 min · **Group:** 1-8
- **Argument hint:** `[company] [fused evidence]`
- **Consumes:** `mi-fuse-all-source`, `mi-snapshot-competitors`
- **Combine with:** `mi-analyze-five-forces`, `mi-analyze-ansoff`, `mi-build-battle-card`

Build a SWOT from fused evidence with quadrant discipline, ranked entries, and the S-O and W-T crossings that make it a decision. Use when the evidence exists and a position must be stated.

**Reach for it when:**

- Leadership wants a SWOT and we have three sweeps and a fusion brief
- Our last SWOT had a competitor's product filed as a weakness
- We need a position on ourselves that customer evidence actually supports
- The SWOT deck lists twenty items per quadrant and decides nothing

**It produces:**

- Four quadrants, max five entries each, every entry sourced and labeled
- Ranked entries with the stated ranking basis per quadrant
- S-O and W-T crossings with a named move
- Quadrant corrections made visible

### `mintel:mi-build-battle-card`

**Battle Card From Evidence** — A card reps use and can defend

- **Discipline:** All-Source Fusion
- **Type:** analysis
- **Time:** 45-90 min · **Group:** 1-4
- **Argument hint:** `[competitor] [fused evidence]`
- **Consumes:** `mi-fuse-all-source`, `mi-mine-voice-of-customer`, `mi-snapshot-competitors`
- **Combine with:** `mi-watch-competitors`, `mi-monitor-pricing-packaging`, `mi-collect-sigint`

Build a field-ready battle card from cited evidence — say this, ask this, watch out for, do not say — with every claim traced to a dated source. Use to arm sales without arming them wrongly.

**Reach for it when:**

- Our battle cards have gone stale and nobody trusts them
- A rep got corrected by a customer using our own card
- We keep losing to one competitor and the field has nothing
- The card is a feature matrix and reps do not open it

**It produces:**

- Thirty-second read: who they are, when you win, when you lose
- Say this, ask this, watch out for, do not say
- Pricing snapshot with a capture date
- Evidence appendix where every claim traces to a source

### `mintel:mi-size-tam-sam-som`

**TAM, SAM, and SOM** — Bottom-up sizing that survives finance

- **Discipline:** GEOINT/DEMOINT
- **Type:** analysis
- **Time:** 60-120 min · **Group:** 1-6
- **Argument hint:** `[market] [denominator and capture rate]`
- **Consumes:** `mi-collect-geoint-demoint`, `mi-collect-finint`
- **Combine with:** `mi-analyze-ansoff`, `mi-scan-market-landscape`, `mi-fuse-all-source`

Build a bottom-up TAM, SAM, and SOM from a cited denominator and a FININT-derived capture rate, expressed in both currency and customers, with sensitivity. Use before a business case meets finance.

**Reach for it when:**

- Finance asked where our market size number came from and we do not have an answer
- Our business case says one percent of a large number
- Two analyst reports disagree by three times and the deck picked one
- We need a SOM we can defend over a three-year horizon

**It produces:**

- TAM, SAM, SOM in both currency and number of customers
- Every input with a source, a vintage, and a label
- Best, base, and worst cases with the assumption that moves each
- Method declared as bottom-up-built or top-down-validated

## Monitor

Diff against a named prior run. Built to execute on a schedule with nobody watching.

### `mintel:mi-monitor-pestel-delta`

**PESTEL Delta Monitor** — What moved outside our control

- **Discipline:** All-Source Fusion
- **Type:** monitor
- **Time:** 45-90 min · **Group:** 1-6
- **Argument hint:** `[market] [prior PESTEL file]`
- **Consumes:** `mi-fuse-all-source`, `mi-scan-market-landscape`
- **Combine with:** `mi-analyze-five-forces`, `mi-size-tam-sam-som`, `mi-watch-competitors`

Re-scan macro factors quarterly against a prior baseline — what moved, what broke, what entered the frame. Use when an artifact may be resting on something that is no longer true.

**Reach for it when:**

- A regulation entered consultation and nobody has assessed what it touches
- Our market entry case assumed conditions that may have changed
- We do a PESTEL every year and nobody reads it twice
- Leadership wants to know what moved outside our control this quarter

**It produces:**

- Run header naming the prior baseline and the window
- Factor-by-factor delta: moved, or no material movement
- Broken assumptions, with the artifact each one breaks
- New to the frame, and the so-what

### `mintel:mi-monitor-pricing-packaging`

**Pricing and Packaging Tracker** — Capture verbatim, then read the diff

- **Discipline:** SIGINT
- **Type:** monitor
- **Time:** 20-45 min · **Group:** 1-3
- **Argument hint:** `[competitors] [prior capture file]`
- **Consumes:** `mi-collect-sigint`, `mi-snapshot-competitors`
- **Combine with:** `mi-build-battle-card`, `mi-watch-competitors`, `mi-collect-finint`

Track competitor pricing and packaging as a diffable time series, capturing tiers, units, and limits verbatim before interpreting them. Use when next quarter's pricing question must be answerable.

**Reach for it when:**

- A competitor changed pricing and nobody can remember what it was before
- We need to know whether their record limits moved, and nobody captured them
- Their entry tier disappeared and we want to know what that means
- Deal desk is guessing at competitor discounting

**It produces:**

- Verbatim capture of tiers, prices, units, inclusions, limits, minimums
- Was/now delta against the prior capture
- Named packaging signals where they appear
- A stored artifact the next run diffs against

### `mintel:mi-refresh-earnings-signals`

**Earnings and Executive Signal Refresh** — Diff how they talk, quarter over quarter

- **Discipline:** FININT
- **Type:** monitor
- **Time:** 45-90 min · **Group:** 1-3
- **Argument hint:** `[company] [prior profile file]`
- **Consumes:** `mi-collect-finint`, `mi-sweep-full-spectrum`
- **Combine with:** `mi-fuse-all-source`, `mi-build-battle-card`, `mi-watch-competitors`

Diff a company's strategy language quarter over quarter — shifted signals, dropped language, new deflections. Use when how a competitor talks is the leading indicator of what they do.

**Reach for it when:**

- They stopped saying something they said in four consecutive calls
- A segment got promoted in the reporting structure and nobody noticed
- We need a quarterly read on a public competitor without rebuilding the profile
- Their metrics changed and we want to know what stopped being flattering

**It produces:**

- Run header naming the prior profile and the quarters compared
- Shifted signals: strategy language, segment emphasis, metric selection
- Dropped language — tracked as carefully as new language
- Deflection log and the so-what

### `mintel:mi-watch-competitors`

**Competitive Intel Watch** — Material shifts only, run over run

- **Discipline:** SIGINT
- **Type:** monitor
- **Time:** 20-45 min · **Group:** 1-3
- **Argument hint:** `[watchlist] [prior run file]`
- **Consumes:** `mi-snapshot-competitors`, `mi-collect-sigint`
- **Combine with:** `mi-build-battle-card`, `mi-fuse-all-source`, `mi-monitor-pricing-packaging`

Diff a competitor watchlist against a prior snapshot, reporting material shifts only, with was/now changelogs and battle-card update flags. Use to make run N+1 a diff instead of a rebuild.

**Reach for it when:**

- Our battle cards go stale and nobody notices until a rep is embarrassed
- We need a competitive update every month and rebuilding it each time is not working
- Leadership wants to know what changed, not what is true
- We want this to run on a schedule without a human answering questions

**It produces:**

- Run header with prior run, window, and sources swept
- Changelog of material shifts only, in was/now format
- Update flags with owners and urgency
- Watchlist for the next run, with escalation triggers

## Coverage Check

Every collection discipline has a `collect`-stage skill behind it. Validation fails if one loses its skill, because `reference/sweep-playbooks.md` names seven channels and a channel with no runnable skill is a door that does not open.

| Discipline | Collection skill |
|---|---|
| OSINT | `mi-collect-osint`, `mi-mine-voice-of-customer`, `mi-scan-market-landscape`, `mi-snapshot-competitors` |
| FININT | `mi-collect-finint` |
| GEOINT/DEMOINT | `mi-collect-geoint-demoint` |
| TECHINT | `mi-collect-techint` |
| HUMINT | `mi-collect-humint` |
| SIGINT | `mi-collect-sigint` |
| MASINT | `mi-collect-masint` |

`mi-sweep-full-spectrum` speaks for all seven at collection-floor depth in a single run.
