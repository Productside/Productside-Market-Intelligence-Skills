# Guided Context Capture: Three Transcripts and One Anti-Pattern

**Synthetic teaching material.** "Northwind Analytics" and "Cartelane" are fictional companies. The interaction shapes are real; nothing here should be read as a claim about an actual business.

This file shows the interaction contract in [Guided Context Capture](../reference/guided-context-capture.md) doing its job in all three modes, and then failing in a way that looks like it worked. Read the anti-pattern last and slowly. It is the one you will actually produce.

---

## Transcript 1 — Guided

The user has a partner call in three hours and knows almost nothing about the counterparty.

> **User:** `Use $mi-sweep-full-spectrum on Cartelane.`

> **Skill:** I have web access, so I will research live and cite URLs with dates.
>
> This is a full-spectrum sweep: seven collection disciplines on one company, fused with confidence stacking, ending in a call-ready brief. Standard depth runs about an hour. I will stop at the brief and a Final Step block — I will not change any artifact on your behalf.
>
> Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**.

> **User:** `1`

> **Skill:** `Setup Q1/3` — What decision will this sweep change?
>
> 1. Whether to partner, and on what terms
> 2. How to position against them in deals
> 3. Whether their announced platform move threatens our roadmap
> 4. Other (specify)
>
> This one matters more than the other two. A partner sweep spends its time on their commercial model and dependency risk; a competitive sweep spends it on their pricing and their weak flank. Same company, different hour.

> **User:** `1 — we're deciding whether to sign a reseller agreement.`

> **Skill:** `Setup Q2/3` — Who signs the check in the market you would both be selling into? That drives which review sites, job titles, and conferences are worth sweeping.
>
> 1. IT and security leadership
> 2. Finance and operations leadership
> 3. Line-of-business product or marketing leadership
> 4. Other (specify)

> **User:** `2`

> **Skill:** I have what I need — you named the decision and the buyer, and the geography is discoverable from their filings, so I will not spend a question on it.
>
> **Search plan** (continuing unless you revise):
>
> - **Identity first:** legal entity, ownership status, tickers, subsidiaries and brands, and the same-name companies I will exclude
> - **Sweep order:** OSINT, FININT, TECHINT, HUMINT, GEOINT/DEMOINT, SIGINT, MASINT — fixed, then fusion
> - **Date window:** 24 months, with filings back three years for Risk Factors diffing
> - **Noise filter:** exclude the identically named logistics firm in Ontario; collapse press-release recycling to a single source; ignore the 2021 acquisition that closed and has been re-reported twice since

Note what happened. Two questions, not three. The third was skipped because the answer was publicly discoverable, and asking for it would have been burden-shifting — the exact work the run exists to perform. The plan named the same-name company *before* collecting, which is where that error costs one line instead of the whole sweep.

---

## Transcript 2 — Context dump

The user has been collecting for two weeks in a spreadsheet and wants it reconciled.

> **User:** `Use $mi-fuse-all-source. Pasting everything we have.` *[pastes 40 lines of findings]*

> **Skill:** I have web access, but fusion does not collect. I will reconcile what you supplied and flag where a targeted gap-fill would help.
>
> **Extracted into the signal inventory — 23 signals across 5 disciplines.**
>
> | Account | Count | Notes |
> |---|---|---|
> | Found in the paste | 18 | Signal, source, and date all present |
> | Inferred from the paste | 5 | You wrote a read, not an observation; I have logged the read as Inference and left the underlying signal blank |
> | Still missing | — | GEOINT/DEMOINT and MASINT hold zero signals |
>
> **Provenance flags.** Six of your 18 sourced signals carry no URL — three hiring counts, two pricing figures, and the "CFO comment on margin." I have tagged all six as **Assumption**, not Fact. A signal whose source I cannot check is an Assumption no matter how confidently it was pasted, and two of those six are currently carrying a story.
>
> One question, not three: your paste answers the rest.
>
> `Setup Q1/3` — Have win/loss interviews been run this cycle? It changes how I weight the two build-signal stories, and nothing in the paste tells me.

> **User:** `No, last round was 8 months ago.`

> **Skill:** Then I will cap the build-signal stories at working hypothesis and say why in the verdict. Public signals infer why deals move; only the interviews know.

The dump did not skip the contract — it *satisfied* most of it. What the mode changes is which questions remain worth a turn. What it must never change is the provenance discipline: six unsourced lines got demoted, in the open, before anything was stacked.

---

## Transcript 3 — Best guess

A scheduled run fires with nobody watching.

> **Scheduler:** `Use $mi-watch-competitors on the analytics watchlist.`

> **Skill:** No human in the loop, so I am running in best-guess mode against stored defaults and labeling every assumption.
>
> **Assumed:** prior run `analytics-market-watch-2026-07-14.md` is the baseline; window is the 35 days since; scope is the three competitors on the stored watchlist; materiality bar as stated in `monitors.md`.
>
> **Search plan:** pricing pages against last capture → homepage and positioning diffs → changelogs → job posting deltas → filings and leadership → certifications. Continuing.
>
> *[run executes]*
>
> **No material change this run.** One line, and stopping.
>
> Cartelane added two customer logos and rewrote a hero paragraph without changing a claim. Both sit below the materiality bar. Runs with no material change: 2 consecutive.

This is the mode's real test, and the run passed it by producing almost nothing. A monitor that always finds something has stopped filtering. Volume is the tell, not the achievement.

---

## The Anti-Pattern — a run that satisfied every rule and taught nobody anything

**This is the failure mode to study.** It is not sloppy. It followed the contract closely enough to pass a review.

> **User:** `Use $mi-collect-humint on Northwind Analytics.`

> **Skill:** I have web access. This is a HUMINT collection sweep — hiring, leadership, sentiment, win/loss framing — ending in a fusion-ready signal inventory. Up to three setup questions. Choose **1. Guided**, **2. Context dump**, or **3. Best guess**.

> **User:** `1`

> **Skill:** `Setup Q1/3` — What decision will this collection feed?
>
> 1. Roadmap prioritization
> 2. Battle card refresh
> 3. Threat assessment
> 4. Other (specify)

> **User:** `1`

> **Skill:** `Setup Q2/3` — How many people does Northwind employ, and roughly how many are in engineering?

> **User:** `I don't know, that's kind of why I'm here.`

> **Skill:** `Setup Q3/3` — What are their current open roles?

> **User:** `...also why I'm here?`

> **Skill:** Understood, proceeding on assumptions.
>
> **Search plan:** leadership roster → open roles by function → departures → sentiment → public statements. Date window: 12 months. Noise filter: exclude same-name companies. Continuing.
>
> *[run executes, produces a well-formed inventory with 14 sourced signals, five ranked inference chains, a watch-items section, and a correct Final Step block]*

### Why It Passes a Quick Read

Three questions, not four. Progress labels honest. A search plan shown before collecting, with a noise filter. It proceeded rather than blocking when the user could not answer. The output carried real URLs, evidence labels, and the right schema. Every mechanical rule in the contract was satisfied, and the artifact at the end is genuinely usable.

### Why It Fails

**Questions 2 and 3 were burden-shifting.** Headcount and open roles are the *output* of a HUMINT sweep, not its input. The skill spent two-thirds of its question budget asking the user to perform the collection, then ran the collection anyway. The user noticed. Most users do not — they apologize for not knowing, and the run has quietly taught them that they should have.

**The budget was spent, not saved.** The contract caps questions at three; it does not require three. Question 1 was the only one that changed the artifact. The right move was "I have what I need" and straight to the search plan — which is what Transcript 1 did with a harder engagement.

**The questions that mattered were never asked.** For a roadmap decision, the two that change the output are whether win/loss interviews are current, and which capability the user suspects is being staffed. Without the first, every build-signal story in the sweep is over-rated. Without the second, the sweep counts postings against no hypothesis.

**The noise filter was decoration.** "Exclude same-name companies" names no company. A filter that does not name what it is filtering has not been applied; it has been mentioned.

### What Makes This Hard to Catch

Every visible marker of a disciplined run is present, and the deliverable is fine. Reviewers check whether the contract was followed, and it was — to the letter, in the order specified, within budget. The contract's mechanical rules are easy to audit and its purpose is not. Nothing in the transcript looks like a failure until you ask what each question bought, and that question does not appear on any checklist.

The tell is subtle and worth memorizing: **the user answered two questions with "that's why I'm here."** When that happens, the run asked for its own output.

### Repair

Before each question, ask what changes in the artifact if the answer flips — and whether you could find the answer yourself in less time than it takes to ask. Headcount and open roles fail both tests. Replace them with the two the human uniquely holds: win/loss currency, and the suspected `[CAPABILITY]`. Then name the same-name companies in the noise filter, or drop the bullet and say the filter was not needed.

Spending a question you did not need is not free. It costs the user's trust that you know which half of this work is yours.
