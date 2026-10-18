# CSTA Proposal Repository

## Root Structure

This repository is organized by shared project infrastructure at the root and project-specific content below `projects/`.

```text
.
├── README.md
├── conference/
│   └── conference-proposal.pdf
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
│       └── check_word_count.py
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

| Proposal | Type | Score | Link |
|---|---|---:|---|
| AP Score Reports as Instructional Data | Full proposal / 60-minute format | 33/35 | [Open proposal](projects/ap-score-reports/proposals/ap-score-reports-as-instructional-data) |
| AP Scores to Instructional Action: A Quick Workflow | Quick workflow / 20-minute format | 28/35 | [Open proposal](projects/ap-score-reports/proposals/ap-score-reports-quick-workflow) |

Update this list whenever a proposal is rescored so the project-level summary always reflects the current score.

## Shared Resources

- [Conference rubric PDF](conference/conference-proposal.pdf)
- [Rubric score report](tools/scoring/Rubric-Score-Report.md)
- [Scoring instructions](tools/scoring/Scoring-Instructions.md)
- [Validation script](tools/validation/check_word_count.py)

## Notes

Each project is responsible for its own `resources/` and `proposals/` folders. Shared infrastructure stays at the repository root so future projects can be added without mixing project-level content into the central workspace.
