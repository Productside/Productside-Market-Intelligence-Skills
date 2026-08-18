# Worked Example: A Surge With a Denominator

**Synthetic teaching case.** Cartelane is fictional, and every posting count, title, date, and review theme below is invented for teaching. Nothing here is a claim about a real company or a real person. No individual is named, which is deliberate: this discipline reports roles and patterns, not people.

**Decision supported:** Accelerate or concede our own ERP integration work this quarter.
**Suspected capability:** Native ERP integration.
**Win/loss status:** Unverified — last round was eight months ago.
**Window:** 12 months. **Prior sweep:** first run.

## Search Plan

- **Sweep order:** leadership roster → open roles by function and geography against baseline → departures and tenure → sentiment themes → public statements
- **Date window:** 12 months, with the prior 12 pulled from careers-page archives for the baseline
- **Noise filter:** roles reposted with changed titles counted once; three agency listings for the same req excluded; Cartelane Logistics (Ontario) excluded by name

## Baseline

| Function | Postings now | Baseline | Baseline source | Read |
|---|---|---|---|---|
| Integration and data engineering | 22 | 3 | Careers-page archive, same 12-month window prior year | **Surge.** 7x against a real denominator. |
| Account executives | 9 | 8 | same | Normal. Logged, not read. |
| Support | 2 | 7 | same | **Contraction.** Worth noting next to the growth story. |
| Solutions architects, EMEA | 4 | 0 | same | New function in a new region. |

Twenty-two postings would have meant nothing on its own. Twenty-two against three is the finding, and the support contraction sitting underneath it is the second one.

## 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| 22 integration and data engineering roles open, against a baseline of 3 | `example.invalid/cartelane-careers`, sampled 2026-08-15 | Fact | Hiring surge in one specialty = building a capability, not adding a feature | Roadmap |
| Support headcount postings down from 7 to 2 while revenue-facing roles hold steady | same | Fact | Cost compression in service while investing in build | Battle card |
| 4 solutions architect roles based in Germany and the Netherlands, no prior EMEA roles | same | Fact | Expansion pre-announcement | Threat assessment |
| VP of Partnerships departed 2026-06, five months after the partner-program announcement | `example.invalid/linkedin-role-change`, 2026-06 | Inference | Senior exit within six months of a strategy announcement → the strategy is in trouble | Battle card |
| Employee review themes: "reorg" in 6 of 19 reviews in the window, absent in the prior window | `example.invalid/reviews`, 2026-02 to 2026-08 | Fact | Two quarters of internal distraction, which is a window | Threat assessment |
| CTO conference talk described reconciliation "without canonical schemas" | `example.invalid/conf-talk`, 2026-03-18 | Fact | Public statement of the technical approach being taken | Roadmap |

**Deduplication applied:** 31 apparent listings collapsed to 22 distinct roles.

## 2. What the Postings Actually Say

This is the half that counting misses.

| Named in postings | Where | Read |
|---|---|---|
| Two named ERP systems, by product name | 14 of 22 integration roles | **Confirmed integration targets.** Stated more plainly than any press release would. |
| A named ledger-interchange standard | 6 roles | They intend to comply with a standard, which dates the work |
| "SOC 2 Type II experience required" | 3 roles | Regulated-segment ambition, longer horizon |
| German and Dutch language preferred | 4 EMEA roles | Local-market selling, not remote coverage |

Fourteen postings naming two specific ERP products settles a question the roadmap has been arguing about for a quarter.

## 3. Leadership and Departures

| Role | Event | Date | What it followed | Read |
|---|---|---|---|---|
| VP of Partnerships | Departed | 2026-06 | Partner-program announcement, 2026-01 | Inference: the partner strategy is being wound down, not scaled. Corroborates the TECHINT deprecation finding independently. |
| Head of Integration Engineering | Joined | 2025-11 | — | Inference: the program has an owner, which is what separates a hiring surge from a hiring spree. |

- **Tenure concentration:** one of six senior roles changed in the window. Not an organization in trouble; a single targeted exit.
- **Prior playbooks:** the new integration lead ran a similar native-connector program at a prior employer, shipping in roughly fourteen months.

## 4. Sentiment Themes

| Theme | Frequency | Source and window | Read |
|---|---|---|---|
| Reorg | Recurring — 6 of 19 reviews | Review platform, 2026-02 to 2026-08 | Roughly two quarters of internal distraction, likely resolving by Q4 |
| Growth strain in support | Concentrated — 3 reviews, all support roles | same | Consistent with the support-posting contraction; evidence about the org, not the product |

Nothing here is used as evidence about Cartelane's product quality. That would be the violation signal, and it is tempting precisely because a frustrated support engineer sounds like a customer.

## 5. Stated Strategy Versus Staffing

| What leadership says | Who they are actually hiring | Gap |
|---|---|---|
| "Our partner ecosystem is central to our integration strategy" (blog, 2026-01) | 22 in-house integration engineers, 3 in the baseline year; VP of Partnerships departed | **Diverging sharply.** The payroll says they are replacing the partner ecosystem, not centering it. |

## 6. Strongest Inference Chains (ranked, 4 shown)

1. **22-vs-3 integration surge + a named program owner + two named ERP targets** → Inference: native ERP integration is staffed and scoped. → Roadmap: this is the corroboration TECHINT needed.
2. **Partner-strategy language + VP departure + in-house hiring** → Inference: the partner model is being retired. → Battle card: displacement angle for their connector partners.
3. **Four EMEA solutions architects with language requirements** → Inference: European entry within 2-3 quarters. → Threat assessment.
4. **Support contraction during a build surge** → Inference: service quality strain likely in the next two quarters. → Battle card, *pending win/loss confirmation.*

## 7. Win/Loss Questions for the Next Round

1. When Cartelane came up, did integration breadth actually decide the evaluation, or was it a checkbox? — *tests: whether chain 1 should move a roadmap at all*
2. Did anyone evaluating Cartelane raise concerns about support responsiveness? — *tests: chain 4, which is currently an inference from posting counts*
3. For deals we lost, were their connectors already native or still partner-built? — *tests: how far along the replacement actually is, from the only people who saw it*
4. Did their partner ecosystem come up as a strength, a risk, or not at all? — *tests: chain 2 from the buyer's side*

## 8. The Gap Flag

> **Gap flag for fusion:** win/loss unverified as of this run. Weight org-instability and build-signal stories accordingly.

Chains 1 and 4 are precisely the kind this flag exists to cap. Chain 1 is a build signal; chain 4 is an org-instability read. Neither may rate above working hypothesis until interviews confirm that integration breadth and support quality actually decide deals in this market.

## 9. Watch Items

- SOC 2 requirement in three roles — escalates if compliance-specific roles appear
- Single senior departure — escalates at a second exit in two quarters

## 10. Collection Gaps and Handoffs

> **No signal found.** Public statements beyond the March conference talk returned nothing. Sources swept: podcast directories, conference archives for two industry events, published interviews. What the absence suggests: their leadership is not doing a press cycle, which is consistent with a program that is not ready to announce. What would close it: the RevOps Summit agenda, published in December.

> **Fusion pairing flag.** The 22-vs-3 surge sits in the same specialty as an existing TECHINT patent cluster. That pair — hiring surge plus patent or paper cluster in one specialty — is the strongest corroboration available in this library, and fusion should treat it as two genuinely independent channels.

## Assumptions to Validate

1. **The baseline came from careers-page archives**, which may be incomplete. If their prior-year hiring was under-captured, the 7x ratio overstates the surge — though not enough to change chain 1's direction.
2. **The VP departure is read as strategy trouble.** People leave for ordinary reasons. The timing and the corresponding hiring pattern argue for the read, but a single exit is thin.
3. **Support contraction is read as cost compression.** It could be automation or an offshore move that postings would not show.

## Final Step

1. Hand this to fusion with the win/loss flag attached (Recommended)
2. Pair it with the existing TECHINT cluster and rate the story
3. Schedule a monthly HUMINT digest so the next run is a diff
4. Take the four win/loss questions into the next interview round

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
