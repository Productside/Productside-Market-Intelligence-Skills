# Worked Example: The Complaint Was Not the Trigger

**Synthetic teaching case.** Cartelane is fictional, and every quote, platform, count, and date below is invented for teaching. No real review, reviewer, or company is represented. In a live run every quote would be real, dated, and attributable to a platform.

**Decision supported:** What goes on the battle card, and whether the connector complaints justify a roadmap change.
**Whose customers:** Cartelane's. **Buyer:** VP RevOps. **End user:** ops analysts.
**Window:** 12 months.

## Sources and Their Skew

| Source | Posts reviewed | Independent sources | Skew to note |
|---|---|---|---|
| Independent review platform | 31 | 31 | Skews negative and toward the recently churned; nobody writes a review about a tool that quietly works |
| Cartelane's own community forum | 84 | 22 | Skews loyal — the unhappy have already left, so weak points here are understated |
| Public RevOps forum | 19 | 14 | Mixed; skews toward practitioners rather than budget holders |
| App store | — | — | No mobile product; channel does not apply |

**Total independent sources: 67.** Enough to cluster. Note the buyer/end-user split: the review platform is mostly buyers, the public forum mostly analysts, and they complain about different things.

## Need Themes (solution-free)

| Theme | Frequency | Evidence |
|---|---|---|
| Cannot reconcile two systems' numbers before a board meeting | **Recurring across sources** — all three | "Every quarter I spend three days making finance's number match ours by hand." — public forum, 2026-04-11 |
| Cannot tell which system is wrong when they disagree | **Recurring across sources** — review platform and public forum | "It tells me there's a mismatch. It doesn't tell me which side to trust." — review platform, 2026-06-02 |
| Connector breaks silently and nobody notices until close | **Recurring across sources** — all three | "Found out in week three that the sync had been failing since the first." — community forum, 2026-02-19 |
| Cannot hand the process to someone else | **Concentrated in one source** — public forum only | "It's all in my head and in one spreadsheet." — public forum, 2026-07-30 |
| Cannot prove the number to an auditor | **Isolated** — one poster, twice | "Audit asked for lineage and we had screenshots." — review platform, 2026-05-14 |

The audit theme is vivid, specific, and appears **twice from one person**. It is labeled isolated for that reason. In an earlier draft it was ranked second, because it was the most quotable thing in the corpus — which is precisely the failure the frequency label exists to prevent.

**Requests recorded, and the need underneath each:**

| What they asked for | What they were trying to do |
|---|---|
| "Slack alerts on sync failure" | Find out a connector broke before close, not during it |
| "Bulk CSV export" | Reconcile by hand when the tool cannot |
| "Field-level audit log" | Prove the number to someone who does not trust it |

Every one of these is a guess at a solution. Building all three would produce a tool with alerts, exports, and logs that still does not tell an analyst which system to trust.

## Competitor Weak Points

| Weak point | Frequency | Evidence | Source skew |
|---|---|---|---|
| Connectors fail silently | **Recurring** — 14 of 31 review posts, plus community and forum | "Silent failures are the worst kind." — review platform, 2026-03-08 | Even the loyal community surfaces this, which strengthens it considerably |
| Implementation is fast, then support slows | **Recurring** — review platform and forum | "Onboarding was three weeks. Getting a ticket answered is three weeks." — review platform, 2026-07-22 | Reviews skew negative; the onboarding half is corroborated positively elsewhere |
| Partner-built connectors vary in quality | **Concentrated** — community forum | "Depends entirely who built yours." — community forum, 2026-01-30 | Loyal-source skew makes a complaint here more notable, not less |

## Switching Triggers

| Trigger event | Direction | Evidence | What it means for us |
|---|---|---|---|
| **A failed or contested audit** | Left them | "We switched after the auditors wouldn't accept our lineage." — review platform, 2026-05-14 | Entry point, and it is the audit theme's real significance |
| **Renewal following a bad quarter-close** | Left them | "Sync broke in Q4 close. We didn't renew in Q1." — public forum, 2026-03-02 | Time outreach to their renewal cycle after any close-period incident |
| **The analyst who owned the spreadsheet left** | Came *to* them | "Our RevOps person quit and nobody could run the process, so we bought something." — public forum, 2026-06-18 | **Churn early warning for us**, and a demand trigger for the category |
| A price increase at renewal | Left them | "Went up 40% and we looked around." — review platform, 2026-08-01 | Their floor just rose 144%; expect more of this |

Four triggers, and they reframe the whole run. The most-complained-about thing — silent connector failures — is a complaint. What actually made people *leave* was an audit, a bad close, or a price increase. Complaints and triggers are different data, and only the second tells you when a competitor is displaceable.

Note also the third row: a trigger that brings customers *in*. Departure language searches surface both directions, and the inbound trigger is a demand signal the category rarely notices.

## So What

- **Strongest theme:** cannot tell which system is wrong when they disagree. Recurring across two independent sources, and it is the job underneath all three feature requests.
- **Most exploitable weak point:** silent connector failure — recurring across all three sources including their own loyal community, which is the corroboration that matters most.
- **Our own churn early warning:** an analyst departure creates demand, and a bad quarter-close creates churn. Both apply to us identically.

## What to Validate Before Acting

1. **Does "which system is wrong" actually decide purchases, or is it a post-purchase frustration?** Reviews are written by people who already bought. Ten win/loss interviews would settle it, and a roadmap bet should not precede them.
2. **The audit trigger rests on one review.** It is a *trigger*, not a theme, and one instance of a trigger is a hypothesis. Two more would make it a pattern.
3. **The community-forum weak point is understated by construction.** Loyal sources under-report; the true incidence of partner-connector variance is probably higher, and nothing here bounds it.

## Collection Gaps

> **No signal found.** App-store data does not exist — no mobile product. Sources swept: both major stores under three name variants. What the absence suggests: their end users are desk-bound, which is consistent with the buyer profile. What would close it: nothing.

> **Structural gap.** Everyone quoted here bought Cartelane. The people who evaluated Cartelane and chose something else are invisible to this method entirely, and they are the population a competitive decision most needs. Only win/loss reaches them.

## Final Step

1. Take the four switching triggers into the battle card (Recommended)
2. Validate "which system is wrong" with ten interviews before any roadmap change
3. Schedule a quarterly mining pass so themes are tracked over time
4. Mine Meridian for contrast

Reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.
