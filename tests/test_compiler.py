from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "packages" / "compiler" / "knowl_compile.py"
SPEC = importlib.util.spec_from_file_location("knowl_compile", MODULE_PATH)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


class SingleFileSectionTests(unittest.TestCase):
    def test_documents_and_indexes_remain_continuous_by_default(self) -> None:
        self.assertFalse(compiler.uses_progressive_sections({"kind": "document"}))
        self.assertFalse(compiler.uses_progressive_sections({"kind": "index"}))
        self.assertTrue(compiler.uses_progressive_sections({"kind": "definition"}))

    def test_section_mode_can_override_the_kind_default(self) -> None:
        self.assertTrue(compiler.uses_progressive_sections({"kind": "document", "section_mode": "progressive"}))
        self.assertFalse(compiler.uses_progressive_sections({"kind": "definition", "section_mode": "continuous"}))

    def test_prelude_remains_core_and_h2_blocks_become_sections(self) -> None:
        core, sections = compiler.split_single_file_sections(
            "A compact definition.\n\n## Examples\nFirst.\n\n## Remarks\nSecond."
        )
        self.assertEqual(core, "A compact definition.")
        self.assertEqual([section["id"] for section in sections], ["examples", "remarks"])
        self.assertEqual(sections[0]["markdown"], "First.")

    def test_leading_h2_becomes_core_instead_of_an_empty_panel(self) -> None:
        core, sections = compiler.split_single_file_sections(
            "## Statement\nThe theorem.\n\n## Examples\nAn example."
        )
        self.assertEqual(core, "The theorem.")
        self.assertEqual([section["title"] for section in sections], ["Examples"])

    def test_standalone_examples_label_is_progressively_disclosed(self) -> None:
        core, sections = compiler.split_single_file_sections(
            "A definition.\n\n**Examples:**\n- One\n- Two"
        )
        self.assertEqual(core, "A definition.")
        self.assertEqual(sections[0]["id"], "examples")
        self.assertIn("- One", sections[0]["markdown"])

    def test_duplicate_section_titles_receive_stable_suffixes(self) -> None:
        _, sections = compiler.split_single_file_sections(
            "Core.\n\n## Example\nOne.\n\n## Example\nTwo."
        )
        self.assertEqual([section["id"] for section in sections], ["example", "example-2"])


class RenderContractTests(unittest.TestCase):
    def test_generated_paths_preserve_legacy_lowercase_urls(self) -> None:
        knowl_id = "shale-paper/segal-unitary-representation-Ufrak"
        self.assertEqual(
            compiler.slug_to_relpath(knowl_id),
            Path("shale-paper/segal-unitary-representation-ufrak"),
        )
        self.assertEqual(
            compiler.target_href(knowl_id),
            "/shale-paper/segal-unitary-representation-ufrak/",
        )
        self.assertEqual(
            compiler.fragment_href(knowl_id),
            "/fragments/shale-paper/segal-unitary-representation-ufrak/core.html",
        )

    def test_inline_dollar_math_is_deterministic(self) -> None:
        for tex in ("1", "(0)", "k[x]", r"\mathbb{F}_q[[t]]"):
            with self.subTest(tex=tex):
                protected, replacements = compiler.protect_math(f"${tex}$")
                self.assertEqual(protected, "@@KNOWL_MATH_0@@")
                self.assertEqual(len(replacements), 1)

    def test_power_series_brackets_inside_math_are_not_wikilinks(self) -> None:
        rendered = compiler.render_inline(r"$\mathbb{F}_q[[t]]$", {})
        self.assertIn('class="katex"', rendered)
        self.assertNotIn('class="knowl"', rendered)
        self.assertNotIn("$", rendered)

    def test_root_relative_markdown_link_is_navigation_only(self) -> None:
        rendered = compiler.render_inline("[Index](/conjectures/generated/example/)", {})
        self.assertIn('class="page-link"', rendered)
        self.assertIn('href="/conjectures/generated/example/"', rendered)
        self.assertNotIn("data-knowl", rendered)

    def test_https_markdown_link_preserves_inline_code_label(self) -> None:
        rendered = compiler.render_inline("[`source.lean`](https://example.com/source)", {})
        self.assertIn('href="https://example.com/source"', rendered)
        self.assertIn("<code>source.lean</code>", rendered)

    def test_unsafe_markdown_link_is_not_activated(self) -> None:
        rendered = compiler.render_inline("[bad](javascript:alert(1))", {})
        self.assertNotIn("<a ", rendered)

    def test_redundant_source_h1_is_removed_from_rendered_core(self) -> None:
        source = "# Document title\n\nFirst paragraph.\n\n## Section"
        self.assertEqual(
            compiler.without_redundant_leading_h1(source),
            "First paragraph.\n\n## Section",
        )

    def make_knowl(self) -> object:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.knowl.md"
            return compiler.knowl_from_meta(
                {
                    "id": "sample/concept",
                    "title": "Sample concept",
                    "kind": "definition",
                    "summary": "A concise orientation sentence.",
                    "aliases": ["sample"],
                    "domains": ["sample"],
                },
                path,
                "A **sample concept** is defined here.",
                sections=[
                    {
                        "id": "examples",
                        "title": "Examples over \\(k\\)",
                        "kind": "markdown",
                        "markdown": "An example.",
                    }
                ],
            )

    def test_fragment_keeps_metadata_out_of_the_reading_flow(self) -> None:
        knowl = self.make_knowl()
        fragment = compiler.render_knowl_core(knowl, {knowl.id: knowl})
        self.assertIn('data-knowl-title="Sample concept"', fragment)
        self.assertNotIn('class="knowl-header"', fragment)
        self.assertNotIn('class="knowl-summary"', fragment)
        self.assertNotIn('class="knowl-footer"', fragment)
        self.assertNotIn('section-links-label', fragment)
        self.assertIn('class="section-chip"', fragment)
        self.assertIn("/sections/examples.html", fragment)
        self.assertEqual(fragment.count('class="knowl-page-link"'), 1)
        self.assertEqual(fragment.count('class="knowl-close"'), 1)

    def test_registry_exposes_section_fragments(self) -> None:
        knowl = self.make_knowl()
        registry = compiler.registry_json({knowl.id: knowl})
        self.assertEqual(registry[knowl.id]["sections"][0]["id"], "examples")
        self.assertTrue(registry[knowl.id]["sections"][0]["fragment"].endswith("/sections/examples.html"))

    def test_generic_knowl_kind_is_storage_metadata_not_reader_copy(self) -> None:
        self.assertEqual(compiler.display_kind("knowl"), "")
        self.assertIsNone(compiler.core_heading_for_kind("knowl"))

    def test_search_artifact_contains_aliases_and_summary(self) -> None:
        knowl = self.make_knowl()
        item = compiler.search_json({knowl.id: knowl})[0]
        self.assertEqual(item["aliases"], ["sample"])
        self.assertEqual(item["summary"], "A concise orientation sentence.")


class PrebuiltDiagramTests(unittest.TestCase):
    def test_prebuilt_diagram_is_used_without_local_tex_tools(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(compiler, "executable", return_value=None):
            renderer = compiler.DiagramRenderer()
            renderer.configure_prebuilt(Path(directory))
            source = r"A \arrow[r] & B"
            prebuilt_path = renderer._prebuilt_path(source, "tikz-cd")
            assert prebuilt_path is not None
            expected = '<figure class="diagram diagram-image">prebuilt</figure>'
            prebuilt_path.write_text(expected, encoding="utf-8")
            self.assertEqual(renderer.render(source, "tikz-cd"), expected)

    def test_refresh_writes_portable_prebuilt_fragment(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(compiler, "executable", return_value=None):
            renderer = compiler.DiagramRenderer()
            renderer._png_engine = "pdflatex"
            renderer._png_converter = "gs"
            renderer._render_png = lambda source, kind: '<figure class="diagram diagram-image">fresh</figure>'
            renderer.configure_prebuilt(Path(directory), refresh=True)
            source = r"A \arrow[r] & B"
            rendered = renderer.render(source, "tikz-cd")
            prebuilt_path = renderer._prebuilt_path(source, "tikz-cd")
            assert prebuilt_path is not None
            self.assertEqual(prebuilt_path.read_text(encoding="utf-8"), rendered)


if __name__ == "__main__":
    unittest.main()
