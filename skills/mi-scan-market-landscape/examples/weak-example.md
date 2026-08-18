# Weak Example: The Map With No Spreadsheets On It

**Synthetic anti-pattern.** Intentionally flawed, and the flaws are hard to spot. It segments the market, maps a dozen players, names dynamics with citations, and identifies whitespace. It follows the template. It would pass a quick review, and the sizing model built on it counted the wrong population.

Same fictional market, scanned by a different analyst.

## The Artifact

### 1. Scope

The revenue operations platform market. Analysts size it at $12.6B globally, growing 18% annually.

### 2. Segmentation

| Segment | Definition |
|---|---|
| SMB | Under 100 employees |
| Mid-market | 100-1,000 employees |
| Enterprise | 1,000+ employees |

### 3. Player Map

**Direct (11):** Cartelane, Meridian, Northwind, and eight others, with positioning summaries and funding for each.

**Adjacent (1):** One CRM vendor, noted as "could potentially enter."

**Emerging (2):** Two seed-stage entrants.

### 4. Dynamics

The market is growing rapidly as companies increasingly prioritize revenue operations. Vendors are competing on integration breadth and AI-driven insights. Consolidation is expected as the category matures. Buyers are becoming more sophisticated.

### 5. Whitespace

- Vertical-specific solutions — opportunity
- SMB segment — underserved, opportunity
- Compliance-focused offerings — opportunity

### 6. Conclusion

The mid-market segment offers the strongest entry opportunity given the fragmented competitive landscape.

## Why It Passes a Quick Read

- Twelve players identified with positioning summaries and funding data — real research.
- Segmentation is clean, mutually exclusive, and immediately usable.
- A market size with a growth rate, sourced to analysts.
- Adjacent and emerging buckets both exist, which many scans omit.
- Whitespace is named specifically rather than gestured at.
- It reaches a clear entry recommendation.

## Why It Fails

**The substitutes and non-consumption bucket is missing entirely.** In the correctly-run version, a spreadsheet maintained by one analyst is named as the current state in eleven of nineteen buyer threads, and non-consumption holds an estimated 60-80% of the problem. Here, the bucket does not exist. *This is the discipline's central violation signal:* a player map containing only vendors, so the largest incumbent in the category is invisible.

The consequence is not academic. The sizing model built on this map counted companies in the vendor categories and produced a TAM that assumes the market is the set of firms who might switch vendors — when most of them have never bought anything. Every downstream number inherits that error.

**Segmentation is by company size, which is how vendors invoice, not how buyers think.** Buyers in this category group alternatives by the *job*: reconciling two departments' numbers, defending a forecast, unsticking handoffs. Size-band segmentation reproduces the vendor view, and it is the segmentation an analyst quadrant would give you for free. It also guarantees the scan cannot find the divergence between buyer language and vendor language — the finding that names an unclaimed category.

**The adjacent bucket has one entry, hedged.** "One CRM vendor, could potentially enter" understates where the actual threat lives. Two CRM vendors and two accounting platforms all own half the required data already, and two have signaled reconciliation on public roadmaps. The adjacent bucket is where a category like this gets eaten, and it received one line and a modal verb.

**The dynamics section is atmosphere.** "Growing rapidly," "increasingly prioritize," "competing on integration breadth and AI-driven insights," "consolidation is expected," "buyers are becoming more sophisticated." Every one of these sentences is true of nearly every B2B software category in nearly every year, and not one carries a citation. The rule asks for four *named* reads with evidence, and the correctly-run version finds a genuinely counterintuitive one: fragmenting at the low end while consolidating at the top, which points entry strategy in a specific direction.

**Every gap is an opportunity.** Three gaps, three opportunities, no dead zones. The SMB gap in particular is where three funded entrants died between 2021 and 2024 — it is empty for a reason, and the reason is that a spreadsheet is genuinely adequate when the pain is quarterly rather than daily. Calling it "underserved, opportunity" inverts the finding. *This is the whitespace violation signal exactly.*

**The market size is one analyst estimate, adopted.** $12.6B is the larger of two credible figures that differ by 3.1x on category definition. The smaller is not mentioned. A scan is not supposed to size anything, and adopting somebody else's number without its conflicting twin is the worst version of doing so.

**It ends with an entry recommendation.** "The mid-market segment offers the strongest entry opportunity" is a strategic conclusion reached from a map that missed the incumbent, mis-segmented the buyers, and understated the adjacent threat. A scan produces the map; the recommendation is what the map is *for*, made later, by someone accountable for it.

## What Makes This Hard to Catch

Absence has no shape. A player map with twelve vendors on it looks complete, and nothing in the document points at the empty bucket. The reviewer's question is "did they find the competitors," and the answer is yes — all of them. The one that matters is not a competitor in any sense the search would return, because spreadsheets do not have websites, funding rounds, or press coverage.

The size-band segmentation is similarly invisible. It is *correct*, it is mutually exclusive and collectively exhaustive, and it matches how every vendor in the space organizes its own site. It fails only against a standard most reviewers do not apply: whose model is this?

And the atmosphere reads as fluency. "Buyers are becoming more sophisticated" is the kind of sentence that sounds like the product of research, costs nothing to write, and cannot be wrong.

## Repair

Add the fourth bucket and go looking for it deliberately: ask what people with this problem who buy nothing do instead. Read buyer threads for the current state, not for vendor comparisons. Estimate the share as a range, label it Inference, and say what it rests on — that estimate is the most consequential number in the scan.

Re-segment from buyer language. Pull the jobs from reviews and forums and let the segments be named in the buyers' words, then set them against the vendor categories and write down the divergence.

Expand the adjacent bucket properly, with what entry would actually require for each player and what they have already signaled. Replace the dynamics prose with four named reads and four citations, and keep the counterintuitive one even though it complicates the story.

Re-judge each gap: who has already tried, what happened, and what would settle it. Name the SMB segment as a dead zone with the three failures behind it. Drop the analyst market size entirely, or report both conflicting figures and adopt neither. Then delete the recommendation and hand the map to sizing, snapshots, and positioning, which is what it is for.
