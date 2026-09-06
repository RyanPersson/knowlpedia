import subprocess
import tempfile
import unittest
import json
from pathlib import Path

from scripts.generate_content_review import (
    ReviewItem,
    added_knowl_paths,
    build_diff_plan,
    changed_character_count,
    modified_knowl_paths,
    parse_text,
    render_index,
    render_complete_knowl,
    render_item_page,
    write_diff_plan,
    write_patch_chunks,
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
            self.assertEqual(
                added_knowl_paths(repo, "baseline", "HEAD"),
                ["content/added.knowl.md"],
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

    def test_added_knowl_renders_alone_with_collapsed_diff(self) -> None:
        current_text = """+++
id = "test/new"
title = "New knowl"
kind = "definition"
summary = "New summary"
aliases = []
domains = ["test"]
+++

New definition.
"""
        current_knowl = parse_text(current_text, "current")
        item = ReviewItem(
            index=0,
            path="content/test/new.knowl.md",
            old_text="",
            current_text=current_text,
            old_knowl=None,
            current_knowl=current_knowl,
            filename="0001-test-new.html",
            change_kind="added",
        )

        page = render_item_page(item, {current_knowl.id: current_knowl}, 1)

        self.assertIn('<details class="source-diff">', page)
        self.assertNotIn('<details class="source-diff" open>', page)
        self.assertIn('class="comparison comparison-added"', page)
        self.assertNotIn('aria-label="Baseline version"', page)

    def test_index_can_toggle_added_knowls(self) -> None:
        text = """+++
id = "test/new"
title = "New knowl"
kind = "definition"
summary = "New summary"
aliases = []
domains = ["test"]
+++

New definition.
"""
        knowl = parse_text(text, "current")
        item = ReviewItem(
            index=0,
            path="content/test/new.knowl.md",
            old_text="",
            current_text=text,
            old_knowl=None,
            current_knowl=knowl,
            filename="0001-test-new.html",
            change_kind="added",
        )

        page = render_index([item], "abc123")

        self.assertIn('id="review-include-added" type="checkbox" checked', page)
        self.assertIn('data-change-kind="added"', page)
        self.assertIn("new knowl ·", page)

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
        larger_item = ReviewItem(
            index=1,
            path="content/test/larger.knowl.md",
            old_text=old_text,
            current_text=old_text + ("x" * 20),
            old_knowl=old_knowl,
            current_knowl=current_knowl,
            filename="0002-test-larger.html",
        )

        page = render_index([item, larger_item], "abc123")

        self.assertIn('<select id="review-sort">', page)
        self.assertIn(
            '<option value="largest" selected>Largest diff first</option>',
            page,
        )
        self.assertIn('data-diff-length="6"', page)
        self.assertLess(
            page.index("items/0002-test-larger.html"),
            page.index("items/0001-test-example.html"),
        )
        self.assertIn('src="items/0002-test-larger.html"', page)

    def test_diff_plan_is_ranked_and_balanced_by_changed_characters(self) -> None:
        comparisons = [
            ("content/large.knowl.md", "", "a" * 10),
            ("content/medium.knowl.md", "", "b" * 6),
            ("content/small.knowl.md", "", "c" * 4),
        ]

        plan = build_diff_plan(comparisons, 2)

        self.assertEqual([item.path for item in plan], [
            "content/large.knowl.md",
            "content/medium.knowl.md",
            "content/small.knowl.md",
        ])
        self.assertEqual([item.changed_characters for item in plan], [10, 6, 4])
        self.assertEqual([item.chunk for item in plan], [1, 2, 2])

    def test_diff_plan_writes_json_lines(self) -> None:
        plan = build_diff_plan([("content/example.knowl.md", "a", "ab")], 1)
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "plan.jsonl"

            write_diff_plan(plan, destination, baseline="develop", proposed="feature")

            record = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(record, {
                "baseline": "develop",
                "changed_characters": 1,
                "chunk": 1,
                "path": "content/example.knowl.md",
                "proposed": "feature",
                "rank": 1,
                "review_direction": "baseline_to_proposed",
            })

    def test_patch_chunks_use_standard_git_diff_polarity(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo"
            repo.mkdir()
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test User")
            self.git(repo, "config", "user.email", "test@example.com")
            content = repo / "content"
            content.mkdir()
            source = content / "example.knowl.md"
            source.write_text("baseline\n", encoding="utf-8")
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "baseline")
            self.git(repo, "branch", "baseline")
            source.write_text("proposed\n", encoding="utf-8")
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "proposed")
            plan = build_diff_plan(
                [("content/example.knowl.md", "baseline\n", "proposed\n")],
                1,
            )

            paths = write_patch_chunks(
                repo,
                plan,
                Path(temp) / "patches",
                "baseline",
                "HEAD",
            )

            patch = paths[0].read_text(encoding="utf-8")
            self.assertIn("diff --git a/content/example.knowl.md b/content/example.knowl.md", patch)
            self.assertIn("--- a/content/example.knowl.md", patch)
            self.assertIn("+++ b/content/example.knowl.md", patch)
            self.assertIn("-baseline", patch)
            self.assertIn("+proposed", patch)

    def test_redirect_comparison_displays_canonical_mathematics(self):
        old = parse_text('+++\nid="old"\ntitle="Old"\nkind="definition"\nsummary="Moved"\nredirect_to="new"\n+++\n', "old")
        new = parse_text('+++\nid="new"\ntitle="New"\nkind="definition"\nsummary="Canonical"\n+++\nCanonical mathematical content.', "new")
        rendered = render_complete_knowl(old, {"old": old, "new": new})
        self.assertIn("Consolidated into", rendered)
        self.assertIn("Canonical mathematical content", rendered)


if __name__ == "__main__":
    unittest.main()
