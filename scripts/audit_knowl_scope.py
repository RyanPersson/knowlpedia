#!/usr/bin/env python3
"""Report knowls that may own more than one independently reusable concept.

This audit deliberately produces review candidates, not edits.  Its strongest
signals are multiple explicit definienda in one knowl and a section that opens
by defining a term different from the page's primary term.  Compound titles
are available as a weaker signal because conjunctions are often legitimate in
theorem, comparison, and construction pages.

The audit also reports an exact-label mismatch when a wikilink's visible label
is the unique title or alias of one knowl but the link targets another.  This
is useful after a bundled page has been split: stale links remain visible
instead of silently opening the old umbrella page.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
import tomllib
import unicodedata


CONTAINER_KINDS = {"document", "index", "page", "section"}
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
FENCED_CODE_RE = re.compile(r"^```[^\n]*\n.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"(?<!`)`[^`\n]+`(?!`)")
WIKILINK_RE = re.compile(r"\[\[([^\]|\n]+?)(?:\|([^\]]+?))?\]\]", re.DOTALL)
DEFINITION_RE = re.compile(
    r"\b(?:A|An|The|This|That|Its|Their)\s+"
    r"\*\*(?P<subject>(?:(?!\*\*)[\s\S]){2,120}?)\*\*"
    r"(?P<tail>[^\n.!?;]{0,80}?)\b(?:is|are|means|consists)\b",
    re.IGNORECASE,
)
CALLED_RE = re.compile(
    r"\b(?:is|are)\s+(?:called|termed)\s+(?:a|an|the)?\s*"
    r"\*\*(?P<subject>(?:(?!\*\*)[\s\S]){2,120}?)\*\*",
    re.IGNORECASE,
)
COMPOUND_TITLE_RE = re.compile(
    r";|,\s+(?:and|or)\s+|\s+(?:and|&)\s+",
    re.IGNORECASE,
)
REFERENCE_TITLES = {"reference", "references", "literature", "sources"}


@dataclass(frozen=True)
class SourceKnowl:
    path: Path
    knowl_id: str
    title: str
    kind: str
    summary: str
    aliases: tuple[str, ...]
    text: str
    body: str
    body_offset: int


@dataclass(frozen=True)
class DefinitionSubject:
    term: str
    normalized: str
    line: int
    section: str
    position: int


@dataclass(frozen=True)
class LinkUse:
    source: SourceKnowl
    target: str
    label: str
    normalized_label: str
    line: int


def split_front_matter(text: str) -> tuple[str, str, int]:
    if not text.startswith("+++\n"):
        raise ValueError("missing TOML front matter")
    end = text.find("\n+++\n", 4)
    if end == -1:
        raise ValueError("unterminated TOML front matter")
    boundary = end + len("\n+++\n")
    return text[4:end], text[boundary:], boundary


def load_knowl(path: Path) -> SourceKnowl:
    text = path.read_text(encoding="utf-8")
    front_matter, body, body_offset = split_front_matter(text)
    metadata = tomllib.loads(front_matter)
    missing = [name for name in ("id", "title", "kind") if not metadata.get(name)]
    if missing:
        raise ValueError(f"missing required metadata: {', '.join(missing)}")
    return SourceKnowl(
        path=path,
        knowl_id=str(metadata["id"]),
        title=str(metadata["title"]),
        kind=str(metadata["kind"]),
        summary=str(metadata.get("summary", "")),
        aliases=tuple(str(alias) for alias in metadata.get("aliases", [])),
        text=text,
        body=body,
        body_offset=body_offset,
    )


def knowl_paths(roots: list[Path]) -> list[Path]:
    paths: set[Path] = set()
    for root in roots:
        if root.is_dir():
            paths.update(root.rglob("*.knowl.md"))
        elif root.name.endswith(".knowl.md"):
            paths.add(root)
    return sorted(paths)


def position_in_spans(position: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= position < end for start, end in spans)


def protected_spans(body: str) -> list[tuple[int, int]]:
    fenced = [(match.start(), match.end()) for match in FENCED_CODE_RE.finditer(body)]
    inline = [
        (match.start(), match.end())
        for match in INLINE_CODE_RE.finditer(body)
        if not position_in_spans(match.start(), fenced)
    ]
    headings = [
        match
        for match in H2_RE.finditer(body)
        if not position_in_spans(match.start(), fenced)
    ]
    references: list[tuple[int, int]] = []
    for index, heading in enumerate(headings):
        if heading.group(1).strip().casefold() not in REFERENCE_TITLES:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        references.append((heading.start(), end))
    return fenced + inline + references


def strip_markup(value: str) -> str:
    value = WIKILINK_RE.sub(lambda match: match.group(2) or match.group(1), value)
    value = re.sub(r"\[([^\]\n]+)\]\([^\n]+\)", r"\1", value)
    value = value.replace("\\(", " ").replace("\\)", " ")
    value = value.replace("\\[", " ").replace("\\]", " ")
    value = value.replace("$", " ")
    value = re.sub(r"\\(?:operatorname|mathrm|mathbf|mathbb|mathcal)\s*\{([^{}]+)\}", r"\1", value)
    value = re.sub(r"\\[A-Za-z]+", " ", value)
    return value.replace("*", " ").replace("_", " ").replace("`", " ")


def normalize_term(value: str) -> str:
    value = unicodedata.normalize("NFKC", strip_markup(value)).casefold()
    characters = [character if character.isalnum() else " " for character in value]
    words = "".join(characters).split()
    if words and words[0] in {"a", "an", "the"}:
        words = words[1:]
    return " ".join(words)


def comparison_key(value: str) -> str:
    """Normalize a visible concept phrase without guessing mathematical synonyms."""

    normalized = normalize_term(value)
    words = normalized.split()
    if not words:
        return ""
    last = words[-1]
    irregular_plurals = {
        "analyses": "analysis",
        "axes": "axis",
        "hypotheses": "hypothesis",
        "indices": "index",
        "matrices": "matrix",
        "theses": "thesis",
        "vertices": "vertex",
    }
    if last in irregular_plurals:
        words[-1] = irregular_plurals[last]
    elif last in {"series", "species"} or last.endswith(("us", "is")):
        pass
    elif len(last) > 4 and last.endswith("ies"):
        words[-1] = last[:-3] + "y"
    elif len(last) > 4 and last.endswith(("sses", "ches", "shes", "xes")):
        words[-1] = last[:-2]
    elif len(last) > 3 and last.endswith("s") and not last.endswith("ss"):
        words[-1] = last[:-1]
    return " ".join(words)


def line_number(knowl: SourceKnowl, body_position: int) -> int:
    return knowl.text.count("\n", 0, knowl.body_offset + body_position) + 1


def section_ranges(body: str, protected: list[tuple[int, int]]) -> list[tuple[int, int, str]]:
    headings = [
        match
        for match in H2_RE.finditer(body)
        if not position_in_spans(match.start(), protected)
    ]
    ranges: list[tuple[int, int, str]] = []
    first = headings[0].start() if headings else len(body)
    ranges.append((0, first, "Core"))
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        ranges.append((heading.end(), end, heading.group(1).strip()))
    return ranges


def section_at(position: int, ranges: list[tuple[int, int, str]]) -> str:
    for start, end, title in ranges:
        if start <= position < end:
            return title
    return "Core"


def definition_subjects(knowl: SourceKnowl) -> list[DefinitionSubject]:
    protected = protected_spans(knowl.body)
    ranges = section_ranges(knowl.body, protected)
    matches = [*DEFINITION_RE.finditer(knowl.body), *CALLED_RE.finditer(knowl.body)]
    subjects: list[DefinitionSubject] = []
    seen: set[tuple[str, int]] = set()
    for match in sorted(matches, key=lambda item: item.start()):
        if position_in_spans(match.start(), protected):
            continue
        raw_subject = match.group("subject").strip()
        # A bold wikilink normally acknowledges another knowl as the owner.
        if "[[" in raw_subject:
            continue
        normalized = comparison_key(raw_subject)
        if not normalized or (normalized, match.start()) in seen:
            continue
        seen.add((normalized, match.start()))
        subjects.append(
            DefinitionSubject(
                term=strip_markup(raw_subject).strip(),
                normalized=normalized,
                line=line_number(knowl, match.start()),
                section=section_at(match.start(), ranges),
                position=match.start(),
            )
        )
    return subjects


def link_uses(knowl: SourceKnowl) -> list[LinkUse]:
    protected = protected_spans(knowl.body)
    uses: list[LinkUse] = []
    for match in WIKILINK_RE.finditer(knowl.body):
        if position_in_spans(match.start(), protected):
            continue
        target = match.group(1).strip().split("#", 1)[0]
        label = (match.group(2) or target.rsplit("/", 1)[-1].replace("-", " ")).strip()
        normalized = comparison_key(label)
        if not target or not normalized:
            continue
        uses.append(
            LinkUse(
                source=knowl,
                target=target,
                label=" ".join(label.split()),
                normalized_label=normalized,
                line=line_number(knowl, match.start()),
            )
        )
    return uses


def primary_keys(knowl: SourceKnowl) -> set[str]:
    return {
        key
        for value in (knowl.title, *knowl.aliases)
        if (key := comparison_key(value))
    }


def title_supports_subject(title_keys: set[str], subject: str) -> bool:
    subject_words = set(subject.split())
    for title in title_keys:
        if title == subject:
            return True
        title_words = set(title.split())
        if subject_words and subject_words <= title_words:
            return True
        if title_words and title_words <= subject_words:
            return True
    return False


def page_findings(
    knowl: SourceKnowl,
    incoming: Counter[str],
    *,
    include_weak: bool,
) -> list[dict[str, object]]:
    if knowl.kind.casefold() in CONTAINER_KINDS:
        return []

    subjects = definition_subjects(knowl)
    unique_subjects: dict[str, DefinitionSubject] = {}
    for subject in subjects:
        unique_subjects.setdefault(subject.normalized, subject)
    # Aliases must be synonyms for the title, not a way to make a second
    # concept look in-scope. Compare section definienda with the title alone;
    # this deliberately catches pages whose aliases include the secondary
    # concept (for example, Tamagawa measure vs. Tamagawa number).
    title_keys = {comparison_key(knowl.title)}
    section_subjects = [
        subject
        for subject in unique_subjects.values()
        if subject.section != "Core"
        and not title_supports_subject(title_keys, subject.normalized)
    ]
    compound_title = bool(COMPOUND_TITLE_RE.search(strip_markup(knowl.title)))

    signals: list[str] = []
    score = 0
    if len(unique_subjects) >= 2:
        signals.append("multiple_explicit_definienda")
        score += 5 + min(len(unique_subjects) - 2, 3)
    if section_subjects:
        signals.append("independent_section_definition")
        score += 3
    if compound_title:
        signals.append("bundled_title")
        score += 1

    subject_keys = set(unique_subjects)
    supported_labels = {
        label: count for label, count in incoming.items() if label in subject_keys
    }
    if len(supported_labels) >= 2:
        signals.append("incoming_label_diversity")
        score += min(len(supported_labels), 3)

    strong = len(unique_subjects) >= 2 or bool(section_subjects)
    if not strong and not (include_weak and compound_title):
        return []

    severity = "high" if score >= 6 else "review"
    return [
        {
            "rule": "multiple_concept_ownership",
            "severity": severity,
            "score": score,
            "source_id": knowl.knowl_id,
            "source_path": str(knowl.path),
            "title": knowl.title,
            "kind": knowl.kind,
            "signals": signals,
            "definition_subjects": [
                {
                    "term": subject.term,
                    "normalized": subject.normalized,
                    "line": subject.line,
                    "section": subject.section,
                }
                for subject in unique_subjects.values()
            ],
            "incoming_labels": dict(incoming.most_common(12)),
            "recommended_action": "semantic_review_only",
        }
    ]


def exact_label_mismatches(
    uses: list[LinkUse],
    term_registry: dict[str, set[str]],
    knowls_by_id: dict[str, SourceKnowl],
) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for use in uses:
        # Short/generic labels and notation are too context-sensitive for this
        # rule ("unit", "G", and "composition" are typical collisions).
        if len(use.normalized_label.split()) < 2 or re.search(
            r"\\|\$", use.label
        ):
            continue
        owners = term_registry.get(use.normalized_label, set())
        if len(owners) != 1:
            continue
        expected = next(iter(owners))
        if expected == use.target:
            continue
        actual = knowls_by_id.get(use.target)
        # A shorter display label often intentionally names a more specific
        # target ("composition" -> "composition of morphisms", for example).
        # Only report the link when the actual target's own title/aliases do
        # not lexically support the label at all.
        if actual and title_supports_subject(
            primary_keys(actual), use.normalized_label
        ):
            continue
        findings.append(
            {
                "rule": "exact_label_target_mismatch",
                "severity": "high",
                "score": 6,
                "source_id": use.source.knowl_id,
                "source_path": str(use.source.path),
                "line": use.line,
                "label": use.label,
                "actual_target": use.target,
                "unique_label_owner": expected,
                "recommended_action": "semantic_review_only",
            }
        )
    return findings


def audit(knowls: list[SourceKnowl], *, include_weak: bool = False) -> list[dict[str, object]]:
    all_uses = [use for knowl in knowls for use in link_uses(knowl)]
    incoming: dict[str, Counter[str]] = defaultdict(Counter)
    for use in all_uses:
        incoming[use.target][use.normalized_label] += 1

    # Exact-label mismatch is intentionally title-only. Aliases are useful for
    # search, but often cross category boundaries and would make this check
    # noisy (for example, algebraic and analytic uses of "regular").
    term_registry: dict[str, set[str]] = defaultdict(set)
    for knowl in knowls:
        key = comparison_key(knowl.title)
        if key:
            term_registry[key].add(knowl.knowl_id)

    findings = [
        finding
        for knowl in knowls
        for finding in page_findings(
            knowl,
            incoming.get(knowl.knowl_id, Counter()),
            include_weak=include_weak,
        )
    ]
    findings.extend(
        exact_label_mismatches(
            all_uses,
            term_registry,
            {knowl.knowl_id: knowl for knowl in knowls},
        )
    )
    return sorted(
        findings,
        key=lambda item: (
            0 if item["severity"] == "high" else 1,
            -int(item["score"]),
            str(item["source_path"]),
            int(item.get("line", 0)),
        ),
    )


def print_text(findings: list[dict[str, object]]) -> None:
    for finding in findings:
        if finding["rule"] == "multiple_concept_ownership":
            subjects = ", ".join(
                f"{item['term']} ({item['section']}:{item['line']})"
                for item in finding["definition_subjects"]  # type: ignore[index]
            )
            print(
                f"{finding['severity']} score={finding['score']} "
                f"{finding['source_path']}: {finding['title']}\n"
                f"  signals: {', '.join(finding['signals'])}\n"
                f"  definienda: {subjects or '(none extracted)'}"
            )
        else:
            print(
                f"high score={finding['score']} {finding['source_path']}:"
                f"{finding['line']}: label {finding['label']!r} targets "
                f"{finding['actual_target']!r}; unique owner is "
                f"{finding['unique_label_owner']!r}"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path)
    parser.add_argument(
        "--format",
        choices=("text", "jsonl"),
        default="text",
        help="Output format (default: text).",
    )
    parser.add_argument(
        "--include-weak",
        action="store_true",
        help="Also report compound-title candidates lacking a stronger signal.",
    )
    parser.add_argument(
        "--fail-on-findings",
        action="store_true",
        help="Exit with status 1 when review findings are present.",
    )
    args = parser.parse_args()

    paths = knowl_paths(args.roots)
    try:
        knowls = [load_knowl(path) for path in paths]
    except (OSError, ValueError, tomllib.TOMLDecodeError) as error:
        print(f"Concept-scope audit could not read the corpus: {error}", file=sys.stderr)
        return 2

    findings = audit(knowls, include_weak=args.include_weak)
    if args.format == "jsonl":
        for finding in findings:
            print(json.dumps(finding, ensure_ascii=False, sort_keys=True))
    else:
        print_text(findings)
        print(
            f"Concept-scope audit: {len(paths)} knowls, "
            f"{len(findings)} review finding(s)."
        )
    return 1 if findings and args.fail_on_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
