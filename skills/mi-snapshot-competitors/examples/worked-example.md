# Worked Example: Three Columns, One of Them Guesswork

**Synthetic teaching case.** Cartelane, Meridian, and Northwind are fictional, and every price, feature, date, and quote below is invented for teaching. Nothing here is a claim about a real vendor.

**Decision supported:** Refresh the battle card and set up a quarterly watch.
**Buyer:** VP RevOps, with Finance running the evaluation.
**Prior snapshot:** First run — this is the baseline.

## Competitor Selection

- **Profiled:** Cartelane, Meridian, Northwind
- **Selection rule:** appearance in lost-deal notes over the last three quarters. Cartelane 7, Meridian 4, Northwind 3.
- **Considered and excluded:** Two larger enterprise vendors with more revenue and more brand, appearing in **zero** of our lost deals. Also excluded: a well-funded entrant that sales has heard of and never competed against.

The excluded pair is the important line. They are the two companies leadership names when asked who our competitors are, and neither has taken a deal from us. Profiling them would have been a quarter spent watching the wrong door.

## Profiles

### Cartelane

| Item | Detail | Source (URL, date) | Label |
|---|---|---|---|
| What they sell | Revenue ops platform, integration-led | `example.invalid/cartelane`, 2026-08-18 | Fact |
| To whom | Mid-market, 100-1,000 employees | `example.invalid/customers`, 2026-08-18 | Fact |
| Positioning in their own words | "One system of record for revenue" | `example.invalid/home`, 2026-08-18 | Fact (about their marketing) |
| Pricing posture | Published; floor $119/user/mo since removing a $49 tier this quarter | `example.invalid/pricing`, 2026-08-18 vs archive 2026-05-14 | Fact |
| Notable strengths | Implementation speed — 7 of 19 reviews, unprompted | `example.invalid/g2`, 2026-08 | Fact |
| Notable exposure | Connector reliability — 14 of 31 reviews mention it | same | Fact |
| Last material thing | Removed the entry tier, raised the floor 144% | `example.invalid/pricing`, 2026-08-18 | Fact |

### Meridian

| Item | Detail | Source (URL, date) | Label |
|---|---|---|---|
| What they sell | Revenue systems, enterprise-down | `example.invalid/meridian`, 2026-08-18 | Fact |
| To whom | Enterprise finance; mid-market via a lighter SKU | 10-K FY2026 segment note | Fact |
| Positioning in their own words | "Balanced growth across all segments" | Q3 FY2026 call | Fact (about their narrative) |
| Pricing posture | Not published; "contact us" only | `example.invalid/meridian-pricing` | Fact |
| Notable strengths | Public-sector footprint; a scope-expanding federal award through 2029 | `example.invalid/usaspending`, 2026-05-30 | Fact |
| Notable exposure | Deferred revenue +4% against revenue +19% | 10-K FY2026 | Fact (audited) |
| Last material thing | Split Public Sector out as its own reporting segment | 10-K FY2026, 2026-02-18 | Fact |

### Northwind

| Item | Detail | Source (URL, date) | Label |
|---|---|---|---|
| What they sell | Forecasting-first tooling | `example.invalid/northwind`, 2026-08-18 | Fact |
| To whom | Sales leadership, not finance | `example.invalid/home` | Inference — inferred from site language and case studies, not stated |
| Positioning in their own words | "Forecast you can defend" | same | Fact |
| Pricing posture | Unknown. No published pricing, private company, no filings | swept 2026-08-18 | **Assumption** — no evidence either way |
| Notable strengths | Forecast accuracy claims, uncorroborated | `example.invalid/northwind-claims` | Assumption |
| Notable exposure | Unknown | — | Assumption |
| Last material thing | Unclear; no announcements in 14 months | `example.invalid/newsroom` | Inference — silence, not absence |

Northwind's profile is mostly unknowns, and it is presented that way rather than filled in. That honesty is what the evidence-quality row below makes visible.

## Comparison Matrix

**Rows derived from:** the evaluation criteria appearing in four RFPs we have seen this year, plus the questions Finance asked in three discovery calls. Not from our feature list.

| Buyer dimension | Us | Cartelane | Meridian | Northwind | Source of the dimension |
|---|---|---|---|---|---|
| Time to first reconciled report | 6 weeks | **3 weeks** | 14 weeks | Unknown | RFP criterion, 4 of 4 |
| Native ERP connectors | 2 | 0 today, 11 endpoints staged | 9 | 0 | RFP criterion, 3 of 4 |
| Finance-side audit trail | Full | Partial | **Full, certified** | None | Finance discovery Q, 3 of 3 |
| Published pricing | Yes | Yes | No | No | Buyer forum language, 6 posts |
| SOC 2 Type II | Yes | In process | **Yes** | Unknown | RFP criterion, 4 of 4 |

We do not win the first row, and Meridian beats us on two. That is what a matrix built from buyer criteria looks like — the version built from our feature list had us winning five of five, and a rep who believed it would have walked into the implementation-speed question unprepared.

### Evidence Quality (required row)

| | Us | Cartelane | Meridian | Northwind |
|---|---|---|---|---|
| Sourcing behind this column | Documented | Documented | Documented (audited filings) | **Guessed** |
| Oldest claim in this column | 2026-08 | 2026-08 | 2026-02 (10-K) | 2025-06 |

Northwind's column is guesswork and says so. Without this row, three cells of "Unknown" sitting beside two columns of filings and pricing pages would read as parity, and a rep would treat a company we know nothing about as a company that has nothing.

## So What (counted)

**Three implications:**

1. Cartelane will beat us on implementation speed until our onboarding changes — it is an RFP criterion in every deal and they are twice as fast.
2. Meridian is not a mid-market threat today, but the segment split plus the federal award means their attention is elsewhere, which is a window rather than a threat.
3. Northwind is unknown, and "unknown" is not "harmless." Three lost deals mentioned them.

**Two risks:**

1. Cartelane's eleven staged endpoints close the connector gap within two quarters, and the matrix flips on the second row.
2. Our SOC 2 advantage over Cartelane disappears when their in-process certification completes.

**Two opportunities:**

1. Cartelane just vacated the sub-$119 segment; their former Starter customers are addressable now with a named list.
2. Their connector-reliability complaints are the ground they are about to claim — a maturity play, cited, before their launch.

**Three assumptions to validate:**

1. **Northwind's column is guesswork.** They appeared in three lost deals and we cannot say what they sell to whom. This is the largest gap in the document.
2. Implementation-speed reviews are self-reported by customers who completed implementation. Failed implementations do not leave reviews.
3. Meridian's mid-market SKU is inferred from a segment note, not from a product page.

## Collection Gaps

> **No signal found.** Northwind pricing, customer count, funding, and headcount could not be established. Sources swept: their site and docs, three funding databases, two review platforms, state incorporation records. What the absence suggests: a small private company that does not court press — which is consistent with appearing in only three deals but says nothing about whether they win them. What would close it: win/loss interviews from those three deals, which would cost an afternoon and close most of this column.

## Storage

Stored as `revops-tooling-snapshot-2026-08-18.md`. Schema stable. The next run diffs against this file.

## Final Step

1. Turn this into a battle card, with Northwind explicitly marked as unknown (Recommended)
2. Set up the quarterly watch that diffs against this baseline
3. Run win/loss on the three Northwind deals — it is the cheapest fix to the biggest gap
4. Take the matrix into positioning

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
