# Weak Example: The Sweep Where Every Number Was Real

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It opens actual filings, cites them, dates them, labels them, and stops before rating confidence. Every individual figure in it is accurate. It would pass a quick review — and the sizing model built on it went to a board meeting.

Same fictional Meridian Revenue Systems case, swept by a different analyst.

## The Artifact

### Search Plan

- **Sweep order:** filings → earnings → funding → procurement
- **Date window:** most recent fiscal year
- **Noise filter:** standard entity disambiguation

### Filing Perimeter

| Item | Value |
|---|---|
| Legal entity | Meridian Revenue Systems, Inc. |
| Ownership | Public |
| Tickers | MRSY |

### 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| Revenue $412M, up 19% YoY | 10-K FY2026, `example.invalid/mrsy-10k`, 2026-02-18 | Fact | Strong growth trajectory | Threat assessment |
| Gross margin 74% | 10-K FY2026, same | Fact | Healthy unit economics; limited discount pressure available to them | Battle card |
| "Over 1,900 customers" | IR page, 2026-02-18 | Fact | Broad installed base | Sizing |
| Risk Factors cite competition, cloud concentration, appropriations cycles, talent retention | 10-K FY2026, same | Fact | Standard risk profile for a company at this scale | — |
| $2.1B announced public-sector modernization budget in their primary vertical | Agency press release, `example.invalid/agency-budget`, 2026-01-09 | Fact | Large addressable public-sector opportunity | Sizing |
| Analyst consensus describes them as well capitalized | `example.invalid/analyst-note`, 2026-03-02 | Fact | No near-term financial pressure | Battle card |

### 2. Strongest Inference Chains

1. **Revenue up 19% with 74% gross margin** → Inference: financially healthy and growing → no quarter-end discount pressure play available.
2. **$412M ÷ 1,900 customers = $217K ACV against a $2.1B public-sector budget** → Inference: room for roughly 9,600 more customers in that budget alone → SOM is not the constraint.
3. **Risk Factors are standard for the category** → Inference: no unusual vulnerabilities disclosed.

### Collection Gaps

- Some data was not publicly available.

## Why It Passes a Quick Read

- Real filings, opened and cited, with dates. Nothing is fabricated.
- Every figure is individually accurate — the revenue, the margin, the customer count, and the budget number are all exactly what their sources say.
- Evidence labels are present and applied consistently.
- The arithmetic in chain 2 is correct.
- It stops before rating confidence, as the discipline requires.
- It reaches a clear, quotable conclusion that a busy executive can act on.

## Why It Fails

**Chain 2 mixes an awarded reality with an announced ambition and multiplies them.** The $412M is audited revenue. The $2.1B is an *announced budget* in an agency press release — not an approved appropriation, not a committed financing, not a tender value, and certainly not an awarded contract. The sweep treats the two as the same class of number, divides one by the other, and produces "room for 9,600 more customers." That figure is now the load-bearing number in a board deck, and it rests on a press release.

*This is the commitment-ladder violation signal exactly:* a story described in committed terms on evidence that is entirely an announcement. It is hard to see because the announcement has a dollar sign on it, and dollar signs read as rigor.

**Risk Factors were quoted, not diffed.** Listing four risks and calling the profile "standard" is the failure the diff exists to prevent. In the correctly-run version of this sweep, two of those four risks were *newly added this year* and one was *removed* — and the two additions corroborate a public-sector push that this document never detects. Reading the section once makes every large company sound equally worried about the same six things, which is precisely what happened here.

**Deferred revenue was never opened.** Revenue growth of 19% is a fact about the past. Deferred revenue growth of 4% is a fact about the future, and it is in the same filing, four pages away. Chain 1 concludes "no discount pressure available to them" from the trailing number while the leading number says the opposite. A rep armed with this card will walk into a quarter-end negotiation expecting no flexibility and will be wrong.

**"Over 1,900 customers" is labeled Fact without qualification.** It is a Fact about what the IR page claims. It is unaudited, the word "over" is unbounded, and nothing establishes whether it counts free tiers, trials, or multiple entities of one buyer. Every downstream number moves with it, and it is the one figure in the table with no auditor behind it — sitting in the same column, in the same font, as the audited ones.

**Procurement was listed in the sweep order and never actually swept.** No award, no modification, no registry record appears anywhere in the inventory. The scope-expanding federal modification — the single strongest piece of *procured* evidence available on this company — is simply absent. The sweep order was written down and then not performed, and nothing in the artifact reveals that.

**"Analyst consensus" is not FININT.** A third-party opinion about capitalization is OSINT, and treating it as a financial fact imports someone else's inference as though it were a number. Worse, it agrees with chain 1, so it reads as corroboration when it is an echo.

**"Some data was not publicly available" is not gap language.** It names no channel, no source swept, and nothing that would close it. It functions as a disclaimer, not a finding.

## What Makes This Hard to Catch

Every number is real. That is the whole disguise. Reviewers checking a financial sweep look for fabricated figures, unsourced claims, and missing dates, and there are none. The failures are all failures of *category*: an announced budget filed next to audited revenue, a company-reported count filed next to an audited one, an analyst opinion filed next to a filing. The inventory schema has one Label column, and F/I/A does not distinguish these — which is exactly why the correctly-run version of this template adds a **Figure type** column.

Chain 2 is the dangerous one because it is arithmetically flawless. Nobody checks correct division. And the number it produces is large, specific, and flattering to whatever anyone wants to do next.

## Repair

Add the figure-type column and refile every row: audited, company-reported, third-party estimate, announced budget, awarded contract. Then re-derive chain 2, and watch it collapse — an announced budget cannot serve as a sizing denominator, and the denominator belongs to GEOINT/DEMOINT anyway.

Pull three years of Risk Factors and diff them. Report added, removed, and reworded separately, and follow the two additions into the segment reporting where they will meet corroborating evidence.

Open deferred revenue and set it against recognized revenue in the same chain, then rewrite the discount-pressure read. Qualify the customer count as unaudited and carry that qualification into every number derived from it.

Actually sweep procurement: USAspending, SAM.gov, and the contract modifications. Drop the analyst note from FININT and let OSINT hold it. And rewrite the gap section to name what was swept, what came back empty, and what the emptiness suggests — starting with the merger filing that does not exist, and the market definition it would have contained.
