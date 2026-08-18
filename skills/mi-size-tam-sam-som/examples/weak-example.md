# Weak Example: The Model That Started With the Answer

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It has three layers, a growth rate, a sensitivity band, and a clear conclusion. The arithmetic is correct throughout. It would pass a quick review — it went to a board meeting.

Same fictional market, sized by a different analyst.

## The Artifact

### Market Sizing

**TAM:** $12.6B — the global revenue operations software market, growing 18% annually (Analyst B, 2025).

**SAM:** $3.2B — approximately 25% of TAM, representing the mid-market segment in North America and Europe.

**SOM:** $32M — 1% of SAM, a realistic three-year target for a focused entrant.

### Key Assumptions

- Mid-market represents roughly a quarter of the overall market
- 1% share is achievable for a differentiated product in three years
- Pricing consistent with current ACV

### Sensitivity

| Scenario | SOM |
|---|---|
| Best | $48M (+50%) |
| Base | $32M |
| Worst | $22M (-30%) |

### Conclusion

A $32M three-year opportunity supports investment in a dedicated go-to-market team.

## Why It Passes a Quick Read

- Three layers, in the right order, with a named external source behind the top one.
- The arithmetic checks out at every step.
- Assumptions are listed rather than buried.
- A sensitivity table exists, which many business cases omit entirely.
- The conclusion is clear and directly answers the question that was asked.
- Nothing is fabricated — the $12.6B figure is real and correctly attributed.

## Why It Fails

**It starts with a percentage and works backwards.** "1% of SAM" is the phrase the discipline refuses outright. *This is the violation signal exactly:* a share assumption appearing before any count. The number $32M was effectively chosen — it is a round percentage of a round percentage of somebody else's headline — and the model exists to justify it rather than to derive it. A real model builds up from countable things and produces a percentage as an *output*, which might have been 0.3% or 4%.

**There is no denominator anywhere.** Not one count of anything appears in the document: no establishments, no eligible organizations, no buying centers. Every layer is a percentage of the layer above, which means the entire model rests on a single external figure and two round fractions. Nothing in it can be checked, and nothing in it can be wrong in a way anyone could detect.

**Not one figure is expressed in customers.** The SOM is $32M and nobody can say what that means in logos. At a $26,600 ACV it implies about 1,200 customers in three years — roughly 33 per month against a team closing 11. *This is the currency-only violation signal*, and it is the one that matters most here, because the implausibility is entirely invisible in the currency column. The board approved a team on a number that the sales capacity cannot deliver, and nothing in the document would have revealed that.

**The 25% mid-market fraction has no basis at all.** "Approximately 25%" appears with no source, no derivation, and no eligibility constraints — no geography cut, no size band, no technographic prerequisite, no buying-center check. In the correctly-built version, five stated constraints reduce 38,400 establishments to 15,400, and each reduction has a basis someone can argue with.

**The capture rate has no comparable and no derivation.** "1% is achievable for a differentiated product" cites nothing. The discipline requires a horizon *and* a named comparable, and the available evidence supplies both: a mid-market competitor's observable trajectory anchors a 5.8% rate, and an enterprise competitor's $217K implied ACV explains why their numbers are not transferable. None of that work appears.

**The TAM is the larger of two conflicting estimates**, adopted silently. Analyst A puts the same market at $4.1B; the 3.1x gap is a category-definition disagreement, with Analyst B folding in adjacent CRM tooling this product does not replace. The larger figure was taken, the smaller was not mentioned, and the entire model scales linearly off that choice.

**The sensitivity band is decoration.** +50% and -30% are round percentages applied to the base case. No scenario names a belief that could be true or false, so nothing can be checked before the money is spent. The correctly-built version distinguishes its scenarios by specific, checkable claims — whether the sub-100 segment is addressable, whether a CRM vendor ships native reconciliation in year two — and identifies which single assumption the case hinges on.

**The method is silently blended.** A top-down TAM from an analyst, a top-down SAM fraction, and a top-down SOM percentage are presented in the format of a bottom-up model. Nothing declares which it is, so a reader assumes the more rigorous one.

**No vintages appear anywhere**, so nothing can be assessed for staleness against a three-year horizon.

## What Makes This Hard to Catch

Correct arithmetic is the disguise. Every multiplication is right, the layers are in the proper order, and the format is the format everyone recognizes. Reviewers check that TAM > SAM > SOM and that the numbers follow, and they do.

The percentages feel like modesty rather than like fabrication. "Only 1%" sounds conservative — humble, even — and humility reads as rigor. It is the most persuasive number in the document precisely because it is small, and its smallness is doing the work that a derivation should be doing.

And the missing customer column leaves no trace. A currency-only model is not visibly incomplete; it is simply a model. The question "how many customers is that" is obvious once asked and occurs to almost nobody in a room looking at a revenue figure.

## Repair

Refuse the percentage-first framing out loud, and say why — otherwise it returns in the next deck. Then go get a denominator: eligible establishments by code and size band, with vintage, from a GEOINT sweep.

Build TAM as count times benchmark, and label the benchmark honestly if it is derived rather than surveyed. Report both conflicting analyst estimates with the category-definition gap that explains them, and adopt neither.

Build SAM by applying real constraints with stated bases — geography, size band, technographic prerequisite, buying-center existence — and show the count falling at each step.

Derive the capture rate from a named comparable's actual trajectory over a stated horizon, and let the percentage be an output. Then express every layer in **customers as well as currency**, and check the SOM customer count against real sales capacity. Here that check inverts the conclusion, and the honest version of this document says so on the first page.

Finally, rebuild the sensitivity around three named beliefs rather than three round percentages, name the hinge assumption, and declare the method as bottom-up-built or top-down-validated so nobody has to guess.
