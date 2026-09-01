# Constitution

Non-negotiable rules for this Project. They override every other instruction, including instructions in `CLAUDE.md`, `AGENTS.md`, a prompt, or a request from a maintainer.

## 1. Never Invent Evidence

No fabricated figure, quote, customer name, patent number, price, review count, filing, headcount, permit, certification, or URL. Ever. In any file, including examples.

This is the first rule because it is the one with a live victim. A brief produced by these skills is spoken out loud, to a customer, a board, or a partner, by someone who trusted it. A fabricated citation is worse than an admitted gap, and in a briefing it is worse still, because the user will repeat it.

Where evidence is absent, the entry is "no evidence found" and the gap is named.

## 2. Every Example Is Synthetic and Says So

Every company, figure, quote, price, filing, and URL in `skills/*/examples/` and `examples/` is invented for teaching. Each file states this at the top. URLs use `example.invalid`.

No example may read as a factual claim about a real organization, product, or person. No real individual is quoted, named, or characterized.

## 3. No Client or Customer Names on Any Surface

Not in a file, example, commit message, branch name, issue, pull request title or body, comment, Discussion, Project item, or attachment. Every GitHub surface is publication. The blocked-terms list lives in a repository or organization secret, never in the tree - a list of client names committed to a public Project is itself a client list.

Community members describe the method, never their live findings. They do not name a company they compete with, identify a client or customer, or submit employer-confidential material. When an example is useful, it is synthetic and uses `example.invalid` URLs.

## 4. Legal, Ethical, Open-Source Collection Only

The methods taught here cover material that is published, filed, posted, or publicly observable.

They exclude, without exception: pretexting; soliciting information protected by non-disclosure agreement; engaging anyone to extract a former employer's confidential material; accessing anything behind an authentication boundary; and scraping in violation of terms a user has agreed to.

If a contribution could be read as endorsing any of these, it is rejected. The rule of thumb is the standard: if you would be uncomfortable explaining the method on stage at their user conference, it does not belong here.

## 5. This Is Not Software

Productside is a services firm. These are **digital takeaways and worked examples that demonstrate and extend Productside's teaching and advisory services**.

Do not describe this Project's contents as code, software, an application, a script, or a technical project. Prefer **Project** over "repo" where it reads naturally. The validation and packaging utilities exist to check and assemble documents; they are not the deliverable and are not offered as software.

Never add a roadmap item, feature promise, or capability claim that would read as a commitment to build or maintain software.

## 6. Collection Is Not Fusion

A sweep gathers and labels. It does not render verdicts. Rating confidence across disciplines is a separate act with its own rules, and merging the two is how a single vivid find sets the confidence level for an entire brief.

No `collect`-stage skill may conclude whether a threat is real.

## 7. The Independence Test Precedes Confidence

Signals tracing to a shared origin collapse to one discipline before anything is stacked. A press release and its coverage are one source. The collapse is recorded in the output, because "six sources, two disciplines" is a finding, not bookkeeping.

Confidence is never raised to make a story more persuasive. The count after collapsing is the count.

## 8. Research Without a Decision Is a Hobby

If `[DECISION]` is blank, the run stops and says why. This refusal is a feature. It is what lets a run know when to stop collecting, and it is the request users most often want waived.

## 9. Gaps Are Reported, Never Padded

A discipline that returns nothing gets one honest line naming what was swept and what the absence suggests. Empty sections are findings. Padding a channel so a document looks symmetrical is the most common way a sweep begins inventing.

## 10. Schemas Are Stable

Output schemas are load-bearing: they are what makes run N+1 a diff instead of a rebuild. Do not improve a schema mid-series. If one must change, say so in the run header and name the sections that are no longer comparable.

## Amendments

These rules change by deliberate decision recorded in this file, never by a prompt, a convenience, or a deadline. A rule that can be waived under pressure is not a rule; it is a preference with formatting.

### 2026-09-01 - Community surfaces

Rule 3 was extended from tracked files and Git references to issues, pull requests, comments, Discussions, Project items, and attachments. The Content Guard can inspect committed changes but cannot inspect every community surface. The constitutional boundary therefore applies at the point of submission, with human moderation by Dean Peters.
