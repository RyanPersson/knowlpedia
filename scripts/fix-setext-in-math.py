#!/usr/bin/env python3
"""
Fix setext heading conflicts inside $$...$$ display math blocks.

CommonMark interprets a line of only `=` or `-` as a setext heading underline,
which breaks Hugo's Goldmark passthrough extension for math blocks.

This script finds lines inside $$...$$ that would trigger setext parsing and
fixes them by appending `{}` (an empty LaTeX group) which is visually identical
but prevents the setext interpretation.

Patterns fixed:
- `=` alone on a line → `={}`
- `===` alone on a line → `==={}`
- `-` alone on a line → `-{}` (less common but possible)

See: https://github.com/gohugoio/hugo-goldmark-extensions/issues/17
"""

import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"

# Setext underline pattern: 0-3 spaces, one or more = or -, optional trailing whitespace
SETEXT_H1_PATTERN = re.compile(r'^([ \t]{0,3})(=+)([ \t]*)$')
SETEXT_H2_PATTERN = re.compile(r'^([ \t]{0,3})(-+)([ \t]*)$')


def fix_setext_in_math_blocks(content: str) -> tuple[str, int]:
    """Fix setext heading patterns inside $$...$$ blocks.

    Returns (fixed_content, count_of_fixes).
    """
    lines = content.split('\n')
    result = []
    fixes = 0
    in_math_block = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track entry/exit from $$ blocks
        # Note: $$ on its own line toggles state; $$...$$ on same line doesn't
        if stripped == '$$':
            in_math_block = not in_math_block
            result.append(line)
            i += 1
            continue

        # Check for $$content$$ on single line (doesn't toggle state)
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            result.append(line)
            i += 1
            continue

        # If inside a math block, check for setext patterns
        if in_math_block:
            # Check for setext H1 (=)
            match = SETEXT_H1_PATTERN.match(line)
            if match:
                indent, equals, trailing = match.groups()
                result.append(f'{indent}{equals}{{}}')
                fixes += 1
                i += 1
                continue

            # Check for setext H2 (-)
            match = SETEXT_H2_PATTERN.match(line)
            if match:
                indent, dashes, trailing = match.groups()
                result.append(f'{indent}{dashes}{{}}')
                fixes += 1
                i += 1
                continue

        result.append(line)
        i += 1

    return '\n'.join(result), fixes


def find_setext_in_math_blocks(content: str) -> list[tuple[int, str]]:
    """Find setext heading patterns inside $$...$$ blocks.

    Returns list of (line_number, line_content) tuples.
    """
    lines = content.split('\n')
    problems = []
    in_math_block = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        if stripped == '$$':
            in_math_block = not in_math_block
            continue

        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            continue

        if in_math_block:
            if SETEXT_H1_PATTERN.match(line) or SETEXT_H2_PATTERN.match(line):
                problems.append((i, line))

    return problems


def process_file(filepath: Path, dry_run: bool = False) -> tuple[bool, int]:
    """Process a single file. Returns (had_issues, fix_count)."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False, 0

    if dry_run:
        problems = find_setext_in_math_blocks(content)
        if problems:
            print(f"\n{filepath}:")
            for line_num, line_content in problems:
                print(f"  Line {line_num}: {line_content.strip()!r}")
        return bool(problems), len(problems)
    else:
        new_content, fixes = fix_setext_in_math_blocks(content)
        if fixes > 0:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"Fixed {fixes} setext pattern(s) in: {filepath}")
        return fixes > 0, fixes


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN - scanning for setext patterns inside $$...$$ blocks\n")
    else:
        print("Fixing setext patterns inside $$...$$ blocks\n")

    files_with_issues = 0
    total_fixes = 0

    for md_file in CONTENT_DIR.rglob("*.md"):
        if md_file.name == "_index.md":
            continue
        had_issues, fix_count = process_file(md_file, dry_run)
        if had_issues:
            files_with_issues += 1
            total_fixes += fix_count

    print(f"\n{'Found' if dry_run else 'Fixed'} {total_fixes} setext pattern(s) in {files_with_issues} file(s)")


if __name__ == "__main__":
    main()
