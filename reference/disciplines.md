# The Disciplines

Eight in total: **seven collection disciplines** plus **all-source
fusion**, which collects nothing and exists to combine the other seven.

Doctrine. Each discipline tells you (1) what to collect, (2) where,
(3) which signal-to-inference chains to run, and (4) which Product
Manager artifact it feeds.

Every example is illustrative, not prescriptive. Swap in the
engagement's own [TARGET] and [CAPABILITY].

| # | Discipline | Plain English | Primary artifact fed |
|---|---|---|---|
| 1 | OSINT | Press, social, analysts, reviews, events | Battle cards, positioning |
| 2 | FININT | Filings, earnings calls, procurement | Battle cards, SOM capture rates |
| 3 | GEOINT/DEMOINT | Census, labor, trade, economic statistics | TAM/SAM/SOM, ICPs, personas, messaging |
| 4 | TECHINT | Patents, technographics, changelogs, standards | Roadmap bets |
| 5 | HUMINT | Talent moves, employee chatter, win/loss | Roadmap bets, battle cards |
| 6 | SIGINT | Web diffs, pricing changes, certs, job posts | Battle cards, pricing strategy |
| 7 | MASINT | Supply chain, facilities, ops exhaust | Threat assessment |
| 8 | All-Source Fusion | Cross-validation and confidence stacking | Everything above |

---

## 1. OSINT -- The Journalist's Desk

*What a good beat reporter knows before the press release drops.*

### Sources

| Source type | Free | Paid |
|---|---|---|
| [TARGET] press and newsroom | Company newsroom, Google Alerts, PR Newswire feeds | Meltwater, Cision |
| Industry periodicals | Trade publications, association newsletters, vertical Substacks for [MARKET] | Analyst subscriptions |
| Analyst coverage | Gartner/Forrester press summaries, free webinar replays | Gartner, Forrester, IDC full reports |
| Social and community | LinkedIn exec posts, Reddit, Hacker News, X | Brandwatch, Sprout listening |
| Review sites | Whichever the [BUYER] reads: G2, Capterra, TrustRadius, app stores, Trustpilot | G2 Buyer Intent |
| Conference footprint | Session titles, sponsor tiers, booth size, speaker rosters at [MARKET] events | n/a |
| Prediction markets | Polymarket, Kalshi, Metaculus, Manifold on regulation, approvals, milestones gating [MARKET] | n/a |

### Signal to inference

- Exec suddenly posting about a new problem space -> positioning pivot
  incoming. Execs test messaging on social 3 to 6 months before launch.
- Sponsor tier jump at a [MARKET] conference -> market entry or
  doubling down.
- Review complaints clustering on one feature -> their roadmap pressure
  point, which is your battle card ammunition.
- Analyst briefing requests visible via analyst posts -> category
  creation attempt.
- Webinar topics shifting -> what they teach the market is what they
  are about to sell.
- Sudden silence on a product line -> sunset in progress.
- Prediction-market odds moving on a regulation or milestone gating
  [MARKET] -> crowd-priced expectations for scenario planning. Leading
  indicator of consensus, not ground truth. Check liquidity before you
  trust the number.

### Feeds
Battle cards (objection handling from review mining), positioning (the
gap between their words and customer words), win/loss context.

---

## 2. FININT -- The Forensic Accountant

*Follow the money. Companies lie in press releases. They lie less in
filings, because lying there is a felony.*

### Sources

| Source type | Free | Paid |
|---|---|---|
| Public filings | SEC EDGAR (US), Companies House (UK), BRIS and European e-Justice company search (EU), national securities regulators and exchanges for [GEOGRAPHY] | AlphaSense, Sentieo |
| Earnings calls | Company IR pages, Seeking Alpha transcripts | AlphaSense (search across calls) |
| Private company signals | Crunchbase free tier, incorporation records, insolvency registers, beneficial-ownership registers where legally accessible | PitchBook, CB Insights |
| Government spend and procurement | USAspending.gov, SAM.gov (US); TED and national portals (EU); Etimad, Monaqasat, EONEPS and country platforms (MENA); development-bank procurement (World Bank, IsDB, EBRD, AfDB, UNGM) | GovWin |
| Competition and state-aid cases | European Commission merger, antitrust, cartel, state-aid databases; national competition authorities | n/a |
| State and sovereign capital | Sovereign wealth fund reports, state-owned enterprise annual reports, PPP pipelines | n/a |

### Signal to inference

- **Risk Factors section changes year over year** -> what genuinely
  scares them. They are legally required to disclose it.
- Segment reporting restructure -> strategic reprioritization. Follow
  which segment got promoted.
- Earnings call Q&A dodges, where analysts ask and execs deflect ->
  soft spot. Probe it in positioning.
- New entity registrations, subsidiaries, or branches in [GEOGRAPHY] ->
  market entry before any announcement.
- Deferred revenue trends -> actual sales momentum versus stated
  momentum.
- Merger filings -> market definitions and named competitors, straight
  from [TARGET]'s own lawyers.
- Contract modifications expanding an incumbent's procurement scope ->
  locked-in account. Plan around it, not through it.
- Sovereign fund or state-aid money backing [TARGET] -> their runway
  math just changed. Discount-pressure plays will not work.
- Prior Information Notices and expressions of interest -> tenders
  telegraphed 3 to 24 months out.

### Feeds
Battle cards (financial stress means discount pressure, which means
quarter-end desperation plays), SOM capture rates (revenue divided by
claimed customer count is a deal size reality check), account
targeting via procurement award patterns.

---

## 3. GEOINT/DEMOINT -- The Cartographer

*The terrain map, not troop movement. Government statistics are free
intelligence most Product Managers never open, and they are the
backbone of every ICP, persona, and TAM that survives scrutiny.*

### Sources

| Source type | Free | Paid |
|---|---|---|
| US market structure | Census Bureau (County Business Patterns, Economic Census, NAICS establishment counts), BEA | IBISWorld, Statista, Grand View Research |
| US labor and buyers | BLS (occupation counts, wages, industry employment), FRED (macro conditions gating budgets) | TalentNeuron |
| EU market structure | Eurostat, PRODCOM, national statistical institutes, ECB data | National data resellers |
| EU trade flows | Eurostat COMEXT, Access2Markets, TARIC (tariffs, quotas, rules of origin) | Panjiva, S&P Global |
| MENA regional | GCC-Stat and Marsa Data Portal, Arab Development Portal, ESCWA, Arab Monetary Fund, SESRIC | n/a |
| MENA national | GASTAT (Saudi), FCSC (UAE), CAPMAS (Egypt), HCP (Morocco), INS (Tunisia), ONS (Algeria), and peers | n/a |
| Global cross-check | World Bank Data and Enterprise Surveys, IMF country reports, OECD.Stat, UN Comtrade, ITC Trade Map | n/a |

### Signal to inference

- Establishment counts by industry code and employee band -> the
  denominator for bottom-up TAM.
- Regional industry concentration -> where SOM actually lives, and
  where field sales should live.
- Occupation growth curves for the [BUYER] and end-user roles -> is the
  population you sell to growing or shrinking.
- Wage trends in buyer roles -> willingness-to-pay ceiling shifts, and
  pricing corridor validation.
- Firmographic distributions (size bands, legal forms, sectors) -> ICP
  boundaries drawn from data, not vibes.
- Buyer-title prevalence by [GEOGRAPHY] -> persona localization. The
  "VP of Product" you message in Boston is a "Head of Digital" in
  Frankfurt and may not exist in Riyadh.
- Language, regulatory, and disclosure environment per country ->
  messaging localization and evidence standards.
- Trade-flow shifts in product-specific codes -> market entry or supply
  relocation before any announcement.

### The TAM/SAM/SOM recipe (this discipline's signature dish)

~~~
TAM: Establishment counts for [MARKET] (Census/NAICS, Eurostat/NACE,
     GCC-Stat, or national equivalent for [GEOGRAPHY])
     x employment or spend benchmarks (BLS, Eurostat, trade associations)
     Validate against two independent analyst reports. If they disagree
     by 3x, say so rather than picking the flattering one.

SAM: TAM filtered by real constraints: [GEOGRAPHY], segment, compliance
     requirements, tech prerequisites (TECHINT technographics),
     local-content and vendor-registration eligibility where applicable.

SOM: SAM x realistic capture rate derived from [TARGET] filings via FININT
     (their revenue / their claimed customer count = deal size reality check)
~~~

### Feeds
TAM/SAM/SOM (the backbone), ICP definition, personas, messaging
localization, market entry prioritization, pricing corridor validation.

---

## 4. TECHINT -- The Patent Examiner

*R&D leaves fingerprints 12 to 18 months before products ship.*

### Sources

| Source type | Free | Paid |
|---|---|---|
| Patents | patents.google.com, USPTO Patent Center, EPO Espacenet, WIPO PatentScope | Clarivate, LexisNexis PatentSight+ |
| Technographics | BuiltWith free lookups, Wappalyzer | HG Insights, BuiltWith Pro, 6sense |
| Product telemetry | Public changelogs, API docs diffs, status pages, GitHub org activity | n/a |
| Standards bodies | Whichever govern [MARKET]: IETF, W3C, ISO committees, CEN/CENELEC/ETSI work programs, industry consortia | n/a |
| Funded research | CORDIS and Horizon Europe project databases (participants, deliverables, pilot sites), university repositories | n/a |
| Academic and preprints | arXiv, Google Scholar, Semantic Scholar, SSRN, proceedings that matter to [MARKET] | Dimensions, Scopus |
| Trademarks | USPTO TESS, EUIPO, WIPO Global Brand Database | Corsearch |

### Signal to inference

- Patent **clusters** (5+ filings in one classification within 12
  months) -> committed bet on [CAPABILITY], not exploration.
- Inventor names repeating across filings -> the actual product team.
  Track their conference talks and LinkedIn.
- Trademark filing for a product-sounding name -> launch inside 6 to 12
  months. Trademarks are cheap and companies file close to launch.
- Trademark filing following a funded research project's completion ->
  commercialization underway.
- [TARGET] repeatedly appearing in funded consortia -> long-range bet,
  12 to 48 months of lead time.
- Research pilot sites -> likely launch customers, named in public
  deliverables.
- [TARGET] chairing a standards committee -> they intend to shape the
  rules of [MARKET], not just play by them.
- [TARGET]-affiliated authors publishing on arXiv or at [MARKET]
  conferences -> R&D direction 6 to 24 months before patents. A paper
  cluster plus a hiring surge in the same specialty is one of the
  strongest fusion pairs available.
- Author affiliations shifting from university to [TARGET] on
  successive papers -> they hired the lab, not just the idea.
- API docs adding endpoints for an unreleased capability -> beta
  program running now.
- Public repo activity, new SDKs, scaffolding -> developer platform
  play.
- Prospects' tech stacks (technographics) -> SAM refinement. Who can
  actually buy you.

### Feeds
Roadmap bets (where to accelerate versus concede), SAM refinement,
battle cards (feature-gap countdown clocks), build/buy/partner
decisions.

---

## 5. HUMINT -- The Sports Scout

*Organizations announce strategy through job boards long before press
releases. People are the tell.*

### Sources

| Source type | Free | Paid |
|---|---|---|
| Job postings | LinkedIn Jobs, [TARGET] careers pages, Indeed | JobsPikr, TalentNeuron, Revelio Labs |
| Employee sentiment | Glassdoor, Blind, Reddit communities for [MARKET] | n/a |
| Leadership moves | LinkedIn announcements, press | BoardEx, The Org |
| Win/loss | Your own sales debriefs, churned-customer interviews | Clozd, DoubleCheck |
| Conference hallway | Your field team's ears at [MARKET] trade shows | n/a |

### Signal to inference

- Hiring surge in one specialty (30+ postings in a quarter) ->
  building [CAPABILITY], not a feature.
- Regional specialist roles appearing for a [GEOGRAPHY] you have not
  seen them in -> expansion pre-announcement.
- Job posts naming specific technologies -> confirmed stack choices,
  which is integration roadmap intelligence.
- Senior product or tech leader exits within 6 months of a strategy
  announcement -> the strategy is in trouble.
- Your own alumni landing at [TARGET] -> assume they know your
  playbook.
- Employee reviews mentioning pivot, reorg, or leadership churn -> two
  quarters of internal distraction, which is your window.
- Win/loss interviews -> the only source that tells you *why* deals
  close. Everything else is inference.

### Feeds
Roadmap bets, battle cards (org instability plays), win/loss program
(ground truth for everything).

---

## 6. SIGINT -- The Wiretap You Are Allowed To Have

*Companies broadcast constantly through what they change on the public
internet. Most competitors never listen.*

### Sources

| Source type | Free | Paid |
|---|---|---|
| Website diffs | Wayback Machine, Visualping free tier | Visualping, Klue, Crayon |
| Pricing pages | Manual snapshots plus Wayback | Klue, Crayon, Kompyte |
| SEO/SEM moves | Google `site:` queries, free Semrush lookups | Semrush, Ahrefs, SpyFu |
| App store metadata | Version notes, screenshot changes, keyword shifts | Sensor Tower, data.ai |
| DNS and infrastructure | crt.sh (new SSL certs reveal new subdomains), DNS records | n/a |
| Webinar and event cadence | [TARGET] events pages, registration platforms | n/a |

### Signal to inference

- New subdomain SSL cert such as `[capability].[target].com` ->
  product launch staging, often weeks ahead.
- Pricing page removes a tier -> packaging overhaul, usually toward
  enterprise.
- Sudden SEM bidding on *your* brand terms -> they consider you the
  threat now. Congratulations.
- Case study page pattern shifts, new vertical or [GEOGRAPHY]
  appearing -> segment push.
- Messaging A/B visible via Wayback diffs -> they are unsure of
  positioning. Hit the wound.

### Feeds
Battle cards (the freshest layer, which is what keeps cards from going
stale), pricing strategy, positioning counter-moves.

---

## 7. MASINT -- The Satellite Photo

*Measure the physical and operational exhaust. Abnormal resource
allocation never lies.*

### Sources

| Source type | Free | Paid |
|---|---|---|
| Supply chain | ImportYeti free tier, Panjiva summaries, Eurostat COMEXT and customs codes, UN Comtrade | S&P Global Supply Chain Intelligence, Panjiva, ImportGenius |
| Facilities and projects | Commercial real estate news, local business journals, permits in [GEOGRAPHY]; industrial-zone and free-zone tenant announcements, environmental permits, utility-connection approvals, EPC contract awards; satellite imagery | CoStar |
| Ops capacity | Support response time sampling, status page incident frequency | n/a |
| Certifications and safety | Whichever gate [MARKET]: ISO, SOC 2, FedRAMP, CE marks; NANDO notified-body designations and Safety Gate recalls (EU); sector registries | n/a |

### Signal to inference

- 20%+ volume change in critical inputs -> pre-launch or demand
  collapse. Check which via FININT.
- New supplier geographies or country-of-origin shifts -> market entry,
  tariff hedging, or a resilience play.
- Certification "in process" listings, or [TARGET] selecting a notified
  body for a new product category -> 12 to 36 month runway into a
  regulated segment, visible to anyone who checks the registry.
- Product recalls or repeated safety-alert patterns -> quality strain,
  with a public citation attached.
- Land allocation, power or water capacity reservations, or engineering
  design contracts preceding equipment procurement -> facility buildout
  6 to 36 months before any launch announcement.
- Support response times stretching plus a hiring freeze in support
  roles -> cash constraint or overwhelmed by growth. Disambiguate via
  employee sentiment.
- Office consolidations -> cost compression. Expect pricing aggression
  to follow.

**Note:** supply chain and facility signals are strongest for hardware
and industrial players. The software equivalent is ops capacity plus
infrastructure-scale language in job postings.

### Feeds
Threat assessment, launch prediction and capacity estimates, battle
cards (capacity-stretch objections: "ask them about their support SLAs
lately").

---

## 8. All-Source Fusion -- The Situation Room

*One signal is an anecdote. Three correlated signals from independent
disciplines is intelligence.*

Full procedure in `fusion.md`. The short version lives in SKILL.md
because every run touches it.

---

## Artifact-to-Discipline Map

| Artifact | Primary disciplines | Refresh cadence |
|---|---|---|
| TAM/SAM/SOM | GEOINT/DEMOINT + FININT (capture rates) + TECHINT (technographics) | Annual, plus event-driven |
| ICPs and personas | GEOINT/DEMOINT + HUMINT (win/loss ground truth) | Semi-annual |
| Messaging and localization | GEOINT/DEMOINT + OSINT | Semi-annual |
| Battle cards | SIGINT + OSINT + HUMINT (win/loss) | Weekly SIGINT layer, monthly rebuild |
| Roadmap bets | TECHINT + HUMINT | Quarterly |
| Positioning | OSINT + FININT (earnings language) | Semi-annual |
| Pricing strategy | SIGINT + FININT + GEOINT/DEMOINT (wage and WTP corridors) | Event-driven |
| Threat assessment | All-source fusion | Quarterly brief, plus event-driven |

---

## Strongest Fusion Pairs

Cheap to check, and they resolve the ambition-versus-commitment question
fast. The first two and the last are source doctrine; the middle rows
are extensions, offered as working pairs rather than canon.

| Pair | What it resolves |
|---|---|
| TECHINT paper or patent cluster + HUMINT hiring surge, same specialty | Is the R&D bet staffed or theoretical |
| SIGINT new subdomain cert + TECHINT API endpoint additions | Is the launch staged or announced |
| OSINT announcement + FININT capex or procurement | Is the strategy funded or narrated |
| MASINT input volume change + FININT deferred revenue trend | Pre-launch buildup or demand collapse |
| SIGINT pricing page change + FININT earnings margin language | Packaging experiment or margin defense |
| HUMINT exec exit + OSINT product line silence | Sunset in progress |
| GEOINT/DEMOINT segment size + FININT investment scale | Does the market they would enter exist at the size the move implies |
