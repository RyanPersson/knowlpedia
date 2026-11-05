#!/usr/bin/env python3
"""Flag knowls that a reader cannot find from their subject's landing pages.

A subject's landing page is the knowl whose ID is the subject itself. From
there, this follows links through the subject's sub-index pages (kind ``index``
or ``section``). A knowl in the subject that none of those pages lists is
missing, and a subject with no landing page is reported on its own.

Findings need a placement decision, so they fail only with --fail-on-findings.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "packages" / "compiler"))
import knowl_compile as compiler


HUB_KINDS = frozenset({"index", "section"})
# Collections read through a source rather than listing a subject's knowls.
EXCLUDED_SUBJECTS = frozenset(compiler.SOURCE_COLLECTIONS) | compiler.DIRECTORY_EXCLUDED_SUBJECTS
SITE_PATH_RE = re.compile(r"\]\(/([^)#\s]+?)/?(?:#[^)\s]*)?\)")


@dataclass
class SubjectReport:
    subject: str
    total: int
    has_landing_page: bool
    hubs: list[str] = field(default_factory=list)
    unreached_hubs: list[str] = field(default_factory=list)
    missing: list[dict[str, str]] = field(default_factory=list)


def linked_ids(markdown: str) -> set[str]:
    """IDs linked from page text, ignoring anything inside code."""
    text = compiler.FENCED_CODE_RE.sub("", markdown)
    text = compiler.INLINE_CODE_RE.sub("", text)
    # Math such as R[[x]] can match as a link, but never names a real knowl.
    links = {match.group(1).split("#", 1)[0].strip() for match in compiler.WIKILINK_RE.finditer(text)}
    links.update(match.group(1) for match in SITE_PATH_RE.finditer(text))
    return links


def load_knowls(content_dir: Path) -> list[compiler.Knowl]:
    return compiler.discover_knowls(content_dir)


def page_text(knowl: compiler.Knowl) -> str:
    return "\n\n".join([knowl.core_markdown, *(section.get("markdown", "") for section in knowl.sections)])


def audit(knowls: Iterable[compiler.Knowl]) -> list[SubjectReport]:
    all_knowls = list(knowls)
    redirects = {knowl.id: knowl.redirect_to for knowl in all_knowls if knowl.redirect_to}
    current = {knowl.id: knowl for knowl in all_knowls if not knowl.redirect_to}
    by_lowercase_path = {knowl_id.lower(): knowl_id for knowl_id in current}

    def resolve(target: str) -> str:
        seen: set[str] = set()
        while target in redirects and target not in seen:
            seen.add(target)
            target = redirects[target]
        return by_lowercase_path.get(target.lower(), target)

    subjects: dict[str, list[compiler.Knowl]] = {}
    for knowl in current.values():
        subject = knowl.id.split("/", 1)[0]
        if subject not in EXCLUDED_SUBJECTS:
            subjects.setdefault(subject, []).append(knowl)

    reports = []
    for subject, members in sorted(subjects.items()):
        hubs = sorted(knowl.id for knowl in members if knowl.kind.lower() in HUB_KINDS and knowl.id != subject)
        report = SubjectReport(subject, len(members), subject in current, hubs)
        listed: set[str] = set()
        if report.has_landing_page:
            listed.add(subject)
            pending = [subject]
            visited: set[str] = set()
            while pending:
                page = pending.pop()
                if page in visited:
                    continue
                visited.add(page)
                for target in map(resolve, linked_ids(page_text(current[page]))):
                    listed.add(target)
                    item = current.get(target)
                    if item and item.kind.lower() in HUB_KINDS and target.split("/", 1)[0] == subject:
                        pending.append(target)
            report.unreached_hubs = [hub for hub in hubs if hub not in visited]
        report.missing = [
            {"id": knowl.id, "title": knowl.title, "kind": knowl.kind}
            for knowl in sorted(members, key=lambda item: item.id)
            if knowl.id not in listed
        ]
        reports.append(report)
    return reports


def print_text(reports: list[SubjectReport], *, list_all: bool) -> None:
    for report in reports:
        if report.has_landing_page and not report.missing and not report.unreached_hubs:
            continue
        notes = [f"{len(report.missing)} of {report.total} knowls missing"]
        if not report.has_landing_page:
            notes.append("no landing page")
        if report.unreached_hubs:
            notes.append(f"{len(report.unreached_hubs)} unlinked sub-index pages")
        print(f"{report.subject}: {'; '.join(notes)}")
        if list_all:
            for item in report.missing:
                print(f"  {item['id']} ({item['kind']}): {item['title']}")
    missing = sum(len(report.missing) for report in reports)
    print(f"{missing} missing knowls across {sum(bool(report.missing) for report in reports)} of {len(reports)} subjects")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("content_dir", type=Path, help="Content directory, such as ../knowlpedia-content/content")
    parser.add_argument("--summary", action="store_true", help="Print per-subject counts without listing each knowl")
    parser.add_argument("--json", type=Path, help="Also write the full report as JSON")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit nonzero when anything is flagged")
    args = parser.parse_args()
    if not args.content_dir.is_dir():
        parser.error(f"no such directory: {args.content_dir}")

    reports = audit(load_knowls(args.content_dir))
    print_text(reports, list_all=not args.summary)
    if args.json:
        args.json.write_text(json.dumps([report.__dict__ for report in reports], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    flagged = any(report.missing or report.unreached_hubs or not report.has_landing_page for report in reports)
    return 1 if args.fail_on_findings and flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
