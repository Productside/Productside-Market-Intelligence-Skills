# Worked Example: Four Rep Claims Went to Do Not Say

**Synthetic teaching case.** Cartelane is fictional, and every price, quote, date, and source below is invented for teaching. Nothing here is a claim about a real vendor. In a live run every appendix row would carry a checkable URL.

**Card date:** 2026-08-18
**For:** Mid-market deals, 100-999 employees, where Finance runs the evaluation.
**Evidence base:** Fusion brief 2026-08-18, SIGINT pricing capture 2026-08-18, VoC mining 2026-08-18.
**Win/loss status:** **Unverified** — last round eight months ago. No win-reason claims appear on this card.

### Decay

| Layer | Goes stale | Re-run |
|---|---|---|
| Pricing (captured 2026-08-18) | Weeks — they changed it this quarter | Weekly |
| Messaging (hero rewritten twice in 96 days) | Weeks, unusually — they are unsettled | Monthly |
| Certifications, funding | Two to four quarters | Quarterly |

## Thirty-Second Read

- **Who they are:** Mid-market revenue ops platform, integration-led, PE-free and venture-backed, ~$40M scale. Fast to implement, currently rebuilding their integration layer in-house.
- **When we win:** Finance is in the room and audit lineage matters; the buyer runs one of our two native ERP connections; the evaluation includes a compliance requirement.
- **When we lose:** Speed to first report decides it. They deliver in three weeks; we take six. In four of four RFPs we have seen this year, that criterion was scored — and we lose it every time.

The "when we lose" line is specific and unflattering. A rep who reads it knows to raise implementation timing early and frame it, rather than being ambushed by it at week four.

## Say This (max 4)

| # | Say | Evidence ref |
|---|---|---|
| 1 | Your auditors accept the number without you assembling a screenshot trail — our lineage is certified, theirs is in process | E1, E2 |
| 2 | You will know a connector broke before close, not during it — silent sync failure is the single most common complaint about their platform | E3 |
| 3 | The price you see is the price you pay; their published floor rose 144% this quarter and their mid-tier add-ons are now unpriced | E4 |
| 4 | Their partner-built connectors are closed to new partners, so if yours breaks, the queue is now internal | E5 |

Four outcomes, not four features. Point 1 is "auditors accept the number," not "we have field-level audit lineage."

## Ask This (max 3)

| # | Question | What it exposes | Evidence ref | Expected counter and your response |
|---|---|---|---|---|
| 1 | "When a sync fails, how do you find out — and how did the last customer find out?" | Silent failure, their most-cited weakness across three independent sources | E3 | They will describe a status dashboard. Follow up: "does it alert, or do you have to look?" |
| 2 | "Is your SOC 2 Type II complete, or in process?" | Certification gap; theirs is listed in-process with a named auditor | E2 | They will say "in process, completing shortly." That is the honest answer and it is fine — the point is the buyer now knows to ask for the report before signing. |
| 3 | "Which of my two ERPs do you connect to natively today, versus through a partner?" | Their partner program is closed and the native layer is unreleased | E5, E6 | They will describe the roadmap. Response: "so today, partner-built" — no further push needed. |

**Cut for lack of evidence:** a question about their support response times. The measured degradation (4h to 19h median) comes from a 34-thread public sample, not from their SLA. Enterprise customers may have entirely different experience, and a rep asking it could be told "our contracted SLA is four hours" and have nothing to say. It sits in Do Not Say instead.

That cut is the discipline working. It was the most tempting question available.

## Watch Out For

| Their claim | Is it true? | Evidence ref | Your response |
|---|---|---|---|
| "We implement in three weeks" | **Yes.** Corroborated in 7 of 19 reviews, unprompted, and it is genuinely fast | E7 | Do not dispute it. "They are fast to stand up. The question is what happens in month four when the reconciliation is contested — that is where lineage matters." |
| "We publish our pricing" | **Yes**, and so do we — this is not a differentiator for either of us | E4 | Concede immediately and move to what the price buys |
| "We are building native ERP connectors" | **Partly.** Eleven endpoints are documented and staged; nothing is generally available | E6 | "Staged, not shipped. Worth asking when it is GA and what the migration from partner connectors looks like." |

Row one is the important one. A rep told the competitor is weak everywhere will contest a true claim, lose credibility, and lose the room. Conceding it costs nothing and buys the reframe.

## Pricing and Packaging Snapshot

**Captured:** 2026-08-18 — **Source:** `example.invalid/cartelane-pricing`

| Tier | List price | Unit | Included | Limits | Minimum |
|---|---|---|---|---|---|
| Growth | $119 | per user/mo | 10 connectors, standard support | 250K records/mo | 10 seats |
| Scale | $189 | per user/mo | Unlimited connectors, SSO | 2M records/mo | 25 seats |
| Enterprise | Contact us | — | — | — | — |

- **Recent change:** Starter tier at $49 with 3 connectors was **removed** between 2026-05-14 and 2026-08-18. Floor rose from $49 to $119, a 144% increase. Annual discount widened from 10% to 20%.
- **"Contact us" boundary:** moved down one tier — Scale add-ons are now unpriced.

## Do Not Say

| Tempting claim | Why it does not hold |
|---|---|
| **"Their support is falling apart."** | Reps are saying this. The evidence is a 34-thread public forum sample showing median first response moving from 4h to 19h. That is a real measurement of *public forum* responses, not of contracted SLAs. A prospect who is a happy Cartelane customer will contradict it, and win/loss has not established that support decides deals here. |
| **"They are losing customers."** | No evidence exists. Nothing in five sweeps supports it. It appears to have come from one lost-deal conversation. |
| **"Their integration platform is vaporware."** | It is staged, not vapor. Eleven documented endpoints and a live staging certificate. Calling it vaporware will be disproven within two quarters and the rep will be remembered for it. |
| **"PE will squeeze them on price."** | They are venture-backed, not PE-held. This claim is factually wrong about the company. |

Four claims reps were actively making. Two are unsupported, one is measurably wrong about the company, and one overstates real evidence. Checking them was the most valuable twenty minutes of this run — the fourth would have been corrected by any buyer who had done basic diligence.

## Evidence Appendix

| Ref | Claim | Source (URL) | Date | Label |
|---|---|---|---|---|
| E1 | Our SOC 2 Type II is complete | Our audit report | 2026-03 | Fact |
| E2 | Their SOC 2 Type II is in process, auditor named | `example.invalid/trust-registry` | 2026-06-04 | Fact |
| E3 | Connector reliability cited in 14 of 31 reviews plus community and forum | `example.invalid/g2`, `example.invalid/community` | 2026-08 | Fact |
| E4 | Starter tier removed; floor $49 → $119; annual discount 10% → 20% | `example.invalid/cartelane-pricing` vs archive | 2026-08-18 vs 2026-05-14 | Fact |
| E5 | Partner program moved to maintenance-only, closed to new partners | `example.invalid/partner-docs` | 2026-07-01 | Fact |
| E6 | 11 endpoints under `/v2/ledger-sync/`, absent from product | `example.invalid/cartelane-api` | 2026-08-12 | Fact |
| E7 | Implementation speed praised in 7 of 19 reviews, unprompted | `example.invalid/g2` | 2026-08 | Fact |

Every claim on the card has a row. Every row is a Fact — no Inference and no Assumption reached the card itself.

## Where Evidence Was Missing

> **No evidence found** for any claim about their customer retention or churn. Sources checked: filings (none — private), review platforms, community forum, funding databases. It has been left off the card entirely and added to Do Not Say. What would close it: nothing publicly; only win/loss and customer conversations.

## Final Step

1. Ship the card, and brief the field specifically on the four Do Not Say items (Recommended)
2. Run win/loss so the support question can be asked at all
3. Set up the weekly SIGINT watch — their pricing changed this quarter and their messaging twice
4. Re-run this card the week their SOC 2 completes; two of four "say this" points depend on it

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
