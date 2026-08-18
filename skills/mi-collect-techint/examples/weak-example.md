# Weak Example: Fourteen Patents and No Clock

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It cites real registries, enumerates filings with numbers and dates, uses evidence labels correctly, and stops before rating confidence. It is diligent retrieval. It would pass a quick review, and the roadmap conversation it fed produced no date.

Same fictional Cartelane case, swept by a different analyst.

## The Artifact

### Search Plan

- **Sweep order:** patents → trademarks → changelogs → repos
- **Date window:** last 24 months
- **Noise filter:** searched under the company name; excluded obvious mismatches

### 1. Signal Inventory (excerpt)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| Patent application 2025-0114xxx, "Method for reconciling transaction records" | `example.invalid/pat1`, 2025-03-11 | Fact | Investment in reconciliation technology | Roadmap |
| Patent application 2025-0288xxx, "System for schema mapping" | `example.invalid/pat2`, 2025-07-02 | Fact | Investment in data mapping | Roadmap |
| Patent application 2026-0031xxx, "Ledger synchronization apparatus" | `example.invalid/pat3`, 2026-01-19 | Fact | Investment in synchronization | Roadmap |
| *(11 further filings listed individually in the same format)* | | | | |
| Trademark "Cartelane Bridge" filed | `example.invalid/tm`, 2026-06-22 | Fact | New brand under development | Positioning |
| Changelog: 14 releases in the window, feature additions across reporting, permissions, and export | `example.invalid/changelog`, 2026-08 | Fact | Active development cadence | Roadmap |
| Public repo shows steady commit activity | `example.invalid/repo`, 2026-08 | Fact | Engineering investment continues | Roadmap |

### 2. Strongest Inference Chains

1. **Fourteen patent applications in the window** → Inference: heavy R&D investment in data integration → Roadmap: we should invest in integration too.
2. **Trademark filed** → Inference: a new product is coming.
3. **Steady release cadence** → Inference: they ship faster than we do.

### Collection Gaps

- Standards bodies and academic sources were not searched.

## Why It Passes a Quick Read

- Fourteen real, individually cited filings with application numbers and dates. This is genuine, verifiable work.
- Evidence labels present and correctly applied — nothing is overclaimed as Fact.
- The trademark and the repo activity are both real signals, correctly identified.
- Chains are ranked and tied to roadmap implications.
- It stops before rating confidence, as the discipline requires.
- It names a gap rather than pretending completeness.

## Why It Fails

**Fourteen filings and no cluster.** The inventory enumerates patents by number and never counts them by classification. This is the discipline's central violation signal, stated exactly: retrieval performed, analysis skipped. The correctly-run version finds that nine of the fourteen sit in one classification and two sit in another — which is the difference between "a committed program in ledger reconciliation" and "heavy R&D investment," a phrase that supports no decision at all.

**Not one row carries a lead time.** The column is mandatory in this discipline and is simply absent. Consequently chain 1 recommends "we should invest in integration too" with no answer to the only question the roadmap actually asks: *by when?* Patents run 12-18 months, the trademark 6-12, and the API diff — which was never found — runs weeks. The shortest clock sets the deadline, and this sweep does not know its own shortest clock.

**The assignee perimeter was never established.** "Searched under the company name" is the whole method. The nine-filing cluster sits under Flowbridge Systems, an entity acquired in 2023 that remains the assignee of record. Five of the fourteen here are under Cartelane; the other nine were found only because a colleague happened to mention the acquisition. In a run without that luck, this sweep concludes there is no meaningful cluster — and it would be wrong in the direction that costs a quarter.

**Deprecations are entirely absent.** The changelog was read for additions only. The partner-connector program moving to "maintenance only" — the single strongest signal available on this company, and the one that converts "building something" into "replacing something" — is nowhere in the document. Companies announce what they build and never announce what they abandon, which is exactly why the sweep has to go looking.

**Inventor names were never extracted.** Three names on seven filings would have identified the team, their prior lab, and a conference talk describing the approach. The document has fourteen patent numbers and zero people.

**Chain 3 is a different discipline wearing this one's clothes.** "They ship faster than we do" is a comparison of release cadence, not a read of what is being built. It also compares two unlike things: their public changelog against an unstated internal baseline. It is the chain most likely to be quoted in a meeting and the least supportable.

**The gap line explains nothing.** "Standards bodies and academic sources were not searched" states an omission without saying what was sought, what the absence would have meant, or what would close it. It reads as an apology rather than a finding — and in this case the honest version is genuinely interesting: no consortium funding, consistent with an acquire-and-hire strategy.

## What Makes This Hard to Catch

Volume reads as rigor. Fourteen individually cited filings with real application numbers looks like more work than nine filings summarized as a cluster — and it *is* more work, just the wrong work. A reviewer scanning for fabrication, missing sources, or thin coverage finds none of those problems. The document's weakness is that it stopped at the retrieval step, and retrieval is the visible half.

The missing lead-time column is the subtlest failure, because nothing looks absent. A table with five populated columns does not announce that it should have six. The consequence only surfaces later, in a roadmap meeting, when someone asks when this lands and the answer is a shrug delivered with fourteen citations behind it.

## Repair

Group the filings by classification and count them per twelve-month window before writing a single inference. Report the concentration, not the list; move the individual numbers to an appendix if anyone wants them.

Add the lead-time column and populate every row — patents 12-18 months, trademark 6-12, API and repo signals in weeks. Then re-rank by clock and let the shortest one set the roadmap decision date.

Establish the assignee perimeter first: name variants, acquired entities, research subsidiaries. Sweep all of them, and say in the plan which same-name assignees were excluded.

Diff the changelog for removals as well as additions, and give deprecations their own table with equal space. Pull the repeating inventor names and find where they came from. Delete chain 3, or rebuild it as a real built-versus-shipped comparison. Then rewrite the gap line to say what was swept, what the silence suggests, and what would close it.
