# Quickstart

## Install

```bash
/plugin marketplace add Productside/Productside-Market-Intelligence-Skills
/plugin install mintel
```

Skills appear as `mintel:<name>`.

## Your First Run, in Five Minutes

You have a meeting about a company you do not know.

```text
Use $mi-sweep-full-spectrum on Acme Corp. Competitor, showed up in two lost
deals, QBR is Thursday.
```

What happens:

1. It states whether it has web access, in one line. Without it, everything comes back labeled Assumption with a knowledge vintage, and nothing is invented.
2. It asks at most three setup questions — the decision, the relationship, and the time available — and skips any you already answered.
3. It shows a four-bullet search plan, identity first, and **continues unless you revise it**. You do not have to approve anything.
4. It sweeps seven disciplines in a fixed order, keeping each channel's findings in its own section.
5. It fuses them, collapsing signals that trace to the same origin before rating anything.
6. It ends in a call-ready brief: a sixty-second summary, three things worth saying, the questions you will be asked, and **the claims you must not make**.

The last section is the one to read first.

## If You Are Not Sure Which Run You Need

```text
Use $mi-router-market-intelligence — a competitor turned up in three lost
deals and my VP wants a read.
```

It fills six variables, refuses to proceed if you cannot name the decision this research will change, and routes you to the run that answers it. It collects nothing itself.

If you cannot name a decision, that refusal is the useful output. Research without a decision is a hobby.

## If You Already Have Evidence

```text
Use $mi-fuse-all-source. Pasting everything we've collected.
```

Fusion does not collect. It inventories what you supplied, collapses signals that share an origin, stacks confidence across genuinely independent disciplines, checks whether an announcement is actually funded, keeps conflicts as conflicts, and ends on responses rather than findings.

Expect it to tell you that your six sources are two disciplines. That is usually the most valuable thing it does.

## To Make It Compound

Any single run is disposable. The series is the asset.

```text
Use $mi-watch-competitors against acme-full-spectrum-2026-08-18.md.
```

The watch diffs against the stored prior run, applies a materiality bar, and reports only what cleared it. If nothing did, it says so in one line and stops — a monitor that always finds something has stopped filtering.

These runs are built to execute with nobody watching: the question budget proceeds on labeled assumptions, the search plan continues unless revised, and the schema is stable enough to diff. That is what makes them schedulable.

## What to Read Next

- [`README.md`](README.md) — the full library, organized by stage
- [`reference/disciplines.md`](reference/disciplines.md) — what each discipline collects, and where
- [`reference/fusion.md`](reference/fusion.md) — the independence test and confidence stacking
- Any skill's `examples/weak-example.md` — the anti-patterns are where the real teaching is
