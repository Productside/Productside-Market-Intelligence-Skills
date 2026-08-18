# Weak Example: Five Ratings and No Money

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. Five forces, five ratings, reasoning under each, and a summary. It follows the framework correctly as most people learned it. It would pass a quick review — it went into an investment memo.

Same fictional industry, analyzed by a different analyst.

## The Artifact

### Industry

The revenue operations software market.

### 1. Competitive Rivalry — Strong

Eleven vendors compete in this space, with aggressive marketing and frequent feature releases. Competition for mid-market accounts is intense, and several vendors have recently expanded their offerings.

### 2. Threat of New Entrants — Moderate

Building a credible product requires meaningful engineering investment and integrations with multiple systems. SOC 2 certification and enterprise sales capability create additional barriers.

### 3. Threat of Substitutes — Weak

Alternatives include general-purpose BI tools and CRM-native reporting, but neither addresses the reconciliation workflow directly. No direct substitute exists.

### 4. Buyer Power — Moderate

Buyers are fragmented, which limits individual leverage, though price transparency in the category gives them reference points.

### 5. Supplier Power — Weak

As a software business, we have no meaningful supply chain dependencies. Talent is the primary input and the market for it is competitive but not constrained.

### Summary

The industry shows strong rivalry, moderate entry threat, weak substitution, moderate buyer power, and weak supplier power. Overall the structure is attractive, with competition being the primary concern.

## Why It Passes a Quick Read

- All five forces are rated, in order, with reasoning under each.
- The reasoning is coherent and reads as informed — nothing is nonsense.
- Rivalry, the force most people care about, gets the most attention.
- It reaches a clear overall verdict that an investment memo can quote.
- The industry is named, and the ratings are internally consistent with the reasoning given.
- Nothing is fabricated.

## Why It Fails

**Not one citation appears anywhere.** Five ratings, five paragraphs, zero sources. *This is the discipline's central violation signal:* a force carrying a rating and reasoning with no source in it. Every rating here is a mood expressed in a table, and none can be argued with productively — a reader who disagrees can only assert a different mood.

**Substitutes rated weak, with AI substitution never mentioned.** In this category, four independent forum posters describe pasting exports into a general-purpose model and doing the reconciliation reasoning there. That is the *core job* being substituted, at small scale, improving on its own schedule without any competitor deciding anything. The rating should be strong; it is rated weak; and the analysis reads as though written before 2023.

**Non-consumption is invisible.** "No direct substitute exists" is stated in a category where an estimated 60-80% of the problem is currently solved by a spreadsheet maintained by one analyst. The largest incumbent in the market does not appear, because the substitutes force was populated with things a customer could *buy*. Buyer power is then rated moderate, missing that the buyer's real alternative — keep the spreadsheet — is the source of most of their leverage.

**Supplier power rated weak because there is no supply chain.** *This is the supplier violation signal verbatim.* The company depends on a single cloud, a single inference provider for its reconciliation feature, and two ERP vendors whose API terms permit unilateral change. The inference provider can alter pricing, impose rate limits, or deprecate a model with notice and no negotiation. That is textbook supplier concentration, and it is rated weak because it does not look like procurement.

**Rivalry rated strong for the wrong reasons.** "Eleven vendors," "aggressive marketing," "frequent releases" — none of these is structural. The structural evidence points the other way: exit barriers are low (two vendors left the category without distress), fixed costs are low, and growth is moderate. The correct rating is moderate, and the correct concern is not that rivals are numerous but that differentiation is falling.

**Entrants rated moderate against contrary evidence.** Two seed-funded entrants shipped in 2026. The barriers described — engineering investment, SOC 2, enterprise sales — are real and were cleared by companies on seed rounds. Meanwhile the interchange standard that is actively lowering switching costs goes unmentioned.

**The industry is defined as "revenue operations software,"** which spans enterprise close suites and mid-market tools with entirely different buyers, switching costs, and structures. A structural analysis of a category whose members do not share a structure produces averages of incompatible things.

**There is no profit pool read.** The analysis ends at the fifth force plus a restatement of the ratings. "Overall the structure is attractive" is asserted, not derived, and it is the opposite of what the ratings would support if they were correct. Nobody is told where the money in this industry accumulates or whether this company can reach it — which is the only question the framework exists to answer, and the only thing the investment memo needed.

## What Makes This Hard to Catch

This is Five Forces as most people learned it, and it is complete by that standard. Five headings, five ratings, reasoning under each, a summary. Reviewers check whether all five forces were addressed, and all five were.

The supplier-power error feels like accuracy rather than omission. "We're a software business, we don't have a supply chain" is true, sounds rigorous, and is the reason the rating is wrong. The dependency that matters does not present itself as a supplier — it presents itself as an API key.

And the substitutes rating is the most comfortable conclusion in the document. "No direct substitute exists" is what everyone in the category believes about their category, right up until the substitute is not direct.

## Repair

Narrow the industry definition until structure is comparable, and say what was excluded and why. Then attach at least one cited signal to every rating, and withhold any rating you cannot cite — a withheld rating with "no evidence found" is more useful in an investment memo than a confident guess.

Rebuild substitutes properly: name non-consumption and the spreadsheet first, then assess AI substitution directly against the three questions — what a model could do adequately today, whether buyers are already doing it, and what still requires the product. Rate it honestly, including "not yet material" if that is where the evidence lands.

Re-rate supplier power with cloud, model, app-store, and data dependencies in the table, and ask of each whether the supplier can change terms unilaterally. Re-rate rivalry on exit barriers, differentiation, growth, and cost profile rather than on vendor count. Re-rate entrants against what the 2026 entrants actually spent.

Then write the profit pool: where the money accumulates in this industry, whether this structure lets you reach it, and what would have to change for that answer to flip. Without it, the memo has five ratings and no conclusion.
