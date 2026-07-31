from pathlib import Path
import tempfile
import unittest

from scripts import audit_external_links as audit


class ExternalLinkAuditTests(unittest.TestCase):
    def write_knowl(self, body: str) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "sample.knowl.md"
        path.write_text(
            "+++\n"
            'id = "sample"\n'
            'title = "Sample"\n'
            'kind = "definition"\n'
            'summary = "Sample."\n'
            'source_url = "https://metadata.example/source"\n'
            "+++\n\n"
            + body,
            encoding="utf-8",
        )
        return path

    def test_flags_external_markdown_link_outside_references(self) -> None:
        path = self.write_knowl(
            "A statement [Book, Chapter 1](https://example.com/book).\n\n"
            "## References\n\n"
            "1. [Book record](https://example.com/book).\n"
        )
        violations = audit.audit_path(path)
        self.assertEqual(len(violations), 1)
        self.assertIn("Book, Chapter 1", violations[0].text)

    def test_reference_links_and_front_matter_urls_are_allowed(self) -> None:
        path = self.write_knowl(
            "A statement.\n\n"
            "## References\n\n"
            "1. [Book record](https://example.com/book).\n"
        )
        self.assertEqual(audit.audit_path(path), [])

    def test_fix_preserves_label_and_reference_destination(self) -> None:
        path = self.write_knowl(
            "See [Book, Chapter 1](https://example.com/book).\n\n"
            "## Reference\n\n"
            "1. [Book record](https://example.com/book).\n"
        )
        self.assertEqual(audit.fix_path(path), 1)
        fixed = path.read_text(encoding="utf-8")
        self.assertIn("See [Book, Chapter 1].", fixed)
        self.assertIn("## References", fixed)
        self.assertIn("[Book record](https://example.com/book)", fixed)
        self.assertEqual(audit.audit_path(path), [])

    def test_multiline_label_and_parenthesized_url(self) -> None:
        path = self.write_knowl(
            "See [Author,\n"
            "Chapter 2](https://example.com/item(2026)).\n\n"
            "## References\n\n"
            "1. [Record](https://example.com/item(2026)).\n"
        )
        links = audit.external_links_outside_references(
            audit.split_front_matter(path.read_text(encoding="utf-8"))[1]
        )
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0].destination, "https://example.com/item(2026)")
        audit.fix_path(path)
        self.assertIn(
            "See [Author,\nChapter 2].",
            path.read_text(encoding="utf-8"),
        )

    def test_flags_bare_external_url(self) -> None:
        path = self.write_knowl("See https://example.com/resource.\n")
        violations = audit.audit_path(path)
        self.assertEqual(len(violations), 1)


if __name__ == "__main__":
    unittest.main()
