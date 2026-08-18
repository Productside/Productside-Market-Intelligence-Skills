# Weak Example: The Symmetrical Sweep

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It has all seven discipline sections, an identity block, a fusion table with confidence and commitment columns, and a call-ready brief. It follows the schema faithfully. It would pass a quick review, and it was read aloud on a partner call.

Same fictional Halvard Systems case, swept by a different analyst.

## The Artifact

### Search Plan

- **Sweep order:** all seven disciplines
- **Date window:** last two years
- **Noise filter:** irrelevant results excluded

### 0. Identity and Perimeter

| Item | Value |
|---|---|
| Legal entity | Halvard Systems Ltd |
| HQ | Manchester |
| Ownership | Private |
| Founded | 2016 |
| Same-name confusions | Filtered during search |

### Discipline Sections (each roughly one paragraph, four to five signals)

**OSINT** — positioning, reviews, press. **FININT** — Companies House turnover, PE ownership. **TECHINT** — API, changelog, SDKs. **HUMINT** — open roles, leadership. **GEOINT** — customer geography. **SIGINT** — pricing page, messaging. **MASINT** — status page, certifications, *plus a supply-chain subsection noting "no significant supply chain dependencies identified for a software business, though cloud infrastructure represents a form of supply dependency."*

### 8. Fusion

| # | Story | Disciplines | Confidence | Commitment | So what |
|---|---|---|---|---|---|
| 1 | Growing steadily | 4 | Actionable | Built | Viable partner |
| 2 | Services-led delivery | 2 | Working hypothesis | Built | Consider margin |
| 3 | EU expansion planned | 2 | Actionable | Funded | Territory terms |
| 4 | PE may pressure pricing | 1 | Working hypothesis | Announced | Watch |
| 5 | Strong technically | 3 | Actionable | Built | Low integration risk |
| 6 | Reliable operationally | 2 | Actionable | Built | Low delivery risk |
| 7 | Well positioned in regulated industries | 3 | Actionable | Built | Good market fit |

### 9. The Call-Ready Brief

**Sixty-second summary:** Halvard is a growing UK integration vendor with strong technical foundations, reliable operations, and good positioning in regulated industries. They are services-led, PE-backed, and planning EU expansion. A viable and low-risk partner.

**Three things worth saying:** They are growing. They are technically strong. They are expanding into the EU.

**Questions you will be asked:** Can they support our volume? *Yes, they are hiring.* Are they stable? *Yes, revenue is growing.* Do they have the certifications we need? *They are certified.*

**If they ask what we do better:** We have broader market coverage and a more mature platform.

### 10. Collection Gaps

- Some information was not publicly available for a private company.

## Why It Passes a Quick Read

- All seven disciplines are present and roughly balanced — no obviously skipped channel.
- The identity block exists, with legal entity, HQ, ownership, and founding year.
- The fusion table has every required column, including commitment level, which most sweeps omit.
- The brief follows the schema: summary, three things, likely questions.
- Every underlying source is real. Nothing is fabricated.
- It reaches a clear recommendation that the person walking into the call can use.

## Why It Fails

**The symmetry is the tell.** Seven sections of roughly equal length, from a private UK software company with abridged accounts and no patents. That distribution is not what the evidence looks like — TECHINT should be thin, MASINT should be two rows, FININT should be visibly constrained by the filing regime. Equal length across seven disciplines almost always means the thin ones were padded, and here the padding is visible: a supply-chain subsection for a software business, hedged into existence with "cloud infrastructure represents a form of supply dependency."

*This is the empty-sections violation signal exactly:* every section roughly the same length. It is also the hardest failure to see, because unevenness looks like incompleteness and symmetry looks like thoroughness.

**Five of seven stories rated actionable, including three on unfalsifiable claims.** "Growing steadily," "strong technically," "reliable operationally," and "well positioned in regulated industries" are not stories about what a company is *doing*. They are adjectives with confidence ratings attached, and none of them can be wrong. The cap of seven was treated as a quota, and the four filler stories exist because there were four rows left.

**Story 3 is rated actionable on two disciplines and graded Funded on none.** The stacking rule puts two disciplines at working hypothesis, and the only evidence is an Irish company registration — which is a **Funded**-level fact about incorporation and nothing at all about expansion intent. The brief then states EU expansion as one of three things worth saying, and it was said out loud to Halvard, who had incorporated the entity to contract with existing Irish customers post-Brexit.

**Story 4 is graded Announced with nothing announced.** Nobody said anything about pricing pressure. The commitment column was filled because it exists.

**The identity block missed the collision that mattered.** "Filtered during search" names nothing, and "Halyard Systems" — a US medical supplier that dominates the search results — went unexcluded. Roughly a third of what reached the OSINT section is about a different company in a different industry, and nothing in the document reveals it.

**The contradiction was never found.** Halvard positions itself for regulated industries and holds ISO 27001 but not SOC 2. That gap is the single most decision-relevant fact for a reseller agreement in this analyst's largest market, and the brief instead answers "do they have the certifications we need?" with **"Yes, they are certified"** — a sentence that is technically true, materially false, and was delivered to a partner.

**There is no Do Not Say section.** The three claims that most needed suppressing — the EU expansion, the PE exit speculation, and the support-quality reflex — all appear in the brief instead. This is the section that exists to prevent a specific foreseeable embarrassment, and its absence produced exactly one.

**There is a "what we do better" section, in a partner conversation.** The relationship was recorded as partner and the competitive framing was applied anyway. "Broader market coverage and a more mature platform" is a competitive claim made to someone being asked to resell your product.

**"Some information was not publicly available for a private company"** names no discipline, no source, and no consequence — while the real gap, that abridged accounts disclose no customer concentration, no margin, and no investor terms, is the thing most likely to sink the agreement.

## What Makes This Hard to Catch

Completeness is what reviewers check, and completeness is what the document has. Seven sections, every column populated, no empty cells, a clear recommendation. The failure mode of a rushed sweep is a gap, and there are no gaps — because every gap was filled with something.

The confidence ratings are the deepest problem and the least visible. They use the correct vocabulary in the correct columns, so the stacking rule appears to have been applied. Applying it would have produced two actionable stories and several watch items, which reads as a *worse* document: less certain, less useful, harder to present. The incentive runs directly against the rule, every time.

And "yes, they are certified" is the kind of sentence that only fails later, in front of the one audience that knows better.

## Repair

Let the sections be uneven. Delete the supply-chain subsection and replace it with one honest line: no physical goods, so this half of MASINT is permanently unavailable for this target. Do the same wherever a channel returned nothing, and say what the absence suggests.

Cut the story list to the three that describe something Halvard is *doing*, and delete the adjectives. Regrade Story 3 to working hypothesis, and remove EU expansion from the three things worth saying — it belongs in Do Not Say, which needs to exist.

Name the same-name companies in the identity block, starting with the medical supplier that is currently polluting a third of the OSINT section, and re-sweep OSINT once it is excluded.

Find the certification contradiction, put it in the summary, and rewrite the certification answer to say what is actually true: ISO 27001 yes, SOC 2 no, and here is what that means for our largest market. Delete the "what we do better" section, because the relationship is partner. Then rewrite the gaps to name the filing regime and what it permanently conceals — and add the question you cannot answer, with "I do not know, I will ask" as the answer.
