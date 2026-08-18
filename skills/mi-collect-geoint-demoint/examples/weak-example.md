# Weak Example: The Denominator That Aged Silently

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It cites real statistical agencies, gives counts by size band, reports occupation and wage data, and produces a clean denominator a sizing model can use immediately. Every source is authoritative. It would pass a quick review — and it did, twice, before a German entry was funded on it.

Same fictional market, swept by a different analyst.

## The Artifact

### Codes Used

NAICS 541511, 511210; NACE 62.01.

### Search Plan

- **Sweep order:** establishments → occupations → wages → market size
- **Date window:** latest available data
- **Noise filter:** standard

### 1. Signal Inventory

| Signal | Source (URL, published) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| US establishments, 50-999 employees: 40,540 | `example.invalid/cbp`, 2026-04 | Fact | US denominator | TAM |
| German enterprises, 50-999 employees: 6,900 | `example.invalid/destatis`, 2026-02 | Fact | German denominator | TAM |
| Combined addressable organizations: 47,440 | Derived | Fact | Total denominator | TAM |
| Revenue operations analysts, US: 214,000, growing | `example.invalid/bls`, 2026-05 | Fact | Buying population is healthy | ICP |
| Median wage $98,400 | `example.invalid/bls-wage`, 2026-05 | Fact | Buyers are well compensated | Pricing |
| Market size: $12.6B globally | `example.invalid/analyst-b`, 2025 | Fact | Large and growing market | TAM |

### 2. Read

The combined denominator of 47,440 organizations against a $12.6B market supports the German entry. The buyer population is growing and well compensated, so a premium price point is defensible.

### Collection Gaps

- Some country-level detail was unavailable.

## Why It Passes a Quick Read

- Every source is an authoritative statistical agency or a named analyst firm, cited with a publication date.
- Counts are given by size band rather than in aggregate, which signals care.
- Occupation and wage data are both present — most sweeps skip wages entirely.
- The arithmetic is correct.
- It produces exactly what the next step needs: a single denominator, ready to size against.
- Evidence labels are applied consistently.

## Why It Fails

**Not one vintage is recorded.** Every row cites a publication date, and the discipline's mandatory column is absent. The US figure describes 2024; the German figure describes 2023; the occupation data describes 2025. Against an 18-month decision horizon reaching into 2028, the German number is the oldest and the most load-bearing, and nothing in the document says so. *This is the vintage violation signal verbatim:* publication years cited, periods described never stated.

**The two denominators were summed, and they are different units.** US Census counts *establishments* — physical locations, so one company with six offices contributes six. Destatis counts *enterprises* — legal entities, so the same company contributes one. "47,440 combined addressable organizations" is not a quantity. It is two incompatible measurements added together, labeled Fact, and handed to a sizing model where it will be multiplied by a price.

**The US count was never deduplicated across overlapping codes.** 541511 and 511210 both capture a substantial set of the same firms. The correctly-run version removes 2,140 duplicates and records the removal. This figure is inflated by roughly that much, in the direction that makes the entry case stronger.

**Code selection is presented as though the data chose it.** Three codes are listed with no statement of what they over-capture (agencies and consultancies that will never buy) or under-capture (buyers inside non-software companies, which the correctly-run version finds is 34% of the eligible population). A four-digit selection would land roughly three times higher. The single largest lever in the entire model is invisible.

**One analyst estimate is cited where two conflict by 3.1x.** The $12.6B figure is the larger of two credible numbers, and the smaller one — $4.1B — is not mentioned. The difference is a category-definition disagreement, and the number chosen is the flattering one. This is the exact failure that kills a business case in front of finance: not the number being wrong, but a CFO having already seen the other one.

**The German occupation gap was missed entirely, because it was an absence.** No German statistical system classifies revenue operations as a distinct occupation. The correctly-run sweep treats this as the most consequential finding available — the persona does not survive the border, and messaging aimed at a "VP RevOps" will reach nobody. This document reports the US occupation figure, does not find a German one, and moves on. A missing row leaves no empty box.

**The wage figure justifies a pricing conclusion with no stated link.** "Buyers are well compensated, so a premium price point is defensible" skips the assumption connecting salary to budget authority. Well-paid individuals do not necessarily control spend, and the ratio doing the work here is unstated and unlabeled.

**"Latest available data" and "standard" describe nothing** and cannot be reproduced. **"Some country-level detail was unavailable"** names no dataset, no source swept, and nothing that would close it — while the actual gap, the German occupation classification, is genuinely interesting and genuinely fixable with a dozen interviews.

## What Makes This Hard to Catch

Statistical authority is the disguise. Census, Destatis, and BLS are unimpeachable sources, and citing them correctly signals that the analyst did real work — which they did. The failures are all in the *handling*: units summed across definitions, codes chosen without disclosure, periods conflated with publication dates, and one of two conflicting estimates quietly selected.

The unit-summing error is the most dangerous and the least visible. "47,440" looks like a count. It reads as more rigorous than two separate numbers, because a single figure feels like a conclusion. Nothing about the arithmetic is wrong; only the meaning is.

And the vintage problem is invisible by construction. Data does not look old. A 2023 figure published in 2026 appears in a table identical to a 2025 figure published in 2026, and the difference only surfaces when someone asks, in a board meeting, whether the German market has moved since — by which time the entry is funded.

## Repair

Add the vintage column and populate it from the dataset documentation rather than the publication page. Flag anything predating the decision horizon, and name the German 2023 figure as the oldest and most load-bearing.

Stop summing. Report US establishments and German enterprises as two numbers with their units named, and say why they cannot be combined. Deduplicate the US count across overlapping codes and record how many were removed.

Disclose the code selection as an analyst judgment, with what it over- and under-captures, and note that a four-digit selection lands roughly 3x higher — that lever belongs in front of the reader, not behind them.

Report both analyst estimates with their methods and the category-definition gap that explains the difference. Adopt neither and average neither. Then go looking for the German occupation classification specifically, discover its absence, and write it up as the finding it is: the persona does not survive the border. Finally, state the salary-to-budget assumption explicitly, or drop the pricing conclusion until sizing can carry it properly.
