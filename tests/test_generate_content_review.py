import subprocess
import tempfile
import unittest
import json
import hashlib
from pathlib import Path

from scripts.generate_content_review import (
    ReviewItem,
    attach_review_notes,
    extract_ref,
    render_review_notes,
    write_review_notes,
    added_knowl_paths,
    build_diff_plan,
    build_ref_comparison,
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

    def note_item(self, change_kind="modified"):
        text = '+++\nid="test/item"\ntitle="Item"\nkind="definition"\nsummary="Example"\n+++\nBody.\n'
        knowl = parse_text(text, "test")
        return ReviewItem(0, "content/test/item.knowl.md", text, text,
                          knowl, None if change_kind == "deleted" else knowl,
                          "0001-item.html", change_kind=change_kind)

    def test_review_notes_distinguish_exact_source_from_other_versions(self):
        item = self.note_item()
        current = {"id": "test/item", "outcome": "corrected",
                   "source_sha256": hashlib.sha256(item.current_text.encode()).hexdigest(),
                   "evidence": "Add the missing hypothesis. <script>bad()</script>"}
        old = {**current, "source_sha256": "older-version", "evidence": "Earlier decision"}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            ledger = root / "reviews/dependency-structure/notes.json"
            ledger.parent.mkdir(parents=True)
            ledger.write_text(json.dumps({"reviews": [old, current],
                                          "triage_records": [{**current, "evidence": "Unreviewed triage"}]}))
            attach_review_notes([item], root, "pinned-commit")
            write_review_notes([item], root / "output")
            page = render_item_page(item, {item.current_knowl.id: item.current_knowl}, 1)
            self.assertLess(page.index('id="review-reasons-heading"'), page.index('<details class="source-diff"'))
            self.assertIn("Notes matching the displayed proposed source", page)
            self.assertIn('class="review-note-history"><summary>', page)
            self.assertIn("Earlier decision", page)
            self.assertNotIn("Unreviewed triage", page)
            self.assertNotIn("<script>bad()</script>", page)
            self.assertIn("&lt;script&gt;bad()&lt;/script&gt;", page)
            exported = json.loads((root / "output/notes/0001-item.json").read_text())
            self.assertEqual(exported["ledger_revision"], "pinned-commit")
            self.assertEqual([r["matches_displayed_source"] for r in exported["records"]], [False, True])
            self.assertEqual(exported["records"][1]["record"], current)
            self.assertEqual(exported['comparison']['baseline_source'], item.old_text)
            self.assertEqual(exported['comparison']['proposed_source'], item.current_text)
            self.assertIn('Message about this diff', page)
            self.assertIn(item.context_hash, page)
            self.assertEqual(item.context_hash, hashlib.sha256((root / 'output/notes/0001-item.json').read_bytes()).hexdigest())

    def test_missing_or_historical_notes_do_not_claim_current_verification(self):
        item = self.note_item()
        self.assertIn("No justification was recorded", render_review_notes(item, {}))
        item.review_notes = [{"ledger": "reviews/old.json", "record_index": 0,
                              "record": {"source_sha256": "old", "evidence": "Earlier reason"}}]
        rendered = render_review_notes(item, {})
        self.assertIn("No saved note matches this exact source revision", rendered)
        self.assertIn('class="review-note-history" open>', rendered)
        self.assertNotIn("Notes matching the displayed", rendered)

    def test_canonical_batch_notes_keep_scope_provenance_and_structured_evidence(self):
        item = self.note_item()
        reference = {"url": "https://example.com/source", "title": "A source <title>", "locator": "Section 2 & 3"}
        current = {
            "id": "test/item", "scope": "targeted", "outcome": "new",
            "source_sha256": hashlib.sha256(item.current_text.encode()).hexdigest(),
            "evidence": {"method": "Checked the stated scalar convention. <script>bad()</script>", "references": [reference]},
            "references": [reference],
        }
        historical = {**current, "source_sha256": "different-source", "evidence": "Earlier bounded check."}
        triage = {**current, "evidence": "Unreviewed triage must stay out."}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            ledger = root / "reviews/refactor-ledger.json"
            ledger.parent.mkdir()
            ledger.write_text(json.dumps({
                "batches": [{"id": "catalog-arithmetic-targeted", "review_shard": "reviews/catalog/arithmetic.json",
                             "entries": [historical, current], "triage_records": [triage]}],
                "triage_records": [triage],
            }))
            shard = root / "reviews/catalog/arithmetic.json"
            shard.parent.mkdir()
            shard.write_text(json.dumps({"reviews": [current], "entries": [current]}))
            attach_review_notes([item], root, "pinned-catalogue-commit")
            self.assertEqual(len(item.review_notes), 2)
            rendered = render_review_notes(item, {})
            self.assertIn("Notes matching the displayed proposed source", rendered)
            self.assertIn("targeted check", rendered)
            self.assertIn("Checked the stated scalar convention.", rendered)
            self.assertIn("&lt;script&gt;bad()&lt;/script&gt;", rendered)
            self.assertNotIn("<script>bad()</script>", rendered)
            self.assertIn('href="https://example.com/source"', rendered)
            self.assertIn("A source &lt;title&gt;", rendered)
            self.assertIn("Section 2 &amp; 3", rendered)
            self.assertIn("batch catalog-arithmetic-targeted", rendered)
            self.assertIn("batches[0].entries[1]", rendered)
            self.assertNotIn("Unreviewed triage", rendered)
            # The same reference in two fields is rendered once per review.
            self.assertEqual(rendered.count("A source &lt;title&gt;"), 2)
            write_review_notes([item], root / "output")
            exported = json.loads((root / "output/notes/0001-item.json").read_text())
            self.assertEqual([row["matches_displayed_source"] for row in exported["records"]], [False, True])
            note = exported["records"][1]
            self.assertEqual(note["record"], current)
            self.assertEqual(note["ledger"], "reviews/refactor-ledger.json")
            self.assertEqual(note["batch_id"], "catalog-arithmetic-targeted")
            self.assertEqual(note["record_locator"], "batches[0].entries[1]")
            self.assertEqual(exported["ledger_revision"], "pinned-catalogue-commit")
            item.current_text += "An unreviewed edit.\n"
            self.assertNotIn("Notes matching the displayed proposed source", render_review_notes(item, {}))

    def test_deleted_knowl_notes_match_baseline(self):
        item = self.note_item("deleted")
        item.current_text = ""
        item.review_notes = [{"ledger": "reviews/old.json", "record_index": 0,
                              "record": {"source_sha256": hashlib.sha256(item.old_text.encode()).hexdigest(),
                                         "evidence": "Removal context"}}]
        self.assertIn("Notes matching the displayed baseline source", render_review_notes(item, {}))

    def test_canonical_targeted_claims_direct_reasoning_and_checked_sources_are_recorded(self):
        item = self.note_item()
        source_review = {
            "id": "test/item", "path": item.path, "scope": "targeted", "outcome": "new",
            "targeted_claims": "Definition core and stated convention; not a complete review.",
            "source_sha256": hashlib.sha256(item.current_text.encode()).hexdigest(),
            "sources": [{"url": "https://example.com/lecture.pdf", "locator": "Definition 1.1, §1.2",
                         "checked": "Checked the stated convention. <script>bad()</script>"}],
            "direct_reasoning": "", "prerequisites_reviewed": [],
        }
        direct_review = {**source_review, "targeted_claims": "", "sources": [],
                         "direct_reasoning": "The defining operations preserve the stated subset."}
        checked_only_review = {**source_review, "targeted_claims": ""}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            ledger = root / "reviews/refactor-ledger.json"
            ledger.parent.mkdir()
            ledger.write_text(json.dumps({"batches": [{
                "id": "transcript-connections-targeted", "entries": [source_review, direct_review, checked_only_review],
                "triage_records": [{**direct_review, "direct_reasoning": "Unreviewed triage"}],
            }]}))
            attach_review_notes([item], root, "pinned-transcript-commit")
            self.assertEqual(len(item.review_notes), 3)
            rendered = render_review_notes(item, {})
            self.assertIn("Notes matching the displayed proposed source", rendered)
            self.assertIn("Targeted claims:", rendered)
            self.assertIn("Definition core and stated convention; not a complete review.", rendered)
            self.assertIn("Recorded direct reasoning:", rendered)
            self.assertIn(direct_review["direct_reasoning"], rendered)
            self.assertIn("Recorded check:", rendered)
            self.assertIn("Definition 1.1, §1.2", rendered)
            self.assertIn("&lt;script&gt;bad()&lt;/script&gt;", rendered)
            self.assertNotIn("<script>bad()</script>", rendered)
            self.assertNotIn("Unreviewed triage", rendered)
            write_review_notes([item], root / "output")
            exported = json.loads((root / "output/notes/0001-item.json").read_text())
            self.assertTrue(all(row["matches_displayed_source"] for row in exported["records"]))
            self.assertEqual([row["record"] for row in exported["records"]],
                             [source_review, direct_review, checked_only_review])

    def test_ref_notes_come_from_compared_commit_not_worktree(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            repo = root / "repo"
            repo.mkdir()
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test User")
            self.git(repo, "config", "user.email", "test@example.com")
            item = self.note_item()
            source = repo / item.path
            source.parent.mkdir(parents=True)
            source.write_text(item.current_text)
            ledger = repo / "reviews/dependency-structure/notes.json"
            ledger.parent.mkdir(parents=True)
            record = {"id": "test/item", "source_sha256": hashlib.sha256(item.current_text.encode()).hexdigest(),
                      "evidence": "Committed explanation"}
            ledger.write_text(json.dumps({"reviews": [record]}))
            canonical = repo / "reviews/refactor-ledger.json"
            canonical_record = {**record, "scope": "targeted", "evidence": {"method": "Committed canonical explanation", "references": []}}
            canonical.write_text(json.dumps({"batches": [{"id": "canonical-batch", "entries": [canonical_record]}]}))
            self.git(repo, "add", ".")
            self.git(repo, "commit", "-m", "Reviewed version")
            ledger.write_text(json.dumps({"reviews": [{**record, "evidence": "Uncommitted replacement"}]}))
            canonical.write_text(json.dumps({"batches": [{"id": "uncommitted-batch", "entries": [
                {**canonical_record, "evidence": "Uncommitted canonical replacement"}]}]}))
            tree = root / "extracted"
            tree.mkdir()
            extract_ref(repo, "HEAD", tree)
            attach_review_notes([item], tree, "HEAD")
            self.assertEqual(item.review_notes[0]["record"]["evidence"], "Committed explanation")
            self.assertEqual(len(item.review_notes), 2)
            canonical_note = item.review_notes[1]
            self.assertEqual(canonical_note["ledger"], "reviews/refactor-ledger.json")
            self.assertEqual(canonical_note["batch_id"], "canonical-batch")
            self.assertEqual(canonical_note["record_locator"], "batches[0].entries[0]")
            self.assertEqual(canonical_note["record"], canonical_record)
            rendered = render_review_notes(item, {})
            self.assertIn("Committed canonical explanation", rendered)
            self.assertNotIn("Uncommitted", rendered)
            self.assertIn("Notes matching the displayed proposed source", rendered)

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

    def test_ref_comparison_manifest_limits_all_change_kinds_without_limiting_link_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            repo = root / "repo"
            repo.mkdir()
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test User")
            self.git(repo, "config", "user.email", "test@example.com")
            self.git(repo, "config", "diff.renames", "false")
            content = repo / "content"
            content.mkdir()

            def write(name: str, body: str) -> None:
                (content / f"{name}.knowl.md").write_text(
                    f'+++\nid = "test/{name}"\ntitle = "{name}"\nkind = "definition"\n'
                    f'summary = "Example {name}."\n+++\n{body}\n', encoding="utf-8",
                )

            for prefix in ("selected", "excluded"):
                write(f"{prefix}-modified", "Original definition.")
                write(f"{prefix}-deleted", "Definition to remove.")
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "baseline")
            self.git(repo, "branch", "baseline")
            for prefix in ("selected", "excluded"):
                write(f"{prefix}-modified", "Updated definition with [[test/excluded-added|a new prerequisite]].")
                write(f"{prefix}-added", "New definition.")
                (content / f"{prefix}-deleted.knowl.md").unlink()
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "changes")

            selected = {f"content/selected-{kind}.knowl.md": kind for kind in ("modified", "added", "deleted")}
            manifest = root / "paths.txt"
            manifest.write_text("\n" + "\n".join(f"  {path}  " for path in selected) + "\nREADME.md\n")
            empty_manifest = root / "empty-paths.txt"
            empty_manifest.write_text("\nREADME.md\n")
            all_changes = {f"content/{prefix}-{kind}.knowl.md": kind
                           for prefix in ("selected", "excluded") for kind in ("modified", "added", "deleted")}
            for name, paths_file, expected in (("filtered", manifest, selected), ("unfiltered", None, all_changes),
                                                ("empty", empty_manifest, {})):
                with self.subTest(manifest=name):
                    output = root / name
                    count = build_ref_comparison(repo, output, "baseline", "HEAD", paths_file,
                                                 "Before", "After", "Selected changes",
                                                 include_added=True, include_deleted=True)
                    notes = [json.loads(path.read_text()) for path in (output / "notes").glob("*.json")]
                    self.assertEqual(count, len(expected))
                    self.assertEqual({note["path"]: note["comparison"]["change_kind"] for note in notes}, expected)
                    self.assertEqual(len(list((output / "items").glob("*.html"))), len(expected))
            selected_page = next((root / "filtered" / "items").glob("*selected-modified.html")).read_text()
            self.assertIn('data-knowl="/fragments/test/excluded-added/core.html"', selected_page)
            self.assertNotIn("missing-knowl", selected_page)

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
