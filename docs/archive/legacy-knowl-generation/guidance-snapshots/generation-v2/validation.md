# Knowl Validation Guide

Comprehensive validation steps to run after generating knowls.

## Automated Validation

### 1. Broken Link Detection

```bash
python3 scripts/validate-knowls.py
```

**What it checks:**
- All `{{< knowl id="..." section="..." >}}` references
- Verifies target file exists in the specified section
- Reports missing files and incorrect section references

**Sample output:**
```
Scanning content/ for knowl references...
Found 7494 knowl references

306 BROKEN references found:

content/algebra-homological/chain-complex.md:
  -> algebra-rings/module.md (missing)
```

**Fixing broken references:**
1. Add missing `section` parameter if linking to different section
2. Create the missing knowl if it should exist
3. Remove the reference if the concept isn't in scope

---

### 2. Anti-Pattern Detection

Run these grep commands after each generation batch:

```bash
SECTION="algebra-commutative"  # Change as needed

# 1. "Related knowls" sections (CRITICAL)
echo "=== Related Sections ==="
grep -r "Related knowls" content/$SECTION/
grep -r "## Related" content/$SECTION/
grep -rn "^\*\*Related" content/$SECTION/

# 2. Knowls inside LaTeX (CRITICAL)
echo "=== Knowls in Math ==="
grep -rn '\$.*{{< knowl' content/$SECTION/
grep -rn '{{< knowl.*\$' content/$SECTION/
grep -rn '\\[.*{{< knowl' content/$SECTION/

# 3. ={{< pattern (CRITICAL)
echo "=== Equation Context ==="
grep -rn '={{< knowl' content/$SECTION/
grep -rn '= {{< knowl' content/$SECTION/
grep -rn '\\in {{< knowl' content/$SECTION/

# 4. Categorized sub-bullets
echo "=== Categorized Bullets ==="
grep -rn '^- [A-Z][a-z]*:$' content/$SECTION/

# 5. Proof sketches (if enforcing removal)
echo "=== Proof Sketches ==="
grep -rin "proof sketch" content/$SECTION/ | wc -l

# 6. Malformed shortcodes
echo "=== Malformed Shortcodes ==="
grep -rn '{< knowl' content/$SECTION/ | grep -v '{{< knowl'
grep -rn '{{{< knowl' content/$SECTION/
```

---

### 3. YAML Validation

Check for LaTeX in description fields:

```bash
# Find descriptions with $ (likely LaTeX)
grep -rn '^description:.*\$' content/$SECTION/

# Find descriptions with backslash (likely LaTeX commands)
grep -rn '^description:.*\\' content/$SECTION/
```

---

### 4. Build Test

```bash
# Full build test
hugo --minify

# Should see no errors. Watch for:
# - "KaTeX error" messages
# - "shortcode not found" messages
# - Template execution errors
```

---

## Manual Validation

### Spot-Check Rendering

1. Start Hugo server: `hugo server`
2. Navigate to the new section
3. Click on 5-10 random knowls
4. Verify:
   - Title renders correctly
   - Math displays properly
   - Cross-links work (click through)
   - Nested knowls expand correctly

### Mathematical Review

For each section, have a subject-matter expert review:
- Accuracy of definitions
- Completeness of theorem statements (all hypotheses included)
- Correctness of examples
- Appropriate level of rigor

---

## Issue Severity

### Critical (Must Fix Before Commit)
- Broken knowl references
- Knowls inside LaTeX math
- Missing section parameter for cross-section links
- Hugo build failures

### High (Fix Before Deploy)
- "Related knowls" sections
- LaTeX in description fields
- Malformed shortcodes

### Medium (Fix When Convenient)
- Proof sketch inconsistency
- Categorized sub-bullets
- Missing examples

### Low (Track for Future)
- Missing knowls that could be added
- Cross-reference opportunities

---

## Validation Script

For convenience, here's a complete validation script:

```bash
#!/bin/bash
# validate-section.sh - Run all validation checks on a section

SECTION=$1
if [ -z "$SECTION" ]; then
    echo "Usage: ./validate-section.sh SECTION_NAME"
    exit 1
fi

echo "=========================================="
echo "Validating content/$SECTION/"
echo "=========================================="

# Count files
FILES=$(ls content/$SECTION/*.md 2>/dev/null | wc -l)
echo "Files: $FILES"

# Broken links
echo ""
echo "=== Broken Links ==="
python3 scripts/validate-knowls.py 2>&1 | grep "content/$SECTION/"

# Anti-patterns
echo ""
echo "=== Related Sections ==="
grep -c "Related knowls\|## Related" content/$SECTION/*.md 2>/dev/null || echo "0"

echo ""
echo "=== Knowls in Math ==="
grep -c '\$.*{{< knowl\|{{< knowl.*\$' content/$SECTION/*.md 2>/dev/null || echo "0"

echo ""
echo "=== Equation Context ==="
grep -c '={{< knowl\|\\in {{< knowl' content/$SECTION/*.md 2>/dev/null || echo "0"

echo ""
echo "=== Proof Sketches ==="
grep -ci "proof sketch" content/$SECTION/*.md 2>/dev/null || echo "0"

echo ""
echo "=== LaTeX in Description ==="
grep -c '^description:.*[\$\\]' content/$SECTION/*.md 2>/dev/null || echo "0"

echo ""
echo "=== Build Test ==="
hugo --minify 2>&1 | grep -i error || echo "Build successful"

echo ""
echo "=========================================="
echo "Validation complete"
echo "=========================================="
```

Save as `scripts/validate-section.sh` and run:
```bash
chmod +x scripts/validate-section.sh
./scripts/validate-section.sh algebra-commutative
```

---

## Current Status by Section

Based on `docs/knowl-modules/issues-by-section.md`:

| Section | Files | Issues |
|---------|-------|--------|
| analysis | 338 | 136 proof sketches, 10 knowl-in-math |
| fiber-bundles | 278 | Clean |
| lie-groups | 146 | 2 proof sketches |
| convex-analysis | 155 | 58 proof sketches, 2 knowl-in-math |
| algebra-groups | 136 | 59 proof sketches |
| algebra-rings | 109 | 12 proof sketches |
| algebra-modules | 85 | 10 proof sketches |
| algebra-fields-galois | 57 | Clean |
| algebra-commutative | 47 | Clean |
| algebra-category-theory | 43 | 3 related sections |
| shared-foundations | 41 | 3 proof sketches |
| algebra-homological | 31 | Clean |
| linear-algebra | 25 | 3 proof sketches |
| algebra-representation-theory | 22 | 1 knowl-in-math |

**"Clean" sections** (no issues): Use these as reference for style/format.
