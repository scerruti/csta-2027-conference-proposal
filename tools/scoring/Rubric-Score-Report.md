# CSTA 2027 Proposal Rubric Score Report

## Scope

This report evaluates the current proposal drafts against the CSTA 2027 proposal rubric:

- [AP Score Reports as Instructional Data](../../projects/ap-score-reports/proposals/ap-score-reports-as-instructional-data/AP-Score-Reports-as-Instructional-Data.md) (Breakout, 60 minutes)
- [AP Scores to Instructional Action: A Quick Workflow](../../projects/ap-score-reports/proposals/ap-score-reports-quick-workflow/AP-Score-Reports-Quick-Workflow.md) (Mini-session, 20 minutes)

Each score is tied to the rubric tier wording in the CSTA 2027 Reviewers Rubric PDF. Where the PDF text extracted poorly, the tier is marked for checking.

## Compliance

The form's limits come from the [Call for Proposals planning sheet](../../conference/CSTA%202027%20Call%20for%20Proposals%20Planning%20Sheet.pdf). Both drafts were checked with `tools/validation/check_submission.py`. Both fail:

- **Breakout:** the session type is "Breakout Session (60 minutes)," but the form's name is "Session (1 hour)." The abstract is 1,820 characters (limit 1,500). Participant Outcomes is 338 characters (takeaways field, 300).
- **Quick workflow:** there is no Learning Goals section, which the Presentation Outline template requires. Participant Outcomes is 304 characters (takeaways field, 300).

Per the scoring instructions, these compliance failures are recorded separately from rubric quality. The scores below describe the drafts as they stand.

The earlier word-count check (`check_word_count.py`) measures words. The form limits are in characters, so it no longer answers the compliance question.

The template requirement is confirmed: the Presentation Outline template is required, and neither draft uses it yet.

## Overall Summary

| Proposal | Score | Summary |
|---|---:|---|
| AP Score Reports as Instructional Data | 28/35 | Strong, specific workflow with named standards indicators and a named educational basis. Held back by the missing Presentation Outline template, the abstract and takeaways length failures, and reliance on one framework. |
| AP Scores to Instructional Action: A Quick Workflow | 26/35 | Clear, focused, and relevant. Shorter in-session practice and no hands-on diagnosis lower the preparedness and recommendation scores. |

## Review: AP Score Reports as Instructional Data

| Criterion | Score | Notes |
|---|---:|---|
| CSTA Standards | 4/5 | Names Standard 4, indicator 4g (Inform instruction through assessment), and Standard 5, indicator 5f (Guide students' use of feedback). Relevant, but the proposal addresses them in one sentence rather than throughout the session. |
| Content | 4/5 | Learning goals, activities timed to 60 minutes, and discussion questions are present, and the activities fit the session type. The template is not used, which is the one missing characteristic, so the score stays at 4 rather than 5. |
| Educational Best Practices / Pedagogy | 4/5 | Three Data Wise steps are named and cited (Steps 2, 4, and 6). All three come from one framework, so a reviewer could count them as one practice. A 5 would need three practices that stand apart from each other. |
| Engaging and Relevance | 4/5 | Directly relevant to AP CS teachers, and the grade-level fit is clear. Practical rather than especially innovative. |
| Takeaways | 4/5 | Tangible resources are named: the Data Deep Dive worksheet (including the CSA and CSP matrices), the browser tool, and a score-band export how-to. The how-to does not exist yet, so the 5 tier is not met until it is written. |
| Attendee Preparedness | 4/5 | Attendees leave with a process, a worksheet, and a tool. Application depends on the tool and the how-to being available. |
| Overall Recommendation | 4/5 | Recommend acceptance with minor improvements. The 5 tier is reserved for the top 5% of submissions, which can't be confirmed from this review. |

### Final Score: 28/35

### Strengths

- Names specific CSTA indicators (4g and 5f) rather than only the standards in general terms
- Educational basis is explicit, with each Data Wise step tied to a session activity
- Resources are concrete and named, not generic
- Fits the 60-minute format with a full timed outline

### Improvements

- Convert the outline to the CSTA 2027 Presentation Outline template. The 5 tier of Content requires it
- Write the score-band export how-to, which is already listed as a resource
- Strengthen the pedagogy basis with practices beyond one framework, if sources are available
- Cut the abstract to 1,500 characters or fewer, and check it with `check_submission.py` after each edit

## Review: AP Scores to Instructional Action: A Quick Workflow

| Criterion | Score | Notes |
|---|---:|---|
| CSTA Standards | 4/5 | Names the same indicators as the breakout (4g and 5f). Relevant to the diagnostic and intervention steps. |
| Content | 4/5 | Learning goals (Participant Outcomes), timed activities, and discussion questions are present, and the activities fit the session type. The template is not used, and the learning goals section is missing its required heading, so the score stays at 4 only while the other three characteristics hold. |
| Educational Best Practices / Pedagogy | 4/5 | Same three Data Wise steps and citation as the breakout. Same caveat: one framework. |
| Engaging and Relevance | 4/5 | Relevant, focused, and useful for teachers who need a quick process after AP results arrive. |
| Takeaways | 4/5 | Same named resources as the breakout, with the same caveat that the score-band how-to is not written yet. |
| Attendee Preparedness | 3/5 | The in-session practice is now a reflective question and a quick reaction, not a diagnosis. Attendees get the process and the worksheet, but the hands-on application moves to take-home work. |
| Overall Recommendation | 3/5 | Acceptable. The workflow is sound, but the shorter in-session practice makes it less distinctive than the breakout. |

### Final Score: 26/35

### Strengths

- Focused on one clear process
- Timing is realistic for 20 minutes
- Educational basis and discussion questions match the breakout
- Clear fit for teachers who want a fast entry point

### Improvements

- Decide whether a short hands-on activity can fit the 20 minutes, which would strengthen attendee preparedness
- Convert the outline to the CSTA 2027 Presentation Outline template, and add a Learning Goals section with its heading
- Write the score-band export how-to

## Changes From Previous Scores

| Proposal | Previous | Current | Main reasons |
|---|---:|---:|---|
| AP Score Reports as Instructional Data | 33 | 28 | Pedagogy was 4 with no named practices, now 4 with three cited steps. Content, Takeaways, and Overall were 5, now 4 because the template, the how-to, and the top 5% tier are not yet met. |
| AP Scores to Instructional Action | 28 (reported as 30) | 26 | Arithmetic corrected first. Pedagogy and Standards are now supported by named indicators and steps. Attendee Preparedness and Overall dropped to 3 after the diagnostic example moved to take-home. |

## Recommended Next Steps

1. Convert both outlines to the CSTA 2027 Presentation Outline template, then rerun `check_submission.py`.
2. Write the score-band export how-to.
3. Decide whether the quick workflow needs a hands-on activity in place of the reflective question.
4. Keep the project and root README score tables in sync with this report after each rescore.
