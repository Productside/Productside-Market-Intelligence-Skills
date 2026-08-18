# Skill Specification

This is the authoring and behavioral source of truth for skills in this Project.

## Location and Naming

Every skill lives at `skills/<skill-name>/SKILL.md`.

- Use lowercase kebab-case.
- Keep names to 64 characters or fewer.
- Match the directory name to frontmatter `name` exactly.

The plugin is named `mintel`, so a skill appears to a user as `mintel:<skill-name>`. Every skill carries the `mi-` prefix, and the verb that follows names the motion it performs.

| Verb | Motion | Example |
|---|---|---|
| `mi-router-` | Instantiate the engagement and route the run | `mi-router-market-intelligence` |
| `mi-collect-`, `mi-sweep-`, `mi-scan-`, `mi-snapshot-`, `mi-mine-` | Gather and label signals | `mi-collect-osint` |
| `mi-fuse-` | Combine disciplines and rate confidence | `mi-fuse-all-source` |
| `mi-analyze-`, `mi-size-`, `mi-build-` | Consume fused evidence and produce a decision artifact | `mi-analyze-swot` |
| `mi-watch-`, `mi-monitor-`, `mi-refresh-` | Diff against a prior run | `mi-watch-competitors` |

**This library is a network, not a chain.** Precedents Thinking numbers its stages because the method *is* a sequence. Market intelligence is not: a Product Manager legitimately enters at collection when a competitor surfaces in a lost deal, at fusion when signals are already in hand, at the act layer when a framework question arrives with its evidence, or at the monitor layer when a series is already running. So the skills declare a `stage` rather than a position, and `consumes` rather than a required predecessor.

### The Five Stages

`scripts/validate-skills.py` holds the registry mapping every skill to a stage and to the collection discipline it speaks for. A directory not in that registry fails validation, and so does a registry entry with no directory.

| Stage | `type` it must declare | What it owes the run |
|---|---|---|
| `instantiate` | `router` | The six variables, the route table, and a refusal to proceed without a `[DECISION]` |
| `collect` | `investigation` | A defensible sweep order, labeled signals, and no verdicts |
| `fuse` | `analysis` | The independence test before any confidence stacking |
| `act` | `analysis` | An artifact that changes, built only from cited evidence |
| `monitor` | `monitor` | A materiality bar, a named prior run, and a was/now changelog |

The `type` is pinned to the stage because it is load-bearing at runtime: a monitor that calls itself an investigation gets scheduled like one and re-collects the world every quarter instead of diffing against what it already holds.

### Discipline Coverage Is Enforced

Every skill declares the collection discipline it speaks for: `OSINT`, `FININT`, `GEOINT/DEMOINT`, `TECHINT`, `HUMINT`, `SIGINT`, `MASINT`, or `All-Source Fusion`. Validation fails if any of the seven collection disciplines has no `collect`-stage skill behind it.

This is the ceiling that keeps the Project from drifting into a general product-management prompt library. The sweep order in `reference/sweep-playbooks.md` names seven channels; if one of them has no runnable skill, the doctrine is pointing at a door that does not open. A new skill earns a place only if it collects for a named discipline, fuses named disciplines, consumes fused evidence into a named artifact, or diffs a named prior run.

## Frontmatter Is a Contract

Frontmatter supports discovery, routing, facilitation, packaging, and review. It is not decorative metadata.

### Two Shapes, One Source

Frontmatter exists in two shapes. **Author the canonical shape only.** The portable shape is generated.

| | Canonical (`skills/*/SKILL.md`) | Portable (generated) |
|---|---|---|
| Audience | Humans reviewing and editing | Strict platform validators |
| Top-level keys | The full rich set below | `name`, `description`, `license`, `metadata` |
| Multi-values | YAML lists, one per line | Pipe-separated strings under `metadata` |
| `agents/openai.yaml` | An `interface` block in frontmatter | A generated file |
| Where it ships | Canonical repository archive | Codex bundle and standalone skill archives |

The portable skill standard accepts only `name`, `description`, `license`, `allowed-tools`, and a string-to-string `metadata` map at the top level. Rather than degrading the canonical source to satisfy the strictest consumer, the packaging pipeline transforms it: `scripts/skill_metadata.py` parses the canonical frontmatter and projects it during the build.

Do not commit `agents/openai.yaml`, and do not flatten canonical frontmatter by hand. Validation rejects both.

Required canonical schema:

```yaml
---
name: mi-collect-techint
description: Trigger-oriented description under 200 characters that says what the skill does and when to use it.
license: CC-BY-NC-SA-4.0
argument-hint: "[target company] [suspected capability]"
intent: >-
  Richer explanation of the Product Manager job, the user served, and why the
  skill exists.
type: investigation
theme: market-competitive-intelligence
stage: collect
discipline: TECHINT
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Product Marketing Manager
  - Business Analyst
  - Competitive Intelligence Analyst
best-for:
  - "Specific use case"
  - "Specific use case"
  - "Specific use case"
scenarios:
  - "Realistic trigger situation"
  - "Another realistic trigger situation"
evidence-required:
  - "Expected artifact or evidence"
  - "Relevant constraint"
  - "Material unknown"
produces:
  - "Named reusable artifact"
  - "Signal inventory"
  - "Collection gaps and handoffs"
estimated-time: "45-90 min"
group-size: "1-4"
consumes:
  - mi-router-market-intelligence
combine-with:
  - mi-fuse-all-source
source-basis:
  - "Authoritative source"
  - "Supporting application"
sources:
  - https://example.org/authoritative-publication
interface:
  display_name: "Human-facing name"
  short_description: "25-64 character summary"
  brand_color: "#00E874"
  default_prompt: "Use $mi-collect-techint to ... and stop at ..."
  allow_implicit_invocation: true
---
```

Rules:

- `description` is trigger metadata, not marketing copy.
- `intent` carries the richer pedagogic and product purpose.
- `stage` and `discipline` must match the registry in `scripts/validate-skills.py`.
- `best-for` and `scenarios` must be concrete enough to improve skill discovery.
- `evidence-required` names what supports the work, not an impossible entry gate.
- `produces` names complete artifacts, not generic insight.
- `consumes` lists skills whose output this one reads; `combine-with` lists useful next moves. Both are lists, and every entry must name a registered skill. Use `[]` for `consumes` when a skill genuinely starts cold.
- `sources` lists the authoritative external URLs behind the skill; `source-basis` names them in prose.
- `source-basis` does not convert a source mention into evidence for every claim in the skill.
- `interface` must include a human-facing display name, a 25-64 character short description, the Productside brand color, a default prompt naming `$<skill-name>` that communicates the work, artifact, and stopping behavior, and an explicit implicit-invocation policy.

## Required Files

```text
skills/<skill-name>/
├── SKILL.md
├── template.md
└── examples/
    ├── worked-example.md
    └── weak-example.md
```

`agents/openai.yaml` is absent by design. It is generated into the Codex bundle and the standalone skill archives from the canonical `interface` block so the two cannot drift.

## Required Teaching Sections

Use this order:

1. `# Skill Name`
2. `## Purpose`
3. `## When to Use It`
4. `## Input`
5. `## Key Concepts`
6. `## Guided Context Capture`
7. `## What It Produces`
8. `## Workflow`
9. `## Human Decision Gate`
10. `## Evidence and Attribution Rules`
11. `## Common Failure Modes`
12. `## Assets and Examples`
13. `## Sources`

The body must teach the reasoning a Product Manager needs to judge the output. A procedural checklist without conceptual explanation is incomplete.

## The Contract Every Run Honors

These are enforced in the body of every skill, not merely recommended.

- **Evidence labels.** Every key line marked **Fact** (documented), **Inference** (evidence-based read, chain shown), or **Assumption** (working guess, basis stated). All three words must appear and be taught.
- **Do not invent.** Each skill carries a per-run list naming its own domain's specific fabrication risks. A generic "be accurate" does not satisfy this. TECHINT invents patent numbers; GEOINT invents establishment counts; OSINT invents review counts. Name yours.
- **Final Step block.** Exactly four numbered next options, recommended one first, then the reply invitation. Option 3 should almost always be the scheduling move, because the compounding value of this work lives in the series rather than in any single run.
- **Question budget.** A hard cap of three questions, then proceed on labeled assumptions. Sizing runs get four, because the constraint set is wider. Never ask a user for facts that are publicly discoverable; that is burden-shifting.
- **Reuse of supplied context.** Every skill states that anything supplied in the invocation, attachments, upstream artifacts, or prior conversation counts as context already given.

### Stage Doctrine

Each stage owns one rule its skills must state in their own words. Validation looks for the phrase, because a rule that lives only in a reference file will be skipped by the person who most needs it.

| Stage | Must state |
|---|---|
| `instantiate` | The route table, and that a blank `[DECISION]` stops the run |
| `collect` | "Collection is not fusion," and that a search plan is shown before researching |
| `fuse` | The independence test, and confidence stacking |
| `act` | That an unevidenced cell reads "no evidence found," never a plausible sentence |
| `monitor` | The materiality bar, and a named prior run |

## Pedagogy Is Functional

The skills must be as pedagogic as they are practical. The Product Manager should leave with both a usable artifact and better judgment about the tradecraft.

Every skill therefore must:

- explain why the discipline or stage exists and what goes wrong when it is skipped
- define the concepts needed to inspect the agent's reasoning
- show the distinction between strong work and a plausible-looking anti-pattern
- explain consequential tradeoffs at recommendations and human gates
- preserve reasoning in examples rather than displaying a polished answer without lineage
- avoid jargon when concrete product language will do

Conciseness is useful only when it removes repetition or noise. Removing the lesson, judgment criteria, or failure explanation is a quality regression.

### Skill Files Teach in Prose, Not Diagrams

No file under `skills/` may contain a mermaid block, and validation enforces it.

These files are read by an agent at inference time. A diagram there costs tokens to restate the numbered `Workflow` section that already exists, and it renders as raw source in most skill viewers and in the Codex bundle. Diagrams belong in the human-facing surfaces that GitHub renders — `README.md` and `reference/`. `prompts/` is likewise prose-only, because those are pasted into arbitrary tools where nothing renders.

### Key Concepts Must Teach

A one-line glossary is not a Key Concepts section. Each concept needs enough explanation for a Product Manager to inspect the agent's reasoning and catch a bad output, which means three things:

1. What the concept is, in the vocabulary of the work rather than the vocabulary of frameworks.
2. Why it matters — what goes wrong downstream when it is ignored.
3. A `*Violation signal:*` line naming how a reader notices it being broken in a real artifact.

Validation requires at least five concepts carrying a violation signal. The signal is the part that converts a definition into a usable check.

### Weak Examples Must Be Plausible

An obviously bad example teaches nothing, because nobody believes they would produce it. The anti-pattern must be work a competent team would actually ship: correct schema, disciplined vocabulary, populated fields, real URLs in the right places, and a real flaw underneath.

Each weak example therefore carries:

- the artifact itself, written to survive a skim
- `## Why It Passes a Quick Read` — what is genuinely fine about it
- `## Why It Fails` — the diagnosis, tied to named concepts and their violation signals
- `## What Makes This Hard to Catch` — why a reviewer would miss it
- `## Repair` — what to do instead

Validation requires the plausibility, diagnosis, and repair sections. Prefer flaws of *degree and judgment* — six sources that collapse to two disciplines, an announcement rated as commitment, a monitor reporting a copy tweak as a material change — over flaws of obvious absence.

## Guided Context Capture Requirements

Every skill follows [Guided Context Capture](../reference/guided-context-capture.md) and also defines its own:

- opening heads-up and named artifact
- `Guided`, `Context dump`, and `Best guess` modes
- no more than three stage-specific setup questions in normal use, four for sizing
- one-question turns and honest progress labels
- context-dump extraction categories
- best-guess assumption behavior
- Adaptive Decision Ladder at the human gate
- explicit stopping boundary

Anything supplied in the invocation, attachments, upstream artifacts, or prior conversation counts as context already given. Do not ask for it again.

**These runs must survive silence.** The three properties that make a run schedulable are the question budget that proceeds on assumptions, the search plan gate that continues unless revised, and the stable schema that lets run N+1 diff against run N. A skill that blocks waiting for input cannot be scheduled, and scheduling is where this library compounds.

## Behavioral Requirements

Every skill must:

- state in one line whether it has web access, and run from training data with everything marked Assumption when it does not
- work with incomplete evidence while labeling gaps
- report a discipline that returned nothing as a gap, in the gap language from `reference/sweep-playbooks.md`, rather than padding the section
- distinguish Fact, Inference, and Assumption
- attach a real, checkable URL and a date to every signal
- research externally discoverable facts when tools are available
- ask humans only for knowledge, judgment, risk acceptance, or authority they uniquely hold
- produce a complete reusable artifact against a stable schema
- expose unresolved questions, conflicts, and collection gaps
- stop at its named human decision gate
- remain useful without a particular AI platform
- stay inside the guardrails: published, filed, posted, or publicly observable only

## Completion Standard

A skill is ready only when:

- its trigger does not materially overlap another skill
- a Product Manager can recognize when to invoke it from metadata alone
- its guided flow works empty-handed, with partial context, and with a complete upstream artifact
- its output matches the reusable template and the schemas in `reference/output-schemas.md`
- the worked and weak examples teach the difference between strong and shallow reasoning
- external claims are sourced and weak evidence remains visibly weak
- `consumes` and `combine-with` references resolve
- a fresh agent can use it without hidden facilitation knowledge
- canonical, native, and clean-distribution validation pass

Run:

```bash
./scripts/test-library.sh
```
