from __future__ import annotations

import importlib.util
import json
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


def write_knowl(path: Path, knowl_id: str, title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "+++",
                f'id = "{knowl_id}"',
                f'title = "{title}"',
                'kind = "definition"',
                f'summary = "Summary for {title}."',
                f'aliases = ["{title}"]',
                'domains = ["sample"]',
                "+++",
                "",
                f"{title} body.",
            ]
        ),
        encoding="utf-8",
    )


def write_package(root: Path) -> None:
    (root / "knowlpack.toml").write_text(
        "\n".join(
            [
                'id = "org.example.profile-test"',
                'title = "Profile Test"',
                'content_dir = "content"',
                'development_content_dirs = ["testing"]',
            ]
        ),
        encoding="utf-8",
    )


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


class BuildProfileTests(unittest.TestCase):
    def test_profile_precedence_is_explicit_then_environment_then_development(self) -> None:
        self.assertEqual(compiler.resolve_profile(environment={}).name, "development")
        self.assertEqual(
            compiler.resolve_profile(environment={"KNOWLPEDIA_PROFILE": "production"}).name,
            "production",
        )
        self.assertEqual(
            compiler.resolve_profile("development", {"KNOWLPEDIA_PROFILE": "production"}).name,
            "development",
        )
        with self.assertRaisesRegex(ValueError, "Unknown Knowlpedia profile"):
            compiler.resolve_profile(environment={"KNOWLPEDIA_PROFILE": "staging"})

    def test_development_and_production_builds_use_different_content_roots(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_package(root)
            write_knowl(root / "content" / "main.knowl.md", "sample/main", "Main")
            write_knowl(root / "testing" / "draft.knowl.md", "sample/draft", "Draft")

            development_out = root / "development-out"
            production_out = root / "production-out"
            self.assertEqual(
                compiler.write_site(root, development_out, profile=compiler.BUILD_PROFILES["development"]),
                0,
            )
            self.assertEqual(
                compiler.write_site(root, production_out, profile=compiler.BUILD_PROFILES["production"]),
                0,
            )

            development_registry = json.loads(
                (development_out / "indexes" / "registry.json").read_text(encoding="utf-8")
            )
            production_registry = json.loads(
                (production_out / "indexes" / "registry.json").read_text(encoding="utf-8")
            )
            self.assertEqual(development_registry["sample/draft"]["visibility"], "development")
            self.assertEqual(set(development_registry), {"sample/main", "sample/draft"})
            self.assertEqual(set(production_registry), {"sample/main"})
            self.assertTrue((development_out / "testing" / "index.html").is_file())
            self.assertFalse((production_out / "testing").exists())
            self.assertTrue((development_out / "index" / "index.html").is_file())
            self.assertFalse((development_out / "library").exists())
            self.assertTrue((development_out / "indexes" / "dependencies.json").is_file())
            self.assertTrue((development_out / "assets" / "knowl-testing.js").is_file())
            self.assertFalse((production_out / "assets" / "knowl-testing.js").exists())
            self.assertIn(
                'data-knowlpedia-profile="development"',
                (development_out / "index.html").read_text(encoding="utf-8"),
            )
            development_html = (development_out / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-knowlpedia-development-content="true"', development_html)
            self.assertIn('data-knowlpedia-testing-ui="true"', development_html)
            production_html = (production_out / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-knowlpedia-profile="production"', production_html)
            self.assertIn('data-knowlpedia-development-content="false"', production_html)
            self.assertIn('data-knowlpedia-testing-ui="false"', production_html)
            self.assertNotIn('id="testing-open"', production_html)

    def test_production_does_not_parse_malformed_testing_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_package(root)
            write_knowl(root / "content" / "main.knowl.md", "sample/main", "Main")
            malformed = root / "testing" / "broken.knowl.md"
            malformed.parent.mkdir(parents=True)
            malformed.write_text("+++\nthis is not toml = [\n+++\n", encoding="utf-8")
            self.assertEqual(
                compiler.write_site(
                    root,
                    root / "production-out",
                    profile=compiler.BUILD_PROFILES["production"],
                ),
                0,
            )
            with self.assertRaises(Exception):
                compiler.write_site(
                    root,
                    root / "development-out",
                    profile=compiler.BUILD_PROFILES["development"],
                )

    def test_duplicate_ids_across_roots_fail_development_build(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_package(root)
            write_knowl(root / "content" / "main.knowl.md", "sample/shared", "Main")
            write_knowl(root / "testing" / "draft.knowl.md", "sample/shared", "Draft")
            with self.assertRaisesRegex(ValueError, "Duplicate knowl ids: sample/shared"):
                compiler.write_site(
                    root,
                    root / "development-out",
                    profile=compiler.BUILD_PROFILES["development"],
                )


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

    def test_all_four_math_delimiters_are_supported(self) -> None:
        forms = (
            (r"\(x + y\)", False),
            ("$x + y$", False),
            (r"\[x + y\]", True),
            ("$$x + y$$", True),
        )
        for source, display in forms:
            with self.subTest(source=source):
                protected, replacements = compiler.protect_math(source)
                self.assertEqual(protected, "@@KNOWL_MATH_0@@")
                self.assertEqual(len(replacements), 1)
                rendered = next(iter(replacements.values()))
                expected_class = "math-display" if display else "math-inline"
                self.assertIn(expected_class, rendered)

    def test_equivalent_delimiters_render_identically(self) -> None:
        self.assertEqual(
            compiler.render_inline(r"\(\mathbb{F}_q[[t]]\)", {}),
            compiler.render_inline(r"$\mathbb{F}_q[[t]]$", {}),
        )
        self.assertEqual(
            compiler.render_markdown("\\[x^2\\]", {}),
            compiler.render_markdown("$$x^2$$", {}),
        )

    def test_power_series_brackets_inside_math_are_not_wikilinks(self) -> None:
        rendered = compiler.render_inline(r"$\mathbb{F}_q[[t]]$", {})
        self.assertIn('class="katex"', rendered)
        self.assertNotIn('class="knowl"', rendered)
        self.assertNotIn("$", rendered)

    def test_top_level_knowl_id_is_rendered_as_a_wikilink(self) -> None:
        target = self.make_knowl()
        target.id = "formal-groups"
        registry = {target.id: target}
        for source in ("[[formal-groups|Formal groups]]", "[[formal-groups]]"):
            with self.subTest(source=source):
                rendered = compiler.render_inline(source, registry)
                self.assertIn('class="knowl"', rendered)
                self.assertIn('href="/formal-groups/"', rendered)
                self.assertIn('data-knowl="/fragments/formal-groups/core.html"', rendered)
                self.assertNotIn("[[", rendered)

        missing = compiler.render_inline("[[unknown-top-level]]", registry)
        self.assertIn('class="missing-knowl"', missing)
        self.assertIn("unknown-top-level", missing)

    def test_wikilink_extraction_supports_top_level_and_multiline_labels(self) -> None:
        source = (
            "[[formal-groups|Formal groups]] and "
            "[[algebra-hyperstructures/hyperfield|a hyperfield\n"
            "with a multiline label]] and "
            "[[fiber-bundles/homotopy-class-mbg|Homotopy class [M,BG]]]"
        )
        self.assertEqual(
            compiler.wikilinks_in_text(source),
            [
                "formal-groups",
                "algebra-hyperstructures/hyperfield",
                "fiber-bundles/homotopy-class-mbg",
            ],
        )
        rendered = compiler.render_inline(source, {})
        self.assertIn(">Homotopy class [M,BG]</a>", rendered)

    def test_wikilink_extraction_ignores_power_series_brackets_in_math(self) -> None:
        source = r"$R[[x]]$ and \(k[[t]]\) but [[formal-groups|formal groups]]"
        self.assertEqual(compiler.wikilinks_in_text(source), ["formal-groups"])

    def test_wikilink_extraction_and_rendering_ignore_inline_code(self) -> None:
        source = "`R[[x]]` and [[formal-groups|code `k[[t]]` and formal groups]]"
        self.assertEqual(compiler.wikilinks_in_text(source), ["formal-groups"])
        rendered = compiler.render_inline(source, {})
        self.assertIn("<code>R[[x]]</code>", rendered)
        self.assertIn(">code <code>k[[t]]</code> and formal groups</a>", rendered)
        self.assertNotIn('href="/x/"', rendered)
        self.assertNotIn('href="/t/"', rendered)

        fenced = "before\n```text\n[[not-a-knowl]]\n```\nafter [[formal-groups]]"
        self.assertEqual(compiler.wikilinks_in_text(fenced), ["formal-groups"])

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

    def test_pipe_table_renders_with_knowl_links_and_math(self) -> None:
        target = self.make_knowl()
        rendered = compiler.render_markdown(
            "| Structure | Relation |\n"
            "| --- | --- |\n"
            "| [[sample/concept|Sample]] | A map $M\\to N$. |",
            {target.id: target},
        )
        self.assertIn("<div class=\"table-scroll\"><table>", rendered)
        self.assertEqual(rendered.count("<th>"), 2)
        self.assertEqual(rendered.count("<td>"), 2)
        self.assertIn("class=\"knowl\"", rendered)
        self.assertIn(">Sample</a>", rendered)
        self.assertIn("class=\"math-inline math-katex\"", rendered)
        self.assertNotIn("<p>|", rendered)

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

    def test_authored_prerequisites_are_validated_and_exported_for_learning_order(self) -> None:
        foundation = self.make_knowl()
        foundation.id = "sample/foundation"
        foundation.title = "Foundation"
        dependent = self.make_knowl()
        dependent.id = "sample/dependent"
        dependent.title = "Dependent"
        dependent.prerequisites = [foundation.id]
        registry = {foundation.id: foundation, dependent.id: dependent}

        errors = [message for message in compiler.validate(registry) if message.severity == "error"]
        self.assertEqual(errors, [])
        self.assertEqual(compiler.registry_json(registry)[dependent.id]["prerequisites"], [foundation.id])
        self.assertIn(
            {
                "source": foundation.id,
                "target": dependent.id,
                "type": "prerequisite",
                "authored": True,
                "dependency_review_count": 0,
                "reviewed": False,
                "provenance": "authored",
            },
            compiler.dependency_graph_json(registry)["edges"],
        )
        self.assertIn(
            {
                "source": dependent.id,
                "source_part": "metadata.prerequisites",
                "type": "prerequisite",
                "target": foundation.id,
            },
            compiler.collect_links(dependent),
        )

    def test_prerequisite_cycles_are_rejected_without_treating_wikilinks_as_dependencies(self) -> None:
        first = self.make_knowl()
        first.id = "sample/first"
        second = self.make_knowl()
        second.id = "sample/second"
        first.prerequisites = [second.id]
        second.prerequisites = [first.id]
        messages = compiler.validate({first.id: first, second.id: second})
        self.assertTrue(any("prerequisite cycle" in message.message for message in messages))

    def test_homepage_and_complete_index_have_distinct_jobs(self) -> None:
        knowl = self.make_knowl()
        knowl.id = "analysis"
        knowl.title = "Analysis"
        registry = {knowl.id: knowl}
        package = {"title": "Knowlpedia"}
        homepage = compiler.render_homepage(registry, package)
        index = compiler.render_index(registry, package)
        graph = compiler.render_graph_page(registry, package)
        self.assertIn('<h1 id="home-title">Knowlpedia</h1>', homepage)
        self.assertIn('href="/index/"', homepage)
        self.assertIn('href="/graph/"', homepage)
        self.assertNotIn('class="index-section"', homepage)
        self.assertIn("Mathematical knowledge, connected", index)
        self.assertIn("Browse all 1 knowls by subject", index)
        self.assertNotIn("production knowls", index)
        self.assertIn("Open a definition without losing your place", index)
        self.assertIn('id="subject-filter"', index)
        self.assertNotIn("The Knowlpedia library", index)
        self.assertNotIn('class="library-breadcrumb"', index)
        self.assertNotIn('class="hero-search"', index)
        self.assertNotIn('class="index-intro"', index)
        self.assertIn('class="index-section"', index)
        self.assertIn('data-dependency-graph', graph)
        self.assertIn('id="graph-orientation"', graph)
        self.assertRegex(graph, r'/assets/graph\.js\?v=[0-9a-f]{12}')
        self.assertRegex(homepage, r'/assets/knowl\.css\?v=[0-9a-f]{12}')

    def test_meta_subjects_are_excluded_from_reader_directories(self) -> None:
        registry = {}
        for knowl_id in ("analysis/concept", "knowlification/batch", "posts/note", "search"):
            knowl = self.make_knowl()
            knowl.id = knowl_id
            knowl.title = knowl_id
            registry[knowl_id] = knowl
        package = {"title": "Knowlpedia"}
        homepage = compiler.render_homepage(registry, package)
        index = compiler.render_index(registry, package)
        self.assertIn('subject-analysis', homepage)
        self.assertIn('subject-analysis', index)
        for subject in ("knowlification", "posts", "search"):
            self.assertNotIn(f'subject-{subject}', homepage)
            self.assertNotIn(f'subject-{subject}', index)

    def test_large_knowl_index_uses_visible_lazy_loading_without_inline_templates(self) -> None:
        targets = {
            f"sample/target-{index}": compiler.Knowl(
                id=f"sample/target-{index}",
                title=f"Target {index}",
                kind="definition",
                summary="A target.",
                aliases=[],
                domains=["sample"],
                source_path=Path(f"target-{index}.knowl.md"),
                core_markdown="A target definition.",
            )
            for index in range(2)
        }
        index_knowl = compiler.Knowl(
            id="sample/index",
            title="Sample index",
            kind="knowl",
            summary="An index.",
            aliases=[],
            domains=["sample"],
            source_path=Path("index.knowl.md"),
            core_markdown=" ".join(f"[[{target}|Open]]" for target in targets),
        )
        registry = {index_knowl.id: index_knowl, **targets}
        with patch.object(compiler, "INLINE_PRELOAD_TEMPLATE_LIMIT", 1):
            rendered = compiler.render_page(index_knowl, registry, {"title": "Knowlpedia"})
        self.assertIn('data-knowl-preload="visible"', rendered)
        self.assertEqual(rendered.count('class="knowl"'), 2)
        self.assertNotIn("<template data-knowl-fragment=", rendered)


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
