#!/usr/bin/env python3
"""Check proposal drafts against the CSTA 2027 Call for Proposals planning sheet.

Limits and allowed values come from:
  conference/CSTA 2027 Call for Proposals Planning Sheet.pdf
  conference/CSTA 2027 Presentation Outline.pdf

Checks that can be read from the Markdown are run automatically. Fields that
only exist on the submission website are listed at the end as manual checks.
"""

import argparse
import re
from pathlib import Path

TITLE_MAX_CHARS = 100
ABSTRACT_MIN_CHARS = 500
ABSTRACT_MAX_CHARS = 1500
TAKEAWAYS_MAX_CHARS = 300

# Session length in minutes, keyed by the planning sheet's proposal type names.
PROPOSAL_TYPES = {
    "Workshop": 150,
    "Session": 60,
    "Mini-Session": 20,
    "Poster": None,  # 2-hour display window, no timed outline
}

# CSTA Teacher Standards indicators offered on the planning sheet.
STANDARD_CODES = {
    "1a", "1b", "1c", "1d", "1e", "1f",
    "2a", "2b", "2c", "2d", "2e",
    "3a", "3b", "3c", "3d", "3e", "3f",
    "4a", "4b", "4c", "4d", "4e", "4f", "4g",
    "5a", "5b", "5c", "5d", "5e", "5f",
}

URL_PATTERN = re.compile(r"https?://\S+")
STANDARD_PATTERN = re.compile(r"\b([1-5][a-g])\b")
TIME_RANGE_PATTERN = re.compile(r"^###\s+(\d{1,2}):(\d{2})-(\d{1,2}):(\d{2})")


def split_sections(markdown_text: str):
    """Return (title, {heading: body}) where headings are level-2 sections."""
    lines = markdown_text.splitlines()
    title = ""
    sections = {}
    current = None
    for line in lines:
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        elif line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return title, {k: "\n".join(v).strip() for k, v in sections.items()}


def count_chars(text: str) -> int:
    return len(text.strip())


def minutes_between(start_h, start_m, end_h, end_m) -> int:
    return (int(end_h) * 60 + int(end_m)) - (int(start_h) * 60 + int(start_m))


def check_file(path: Path):
    text = path.read_text(encoding="utf-8")
    title, sections = split_sections(text)
    results = []  # (status, message)

    def add(status, message):
        results.append((status, message))

    # Proposal title
    if not title:
        add("FAIL", "No title (level-1 heading) found.")
    elif count_chars(title) > TITLE_MAX_CHARS:
        add("FAIL", f"Title is {count_chars(title)} characters; the limit is {TITLE_MAX_CHARS}.")
    else:
        add("PASS", f"Title is {count_chars(title)} characters (limit {TITLE_MAX_CHARS}).")

    # Proposal type and matching length
    type_body = sections.get("Session Type", "")
    # Longest names first, so "Mini-Session" is not read as "Session"
    type_match = next((name for name in sorted(PROPOSAL_TYPES, key=len, reverse=True)
                       if name.lower() in type_body.lower()), None)
    if not type_body:
        add("FAIL", "No 'Session Type' section. The planning sheet requires one of: "
                    + ", ".join(PROPOSAL_TYPES) + ".")
    elif "breakout" in type_body.lower():
        add("FAIL", f"'Session Type' says '{type_body}'. The planning sheet calls this format "
                    "'Session (1 hour)', so use that name.")
        type_match = None
    elif type_match is None:
        add("FAIL", f"'Session Type' does not use a planning-sheet type name: '{type_body}'.")
    else:
        add("PASS", f"Proposal type is '{type_match}'.")

    # Abstract length, in characters
    abstract = sections.get("Abstract", "")
    if not abstract:
        add("FAIL", "No 'Abstract' section found.")
    else:
        n = count_chars(abstract)
        if n < ABSTRACT_MIN_CHARS:
            add("FAIL", f"Abstract is {n} characters; the minimum is {ABSTRACT_MIN_CHARS}.")
        elif n > ABSTRACT_MAX_CHARS:
            add("FAIL", f"Abstract is {n} characters; the maximum is {ABSTRACT_MAX_CHARS}.")
        else:
            add("PASS", f"Abstract is {n} characters ({ABSTRACT_MIN_CHARS}-{ABSTRACT_MAX_CHARS} allowed).")

    # Takeaways: checked against the Participant Outcomes section as a proxy
    outcomes = sections.get("Participant Outcomes", "")
    if not outcomes:
        add("FAIL", "No 'Participant Outcomes' section to check against the takeaways field.")
    else:
        n = count_chars(outcomes)
        if n > TAKEAWAYS_MAX_CHARS:
            add("WARN", f"Participant Outcomes is {n} characters; the takeaways field allows "
                        f"{TAKEAWAYS_MAX_CHARS}. Shorten the takeaways text for the form.")
        else:
            add("PASS", f"Participant Outcomes is {n} characters (takeaways field allows {TAKEAWAYS_MAX_CHARS}).")

    # Timed outline matches the proposal type
    outline_lines = [line for line in text.splitlines() if TIME_RANGE_PATTERN.match(line)]
    if outline_lines and type_match and PROPOSAL_TYPES[type_match]:
        total = 0
        for line in outline_lines:
            m = TIME_RANGE_PATTERN.match(line)
            total += minutes_between(*m.groups())
        expected = PROPOSAL_TYPES[type_match]
        if total == expected:
            add("PASS", f"Timed outline totals {total} minutes, matching '{type_match}'.")
        else:
            add("FAIL", f"Timed outline totals {total} minutes; '{type_match}' requires {expected}.")
    elif not outline_lines:
        add("FAIL", "No timed outline found (headings like '### 0:00-0:08').")

    # Presentation Outline template sections
    if "Learning Goals" in sections or "Learning Goals" in text:
        add("PASS", "Learning goals present.")
    else:
        add("FAIL", "No learning goals section (required by the Presentation Outline template).")
    if re.search(r"discussion", text, re.IGNORECASE):
        add("PASS", "Discussion questions present.")
    else:
        add("FAIL", "No discussion questions (required by the Presentation Outline template).")
    if re.search(r"participant engagement|engagement", text, re.IGNORECASE):
        add("PASS", "Engagement activities present.")
    else:
        add("FAIL", "No engagement activities (required by the Presentation Outline template).")

    # Standards codes
    codes_found = sorted(set(STANDARD_PATTERN.findall(text)))
    invalid = [c for c in codes_found if c not in STANDARD_CODES]
    if not codes_found:
        add("FAIL", "No CSTA Teacher Standards indicator codes found (e.g., 4g, 5f).")
    elif invalid:
        add("FAIL", f"Standards codes not on the planning sheet: {', '.join(invalid)}.")
    else:
        add("PASS", f"Standards codes used: {', '.join(codes_found)}.")

    # URLs: the planning sheet says not to include URLs that identify the presenter
    urls = URL_PATTERN.findall(text)
    if urls:
        add("WARN", "Links appear in the proposal. Check that none identify the presenter "
                    "(for example, a personal GitHub or Google Doc):")
        for url in urls:
            add("WARN", f"  {url}")

    return results


MANUAL_CHECKS = [
    "Primary and optional secondary grade level selected on the form (High School, etc.).",
    "Topic selected from the planning-sheet list.",
    "Standards selected on the form match the codes in the abstract.",
    "Equity/inclusion focus question answered.",
    "Takeaways text entered on the form (300 characters maximum).",
    "Presentation outline PDF uses the required CSTA 2027 Presentation Outline template.",
    "Outline PDF contains no presenter-identifying information.",
    "Outline PDF time allotment matches the proposal type.",
]


def main():
    parser = argparse.ArgumentParser(description="Check proposal drafts against the CSTA 2027 planning sheet.")
    parser.add_argument("paths", nargs="+", help="Markdown proposal files to check.")
    args = parser.parse_args()

    any_fail = False
    for raw in args.paths:
        path = Path(raw)
        print(f"File: {path.name}")
        print("=" * 56)
        for status, message in check_file(path):
            if status == "FAIL":
                any_fail = True
            print(f"  [{status}] {message}")
        print()

    print("Manual checks on the submission form and outline PDF:")
    for item in MANUAL_CHECKS:
        print(f"  [ ] {item}")
    print()
    print("Summary:", "FAIL" if any_fail else "PASS (automated checks)")
    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
