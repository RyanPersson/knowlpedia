#!/usr/bin/env python3
"""
Generate minimal-current-inventory.md from the actual filesystem content.

This script scans all knowl sections and creates a compact inventory file
organized by directory and type (based on filename patterns).

Usage:
    python3 scripts/tests/generate_inventory.py              # Print to stdout
    python3 scripts/tests/generate_inventory.py --write      # Write to file
    python3 scripts/tests/generate_inventory.py --diff       # Show what would change
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import date

REPO_ROOT = Path(__file__).parent.parent.parent
CONTENT_DIR = REPO_ROOT / "content"
INVENTORY_FILE = REPO_ROOT / "docs" / "knowl-modules" / "minimal-current-inventory.md"

# Section groupings for organization
SECTION_GROUPS = {
    "Shared Pools": ["shared-foundations", "linear-algebra"],
    "Analysis Modules": ["real-analysis", "topology", "measure-theory"],
    "Algebra Modules": [
        "algebra-groups", "algebra-rings", "algebra-modules",
        "algebra-fields-galois", "algebra-commutative", "algebra-homological",
        "algebra-representation-theory", "algebra-category-theory"
    ],
    "Specialized Modules": [
        "convex-analysis", "lie-groups", "fiber-bundles",
        "langlands-letter", "shale-paper"
    ],
    "Physics Modules": [
        "thermodynamics", "stat-mech", "stat-mech-lattice", "stat-mech-quantum",
        "quantum-foundations"
    ],
    "Probability & Analysis": [
        "probability", "large-deviations", "asymptotics", "discrete-structures"
    ],
    "Geometry": ["differential-geometry"],
}

# Flatten to get all sections in order
ALL_SECTIONS = []
for sections in SECTION_GROUPS.values():
    ALL_SECTIONS.extend(sections)

# Patterns to classify knowls by type
TYPE_PATTERNS = [
    ("Theorems", re.compile(r'-theorem$|^theorem-')),
    ("Lemmas", re.compile(r'-lemma$|^lemma-')),
    ("Corollaries", re.compile(r'-corollary$|^corollary-')),
    ("Propositions", re.compile(r'-proposition$|^proposition-')),
    ("Axioms", re.compile(r'-axiom|^axiom-')),
    ("Tests/Criteria", re.compile(r'-test$|-criterion$|^test-|^criterion-')),
    ("Conventions", re.compile(r'-convention$|^convention-')),
    ("Examples", re.compile(r'^example-|^counterexample-')),
    ("Constructions", re.compile(r'^construction-')),
    ("TFAE", re.compile(r'^tfae-')),
    # Default: Definitions (anything not matching above)
]


def classify_knowl(slug: str) -> str:
    """Classify a knowl slug into a type category."""
    for type_name, pattern in TYPE_PATTERNS:
        if pattern.search(slug):
            return type_name
    return "Definitions"


def get_section_knowls(section: str) -> dict:
    """Get all knowls in a section, organized by type."""
    sec_dir = CONTENT_DIR / section
    if not sec_dir.exists():
        return {}

    by_type = defaultdict(list)
    for f in sorted(sec_dir.glob("*.md")):
        if f.name == "_index.md":
            continue
        slug = f.stem
        knowl_type = classify_knowl(slug)
        by_type[knowl_type].append(slug)

    return dict(by_type)


def generate_inventory() -> str:
    """Generate the full inventory markdown content."""
    lines = [
        "# Minimal Knowl Inventory",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "Compact listing of all knowl filenames by directory and type.",
        "",
        "---",
    ]

    total = 0
    section_counts = []

    for group_name, sections in SECTION_GROUPS.items():
        # Check if any sections in this group have content
        has_content = any(
            (CONTENT_DIR / sec).exists() and
            any((CONTENT_DIR / sec).glob("*.md"))
            for sec in sections
        )
        if not has_content:
            continue

        lines.append("")
        lines.append(f"## {group_name}")

        for section in sections:
            knowls_by_type = get_section_knowls(section)
            if not knowls_by_type:
                continue

            count = sum(len(slugs) for slugs in knowls_by_type.values())
            total += count
            section_counts.append((section, count))

            lines.append("")
            lines.append(f"### `{section}` ({count})")
            lines.append("")

            # Output in a consistent type order
            type_order = ["Definitions", "Theorems", "Lemmas", "Corollaries",
                          "Propositions", "Axioms", "Conventions", "Tests/Criteria",
                          "Examples", "Constructions", "TFAE"]

            for type_name in type_order:
                if type_name in knowls_by_type:
                    slugs = knowls_by_type[type_name]
                    lines.append(f"**{type_name}:** ({len(slugs)})")
                    lines.append(", ".join(slugs))
                    lines.append("")

            # Any other types not in the order
            for type_name, slugs in sorted(knowls_by_type.items()):
                if type_name not in type_order:
                    lines.append(f"**{type_name}:** ({len(slugs)})")
                    lines.append(", ".join(slugs))
                    lines.append("")

            lines.append("---")

    # Summary table
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Section | Count |")
    lines.append("|---------|-------|")
    for section, count in section_counts:
        lines.append(f"| {section} | {count} |")
    lines.append(f"| **Total** | **{total}** |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate knowl inventory from filesystem")
    parser.add_argument("--write", "-w", action="store_true",
                        help="Write to minimal-current-inventory.md")
    parser.add_argument("--diff", "-d", action="store_true",
                        help="Show what would change (requires diff command)")
    args = parser.parse_args()

    content = generate_inventory()

    if args.diff:
        import tempfile
        import subprocess
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_path = f.name
        try:
            subprocess.run(["diff", "-u", str(INVENTORY_FILE), temp_path])
        finally:
            os.unlink(temp_path)
    elif args.write:
        INVENTORY_FILE.write_text(content)
        print(f"Wrote {INVENTORY_FILE}")
    else:
        print(content)


if __name__ == "__main__":
    main()
