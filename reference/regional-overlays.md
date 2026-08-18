# Regional Source Overlays

The disciplines do not change across markets. The sources do, and so
does the evidentiary burden.

Load the overlay matching [GEOGRAPHY] **after** completing the
Instantiate block, and complete [GEOGRAPHY] at country level. "EMEA" is
not a geography; it is a sales region wearing a map.

**The two lessons worth carrying everywhere:**

- **EU:** the challenge is finding the right record inside a rich but
  fragmented disclosure system. BRIS, TED, CORDIS, EUR-Lex, and
  Eurostat each hold a piece. Nobody holds it all.
- **MENA:** the challenge is separating national ambition from funded,
  procured, permitted, operational commitment.

---

## European Union Overlay

Unusually rich public data, spread across EU-level portals, national
registries, regulators, standards bodies, and Member State procurement
systems.

### Procurement and contracts (maps to FININT)

**Sources:** TED (Tenders Electronic Daily) for planning notices,
tenders, awards, direct-award preannouncements, modifications,
concessions, utilities procurement; TED Open Data and Search API for
trend, supplier-concentration, and incumbent analysis; EU Funding and
Tenders Portal for EU-funded programs and consortium activity; national
and regional portals for below-threshold opportunities; sector portals
for utilities, transport, healthcare, municipal, and defence.

**Signals:** Prior Information Notices before a formal tender; contract
modifications expanding an incumbent's scope; recurring
framework-agreement winners; Common Procurement Vocabulary codes
appearing at new buying authorities; evaluation criteria shifting from
lowest price toward lifecycle cost, sustainability, cybersecurity,
interoperability, or resilience; increased use of negotiated procedures
or direct awards; groups of municipalities or utilities buying the same
capability; requirements spreading from one Member State into others.

**Lead time:** 3 to 24 months.
**Feeds:** sizing, account targeting, pricing corridors, partner
strategy, product requirements, roadmap timing.

### Company and financial (maps to FININT)

**Sources:** BRIS (Business Registers Interconnection System); European
e-Justice company search; national company registries; national
securities regulators and exchanges; annual accounts and ESEF-formatted
reports; insolvency registers; Beneficial Ownership Register
Interconnection System where access is legally available; European
Commission merger, antitrust, cartel, and state-aid case databases.

BRIS connects national business registers across the EU and EEA.
Connected registers may expose legal form, registered seat,
representatives, branches, mergers, and annual accounts, though depth
and cost vary by country.

**Signals:** new subsidiaries or branches in target countries;
cross-border mergers; director or legal-representative changes;
subsidiary names revealing a new product or market; state-aid awards
supporting factory expansion; merger filings exposing market
definitions and named competitors; antitrust cases exposing pricing,
channel, or exclusivity practices; insolvency among distributors,
suppliers, or customers.

### Technical, research, standards (maps to TECHINT)

**Sources:** EPO and Espacenet; EUIPO trademark and design databases;
CORDIS for EU-funded project participants, deliverables, publications,
and collaboration networks; Horizon Europe projects and consortium
announcements; CEN, CENELEC, and ETSI work programs; industry standards
organizations; Commission research and innovation dashboards;
university and research-institute project repositories.

**Signals:** competitors repeatedly appearing in funded consortia;
research partners becoming commercial partners; pilot sites indicating
likely launch customers; project deliverables becoming product
capabilities; competitors chairing standards committees; trademark
filings following project completion; consortium members later
appearing in acquisitions or partnerships; patent, standards, and
Horizon activity converging on one technology.

**Lead time:** 12 to 48 months for research and standards; 6 to 18
months for commercialization signals.

### Market, trade, supply (maps to GEOINT/DEMOINT and MASINT)

**Sources:** Eurostat; Eurostat COMEXT and international trade
statistics; Access2Markets; TARIC; PRODCOM manufacturing statistics;
ECB data; national statistical institutes; European Environment Agency
industrial datasets; EU customs, trade-defence, anti-dumping, and
safeguard proceedings.

**Signals:** imports growing faster than domestic production; new
anti-dumping or countervailing investigations; tariff changes altering
competitor economics; country-level manufacturing output diverging;
competitors changing country of origin or assembly location; sudden
movement in product-specific trade codes; local production increasing
before a commercial announcement; rules-of-origin changes affecting
supplier selection; customs classifications revealing a product's
physical configuration.

**Lead time:** 3 to 24 months.

### Regulatory, certification, trust (maps to MASINT)

**Sources:** EUR-Lex; Commission "Have Your Say" consultations;
national regulator consultations; NANDO notified-body database; Safety
Gate; European Chemicals Agency databases; ENISA and national
cybersecurity authorities; sector regulatory databases; product
certification, withdrawal, suspension, and recall notices.

**Signals:** competitors selecting a notified body for a new product
category; new conformity-assessment capacity appearing in a market;
proposed regulations naming technologies or risk classes; consultation
submissions revealing industry positions; recalls or repeated
safety-alert patterns; certification suspensions; competitors lobbying
for exceptions or transition periods; new cybersecurity or
environmental requirements appearing in procurement language.

**Lead time:** 6 to 36 months.
**Feeds:** regulatory roadmap, compliance differentiation, trust
positioning, product architecture, market-entry timing.

---

## MENA Overlay

MENA is not one disclosure environment. The GCC, Levant, and North
Africa differ substantially in language, procurement structure,
company-data accessibility, state ownership, regulatory publication,
and digital maturity.

**Instantiate at country level.** At minimum specify: GCC, Levant, or
North Africa; the individual countries; Arabic, English, or French
research requirements; public-sector, state-owned enterprise, or
private-sector buyer; local-content requirements; development-bank or
sovereign funding involvement.

### Regional sources (use before country portals)

**Economic and market data:** GCC-Stat and its Marsa Data Portal for
GCC population, GDP, trade, energy, tourism, and labor indicators, with
links to national statistical agencies; Arab Development Portal and
ESCWA data; Arab Monetary Fund datasets; World Bank Data and Enterprise
Surveys; IMF country reports; SESRIC statistics; UN Comtrade and ITC
Trade Map; national statistics authorities.

**Development-funded procurement:** Islamic Development Bank project
procurement; World Bank procurement notices; EBRD Client
e-Procurement Portal (ECEPP); United Nations Global Marketplace;
African Development Bank procurement for North Africa; European
Investment Bank and EU external-action tenders; country development and
sovereign funds.

**Signals:** development projects entering procurement planning;
expressions of interest preceding major tenders; funding approvals
identifying future buying authorities; environmental and social
assessments revealing equipment requirements; consultant contracts
preceding major systems procurement; repeated project-financing
partners; procurement packages split into civil works, equipment,
software, and operations; awards that establish an incumbent for later
phases.

### GCC and Levant procurement

| Country | Primary official source | Useful intelligence |
|---|---|---|
| Saudi Arabia | Etimad | Active and awarded competitions, tender documents, supplier requirements, framework agreements |
| United Arab Emirates | Ministry of Finance Digital Procurement Platform | Federal tenders, awards, supplier participation, framework activity |
| Qatar | Monaqasat | Active, future, opened, awarded, cancelled, closed government tenders |
| Oman | Tender Board e-Tendering / ESNAD | Tenders, awards, supplier classifications, purchasing categories, local-content requirements |
| Bahrain | Tender Board and eTendering | Published tenders, opened bids, award reports, buyer activity |
| Kuwait | Central Agency for Public Tenders | Central-government tenders, archives, supplier registration, awards |
| Jordan | JONEPS | Procurement plans, invitations, prequalification, expressions of interest, tenders and awards |

### North Africa procurement

| Country | Primary official source | Useful intelligence |
|---|---|---|
| Egypt | EONEPS | Procurement announcements, supplier registration, catalogs, procurement law, entity notices |
| Morocco | Portail des Marches Publics | Public tenders, buyer notices, results, awards, documentation |
| Tunisia | TUNEPS | Procurement plans, tenders, evaluations, awards, contracts, consultations, supplier participation |
| Algeria | Electronic Public Procurement Portal | Public procurement notices and electronic tender information |

### Financial and company

**Sources:** national stock exchanges and securities regulators;
prospectus and listed-company disclosure databases; commercial
registries; central-bank publications; national statistics authorities;
sovereign wealth fund reports and portfolio announcements; ministries of
finance, economy, investment, industry, energy, planning; economic-city,
industrial-zone, and free-zone registries; state-owned enterprise annual
reports; public-private partnership pipelines.

For GCC sizing, start with GCC-Stat then move to national sources:
GASTAT (Saudi Arabia), Federal Competitiveness and Statistics Centre
(UAE), National Planning Council (Qatar), NCSI (Oman), Information and
eGovernment Authority (Bahrain), Central Statistical Bureau (Kuwait).
For North Africa: CAPMAS (Egypt), High Commission for Planning
(Morocco), National Institute of Statistics (Tunisia), National Office
of Statistics (Algeria).

**Signals:** sovereign funds establishing a new portfolio company;
government ownership consolidated or reduced; capital injections into
state-owned enterprises; prospectuses naming government projects or
anchor customers; new industrial licenses; free-zone registrations;
foreign-ownership rules changing; PPP pipelines expanding; national
development strategies moving from policy language into funded programs;
diversification spending shifting between sectors.

### Ecosystem and localization

In MENA markets, competitive advantage may depend as much on local
presence and state alignment as on product capability.

**Sources:** local-content authorities and procurement rules; national
industrial-development programs; in-country value and localization
scorecards; approved vendor lists; distributor and system-integrator
registries; chambers of commerce; economic zone and industrial-city
directories; sovereign wealth fund portfolios; national technology and
manufacturing programs; government-backed accelerators; utility, oil and
gas, mining, infrastructure, and transport vendor-registration systems.

**Signals:** local-content scoring added to tender evaluations;
competitors establishing regional headquarters; local assembly or
manufacturing announcements; joint ventures with government-related
entities; new certified distributors; technology-transfer commitments;
training academies launched with public institutions; competitors
joining national industrial programs; sovereign funds backing a
competitor, customer, supplier, or channel partner; procurement
eligibility becoming dependent on local registration or classification.

### Facility and project

**Sources:** industrial-city and economic-zone announcements;
environmental permits; utility-connection approvals; construction and
municipal permits; port and free-zone tenant announcements; PPP
pipelines; ministries of industry, energy, mining, transport, housing,
infrastructure; national oil, water, power, rail, and logistics
companies; satellite imagery; development-bank environmental and social
documents; engineering, procurement, and construction contract awards.

**Signals:** land allocation before construction; power or water
capacity reserved for a facility; engineering-design contracts preceding
equipment procurement; environmental assessment before project approval;
port or rail connectivity expanding; new industrial tenants entering an
economic zone; local fabrication or assembly requirements; contractor
mobilization before an official launch; utilities publishing
future-project lists; large projects divided into successive procurement
packages.

**Lead time:** 6 to 36 months.

### MENA research guardrails

- Search in **Arabic and English** across the GCC and Levant. Search in
  **Arabic and French** across much of North Africa.
- Do not assume the English version of a portal contains every notice.
- Treat government strategy announcements as intent until funding,
  procurement, land, permits, hiring, or contracts corroborate them.
- Distinguish the government, the sovereign fund, the state-owned
  enterprise, the regulator, and a royal or executive initiative. They
  signal different levels of commitment.
- Watch local-content and vendor-registration requirements. A strong
  product that cannot qualify to bid is not currently a competitor.
- Record whether an amount is an announced budget, an approved budget,
  committed financing, a tender value, or an awarded contract value.
  Those are five different numbers wearing the same headline.
- Expect inconsistent identifiers and transliterations. Search Arabic,
  English, French, abbreviations, former names, and parent-company
  names.
- Archive source documents. Regional portals restructure, replace files,
  and offer limited historical search.
- Cross-check headline megaproject claims against procurement,
  contractor awards, development-bank documents, permits, and facility
  activity.

---

## Building a New Overlay

APAC, LATAM, and Sub-Saharan Africa follow the same pattern. To build
one, find and document six things per country:

1. **Procurement platform** -- and whether below-threshold buying
   happens elsewhere
2. **Company registry** -- and what it actually exposes versus charges
   for
3. **Statistics bureau** -- establishment counts, occupations, wages,
   trade codes
4. **Standards and regulatory databases** -- what gates entry, and the
   certification lead time
5. **Language requirements** -- which languages the primary sources
   publish in, and whether the English version is complete
6. **The local evidentiary burden** -- what class of announcement is
   routinely made and routinely not funded, and which source class
   corroborates commitment

That sixth item is the one people skip and the one that determines
whether the overlay is useful. Every market has a characteristic gap
between what gets announced and what gets built. Name it explicitly.
