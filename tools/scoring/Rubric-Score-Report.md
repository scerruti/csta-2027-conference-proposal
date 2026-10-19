# CSTA 2027 Proposal Rubric Score Report

## Scope

Scores of record from round six, the first round on the rebuilt proposals, following the [blind scoring procedure](Scoring-Instructions.md#blind-scoring-required-before-each-report).

- **Pinned commit:** `bd1c53733feef158dfb760101029b04e8f5989a1`. Reviewers read a snapshot exported from this commit, not the working tree.
- **Review date:** 2026-10-18.
- **Structure check:** `check_submission.py` passed on both proposals.
- **Reviewers:** one session per proposal per reviewer. Each proposal was scored by one Opus and two Sonnet reviewers, each in its own session, with only the tiers file, that proposal, and its outline PDF. No reviewer saw the other proposal or another reviewer's scores.
- **Raw outputs:** saved verbatim in [`rounds/bd1c53733feef158dfb760101029b04e8f5989a1/`](rounds/bd1c53733feef158dfb760101029b04e8f5989a1/).

- [Acting on AP CS Score Reports: A Hands-On Data-Driven Cycle](../../projects/ap-score-reports/proposals/ap-score-reports-as-instructional-data/AP-Score-Reports-as-Instructional-Data.md): Session (1 hour).
- [From Data-Aware to Data-Driven: Acting on AP CS Score Reports](../../projects/ap-score-reports/proposals/ap-score-reports-quick-workflow/AP-Score-Reports-Quick-Workflow.md): Mini-Session (20 minutes).

## Method

- **Score of record:** the median of the three reviewers for each criterion.
- **Reconciliation:** not needed. No criterion had a spread of two or more tiers.
- **Quote check:** a script compared every quoted passage (128 fragments) with the proposal and outline text at the pinned commit. All were found verbatim. A fabricated control phrase was correctly not found.
- **Totals:** every reviewer's total equals the sum of its criteria.
- **Note on inputs:** the tiers file's counting rule still uses "four steps of Data Wise" as its example of a single framework. All six reviewers applied it correctly, counting the proposals' Data Wise sentence as no additional practice.

## Compliance

Both proposals pass the submission check on every automated item. Manual items remain: the website form fields (including Student Subtopics, grade level, and the device question) and the outline PDF upload.

## Overall Summary

| Proposal | Score of record | Reviewer totals (Opus, Sonnet A, Sonnet B) | Summary |
|---|---:|---|---|
| Acting on AP CS Score Reports: A Hands-On Data-Driven Cycle | 34/35 | 35, 34, 32 | Top tier on six criteria. Held back only on Attendee Preparedness: participants without data or with portal problems may leave with less, and the hour is tight. |
| From Data-Aware to Data-Driven: Acting on AP CS Score Reports | 30/35 | 30, 29, 31 | Pedagogy and Takeaways at top tier. Held back by a tight 20-minute schedule, a thin 3f link, and no in-session practice of the Respond stage. |

## Review: Acting on AP CS Score Reports: A Hands-On Data-Driven Cycle

| Criterion | Median | Reviewers | Evidence and gaps |
|---|---:|---|---|
| CSTA Standards | 5/5 | 5, 5, 5 | 4g, 4f, and 3f each tied to timed segments. 3f is the weakest because follow-up is optional. No Student Subtopics, which the rubric's "and/or" allows. |
| Content | 5/5 | 5, 5, 5 | All four characteristics present. Timing called tight but credible. |
| Educational Best Practices / Pedagogy | 5/5 | 5, 5, 5 | Four distinct practices counted: data use as a cycle, structured cross-school collaboration (both Marsh), formative assessment, foundational concepts. Data Wise not counted. |
| Engaging and Relevance | 5/5 | 5, 5, 4 | Own data and real artifacts. Sonnet B: narrow AP-only audience, practical rather than innovative. |
| Takeaways | 5/5 | 5, 5, 5 | Four resources described in detail; tangible and intangible named. |
| Attendee Preparedness | 4/5 | 5, 4, 4 | Finished products, but attendees without data or with portal problems may leave less prepared. |
| Overall Recommendation | 5/5 | 5, 5, 4 | Strongly recommend from two reviewers. Sonnet B: needs broader appeal for top 5%. |

## Review: From Data-Aware to Data-Driven: Acting on AP CS Score Reports

| Criterion | Median | Reviewers | Evidence and gaps |
|---|---:|---|---|
| CSTA Standards | 4/5 | 4, 4, 4 | 4g and 4f strong. All three reviewers found the 3f link thin: a Think-Pair-Share with a stranger is not PLC participation. No Student Subtopics. |
| Content | 4/5 | 4, 4, 5 | Two reviewers found characteristic (d) not clearly met: Investigate and Respond each pack content, a Think-Pair-Share, and a whole-room question into 6 minutes. |
| Educational Best Practices / Pedagogy | 5/5 | 5, 5, 5 | Four practices counted: Marsh, Black and Wiliam, Cabo, Think-Pair-Share. Data Wise not counted. |
| Engaging and Relevance | 4/5 | 4, 4, 4 | Timely and relevant. Narrow audience; engagement is mostly repeated Think-Pair-Share. |
| Takeaways | 5/5 | 5, 4, 5 | Resources described in detail. Sonnet A: only one intangible takeaway. |
| Attendee Preparedness | 4/5 | 4, 4, 4 | Attendees practice only the first steps; Respond is described but not practiced. |
| Overall Recommendation | 4/5 | 4, 4, 4 | Recommend (top 25%). Tight timing, thin 3f, narrow audience. |

## Changes From Round Five

| Proposal | Round 5 | Round 6 | Notes |
|---|---:|---:|---|
| Breakout | 28 | 34 | Round 5 scored the Data Wise version (titled "AP Score Reports as Instructional Data"). The proposal was rebuilt from the workshop-based process before round 6. |
| Mini | 27 | 30 | Round 5 scored the Data Wise version (titled "AP Scores to Instructional Action: A Quick Workflow"). Rebuilt before round 6. |

Round five's raw outputs remain in [`rounds/9033c9235dfb38df03d672738e6222dab8a71cf9/`](rounds/9033c9235dfb38df03d672738e6222dab8a71cf9/), and its report is in the git history at commit `cb44c8c`.

## Open Issues

- **Mini timing:** Investigate and Respond each have 6 minutes for content, a Think-Pair-Share, and a whole-room question. Two of three reviewers judged this not clearly achievable.
- **Mini 3f:** all three reviewers found the link to professional learning communities thin.
- **Mini Preparedness:** the Respond stage is described but not practiced. This is built into the mini's design as an overview; the open question is whether it can be shown, briefly, rather than only described.
- **Breakout Preparedness:** attendees without data or with portal problems may leave with less.
- **Both:** no Student Subtopics. These are chosen on the submission form.
- **Both, Overall:** reviewers cite the narrow AP-only audience as the reason for not reaching top 5%.
