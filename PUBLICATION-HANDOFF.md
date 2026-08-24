# Publication Handoff

**For an AI assistant or agent picking up this work. Read all of it before editing.**

This Project is private and is being prepared to go **public**. It was audited on 2026-08-23 against Productside's governance standard (`productside-launchkit` -> `docs/02-governance/02-09-positioning-licensing-and-terms.md`). **The content is clean and clears the IP bar.** The four content gaps that audit found are now closed. What remains is configuration that only a human org admin can do.

**Deadline: Monday, August 31, 2026.** This Project is the subject of a live Productside webinar on Wednesday, September 2, in which a collaborator opens a pull request against it and a maintainer merges it on camera. It must be public, with a working content guard and branch protection, before then.

**Delete this file as the final step.** It is internal housekeeping and should not ship publicly. See "Finish" below.

**Status as of 2026-08-24.** Validation passes at 147 files including the release gate. Three commits on `main`, all workflow runs green. Nothing from `sources/` is tracked.

---

## Do not do these things

- **Do not rename this Project.** `-Skills` is deliberate: `Productside-Market-Intelligence` would read as a service Productside sells, while `-Skills` reads as instructional material about the discipline. The name is also baked into the install command in `QUICKSTART.md`. Decided 2026-08-23.
- **Do not remove the `deanpeters/product-manager-prompts` references.** They appear in `README.md`, `CLAUDE.md`, `NOTICE.md`, `prompts/README.md`, and several `SKILL.md` files. They are deliberate attribution, documented in `NOTICE.md` as "by the same author and carried here with the same license." Removing them breaks the provenance chain.
- **Do not touch `sources/`.** It is gitignored on purpose as a provenance shelf and must never be committed.
- **Do not change the license.** CC BY-NC-SA 4.0 is correct here. Do not substitute MIT, Apache, or any other software license -- per 02-09, a software license would categorize these materials as software in writing, which is the exact argument Productside is trying not to lose. The deviation from the org default ND is deliberate and is now explained in `NOTICE.md`; do not "correct" it.
- **Do not describe anything here as code, software, an application, or a script.** See `CONSTITUTION.md` rule 5.

---

## Already done -- do not redo

The audit's Edits A through D were applied in commit `c2470f1` on 2026-08-23:

| Edit | What was done |
|---|---|
| A | `LICENSE` gained the `280 Group LLC dba Productside` copyright line and the plain-language warranty disclaimer above the Creative Commons text |
| B | `README.md` gained the canonical `## About These Materials` positioning statement, immediately before `## License` |
| C | `NOTICE.md` records why this Project is CC BY-NC-**SA** rather than the org default **ND** |
| D | `.github/CODEOWNERS` was repointed from the nonexistent `@Productside/maintainers` and `@Productside/owners` teams to `@deanpeters` (option 2 of the three offered) |

Earlier commits added `TRADEMARKS.md`, set publisher attribution across the plugin manifests to 280 Group LLC dba Productside, and made the Content Guard fail closed. All are done and verified.

---

## Read this before flipping to public

Two things interact badly and both were found on 2026-08-24. One is fixed; the other needs a human decision.

### The fork pull request problem -- fixed, but understand it

`.github/workflows/content-guard.yml` fails closed on a public Project when `BLOCKED_TERMS` is missing. GitHub **withholds secrets from workflow runs triggered by a pull request from a fork**, by design and with no way around it. Those two facts together meant every outside pull request against this Project would have gone permanently red once public -- including the one opened on camera during the webinar.

The guard now exempts fork pull requests: it warns there instead of failing, because failing would not be a safety property, just a broken gate. The compensating control is maintainer review before merge, plus the guard running with the secret on every push. The same fix was backported to `Productside/.github`, `Productside-Resources`, and `productside-launchkit/templates/content-guard.sample.yml` so all four copies behave identically.

### The webinar collaborator needs write access -- decide this

Current collaborators and their roles:

| User | Role |
|---|---|
| `deanpeters` | admin |
| `RyanCProductside` | admin |
| `cpetti2026` | admin |
| `kenkran` | **read** |
| `ralexin` | **read** |

There are no pending invitations; all five have accepted.

**A read-only collaborator cannot push a branch to this repository.** They can only fork and open a pull request from the fork, which is the path that gets no secrets. If the webinar's pull request is meant to come from `kenkran` or `ralexin`, either:

1. **Raise them to write**, so they push a branch here and the pull request runs with the secret and a fully green Content Guard, or
2. **Accept the fork path**, in which case the Content Guard will show a warning annotation rather than a clean pass on that run. It will not be red, but it will not say `No blocked terms found.` either.

Option 1 is the better demo. Decide before the rehearsal, not during it.

---

## Human-only, cannot be done by an agent

These require Productside org admin access and must happen **in this order**.

### 1. Scope the `BLOCKED_TERMS` organization secret to all repositories

**This is the single highest-consequence item, and it is still not done.** `gh secret list` on this repository returns nothing.

The secret exists and works -- `Productside/.github` and `Productside-Resources` both receive it -- but it is scoped to selected repositories, so a repository created after it was configured does not inherit it. That is why this Project's first run on 2026-08-18 reported success while checking nothing.

Organization Settings -> Secrets and variables -> Actions -> `BLOCKED_TERMS` -> Repository access -> **All repositories**. Scope it org-wide rather than granting this one repository, so the next new Project inherits it with no setup step. The policy is written up in `productside-launchkit/docs/02-governance/02-08-repository-operations.md`.

An agent cannot do this: it needs the `admin:org` token scope, and the working token carries only `gist`, `read:org`, `repo`, `workflow`. Granting that scope is an interactive browser flow. If you want an agent to finish it, run `gh auth refresh -h github.com -s admin:org` first.

**Verify before moving on.** Re-run the Content Guard and confirm the log reads `No blocked terms found.` with **no warning line above it**. That phrase on its own does not mean the check ran -- that is precisely how this stayed invisible for a week.

### 2. Flip the repository to public

Only after step 1 is verified. Flip first and every run goes red, including the check on the webinar's pull request.

Confirm at least one workflow run is green afterward.

### 3. Enable branch protection on `main`

Require a pull request before merging, and require one approval. Without this the webinar's review-and-merge segment is ceremonial, because a collaborator with write access could push straight to `main`.

**This cannot be done before step 2.** The API currently returns `Upgrade to GitHub Pro or make this repository public to enable this feature` -- branch protection is unavailable on a private repository on this plan. The ordering above is therefore forced, not preferred.

### 4. Confirm the webinar collaborator's access

See "The webinar collaborator needs write access" above. All five collaborators have accepted; the open question is the read-versus-write decision for whoever opens the pull request.

### Optional, and free only while private

All three commits are authored `Dean Peters` under two different addresses -- `deanpeters@gmail.com` on two, `peters.dean@gmail.com` on one. Once public that is permanent and visible. With three commits it is trivial to rewrite now. This is a preference, not a requirement.

---

## Verify

After any content edit:

```bash
./scripts/test-library.sh
```

It must pass. Then confirm nothing from the provenance shelf was staged:

```bash
git status --short
git ls-files sources | wc -l    # must be 0
```

---

## Finish

**Delete this file and commit the deletion** before the Project goes public. It is internal preparation notes, it names collaborators and their access levels, and it has no place in a published Project.

It is committed here rather than left untracked so that the work survives a lost working directory and so the next agent picking this up sees it. That convenience expires the moment the repository goes public.
