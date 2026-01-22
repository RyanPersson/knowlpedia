#!/usr/bin/env python3
"""
Collapse multi-line $$...$$ display math to single-line format.

Build-time KaTeX requires display math on a single line. This script converts:
    $$
    x = y
    $$
to:
    $$x = y$$

Preserves indentation for math inside list items, etc.
"""

import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"

def find_and_fix_multiline_dollar_blocks(content: str) -> str:
    """Find and collapse multi-line $$ blocks that have 2+ lines of LaTeX content.

    Single-line content like:
        $$
        x = y
        $$
    is fine and left alone.

    Only multi-line content like:
        $$
        x = y
        z = w
        $$
    needs to be collapsed.
    """
    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check if this line is just $$
        if stripped == '$$':
            indent = line[:len(line) - len(line.lstrip())]

            # Look for the closing $$
            math_lines = []
            j = i + 1
            while j < len(lines):
                inner_line = lines[j]
                inner_stripped = inner_line.strip()
                if inner_stripped == '$$':
                    # Found closing $$
                    # Only collapse if there are 2+ lines of LaTeX content
                    if len(math_lines) > 1:
                        collapsed = ' '.join(' '.join(math_lines).split())
                        result.append(f'{indent}$${collapsed}$$')
                    else:
                        # Single line content - keep original format
                        result.append(line)  # opening $$
                        for ml in math_lines:
                            result.append(ml)
                        result.append(lines[j])  # closing $$
                    i = j + 1
                    break
                else:
                    math_lines.append(inner_line)
                    j += 1
            else:
                # No closing $$ found, keep line as-is
                result.append(line)
                i += 1
        else:
            result.append(line)
            i += 1

    return '\n'.join(result)

def fix_multiline_dollar_math(content: str) -> str:
    """Convert multi-line $$...$$ to single-line $$...$$."""
    return find_and_fix_multiline_dollar_blocks(content)

def process_file(filepath: Path, dry_run: bool = False) -> bool:
    """Process a single file. Returns True if changes were made."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    new_content = fix_multiline_dollar_math(content)

    if new_content != content:
        if dry_run:
            print(f"Would fix: {filepath}")
        else:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"Fixed: {filepath}")
        return True
    return False

def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN - no files will be modified\n")

    files_checked = 0
    files_fixed = 0

    for md_file in CONTENT_DIR.rglob("*.md"):
        if md_file.name == "_index.md":
            continue
        files_checked += 1
        if process_file(md_file, dry_run):
            files_fixed += 1

    print(f"\nChecked {files_checked} files, fixed {files_fixed}")

if __name__ == "__main__":
    main()
