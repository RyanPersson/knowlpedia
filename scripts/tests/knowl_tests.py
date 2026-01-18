#!/usr/bin/env python3
"""
Knowl Test Suite - Comprehensive validation for the knowlpedia content system.

Usage:
    python3 scripts/tests/knowl_tests.py                    # Run all tests
    python3 scripts/tests/knowl_tests.py --test inventory   # Run specific test
    python3 scripts/tests/knowl_tests.py --section algebra-groups  # Test one section
    python3 scripts/tests/knowl_tests.py --list             # List available tests
    python3 scripts/tests/knowl_tests.py --fix              # Auto-fix where possible

Exit codes:
    0 = All tests passed
    1 = Test failures (broken refs, anti-patterns, etc.)
    2 = Configuration/runtime error
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Callable

# ============================================================================
# Configuration
# ============================================================================

REPO_ROOT = Path(__file__).parent.parent.parent
CONTENT_DIR = REPO_ROOT / "content"
DOCS_DIR = REPO_ROOT / "docs"
INVENTORY_FILE = DOCS_DIR / "knowl-modules" / "minimal-current-inventory.md"

# Sections that contain knowls (excludes posts, etc.)
KNOWL_SECTIONS = [
    "shared-foundations", "linear-algebra", "real-analysis", "topology",
    "measure-theory", "algebra-groups", "algebra-rings", "algebra-modules",
    "algebra-fields-galois", "algebra-commutative", "algebra-homological",
    "algebra-representation-theory", "algebra-category-theory",
    "convex-analysis", "lie-groups", "fiber-bundles",
    "langlands-letter", "shale-paper",
    # Newer sections
    "probability", "large-deviations", "asymptotics", "discrete-structures",
    "quantum-foundations", "thermodynamics", "stat-mech", "stat-mech-lattice",
    "stat-mech-quantum", "differential-geometry",
]

# ============================================================================
# Test Result Types
# ============================================================================

@dataclass
class Issue:
    """A single test issue/failure."""
    file: Path
    line: Optional[int]
    message: str
    severity: str = "error"  # error, warning, info
    fixable: bool = False

@dataclass
class TestResult:
    """Result of running a single test."""
    name: str
    passed: bool
    issues: List[Issue] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)

    def add_issue(self, file: Path, message: str, line: int = None,
                  severity: str = "error", fixable: bool = False):
        self.issues.append(Issue(file, line, message, severity, fixable))
        # Only fail on errors, not warnings or info
        if severity == "error":
            self.passed = False

# ============================================================================
# Utility Functions
# ============================================================================

def get_knowl_files(section: str = None) -> List[Path]:
    """Get all knowl markdown files, optionally filtered by section."""
    files = []
    sections = [section] if section else KNOWL_SECTIONS

    for sec in sections:
        sec_dir = CONTENT_DIR / sec
        if sec_dir.exists():
            for f in sec_dir.glob("*.md"):
                if f.name != "_index.md":
                    files.append(f)
    return files

def get_all_knowl_ids() -> Dict[str, Set[str]]:
    """Return {section: {knowl_id, ...}} for all sections."""
    result = {}
    for section in KNOWL_SECTIONS:
        sec_dir = CONTENT_DIR / section
        if sec_dir.exists():
            result[section] = {
                f.stem for f in sec_dir.glob("*.md")
                if f.name != "_index.md"
            }
    return result

def parse_frontmatter(content: str) -> Optional[dict]:
    """Parse YAML frontmatter from markdown content (simple regex-based)."""
    if not content.startswith("---"):
        return None
    try:
        end = content.index("---", 3)
        yaml_str = content[3:end]
        # Simple key: value parsing (handles most cases)
        result = {}
        for line in yaml_str.strip().split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('#'):
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                result[key] = value
        return result
    except ValueError:
        return None

# ============================================================================
# Test: Broken Knowl References
# ============================================================================

KNOWL_PATTERN = re.compile(r'\{\{<\s*knowl\s+([^>]+)>\}\}')
ID_PATTERN = re.compile(r'id="([^"]+)"')
SECTION_PATTERN = re.compile(r'section="([^"]+)"')

def test_broken_references(section: str = None) -> TestResult:
    """Check that all knowl references point to existing files."""
    result = TestResult(name="broken_references", passed=True)
    all_knowls = get_all_knowl_ids()

    for md_file in get_knowl_files(section):
        file_section = md_file.parent.name
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            result.add_issue(md_file, f"Could not read file: {e}")
            continue

        for i, line in enumerate(content.split('\n'), 1):
            for match in KNOWL_PATTERN.finditer(line):
                attrs = match.group(1)
                id_match = ID_PATTERN.search(attrs)
                section_match = SECTION_PATTERN.search(attrs)

                if id_match:
                    knowl_id = id_match.group(1)
                    knowl_section = section_match.group(1) if section_match else file_section

                    # Check if target exists
                    if knowl_section not in all_knowls:
                        result.add_issue(
                            md_file,
                            f"Unknown section '{knowl_section}' in reference to '{knowl_id}'",
                            line=i
                        )
                    elif knowl_id not in all_knowls.get(knowl_section, set()):
                        result.add_issue(
                            md_file,
                            f"Broken reference: {knowl_section}/{knowl_id}.md does not exist",
                            line=i
                        )

    result.stats["files_checked"] = len(get_knowl_files(section))
    result.stats["broken_refs"] = len(result.issues)
    return result

# ============================================================================
# Test: Anti-Patterns
# ============================================================================

ANTI_PATTERNS = [
    # (name, pattern, message, severity)
    ("related_section",
     re.compile(r'^##\s*Related|^\*\*Related\s+knowls', re.MULTILINE | re.IGNORECASE),
     "Contains 'Related knowls' section - links should be woven into prose",
     "error"),

    # CRITICAL: Knowl inside math delimiters causes HUGOSHORTCODE rendering errors
    # Matches \( ... {{< knowl ... on the same line (before closing \))
    ("knowl_in_inline_math",
     re.compile(r'\\\([^\n\\]*\{\{<\s*knowl'),
     "Knowl shortcode inside \\(...\\) math delimiters - will render as HUGOSHORTCODE garbage",
     "error"),

    # Knowl inside display math \[ ... \] - only match if knowl appears on same line as \[ or on a line between \[ and \]
    # More conservative: only catch knowls on lines that are clearly inside a math block
    # (line starting with common math patterns or knowl immediately after \[)
    ("knowl_in_display_math",
     re.compile(r'\\\[\s*\{\{<\s*knowl|\\\[[^\]]*\n[^\]]*\{\{<\s*knowl'),
     "Knowl shortcode inside \\[...\\] display math - will render as HUGOSHORTCODE garbage",
     "error"),

    # Conservative check: knowl immediately after math operators suggests equation context
    # This catches patterns like `$x \in {{< knowl` or `$f(x) = {{< knowl`
    ("knowl_after_math_operator",
     re.compile(r'\\(?:in|subseteq|subset|supseteq|supset|to|mapsto|rightarrow|leftarrow|Rightarrow)\s*\{\{<\s*knowl'),
     "Knowl shortcode after LaTeX operator (likely in equation context)",
     "warning"),

    ("knowl_after_equals",
     re.compile(r'=\s*\{\{<\s*knowl'),
     "Knowl shortcode immediately after '=' (equation context)",
     "warning"),

    ("triple_braces",
     re.compile(r'\{\{\{<|\>\}\}\}'),
     "Triple braces in shortcode (should be double)",
     "error"),

    ("single_brace",
     re.compile(r'(?<!\{)\{<\s*knowl'),
     "Single opening brace in shortcode (should be double)",
     "error"),

    ("latex_in_description",
     re.compile(r'^description:\s*"[^"]*[\$\\][^"]*"', re.MULTILINE),
     "LaTeX in description field (should be plain text)",
     "warning"),

    ("md_in_knowl_id",
     re.compile(r'knowl\s+id="[^"]+\.md"'),
     "'.md' extension in knowl id (should be slug only)",
     "error"),
]

def test_anti_patterns(section: str = None) -> TestResult:
    """Detect known anti-patterns in knowl content."""
    result = TestResult(name="anti_patterns", passed=True)
    pattern_counts = defaultdict(int)

    for md_file in get_knowl_files(section):
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception:
            continue

        for name, pattern, message, severity in ANTI_PATTERNS:
            matches = list(pattern.finditer(content))
            if matches:
                pattern_counts[name] += len(matches)
                for match in matches:
                    # Find line number
                    line_num = content[:match.start()].count('\n') + 1
                    result.add_issue(
                        md_file, message, line=line_num,
                        severity=severity,
                        fixable=(name in ["triple_braces", "single_brace", "md_in_knowl_id"])
                    )

    result.stats = dict(pattern_counts)
    return result

# ============================================================================
# Test: Inventory Sync
# ============================================================================

def parse_inventory() -> Dict[str, Set[str]]:
    """Parse minimal-current-inventory.md to get expected knowls."""
    if not INVENTORY_FILE.exists():
        return {}

    content = INVENTORY_FILE.read_text()
    inventory = {}
    current_section = None

    # Pattern for section headers: ### `section-name` (count)
    section_pattern = re.compile(r'^###\s+`([a-z0-9-]+)`\s+\(\d+\)', re.MULTILINE)

    # Find all sections and their positions
    sections = [(m.group(1), m.end()) for m in section_pattern.finditer(content)]

    for i, (section_name, start_pos) in enumerate(sections):
        # Find end of this section (start of next, or end of file)
        end_pos = sections[i + 1][1] if i + 1 < len(sections) else len(content)
        section_content = content[start_pos:end_pos]

        # Extract knowl slugs (comma-separated after type headers)
        # Slugs are listed as: slug1, slug2, slug3
        slugs = set()
        # Look for lines that are comma-separated lists of slugs
        for line in section_content.split('\n'):
            line = line.strip()
            # Skip headers and empty lines
            if not line or line.startswith('#') or line.startswith('**') or line.startswith('|') or line.startswith('---'):
                continue
            # This should be a list of slugs
            for slug in line.split(', '):
                slug = slug.strip()
                if slug and re.match(r'^[a-zA-Z0-9_-]+$', slug):
                    slugs.add(slug)

        if slugs:
            inventory[section_name] = slugs

    return inventory

def test_inventory_sync(section: str = None) -> TestResult:
    """Check that inventory file matches actual filesystem content."""
    result = TestResult(name="inventory_sync", passed=True)

    inventory = parse_inventory()
    if not inventory:
        result.add_issue(
            INVENTORY_FILE,
            "Could not parse inventory file or file not found",
            severity="warning"
        )
        return result

    actual = get_all_knowl_ids()
    sections_to_check = [section] if section else list(set(inventory.keys()) | set(actual.keys()))

    missing_from_fs = []  # In inventory but not filesystem
    missing_from_inv = []  # In filesystem but not inventory

    for sec in sections_to_check:
        inv_set = inventory.get(sec, set())
        fs_set = actual.get(sec, set())

        for slug in inv_set - fs_set:
            missing_from_fs.append(f"{sec}/{slug}")
            result.add_issue(
                INVENTORY_FILE,
                f"Listed in inventory but not on filesystem: {sec}/{slug}.md"
            )

        for slug in fs_set - inv_set:
            missing_from_inv.append(f"{sec}/{slug}")
            result.add_issue(
                CONTENT_DIR / sec / f"{slug}.md",
                f"Exists on filesystem but not in inventory: {sec}/{slug}.md"
            )

    result.stats["sections_checked"] = len(sections_to_check)
    result.stats["missing_from_filesystem"] = len(missing_from_fs)
    result.stats["missing_from_inventory"] = len(missing_from_inv)
    return result

# ============================================================================
# Test: Frontmatter Validation
# ============================================================================

REQUIRED_FIELDS = ["title"]
RECOMMENDED_FIELDS = ["description"]

def test_frontmatter(section: str = None) -> TestResult:
    """Validate YAML frontmatter in all knowl files."""
    result = TestResult(name="frontmatter", passed=True)

    for md_file in get_knowl_files(section):
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            result.add_issue(md_file, f"Could not read: {e}")
            continue

        fm = parse_frontmatter(content)
        if fm is None:
            result.add_issue(md_file, "Missing or invalid YAML frontmatter")
            continue

        for field in REQUIRED_FIELDS:
            if field not in fm or not fm[field]:
                result.add_issue(md_file, f"Missing required field: {field}")

        for field in RECOMMENDED_FIELDS:
            if field not in fm or not fm[field]:
                result.add_issue(
                    md_file,
                    f"Missing recommended field: {field}",
                    severity="warning"
                )

    return result

# ============================================================================
# Test: Duplicate Knowl IDs
# ============================================================================

def test_duplicates(section: str = None) -> TestResult:
    """Check for duplicate knowl IDs within sections."""
    result = TestResult(name="duplicates", passed=True)

    sections = [section] if section else KNOWL_SECTIONS

    for sec in sections:
        sec_dir = CONTENT_DIR / sec
        if not sec_dir.exists():
            continue

        seen = {}
        for f in sec_dir.glob("*.md"):
            if f.name == "_index.md":
                continue
            slug = f.stem
            if slug in seen:
                result.add_issue(
                    f,
                    f"Duplicate knowl ID '{slug}' (also at {seen[slug]})"
                )
            else:
                seen[slug] = f

    return result

# ============================================================================
# Test: Orphan Detection
# ============================================================================

def test_orphans(section: str = None) -> TestResult:
    """Find knowls that are never referenced by any other knowl."""
    result = TestResult(name="orphans", passed=True)

    # Collect all references
    all_refs = defaultdict(set)  # {(section, id): set of referencing files}
    all_knowls = set()

    for md_file in get_knowl_files(section):
        file_section = md_file.parent.name
        all_knowls.add((file_section, md_file.stem))

        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception:
            continue

        for match in KNOWL_PATTERN.finditer(content):
            attrs = match.group(1)
            id_match = ID_PATTERN.search(attrs)
            section_match = SECTION_PATTERN.search(attrs)

            if id_match:
                knowl_id = id_match.group(1)
                knowl_section = section_match.group(1) if section_match else file_section
                all_refs[(knowl_section, knowl_id)].add(md_file)

    # Find orphans
    orphans = all_knowls - set(all_refs.keys())

    for sec, slug in sorted(orphans):
        result.add_issue(
            CONTENT_DIR / sec / f"{slug}.md",
            f"Orphan knowl: never referenced by any other knowl",
            severity="info"
        )

    result.stats["total_knowls"] = len(all_knowls)
    result.stats["orphans"] = len(orphans)
    # Don't fail on orphans - they're just informational
    result.passed = True
    return result

# ============================================================================
# Test: Section Counts
# ============================================================================

def test_section_counts(section: str = None) -> TestResult:
    """Verify knowl counts per section match inventory."""
    result = TestResult(name="section_counts", passed=True)

    inventory = parse_inventory()
    actual = get_all_knowl_ids()

    sections = [section] if section else KNOWL_SECTIONS

    for sec in sections:
        inv_count = len(inventory.get(sec, set()))
        actual_count = len(actual.get(sec, set()))

        if inv_count > 0 and inv_count != actual_count:
            result.add_issue(
                CONTENT_DIR / sec,
                f"Count mismatch: inventory has {inv_count}, filesystem has {actual_count}",
                severity="warning"
            )

    return result

# ============================================================================
# Test: Hugo Build (checks for HUGOSHORTCODE rendering errors)
# ============================================================================

import subprocess
import tempfile
import shutil

def test_hugo_build(section: str = None) -> TestResult:
    """Build site and check for HUGOSHORTCODE placeholder errors in rendered HTML.

    This catches shortcode rendering issues regardless of cause (e.g., shortcodes
    inside math delimiters, malformed shortcodes, etc.). The HUGOSHORTCODE placeholder
    appears when Hugo can't properly resolve a shortcode during rendering.
    """
    result = TestResult(name="hugo_build", passed=True)

    # Build to a temp directory
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            proc = subprocess.run(
                ["hugo", "--destination", tmpdir],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=120
            )
        except subprocess.TimeoutExpired:
            result.add_issue(REPO_ROOT, "Hugo build timed out after 120s")
            return result
        except FileNotFoundError:
            result.add_issue(REPO_ROOT, "Hugo not found - install hugo to run this test", severity="warning")
            return result

        if proc.returncode != 0:
            # Check stderr for specific errors
            for line in proc.stderr.split('\n'):
                if 'ERROR' in line:
                    result.add_issue(REPO_ROOT, f"Hugo build error: {line.strip()}")

        # Search rendered HTML for HUGOSHORTCODE placeholders
        placeholder_pattern = re.compile(r'HUGOSHORTCODE\d+[a-zA-Z0-9]*')
        # Pattern to match JSON-LD script blocks (SEO metadata)
        jsonld_pattern = re.compile(r'<script type="application/ld\+json">.*?</script>', re.DOTALL)

        files_with_errors = []
        files_with_jsonld_only = []

        for html_file in Path(tmpdir).rglob("*.html"):
            try:
                content = html_file.read_text(encoding='utf-8', errors='ignore')

                # Check for errors in visible content (excluding JSON-LD)
                visible_content = jsonld_pattern.sub('', content)
                visible_matches = placeholder_pattern.findall(visible_content)

                # Check for errors in JSON-LD only
                jsonld_content = ''.join(jsonld_pattern.findall(content))
                jsonld_matches = placeholder_pattern.findall(jsonld_content)

                # Determine source file
                rel_path = html_file.relative_to(tmpdir)
                parts = list(rel_path.parts)
                if parts[-1] == "index.html":
                    parts = parts[:-1]
                source_guess = "/".join(parts) + ".md" if parts else "unknown"
                source_path = CONTENT_DIR / source_guess if len(parts) > 1 else REPO_ROOT

                if visible_matches:
                    # Visible content errors are critical
                    files_with_errors.append((source_guess, len(visible_matches)))
                    result.add_issue(
                        source_path,
                        f"HUGOSHORTCODE in visible content ({len(visible_matches)} occurrences) - shortcode inside math or malformed",
                    )
                elif jsonld_matches:
                    # JSON-LD only errors are warnings (don't affect user experience)
                    files_with_jsonld_only.append((source_guess, len(jsonld_matches)))
                    result.add_issue(
                        source_path,
                        f"HUGOSHORTCODE in JSON-LD metadata only ({len(jsonld_matches)} occurrences) - page renders correctly",
                        severity="warning"
                    )
            except Exception:
                continue

        result.stats["build_success"] = 1 if proc.returncode == 0 else 0
        result.stats["visible_errors"] = len(files_with_errors)
        result.stats["jsonld_warnings"] = len(files_with_jsonld_only)

    return result

# ============================================================================
# Test Registry
# ============================================================================

TESTS: Dict[str, Callable] = {
    "broken_references": test_broken_references,
    "anti_patterns": test_anti_patterns,
    "inventory_sync": test_inventory_sync,
    "frontmatter": test_frontmatter,
    "duplicates": test_duplicates,
    "orphans": test_orphans,
    "section_counts": test_section_counts,
    "hugo_build": test_hugo_build,
}

# ============================================================================
# Output Formatting
# ============================================================================

def print_result(result: TestResult, verbose: bool = False):
    """Print test result with appropriate formatting."""
    status = "✓ PASS" if result.passed else "✗ FAIL"
    color = "\033[32m" if result.passed else "\033[31m"
    reset = "\033[0m"

    print(f"{color}{status}{reset} {result.name}")

    if result.stats:
        stats_str = ", ".join(f"{k}={v}" for k, v in result.stats.items())
        print(f"       Stats: {stats_str}")

    if not result.passed or verbose:
        # Group issues by file
        by_file = defaultdict(list)
        for issue in result.issues:
            by_file[issue.file].append(issue)

        for file, issues in sorted(by_file.items()):
            rel_path = file.relative_to(REPO_ROOT) if file.is_relative_to(REPO_ROOT) else file
            print(f"       {rel_path}:")
            for issue in issues[:5]:  # Limit per file
                line_info = f":{issue.line}" if issue.line else ""
                severity_marker = "⚠" if issue.severity == "warning" else "✗"
                print(f"         {severity_marker} {issue.message}{line_info}")
            if len(issues) > 5:
                print(f"         ... and {len(issues) - 5} more")

# ============================================================================
# Main Runner
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Run knowl validation tests")
    parser.add_argument("--test", "-t", help="Run specific test(s)", action="append")
    parser.add_argument("--section", "-s", help="Test only specific section")
    parser.add_argument("--list", "-l", action="store_true", help="List available tests")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--fix", action="store_true", help="Auto-fix fixable issues")
    args = parser.parse_args()

    if args.list:
        print("Available tests:")
        for name, func in TESTS.items():
            doc = func.__doc__.split('\n')[0] if func.__doc__ else ""
            print(f"  {name}: {doc}")
        return 0

    # Select tests to run
    test_names = args.test if args.test else list(TESTS.keys())

    print(f"Running {len(test_names)} test(s)...")
    if args.section:
        print(f"Filtering to section: {args.section}")
    print()

    results = []
    for name in test_names:
        if name not in TESTS:
            print(f"Unknown test: {name}")
            continue

        result = TESTS[name](args.section)
        results.append(result)
        print_result(result, args.verbose)

    # Summary
    print()
    passed = sum(1 for r in results if r.passed)
    failed = len(results) - passed

    if failed == 0:
        print(f"\033[32m✓ All {passed} tests passed\033[0m")
        return 0
    else:
        print(f"\033[31m✗ {failed} test(s) failed, {passed} passed\033[0m")
        return 1

if __name__ == "__main__":
    sys.exit(main())
