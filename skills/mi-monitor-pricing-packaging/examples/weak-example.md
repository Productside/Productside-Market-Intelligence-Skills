# Weak Example: Pricing Simplified

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It is dated, sourced, covers both competitors, notices a real change, and produces an action. It is faster to write and easier to read than the correct version. It would pass a quick review — and three months later it could not answer the question it was built for.

Same fictional competitor set, captured by a different analyst.

## The Artifact

### Pricing Update — August 2026

**Competitors reviewed:** Cartelane, Meridian
**Date:** 2026-08-18

### Cartelane

Cartelane has simplified its pricing, moving from four tiers to three. Their entry point is now higher, starting at $119/user/month for Growth, with Scale at $189 and Enterprise on request. They have also improved the connector allowance at the Growth level and are offering a stronger annual discount.

**Read:** Cartelane is moving upmarket and competing less on price. This is good news for us at the low end.

### Meridian

No published pricing. Contact-us model as before.

### Action

Update the battle card pricing table.

## Why It Passes a Quick Read

- Dated, with both competitors covered.
- It correctly identifies a real and significant change — the entry point rising.
- It gives an actual read and a concrete action.
- The prose is clear and immediately understandable, which a table is not.
- Nothing in it is false.
- It took ten minutes.

## Why It Fails

**Nothing was captured verbatim.** This is a summary of a pricing page, not a record of one. *This is the discipline's defining violation signal, stated almost word for word:* the record says "simplified" and nowhere preserves what the tiers were called, what they cost, or what they included. Once the page changes again, the 2026-08-18 state is gone permanently — a reconstruction from this document is impossible.

The asymmetry is the whole point of the rule: the interpretation is reproducible from the capture, and the capture is not reproducible from the interpretation.

**The limits, inclusions, and minimums were never recorded, and that is where the real change was.** Growth held at $119 while its monthly record limit was cut from 500,000 to 250,000. A customer at 400,000 records is now forced to Scale — a 59% increase presented as a feature improvement. This document reports the *opposite*: "improved the connector allowance," which is the visible half of a trade whose invisible half is a price rise.

Three months later, deal desk asked whether Cartelane's throughput limits had moved. Nobody could answer, and the prior page was no longer archived.

**No prior capture is named and no interval is stated.** "Moving from four tiers to three" implies a prior state that exists nowhere in the document. A reader cannot tell whether the fourth tier disappeared this quarter or last year, or what it was called and cost. *This is the named-prior-capture violation signal*, and it makes the delta unverifiable.

**The read is single, confident, and possibly backwards.** "Moving upmarket and competing less on price — good news for us at the low end" chooses one explanation. The widening annual discount points equally at cash or retention pressure, which would mean *more* price aggression in contested deals, not less. Those two readings point opposite ways about the competitor's health, and telling deal desk the wrong one has direct consequences at quarter end.

**"Improved the connector allowance" and "stronger annual discount" are interpretations in place of data.** Five to ten connectors, and 10% to 20%, are facts that fit in a table and are gone from this document. "Stronger" cannot be diffed against anything next quarter.

**The premium support line vanished entirely.** It moved from $29/user/month to "contact us," which is a real packaging signal — and it is not mentioned, because the summary covered only what looked like headline pricing.

**Meridian's "no published pricing" is reported and not recorded as a field.** Captured properly in two consecutive runs, the stability of their contact-us posture is a data point in a series. Here it is an aside.

**The action has no urgency, no owner, and misses two of three.** "Update the battle card pricing table" is right and incomplete: deal desk guidance needs review because their annual discount doubled, and the repriced customer population is a campaign, not a footnote.

## What Makes This Hard to Catch

Prose reads better than a table, and it reads like understanding. A paragraph saying "Cartelane has simplified its pricing and moved upmarket" sounds like an analyst who grasped the situation; a nine-column verbatim table looks like data entry. Reviewers reward the first.

The document is also *correct*. Every sentence in it is true. The failure is entirely in what was not written down, and omissions in a summary are invisible by construction — nobody reading "simplified from four tiers to three" senses that a record limit halved.

And the cost is deferred. This report was useful in August. It failed in November, in a different meeting, to a different person, who had no way to know that the answer had been discarded rather than never collected.

## Repair

Capture every field verbatim before writing a word of interpretation: tier names, list prices, billing period, unit, inclusions, limits, add-ons, minimums, overage rates, trial terms, published discounts, and the contact-us boundary. Use the same fields every run.

Name the prior capture file in the header and state the interval. Then diff field by field and write each change in was/now format with both dates — which surfaces the halved record limit, the $29 premium-support line going unpriced, and the seat minimum doubling, none of which the summary contained.

Name packaging signals only where their pattern actually appears, and leave the others blank. Flag the annual-discount change as ambiguous, give both explanations, and route it to FININT rather than choosing.

Record Meridian's "not published" as a field value in every run, so their posture becomes part of the series. Then set three update flags with owners and urgency, and store the capture under the naming convention so November's question has somewhere to land.
