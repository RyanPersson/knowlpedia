from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from test_compiler import compiler, write_knowl, write_package
from test_compose_content import composer
from test_check_rendering_errors import checker


class PrivateLibraryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.public = self.root / "public-package"
        self.public.mkdir()
        write_package(self.public)
        write_knowl(self.public / "content/group.knowl.md", "sample/group", "Group")
        write_knowl(self.public / "content/set.knowl.md", "sample/set", "Set")
        group = self.public / "content/group.knowl.md"
        group.write_text(group.read_text() + "\n\nA [[sample/set|set]] with an operation.\n")
        self.private = self.root / "private-package"
        (self.private / "documents").mkdir(parents=True)
        (self.private / "knowlpack.toml").write_text('id="private"\ntitle="Private"\nprivate=true\ncontent_dir="documents"\n')
        self.document = self.private / "documents/reading.knowl.md"
        self.document.write_text(
            '+++\nid="documents/reading"\ntitle="PRIVATE_TITLE_SENTINEL"\nkind="document"\n'
            'summary="Private fixture"\nsection_mode="continuous"\n+++\n\n'
            '# Original heading\n\nPRIVATE_BODY_SENTINEL. A [[sample/group|group]].\n\n## Later heading\n\nUnchanged words.\n'
        )
        (self.private / "docs").mkdir()
        (self.private / "docs/source.pdf").write_bytes(b"RAW_PDF_SENTINEL")
        self.output = self.root / "site"

    def test_development_library_links_documents_to_nested_public_fragments(self):
        original = self.document.read_bytes()
        self.assertEqual(compiler.write_site(self.public, self.output, private_package=self.private), 0)
        library = (self.output / "library/index.html").read_text()
        self.assertIn('href="/documents/reading/"', library)
        self.assertIn('id="docs-open"', library)
        self.assertTrue((self.output / "docs/index.html").exists())
        page = (self.output / "documents/reading/index.html").read_text()
        self.assertIn('data-knowl-visibility="private"', page)
        self.assertIn('data-knowl="/fragments/sample/group/core.html"', page)
        self.assertIn('<h2>Later heading</h2>', page)
        self.assertNotIn('<details class="knowl-section"', page)
        group = (self.output / "fragments/sample/group/core.html").read_text()
        self.assertIn('data-knowl="/fragments/sample/set/core.html"', group)
        self.assertEqual(self.document.read_bytes(), original)
        self.assertNotIn('PRIVATE_TITLE_SENTINEL', (self.output / "index/index.html").read_text())
        self.assertFalse(any(path.suffix == ".pdf" for path in self.output.rglob("*")))

    def test_production_rebuild_removes_private_text_routes_and_indexes(self):
        compiler.write_site(self.public, self.output, private_package=self.private)
        result = compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES["production"])
        self.assertEqual(result, 0)
        for route in ["docs", "library", "documents", "fragments/documents"]:
            self.assertFalse((self.output / route).exists(), route)
        for path in self.output.rglob("*"):
            if path.is_file() and path.suffix in {".html", ".json"}:
                text = path.read_text()
                self.assertNotIn("PRIVATE_", text, str(path))
                self.assertNotIn("documents/reading", text, str(path))
                self.assertNotIn('id="library-open"', text, str(path))
        self.assertEqual(checker.check_build_profile(self.output, "production"), [])

    def test_production_refuses_private_input_and_malformed_private_files(self):
        self.document.write_text("not valid TOML")
        with self.assertRaisesRegex(ValueError, "only available in development"):
            compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES["production"], private_package=self.private)
        self.assertFalse(self.output.exists())
        self.assertEqual(compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES["production"]), 0)

    def test_private_package_cannot_be_promoted_through_composition_or_primary_input(self):
        for primary, contributors in [(self.public, [self.private]), (self.private, [])]:
            with self.subTest(primary=primary):
                with self.assertRaisesRegex(ValueError, "Private packages"):
                    composer.compose(primary, contributors, self.root / "composed")
        with self.assertRaisesRegex(ValueError, "Private packages"):
            compiler.write_site(self.private, self.output, profile=compiler.BUILD_PROFILES["production"])

    def test_reserved_document_ids_cannot_be_published_from_public_corpus(self):
        write_knowl(self.public / "content/copied.knowl.md", "documents/copied", "Copied")
        with self.assertRaisesRegex(ValueError, "Reserved development route"):
            compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES["production"])

    def test_private_document_ids_cannot_escape_their_namespace(self):
        self.document.write_text(self.document.read_text().replace('documents/reading', 'documents/../../index'))
        with self.assertRaisesRegex(ValueError, "under documents/"):
            compiler.write_site(self.public, self.output, private_package=self.private)
        self.assertFalse(self.output.exists())

    def test_production_checker_catches_leftover_private_artifacts(self):
        compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES["production"])
        (self.output / "fragments/documents").mkdir(parents=True)
        (self.output / "fragments/documents/leak.html").write_text("PRIVATE_LEAK")
        issues = checker.check_build_profile(self.output, "production")
        self.assertTrue(any(issue.file == "fragments/documents" for issue in issues))

    def test_empty_cache_still_has_a_usable_library(self):
        self.document.unlink()
        compiler.write_site(self.public, self.output, private_package=self.private)
        self.assertIn('class="library-empty"', (self.output / "library/index.html").read_text())
        report = json.loads((self.output / "reports/build.json").read_text())
        self.assertEqual(report["private_document_ids"], [])

    def test_production_checker_catches_private_json_without_a_private_page(self):
        compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES["production"])
        (self.output / "indexes/search.json").write_text('[{"id":"documents/reading","title":"PRIVATE_TITLE"}]')
        issues = checker.check_build_profile(self.output, "production")
        self.assertTrue(any(issue.kind == "private_index_in_production" for issue in issues))


if __name__ == "__main__":
    unittest.main()
