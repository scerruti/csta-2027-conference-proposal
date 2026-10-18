#!/usr/bin/env python3

import argparse
import re
from pathlib import Path

DEFAULT_LIMITS = {
    "title_chars": 60,
    "short_description_chars": 140,
    "abstract_words": 250,
    "learning_goals_words": 250,
}


def normalize_heading(value: str) -> str:
    value = value.strip().lower()
    value = value.replace("#", "")
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def extract_sections(markdown_text: str):
    sections = {}
    current = None
    label_pattern = re.compile(
        r"^(?:#+\s*)?(Title|Abstract|Description|Short Description|Learning Goals|Participant Outcomes|Session Outline|Session Timed Outline|Discussion Questions|Related Links|Summary|Overview)\s*$",
        re.IGNORECASE,
    )

    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        heading_match = re.match(r"^(#+)\s+(.*)$", line)
        if heading_match:
            current = normalize_heading(heading_match.group(2))
            sections.setdefault(current, [])
        else:
            label_match = label_pattern.match(line.strip())
            if label_match:
                current = normalize_heading(label_match.group(1))
                sections.setdefault(current, [])
            elif current is not None:
                sections[current].append(line)

    cleaned_sections = {}
    for key, value in sections.items():
        cleaned = "\n".join(value).strip()
        if cleaned:
            cleaned_sections[key] = cleaned
    return cleaned_sections


def first_meaningful_line(value: str):
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    if not lines:
        return ""
    if lines[0].lower().startswith("title"):
        lines = lines[1:]
    if lines:
        return " ".join(lines)
    return ""


def get_title(lines):
    for heading in ["title", "session title", "proposal title"]:
        if heading in lines:
            return first_meaningful_line(lines[heading])

    if "content" in lines:
        return first_meaningful_line(lines["content"])

    return ""


def get_section_text(lines, *names):
    for name in names:
        if name in lines:
            return lines[name]
    return ""


def count_words(text: str) -> int:
    cleaned = re.sub(r"https?://\S+|www\.\S+", " ", text)
    tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", cleaned)
    return len(tokens)


def count_chars(text: str) -> int:
    return len(text.strip())


def evaluate_section(name: str, value: str, limit: int, metric: str):
    if metric == "chars":
        actual = count_chars(value)
    elif metric == "words":
        actual = count_words(value)
    else:
        raise ValueError(f"Unsupported metric: {metric}")

    if actual <= limit:
        status = "PASS"
    else:
        status = "FAIL"

    return {
        "name": name,
        "actual": actual,
        "limit": limit,
        "metric": metric,
        "status": status,
    }


def analyze_file(path: Path, limits: dict):
    markdown = path.read_text(encoding="utf-8")
    sections = extract_sections(markdown)

    # Title is often in a heading like "# Title" or "## Title"
    title_value = get_title(sections)

    # Abstract is the main proposal text and is usually a block under an Abstract heading
    abstract_value = get_section_text(sections, "abstract", "proposal abstract", "session abstract")

    # Some files also include a short description or summary line in plain text
    short_desc = get_section_text(sections, "short description", "description", "summary")
    if not short_desc:
        short_desc = ""

    results = []
    if title_value:
        results.append(evaluate_section("Title", title_value, limits["title_chars"], "chars"))
    if abstract_value:
        results.append(evaluate_section("Abstract", abstract_value, limits["abstract_words"], "words"))
    if short_desc:
        results.append(evaluate_section("Short Description", short_desc, limits["short_description_chars"], "chars"))

    # If a file includes learning goals, check them too but do not fail if absent
    learning_goals = get_section_text(sections, "learning goals", "participant outcomes")
    if learning_goals:
        results.append(evaluate_section("Learning Goals", learning_goals, limits["learning_goals_words"], "words"))

    return results


def main():
    parser = argparse.ArgumentParser(description="Check CSTA-style proposal section lengths against configured limits.")
    parser.add_argument("paths", nargs="*", default=["."], help="Markdown files or folders to check. Defaults to the current folder.")
    parser.add_argument("--title-chars", type=int, default=DEFAULT_LIMITS["title_chars"])
    parser.add_argument("--short-description-chars", type=int, default=DEFAULT_LIMITS["short_description_chars"])
    parser.add_argument("--abstract-words", type=int, default=DEFAULT_LIMITS["abstract_words"])
    parser.add_argument("--learning-goals-words", type=int, default=DEFAULT_LIMITS["learning_goals_words"])
    args = parser.parse_args()

    limits = {
        "title_chars": args.title_chars,
        "short_description_chars": args.short_description_chars,
        "abstract_words": args.abstract_words,
        "learning_goals_words": args.learning_goals_words,
    }

    files = []
    for raw in args.paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.glob("*.md")))
        elif p.is_file() and p.suffix.lower() == ".md":
            files.append(p)

    if not files:
        print("No Markdown files found to check.")
        return 1

    print("CSTA-style Word/Character Compliance Report")
    print("=" * 56)
    print(f"Limits: title <= {limits['title_chars']} chars, short description <= {limits['short_description_chars']} chars, abstract <= {limits['abstract_words']} words")
    print()

    all_ok = True
    for file in files:
        print(f"File: {file.name}")
        results = analyze_file(file, limits)
        if not results:
            print("  No measurable sections found.")
            print()
            continue

        file_ok = True
        for item in results:
            label = f"{item['name']}:"
            status = item['status']
            if status == "FAIL":
                file_ok = False
                all_ok = False
            print(f"  {label:<22} {item['actual']:<4} {item['metric']:<5} | limit {item['limit']:<4} | {status}")
        print(f"  Overall: {'PASS' if file_ok else 'FAIL'}")
        print()

    print("Summary:", "PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
