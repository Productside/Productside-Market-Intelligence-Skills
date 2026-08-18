# The Original Prompts

These are the twenty-one runnable investigation prompts this Project was distilled from, carried here verbatim from the `market-intelligence` directory of [github.com/deanpeters/product-manager-prompts](https://github.com/deanpeters/product-manager-prompts).

## Why They Are Here

The skills in [`skills/`](../skills/) are the maintained form of this material: validated frontmatter, a stable interaction contract, worked and weak examples, and a doctrine layer in [`reference/`](../reference/) they point into.

The prompts are for the case where a skill cannot be installed — a chat interface, a tool without plugin support, a colleague who wants to paste something into whatever they already use. Copy the file's contents, fill the bracketed variables, and run it.

They are prose-only by design. Nothing renders in the arbitrary tools these get pasted into.

## Which Prompt Maps to Which Skill

| Prompt | Skill |
|---|---|
| `full-spectrum-company-sweep-prompt.md` | `mi-sweep-full-spectrum` |
| `osint-collection-prompt.md` | `mi-collect-osint` |
| `finint-collection-prompt.md` | `mi-collect-finint` |
| `geoint-demoint-collection-prompt.md` | `mi-collect-geoint-demoint` |
| `techint-collection-prompt.md` | `mi-collect-techint` |
| `humint-collection-prompt.md` | `mi-collect-humint` |
| `sigint-collection-prompt.md` | `mi-collect-sigint` |
| `masint-collection-prompt.md` | `mi-collect-masint` |
| `all-source-fusion-prompt.md` | `mi-fuse-all-source` |
| `market-landscape-scan-prompt.md` | `mi-scan-market-landscape` |
| `competitive-research-snapshot-prompt.md` | `mi-snapshot-competitors` |
| `voice-of-customer-miner-prompt.md` | `mi-mine-voice-of-customer` |
| `swot-analysis-prompt.md` | `mi-analyze-swot` |
| `porters-five-forces-prompt.md` | `mi-analyze-five-forces` |
| `ansoff-matrix-prompt.md` | `mi-analyze-ansoff` |
| `tam-sam-som-analysis-prompt.md` | `mi-size-tam-sam-som` |
| `battle-card-builder-prompt.md` | `mi-build-battle-card` |
| `competitive-intel-watch-prompt.md` | `mi-watch-competitors` |
| `pricing-packaging-tracker-prompt.md` | `mi-monitor-pricing-packaging` |
| `pestel-delta-monitor-prompt.md` | `mi-monitor-pestel-delta` |
| `earnings-executive-signal-refresh-prompt.md` | `mi-refresh-earnings-signals` |

## Divergence

These files are a snapshot of the upstream source. The skills are maintained; the prompts are not re-synced automatically. **Where the two disagree, the skill is current.**

One link in `humint-collection-prompt.md` was rewritten to an absolute URL, because it pointed at a sibling directory that exists in the upstream project and not here. Nothing else was changed.
