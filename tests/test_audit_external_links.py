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

    def test_fix_removes_body_citation_and_preserves_reference_destination(self) -> None:
        path = self.write_knowl(
            "See [Book, Chapter 1](https://example.com/book).\n\n"
            "## Reference\n\n"
            "1. [Book record](https://example.com/book).\n"
        )
        self.assertEqual(audit.fix_path(path), 1)
        fixed = path.read_text(encoding="utf-8")
        self.assertNotIn("Book, Chapter 1", fixed)
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
        self.assertNotIn("Author", path.read_text(encoding="utf-8"))

    def test_fix_removes_attribution_sentence_but_keeps_mathematics(self) -> None:
        path = self.write_knowl(
            "The map is injective. This criterion is developed in "
            "[Book, Chapter 2](https://example.com/book).\n\n"
            "A proper injective immersion is an embedding, a useful condition "
            "recorded in [Book, Chapter 3](https://example.com/book).\n\n"
            "## References\n\n"
            "1. [Book record](https://example.com/book).\n"
        )
        self.assertEqual(audit.fix_path(path), 2)
        fixed = path.read_text(encoding="utf-8")
        self.assertIn("The map is injective.", fixed)
        self.assertNotIn("This criterion", fixed)
        self.assertIn("A proper injective immersion is an embedding.", fixed)
        self.assertNotIn("recorded in", fixed)

    def test_flags_bare_external_url(self) -> None:
        path = self.write_knowl("See https://example.com/resource.\n")
        violations = audit.audit_path(path)
        self.assertEqual(len(violations), 1)

    def test_unmatched_mathematical_interval_does_not_absorb_reference_link(self) -> None:
        path = self.write_knowl(
            r"A map to \([0,\infty)\) is proper." "\n\n"
            "## References\n\n"
            "1. [Book record](https://example.com/book).\n"
        )
        self.assertEqual(audit.audit_path(path), [])
        audit.fix_path(path)
        fixed = path.read_text(encoding="utf-8")
        self.assertIn(r"\([0,\infty)\)", fixed)
        self.assertIn("[Book record](https://example.com/book)", fixed)

    def test_flags_plain_text_citation_outside_references(self) -> None:
        path = self.write_knowl(
            "A statement [Book, Chapter 1].\n\n"
            "## References\n\n"
            "1. [Book record](https://example.com/book).\n"
        )
        violations = audit.audit_path(path)
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].kind, "plain-text citation")

    def test_plain_text_citation_is_allowed_in_references(self) -> None:
        path = self.write_knowl(
            "A statement.\n\n"
            "## References\n\n"
            "1. [Book, Chapter 1].\n"
        )
        self.assertEqual(audit.audit_path(path), [])


if __name__ == "__main__":
    unittest.main()
