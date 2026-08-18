# Weak Example: The Diff That Had No Before

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It cites live pages with capture dates, uses evidence labels, ranks its chains, and reaches conclusions a battle card can use tomorrow. It respects every ethical boundary. It would pass a quick review, and two of its lines went onto a card that a rep quoted to a customer.

Same fictional Cartelane case, swept by a different analyst.

## The Artifact

### Search Plan

- **Sweep order:** pricing → homepage → docs → certificates
- **Date window:** current
- **Noise filter:** ignored cosmetic changes

### 1. Signal Inventory

| Signal | Source (URL, capture date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| Pricing page shows three tiers: Growth $119, Scale $189, Enterprise "contact us" | `example.invalid/cartelane-pricing`, 2026-08-18 | Fact | Enterprise-oriented packaging; they are not competing on price | Battle card |
| Homepage hero reads "One system of record for revenue" | `example.invalid/cartelane-home`, 2026-08-18 | Fact | Platform positioning | Positioning |
| API docs include a `/v2/ledger-sync/` section with 11 endpoints | `example.invalid/cartelane-api`, 2026-08-12 | Fact | Integration capability exists | Roadmap |
| Subdomain `ledger.cartelane.example` resolves | `example.invalid/dns`, 2026-08-18 | Fact | Integration product is live | Battle card |
| Status page shows 4 incidents in 90 days | `example.invalid/status`, 2026-08-18 | Fact | Reliability is weak | Battle card |
| Partner directory lists 31 partners | `example.invalid/partners`, 2026-08-18 | Fact | Strong partner ecosystem | Threat assessment |

### 2. Strongest Inference Chains

1. **Three tiers starting at $119** → Inference: they price above us at entry → Battle card: we win on cost of entry.
2. **`ledger-sync` endpoints and a live subdomain** → Inference: their integration product has shipped → Battle card: do not claim an integration advantage.
3. **Four incidents in 90 days** → Inference: reliability problems → Battle card: lead with uptime.

### Collection Gaps

- None material.

## Why It Passes a Quick Read

- Every page is real, cited, and carries a capture date.
- Evidence labels are applied consistently, and nothing is fabricated.
- The certificate and endpoint findings are genuinely good catches that most sweeps miss entirely.
- Chains are ranked and end in specific, usable field actions.
- It stops before rating confidence, as the discipline requires.
- It respects every ethical boundary — public pages only, nothing behind authentication.

## Why It Fails

**Not one row has a before-state.** This is a SIGINT sweep in which nothing is diffed. Every row records what a page says today, which the discipline's mandatory column exists to prevent being read as movement. The word "diff" appears nowhere and neither does a prior capture, an archive snapshot, or the May run that exists in the same folder.

*The violation signal is present six times over:* rows describing current state, read as change. The most expensive instance is chain 1.

**Chain 1 inverts the actual finding.** "They price above us at entry" is true of the page today and misses that the $49 Starter tier *was removed this quarter* and the floor rose 144%. The real intelligence — an entire segment of their installed base was just repriced and is now addressable — is invisible without the before. The card that resulted tells the field to compete on entry cost against a competitor that has just vacated the entry segment, which is a play against an opponent who left the field.

**Chain 2 reads staging as shipping.** A subdomain that resolves to a login page and eleven endpoints documented but absent from the product is *staging*, not launch. The sweep upgrades it to "has shipped" and then instructs the field to stop claiming an integration advantage — surrendering a position that is still held, weeks before it needed to be surrendered. The correctly-run version treats the same two signals as the earliest possible warning and sets a decision date *ahead* of the announcement.

**Chain 3 builds a customer-facing claim on a baseline with no baseline.** Four incidents in ninety days is a number with no comparison: not against their own prior period, not against the category, not against our own status page. "Lead with uptime" went onto a card, and a rep said it to a prospect who had read both status pages.

**Verbatim capture never happened.** Prices and tier names appear inline in a chain, and nowhere are units, limits, inclusions, minimums, add-ons, or trial terms recorded. Next quarter, when someone asks whether the record limit moved, this document cannot answer, and the quarter after that the question is unanswerable forever. In this discipline the note-taking *is* the tradecraft.

**Messaging was read once.** One snapshot of the hero yields "platform positioning." Three snapshots would have shown it rewritten twice in ninety-six days — positioning uncertainty, and the most exploitable finding available on this company. A single reading cannot detect churn by construction.

**Brand-term bidding was never checked**, so the fact that Cartelane started targeting this company's own customers with migration ad copy is simply absent. It is in the sweep order the discipline specifies and not in the sweep order this analyst wrote.

**"None material" is not a gap statement.** The app-store channel returned nothing, archive coverage is discontinuous, and the status-page history has no prior reading. Three real limitations, all unreported.

## What Makes This Hard to Catch

A SIGINT sweep with no before-state looks exactly like a SIGINT sweep with one, because the evidence column is populated either way. The rows are true. The URLs work. The capture dates are recent, which reads as freshness rather than as the absence of history. Reviewers check whether sources are real and current; a missing prior-state column has nothing to point at.

The certificate and endpoint catches make it worse, not better. They are sophisticated finds that signal a capable analyst, and they buy credibility for chain 2, which is the chain that gave away a live competitive position.

And every conclusion is decisive. "We win on cost of entry," "do not claim an integration advantage," "lead with uptime" — three clear instructions, each confidently wrong in a way that only shows up in front of a customer.

## Repair

Find the prior state before writing a single inference. The May capture is in the same folder; three archive snapshots are available. Populate the before-to-after column on every row, and move anything with no prior state into a clearly labeled baseline-captures table so it can never be read as movement.

Rebuild chain 1 around the removed Starter tier and the 144% floor increase, and rewrite the field guidance accordingly. Downgrade chain 2 from shipped to staged, attach a point-event staleness note, and set the roadmap decision date ahead of the announcement window. Pull chain 3 off the card entirely until a comparison exists.

Capture pricing verbatim — tiers, units, limits, inclusions, minimums, add-ons, trial terms — before interpreting any of it. Pull three archive snapshots of the hero and count the rewrites. Check their bidding on your own brand terms, which the sweep order calls for and this run skipped. Then write the real gap statement, including the honest one: archive coverage is not continuous, so the messaging count is a floor, not a total.
