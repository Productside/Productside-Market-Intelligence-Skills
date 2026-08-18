# Weak Example: The Quarter Everything Moved

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. Six factors, each with current developments and an implication, ending in strategic considerations. It is well informed and reads as comprehensive. It would pass a quick review — it has been produced quarterly for two years and nobody has ever acted on one.

Same fictional market, run by a different analyst.

## The Artifact

### PESTEL Analysis — Q3 2026

**Market:** Revenue operations tooling, North America and Europe

**Political:** Trade policy uncertainty continues to affect cross-border software procurement. Government digitization initiatives are expanding in several markets, creating potential demand. *Implication: monitor policy developments.*

**Economic:** Interest rates remain elevated, constraining discretionary technology spending. Wage growth in knowledge-worker roles continues. Currency volatility affects European pricing. *Implication: buyers may be more price-sensitive.*

**Social:** Remote and hybrid work continue to reshape how teams collaborate. There is growing expectation of self-serve software experiences. Data privacy awareness is increasing among buyers. *Implication: emphasize ease of adoption.*

**Technological:** AI capabilities are advancing rapidly across the software landscape. Integration standards continue to evolve. Cloud infrastructure costs are shifting. *Implication: AI features are increasingly table stakes.*

**Environmental:** Sustainability reporting requirements are expanding. Corporate ESG commitments are influencing vendor selection. *Implication: consider our sustainability posture.*

**Legal:** Regulatory scrutiny of data handling is increasing. New financial reporting rules are coming in several jurisdictions. Employment law changes affect our customers' operations. *Implication: compliance is a growing consideration.*

### Strategic Considerations

The macro environment remains dynamic. Key themes are AI adoption, cost pressure, and regulatory complexity. We should continue to monitor developments and ensure our positioning reflects these trends.

## Why It Passes a Quick Read

- All six factors covered, in order, with multiple developments under each.
- Every observation is broadly accurate about the world.
- Each factor carries an implication, so it does not merely describe.
- It ends with a synthesis identifying named themes.
- It is delivered on schedule, every quarter.
- Nothing in it is false.

## Why It Fails

**There is no baseline and no window, so nothing is a delta.** No prior PESTEL is named and no date range is given. Every factor is written as a current-state description of the world, which means the reader cannot tell what changed this quarter versus what has been true for three years. *This is the baseline violation signal exactly:* every factor has an implied "now" with no prior state in any document.

Run this way, the report is a baseline in delta clothing — and produced quarterly, it is eight consecutive baselines that were never compared to each other.

**All six factors moved.** Every quarter, for two years. *This is the horoscope failure*, and it is diagnostic: a filtered quarter has several factors reporting no material movement, and this report has never contained that entry. The correctly-run version of this same quarter finds four of six held steady and two moved — one of them a wage-series revision that this report describes as "wage growth continues," which is the opposite of what happened.

**No threshold is named anywhere.** "Interest rates remain elevated" is a fact about the world. It becomes a finding only when it crosses a level that matters to something named — a capex approval threshold, a corridor boundary, a discount rate in a business case. Without thresholds, every factor is permanently in motion and permanently unactionable.

**Not one artifact is named, so the broken-assumptions section does not exist.** The pricing corridor built on an 11% wage trend that has been revised to 6% is invalidated in its upper half this quarter, and nothing here reveals it — because the report describes conditions rather than checking assumptions. This is the section that earns the run, and its absence is why nobody has acted on eight consecutive reports.

**"New to the frame" is absent, and it cost the most.** A sustainability-disclosure threshold entering consultation to drop from 750 to 250 employees would bring roughly 40% of the German SAM into scope with a reconciliation obligation attached. The report mentions that "sustainability reporting requirements are expanding" — generically, at the level of the whole world — and misses the specific consultation that turns a compliance burden into a demand driver for this exact product.

**Regulatory states are collapsed into "coming."** "New financial reporting rules are coming in several jurisdictions" merges proposed, in consultation, adopted, and in force. The German amendment relevant here is still only *proposed* and has not entered consultation — no timeline exists — while the entry case has been quietly assuming an eighteen-month horizon.

**The implications are instructions to keep reading.** "Monitor policy developments," "consider our sustainability posture," "compliance is a growing consideration." None names an artifact, an owner, or a decision. They are the shape of an implication without the content.

**The synthesis is true of every B2B software company in 2026.** "AI adoption, cost pressure, and regulatory complexity" would fit any category, which means it distinguishes nothing about this one.

## What Makes This Hard to Catch

Every sentence is accurate. Interest rates *are* elevated, AI *is* advancing, sustainability reporting *is* expanding. A reviewer checking for errors finds none, and the breadth reads as awareness. The document fails not on truth but on specificity, and specificity has no error to point at.

The all-six-moved pattern is nearly invisible in any single quarter. A report saying six things changed is unremarkable; it is only across four or five quarters that the pattern becomes obviously impossible, and by then the report has become furniture that nobody reads closely.

And "no material movement" is genuinely uncomfortable to write. It looks like less work in a document whose author is being judged on evident effort, and the incentive runs one way, every quarter, forever.

## Repair

Find the baseline. If none exists, **stop** — say so and offer to build one, because a first pass labeled as a delta is worse than no report. If it exists, name it in the header along with the window and the sources swept.

Set thresholds before examining anything: what level of rate, wage, currency, or regulatory stage would matter to which named artifact. Then take each factor and ask whether it crossed one. Expect most quarters to produce several one-line "no material movement" entries, and write them.

Rewrite the economic factor around the actual event — a wage-series revision from 11% to 6% — in was/now format with both releases cited. Then check the pricing corridor and the sizing model against it, and write the broken-assumptions table naming each artifact, its assumption, and what is now true.

Distinguish proposed, in consultation, adopted, and in force for every regulation, and give the German amendment its real state. Add the new-to-the-frame section and go looking for factors that did not apply last quarter — which is where the disclosure-threshold consultation was sitting. Then delete the synthesis and let the broken assumptions be the so-what.
