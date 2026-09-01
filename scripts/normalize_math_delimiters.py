#!/usr/bin/env python3
"""Normalize Markdown math to ``\\(...\\)`` and ``\\[...\\]`` delimiters.

The compiler intentionally continues to accept both the TeX-style delimiters
and Markdown's ``$...$`` / ``$$...$$`` forms.  This script only establishes a
canonical spelling in source files.  Markdown code spans and fenced code blocks
are left untouched.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DOLLAR_MATH_RE = re.compile(
    r"(?s)\$\$(.+?)\$\$|(?<!\\)\$(?!\$)(.+?)(?<!\\)\$"
)
FENCE_OPEN_RE = re.compile(r"(?m)^(?P<indent> {0,3})(?P<marker>`{3,}|~{3,})[^\n]*(?:\n|$)")


@dataclass(frozen=True)
class Normalization:
    text: str
    inline_count: int
    display_count: int


def _fenced_code_ranges(text: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    position = 0
    while opening := FENCE_OPEN_RE.search(text, position):
        marker = opening.group("marker")
        closing_re = re.compile(
            rf"(?m)^ {{0,3}}{re.escape(marker[0])}{{{len(marker)},}}[ \t]*(?:\n|$)"
        )
        closing = closing_re.search(text, opening.end())
        end = closing.end() if closing else len(text)
        ranges.append((opening.start(), end))
        position = end
    return ranges


def _inline_code_ranges(text: str, excluded: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    excluded_index = 0
    position = 0
    while position < len(text):
        while excluded_index < len(excluded) and excluded[excluded_index][1] <= position:
            excluded_index += 1
        if excluded_index < len(excluded):
            start, end = excluded[excluded_index]
            if start <= position < end:
                position = end
                continue
        if text[position] != "`":
            position += 1
            continue
        end_of_run = position + 1
        while end_of_run < len(text) and text[end_of_run] == "`":
            end_of_run += 1
        marker = text[position:end_of_run]
        closing = text.find(marker, end_of_run)
        if closing == -1:
            position = end_of_run
            continue
        ranges.append((position, closing + len(marker)))
        position = closing + len(marker)
    return ranges


def _protect_code(text: str) -> tuple[str, dict[str, str]]:
    fenced = _fenced_code_ranges(text)
    ranges = sorted(fenced + _inline_code_ranges(text, fenced))
    replacements: dict[str, str] = {}
    chunks: list[str] = []
    position = 0
    for start, end in ranges:
        chunks.append(text[position:start])
        token = f"\x00KNOWL_CODE_{len(replacements)}\x00"
        replacements[token] = text[start:end]
        chunks.append(token)
        position = end
    chunks.append(text[position:])
    return "".join(chunks), replacements


def _normalize_dollars(
    text: str,
    *,
    inline_open: str = r"\(",
    inline_close: str = r"\)",
    display_open: str = r"\[",
    display_close: str = r"\]",
) -> Normalization:
    inline_count = 0
    display_count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal inline_count, display_count
        if match.group(1) is not None:
            display_count += 1
            return f"{display_open}{match.group(1)}{display_close}"
        inline_count += 1
        return f"{inline_open}{match.group(2)}{inline_close}"

    return Normalization(DOLLAR_MATH_RE.sub(replace, text), inline_count, display_count)


def normalize_text(text: str) -> Normalization:
    protected, code_replacements = _protect_code(text)
    result = _normalize_dollars(protected)
    normalized = result.text
    for token, code in code_replacements.items():
        normalized = normalized.replace(token, code)
    return Normalization(normalized, result.inline_count, result.display_count)


def _normalize_toml_strings(front_matter: str) -> Normalization:
    """Normalize math inside TOML strings without introducing invalid escapes."""

    chunks: list[str] = []
    inline_count = 0
    display_count = 0
    position = 0
    length = len(front_matter)

    while position < length:
        if front_matter[position] == "#":
            end = front_matter.find("\n", position)
            end = length if end == -1 else end
            chunks.append(front_matter[position:end])
            position = end
            continue

        quote = front_matter[position]
        if quote not in {"'", '"'}:
            chunks.append(quote)
            position += 1
            continue

        marker = quote * 3 if front_matter.startswith(quote * 3, position) else quote
        content_start = position + len(marker)
        content_end = content_start
        if quote == "'":
            found = front_matter.find(marker, content_start)
            content_end = length if found == -1 else found
        else:
            while content_end < length:
                if front_matter.startswith(marker, content_end):
                    backslashes = 0
                    check = content_end - 1
                    while check >= content_start and front_matter[check] == "\\":
                        backslashes += 1
                        check -= 1
                    if backslashes % 2 == 0:
                        break
                content_end += 1

        content = front_matter[content_start:content_end]
        if quote == '"':
            result = _normalize_dollars(
                content,
                inline_open=r"\\(",
                inline_close=r"\\)",
                display_open=r"\\[",
                display_close=r"\\]",
            )
        else:
            result = _normalize_dollars(content)
        chunks.extend((marker, result.text))
        inline_count += result.inline_count
        display_count += result.display_count
        if content_end < length:
            chunks.append(marker)
            position = content_end + len(marker)
        else:
            position = length

    return Normalization("".join(chunks), inline_count, display_count)


def normalize_knowl_source(text: str) -> Normalization:
    if not text.startswith("+++\n"):
        return normalize_text(text)
    closing = text.find("\n+++", 4)
    if closing == -1:
        return normalize_text(text)
    front_end = closing + len("\n+++")
    front = _normalize_toml_strings(text[:front_end])
    body = normalize_text(text[front_end:])
    return Normalization(
        front.text + body.text,
        front.inline_count + body.inline_count,
        front.display_count + body.display_count,
    )


def iter_source_files(paths: Iterable[Path]) -> Iterable[Path]:
    seen: set[Path] = set()
    for path in paths:
        candidates = path.rglob("*.knowl.md") if path.is_dir() else (path,)
        for candidate in candidates:
            resolved = candidate.resolve()
            if resolved not in seen and candidate.is_file():
                seen.add(resolved)
                yield candidate


def normalize_paths(paths: Iterable[Path], *, check: bool) -> tuple[int, int, int]:
    changed_files = 0
    inline_count = 0
    display_count = 0
    for path in iter_source_files(paths):
        original = path.read_text(encoding="utf-8")
        result = normalize_knowl_source(original)
        if result.text == original:
            continue
        changed_files += 1
        inline_count += result.inline_count
        display_count += result.display_count
        if not check:
            path.write_text(result.text, encoding="utf-8")
    return changed_files, inline_count, display_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="knowl files or directories")
    parser.add_argument(
        "--check",
        action="store_true",
        help="report files needing normalization without changing them",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    missing = [str(path) for path in args.paths if not path.exists()]
    if missing:
        print(f"Missing path(s): {', '.join(missing)}", file=sys.stderr)
        return 2
    changed, inline, display = normalize_paths(args.paths, check=args.check)
    action = "would normalize" if args.check else "normalized"
    print(
        f"{action} {changed} file(s): "
        f"{inline} inline and {display} display delimiter pair(s)"
    )
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
