# Knowl Test Suite

Comprehensive validation for the knowlpedia content system.

## Quick Start

```bash
# Run all tests
python3 scripts/tests/knowl_tests.py

# Run specific test
python3 scripts/tests/knowl_tests.py -t broken_references
python3 scripts/tests/knowl_tests.py -t anti_patterns

# Test a specific section
python3 scripts/tests/knowl_tests.py -s algebra-groups

# List available tests
python3 scripts/tests/knowl_tests.py --list
```

## Available Tests

| Test | Description | Severity |
|------|-------------|----------|
| `broken_references` | Checks all `{{< knowl >}}` references point to existing files | Critical |
| `anti_patterns` | Detects known anti-patterns (related sections, triple braces, etc.) | Critical/Warning |
| `inventory_sync` | Checks inventory file matches filesystem | Warning |
| `frontmatter` | Validates YAML frontmatter (title, description) | Warning |
| `duplicates` | Checks for duplicate knowl IDs within sections | Error |
| `orphans` | Finds knowls never referenced by others | Info |
| `section_counts` | Verifies inventory counts match filesystem | Warning |

## Anti-Patterns Detected

1. **Related Sections** - "Related knowls" or "## Related" sections at end of file
2. **Triple Braces** - `{{{<` or `>}}}` instead of `{{<` and `>}}`
3. **Single Braces** - `{<` instead of `{{<`
4. **Math Operator Context** - Knowl immediately after `\in`, `\to`, `=`, etc.
5. **LaTeX in Description** - `$` or `\` in YAML description field
6. **`.md` in ID** - `knowl id="foo.md"` instead of `knowl id="foo"`

## Inventory Management

```bash
# Regenerate inventory from filesystem
python3 scripts/tests/generate_inventory.py --write

# Preview changes
python3 scripts/tests/generate_inventory.py --diff
```

## Exit Codes

- `0` - All tests passed
- `1` - Test failures found
- `2` - Configuration/runtime error

## Integration with Existing Scripts

These tests complement the existing scripts:

- `scripts/validate-knowls.py` - Simpler broken reference checker (now superseded)
- `scripts/fix-knowls.py` - Auto-fixes common GPT output issues (triple braces, etc.)

Recommended workflow after generating knowls:
```bash
# Fix known issues automatically
python3 scripts/fix-knowls.py content/NEW-SECTION/

# Run comprehensive validation
python3 scripts/tests/knowl_tests.py -s NEW-SECTION

# If inventory_sync fails, regenerate
python3 scripts/tests/generate_inventory.py --write
```

## Adding New Tests

Add new test functions to `knowl_tests.py`:

```python
def test_my_check(section: str = None) -> TestResult:
    """Description of what this test checks."""
    result = TestResult(name="my_check", passed=True)

    for md_file in get_knowl_files(section):
        # Your validation logic
        if problem_found:
            result.add_issue(md_file, "Description of problem", line=42)

    return result

# Register in TESTS dict
TESTS["my_check"] = test_my_check
```
