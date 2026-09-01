# Contributing

Thank you for helping improve the method. You do not need to write a complete skill or use command-line tools to contribute. A field report about the method, a judgment call, or a sharper weak example can be more useful than a large change.

Start with [`COMMUNITY.md`](COMMUNITY.md). It explains what belongs in Discussions, issues, and pull requests, and what must never be posted publicly.

## Contributor Terms

By submitting a contribution to this Project, you agree to [`CONTRIBUTOR-TERMS.md`](CONTRIBUTOR-TERMS.md).

In plain language:

- you keep ownership of your contribution
- accepted contributors receive attribution in [`CONTRIBUTORS.md`](CONTRIBUTORS.md) and the Project history
- you grant 280 Group LLC dba Productside the permanent rights needed to use, edit, publish, distribute, sublicense, and commercially use the contribution
- you confirm that you created the contribution or have permission to submit it
- you do not submit client material, employer-confidential material, live competitive findings, or anything another person owns

These contributor terms are separate from the Project's public [CC BY-NC-ND 4.0 license](LICENSE). The public license governs what people may do with published Project materials. The contributor terms govern what Productside may do with a submission.

## The Contribution Test

A change earns a place in this Project if it does one of four things:

1. **Collects** for a named intelligence discipline
2. **Fuses** named disciplines into confidence-rated stories
3. **Consumes** fused evidence into a named decision artifact
4. **Diffs** a named prior run

If a proposed skill does none of these, it belongs in a general product-management library, not here. This test is the boundary that keeps the Project from drifting into a prompt collection, and `scripts/validate-skills.py` enforces its structural half: every skill must appear in `SKILL_REGISTRY` with a stage and a discipline, and every one of the seven collection disciplines must have a `collect`-stage skill behind it.

## Before You Write

Read [`docs/SKILL-SPEC.md`](docs/SKILL-SPEC.md). It is the authoring and behavioral source of truth: frontmatter schema, the thirteen required sections, the stage doctrine each skill must state, and the standard for worked and weak examples.

Read [`reference/guided-context-capture.md`](reference/guided-context-capture.md) for the interaction contract every skill honors.

For a substantial change or new skill, open a proposal before investing the work. Response times vary, and a proposal is not a promise that Productside will accept or publish the contribution.

## Adding a Skill

1. Add the name to `SKILL_REGISTRY` in `scripts/validate-skills.py` with its stage and discipline.
2. Create `skills/<name>/` with `SKILL.md`, `template.md`, and `examples/worked-example.md` and `examples/weak-example.md`.
3. Run `./scripts/test-library.sh` until it passes.

Validation is not a formality here. It checks the frontmatter contract, the portable projection, the section order, the evidence labels, the do-not-invent list, the Final Step block, the stage doctrine, five Key Concepts each carrying a violation signal, and the structure of both examples.

## Writing Standards

- **Examples are synthetic and labeled.** Every company, figure, quote, price, and URL in an example is invented for teaching. Use `example.invalid` for URLs. Never write an example that could be read as a factual claim about a real organization.
- **Weak examples must be plausible.** An obviously bad example teaches nothing, because nobody believes they would produce it. The anti-pattern must be work a competent team would ship: correct schema, disciplined vocabulary, populated fields, and a real flaw underneath.
- **Key Concepts must teach.** Each concept explains what it is, why it matters downstream, and carries a `*Violation signal:*` line naming how a reader notices it being broken.
- **Prose, not diagrams, under `skills/`.** Those files are read by an agent at inference time, where a diagram costs tokens and renders as raw source. Diagrams belong in `README.md` and `reference/`.
- **ASCII only, no emojis**, in skill and reference files.

## Guardrails

Contributions must stay inside legal, ethical, open-source collection: published, filed, posted, or publicly observable material. Anything that teaches pretexting, solicitation of confidential information, or access behind an authentication boundary will be rejected on sight.

## What Never Enters This Project

- Client or customer names, in any file, ever
- Credentials, tokens, or keys
- Word, PowerPoint, Excel, PDF, or saved email files — those live in SharePoint
- Real competitive research about a named company, however well sourced

The last one surprises people. This Project teaches a method; it is not a place to store the output of running it.

These restrictions apply equally to files, issues, pull requests, comments, Discussions, Project items, and attachments. Describe the method, not your findings.
