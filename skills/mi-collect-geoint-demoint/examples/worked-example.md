# Worked Example: A Denominator With Its Vintage Showing

**Synthetic teaching case.** Every establishment count, occupation figure, wage number, and analyst estimate below is invented for teaching. The source *types* are real; the numbers are not. Nothing here should be cited as a fact about any market.

**Decision supported:** Whether to fund a German market entry next fiscal year.
**Decision horizon:** 18 months.
**Countries in scope:** United States, Germany.

## Code Selection (disclosed, not assumed)

| Code | System | Description | Over-captures | Under-captures |
|---|---|---|---|---|
| 541511 | NAICS | Custom computer programming services | Agencies and consultancies that would never buy tooling | Software vendors classified as publishers |
| 511210 | NAICS | Software publishers | Consumer software, games, embedded | Our buyers who sit inside non-software companies |
| 62.01 | NACE | Computer programming activities | Same over-capture as 541511 | Same |

**Why these codes:** Our buyer is a revenue-operations function, which no statistical system counts directly. These codes capture the *industries where that function is dense*, which is the closest available proxy. This is an analyst judgment, and a different analyst could defensibly choose 5415 at the four-digit level and land three times higher.

**Overlap handling:** Establishments reporting under both 541511 and 511210 were deduplicated using the Census enterprise-level file; 2,140 duplicates removed and the removal is recorded.

## Search Plan

- **Sweep order:** establishment counts → regional concentration → occupations and growth → wages → firmographics → title prevalence by country → trade flows (n/a, no goods) → footprint
- **Vintage window:** nothing older than 2023 accepted for the denominator, given an 18-month horizon
- **Noise filter:** US "establishment" counts locations, German figures count enterprises — these are different units and are never summed

## 1. Signal Inventory (excerpt)

| Signal | Source (URL, published) | **Vintage** | Label | Inference chain | Feeds |
|---|---|---|---|---|---|
| US establishments, 541511 + 511210, 50-999 employees: 38,400 after dedup | `example.invalid/cbp`, published 2026-04 | **2024** | Fact | The eligible denominator | TAM |
| German enterprises, NACE 62.01, 50-999 employees: 6,900 | `example.invalid/destatis`, published 2026-02 | **2023** | Fact | German denominator — one year staler than the US figure | TAM |
| US occupation count, revenue/sales operations analysts: 214,000, +7% over 3 years | `example.invalid/bls`, published 2026-05 | **2025** | Fact | The buying population is growing | ICP, Persona |
| German equivalent occupation: no distinct classification exists | `example.invalid/destatis-occ`, published 2026-02 | **2023** | Fact | The role is not counted separately, which is itself a finding | Persona |
| US median wage, that occupation: $98,400, +11% over 3 years | `example.invalid/bls-wage`, published 2026-05 | **2025** | Fact | WTP ceiling rising | Pricing |
| Regional concentration: 41% of eligible US establishments in 5 metro areas | `example.invalid/cbp-metro`, published 2026-04 | **2024** | Fact | Where SOM lives and where field sales should live | Go-to-market |

**Stale flags:** The German enterprise count carries a **2023** vintage against an 18-month decision horizon reaching into 2028. It is the oldest figure in the set and the one the entry decision most depends on. Treated as a Fact about 2023 and an Assumption about 2027.

## 2. The Denominator

| Country | Code | Size band | Establishments | Vintage | Source |
|---|---|---|---|---|---|
| US | 541511 + 511210 | 50-999 | 38,400 (after removing 2,140 duplicates) | 2024 | `example.invalid/cbp` |
| Germany | NACE 62.01 | 50-999 | 6,900 | 2023 | `example.invalid/destatis` |

**Denominator total:** Not stated as a single number. US counts *establishments* (locations); Germany counts *enterprises* (legal entities). Summing them would produce a figure that means nothing, and the temptation to do it is exactly why the units are named in the table.

## 3. Regional Concentration

| Region | Share of establishments | Vintage | Read |
|---|---|---|---|
| Top 5 US metros | 41% | 2024 | Field sales concentrates here; the long tail is a digital motion |
| Bavaria + NRW | 48% of German enterprises | 2023 | A German entry is effectively a two-region entry |

## 4. The Buying Population

| Role | Country | Occupation count | Growth | Median wage | Vintage | Read |
|---|---|---|---|---|---|---|
| Revenue/sales operations analyst | US | 214,000 | +7% / 3 yr | $98,400 | 2025 | Population growing; wage growth outpacing inflation, so budgets are expanding |
| Nearest equivalent | Germany | Not separately classified | — | — | 2023 | **The role is not counted.** See title prevalence below. |

**Wage-based pricing corridor:** A tool used by this role, priced at roughly 2-4% of loaded salary, supports $200-400 per seat per month in the US. *The 2-4% ratio is an Assumption* drawn from category convention, not from any statistic here, and it is labeled as such because it is doing quiet load-bearing work.

## 5. Buyer-Title Prevalence by Country

| Country | Equivalent title | Prevalence | Source | Read |
|---|---|---|---|---|
| US | VP / Director of Revenue Operations | Common; distinct occupation code | `example.invalid/bls` | Persona holds as written |
| Germany | "Leiter Vertriebssteuerung" or the duties folded into Controlling | No distinct classification; duties distributed across finance and sales leadership | `example.invalid/destatis-occ` | **Persona does not survive the border.** Messaging aimed at a VP RevOps will land on nobody. |

This row is the most consequential finding in the sweep, and it came from noticing an *absence* in an occupation table.

## 6. Firmographics and ICP Boundaries

| Dimension | Distribution | Vintage | ICP boundary it supports |
|---|---|---|---|
| Size band | 61% of eligible establishments at 50-249 employees | 2024 | ICP floor at 50, not 100 — the mass is below where we currently target |
| Legal form (DE) | 72% GmbH | 2023 | Contracting and invoicing requirements for entry |
| Sector | 34% outside software, in finance and logistics | 2024 | Our ICP excludes them today; the data says that is a choice, not a constraint |

## 7. Trade Flows

Not applicable. No physical product codes.

## 8. Conflicting Estimates

| Estimate | Source | Vintage | Method | Difference |
|---|---|---|---|---|
| $4.1B global market | Analyst A | 2025 | Top-down, method undisclosed | — |
| $12.6B global market | Analyst B | 2025 | Top-down, includes adjacent CRM tooling | **3.1x** |

**What explains the gap:** category definition. Analyst B folds in adjacent CRM functionality that our product does not replace. Both are reported. Neither is adopted, and neither is averaged — averaging would produce $8.35B, a number nobody can defend and that describes no market.

## 9. Watch Items

- German enterprise counts — the 2024 release is due next spring and will close the vintage gap
- US occupation growth — a second consecutive release showing +7% would make the population trend durable

## 10. Collection Gaps and Handoffs

> **No signal found.** No statistical system counts "revenue operations" as an occupation in Germany. Sources swept: Destatis occupational classification, Eurostat occupation tables, federal employment agency categories. What the absence suggests: the function exists but is distributed rather than titled, which changes the entry motion from "find the VP RevOps" to "find where these duties sit." What would close it: nothing statistical. A dozen buyer interviews would close it in a fortnight.

> **Vintage gap.** The German denominator is a year staler than the US one. Not fatal, but it must be stated wherever the two are compared.

- **Handoffs:** denominator → `mi-size-tam-sam-som`; capture rate → `mi-collect-finint`; the persona finding → `mi-mine-voice-of-customer` for German-language sources

## Assumptions to Validate

1. **The code selection is the biggest lever in this document.** A four-digit selection would land roughly 3x higher. Everything downstream inherits this judgment, and it is a judgment.
2. **The 2-4% of loaded salary pricing heuristic** is convention, not evidence. It is the only number here with no statistical source.
3. **The German 2023 vintage is treated as approximately current.** If German enterprise formation moved sharply in 2024-25, the entry case moves with it.

This sweep produces the denominator. It does not produce a TAM, a SAM, or a SOM, and it deliberately declines to combine two incompatible units into a single headline number.

## Final Step

1. Take this denominator into sizing (Recommended)
2. Widen the code selection to four-digit and re-count, so the 3x lever is visible in the model
3. Schedule an annual refresh, since sizing rot is slow but real
4. Turn the firmographic distribution into revised ICP boundaries

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
