# Sweep Playbooks

How to actually run collection. `disciplines.md` says what exists;
this says what order to touch it in, what you are forbidden to invent,
and where each sweep hands off.

A sweep collects and labels. It does not render a verdict. Confidence
rating across disciplines belongs to `fusion.md`.

---

## Section 0: Identity and Perimeter (every sweep, always first)

Establish what you are researching before researching it. One short
block. Errors here poison everything below.

- Legal entity name and any trading names
- Headquarters and material locations
- Ownership status: public, private, PE-held, subsidiary, state-linked
- Tickers, exchanges, filing jurisdictions
- Founding year
- Major brands and subsidiaries
- Same-name confusions to avoid, named explicitly

Then state the noise filter you will apply: how you will avoid
same-name companies, acquisitions that closed years ago, and press
releases recycled by aggregators into what looks like three sources.

---

## The Full-Spectrum Sweep

For when a company suddenly matters and there is one sitting to get
smart. All seven disciplines at collection-floor depth, fused, ending
in a call-ready brief.

**Fixed order.** Do not reorder because one channel looks juicier.
Coverage you can defend beats whatever the search engine served first.

1. Identity and perimeter
2. OSINT -- the public record
3. FININT -- money and commitment
4. TECHINT -- what they have actually built
5. HUMINT -- people and intent
6. GEOINT/DEMOINT -- terrain and population
7. SIGINT -- emissions and digital exhaust
8. MASINT -- measurable signatures
9. Fusion with confidence stacking
10. Call-ready brief
11. Collection gaps

Announce each discipline as it starts. Keep its findings in its own
section so a reader can see which channel produced which claim, and
challenge one link instead of dismissing the whole brief.

**Depth settings**

| Depth | Per discipline | Fits |
|---|---|---|
| Rapid | Highest-value pass only. Enough to hold a conversation without embarrassing yourself. | A coffee break |
| Standard | The collection floor. The default. | An hour or two |
| Deep | Extended sweeps, more inference chains, more sourcing per claim. | A research afternoon |

**When to use something else instead**

- Maximum rigor on one discipline: run that single sweep, not this.
- The subject is a market or category, not a company: landscape scan,
  sizing, or forces analysis answer different questions.
- You already hold recent sweeps and only need them reconciled: that is
  fusion, not collection.
- The company is pre-public, pre-product, pre-press: most disciplines
  return nothing and the honest output is a short list of what cannot
  be known yet.

Output schema: `output-schemas.md`, full-spectrum brief.

---

## Single-Discipline Sweeps

Each follows the same shape. Search plan, ordered sweep, signal
inventory, ranked inference chains, watch items, gaps and handoffs.
Cap inference chains at 5 in Just Enough Mode.

### OSINT sweep

**Order:** newsroom and press -> analyst coverage and briefing chatter
-> exec and company social -> review-site clusters on the [BUYER]'s
sites -> conference and webinar footprint -> prediction markets where a
regulation or milestone gates [MARKET].

**Do not invent:** press quotes, analyst ratings, review counts, event
sponsorships, market odds.

**Signature output:** the say versus said-about gap. Their positioning
language minus their customers' language. That gap is the exposed
flank.

**Handoffs:** review clusters -> voice-of-customer mining. Whole market
-> landscape scan. Next run -> watch diff.

### FININT sweep

**Order:** latest annual and quarterly filings (Risk Factors first,
diffed against last year) -> segment reporting structure -> earnings
call Q&A, specifically the dodges -> funding, debt, ownership structure
-> entity and subsidiary registrations in [GEOGRAPHY] -> procurement
awards and contract modifications -> competition and state-aid cases.

**Do not invent:** revenue, funding amounts, margins, deferred revenue,
customer counts, contract values, executive quotes from calls.

**Signature output:** what the money says versus what the press release
says. Money is the least deniable signal a company emits.

**Handoffs:** capture rates -> TAM/SAM/SOM. Executive language shifts
-> earnings signal refresh on a quarterly diff.

### TECHINT sweep

**Order:** patent search by assignee and classification, looking for
clusters -> inventor names repeating -> trademark filings -> public
changelogs, release notes, and deprecations -> API documentation diffs
-> repo and SDK activity -> standards committee participation ->
funded research consortia -> preprints and conference papers by
affiliated authors.

**Do not invent:** patent numbers, application dates, classifications,
inventor names, paper titles, repo names, endpoint names.

**Required column: Lead time.** Date every signal and state its typical
lead time (patents 12 to 18 months, trademarks 6 to 12, preprints 6 to
24, consortia 12 to 48, API endpoints weeks). A roadmap implication
without a clock is a direction without a deadline.

**Signature output:** what they are building versus what they are
shipping. Deprecations are especially informative, because they say
what a company has given up on.

**Handoffs:** technographics -> SAM refinement. Feature gaps -> battle
card countdown clocks. Paired with HUMINT hiring -> the strongest
fusion signal available.

### HUMINT sweep

**Order:** leadership roster and prior playbooks -> open roles by
function and geography, counted against a baseline -> departures and
tenure concentration -> employee sentiment themes -> public statements
in interviews, talks, podcasts -> your own win/loss and churn debriefs.

**Do not invent:** headcounts, posting counts, names, tenure dates,
quotes from reviews or interviews.

**Signature output:** a job posting is a roadmap with a salary band.
Executives repeat their last playbook more often than they invent a new
one.

**Required output: win/loss framing.** Public HUMINT infers why deals
move. Only your team's interviews know. So every HUMINT sweep ends by
generating 3 to 5 questions for the next win/loss and churned-customer
interviews, each tied to a specific signal this sweep collected. Then
emit the flag:

> **Gap flag for fusion:** win/loss unverified as of this run. Weight
> org-instability and build-signal stories accordingly.

**Handoffs:** win/loss is ground truth. If the sweep and the interviews
disagree, the interviews win.

### GEOINT/DEMOINT sweep

**Order:** establishment counts by industry code and employee band ->
regional concentration -> occupation counts and growth for the [BUYER]
and end-user roles -> wage trends in those roles -> firmographic
distributions -> buyer-title prevalence by country -> trade flows in
product-specific codes -> [TARGET]'s own physical footprint and
regions served.

**Do not invent:** establishment counts, occupation counts, wage
figures, trade volumes, market size numbers. If two analyst reports
disagree by 3x, report both and say so.

**Required column: vintage.** Name the statistical vintage of every
dataset, not just its publication date, and flag anything older than
the decision's horizon. A 2019 establishment count answering a 2026
sizing question is a Fact about 2019 and an Assumption about now.

**Signature output:** the denominator. Everything sized without it is
a vibe with a dollar sign.

**Handoffs:** TAM/SAM/SOM recipe. ICP boundaries. Persona
localization. Pricing corridors.

### SIGINT sweep

**Order:** pricing page against its last snapshot -> site and messaging
diffs via Wayback -> documentation and status page history -> new SSL
certs and subdomains -> app store metadata and version notes -> SEM and
SEO term movement, including bids on your brand -> job posting deltas
since the last observable window -> certifications listed.

**Do not invent:** prices, tier names, cert issue dates, subdomains,
app versions, keyword rankings, outage dates.

**Required column: before -> after.** A change without a before-state is
an observation, not a diff. If you cannot establish the prior state, say
so and log it as a baseline capture rather than a change.

**Signature output:** the freshest layer. This is what keeps battle
cards from going stale.

**Handoffs:** pricing tracker for the time series. Watch report for the
diff. Positioning counter-moves.

### MASINT sweep

**Order:** scale proxies (app store ranks, review velocity, community
size, support forum volume, integration counts, package download
counts) -> trend direction on each with the window stated -> supply
chain and import/export records where physical goods exist ->
facilities, permits, land, utility connections -> certification and
notified-body registries -> ops capacity via status pages and support
response sampling -> anomalies with candidate explanations.

**Do not invent:** volumes, download counts, review velocity, permit
records, certification dates, incident dates.

**Required column: disambiguate via.** Every anomaly names the
discipline that would resolve it. A MASINT signal without a
disambiguation path is a Rorschach test, not intelligence: input volume
up 20% is pre-launch buildup or demand collapse, and only FININT or
HUMINT tells you which.

**Signature output:** anomalies. Abnormal resource allocation never
lies, but it does not explain itself either.

**Handoffs:** threat assessment. Launch prediction. Capacity-stretch
objections for battle cards.

---

## Gap Language

A discipline that returns nothing gets one line, not padding.

> **No signal found.** [Discipline] returned nothing on [what was
> sought]. Sources swept: [list]. What the absence itself suggests:
> [read]. What would close it: [the specific filing, registry,
> conversation, or deep sweep].

Empty sections are findings. A private company with no filings is
telling you something about how much you will ever know via FININT. A
software company with no supply chain is not a MASINT failure; it is a
reason to substitute ops capacity signals.

Never write "no information available" and move on. Say what you swept.

---

## The Bulk Drop

If the user pastes what they already have, do not re-collect it.

1. Extract every signal into the inventory schema.
2. Account for it: found in the paste, inferred from the paste, still
   missing.
3. Ask only about the gaps, within the 3-question budget.
4. Tag pasted signals with their provenance. A signal whose source you
   cannot check is an Assumption, no matter how confidently it was
   pasted.

---

## Anti-Patterns Specific to Collection

- Reordering the sweep because one channel looked more interesting.
  The order is the defensibility.
- Counting a press release and its three coverage articles as four
  signals.
- Treating the company's own product page as a Fact about the market.
- Letting a single vivid find set the confidence level for the run.
- Padding an empty discipline so the document looks symmetrical.
- Collecting past the point where the [DECISION] would change. Stop
  when the answer stops moving.
