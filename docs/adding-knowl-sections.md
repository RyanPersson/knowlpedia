# Adding Knowl Sections

This guide walks through the complete process of adding a new batch of generated knowls to the site.

---

## Overview

When adding a new knowl section (or batch of knowls to an existing section), you need to update:

1. **Content files** — The actual `.md` knowl files in `content/<section>/`
2. **Section index** — The `_index.md` file that lists all knowls in the section
3. **Navigation menu** — The `hugo.toml` config if adding a new section
4. **Inventory docs** — The `docs/knowl-modules/current-inventory.md` file

---

## Step 1: Add Content Files

Place the generated `.md` files in the appropriate section directory:

```
content/<section-name>/
├── _index.md           # Section index (update in step 2)
├── knowl-one.md
├── knowl-two.md
└── ...
```

### File Format

Each knowl file should have this structure:

```markdown
---
title: "Human-readable title"
description: "Brief description for SEO/previews"
---

**Term being defined:** Definition text with inline math $x^2$ and display math:
$$
\int_a^b f(x)\,dx
$$

Reference other knowls: {{</* knowl id="other-knowl" text="link text" */>}}
```

### Important LaTeX Guidelines

**Avoid these patterns that break KaTeX rendering:**

```markdown
# BAD - equals sign alone on a line inside math block
$$
x + y
=
z
$$

# GOOD - keep equation on single line or use aligned environment
$$
x + y = z
$$
```

**Avoid math inside knowl text parameters:**

```markdown
# BAD - math in knowl text breaks rendering
{{</* knowl id="group" text="$GL(n)$" */>}}

# GOOD - use plain text, put math outside
$GL(n)$ (see {{</* knowl id="general-linear-group" text="general linear group" */>}})
```

---

## Step 2: Update Section Index

Edit `content/<section>/_index.md` to include the new knowls.

### Index Structure

```markdown
---
title: "Section Title"
description: "Section description"
---

## Category One

- {{</* knowl id="knowl-id" text="Display Text" */>}}
- {{</* knowl id="another-knowl" text="Another Knowl" */>}}

## Category Two

- {{</* knowl id="theorem-name" text="Theorem Name" */>}}

---

## Uncategorized

- {{</* knowl id="new-knowl" text="New Knowl Title" */>}}
```

### Quick Method: Add to Uncategorized

If you don't want to categorize immediately, add new knowls to an `## Uncategorized` section at the end:

```markdown
---

## Uncategorized

- {{</* knowl id="new-knowl-1" text="Title from frontmatter" */>}}
- {{</* knowl id="new-knowl-2" text="Title from frontmatter" */>}}
```

### Verifying Index Completeness

Run this to find orphaned knowls (files not in index) or invalid references (index entries without files):

```bash
# From blog root
python3 scripts/validate-knowls.py
```

Or manually check:

```bash
# List files in section
ls content/<section>/*.md | grep -v _index

# Compare with knowl ids in index
grep 'knowl id=' content/<section>/_index.md
```

---

## Step 3: Update Navigation Menu (New Sections Only)

If adding a **new section**, edit `hugo.toml` to add it to the navigation menu.

### Menu Structure

The menu uses parent-child relationships for dropdowns:

```toml
# Parent (dropdown header)
[[menu.main]]
  identifier = "algebra"      # Unique ID
  name = "Algebra"            # Display name
  weight = 30                 # Order (lower = earlier)

# Child (dropdown item)
[[menu.main]]
  identifier = "algebra-groups"
  name = "Groups"
  url = "/algebra-groups/"
  parent = "algebra"          # Must match parent's identifier
  weight = 1                  # Order within dropdown
```

### Current Dropdown Structure

| Dropdown | Sections |
|----------|----------|
| Foundations | shared-foundations, linear-algebra |
| Analysis | real-analysis, topology, measure-theory, convex-analysis |
| Algebra | algebra-groups, algebra-rings, algebra-modules, algebra-fields-galois, algebra-commutative, algebra-homological, algebra-representation-theory, algebra-category-theory |
| Misc | lie-groups, fiber-bundles, langlands-letter |

---

## Step 4: Update Inventory Documentation

Edit `docs/knowl-modules/current-inventory.md` to reflect the new content.

### Format

```markdown
### `section-name` (N knowls)

**Definitions:** (count)
- Term name → `file-name.md`
- Another term → `another-file.md`

**Theorems:** (count)
- Theorem name → `theorem-file.md`
```

### Updating Counts

Update the knowl count in the section header and the README tables.

---

## Step 5: Verify Everything Works

1. **Check Hugo builds without errors:**
   ```bash
   hugo server
   ```

2. **Test knowl rendering:**
   - Navigate to the section index page
   - Click several knowls to verify they expand correctly
   - Check that math renders properly (not showing raw LaTeX)

3. **Check for broken cross-references:**
   ```bash
   python3 scripts/validate-knowls.py
   ```

---

## Checklist

- [ ] Content files added to `content/<section>/`
- [ ] Each file has proper frontmatter (title, description)
- [ ] No problematic LaTeX patterns (isolated `=` on lines, math in knowl text)
- [ ] Section `_index.md` updated with all new knowls
- [ ] Navigation menu updated (if new section)
- [ ] `docs/knowl-modules/current-inventory.md` updated
- [ ] `docs/knowl-modules/README.md` counts updated (if significant changes)
- [ ] Hugo builds without errors
- [ ] Knowls render correctly in browser

---

## Common Issues

### "HAHAHUGOSHORTCODE" Error

Math inside knowl text parameter. Move math outside the shortcode.

### Raw LaTeX Showing Instead of Rendered Math

Usually caused by:
- `=`, `+`, or `-` alone on a line inside `$$...$$` blocks
- Missing KaTeX CSS (check browser dev tools)

### Knowl Not Found (404)

- Check that the file exists with the exact ID (filename without `.md`)
- Check for typos in the knowl shortcode `id` parameter
- Verify the section parameter if referencing cross-section

### Circular References

Knowls can reference each other, but avoid A→B→A chains that create infinite expansion loops. The JS handles this gracefully but it's confusing UX.
