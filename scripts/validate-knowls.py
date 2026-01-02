#!/usr/bin/env python3
"""
Validate knowl references in the content directory.
Checks that all {{< knowl id="..." section="..." >}} references point to existing files.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# Pattern to match knowl shortcodes
KNOWL_PATTERN = re.compile(r'\{\{<\s*knowl\s+([^>]+)>\}\}')
# Pattern to extract id and section from shortcode attributes
ID_PATTERN = re.compile(r'id="([^"]+)"')
SECTION_PATTERN = re.compile(r'section="([^"]+)"')


def find_knowl_references(content_dir: Path):
    """Find all knowl references in markdown files."""
    references = []

    for md_file in content_dir.rglob("*.md"):
        # Skip _index.md files
        if md_file.name == "_index.md":
            continue

        # Get the section from the file's parent directory
        file_section = md_file.parent.name

        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}", file=sys.stderr)
            continue

        for match in KNOWL_PATTERN.finditer(content):
            attrs = match.group(1)

            id_match = ID_PATTERN.search(attrs)
            section_match = SECTION_PATTERN.search(attrs)

            if id_match:
                knowl_id = id_match.group(1)
                # If no section specified, use the file's section
                knowl_section = section_match.group(1) if section_match else file_section

                references.append({
                    'source_file': md_file,
                    'knowl_id': knowl_id,
                    'knowl_section': knowl_section,
                    'line_content': match.group(0)
                })

    return references


def validate_references(content_dir: Path, references: list):
    """Check if referenced knowl files exist."""
    broken = []
    valid_count = 0

    for ref in references:
        target_path = content_dir / ref['knowl_section'] / f"{ref['knowl_id']}.md"

        if not target_path.exists():
            broken.append(ref)
        else:
            valid_count += 1

    return broken, valid_count


def main():
    # Find content directory
    script_dir = Path(__file__).parent
    content_dir = script_dir.parent / "content"

    if not content_dir.exists():
        print(f"Error: Content directory not found at {content_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning {content_dir} for knowl references...")

    references = find_knowl_references(content_dir)
    print(f"Found {len(references)} knowl references")

    broken, valid_count = validate_references(content_dir, references)

    if broken:
        print(f"\n{len(broken)} BROKEN references found:\n")

        # Group by source file for cleaner output
        by_source = defaultdict(list)
        for ref in broken:
            by_source[ref['source_file']].append(ref)

        for source_file, refs in sorted(by_source.items()):
            rel_path = source_file.relative_to(content_dir.parent)
            print(f"{rel_path}:")
            for ref in refs:
                target = f"{ref['knowl_section']}/{ref['knowl_id']}.md"
                print(f"  -> {target} (missing)")
            print()

        print(f"Summary: {valid_count} valid, {len(broken)} broken")
        sys.exit(1)
    else:
        print(f"\nAll {valid_count} knowl references are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
