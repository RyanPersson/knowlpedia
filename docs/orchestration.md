# Knowl Generation Orchestration Guide

This document explains how to automate the generation of knowl files for new content sections using GPT-5.2 Pro via the Oracle browser automation tool.

## Prerequisites

1. **Oracle CLI** must be installed and configured
2. **Chrome** must be running with remote debugging: `~/.oracle/start-chrome.sh`
3. Read the Oracle documentation: `~/docs/oracle-parallel-tasks.md`

## Critical Rules

### 1. Avoid Manual Approval Commands

**NEVER** use individual `cat > file << 'EOF'` commands or individual `Write` tool calls for creating multiple files. These require manual approval for each file.

**ALWAYS** use Python scripts to batch create files:

```python
# GOOD - Single script creates all files
cat > /tmp/create-files.py << 'PYSCRIPT'
import os
for slug, content in files.items():
    with open(f"/path/{slug}.md", 'w') as f:
        f.write(content)
PYSCRIPT
python3 /tmp/create-files.py
```

### 2. Remember to Create Layouts

When adding a new content section (e.g., `content/algebra-foo/`), you **MUST** also create corresponding layouts:

```
layouts/algebra-foo/
├── single.html   # Template for individual knowl pages
└── list.html     # Template for section index page
```

Copy from an existing section and update the back-link text:
```bash
mkdir -p layouts/NEW-SECTION
cp layouts/algebra-modules/single.html layouts/NEW-SECTION/
cp layouts/algebra-modules/list.html layouts/NEW-SECTION/
# Then edit single.html to change the back-link text
```

### 3. Update decomposition.md with Checkmarks

After creating knowl files, add checkmarks to `docs/knowl-modules/decomposition.md`:
- Pattern: `- Description → \`slug.md\`` becomes `✓ - Description → \`slug.md\``

### 4. Use Correct Shortcode Syntax in _index.md

The `_index.md` file for each section must use **proper knowl shortcode syntax**:

**CORRECT** (renders as clickable knowl):
```markdown
- {{< knowl id="field-extension" text="Field extension" >}}
```

**WRONG** (renders as literal text):
```markdown
{{< knowl id="field-extension" >}}
```

The `text` parameter is **required** for the shortcode to render properly on index pages.

Also structure the _index.md with:
- Markdown headers (`## Definitions`, `## Theorems`, etc.)
- Bullet points for each knowl
- Logical groupings with subheaders

See `content/algebra-modules/_index.md` for a good example.

### 5. Cross-Section Links MUST Include `section` Parameter

**CRITICAL**: When linking to a knowl in a *different* content section, you MUST specify the `section` parameter. The shortcode defaults to the current page's section.

**Same section** (section parameter optional):
```markdown
{{< knowl id="field-extension" text="field extension" >}}
```

**Different section** (section parameter REQUIRED):
```markdown
{{< knowl id="vector-space" section="shared-linear-algebra" text="vector space" >}}
{{< knowl id="ring" section="algebra-rings" text="ring" >}}
{{< knowl id="group" section="algebra-groups" text="group" >}}
```

**Section directory mapping:**
- `shared-foundations` - basic set theory, logic, functions
- `shared-linear-algebra` - vector spaces, linear maps, matrices, eigenvalues
- `algebra-groups` - groups, subgroups, homomorphisms, actions
- `algebra-rings` - rings, ideals, fields, polynomials
- `algebra-modules` - modules, exact sequences, tensor products
- `algebra-fields-galois` - field extensions, Galois theory

The batch prompt MUST tell GPT which section each prerequisite slug belongs to so it can generate correct cross-links.

## Complete Workflow

### Step 1: Extract Slugs from decomposition.md

```python
import re

with open("docs/knowl-modules/decomposition.md", 'r') as f:
    decomp = f.read()

# Find the section
section_match = re.search(r'### `SECTION-NAME`.*?(?=\n---\n|\n### `)', decomp, re.DOTALL)
section = section_match.group(0)

# Extract slugs
slug_pattern = r'→ `([a-z0-9-]+\.md)`'
slugs = [s[:-3] for s in re.findall(slug_pattern, section)]
print(f"Found {len(slugs)} slugs")
```

### Step 2: Gather Prerequisite Slugs WITH Section Info

The *Depends on* line in decomposition.md tells you which modules to include. **You must track which section each slug belongs to.**

```python
# Build slug -> section mapping for all prerequisites
prereq_sections = {
    "shared-foundations": [],
    "shared-linear-algebra": [],
    "algebra-groups": [],
    "algebra-rings": [],
    "algebra-modules": [],
    # Add more as needed
}

for section, slugs_list in prereq_sections.items():
    dir_path = f"content/{section}"
    if os.path.exists(dir_path):
        prereq_sections[section] = [f[:-3] for f in os.listdir(dir_path)
                                     if f.endswith('.md') and f != '_index.md']
```

### Step 3: Create Batch Prompt Files (with section info)

Split slugs into batches of **20-25** (not 30 - smaller batches are faster and more reliable).

**CRITICAL**: The prompt must tell GPT which section each prerequisite belongs to, so it generates correct `section="..."` parameters.

```python
batch_size = 20  # Smaller batches = faster completion
batches = [slugs[i:i+batch_size] for i in range(0, len(slugs), batch_size)]

# Format prereqs with section info
prereqs_formatted = ""
for section, section_slugs in prereq_sections.items():
    if section_slugs:
        prereqs_formatted += f"\n**{section}**: {', '.join(section_slugs)}"

prompt_template = '''You are creating knowls (short definition/theorem cards) for a math blog.

For each slug below, generate a markdown file with:
1. YAML front matter with `title` and `description`
2. A clear statement of the definition/theorem
3. Cross-links using Hugo shortcode (see syntax below)
4. 2-3 concrete examples where applicable

**CROSS-LINK SYNTAX:**
- For slugs in the CURRENT module: `{{</* knowl id="slug" text="display" */>}}`
- For slugs in OTHER modules: `{{</* knowl id="slug" section="section-name" text="display" */>}}`

**Available slugs by section (use section parameter when linking):**
{prereqs}

**Current module ({current_section}) slugs (no section parameter needed):**
{current}

**Generate knowls for these slugs:**
{batch}

Output format for each:
**`slug.md`**
```markdown
---
title: "Title"
description: "One-line description"
---

Content with cross-links...
```
'''

for i, batch in enumerate(batches, 1):
    content = prompt_template.format(
        prereqs=', '.join(prereq_slugs),
        current=', '.join(slugs),
        batch='\n'.join(f'- {s}' for s in batch)
    )
    with open(f"/tmp/batch{i}.md", 'w') as f:
        f.write(content)
```

### Step 4: Run Oracle Parallel

```bash
~/.oracle/oracle-parallel.sh \
  -pf /tmp/batch1.md \
  -pf /tmp/batch2.md \
  -pf /tmp/batch3.md
```

This runs up to 6 batches in parallel. Each batch takes ~10-18 minutes.

**Session outputs are saved to:** `~/.oracle/sessions/*/output.log`

The session names are auto-generated from the prompt's first words. Find them with:
```bash
ls -lt ~/.oracle/sessions/ | head -10
```

### Step 5: Parse Outputs and Create Files

```python
import re
import os

output_dir = "content/NEW-SECTION"
os.makedirs(output_dir, exist_ok=True)

session_files = [
    "~/.oracle/sessions/SESSION-NAME-1/output.log",
    "~/.oracle/sessions/SESSION-NAME-2/output.log",
]

pattern = r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```'

for session_file in session_files:
    with open(os.path.expanduser(session_file), 'r') as f:
        content = f.read()
    
    matches = re.findall(pattern, content, re.DOTALL)
    for filename, body in matches:
        # Fix malformed shortcodes
        body = re.sub(r'\{<\/\*', r'{{</*', body)
        body = re.sub(r'\*\/>}', r'*/>}}', body)
        body = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', body)
        
        with open(os.path.join(output_dir, filename), 'w') as f:
            f.write(body + '\n')
```

### Step 6: Create _index.md (Structured with text parameter)

The _index.md needs proper structure with headers, bullet points, and the `text` parameter.

**Option A: Parse titles from decomposition.md (recommended)**

```python
import re, os

# Read decomposition.md to get slug -> title mappings
with open("docs/knowl-modules/decomposition.md", 'r') as f:
    decomp = f.read()

# Extract section
section_match = re.search(r'### `SECTION-NAME`.*?(?=\n---\n|\n### `)', decomp, re.DOTALL)
section = section_match.group(0)

# Build slug -> title map
slug_to_title = {}
for match in re.finditer(r'- (?:✓ )?([^→]+)→ `([a-z0-9-]+)\.md`', section):
    slug_to_title[match.group(2)] = match.group(1).strip()

# Get created knowl files
knowl_files = sorted([f[:-3] for f in os.listdir(output_dir)
                      if f.endswith('.md') and f != '_index.md'])

# Build structured index - group by category from decomposition.md
# Categories are listed in order: Definitions, Theorems, Lemmas, Propositions, Corollaries
index = '''---
title: "Section Title"
description: "Section description."
build:
  list: local
---

Introductory text.

## Definitions

'''

for slug in knowl_files:
    title = slug_to_title.get(slug, slug.replace("-", " ").title())
    index += f'- {{{{< knowl id="{slug}" text="{title}" >}}}}\n'

# Add more sections as needed: ## Theorems, ## Lemmas, etc.

with open(os.path.join(output_dir, '_index.md'), 'w') as f:
    f.write(index)
```

**Key requirements:**
1. Use `text` parameter: `{{< knowl id="slug" text="Display Title" >}}`
2. Use bullet points: `- {{< knowl ... >}}`
3. Add section headers: `## Definitions`, `## Theorems`, etc.
4. See `content/algebra-modules/_index.md` for full example

### Step 7: Create Layouts

```bash
mkdir -p layouts/NEW-SECTION

# single.html - copy and modify back-link
cat > layouts/NEW-SECTION/single.html << 'EOF'
{{ define "main" }}
<article class="post-single glossary-entry">
  <header class="post-header">
    {{ partial "breadcrumbs.html" . }}
    <h1 class="post-title">{{ .Title }}</h1>
    {{- if .Description }}
    <div class="post-description">{{ .Description }}</div>
    {{- end }}
  </header>

  <div class="knowl-content" data-knowl-id="{{ .File.ContentBaseName }}">
    <div class="knowl-header">
      <strong>{{ .Title }}</strong>
      <button class="knowl-close" aria-label="Close">&times;</button>
    </div>
    <div class="knowl-body">{{ .Content }}</div>
    <div class="knowl-footer">
      <button class="knowl-close" aria-label="Close">&times;</button>
    </div>
  </div>

  <footer class="post-footer">
    <p><a href="/NEW-SECTION/">← Back to Section Name</a></p>
  </footer>
</article>
{{ end }}
EOF

# list.html
cat > layouts/NEW-SECTION/list.html << 'EOF'
{{ define "main" }}
<article class="post-single">
  <header class="post-header">
    <h1 class="post-title">{{ .Title }}</h1>
    {{- if .Description }}
    <div class="post-description">{{ .Description }}</div>
    {{- end }}
  </header>
  <div class="post-content">{{ .Content }}</div>
</article>
{{ end }}
EOF
```

### Step 8: Add Checkmarks to decomposition.md

```python
decomp_path = "docs/knowl-modules/decomposition.md"
with open(decomp_path, 'r') as f:
    decomp = f.read()

for slug in knowl_files:
    pattern = rf'^(- [^→]+→ )`{re.escape(slug)}\.md`'
    replacement = rf'✓ \1`{slug}.md`'
    decomp = re.sub(pattern, replacement, decomp, flags=re.MULTILINE)

with open(decomp_path, 'w') as f:
    f.write(decomp)
```

### Step 9: Verify

```bash
# Count files (should be N knowls + 1 _index.md)
ls content/NEW-SECTION/ | wc -l

# Count checkmarks
grep -c "^✓ -" docs/knowl-modules/decomposition.md

# Test build
hugo server
```

## All-in-One Python Script Template

For convenience, here's a complete script that does steps 5-8 after oracle completes:

```python
#!/usr/bin/env python3
"""
Run after oracle-parallel completes.
Usage: python3 process-knowls.py SECTION-NAME SESSION1 SESSION2 ...
"""
import re, os, sys

section = sys.argv[1]  # e.g., "algebra-fields-galois"
sessions = sys.argv[2:]  # e.g., "you-are-creating-knowls-short" ...

output_dir = f"content/{section}"
os.makedirs(output_dir, exist_ok=True)

# Parse all sessions
pattern = r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```'
created = []

for session in sessions:
    path = os.path.expanduser(f"~/.oracle/sessions/{session}/output.log")
    with open(path, 'r') as f:
        content = f.read()
    for filename, body in re.findall(pattern, content, re.DOTALL):
        body = re.sub(r'\{<\/\*', r'{{</*', body)
        body = re.sub(r'\*\/>}', r'*/>}}', body)
        body = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', body)
        with open(os.path.join(output_dir, filename), 'w') as f:
            f.write(body + '\n')
        created.append(filename[:-3])

print(f"Created {len(created)} knowl files")

# Create _index.md
knowl_files = sorted(set(created))
index = f'''---
title: "EDIT: Section Title"
description: "EDIT: Description"
build:
  list: local
---

EDIT: Intro text.

'''
for slug in knowl_files:
    index += f'{{{{</* knowl id="{slug}" */>}}}}\n'
with open(os.path.join(output_dir, '_index.md'), 'w') as f:
    f.write(index)

# Update decomposition.md
decomp_path = "docs/knowl-modules/decomposition.md"
with open(decomp_path, 'r') as f:
    decomp = f.read()
updated = 0
for slug in knowl_files:
    pattern = rf'^(- [^→]+→ )`{re.escape(slug)}\.md`'
    new, count = re.subn(pattern, rf'✓ \1`{slug}.md`', decomp, flags=re.MULTILINE)
    if count:
        decomp = new
        updated += count
with open(decomp_path, 'w') as f:
    f.write(decomp)
print(f"Added {updated} checkmarks to decomposition.md")
print(f"\n⚠️  Don't forget to create layouts/{section}/ !")
```

## Checklist for New Section

- [ ] Extract slugs from decomposition.md
- [ ] Identify prerequisite modules from *Depends on* line
- [ ] Create batch prompt files (20-25 slugs each)
- [ ] Run oracle-parallel with all batches
- [ ] Parse outputs and create knowl files
- [ ] Create `_index.md` with proper title/description
- [ ] Create `layouts/SECTION/single.html` and `list.html`
- [ ] Add checkmarks to decomposition.md
- [ ] Verify file counts match expected
- [ ] Test with `hugo server`

## Reference Files

- Oracle docs: `~/docs/oracle-parallel-tasks.md`
- Knowl generation workflow: `docs/knowl-generation/README.md`
- Module decomposition: `docs/knowl-modules/decomposition.md`
- Example layouts: `layouts/algebra-modules/`
