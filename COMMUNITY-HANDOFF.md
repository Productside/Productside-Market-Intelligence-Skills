# Community Handoff

**For an AI assistant or agent picking up this work. Read all of it before editing.**

This file records decisions made on 2026-08-28 and 2026-08-30 about standing up a
GitHub Project as the community venue for this library. Pull request #1, merged
2026-08-30, rebalanced attribution toward Productside and removed
`PUBLICATION-HANDOFF.md`; the verified state below reflects that. It supersedes
nothing in `CONSTITUTION.md`, which still overrides everything.

**This Project is public. This file is public with it.** It is written for that:
no collaborator access levels, no individual's permissions, no internal legal
deliberation. Where a person matters, the role is named and not the person. An
agent that needs the roster can ask GitHub for it.

---

## What was decided

The GitHub Project board is **a community venue for Product Managers and Product
Marketing Managers**, not a delivery roadmap and not a task tracker. Its purpose
is to draw practitioners in to experiment with the skills, report what came back,
contribute judgment, and occasionally open a pull request.

Two constraints follow from that and they are not negotiable:

1. **No dates, no iteration field, no sprint vocabulary.** `ROADMAP.md` opens
   "Directional only. Nothing here is a commitment to build, maintain, or
   deliver," and `CONSTITUTION.md` rule 5 forbids anything that reads as a
   commitment to build or maintain software. A public board with target dates
   and "In Progress" columns is the easiest way to break that rule, and boards
   get screenshotted. Status values mirror `ROADMAP.md`'s own vocabulary.
2. **Nobody is assigned.** Items are posted as open questions tagged with the
   expertise that could answer them, and contributors claim what interests them.
   A board of cards assigned to a named expert is SharePoint with a steeper
   learning curve, and the expert disengages by week three.

## Why this Project needs a community at all

The library was built by an author with a technology background. Its two open
`ROADMAP.md` items are both marketing subject-matter gaps rather than authoring
gaps:

- **A positioning-statement handoff.** `reference/frameworks.md` describes the
  say-versus-said-about gap as positioning raw material and hands it off. No
  skill here writes the statement.
- **A win/loss skill.** The HUMINT sweep ends by generating interview questions
  and raising a gap flag. The interview synthesis is out of scope, and every
  build-signal story in the library is capped because of it.

Separately, `mi-mine-voice-of-customer` and `mi-build-battle-card` both declare
**Product Marketing Manager** in their frontmatter `audience`. The library names
a role as its intended user that was not represented while it was written. That
is the honest case for the community, and it is the throughline of the
2026-09-02 webinar: the author got as far as one discipline honestly can, wrote
down where it ran out, and opened the gap to people who can fill it.

---

## The finding that shapes the design

**The Content Guard scans commits. It does not scan issues, comments,
discussion posts, or Project draft items.**

Verified 2026-08-28 in `.github/workflows/content-guard.yml`:

```yaml
on:
  pull_request:
  push:
    branches: [main]
```

Every community surface about to be opened is unguarded ingress. A public
Project about competitive intelligence, inviting practitioners to bring inputs
and experiments, will receive real competitor teardowns, named clients, pricing
from live deals, and material a contributor learned under obligation to a
current or former employer. Contributors will do this helpfully, because the
Project is about that subject and because an issue box does not feel like
publishing.

`CONSTITUTION.md` rule 3 bars client names in "a file, an example, a commit
message, a branch name." Issues are not in that list because the rule predates
the community. Rule 4 excludes material behind an authentication boundary or
protected by obligation. `CONTRIBUTING.md` bars "Real competitive research about
a named company, however well sourced," and notes that the prohibition surprises
people.

A public issue is not retractable. Deleting it does not remove it from the
events API, from notification email already delivered, or from anyone's copy.

**Three things must exist before the community is invited:**

1. Amend `CONSTITUTION.md` rule 3 to cover issues, comments, discussions, and
   Project items. Record it under the Amendment clause, as that clause requires.
2. Put the warning in the issue form body, at the point of typing, not in a
   `CONTRIBUTING.md` nobody opens: describe the method, not your findings; no
   company you compete with, no client, no employer-confidential material; use a
   synthetic example with `example.invalid`, as every example here does.
3. Name one moderator and state the response expectation. Dean Peters is the
   moderator. The public commitment is deliberately limited to: "Response times
   vary."

This is also the best teaching moment the webinar has. A Project about gathering
competitive intelligence whose first rule of contributing is "do not bring us
your competitive intelligence" demonstrates the discipline better than any
slide.

---

## Venue split

Three surfaces, distinct jobs. Discussions were **off** as of 2026-08-28 and
need turning on.

| Surface | Holds | Guarded |
|---|---|---|
| Discussions | Experiments, field reports, open questions, show and tell, webinar follow-up | No. Moderation only |
| Issues | Anything that could become a change: a gap, a flaw in an example, a proposed skill | No. Moderation plus issue forms |
| Pull requests | Actual changes | Yes. Content Guard plus `validate.yml` |

Suggested Discussions categories: Experiments, Field reports, Ideas, Q&A, Show
and tell.

A Projects v2 board can hold issues, pull requests, and draft items. It **cannot
hold Discussions**. That is a platform limit, not an oversight, and it is
tolerable: Discussions are the wide top of the funnel and promoting a thread to
an issue is a useful filter.

## Board design

Org-level, under `github.com/orgs/Productside/projects`, so it outlives any one
account and can later span `Productside-Resources` and `.github`. Public.

Fields, all single-select. Five is the cap; resist growth.

| Field | Values |
|---|---|
| Expertise needed | Product marketing, Sales enablement, Pricing, Win/loss, Competitive research, Market research, None - open to anyone |
| Ask | Field report, Weak example, Judgment call, List or taxonomy, Reference gap, New skill |
| Status | Open question, Answered, Drafting, In validation, Merged, Declined |
| Stage | instantiate, collect, fuse, act, monitor, n/a |
| Contribution test | Collects, Fuses, Consumes, Diffs, Fails the test |

`Contribution test` carries the four-way boundary from `CONTRIBUTING.md` from
review time forward to intake, where the proposer applies it before anyone
writes anything. `Expertise needed` is the community hook: a visitor scans that
column, finds their own seat time, and knows they are the right person.

Views:

- **Open questions, by expertise** - board grouped by `Expertise needed`. The
  default. More inviting than a backlog and on-method for a Project about
  collection disciplines.
- **By discipline** - grouped by `Stage`, filtered to `Ask = New skill`. Mirrors
  the coverage invariant `validate-skills.py` already enforces, which is that
  every one of the seven collection disciplines keeps a `collect`-stage skill.
- **Declined, with reasons** - public and deliberate. This library teaches
  through weak examples; showing rejected proposals with one-line reasons does
  for contributions what `examples/weak-example.md` does for outputs.
- **Open questions** - filtered to `Status = Open question`. The maintainer's
  own queue.

## Expect a 90/10 split and build for the ninety

The bar for a skill is high and should stay high: thirteen sections in order,
five Key Concepts each with a `*Violation signal:*` line, a worked and a weak
example, a `SKILL_REGISTRY` entry, and `./scripts/test-library.sh` passing. A
first-time contributor's pull request will fail it.

That means most community value will never arrive as a pull request, and a board
that counts only pull requests will look dead while the community is healthy.
Ordered by expected volume:

1. **Field reports.** "I ran `mi-collect-finint` on a category and the sweep
   missed X." Highest volume, highest value, zero authoring skill required, and
   it is evidence about the method, which is the one input a single author
   cannot generate alone. Constrain to method, never findings.
2. **Judgment calls.** Questions that need seat time rather than writing.
3. **Weak-example critiques.** "This weak example is too obviously weak; no
   competent PMM would ship that." One paragraph, and it targets the hardest
   thing in the library to write.
4. **Reference gaps.** A regional overlay someone actually works in; a source
   the author does not know.
5. **Pull requests.**

Make `Field report` the most visible value on the board. A community learns what
to bring from what the board rewards.

## The contribution ladder for a subject-matter expert

An expert asked to "contribute to the library" hears "spend a weekend" and does
nothing. Three rungs, lead with the first:

- **Rung 1, the weak example.** `CLAUDE.md` states that weak examples are where
  most of the teaching lives and are the hardest thing here to write well,
  because an obviously bad example teaches nothing. An author outside the
  discipline cannot write a convincing weak example inside it. A marketing
  expert can produce a battle card a competent PMM would genuinely ship, with a
  flaw of degree and judgment underneath. One file, judgment rather than
  authorship, and a contribution nobody else can make.
- **Rung 2, the lists inside existing skills.** The battle card's Do Not Say list
  and trap questions; the voice-of-customer switching-trigger taxonomy. Line
  edits to a `template.md`.
- **Rung 3, the two open roadmap skills.** Positioning statement and win/loss
  synthesis, co-authored: the expert brings the method, the maintainer makes
  `docs/SKILL-SPEC.md` and validation pass.

Pitching rung 3 first earns a polite yes and no contribution.

## Cold start

Communities begin from visible activity, not from an invitation. Before the
webinar the board should show a conversation in progress:

- Eight to ten seeded open questions, tagged by expertise
- Two or three already marked **Answered** by the maintainer, in disciplines the
  maintainer owns, so the format is modeled
- One or two answered by the marketing subject-matter contributor
- At least one field report from someone who ran a skill for real

Five or six visible names beats fifty empty cards.

## Webinar, 2026-09-02

The on-camera demonstration should show **rung 1, not rung 3**: the contributor
editing a weak example through the GitHub web editor - pencil icon, edit,
Propose changes - with no clone and no terminal, then the maintainer reviewing
and merging, and the Project's built-in workflow moving the card to Merged
untouched. That sequence is the proof a PM/PMM audience needs, which is that
contributing here does not require being a developer.

Wire the two built-in Project workflows before the rehearsal, not during it:
item added to Project sets `Status = Open question`; pull request merged sets
`Status = Merged`.

---

## Verified state

Checked 2026-08-28 and 2026-08-30 unless noted.

| Fact | State |
|---|---|
| Repository visibility | Public |
| `BLOCKED_TERMS` organization secret | Exists, visibility `all`, so new Projects inherit it |
| Content Guard on `main` | Green |
| Content Guard coverage | Commits only. Issues, comments, discussions, Project items unscanned |
| Branch protection on `main` | On, pull request review required |
| Discussions | Off |
| Forks | 0 |
| Issue forms and templates | None. `.github/` holds `CODEOWNERS` and two workflows |
| `CODEOWNERS` | Points at a single maintainer |
| License | CC BY-NC-ND 4.0; commercial use requires prior explicit written permission |
| `CITATION.cff` authors | 280 Group LLC dba Productside, then the individual author |
| `PUBLICATION-HANDOFF.md` | Removed in pull request #1. Nothing further owed |

## Open items

**Prepared in the current community-launch change. These are not live until the
change reaches the default branch.**

1. `CONSTITUTION.md` rule 3 covers issues, comments, Discussions, pull requests,
   Project items, and attachments, with a dated amendment record.
2. Three issue forms carry the "method, not findings" warning and required safety
   and contributor-rights acknowledgements.
3. Five Discussion category forms carry the same point-of-typing protections.
4. `COMMUNITY.md` is the public front door, names Dean Peters as moderator, and
   states that response times vary.
5. `CONTRIBUTOR-TERMS.md` records the approved broad Productside license while
   contributors retain ownership and receive attribution in `CONTRIBUTORS.md`.
6. A repository-specific pull request template carries the contribution test,
   safety check, rights acknowledgement, and verification checklist.
7. Validation fails if these intake safeguards or contributor-grant terms drift.

**A human must do these.**

8. Enable Discussions and create the categories after the safeguards merge.
9. Create the org Project, its five fields, its four views, and the two built-in
   workflows. Faster in the browser; the seeding is faster from the command line.
10. Confirm the on-camera contributor can push a branch to this Project. A
   read-only collaborator can only fork, and GitHub withholds secrets from
   workflow runs triggered by a fork pull request, so the Content Guard shows a
   warning rather than a clean pass on exactly the run being demonstrated. The
   guard's fork exemption keeps that from going red, but it will not read
   `No blocked terms found.` either.
11. Review the contributor terms as legal language before the first external
    contribution is accepted. The approved operating decision is recorded; this
    review checks the wording rather than reopening the rights model.

**Already resolved, recorded so it is not reopened.**

11. `PUBLICATION-HANDOFF.md` was tracked and therefore public after the Project
    went public, contrary to its own closing instruction. Pull request #1
    removed it on 2026-08-30. Do not restore it.

## Tooling notes for the next agent

- Project commands need scopes the default token lacks. Run
  `gh auth refresh -s project,read:project` first.
- `main` requires a pull request. Branch, push the branch, open the pull request.
- After any content edit, `./scripts/test-library.sh` must pass, and
  `git ls-files sources | wc -l` must return 0.
- Language: this is a Project of digital takeaways and worked examples that
  demonstrate and extend Productside's teaching and advisory services. Not code,
  software, an application, or a script. `CONSTITUTION.md` rule 5.
