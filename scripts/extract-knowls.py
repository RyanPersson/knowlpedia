#!/usr/bin/env python3
"""
Extract knowls from Oracle session output logs.
Parses markdown code blocks and writes each knowl to its destination.
"""
import os
import re
import sys
from pathlib import Path

BLOG_ROOT = Path(__file__).parent.parent
CONTENT_DIR = BLOG_ROOT / "content"


def extract_knowls_from_log(log_path):
    """Extract knowl entries from an Oracle session log."""
    with open(log_path) as f:
        content = f.read()

    knowls = {}

    # Pattern: **`slug.md`** followed by ```markdown ... ```
    pattern = r'\*\*`([a-z0-9-]+)\.md`\*\*\s*\n```markdown\n(.*?)```'

    for match in re.finditer(pattern, content, re.DOTALL):
        slug = match.group(1)
        knowl_content = match.group(2).strip()
        knowls[slug] = knowl_content

    return knowls


def write_knowls(knowls, section_name):
    """Write knowls to the content directory."""
    section_dir = CONTENT_DIR / section_name
    section_dir.mkdir(parents=True, exist_ok=True)

    written = []
    for slug, content in knowls.items():
        file_path = section_dir / f"{slug}.md"
        with open(file_path, 'w') as f:
            f.write(content + '\n')
        written.append(slug)

    return written


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 extract-knowls.py <section-name> <session-name> [session-name...]")
        print("Example: python3 extract-knowls.py shared-foundations session-80 session-81")
        sys.exit(1)

    section_name = sys.argv[1]
    session_names = sys.argv[2:]

    all_knowls = {}

    for session in session_names:
        log_path = Path.home() / ".oracle/sessions" / session / "output.log"
        if not log_path.exists():
            print(f"Warning: {log_path} not found, skipping")
            continue

        knowls = extract_knowls_from_log(log_path)
        print(f"Extracted {len(knowls)} knowls from {session}")
        all_knowls.update(knowls)

    if not all_knowls:
        print("No knowls extracted!")
        sys.exit(1)

    written = write_knowls(all_knowls, section_name)
    print(f"\nWrote {len(written)} knowls to content/{section_name}/")

    # List written files
    for slug in sorted(written):
        print(f"  {slug}.md")


if __name__ == "__main__":
    main()
