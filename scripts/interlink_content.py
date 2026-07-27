#!/usr/bin/env python3
"""Find and optionally apply missing semantic links in Knowlpedia content.

The default mode is read-only: candidates are written as JSON Lines.  The
script deliberately ignores front matter, headings, references, code, math,
Markdown links, and existing ``[[target|label]]`` wrappers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tomllib
from dataclasses import dataclass
from pathlib import Path


FRONTMATTER_FENCE = "+++"
WIKILINK_RE = re.compile(r"\[\[([^|\]\n]+)\|([^\]\n]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\([^) \n]+(?:\s+\"[^\"]*\")?\)")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
EMPHASIS_RE = re.compile(r"\*\*[^*\n]+\*\*|(?<!\*)\*[^*\n]+\*(?!\*)")
INLINE_MATH_RE = re.compile(
    r"\\\([^\n]*?\\\)|\\\[[^\n]*?\\\]|\$\$[^\n]*?\$\$|(?<!\\)\$(?!\$)[^\n$]*?(?<!\\)\$"
)
WORD_RE = re.compile(r"\w", re.UNICODE)
REFERENCE_HEADINGS = {
    "bibliography",
    "literature",
    "reference",
    "references",
    "sources",
}
NON_CONTENT_KINDS = {"document", "index", "page", "section"}


@dataclass(frozen=True)
class Knowl:
    id: str
    title: str
    aliases: tuple[str, ...]
    kind: str
    path: Path


@dataclass(frozen=True)
class Term:
    surface: str
    normalized: str
    target: str
    origin: str


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    source_id: str
    source_path: str
    line: int
    column: int
    surface: str
    target: str
    origin: str
    section: str
    context: str

    def as_dict(self) -> dict[str, object]:
        return {
            "candidate_id": self.candidate_id,
            "source_id": self.source_id,
            "source_path": self.source_path,
            "line": self.line,
            "column": self.column,
            "surface": self.surface,
            "target": self.target,
            "origin": self.origin,
            "section": self.section,
            "context": self.context,
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-root",
        type=Path,
        required=True,
        help="Directory containing the section folders and *.knowl.md files.",
    )
    parser.add_argument(
        "--git-added-since",
        metavar="REV",
        help="Scan files added between REV and HEAD in the content repository.",
    )
    parser.add_argument(
        "--paths-file",
        type=Path,
        help="Scan repository-relative paths listed one per line.",
    )
    parser.add_argument(
        "--include-aliases",
        action="store_true",
        help="Use explicit front-matter aliases in addition to canonical titles.",
    )
    parser.add_argument(
        "--include-plurals",
        action="store_true",
        help="Generate conservative English plural variants of title terms.",
    )
    parser.add_argument(
        "--allow-single-word",
        action="store_true",
        help="Permit single-word terms; disabled by default to reduce ambiguity.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        required=True,
        help="JSONL candidate ledger to write.",
    )
    parser.add_argument(
        "--accept-file",
        type=Path,
        help="File containing candidate IDs to apply, one per line.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply exactly the candidates named by --accept-file.",
    )
    return parser.parse_args()


def split_frontmatter(text: str) -> tuple[dict[str, object], list[str], int]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != FRONTMATTER_FENCE:
        raise ValueError("missing opening +++ front-matter fence")
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_FENCE:
            raw = "".join(lines[1:index])
            return tomllib.loads(raw), lines, index + 1
    raise ValueError("missing closing +++ front-matter fence")


def load_knowls(content_root: Path) -> tuple[dict[str, Knowl], dict[Path, Knowl]]:
    by_id: dict[str, Knowl] = {}
    by_path: dict[Path, Knowl] = {}
    for path in sorted(content_root.rglob("*.knowl.md")):
        meta, _, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        knowl_id = str(meta["id"])
        knowl = Knowl(
            id=knowl_id,
            title=str(meta["title"]),
            aliases=tuple(str(alias) for alias in meta.get("aliases", [])),
            kind=str(meta.get("kind", "knowl")),
            path=path,
        )
        if knowl_id in by_id:
            raise ValueError(f"duplicate knowl id: {knowl_id}")
        by_id[knowl_id] = knowl
        by_path[path.resolve()] = knowl
    return by_id, by_path


def normalize_surface(surface: str) -> str:
    return " ".join(surface.casefold().split())


def is_plain_term(surface: str, allow_single_word: bool) -> bool:
    if not surface or len(surface) < 3 or len(surface) > 120:
        return False
    if any(token in surface for token in ("[[", "]]", "\\", "/", "_", "=", "{", "}")):
        return False
    if not allow_single_word and len(surface.split()) < 2:
        return False
    return bool(WORD_RE.search(surface))


def plural_variant(surface: str) -> str | None:
    words = surface.split()
    if not words:
        return None
    final = words[-1]
    lower = final.casefold()
    if lower.endswith(("s", "x", "z", "ch", "sh")):
        plural = final + "es"
    elif lower.endswith("y") and len(final) > 1 and final[-2].casefold() not in "aeiou":
        plural = final[:-1] + "ies"
    else:
        plural = final + "s"
    return " ".join([*words[:-1], plural])


def build_terms(
    knowls: dict[str, Knowl],
    *,
    include_aliases: bool,
    include_plurals: bool,
    allow_single_word: bool,
) -> list[Term]:
    claims: dict[str, list[tuple[str, str, str]]] = {}
    for knowl in knowls.values():
        if knowl.kind in NON_CONTENT_KINDS:
            continue
        surfaces: list[tuple[str, str]] = [(knowl.title, "title")]
        if include_aliases:
            surfaces.extend((alias, "alias") for alias in knowl.aliases)
        for surface, origin in surfaces:
            surface = " ".join(surface.split())
            if is_plain_term(surface, allow_single_word):
                claims.setdefault(normalize_surface(surface), []).append(
                    (surface, knowl.id, origin)
                )
            if include_plurals:
                plural = plural_variant(surface)
                if plural and is_plain_term(plural, allow_single_word):
                    claims.setdefault(normalize_surface(plural), []).append(
                        (plural, knowl.id, f"{origin}_plural")
                    )

    terms: list[Term] = []
    for normalized, entries in claims.items():
        targets = {target for _, target, _ in entries}
        if len(targets) != 1:
            continue
        surface, target, origin = sorted(
            entries,
            key=lambda item: (
                0 if item[2] == "title" else 1,
                len(item[0]),
                item[0],
            ),
        )[0]
        terms.append(Term(surface, normalized, target, origin))
    return sorted(terms, key=lambda term: (-len(term.surface), term.normalized, term.target))


def source_paths(
    content_root: Path,
    *,
    git_added_since: str | None,
    paths_file: Path | None,
) -> list[Path]:
    repo = content_root.parent
    if git_added_since:
        output = subprocess.check_output(
            [
                "git",
                "-C",
                str(repo),
                "diff",
                "--name-only",
                "--diff-filter=A",
                f"{git_added_since}..HEAD",
                "--",
                str(content_root.relative_to(repo)),
            ],
            text=True,
        )
        paths = [repo / line for line in output.splitlines() if line.strip()]
    elif paths_file:
        paths = [
            repo / line.strip()
            for line in paths_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    else:
        paths = sorted(content_root.rglob("*.knowl.md"))
    return sorted(
        path.resolve()
        for path in paths
        if path.name.endswith(".knowl.md") and path.exists()
    )


def protected_spans(line: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for regex in (
        WIKILINK_RE,
        MARKDOWN_LINK_RE,
        INLINE_CODE_RE,
        EMPHASIS_RE,
        INLINE_MATH_RE,
    ):
        spans.extend((match.start(), match.end()) for match in regex.finditer(line))
    return sorted(spans)


def overlaps(start: int, end: int, spans: list[tuple[int, int]]) -> bool:
    return any(start < span_end and end > span_start for span_start, span_end in spans)


def compile_term_pattern(terms: list[Term]) -> re.Pattern[str]:
    alternatives = [
        re.escape(term.surface).replace(r"\ ", r"\s+")
        for term in terms
    ]
    return re.compile(
        rf"(?<![\w-])(?:{'|'.join(alternatives)})(?![\w-])",
        re.IGNORECASE,
    )


def candidate_id(
    source_id: str,
    line: int,
    column: int,
    surface: str,
    target: str,
) -> str:
    payload = f"{source_id}\0{line}\0{column}\0{surface}\0{target}".encode()
    return hashlib.sha256(payload).hexdigest()[:20]


def scan_file(
    path: Path,
    knowl: Knowl,
    terms_by_normalized: dict[str, Term],
    term_pattern: re.Pattern[str],
    repo: Path,
) -> list[Candidate]:
    text = path.read_text(encoding="utf-8")
    _, lines, body_start = split_frontmatter(text)
    linked_targets = {match.group(1).split("#", 1)[0] for match in WIKILINK_RE.finditer(text)}
    claimed_targets = set(linked_targets)
    candidates: list[Candidate] = []
    section = "core"
    in_fence = False
    in_display_math = False

    for index, raw_line in enumerate(lines[body_start:], start=body_start + 1):
        line = raw_line.rstrip("\r\n")
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith(r"\[") or stripped.startswith("$$"):
            if not (
                (stripped.startswith(r"\[") and stripped.endswith(r"\]") and len(stripped) > 4)
                or (stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4)
            ):
                in_display_math = not in_display_math
            continue
        if in_display_math:
            if stripped.endswith(r"\]") or stripped.endswith("$$"):
                in_display_math = False
            continue
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if line.startswith("#"):
            continue
        if section.casefold() in REFERENCE_HEADINGS:
            continue
        if not stripped:
            continue

        spans = protected_spans(line)
        occupied = list(spans)
        line_matches: list[tuple[int, int, Term, str]] = []
        for match in term_pattern.finditer(line):
            surface = match.group(0)
            term = terms_by_normalized[normalize_surface(surface)]
            if term.target == knowl.id or term.target in claimed_targets:
                continue
            start, end = match.span()
            if overlaps(start, end, occupied):
                continue
            line_matches.append((start, end, term, surface))

        for start, end, term, surface in sorted(
            line_matches,
            key=lambda item: (item[0], -(item[1] - item[0]), item[2].target),
        ):
            if term.target in claimed_targets or overlaps(start, end, occupied):
                continue
            occupied.append((start, end))
            claimed_targets.add(term.target)
            candidates.append(
                Candidate(
                    candidate_id=candidate_id(
                        knowl.id, index, start + 1, surface, term.target
                    ),
                    source_id=knowl.id,
                    source_path=str(path.relative_to(repo)),
                    line=index,
                    column=start + 1,
                    surface=surface,
                    target=term.target,
                    origin=term.origin,
                    section=section,
                    context=stripped,
                )
            )
    return candidates


def apply_candidates(
    repo: Path,
    candidates: list[Candidate],
    accepted_ids: set[str],
) -> tuple[int, int]:
    selected = [candidate for candidate in candidates if candidate.candidate_id in accepted_ids]
    missing = accepted_ids - {candidate.candidate_id for candidate in selected}
    if missing:
        raise ValueError(f"accepted candidate IDs not found in fresh scan: {sorted(missing)}")

    by_path: dict[str, list[Candidate]] = {}
    for candidate in selected:
        by_path.setdefault(candidate.source_path, []).append(candidate)

    applied = 0
    for relative, path_candidates in sorted(by_path.items()):
        path = repo / relative
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        for candidate in sorted(
            path_candidates,
            key=lambda item: (item.line, item.column),
            reverse=True,
        ):
            line_index = candidate.line - 1
            line = lines[line_index]
            start = candidate.column - 1
            end = start + len(candidate.surface)
            if line[start:end] != candidate.surface:
                raise ValueError(
                    f"stale candidate {candidate.candidate_id}: "
                    f"{relative}:{candidate.line}:{candidate.column}"
                )
            wrapper = f"[[{candidate.target}|{candidate.surface}]]"
            lines[line_index] = line[:start] + wrapper + line[end:]
            applied += 1
        path.write_text("".join(lines), encoding="utf-8")
    return applied, len(by_path)


def main() -> int:
    args = parse_args()
    if args.apply and not args.accept_file:
        raise SystemExit("--apply requires --accept-file")

    content_root = args.content_root.resolve()
    repo = content_root.parent
    knowls, by_path = load_knowls(content_root)
    terms = build_terms(
        knowls,
        include_aliases=args.include_aliases,
        include_plurals=args.include_plurals,
        allow_single_word=args.allow_single_word,
    )
    terms_by_normalized = {term.normalized: term for term in terms}
    term_pattern = compile_term_pattern(terms)
    paths = source_paths(
        content_root,
        git_added_since=args.git_added_since,
        paths_file=args.paths_file.resolve() if args.paths_file else None,
    )

    candidates: list[Candidate] = []
    for path in paths:
        knowl = by_path.get(path)
        if knowl is None:
            raise ValueError(f"source path is not a registered knowl: {path}")
        candidates.extend(
            scan_file(
                path,
                knowl,
                terms_by_normalized,
                term_pattern,
                repo,
            )
        )

    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8") as handle:
        for candidate in candidates:
            handle.write(json.dumps(candidate.as_dict(), ensure_ascii=False) + "\n")

    applied = changed_files = 0
    if args.apply:
        accepted_ids = {
            line.strip()
            for line in args.accept_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
        applied, changed_files = apply_candidates(repo, candidates, accepted_ids)

    print(f"scanned_files={len(paths)}")
    print(f"registry_knowls={len(knowls)}")
    print(f"candidate_terms={len(terms)}")
    print(f"candidates={len(candidates)}")
    print(f"applied={applied}")
    print(f"changed_files={changed_files}")
    print(f"report={args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
