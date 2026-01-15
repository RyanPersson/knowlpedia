#!/usr/bin/env python3
"""
Prepare batch prompts for knowl generation via Oracle.
Extracts slugs from proposed-analysis-reorg.md and creates batch prompt files.
"""
import os
import re
import sys
from pathlib import Path

BLOG_ROOT = Path(__file__).parent.parent
PROPOSED_REORG = BLOG_ROOT / "docs/knowl-modules/proposed-analysis-reorg.md"
BATCH_DIR = BLOG_ROOT / "tmp/batches"
BATCH_SIZE = 17  # ~17 slugs per batch for reliable generation

PROMPT_TEMPLATE = '''You are creating knowls (short definition/theorem cards) for a mathematics reference site.

For each slug below, generate a markdown file following these rules exactly.

---

## OUTPUT FORMAT

For each knowl, output:

**`slug-name.md`**
```markdown
---
title: "Display Title"
description: "One-line plain-text description (NO LaTeX)"
---

[Content here]
```

---

## CRITICAL RULES (MUST FOLLOW)

### 1. NO "Related" Sections
DO NOT include any of these at the end of a knowl:
- `## Related knowls`
- `## See also`
- `**Related knowls.**`
- Any list of "related" concepts

All cross-links must be woven naturally into the prose.

### 2. NO Knowl Shortcodes Inside Math
NEVER place `{{< knowl ... >}}` inside LaTeX math (`$...$` or `$$...$$`).

BAD: `Let $x \\in {{< knowl id="open-ball" text="B(a,r)" >}}$`
GOOD: `Let $x \\in B(a,r)$ be in the {{< knowl id="open-ball" text="open ball" >}}`

### 3. Cross-Section Links MUST Include `section`
When linking to a knowl in a DIFFERENT section, you MUST specify the section parameter.

Same section (no section param needed):
`{{< knowl id="subset" text="subset" >}}`

Different section (section param REQUIRED):
`{{< knowl id="ring" section="algebra-rings" text="ring" >}}`

### 4. Plain-Text Description
The `description` field in YAML must be plain text only. NO LaTeX.

### 5. Correct Shortcode Syntax
Use exactly double curly braces: `{{<` and `>}}`
- NOT `{<` (single brace)
- NOT `{{{<` (triple brace)

### 6. NO Proof Sketches
Do not include "Proof sketch" sections.

---

## CONTENT STRUCTURE

### For Definitions
```markdown
A **[term]** is [formal definition with LaTeX].

[1-2 sentences of context with cross-links to prerequisite concepts]

**Examples:**
- [Concrete example 1]
- [Concrete example 2]
```

### For Theorems/Axioms/Principles
```markdown
**[Name]:** [Precise statement with all hypotheses]

[1-2 sentences connecting to related concepts with cross-links]
```

---

## SECTION DIRECTORY REFERENCE

| Section | Content |
|---------|---------|
| `shared-foundations` | Set theory, logic, functions, relations |
| `linear-algebra` | Vector spaces, linear maps, matrices |
| `topology` | Topological spaces, metric spaces, compactness |
| `measure-theory` | Sigma-algebras, measures, Lebesgue |
| `real-analysis` | Real numbers, sequences, series, calculus |
| `algebra-groups` | Groups, subgroups, actions |
| `algebra-rings` | Rings, ideals, fields |

---

## AVAILABLE SLUGS

**Current section ({section_name}) - no section param needed:**
{current_slugs}

{other_sections}

---

## YOUR BATCH

Generate knowls for these slugs:
{batch_slugs}

---

## VERIFICATION BEFORE OUTPUT

For each knowl, verify:
- [ ] No "Related" section at the end
- [ ] No shortcodes inside `$...$` or `$$...$$`
- [ ] All cross-section links have `section` param
- [ ] `description` is plain text
- [ ] Shortcodes use `{{<` and `>}}`
- [ ] No proof sketch sections
'''


def parse_proposed_reorg():
    """Parse proposed-analysis-reorg.md to extract slugs per section."""
    with open(PROPOSED_REORG) as f:
        content = f.read()

    sections = {}
    current_section = None
    current_slugs = []

    for line in content.split('\n'):
        stripped = line.strip()

        # Section header like "shared-foundations/ (50)" (no leading whitespace)
        if not line.startswith(' ') and re.match(r'^([a-z-]+)/\s*\(\d+\)', stripped):
            if current_section:
                sections[current_section] = current_slugs
            current_section = re.match(r'^([a-z-]+)/', stripped).group(1)
            current_slugs = []
            continue

        # Skip subsection headers like "  definitions/ (44)"
        if re.match(r'^  [a-z-]+/\s*\(\d+\)', line):
            continue

        # Slug line (indented with 4 spaces, just a slug name)
        if line.startswith('    ') and re.match(r'^[a-z][a-z0-9-]*$', stripped) and current_section:
            current_slugs.append(stripped)

    # Don't forget last section
    if current_section:
        sections[current_section] = current_slugs

    return sections


def create_batches(slugs, batch_size=BATCH_SIZE):
    """Split slugs into batches."""
    return [slugs[i:i+batch_size] for i in range(0, len(slugs), batch_size)]


def create_batch_prompt(section_name, all_section_slugs, batch_slugs, other_sections_info=""):
    """Create a batch prompt from the template."""
    prompt = PROMPT_TEMPLATE
    prompt = prompt.replace("{section_name}", section_name)
    prompt = prompt.replace("{current_slugs}", ", ".join(all_section_slugs))
    prompt = prompt.replace("{batch_slugs}", "\n".join(f"- {s}" for s in batch_slugs))
    prompt = prompt.replace("{other_sections}", other_sections_info)
    return prompt


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 prepare-batches.py <section-name>")
        print("Available sections: shared-foundations, linear-algebra, topology, measure-theory, real-analysis")
        sys.exit(1)

    section_name = sys.argv[1]
    sections = parse_proposed_reorg()

    if section_name not in sections:
        print(f"Error: Section '{section_name}' not found in proposed-analysis-reorg.md")
        print(f"Available: {', '.join(sections.keys())}")
        sys.exit(1)

    slugs = sections[section_name]
    batches = create_batches(slugs)

    # Build other sections info for cross-linking
    other_sections_info = ""
    for other_section, other_slugs in sections.items():
        if other_section != section_name and other_slugs:
            other_sections_info += f"\n**{other_section}:** {', '.join(other_slugs[:30])}"
            if len(other_slugs) > 30:
                other_sections_info += f" ... ({len(other_slugs)} total)"
            other_sections_info += "\n"

    # Create batch directory
    section_batch_dir = BATCH_DIR / section_name
    section_batch_dir.mkdir(parents=True, exist_ok=True)

    # Write batch files
    batch_files = []
    for i, batch in enumerate(batches, 1):
        prompt = create_batch_prompt(section_name, slugs, batch, other_sections_info)
        batch_file = section_batch_dir / f"batch{i}.md"
        with open(batch_file, 'w') as f:
            f.write(prompt)
        batch_files.append(batch_file)
        print(f"Created {batch_file} ({len(batch)} slugs)")

    print(f"\nTotal: {len(slugs)} slugs in {len(batches)} batches")
    print(f"\nTo run Oracle:")
    pf_args = " \\\n  ".join(f"-pf {f}" for f in batch_files)
    print(f"~/.oracle/oracle-parallel.sh \\\n  {pf_args} \\\n  --sessions-file tmp/batches/{section_name}/sessions.txt")


if __name__ == "__main__":
    main()
