# Agent Working Guide

This file is the cold-start operating guide for agents working in this Project.
It supplements, but does not replace, the governing documents below.

## Authority Order

When instructions conflict, use this order:

1. [`CONSTITUTION.md`](CONSTITUTION.md) - non-negotiable evidence, ethics, scope, and language rules
2. [`docs/SKILL-SPEC.md`](docs/SKILL-SPEC.md) - authoring and behavioral contract for everything under `skills/`
3. [`CLAUDE.md`](CLAUDE.md) - Project-wide working contract
4. [`CONTRIBUTING.md`](CONTRIBUTING.md) - contribution boundaries and author workflow
5. This file and the current task

Do not silently weaken a higher-order rule to satisfy a request, deadline, or
plausible-looking shortcut. Name the conflict and stop.

## Cold Start

Before editing:

1. Run `git status --short --branch`. Preserve existing work and do not clean,
   reset, or rewrite unrelated changes.
2. Read `CONSTITUTION.md`, `CLAUDE.md`, and the relevant part of `README.md`.
3. Read the source of truth for the area being changed:
   - `skills/`: `docs/SKILL-SPEC.md` and the relevant files under `reference/`
   - interaction behavior: `reference/guided-context-capture.md`
   - schemas: `reference/output-schemas.md`
   - packaging: `scripts/release_tools.py` and `release/public-files.txt`
   - provenance: `sources/README.md`
4. Run `./scripts/test-library.sh` before substantive work so pre-existing
   failures are distinguishable from regressions.
5. Inspect neighboring skills or documents before introducing a new pattern.

Make the smallest coherent change. Do not perform unrelated cleanup, rename
files casually, or commit unless the user explicitly asks.

## What This Project Is

This is a library of 22 instructional market-intelligence skills developed by
Productside for Product Managers, Product Marketers, and Business Analysts. The
materials teach people to collect, fuse, act on, and monitor evidence with a
visible trail of sources, dates, and confidence.

The library is a network, not a sequence. A user may enter at any of five stages:

| Stage | Job | Non-negotiable doctrine |
|---|---|---|
| `instantiate` | Define six variables and route the run | A blank `[DECISION]` stops the run |
| `collect` | Gather and label signals | Collection is not fusion; show the search plan first |
| `fuse` | Reconcile disciplines and rate confidence | Collapse shared origins before confidence stacking |
| `act` | Turn fused evidence into a decision artifact | An unsupported cell says `no evidence found` |
| `monitor` | Diff against a named prior run | Apply the materiality bar and report was/now |

A proposed skill belongs only if it does at least one of these jobs: collects
for a named discipline, fuses named disciplines, consumes fused evidence into a
named artifact, or diffs a named prior run. There is no utility tier.

Describe the contents as **digital takeaways and worked examples that
demonstrate and extend Productside's teaching and advisory services**. Prefer
**Project** over "repo" in audience-facing prose. Do not frame the deliverable as
software, an application, a data service, or a future capability commitment.

## Evidence, Privacy, and Ethics

These rules apply everywhere, including documentation, examples, branch names,
and commit messages:

- Never invent a factual claim, figure, quote, price, filing, patent, permit,
  certification, person, or URL. An honest gap is the correct output.
- Teaching examples must be explicitly labeled synthetic at the top. Use
  fictional organizations and `example.invalid` URLs. Never let an example read
  like a claim about a real organization or person.
- Never include a client or customer name. The blocked-terms list stays in a
  secret, never in this Project.
- Never store real competitive research about a named company here, even when it
  is well sourced. This Project teaches the method; it does not hold run output.
- Use only material that is published, filed, posted, or publicly observable.
  Exclude pretexting, confidential-information solicitation, access behind an
  authentication boundary, and scraping that violates accepted terms.
- Never add credentials, keys, tokens, private home paths, or saved office/email
  artifacts.

Synthetic examples are invented teaching artifacts, not invented evidence. Keep
that distinction explicit in both the label and the prose.

## Where Truth Lives

| Path | Role |
|---|---|
| `skills/` | Canonical skill source: `SKILL.md`, `template.md`, and two examples per skill |
| `reference/` | Maintained doctrine, playbooks, interaction rules, and output schemas |
| `prompts/` | Legacy runnable prompt snapshots for tools without skill support |
| `sources/` | Private provenance shelf; never included in a public archive |
| `scripts/validate-skills.py` | Authoritative skill registry and structural/behavioral validation |
| `scripts/skill_metadata.py` | Canonical-to-portable metadata projection |
| `scripts/release_tools.py` | Public-surface checks and deterministic packaging rules |
| `catalog/INDEX.md` | Human-facing inventory of all skills and triggers |
| `release/public-files.txt` | Explicit public release allowlist |

Where a prompt and a skill disagree, the skill is current. Do not automatically
resynchronize `prompts/` unless the task explicitly includes that work.

## Editing Skills

Read `docs/SKILL-SPEC.md` in full before touching anything under `skills/`.

When adding a skill:

1. Add it to `SKILL_REGISTRY` in `scripts/validate-skills.py` first, with its
   stage and discipline.
2. Add exactly:
   - `skills/<name>/SKILL.md`
   - `skills/<name>/template.md`
   - `skills/<name>/examples/worked-example.md`
   - `skills/<name>/examples/weak-example.md`
3. Update the catalog and any genuinely affected discovery documentation.
4. Confirm `consumes` and `combine-with` point only to registered skills.

For every skill change:

- Author only the rich canonical frontmatter in `SKILL.md`. Do not flatten list
  fields for portable consumers.
- Never commit `skills/*/agents/openai.yaml`; packaging generates it from the
  canonical `interface` block.
- Preserve the 13 required teaching sections and their order.
- Preserve the evidence labels `Fact`, `Inference`, and `Assumption`.
- Keep the stage doctrine, question budget, context reuse, search-plan behavior,
  human decision gate, and four-option Final Step behavior explicit.
- Keep output schemas stable and aligned with `reference/output-schemas.md`.
- Treat weak examples as load-bearing instruction. They should look competent
  on a quick read and fail because of a subtle judgment error, then explain why
  the error is easy to miss and how to repair it.
- Give each Key Concept enough explanation to improve judgment, including its
  `*Violation signal:*`.
- Preserve the separation between collection and fusion. A collect-stage skill
  may gather and label signals but may not decide whether a threat is real.

## Writing and Format Rules

- Use plain, direct language for smart readers who may not be full-time
  programmers. Explain the job, reasoning, tradeoffs, and visible failure signs.
- Use ASCII only and no emojis under `skills/`, `reference/`, and `prompts/`.
- Use prose, not Mermaid, under `skills/` and `prompts/`.
- Mermaid is permitted in human-facing Markdown such as `README.md` and
  `reference/`; quote every node label so link validation does not misread it.
- Preserve established names: the plugin is `mintel`; skills use the `mi-`
  prefix; stages and disciplines use the vocabulary in `docs/SKILL-SPEC.md`.
- Do not replace a stable schema, documented doctrine, or researched source
  decision because a different structure looks cleaner.
- Gaps, conflicts, assumptions, and stopping boundaries must remain visible.

## Packaging and Public Surface

Canonical and portable distributions intentionally differ:

- Canonical `SKILL.md` files retain rich, readable frontmatter.
- Codex and standalone archives receive projected portable frontmatter plus a
  generated `agents/openai.yaml`.
- `sources/` is provenance, not distributable content, and must stay out of
  `release/public-files.txt` and every archive.
- Plugin manifest versions must match `VERSION`.
- Public files must not contain secrets, local home paths, broken links, unsafe
  archive members, or unsupported office/email artifacts.

Use `python3 scripts/build_release.py` only when the task includes building
release artifacts. Generated archives belong under ignored `dist/`; do not add
them to the Project unless explicitly requested.

## Verification and Completion

Before finishing any content or validation change, run:

```bash
./scripts/test-library.sh
```

The required gate checks all 22 skills, rich and portable metadata, stage
doctrine, examples and templates, plugin manifests, public allowlist, links,
diagram syntax, deterministic archives, and clean extraction. A narrower check
does not replace the full gate.

Then inspect `git diff --check`, `git diff --stat`, and the relevant diff. Report
failures honestly; do not claim readiness from a partial check. If the gate
cannot run, state why and give the exact command still required.

At handoff, briefly state:

1. what changed and where
2. how it was verified, including the actual result
3. any unresolved caveat or the next sensible step
