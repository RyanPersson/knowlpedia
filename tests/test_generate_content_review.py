import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.generate_content_review import (
    ReviewItem,
    changed_character_count,
    modified_knowl_paths,
    parse_text,
    render_index,
    render_item_page,
)


class GenerateContentReviewTests(unittest.TestCase):
    def git(self, repo: Path, *args: str) -> None:
        subprocess.run(
            ["git", *args],
            cwd=repo,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def test_ref_comparison_selects_only_modified_existing_knowls(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test User")
            self.git(repo, "config", "user.email", "test@example.com")
            content = repo / "content"
            content.mkdir()
            existing = content / "existing.knowl.md"
            existing.write_text("old\n", encoding="utf-8")
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "baseline")
            self.git(repo, "branch", "baseline")

            existing.write_text("new\n", encoding="utf-8")
            (content / "added.knowl.md").write_text("added\n", encoding="utf-8")
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "changes")

            self.assertEqual(
                modified_knowl_paths(repo, "baseline", "HEAD"),
                ["content/existing.knowl.md"],
            )

    def test_source_diff_is_open_and_precedes_rendered_comparison(self) -> None:
        old_text = """+++
id = "test/example"
title = "Example"
kind = "definition"
summary = "Old summary"
aliases = []
domains = ["test"]
+++

Old definition.
"""
        current_text = old_text.replace("Old definition", "New definition")
        old_knowl = parse_text(old_text, "old")
        current_knowl = parse_text(current_text, "current")
        item = ReviewItem(
            index=0,
            path="content/test/example.knowl.md",
            old_text=old_text,
            current_text=current_text,
            old_knowl=old_knowl,
            current_knowl=current_knowl,
            filename="0001-test-example.html",
        )

        page = render_item_page(item, {current_knowl.id: current_knowl}, 1)

        diff_position = page.index('<details class="source-diff" open>')
        comparison_position = page.index('<main class="comparison">')
        self.assertLess(diff_position, comparison_position)

    def test_changed_character_count_normalizes_math_delimiters(self) -> None:
        self.assertEqual(changed_character_count(r"Value: \(x\)", "Value: $x$"), 0)
        self.assertEqual(changed_character_count("abc", "axcde"), 4)

    def test_index_offers_diff_length_sorting(self) -> None:
        old_text = """+++
id = "test/example"
title = "Example"
kind = "definition"
summary = "Old summary"
aliases = []
domains = ["test"]
+++

Old definition.
"""
        current_text = old_text.replace("Old definition", "New definition")
        old_knowl = parse_text(old_text, "old")
        current_knowl = parse_text(current_text, "current")
        item = ReviewItem(
            index=0,
            path="content/test/example.knowl.md",
            old_text=old_text,
            current_text=current_text,
            old_knowl=old_knowl,
            current_knowl=current_knowl,
            filename="0001-test-example.html",
        )

        page = render_index([item], "abc123")

        self.assertIn('<select id="review-sort">', page)
        self.assertIn(
            '<option value="largest" selected>Largest diff first</option>',
            page,
        )
        self.assertIn('data-diff-length="6"', page)


if __name__ == "__main__":
    unittest.main()
