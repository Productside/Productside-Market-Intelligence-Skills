# Worked Example: Ninety Minutes Before a Partner Call

**Synthetic teaching case.** "Halvard Systems" is fictional, and every figure, date, and source below is invented for teaching. Nothing here is a claim about a real company. The shape of the brief is what to copy.

**Prepared for:** A reseller-agreement call at 4pm today.
**Depth:** Standard. **Relationship:** Partner (not competitor — this changes the whole hour).
**Prior sweep:** First run.

## Search Plan

- **Identity:** Halvard Systems Ltd (UK), trading as Halvard; excluding Halvard Marine (unrelated Norwegian shipping firm) and "Halyard Systems," a US medical supplier that dominates the search results
- **Sweep order:** OSINT → FININT → TECHINT → HUMINT → GEOINT/DEMOINT → SIGINT → MASINT → fusion → brief
- **Date window:** 24 months; filings back three years
- **Noise filter:** the 2024 acquisition has been re-reported three times and will be collapsed to one origin

## 0. Identity and Perimeter

| Item | Value |
|---|---|
| Legal entity | Halvard Systems Ltd (England and Wales) |
| HQ | Manchester; second office Dublin |
| Ownership | Private, PE-held since 2024 (majority) |
| Filings | Companies House; no listed securities |
| Founded | 2016 |
| Brands and subsidiaries | Halvard Connect; Halvard Systems Ireland Ltd |
| **Same-name confusions excluded** | Halvard Marine AS (Norwegian shipping); "Halyard Systems" (US medical supplier — dominates search, unrelated) |

The "Halyard" collision cost one line here. Left unnamed, roughly a third of the OSINT results would have been about surgical drapes.

## 1. OSINT — The Public Record

| Signal | Source (URL, date) | Label |
|---|---|---|
| Positioning: "the integration layer for regulated industries" | `example.invalid/halvard-home`, 2026-08-18 | Fact (a claim, not a market fact) |
| G2 reviews cluster on implementation speed, positively (11 of 19) | `example.invalid/g2`, 2026-08-18 | Fact |
| Two reviews cite support responsiveness negatively; isolated, not a cluster | same | Fact |
| PE acquisition announced 2024, re-reported 2024, 2025, 2026 | `example.invalid/newsroom`, 2024-09-11 | Fact — **one origin, three appearances** |

## 2. FININT — Money and Commitment

| Signal | Source (URL, date) | Label |
|---|---|---|
| Companies House: turnover £31M FY2025, up from £24M | `example.invalid/ch-accounts`, filed 2026-03 | Fact (audited, abridged) |
| PE majority holder disclosed; no debt covenant detail in abridged accounts | same | Fact |
| Irish subsidiary incorporated 2025-11, no accounts filed yet | `example.invalid/cro`, 2025-11 | Fact |

## 3. TECHINT — What They Have Actually Built

| Signal | Source (URL, date) | Label |
|---|---|---|
| Public API documented, 60+ endpoints, changelog updated 14x in 12 months | `example.invalid/halvard-api`, 2026-08-12 | Fact |
| No patent filings under any name variant | `example.invalid/patents`, searched 2026-08-18 | Fact |
| SDKs published for three languages; one deprecated 2026-05 | `example.invalid/repo`, 2026-08 | Fact |

## 4. HUMINT — People and Intent

| Signal | Source (URL, date) | Label |
|---|---|---|
| 14 open roles, 9 in solutions and implementation, against a baseline of 11 total | `example.invalid/careers`, 2026-08-15 | Fact |
| CEO and CTO both founders, still in post | `example.invalid/leadership`, 2026-08-18 | Fact |
| No senior departures in the window | same | Fact |

## 5. GEOINT/DEMOINT — Terrain and Population

| Signal | Source (URL, date) | Label |
|---|---|---|
| Customers named publicly: 21, of which 18 UK, 2 IE, 1 NL | `example.invalid/customers`, 2026-08-18 | Fact |
| No presence in our two largest markets | derived from the above | Inference |

## 6. SIGINT — Emissions and Digital Exhaust

| Signal | Source (URL, date) | Label |
|---|---|---|
| Pricing not published; "contact us" only | `example.invalid/pricing`, 2026-08-18 | Fact |
| Homepage messaging unchanged in 14 months (archive) | `example.invalid/archive`, snapshots 2025-06, 2026-01, 2026-08 | Fact |
| No bidding on our brand terms | `example.invalid/serp`, 2026-08-16 | Fact |

Messaging unchanged for fourteen months is **defended ground**, and for a partner conversation that is reassuring rather than exploitable.

## 7. MASINT — Measurable Signatures

| Signal | Source (URL, date) | Label |
|---|---|---|
| Status page: 1 incident in 12 months, minor | `example.invalid/status`, 2026-08-18 | Fact |
| ISO 27001 certified; SOC 2 not listed | `example.invalid/trust`, 2026-08-18 | Fact |

## 8. Fusion — Confidence Stacking

**Same-source collapses:** 6 apparent sources reduced to **4 independent origins**. The PE acquisition accounted for three of the six.

| # | Story | Disciplines supporting | Confidence | Commitment | So what |
|---|---|---|---|---|---|
| 1 | Services-led delivery model, not product-led | 3 — HUMINT (9 of 14 roles in implementation), OSINT (implementation-speed reviews), FININT (revenue per named customer ≈ £1.5M, implying large bespoke engagements) | **Actionable** | Built | Reseller economics: we would be selling something that needs their people. Margin and capacity both matter. |
| 2 | Preparing an EU expansion | 2 — FININT (Irish subsidiary), GEOINT (one NL customer) | **Working hypothesis** | Funded | Territory clauses in the agreement need to anticipate this. Probe on the call. |
| 3 | PE ownership may pressure pricing or exit within 2-3 years | 1 — FININT | **Watch item** | n/a | Log only. Ask about investor horizon; do not assert it. |

Three stories, not seven. A ninety-minute standard sweep on a stable private company should produce three, and the cap is a ceiling.

### Contradictions Worth Naming

- They position as "the integration layer for regulated industries," yet hold ISO 27001 and **not** SOC 2, which most regulated buyers in our markets require. Their positioning and their certification posture disagree. The certification is the harder fact.

## 9. The Call-Ready Brief

### Sixty-Second Summary

Halvard is a nine-year-old, Manchester-based, PE-backed integration vendor doing about £31M in turnover, growing roughly 30%. They sell into regulated industries in the UK and Ireland, with twenty-one named customers and an implementation-heavy delivery model — nine of their fourteen open roles are solutions and implementation, and their reviews praise implementation speed. They are stable: founders in post, no senior departures, messaging unchanged for over a year, one minor incident in twelve months. The thing that matters most for this call is that they hold ISO 27001 but not SOC 2, which our largest market's buyers generally require.

### The Three Things Worth Saying

1. Their delivery model is services-led — nine of fourteen open roles are implementation. *Evidence: careers page against baseline, plus review themes.*
2. They are almost entirely UK and Ireland today, with one Dutch customer. *Evidence: their own published customer list.*
3. They incorporated an Irish entity in November. *Evidence: Irish company register.*

Each is a Fact or a corroborated Inference. None rests on a single Assumption.

### Questions You Will Be Asked

| Likely question | Short answer | Confidence |
|---|---|---|
| Can they support our volume? | Unclear — services-led delivery scales with headcount, and they are hiring nine implementation roles now | Hedge |
| Are they financially stable? | Turnover £31M, up from £24M, audited abridged accounts | Solid |
| Do they have SOC 2? | No. ISO 27001 only, per their own trust page | Solid |
| What is the PE investor's horizon? | **I do not know.** Abridged accounts do not disclose it and I will not guess. Worth asking directly on the call. | Do not know |

The last row is required and is the most useful line in the table. Investor horizon materially affects a multi-year reseller agreement, and guessing at it in front of them would be both wrong and visibly wrong.

### Do Not Say

- **"You're planning an EU expansion."** The Irish entity supports it; nothing confirms it. Stated as fact to the people who would know, it reads as either a bad guess or unsettling surveillance.
- **"Your support is a weakness."** Two negative reviews out of nineteen is not a cluster, and this framing is competitive reflex leaking into a partner conversation.
- **"PE owners will want an exit soon."** One discipline, zero evidence about this fund's horizon, and an insult delivered as analysis.

### If They Ask What We Do Better

Omitted. The relationship is partner. A "what we do better" section in a reseller conversation is a category error, and the schema includes this section only for competitor and prospect runs.

## 10. Collection Gaps

> **No signal found.** TECHINT patents returned nothing under any name variant. Sources swept: three patent registries. What the absence suggests: their moat is delivery and domain knowledge, not intellectual property — which is consistent with the services-led story and is genuinely useful for a reseller decision. What would close it: nothing.

> **Thin by structure.** MASINT is two rows because Halvard ships no physical goods. Not a failure; a fact about which channels can ever inform on them.

> **Blocked by filing regime.** Abridged accounts under UK small-company rules disclose no segment detail, no customer concentration, and no investor terms. This is the single largest gap and it is permanent until they grow past the threshold.

- **Questions this sweep could not answer:** customer concentration, gross margin, PE investor horizon, real delivery capacity

## Assumptions to Validate

1. **Revenue per named customer (£1.5M) assumes the 21 named customers are most of their book.** If they have many unnamed smaller accounts, the "large bespoke engagements" read collapses, and with it Story 1.
2. **The Irish entity is read as EU expansion.** It could be a post-Brexit contracting vehicle for existing Irish customers, which is a completely different fact.
3. **No senior departures is read as stability.** A private company's leadership changes are not always visible.

## Storage

Stored as `halvard-systems-full-spectrum-2026-08-18.md`.

## Final Step

1. Use the brief for the 4pm call (Recommended)
2. Go deep on FININT before signing anything — customer concentration is the gap that matters
3. Schedule this as a quarterly watch during the agreement term
4. Convert the certification finding into a contract requirement

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
