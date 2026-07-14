#!/usr/bin/env python3
"""Prove that progressive section parsing preserves source content in order."""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path


COMPILER_PATH = Path(__file__).resolve().parents[1] / "packages" / "compiler" / "knowl_compile.py"
SPEC = importlib.util.spec_from_file_location("knowl_compile_for_audit", COMPILER_PATH)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


def source_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n+++\n", 4)
    if not text.startswith("+++\n") or end == -1:
        raise ValueError(f"{path}: malformed front matter")
    return text[end + 5 :].strip()


def content_lines(text: str) -> list[str]:
    result: list[str] = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            result.append(line.rstrip())
            continue
        if not in_fence and re.match(r"^##\s+", line):
            continue
        if not in_fence and re.match(r"^\*\*Examples?:\*\*\s*$", stripped, re.IGNORECASE):
            continue
        if stripped:
            result.append(line.rstrip())
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("content_root", type=Path)
    args = parser.parse_args()

    failures: list[Path] = []
    checked = 0
    section_count = 0
    for path in sorted(args.content_root.rglob("*.knowl.md")):
        body = source_body(path)
        knowl = compiler.parse_single_file(path)
        core, sections = knowl.core_markdown, knowl.sections
        reconstructed = "\n".join([core, *(section["markdown"] for section in sections)])
        if content_lines(body) != content_lines(reconstructed):
            failures.append(path)
        checked += 1
        section_count += len(sections)

    if failures:
        for path in failures[:20]:
            print(f"content-order mismatch: {path}", file=sys.stderr)
        print(f"Failed: {len(failures)} of {checked} files", file=sys.stderr)
        return 1

    print(f"Section audit passed: {checked} files, {section_count} extracted sections, content order preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
