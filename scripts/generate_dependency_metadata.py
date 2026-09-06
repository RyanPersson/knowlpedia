#!/usr/bin/env python3
"""Generate conservative prerequisite metadata from a knowl's definition core.

The default mode is report-only. Existing reviewed dependency metadata is never
changed. Use a deterministic sample report before applying the heuristic across
the corpus.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path


HEURISTIC_VERSION = "definition-links-v1"
SEMANTIC_REPAIR_VERSION = "semantic-cycle-repair-v1"
NON_CONCEPT_KINDS = {"document", "index", "page", "section"}
WIKILINK_RE = re.compile(
    r"\[\[([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*(?:#[^\]|]+)?)(?:\|((?:[^\]]|\](?=\]\])|\](?!\]))*?))?\]\](?!\])"
)
FENCED_CODE_RE = re.compile(r"^```[^\n]*\n.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"(?<!`)`[^`\n]+`(?!`)")
MATH_RE = re.compile(
    r"(?s)(\$\$.+?\$\$|\\\[.+?\\\]|\\\(.+?\\\)|(?<!\\)\$(?!\$).+?(?<!\\)\$)"
)
HEADING_RE = re.compile(r"^##\s+.+?\s*$", re.MULTILINE)
EXAMPLES_RE = re.compile(r"^\*\*(?:Example|Examples):\*\*\s*$", re.MULTILINE | re.IGNORECASE)


@dataclass(frozen=True)
class SourceKnowl:
    id: str
    title: str
    kind: str
    path: Path
    meta: dict[str, object]
    text: str
    frontmatter: str
    body: str


@dataclass(frozen=True)
class DependencyProposal:
    knowl: SourceKnowl
    inferred: tuple[str, ...]
    existing: tuple[str, ...]
    final: tuple[str, ...]
    review_count: int
    status: str

    def as_dict(self, repo_root: Path) -> dict[str, object]:
        return {
            "id": self.knowl.id,
            "title": self.knowl.title,
            "kind": self.knowl.kind,
            "path": str(self.knowl.path.relative_to(repo_root)),
            "inferred": list(self.inferred),
            "existing": list(self.existing),
            "final": list(self.final),
            "added": [item for item in self.final if item not in self.existing],
            "dependency_review_count": self.review_count,
            "heuristic": HEURISTIC_VERSION,
            "status": self.status,
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--sample-size", type=int, help="Report a deterministic random sample.")
    parser.add_argument("--seed", type=int, default=20260827)
    parser.add_argument("--paths-file", type=Path, help="Limit processing to repository-relative paths.")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write metadata for the selected files. Omit for the default report-only mode.",
    )
    return parser.parse_args()


def split_source(path: Path) -> SourceKnowl:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++\n"):
        raise ValueError(f"{path}: missing opening TOML front matter")
    end = text.find("\n+++\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated TOML front matter")
    frontmatter = text[4:end]
    body = text[end + 5 :]
    meta = tomllib.loads(frontmatter)
    return SourceKnowl(
        id=str(meta["id"]),
        title=str(meta["title"]),
        kind=str(meta.get("kind", "knowl")).lower(),
        path=path,
        meta=meta,
        text=text,
        frontmatter=frontmatter,
        body=body,
    )


def heading_offsets(markdown: str) -> list[int]:
    offsets: list[int] = []
    in_fence = False
    position = 0
    for line in markdown.splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"^##\s+", line):
            offsets.append(position)
        position += len(line)
    return offsets


def definition_core(markdown: str) -> str:
    """Match the compiler's short core closely enough for dependency seeding."""

    headings = heading_offsets(markdown)
    if not headings:
        core = markdown
    elif not markdown[: headings[0]].strip():
        first_line_end = markdown.find("\n", headings[0])
        first_line_end = len(markdown) if first_line_end == -1 else first_line_end + 1
        end = headings[1] if len(headings) > 1 else len(markdown)
        core = markdown[first_line_end:end]
    else:
        core = markdown[: headings[0]]
    examples = EXAMPLES_RE.search(core)
    if examples:
        core = core[: examples.start()]
    return core.strip()


def protected_for_wikilinks(markdown: str) -> str:
    protected = FENCED_CODE_RE.sub(" ", markdown)
    protected = INLINE_CODE_RE.sub(" ", protected)
    return MATH_RE.sub(" ", protected)


def infer_dependencies(knowl: SourceKnowl, known_ids: set[str]) -> tuple[str, ...]:
    core = protected_for_wikilinks(definition_core(knowl.body))
    inferred: list[str] = []
    for match in WIKILINK_RE.finditer(core):
        target = match.group(1).strip().split("#", 1)[0]
        if target == knowl.id or target not in known_ids or target in inferred:
            continue
        inferred.append(target)
    return tuple(inferred)


def nonnegative_review_count(knowl: SourceKnowl) -> int:
    value = knowl.meta.get("dependency_review_count", 0)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{knowl.path}: dependency_review_count must be a nonnegative integer")
    return value


def propose(knowl: SourceKnowl, known_ids: set[str]) -> DependencyProposal:
    review_count = nonnegative_review_count(knowl)
    raw_existing = knowl.meta.get("prerequisites", [])
    if not isinstance(raw_existing, list) or not all(isinstance(item, str) for item in raw_existing):
        raise ValueError(f"{knowl.path}: prerequisites must be a list of knowl IDs")
    existing = tuple(dict.fromkeys(raw_existing))
    inferred = infer_dependencies(knowl, known_ids)
    provenance = knowl.meta.get("dependency_heuristic")
    if review_count > 0:
        return DependencyProposal(knowl, inferred, existing, existing, review_count, "reviewed_preserved")
    if provenance == SEMANTIC_REPAIR_VERSION:
        return DependencyProposal(knowl, inferred, existing, existing, review_count, "semantic_repair_preserved")
    # Metadata owned by this heuristic is a cache of the current definition
    # core, so a rerun must remove candidates that disappeared when the core
    # was edited. Authored or legacy prerequisites are retained and augmented.
    if knowl.meta.get("dependency_heuristic") == HEURISTIC_VERSION:
        final = inferred
    else:
        final = tuple(dict.fromkeys((*existing, *inferred)))
    status = "unchanged" if (
        final == existing
        and knowl.meta.get("dependency_heuristic") == HEURISTIC_VERSION
        and "dependency_review_count" in knowl.meta
    ) else "proposed"
    return DependencyProposal(knowl, inferred, existing, final, review_count, status)


def toml_string_list(values: tuple[str, ...]) -> str:
    return "[" + ", ".join(json.dumps(value, ensure_ascii=False) for value in values) + "]"


def upsert_frontmatter_line(lines: list[str], key: str, rendered: str, after_keys: tuple[str, ...]) -> None:
    pattern = re.compile(rf"^{re.escape(key)}\s*=")
    for index, line in enumerate(lines):
        if pattern.match(line):
            lines[index] = f"{key} = {rendered}"
            return
    insert_at = len(lines)
    for index, line in enumerate(lines):
        if any(re.match(rf"^{re.escape(after)}\s*=", line) for after in after_keys):
            insert_at = index + 1
    lines.insert(insert_at, f"{key} = {rendered}")


def apply_proposal(proposal: DependencyProposal) -> bool:
    if proposal.status in {"reviewed_preserved", "semantic_repair_preserved"}:
        return False
    lines = proposal.knowl.frontmatter.splitlines()
    upsert_frontmatter_line(lines, "prerequisites", toml_string_list(proposal.final), ("domains",))
    prior_provenance = proposal.knowl.meta.get("dependency_heuristic")
    provenance = (
        f"authored+{HEURISTIC_VERSION}"
        if isinstance(prior_provenance, str) and prior_provenance.startswith("authored")
        else HEURISTIC_VERSION
    )
    upsert_frontmatter_line(lines, "dependency_heuristic", json.dumps(provenance), ("prerequisites",))
    upsert_frontmatter_line(lines, "dependency_review_count", "0", ("dependency_heuristic",))
    updated = "+++\n" + "\n".join(lines) + "\n+++\n" + proposal.knowl.body
    if updated == proposal.knowl.text:
        return False
    proposal.knowl.path.write_text(updated, encoding="utf-8")
    return True


def selected_paths(content_root: Path, paths_file: Path | None) -> list[Path]:
    if not paths_file:
        return sorted(content_root.rglob("*.knowl.md"))
    repo_root = content_root.parent
    return sorted(
        (repo_root / line.strip()).resolve()
        for line in paths_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def choose_sample(items: list[SourceKnowl], size: int | None, seed: int) -> list[SourceKnowl]:
    if size is None or size >= len(items):
        return items
    if size < 1:
        raise ValueError("sample size must be positive")
    return sorted(random.Random(seed).sample(items, size), key=lambda item: item.id)


def run(args: argparse.Namespace) -> dict[str, int]:
    content_root = args.content_root.resolve()
    repo_root = content_root.parent
    all_knowls = [split_source(path) for path in sorted(content_root.rglob("*.knowl.md"))]
    known_ids = {knowl.id for knowl in all_knowls}
    requested = {path.resolve() for path in selected_paths(content_root, args.paths_file)}
    eligible = [
        knowl
        for knowl in all_knowls
        if knowl.path.resolve() in requested and knowl.kind not in NON_CONCEPT_KINDS
    ]
    selected = choose_sample(eligible, args.sample_size, args.seed)
    proposals = [propose(knowl, known_ids) for knowl in selected]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        "".join(json.dumps(item.as_dict(repo_root), ensure_ascii=False) + "\n" for item in proposals),
        encoding="utf-8",
    )
    changed = 0
    if args.apply:
        changed = sum(apply_proposal(item) for item in proposals)
    return {
        "eligible": len(eligible),
        "selected": len(selected),
        "with_inferred_dependencies": sum(bool(item.inferred) for item in proposals),
        "inferred_edges": sum(len(item.inferred) for item in proposals),
        "reviewed_preserved": sum(item.status == "reviewed_preserved" for item in proposals),
        "semantic_repair_preserved": sum(item.status == "semantic_repair_preserved" for item in proposals),
        "changed": changed,
    }


def main() -> int:
    args = parse_args()
    try:
        stats = run(args)
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    action = "applied" if args.apply else "reported"
    print(f"{action} dependency metadata: " + ", ".join(f"{key}={value}" for key, value in stats.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
