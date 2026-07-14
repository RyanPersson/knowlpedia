from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_rendering_errors.py"
SPEC = importlib.util.spec_from_file_location("check_rendering_errors", MODULE_PATH)
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


class RenderedHtmlCheckerTests(unittest.TestCase):
    def scan(self, html: str, extra_files: tuple[str, ...] = ()) -> list[object]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "index.html"
            page.write_text(html, encoding="utf-8")
            for relative_path in extra_files:
                target = root / relative_path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("fixture", encoding="utf-8")
            return checker.scan_tree(root)

    def test_flags_every_visible_dollar_and_raw_math_form(self) -> None:
        issues = self.scan("<html><body><p>$x$ and a lone $ sign plus $$y$$.</p></body></html>")
        kinds = [issue.kind for issue in issues]
        self.assertIn("raw_inline_math", kinds)
        self.assertIn("raw_dollar", kinds)
        self.assertIn("raw_display_math_delimiter", kinds)

    def test_ignores_dollars_in_rendered_math_code_and_scripts(self) -> None:
        issues = self.scan(
            '<html><head><link href="/asset.css"></head><body>'
            '<span class="katex">$rendered$</span><code>$code$</code><script>$script$</script>'
            "</body></html>",
            ("asset.css",),
        )
        self.assertEqual(issues, [])

    def test_checks_local_pages_assets_and_knowl_fragments(self) -> None:
        issues = self.scan(
            '<a href="/valid/">valid</a><a href="/missing/">missing</a>'
            '<a data-knowl="/fragments/valid/core.html">valid knowl</a>'
            '<a data-knowl="/fragments/missing/core.html">missing knowl</a>',
            ("valid/index.html", "fragments/valid/core.html"),
        )
        self.assertEqual(
            [issue.kind for issue in issues],
            ["broken_local_link", "broken_knowl_target"],
        )

    def test_flags_compiler_missing_knowl_marker(self) -> None:
        issues = self.scan('<a class="missing-knowl" href="/missing/">missing</a>')
        self.assertEqual([issue.kind for issue in issues], ["missing-knowl", "broken_local_link"])

    def test_fragment_only_mode_avoids_page_copies(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text("<p>$page copy$</p>", encoding="utf-8")
            fragment = root / "fragments" / "sample" / "core.html"
            fragment.parent.mkdir(parents=True)
            fragment.write_text("<p>$canonical$</p>", encoding="utf-8")
            issues = checker.scan_tree(root, fragments_only=True)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].file, "fragments/sample/core.html")


if __name__ == "__main__":
    unittest.main()
