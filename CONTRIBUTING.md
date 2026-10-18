# Contributing

This repository holds draft proposals for the CSTA 2027 conference, the scoring tools used to review them, and the submission checks that compare drafts against the Call for Proposals. It is shared with San Diego chapter members, so contributions from other teachers are welcome.

## What's in the repo

- `projects/` holds one folder per proposal topic. Each project has its own `README.md`, `resources/`, and `proposals/`.
- `projects/<project>/proposals/<proposal-slug>/` holds one proposal: its draft `.md` file, a `README.md`, and optional notes.
- `conference/` holds the CSTA materials: the rubric, the planning sheet, and the Presentation Outline template.
- `tools/scoring/` holds the rubric score report and the scoring instructions.
- `tools/validation/` holds the checks that run on proposal drafts.

## Setup

You need Python 3. The scripts use only the standard library, so there is nothing to install.

```bash
git clone https://github.com/scerruti/csta-2027-conference-proposal.git
cd csta-2027-conference-proposal
```

## Check a proposal before you share it

Run the submission check on any proposal draft:

```bash
python3 tools/validation/check_submission.py path/to/proposal.md
```

It checks the limits from the CSTA planning sheet:

- Title: 100 characters or fewer
- Abstract: 500 to 1,500 characters
- Participant Outcomes (the takeaways proxy): 300 characters or fewer
- Session type: "Session (1 hour)," "Mini-Session (20 minutes)," "Workshop (2.5 hours)," or "Poster"
- Timed outline: segment times add up to the session length
- Presentation Outline sections: learning goals, discussion questions, and engagement activities
- Standards codes: must be on the planning sheet
- Links: flags any URL so you can check that none identify the presenter

It also prints manual checks for the website form and the outline PDF. The script can't see those, so check them yourself.

Limits are measured in characters, as the form measures them, so word counts don't apply.

## Add a proposal

1. Create a folder under `projects/<project>/proposals/` with a short slug, such as `ap-score-reports-quick-workflow`.
2. Add the draft as a Markdown file in that folder. Use these headings, in this order:
   - `# Title` (the level-1 heading)
   - `## Session Type`, with one of the planning-sheet type names
   - `## Abstract`
   - `## Learning Goals`, or `## Participant Outcomes` if you name the goals that way
   - `## Educational Basis`, naming the practices and sources you rely on
   - `## Session Outline` or `## Session Timed Outline`, with timed headings such as `### 0:00-0:08 | Topic`
   - `## Discussion Questions`
   - `## Related Links`
3. Add a `README.md` in the folder that lists the files, the same way the existing proposals do.
4. Run `check_submission.py` and fix each FAIL. Review each WARN.
5. Add the proposal to the project's score table in `projects/<project>/README.md` and the root `README.md`.

## Keep proposals free of identifying details

The planning sheet says reviewers must not see information that identifies the presenter. Before you share a draft or submit it:

- Remove personal GitHub, Google Doc, or other links that identify you.
- Keep names and contact details out of the proposal text.
- Keep the outline PDF to the Presentation Outline template, with no presenter details.

Don't commit personal data, such as demographics, teacher verification links, or contact details. The planning sheet asks for these on the website only.

## Build the Presentation Outline PDF

The CSTA 2027 Presentation Outline template in `conference/` is required for every submission. Build the outline PDF from that template, using the timed outline and discussion questions from your proposal. The planning sheet also requires the time in the outline to match the session type. The PDF is not in the repo yet; add it to the proposal folder once it is built.

## Scoring

Scores follow the [scoring instructions](tools/scoring/Scoring-Instructions.md) and the CSTA 2027 rubric in `conference/`. After a rescore:

1. Get a blind review first: a fresh reviewer scores the proposal from the rubric tiers, the proposal, and its outline PDF only (see the [blind scoring procedure](tools/scoring/Scoring-Instructions.md#blind-scoring-required-before-each-report)).
2. Update the proposal's entry in [the rubric score report](tools/scoring/Rubric-Score-Report.md) with the blind scores.
3. Update the score and submission-check columns in the project README and the root README.
4. Record the compliance status separately from the rubric score, as the scoring instructions require.

## Making changes

- Make one logical change per commit, with a message that says what changed and why.
- Run `check_submission.py` on any proposal you touched.
- Open a pull request against `main`. Describe which proposal or tool changed and what the checker reports before and after.
- Keep working notes in each proposal's README (under Open Questions), not in separate notes files. Only the proposal Markdown and its outline PDF are submitted.

## Open items

These are tracked in the [rubric score report](tools/scoring/Rubric-Score-Report.md):

- Both proposals have draft Presentation Outline PDFs (`Presentation-Outline-DRAFT.pdf`) in their folders. Upload the final versions after review.
- Resources named in the proposals but not yet written: the score-band export how-to, the worksheet glossary, and the mini-session take-home guide.
- The CSTA PDFs in `conference/` are included in this public repo. Confirm with CSTA that they can be shared publicly before you add more CSTA material.
