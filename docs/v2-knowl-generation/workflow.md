# Knowl Generation Workflow v2

Complete step-by-step process for generating knowls using the improved workflow.

## Prerequisites

1. Familiarity with `anti-patterns.md` (read first!)
2. Oracle CLI installed and configured (for GPT-5.2 automation)
3. Chrome running with remote debugging: `~/.oracle/start-chrome.sh`
4. Hugo installed for local testing

## Overview

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. ENUMERATE                                                     │
│    Input: Subject + Level                                        │
│    Output: Categorized list of all items                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│ 2. PREPARE                                                       │
│    Input: Item list                                              │
│    Output: Slug manifest + batch prompts                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│ 3. GENERATE (Parallel)                                           │
│    Input: Batch prompts (via Oracle)                             │
│    Output: Raw knowl files                                       │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│ 4. PARSE & FIX                                                   │
│    Input: Oracle output logs                                     │
│    Output: Clean knowl markdown files                            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│ 5. VALIDATE                                                      │
│    Input: Generated files                                        │
│    Output: Issue report                                          │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│ 6. REVIEW & COMMIT                                               │
│    Input: Validated files                                        │
│    Output: Committed to content submodule                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step 1: Enumerate

Use `docs/knowl-generation/step-1-enumeration.md` to generate a complete list.

**Input:** Subject, level, and scope
```
Subject: Commutative Algebra
Level: 400-level (undergraduate)
Scope: Through Noether normalization, excluding schemes
```

**Output:** Categorized list
```
## Definitions
- Ring
- Ideal
- Prime ideal
- Maximal ideal
...

## Theorems
- Hilbert Basis Theorem
- Nullstellensatz
...
```

---

## Step 2: Prepare Batches

### 2.1 Create Slug Manifest

Convert each item to a slug:
- Lowercase
- Spaces → hyphens
- Remove apostrophes, parentheses
- Examples: "Hilbert's Basis Theorem" → `hilberts-basis-theorem`

### 2.2 Gather Prerequisite Slugs

Check the decomposition.md for *Depends on* line. Collect all slugs from prerequisite sections:

```python
import os

prereq_sections = {
    "shared-foundations": [],
    "linear-algebra": [],
    "algebra-groups": [],
    "algebra-rings": [],
    # Add as needed
}

for section, slugs_list in prereq_sections.items():
    dir_path = f"content/{section}"
    if os.path.exists(dir_path):
        prereq_sections[section] = [
            f[:-3] for f in os.listdir(dir_path)
            if f.endswith('.md') and f != '_index.md'
        ]
```

### 2.3 Create Batch Prompts

Use `prompt-template.md` as the base. Fill in:
- `{SECTION_NAME}` - Target section
- `{CURRENT_SLUGS}` - All slugs for this section
- `{BATCH_SLUGS}` - This batch's 20-25 slugs
- Prerequisite section slugs

**Batch sizing:**
- 20-25 slugs per batch (smaller = more reliable)
- Use 6 parallel batches (fewer only if there aren't enough slugs to fill 6)

```python
batch_size = 20
batches = [slugs[i:i+batch_size] for i in range(0, len(slugs), batch_size)]

for i, batch in enumerate(batches, 1):
    prompt = prompt_template.format(
        SECTION_NAME=section_name,
        CURRENT_SLUGS=", ".join(all_slugs),
        BATCH_SLUGS="\n".join(f"- {s}" for s in batch),
        # ... other sections
    )
    with open(f"tmp/batch{i}.md", 'w') as f:
        f.write(prompt)
```

---

## Step 3: Generate (Oracle Parallel)

### 3.1 Run Oracle

```bash
~/.oracle/oracle-parallel.sh \
  -pf tmp/batch1.md \
  -pf tmp/batch2.md \
  -pf tmp/batch3.md \
  -pf tmp/batch4.md \
  -pf tmp/batch5.md \
  -pf tmp/batch6.md \
  --sessions-file tmp/sessions.txt
```

**Runtime:** 20-40 minutes per batch (running in parallel)

### 3.2 Monitor Progress

```bash
# Check if complete
cat tmp/sessions.txt

# View a session's output
cat ~/.oracle/sessions/SESSION_NAME/output.log
```

---

## Step 4: Parse & Fix

### 4.1 Extract Knowls from Output

```python
import re
import os

output_dir = f"content/{section_name}"
os.makedirs(output_dir, exist_ok=True)

# Read sessions file
with open("tmp/sessions.txt") as f:
    sessions = [s.strip() for s in f.readlines()]

# Patterns for GPT output format variations
patterns = [
    r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```',
    r'## `([a-z0-9-]+\.md)`\s*\n+```markdown\n(---\n.*?)\n```',
]

created = []
for session in sessions:
    path = os.path.expanduser(f"~/.oracle/sessions/{session}/output.log")
    with open(path) as f:
        content = f.read()

    for pattern in patterns:
        for filename, body in re.findall(pattern, content, re.DOTALL):
            body = fix_content(body)  # See 4.2
            with open(os.path.join(output_dir, filename), 'w') as f:
                f.write(body + '\n')
            created.append(filename[:-3])

print(f"Created {len(created)} files")
```

### 4.2 Fix Common Issues

```python
def fix_content(body):
    # CRITICAL: GPT almost always outputs triple braces despite instructions.
    # This fix is REQUIRED for every batch.
    body = re.sub(r'\{\{\{<', r'{{<', body)
    body = re.sub(r'>\}\}\}', r'>}}', body)

    # Fix single braces
    body = re.sub(r'\{< knowl', r'{{< knowl', body)
    body = re.sub(r' >\}', r' >}}', body)

    # Remove .md from knowl ids
    body = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', body)

    # Clean LaTeX from description
    def clean_desc(match):
        desc = match.group(1)
        desc = re.sub(r'\\[a-zA-Z]+', '', desc)
        desc = re.sub(r'\$[^$]*\$', '', desc)
        return f'description: "{desc.strip()}"'
    body = re.sub(r'^description:\s*"([^"]*)"', clean_desc, body, flags=re.MULTILINE)

    return body
```

### 4.3 Create _index.md

```python
knowl_files = sorted([f[:-3] for f in os.listdir(output_dir)
                      if f.endswith('.md') and f != '_index.md'])

index = f'''---
title: "{section_title}"
description: "{section_description}"
build:
  list: local
---

{section_intro}

## Definitions

'''

for slug in knowl_files:
    title = slug.replace("-", " ").title()
    index += f'- {{{{< knowl id="{slug}" text="{title}" >}}}}\n'

with open(os.path.join(output_dir, '_index.md'), 'w') as f:
    f.write(index)
```

---

## Step 5: Validate

### 5.1 Check for Broken Links

```bash
python3 scripts/validate-knowls.py
```

Fix any broken references by either:
- Adding missing `section` parameter
- Creating missing knowls
- Removing references to non-existent concepts

### 5.2 Check for Anti-Patterns

```bash
# Related sections
grep -r "Related knowls" content/SECTION/
grep -r "## Related" content/SECTION/

# Knowls in math
grep -r '\$.*{{< knowl' content/SECTION/
grep -r '={{< knowl' content/SECTION/

# Proof sketches (if removing for consistency)
grep -ri "proof sketch" content/SECTION/
```

### 5.3 Test Build

```bash
hugo server
# Navigate to the new section, verify rendering
```

---

## Step 6: Review & Commit

### 6.1 Manual Review

Spot-check 5-10 knowls for:
- Mathematical accuracy
- Natural prose flow
- Correct cross-links
- Proper rendering

### 6.2 Commit to Content Submodule

```bash
cd content/
git checkout -b add-SECTION-knowls
git add SECTION/
git commit -m "Add SECTION knowls (N files)"
git checkout main
git merge add-SECTION-knowls
git push

cd ..
git add content
git commit -m "Update content submodule: add SECTION knowls"
# User pushes manually
```

---

## Quick Reference

### Batch Prompt Checklist
- [ ] Section name specified
- [ ] Current section slugs listed
- [ ] Prerequisite sections included with slugs
- [ ] Batch size ≤ 25 slugs
- [ ] Anti-pattern rules included in prompt

### Post-Generation Checklist
- [ ] `validate-knowls.py` passes
- [ ] No "Related" sections (`grep -r "Related"`)
- [ ] No knowls in math (`grep -r '\$.*{{< knowl'`)
- [ ] Hugo builds without errors
- [ ] Spot-check renders correctly
- [ ] _index.md created with proper structure
