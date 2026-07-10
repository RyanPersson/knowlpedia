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
{{< knowl id="vector-space" section="linear-algebra" text="vector space" >}}
{{< knowl id="ring" section="algebra-rings" text="ring" >}}
{{< knowl id="group" section="algebra-groups" text="group" >}}
```

**Section directory mapping:**
- `shared-foundations` - basic set theory, logic, functions
- `linear-algebra` - vector spaces, linear maps, matrices, eigenvalues
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
    "linear-algebra": [],
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

**Batch sizing rules:**
- **Max 20 slugs per batch** (smaller = faster, more reliable)
- **Use 6 parallel batches** (fewer only if there aren't enough slugs to fill 6)
- If a module has >120 slugs, run additional batches after the first 6 complete
- **Only one Claude Code agent should run oracle batches at a time** (oracle doesn't support concurrent batch sets)

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
- For slugs in the CURRENT module: `{{< knowl id="slug" text="display" >}}`
- For slugs in OTHER modules: `{{< knowl id="slug" section="section-name" text="display" >}}`

**CRITICAL RULES:**
- DO NOT include a "Related" or "Related knowls" section at the end
- DO NOT put knowl shortcodes inside LaTeX math blocks (keep shortcodes in prose only)
- All cross-links must be woven naturally into the prose

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

Content with natural cross-links woven into prose...
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

**Config file mode (recommended for automation):**

The prepare-batches.py script creates an `oracle-config.txt` file. Using config mode allows the same command to be run repeatedly without manual approval:

```bash
~/.oracle/oracle-parallel.sh \
  --config /path/to/batches/oracle-config.txt \
  --sessions-file /path/to/batches/sessions.txt
```

**Legacy mode (explicit batch files):**

```bash
~/.oracle/oracle-parallel.sh \
  -pf /tmp/batch1.md \
  -pf /tmp/batch2.md \
  -pf /tmp/batch3.md \
  -pf /tmp/batch4.md \
  -pf /tmp/batch5.md \
  -pf /tmp/batch6.md \
  --sessions-file /tmp/sessions.txt
```

This runs 6 batches in parallel. **Each batch takes 20-40 minutes.**

**Session outputs are saved to:** `~/.oracle/sessions/*/output.log`

#### Session Name Discovery (Automatic)

The script now automatically tracks which sessions were created and outputs them:

```
=== Sessions created ===
you-are-creating-knowls-short-41
you-are-creating-knowls-short-42
...

SESSIONS:you-are-creating-knowls-short-41:you-are-creating-knowls-short-42:...
```

**Options for retrieving session names:**
1. **`--sessions-file /tmp/sessions.txt`** - Writes session names to file (one per line)
2. **Parse `SESSIONS:` line** - Always printed at end, colon-separated
3. **Manual:** `ls -lt ~/.oracle/sessions/ | head -10`

#### Monitoring Long-Running Tasks

Oracle tasks take 20-40 minutes. When using Claude Code's TaskOutput:
- **Set timeout to 600000ms (10 min max)** and poll multiple times
- **Alternative:** Run in background and manually check completion

```bash
# Check if sessions file exists (indicates completion)
while [ ! -f /tmp/sessions.txt ]; do sleep 60; done
cat /tmp/sessions.txt
```

### Step 5: Parse Outputs and Create Files

**IMPORTANT:** GPT output format varies. Use multiple regex patterns to catch all formats.

```python
import re
import os

output_dir = "content/NEW-SECTION"
os.makedirs(output_dir, exist_ok=True)

session_files = [
    "~/.oracle/sessions/SESSION-NAME-1/output.log",
    "~/.oracle/sessions/SESSION-NAME-2/output.log",
]

# Multiple patterns to handle format variations:
# Pattern 1: **`slug.md`** or **slug.md**
# Pattern 2: ## `slug.md` (alternative heading format)
patterns = [
    r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```',
    r'## `([a-z0-9-]+\.md)`\s*\n+```markdown\n(---\n.*?)\n```',
]

def fix_content(body):
    """Fix common GPT output issues."""
    # Fix triple braces to double braces
    body = re.sub(r'\{\{\{<', r'{{<', body)
    body = re.sub(r'>\}\}\}', r'>}}', body)
    # Fix malformed shortcodes (GPT sometimes outputs {< instead of {{<)
    body = re.sub(r'\{< knowl', r'{{< knowl', body)
    body = re.sub(r' >\}', r' >}}', body)
    body = re.sub(r'\{<\/\*', r'{{</*', body)
    body = re.sub(r'\*\/>}}', r'*/>}}', body)
    # Remove .md from knowl id references
    body = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', body)
    # Fix escaped asterisks in LaTeX
    body = re.sub(r'\\\*', r'*', body)
    # Clean LaTeX from YAML description (causes Hugo parse errors)
    def clean_desc(match):
        desc = match.group(1)
        desc = re.sub(r'\\\\+[a-zA-Z]*', '', desc)
        desc = re.sub(r'\\[a-zA-Z]+', '', desc)
        desc = re.sub(r'\\[^a-zA-Z]', '', desc)
        desc = re.sub(r'\s+', ' ', desc).strip()
        return f'description: "{desc}"'
    body = re.sub(r'^description:\s*"([^"]*)"', clean_desc, body, flags=re.MULTILINE)
    return body

created = []
for session_file in session_files:
    with open(os.path.expanduser(session_file), 'r') as f:
        content = f.read()

    for pattern in patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        for filename, body in matches:
            body = fix_content(body)
            with open(os.path.join(output_dir, filename), 'w') as f:
                f.write(body + '\n')
            created.append(filename)

print(f"Created {len(created)} files")
```

**Verify file count matches expected slugs.** If count is low, check session logs for format variations.


### Step 5.5: Fix Common Issues (REQUIRED)

**CRITICAL:** GPT almost always outputs triple braces `{{{<` despite instructions. Run the fix script after every batch:

```bash
python3 scripts/fix-knowls.py content/NEW-SECTION/
```

This fixes:
- Triple braces `{{{<` → `{{<`
- Single braces `{<` → `{{<`
- `.md` in knowl ids
- LaTeX in YAML descriptions

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
Usage: python3 process-knowls.py SECTION-NAME [SESSION1 SESSION2 ...]
       python3 process-knowls.py SECTION-NAME --sessions-file /tmp/sessions.txt
"""
import re, os, sys

section = sys.argv[1]  # e.g., "algebra-fields-galois"

# Get sessions from file or command line
if '--sessions-file' in sys.argv:
    idx = sys.argv.index('--sessions-file')
    with open(sys.argv[idx + 1], 'r') as f:
        sessions = [s.strip() for s in f.readlines() if s.strip()]
else:
    sessions = sys.argv[2:]  # e.g., "you-are-creating-knowls-short-29" ...

output_dir = f"content/{section}"
os.makedirs(output_dir, exist_ok=True)

# Multiple patterns to handle GPT output format variations
patterns = [
    r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```',  # **`slug.md`**
    r'## `([a-z0-9-]+\.md)`\s*\n+```markdown\n(---\n.*?)\n```',          # ## `slug.md`
]

created = []

for session in sessions:
    path = os.path.expanduser(f"~/.oracle/sessions/{session}/output.log")
    with open(path, 'r') as f:
        content = f.read()

    for pattern in patterns:
        for filename, body in re.findall(pattern, content, re.DOTALL):
            if filename in [f + '.md' for f in created]:
                continue  # Skip duplicates

            # Fix malformed shortcodes
            body = re.sub(r'\{< knowl', r'{{< knowl', body)
            body = re.sub(r' >\}', r' >}}', body)
            body = re.sub(r'\{<\/\*', r'{{</*', body)
            body = re.sub(r'\*\/>}}', r'*/>}}', body)
            # Remove .md from knowl id references
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

## Advanced: Multi-Process Parallelization

The oracle-parallel.sh script has a default cap of 6 concurrent agents per process. However, **multiple oracle-parallel processes can run concurrently** with no rate limiting observed.

### Discovery

During stat-mech prerequisite generation (Jan 2026), we tested running 12 agents simultaneously:
- Phase 2: 4 agents (probability batches 7-10)
- Phase 3: 2 agents (convex-analysis)
- Phase 4: 2 agents (large-deviations)
- Phase 5: 1 agent (asymptotics)
- Phase 6: 1 agent (discrete-structures)
- Phase 7: 2 agents (quantum-foundations)

All 12 agents completed successfully with no throttling or failures.

### How to Run Multi-Process

Launch multiple oracle-parallel processes in background:

```bash
# Process 1: Phase 2 (4 agents)
~/.oracle/oracle-parallel.sh \
  -pf /tmp/phase2/batch7.md \
  -pf /tmp/phase2/batch8.md \
  -pf /tmp/phase2/batch9.md \
  -pf /tmp/phase2/batch10.md \
  --sessions-file /tmp/phase2/sessions.txt &

# Process 2: Phase 3 (2 agents)
~/.oracle/oracle-parallel.sh \
  -pf /tmp/phase3/batch1.md \
  -pf /tmp/phase3/batch2.md \
  --sessions-file /tmp/phase3/sessions.txt &

# ... more processes

wait  # Wait for all to complete
```

### Optimal Batch Sizing

Smaller batches (4-6 slugs) are more reliable than larger ones (20+ slugs):
- Faster completion per batch
- Lower risk of GPT losing context or producing malformed output
- Easier to parse and validate results

### Session Parsing Across Concurrent Processes

When running multiple processes concurrently, sessions from different phases may interleave. Use the `--sessions-file` option to track which sessions belong to which phase.

```python
# Parse sessions file and extract knowls
with open('/tmp/phase2/sessions.txt', 'r') as f:
    sessions = [s.strip() for s in f.readlines()]

for session in sessions:
    path = f"~/.oracle/sessions/{session}/output.log"
    # Parse and extract knowls...
```

### Common GPT Output Fixes

GPT frequently produces malformed shortcodes despite clear instructions. Always run these fixes:

```python
def fix_content(body):
    # Triple braces to double
    body = re.sub(r'\{\{\{<', r'{{<', body)
    body = re.sub(r'>\}\}\}', r'>}}', body)
    # Single brace to double (most common issue)
    body = re.sub(r'(?<!\{)\{< knowl', r'{{< knowl', body)
    body = re.sub(r' >\}(?!\})', r' >}}', body)
    # Wrong attribute name
    body = re.sub(r'knowl slug=', r'knowl id=', body)
    # Remove .md from ids
    body = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', body)
    return body
```

### Results Summary (Stat-Mech Prerequisites, Jan 2026)

- **108 knowls generated** across 7 phases in ~30 minutes
- **12 concurrent agents** with no rate limiting
- **5 new sections created**: probability, large-deviations, asymptotics, discrete-structures, quantum-foundations
- **Batch size**: 4-6 slugs per batch

## Reference Files

- Oracle docs: `~/docs/oracle-parallel-tasks.md`
- Knowl generation workflow: `docs/knowl-generation/README.md`
- Module decomposition: `docs/knowl-modules/decomposition.md`
- Example layouts: `layouts/algebra-modules/`
