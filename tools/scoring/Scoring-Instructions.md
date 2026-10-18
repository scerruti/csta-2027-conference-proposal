# CSTA Proposal Scoring Instructions

## Purpose

This document provides a repeatable rubric-based procedure for scoring CSTA conference proposals in this repository. It is designed so that another model, reviewer, or collaborator can apply the same scoring method independently to the breakout session, mini-session, workshop, poster, or future project files added to this workspace.

## CSTA Teacher Standards Reference

For this rubric, reviewers should use the official CSTA Teacher Standards resource as the standards reference:

- CSTA Teacher Standards (interactive): https://csteachers.org/teacherstandards/interactive/

The reviewer should look for explicit alignment to the standards categories, especially:

- Standard 1: CS Knowledge and Skills
- Standard 2: Equity and Inclusion
- Standard 3: Professional Growth and Identity
- Standard 4: Instructional Design
- Standard 5: Classroom Practice

When a proposal references instructional design, assessment use, classroom practice, or equitable implementation, it should be evaluated against the relevant standards areas above.

## Required Inputs

Before scoring, the reviewer should have:

- the proposal text to evaluate
- the CSTA 2027 proposal rubric
- the session type (breakout, mini-session, workshop, poster, etc.)
- the target audience and instructional context

## Pre-Scoring Compliance Check

Before applying the rubric, the reviewer must run the repository word-count compliance check for the proposal file(s) being scored.

Use the project validator:

- python3 tools/validation/check_word_count.py projects/ap-score-reports/proposals/ap-score-reports-as-instructional-data/AP-Score-Reports-as-Instructional-Data.md projects/ap-score-reports/proposals/ap-score-reports-quick-workflow/AP-Score-Reports-Quick-Workflow.md

If the target project includes additional proposal files, include them in the same command. A proposal that fails the word-count check should be flagged as noncompliant before the rubric score is recorded, and any score report should note that compliance issue separately from rubric quality.

## Scoring Method

Use the rubric categories below, with each category scored from 1 to 5.

### 1. Standards Alignment (1-5)

Score based on how explicitly the proposal connects to CSTA Teacher Standards and/or Student Subtopics.

Guidance:

- 5: clearly and specifically names relevant standards or subtopics and connects them to the session goals
- 4: explicitly references CSTA standards in general terms and connects them to instructional practice
- 3: relevant to standards but not explicitly named
- 2: weak or minimal standards connection
- 1: no meaningful standards alignment

### 2. Content Quality (1-5)

Score based on completeness, clarity, and structure of the proposal outline.

Guidance:

- 5: clear structure, strong outline, detailed learning goals, activities, and a strong fit for the session type
- 4: strong overall quality with minor gaps
- 3: adequate structure but somewhat incomplete or thin
- 2: limited detail or weak alignment to session type
- 1: unclear or underdeveloped content

### 3. Educational Best Practices / Pedagogy (1-5)

Score based on whether the proposal demonstrates sound instructional practice and educational reasoning.

Guidance:

- 5: strong evidence of research-informed or highly defensible pedagogical choices
- 4: clearly grounded in sound pedagogy with minor room for improvement
- 3: generally sound but without much depth or explicit rationale
- 2: limited evidence of pedagogy or educational grounding
- 1: weak or unclear instructional rationale

### 4. Engaging and Relevance (1-5)

Score based on how engaging, relevant, and audience-appropriate the proposal is.

Guidance:

- 5: highly engaging, highly relevant, and clearly important to CS education professionals
- 4: relevant and engaging with minor areas to strengthen
- 3: generally relevant but not especially distinctive
- 2: somewhat relevant or not especially compelling
- 1: not engaging or not relevant to the audience

### 5. Takeaways (1-5)

Score based on how clear and useful the session outcomes are.

Guidance:

- 5: clear, tangible, and intangible takeaways; strong participant resources and practical value
- 4: takesaways are clear and useful, with some room for improvement
- 3: takeaways are present but somewhat general
- 2: limited or weak takeaways
- 1: no meaningful takeaways

### 6. Attendee Preparedness (1-5)

Score based on how likely attendees are to leave with usable knowledge or tools.

Guidance:

- 5: attendees leave with clear tools, workflows, or strategies they can immediately use
- 4: strong practical value with minor limitations
- 3: some value but not highly actionable
- 2: weak transfer to classroom practice
- 1: little or no attendee value

### 7. Overall Recommendation (1-5)

This is the final judgment of whether the proposal should be accepted based on all prior criteria.

Guidance:

- 5: strongly recommend acceptance
- 4: recommend acceptance with minor improvements
- 3: acceptable but not exceptional
- 2: weak case for acceptance
- 1: do not recommend

## Session-Type Adjustment Rules

Use the session type to interpret the content, but keep the rubric categories consistent.

### Breakout Session (60 minutes)

A breakout session should show:

- detailed flow or timing
- broader instructional depth
- richer activity sequence
- stronger participant takeaways

### Mini-Session (20 minutes)

A mini-session should be evaluated for:

- clarity and precision
- a concise but strong core message
- a practical, action-oriented takeaway
- a focused teacher workflow or key insight

Mini-sessions should not be expected to match breakout depth, but they should still demonstrate quality across all rubric criteria.

### Workshop (2.5 hours)

A workshop should show:

- significant participant interaction
- substantial hands-on or discussion activities
- a more developed sequence of applied practice
- clear participant learning outcomes and active engagement

### Poster Session

A poster should show:

- a focused, visual, and understandable problem or project
- clear relevance to CS education practice
- concise explanatory value for a learner or audience
- practical takeaways that can be absorbed in a short viewing window

### Other Formats

For any other session type, apply the same rubric categories while adjusting the expectations to the format. The key is to judge the proposal against what the format realistically allows, not against a longer or different session type.

## Suggested Scoring Template

Use this template for each proposal:

- Title:
- Session Type:
- Standards: /5
- Content: /5
- Pedagogy: /5
- Engaging and Relevance: /5
- Takeaways: /5
- Attendee Preparedness: /5
- Overall Recommendation: /5
- Total Score: /35
- Brief Summary:
- Biggest Strengths:
- Biggest Gaps:

## Recommendation Summary

After scoring, summarize the proposal in a brief paragraph:

- whether it is a strong candidate
- what the main strengths are
- the main gap or improvement area
- whether the proposal fits the target session type

## Best Practice for Future Projects

When adding new proposal documents to the repository:

1. Run the word-count compliance check before scoring.
2. Keep the title within the required character limit.
3. Check the abstract against the word limit.
4. Include a standards-alignment sentence if the rubric is being used.
5. Document the session type clearly.
6. Add a score report using the same rubric categories.
7. After any rescore, update the project README proposal list to reflect the current score, proposal type, and link.
8. If multiple proposals are in the same project, keep the project README and the proposal-level README aligned.

## Final Note

This procedure is intended to create consistent, transparent proposal review. It is most useful when used with the same rubric categories, a consistent session-type adjustment, and an explicit record of the final score and rationale.
