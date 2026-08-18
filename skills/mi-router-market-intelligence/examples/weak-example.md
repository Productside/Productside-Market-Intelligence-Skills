# Weak Example: The Instantiation That Filled Every Box

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are meant to be hard to spot. Every field is populated, the labels are used correctly, identity is established, a blind spot is named, and a route is recommended with a reason. It would pass a quick review and did — the sweep it authorized ran for two days.

It continues the fictional Cartelane case, instantiated by a different analyst.

## The Artifact

### The Six Variables

| Variable | Value | Label |
|---|---|---|
| `[TARGET]` | Cartelane, Inc. | Fact |
| `[MARKET]` | Revenue operations software | Fact |
| `[GEOGRAPHY]` | North America and EMEA | Fact |
| `[BUYER]` | VP of Revenue Operations | Fact |
| `[CAPABILITY]` | Platform expansion | Inference |
| `[DECISION]` | Understand Cartelane's competitive position ahead of the QBR | Fact |

### Identity and Perimeter

- **Legal entity:** Cartelane, Inc.
- **Ownership:** Private, venture-backed
- **Tickers:** None
- **Brands:** Cartelane Flow
- **Same-name confusions to exclude:** Standard name-collision filtering applied

### Engagement Frame

- **Relationship:** Competitor
- **Depth:** Deep
- **Time available:** Before Thursday's QBR

### Routing Recommendation

- **Recommended run:** `mi-sweep-full-spectrum`, deep
- **Why:** A comprehensive read supports a comprehensive discussion. The QBR audience is senior and will ask across several dimensions.
- **What this run will not answer:** Internal Cartelane decisions that are not public.

## Why It Passes a Quick Read

- All six variables are filled — no blanks, which is the failure most reviewers are scanning for.
- Evidence labels are present and mostly used correctly.
- Identity and perimeter exists as a section, with ownership status and brands.
- A blind spot is explicitly named, which weak instantiations usually omit.
- The route carries a stated rationale rather than appearing by default.
- Nothing in it is a lie.

## Why It Fails

**`[DECISION]` is not a decision.** "Understand Cartelane's competitive position ahead of the QBR" names an audience and an occasion, not a choice. Nothing the sweep returns could be wrong in a way anyone would notice, and — more expensively — nothing tells the run when to stop. A decision is what lets you say "the answer has stopped moving, we are done." Without one, the sweep runs until the analyst is tired. It ran for two days.

*This is the decision gate's violation signal exactly:* the engagement is described in terms of a company rather than in terms of a choice. It is also the hardest one to catch, because the sentence contains the word "ahead of," which reads like purpose.

**`[GEOGRAPHY]` is a sales region wearing a map.** "North America and EMEA" determines nothing. It does not tell the run whether to open Companies House, BRIS, or Eurostat; whether to load the EU overlay; or which statistical vintage governs the denominator. The variable exists to select registries, and this value selects none of them. Labeling it Fact compounds the error — it is a Fact about the org chart, not about the engagement.

**Three labels are wrong in the same direction.** `[MARKET]` carries no classification codes and is labeled Fact — it is the analyst's own category language, which is an Assumption about how Cartelane and the statistical agencies classify them. `[BUYER]` is labeled Fact on no stated basis. Every mislabel here reads *up*, toward more certainty, which is the direction mislabels always drift when nobody is checking.

**`[CAPABILITY]` is unfalsifiable.** "Platform expansion" is a phrase that fits almost any software company on almost any quarter. A capability hypothesis earns its place by being specific enough to be wrong — "native ERP integrations replacing the partner-built connectors" can fail; "platform expansion" cannot. The sweep therefore had nothing to sweep *against*, and every signal it found could be read as confirming.

**The same-name filter names nothing.** "Standard name-collision filtering applied" is the violation signal for identity and perimeter, stated almost verbatim. There is no standard filter. There is only the specific list of entities you decided to exclude, and if you cannot name one you have not looked. The Ontario freight brokerage went unexcluded, and two of its job postings reached the HUMINT section.

**Depth was chosen from the subject's interest, not the calendar.** Deep is a research afternoon; the QBR is Thursday. The seniority of the audience is an argument for a *tighter* brief, not a longer sweep.

**The blind spot named is not a blind spot.** "Internal decisions that are not public" is true of all open-source collection everywhere. A useful blind-spot line names what *this* route misses that another route would catch — here, that a build-signal story cannot rate above working hypothesis without current win/loss interviews. Naming the universal limitation instead of the specific one lets the brief be read as more complete than it is.

## What Makes This Hard to Catch

Completeness is the disguise. Reviewers check instantiation blocks for blanks, and there are none. The labels are present, which signals discipline. The route has a reason attached, which signals deliberation. Every individual line is defensible in isolation; the failures are all failures of *specificity*, and specificity has no empty box to reveal its absence.

The compounding is what makes it expensive. A vague `[DECISION]` removes the stopping rule, a vague `[CAPABILITY]` removes the falsifiability, and a vague `[GEOGRAPHY]` removes the source selection. Individually each is a shrug. Together they authorize a two-day sweep that cannot conclude, cannot be wrong, and cannot be defended — and it will be presented on Thursday with confidence, because it took two days.

## Repair

Push `[DECISION]` until it names a choice with an owner and a date: *whether to reprioritize the integrations roadmap this quarter.* Then ask what would have to be true for the answer to flip, and stop collecting when that stops moving.

Fill `[GEOGRAPHY]` at country level — United States and Canada — and load an overlay only if a country outside the US actually appears. Relabel `[MARKET]` and `[BUYER]` to Inference and state the basis, or find the filed classification and earn the Fact.

Replace `[CAPABILITY]` with a hypothesis that can fail, and record where it came from. If it came from one seller's recollection of one call, label it Assumption and rank it first in Assumptions to Validate.

Name the excluded entities: Cartelane Logistics of Ontario, and the "Cartlane" misspelling. Downgrade depth to standard, because Thursday. And rewrite the blind spot to name what this route specifically cannot reach — then say it again in the brief, where the VP will read it.
