from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "packages" / "compiler" / "knowl_compile.py"
SPEC = importlib.util.spec_from_file_location("knowl_compile_seo", MODULE_PATH)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)
seo = compiler.seo


def knowl(**overrides):
    values = {
        "id": "algebra-modules/module",
        "title": "Module",
        "kind": "knowl",
        "summary": "An abelian group with a scalar action.",
        "aliases": [],
        "domains": [],
        "source_path": Path("module.knowl.md"),
        "core_markdown": "Body.",
    }
    return compiler.Knowl(**{**values, **overrides})


def head_schema(head: str) -> dict:
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', head)
    assert match
    return json.loads(match.group(1))


class PlainTextTests(unittest.TestCase):
    def test_flattens_links_markdown_and_math(self):
        text = r"A **left** [[algebra-rings/ring|ring]] over \(\mathbb{Z}\) see [notes](https://example.com)."
        self.assertEqual(seo.plain_text(text), "A left ring over ℤ see notes.")

    def test_converts_title_math(self):
        self.assertEqual(seo.plain_text(r"\(L\)-packet"), "L-packet")
        self.assertEqual(seo.plain_text(r"Root \(\mathfrak{sl}_2\)-subalgebra"), "Root sl₂-subalgebra")
        self.assertEqual(seo.plain_text(r"\(\overline{\mathbb Q}\)"), "ℚ̅")
        self.assertEqual(seo.plain_text(r"\(G\hookrightarrow H\)"), "G↪ H")

    def test_truncates_at_word_boundary(self):
        result = seo.truncate("word " * 60)
        self.assertLessEqual(len(result), seo.DESCRIPTION_LIMIT)
        self.assertTrue(result.endswith("word…"))


class TitleTests(unittest.TestCase):
    def full(self, item, subject="algebra-modules", label="Modules"):
        return seo.knowl_head(item, "/x/", subject, label)[0]

    def test_generic_knowl_is_a_definition(self):
        self.assertEqual(self.full(knowl()), "Module (abstract algebra): definition | Knowlpedia")

    def test_generic_knowl_naming_a_result_is_not_called_a_definition(self):
        self.assertEqual(self.full(knowl(title="Nakayama's lemma")), "Nakayama's lemma (abstract algebra) | Knowlpedia")
        self.assertEqual(
            self.full(knowl(title="Separable polynomials have distinct roots")),
            "Separable polynomials have distinct roots (abstract algebra) | Knowlpedia",
        )

    def test_explicit_kind_replaces_definition_unless_title_says_it(self):
        self.assertEqual(self.full(knowl(title="Five lemma", kind="lemma")), "Five lemma (abstract algebra) | Knowlpedia")
        self.assertEqual(self.full(knowl(title="Snake", kind="lemma")), "Snake (abstract algebra): lemma | Knowlpedia")

    def test_learning_path(self):
        item = knowl(id="posts/modules", title="Modules", kind="page", learning_path=True)
        self.assertEqual(self.full(item, "posts", "Long-form documents"), "Modules: learning path | Knowlpedia")

    def test_subject_page_has_its_own_format(self):
        item = knowl(id="algebra-commutative", title="Algebra: Commutative Algebra", kind="section")
        self.assertEqual(
            self.full(item, "algebra-commutative", "Commutative algebra"),
            "Commutative algebra: definitions and theorems | Knowlpedia",
        )

    def test_subject_page_name_overrides_an_awkward_label(self):
        item = knowl(id="analysis", title="Analysis", kind="section")
        self.assertEqual(
            self.full(item, "analysis", "Analysis: geometric and quantitative tools"),
            "Analysis: definitions and theorems | Knowlpedia",
        )

    def test_landing_page_that_is_not_a_subject_uses_its_title(self):
        item = knowl(id="shale-paper", title="Shale's Paper", kind="section")
        self.assertEqual(self.full(item, "shale-paper", "Shale's paper"), "Shale's Paper | Knowlpedia")

    def test_sub_index_page_keeps_the_subject_qualifier(self):
        item = knowl(id="ergodic-theory/examples-index", title="Examples", kind="index")
        self.assertEqual(self.full(item, "ergodic-theory", "Ergodic theory"), "Examples (ergodic theory) | Knowlpedia")

    def test_title_matching_its_subject_is_not_repeated(self):
        item = knowl(id="algebra-category-theory/index", title="Category Theory", kind="index")
        self.assertEqual(self.full(item, "algebra-category-theory", "Category theory"), "Category Theory | Knowlpedia")

    def test_subject_falls_back_to_index_label(self):
        self.assertEqual(seo.subject_qualifier("measure-theory", "Measure theory"), "measure theory")


class AliasTests(unittest.TestCase):
    def test_drops_slugs_restatements_and_plurals(self):
        item = knowl(
            title="Cusp form",
            aliases=["cusp form", "cusp forms", "cusp-form-page", "a/b", "cuspidal modular form", "Cuspidal modular form"],
        )
        self.assertEqual(seo.display_aliases(item), ["cuspidal modular form"])


class SchemaTests(unittest.TestCase):
    def test_definition_uses_defined_term_and_breadcrumbs(self):
        item = knowl(aliases=["R-module structure"])
        _, head = seo.knowl_head(item, "/algebra-modules/module/", "algebra-modules", "Modules")
        entity, crumbs = head_schema(head)["@graph"]
        self.assertEqual(entity["@type"], "DefinedTerm")
        self.assertEqual(entity["alternateName"], ["R-module structure"])
        self.assertEqual(entity["inDefinedTermSet"]["url"], "https://knowlpedia.com/index/#subject-algebra-modules")
        self.assertEqual(crumbs["itemListElement"][-1], {"@type": "ListItem", "position": 3, "name": "Module"})

    def test_alternate_name_is_omitted_without_aliases(self):
        _, head = seo.knowl_head(knowl(aliases=["module"]), "/m/", "algebra-modules", "Modules")
        self.assertNotIn("alternateName", head_schema(head)["@graph"][0])

    def test_theorem_uses_article(self):
        _, head = seo.knowl_head(knowl(title="Ado's theorem", kind="theorem"), "/a/", "lie-groups", "Lie groups")
        self.assertEqual(head_schema(head)["@graph"][0]["@type"], "Article")

    def test_json_ld_cannot_close_its_script_tag(self):
        _, head = seo.knowl_head(knowl(summary="x </script> y"), "/a/", "s", "S")
        self.assertNotIn("</script> y", head)
        self.assertEqual(head_schema(head)["@graph"][0]["description"], "x </script> y")

    def test_head_tags_are_attribute_escaped(self):
        _, head = seo.knowl_head(knowl(summary='A "quoted" & <odd> term'), "/a/", "s", "S")
        self.assertIn('<meta name="description" content="A &quot;quoted&quot; &amp; &lt;odd&gt; term">', head)
        self.assertIn('<link rel="alternate" type="text/markdown" href="https://knowlpedia.com/a/index.md">', head)


class MarkdownTests(unittest.TestCase):
    @staticmethod
    def resolve(target):
        base = target.split("#", 1)[0]
        if base == "private/note":
            return None
        return f"https://knowlpedia.com/{base}/" + (f"#{target.split('#', 1)[1]}" if "#" in target else "")

    def test_links_go_to_canonical_html_and_math_is_preserved(self):
        text = r"See [[a/b|the ring]], [[a/c#section.x|part]], [cat](/catalog/), [web](https://e.org), and \(R[[x]]\)."
        self.assertEqual(
            seo.rewrite_links(text, self.resolve),
            r"See [the ring](https://knowlpedia.com/a/b/), [part](https://knowlpedia.com/a/c/#section.x), "
            r"[cat](https://knowlpedia.com/catalog/), [web](https://e.org), and \(R[[x]]\).",
        )

    def test_unpublished_targets_become_plain_labels(self):
        self.assertEqual(seo.rewrite_links("[[private/note|secret]]", self.resolve), "secret")

    def test_code_blocks_are_untouched(self):
        text = "```\n[[a/b|x]]\n```\n\nand `[[a/b]]`"
        self.assertEqual(seo.rewrite_links(text, self.resolve), text)

    def test_title_links_are_rewritten(self):
        item = knowl(title="Operator on a [[a/b|Hilbert space]]", core_markdown="")
        self.assertIn("# Operator on a [Hilbert space](https://knowlpedia.com/a/b/)\n", seo.markdown_document(item, "/x/", "", self.resolve))

    def test_document_starts_with_canonical_line(self):
        item = knowl(sections=[{"id": "examples", "title": "Examples", "kind": "markdown", "markdown": "An example."}])
        document = seo.markdown_document(item, "/algebra-modules/module/", item.core_markdown, self.resolve)
        self.assertTrue(document.startswith("Canonical: https://knowlpedia.com/algebra-modules/module/\n\n# Module\n"))
        self.assertIn("## Examples\n\nAn example.", document)


class DescriptionTests(unittest.TestCase):
    def test_uses_the_summary(self):
        self.assertEqual(seo.page_description(knowl()), "An abelian group with a scalar action.")

    def test_summary_restating_the_title_falls_back_to_the_first_paragraph(self):
        item = knowl(title="Notes", summary="Notes", core_markdown="## Heading\n\nThe real **intro** paragraph.\n\nMore.")
        self.assertEqual(seo.page_description(item), "The real intro paragraph.")

    def test_keeps_the_title_when_there_is_nothing_else(self):
        self.assertEqual(seo.page_description(knowl(title="Notes", summary="Notes", core_markdown="")), "Notes")


class SiteOutputTests(unittest.TestCase):
    def build(self, root: Path, private: bool = False) -> Path:
        package = root / "package"
        (package / "content" / "group").mkdir(parents=True)
        (package / "testing").mkdir()
        (package / "knowlpack.toml").write_text(
            'id = "t"\ntitle = "Knowlpedia"\nversion = "0"\nauthors = ["a"]\nlicense = "x"\n'
            'content_dir = "content"\ndevelopment_content_dirs = ["testing"]\n',
            encoding="utf-8",
        )

        def write(path: Path, knowl_id: str, title: str, body: str) -> None:
            path.write_text(
                f'+++\nid = "{knowl_id}"\ntitle = "{title}"\nkind = "definition"\nsummary = "About {title}."\n+++\n\n{body}\n',
                encoding="utf-8",
            )

        long_body = "First sentence. Second sentence. Third sentence with [[group/stub|a link]]."
        write(package / "content" / "group" / "full.knowl.md", "group/full", "Full", long_body)
        write(package / "content" / "group" / "stub.knowl.md", "group/stub", "Stub", "Only one sentence.")
        write(package / "testing" / "draft.knowl.md", "testing-area/draft", "Draft", long_body)
        out = root / "out"
        profile = compiler.BUILD_PROFILES["development"]
        self.assertEqual(compiler.write_site(package, out, profile=profile), 0)
        return out

    def test_discovery_files_cover_only_public_pages(self):
        with tempfile.TemporaryDirectory() as temporary:
            out = self.build(Path(temporary))
            self.assertIn("Allow: /", (out / "robots.txt").read_text(encoding="utf-8"))
            namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            locations = {
                node.text for node in ET.parse(out / "sitemap.xml").getroot().findall("s:url/s:loc", namespace)
            }
            self.assertIn("https://knowlpedia.com/group/full/", locations)
            self.assertIn("https://knowlpedia.com/", locations)
            self.assertIn("https://knowlpedia.com/group/stub/", locations)
            self.assertFalse(any("draft" in location or location.endswith(".md") for location in locations))
            llms = (out / "llms.txt").read_text(encoding="utf-8")
            self.assertTrue(llms.startswith("# Knowlpedia\n\n> A linked library of 2 "))
            self.assertIn("(https://knowlpedia.com/index/#subject-group): 2 knowls", llms)
            self.assertNotIn("Draft", llms)

    def test_public_pages_get_metadata_and_markdown_but_testing_pages_do_not(self):
        with tempfile.TemporaryDirectory() as temporary:
            out = self.build(Path(temporary))
            page = (out / "group" / "full" / "index.html").read_text(encoding="utf-8")
            self.assertIn('<link rel="canonical" href="https://knowlpedia.com/group/full/">', page)
            markdown = (out / "group" / "full" / "index.md").read_text(encoding="utf-8")
            self.assertIn("[a link](https://knowlpedia.com/group/stub/)", markdown)
            self.assertNotIn("index.md", markdown)
            draft = (out / "testing-area" / "draft" / "index.html").read_text(encoding="utf-8")
            self.assertNotIn('rel="canonical"', draft)
            self.assertFalse((out / "testing-area" / "draft" / "index.md").exists())


if __name__ == "__main__":
    unittest.main()
