# CSTA Proposal Repository

## Root Structure

This repository is organized by shared project infrastructure at the root and project-specific content below `projects/`.

```text
.
├── CONTRIBUTING.md
├── README.md
├── conference/
│   ├── conference-proposal.pdf
│   ├── CSTA 2027 Call for Proposals Planning Sheet.pdf
│   └── CSTA 2027 Presentation Outline.pdf
├── projects/
│   └── ap-score-reports/
│       ├── README.md
│       ├── resources/
│       └── proposals/
│           ├── ap-score-reports-as-instructional-data/
│           └── ap-score-reports-quick-workflow/
├── tools/
│   ├── scoring/
│   │   ├── Rubric-Score-Report.md
│   │   └── Scoring-Instructions.md
│   └── validation/
│       └── check_submission.py
└── ...
```

## Root Responsibilities

The root of the repository contains:

- project folders
- shared conference materials
- scoring tools and reports
- validation tools
- the repository-level index

## Current Projects

- [AP Score Reports](projects/ap-score-reports)

### AP Score Reports Proposal Index

| Proposal | Type | Score | Submission checks | Link |
|---|---|---:|---|---|
| AP Score Reports as Instructional Data | Session (1 hour) | 28/35 | Fails: type name, abstract length. Warns: takeaways length | [Open proposal](projects/ap-score-reports/proposals/ap-score-reports-as-instructional-data) |
| AP Scores to Instructional Action: A Quick Workflow | Mini-Session (20 minutes) | 26/35 | Fails: no Learning Goals section. Warns: takeaways length | [Open proposal](projects/ap-score-reports/proposals/ap-score-reports-quick-workflow) |

Scores are from the [rubric score report](tools/scoring/Rubric-Score-Report.md). Submission checks come from `tools/validation/check_submission.py`. Update this list whenever a proposal is rescored or rechecked.

## Shared Resources

- [Conference rubric PDF](conference/conference-proposal.pdf)
- [Call for Proposals planning sheet](conference/CSTA%202027%20Call%20for%20Proposals%20Planning%20Sheet.pdf)
- [Presentation outline template](conference/CSTA%202027%20Presentation%20Outline.pdf)
- [Rubric score report](tools/scoring/Rubric-Score-Report.md)
- [Scoring instructions](tools/scoring/Scoring-Instructions.md)
- [Submission check script](tools/validation/check_submission.py)

New to the repo? Start with [CONTRIBUTING.md](CONTRIBUTING.md).

## Notes

Each project is responsible for its own `resources/` and `proposals/` folders. Shared infrastructure stays at the repository root so future projects can be added without mixing project-level content into the central workspace.
