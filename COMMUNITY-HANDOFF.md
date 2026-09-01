# Community and Public-Share Handoff

**For a maintainer or agent continuing this work. Read `CONSTITUTION.md` first.**

This document records the current community posture, the decision to defer a
GitHub Project, and the public-share checks for the 2026-09-02 webinar. It is a
continuation guide, not a promise to launch or maintain a community program.

## Current Decision

Do not create a GitHub Project board now.

Do not enable GitHub Discussions merely to make the Project look active. The
repository already has guided issue forms for concrete questions, field
reports, and skill proposals. Pull requests remain the place for reviewed
changes. That is enough surface area for the current stage.

If a GitHub Project is created later, it must be a bounded thematic initiative,
not a permanent backlog or a general task board. The long-term themes and entry
criteria live in `ROADMAP.md`.

## Current Community Model

| Surface | Current state | Job |
|---|---|---|
| README and Quickstart | Live | Explain the library and produce a first useful run |
| Issues | Enabled with guided forms | Hold method-level field reports, open questions, and skill proposals |
| Pull requests | Enabled and protected | Hold reviewed changes that pass the contribution test |
| Discussions | Intentionally off | Reconsider only when recurring conversations exceed what issues can hold |
| GitHub Project | Deferred | Create only for a bounded future theme |

Dean Peters (`@deanpeters`) is the moderator. The public response expectation
is: **Response times vary.**

## Why a General Project Board Is Deferred

A general board would add ceremony without adding a clear community job. It
would also risk looking like a delivery roadmap, which conflicts with the
Project's stated posture: directional possibilities are not commitments to
build, maintain, or deliver.

The right trigger is not "we have issues." The right trigger is a theme that
needs a temporary shared research surface, a defined contribution format, and a
clear destination for what the group learns.

Candidate long-term themes include:

- domain-specific extensions to sources, inference chains, taxonomies, and
  guardrails
- public practice or failure studies using well-known, rights-clear sources
- cross-domain research on judgment calls shared by product management,
  product marketing, pricing, sales enablement, market research, and
  competitive intelligence

These are not scheduled.

## Named-Company Research Boundary

A future theme about well-known companies needs a governance decision before it
opens. The current Project teaches a method; it does not store real competitive
research about named companies.

Public company case studies may be useful source material, but the durable
contribution must remain compatible with the Constitution. Possible safe
outputs include:

- a method-level finding supported by public, rights-clear sources
- a bibliography or source map that does not become a competitor dossier
- a synthetic worked or weak example that teaches the observed judgment
- a deliberately separate publication with its own review and rights decision

Do not seed a future Project with named-company research until that boundary is
resolved explicitly. A Project item, issue, comment, attachment, or Discussion
is a public surface.

## Webinar Handoff: 2026-09-02

### What to share

Use the default `main` branch:

`https://github.com/Productside/Productside-Market-Intelligence-Skills`

The shortest useful audience path is:

1. Read the opening premise and **Start Here** section in `README.md`.
2. Open `QUICKSTART.md` for the five-minute first run.
3. Show one worked example and one weak example from the same skill.
4. Point to `COMMUNITY.md` only if someone asks how to contribute.

The audience does not need the architecture, packaging pipeline, or community
governance before seeing a useful run.

### Recommended demonstration

Demonstrate one decision-shaped run, not the entire library. Good choices:

- `mi-router-market-intelligence` when the teaching point is that research
  stops without a named decision
- `mi-sweep-full-spectrum` when the audience wants the end-to-end collection
  and fusion motion
- `mi-fuse-all-source` when the teaching point is that six sources may collapse
  to two independent disciplines

Show the result before explaining the machinery. The most distinctive moments
are the search plan, the evidence labels, the independence test, the visible
gaps, and the final claims the user must not make.

### Contribution call to action

Do not announce a GitHub Project or Discussions. The accurate invitation is:

- run a skill
- report what the **method** caught or missed without posting the company or
  findings
- sharpen a weak example or identify a reference gap
- use the guided issue forms if there is a concrete question or improvement

The rule at the door remains: **Describe the method, not your findings.**

### Language to preserve

Describe these materials as **digital takeaways and worked examples that
demonstrate and extend Productside's teaching and advisory services**.

Do not describe the library as software, an application, a data service, or a
promise of future capability. Do not imply that Productside will respond on a
fixed schedule or accept every contribution.

## Verified Public State

Checked 2026-09-01.

| Check | Result |
|---|---|
| Visibility | Public |
| Default branch | `main` |
| Repository description | Names the 22 instructional skills and intended audiences |
| Issues | Enabled |
| Guided issue forms | Field report, open question or gap, skill proposal |
| Blank issues | Disabled |
| Discussions | Off by decision |
| GitHub Project surface | Disabled; no board was created during this work |
| Pull request template | Present |
| Branch protection | One approving review required on `main` |
| Content Guard | Green on current `main` |
| Validate library workflow | Green on current `main` |
| License | CC BY-NC-ND 4.0; commercial use requires prior explicit written permission |
| Moderator | Dean Peters |
| Response expectation | Response times vary |
| Open issues | None at time of check |
| GitHub releases | None; repository installation is the documented path |

## Safeguards Already in Place

- `CONSTITUTION.md` covers files, issues, pull requests, comments, Discussions,
  Project items, and attachments.
- `COMMUNITY.md` puts the method-not-findings boundary at the front door.
- Issue and Discussion form files carry safety and contributor-rights
  acknowledgements, even though Discussions are not currently enabled.
- `CONTRIBUTOR-TERMS.md` preserves contributor ownership and attribution while
  granting 280 Group LLC dba Productside durable rights to accepted work.
- `LICENSE`, `NOTICE.md`, `README.md`, plugin manifests, skill metadata, and
  prompt footers use CC BY-NC-ND 4.0.
- `scripts/test-library.sh` validates the public surface and builds deterministic
  clean archives.
- The Content Guard checks committed changes for forbidden file types,
  oversized files, credentials, and configured blocked terms.

The Content Guard does not inspect issue bodies or other live community text.
Human moderation remains the control on those surfaces.

## Long-Term Activation Gate for a Thematic Project

Before creating any future board, record:

1. The named research or contribution question
2. The theme boundary and explicit exclusions
3. The safe contribution format
4. The moderator
5. The destination for accepted findings
6. The closing condition

Only then choose fields, views, seed issues, or Discussion categories. Do not
create empty community furniture and then search for a reason to use it.

## Continuation Checks

Before a public share or release:

```bash
git status --short --branch
./scripts/test-library.sh
git diff --check
git ls-files sources | wc -l
```

The last command must return `0`. Report failures honestly. Do not repair an
unrelated failure under cover of release preparation.

`main` is protected. A change reaches it through a branch and pull request. Do
not create a release archive unless the task explicitly includes a release.
