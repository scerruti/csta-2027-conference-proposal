# Action Plan

Deferred work, recorded so it is not lost. None of these items is in progress.

## Proposal Timing

From the round-six blind review (see the [rubric score report](tools/scoring/Rubric-Score-Report.md)).

- **Mini: Investigate and Respond are overpacked.** Each 6-minute stage holds content, a Think-Pair-Share, and a whole-room question. Two of three reviewers judged this not clearly achievable (Content 4/5). The simplest lever is cutting one whole-room question from Investigate or Respond; the trade-off is less of the "why" discussion that reviewers asked for in earlier rounds.
- **Breakout: the hour is tight.** All three reviewers accepted the timing but called it tight, especially the 12-minute Hypothesize round for groups of four and the reliance on live portal access during Slice and Download.

## Scoring Tooling

- **Better file names.** Round folders are named by the full 40-character commit hash (`tools/scoring/rounds/<hash>/`), which is hard to read and gives no round number or date. Adopt a readable scheme, such as `rounds/round-06-bd1c537/`, and update the [scoring instructions](tools/scoring/Scoring-Instructions.md) to match.
- **Score only modified proposals.** The procedure currently rescores every proposal each round. Instead, compare each proposal's files (its Markdown and outline PDF) against the commit pinned in the last round, rescore only the proposals that changed, and carry the previous scores of record forward for the rest. Update the scoring instructions and the score report format to show which round each score comes from.
