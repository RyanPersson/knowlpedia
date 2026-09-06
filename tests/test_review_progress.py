import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("review_progress", Path(__file__).parents[1] / "scripts/review_progress.py")
progress = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(progress)


class ReviewProgressTests(unittest.TestCase):
    def test_targeted_corrections_do_not_complete_review_and_new_nodes_do_not_shrink_backlog(self):
        baseline = {"a": {}, "b": {}, "c": {}}
        current = {"a": {"sha256": "a"}, "b": {"sha256": "b"}, "c": {"sha256": "c"}, "new": {"sha256": "n"}}
        ledger = {"baseline_content_ref": "base", "batches": [{"id": "one", "entries": [
            {"id": "a", "scope": "targeted", "outcome": "corrected"},
            {"id": "b", "scope": "full", "outcome": "reviewed_unchanged", "source_sha256": "b", "evidence": "Read the complete page."},
            {"id": "new", "scope": "full", "outcome": "new", "source_sha256": "n", "evidence": "Reviewed new theorem."},
        ]}]}
        stats = progress.summarize(ledger, baseline, current)
        self.assertEqual(stats["baseline_corrected"], 1)
        self.assertEqual(stats["baseline_fully_reviewed"], 1)
        self.assertEqual(stats["baseline_remaining"], 2)
        current["b"]["sha256"] = "edited"
        stats = progress.summarize(ledger, baseline, current)
        self.assertEqual(stats["baseline_remaining"], 3)
        self.assertEqual(stats["stale_full_reviews"], 1)

    def test_metadata_only_cannot_inflate_corrections(self):
        ledger = {"baseline_content_ref": "base", "batches": [{"id": "one", "entries": [
            {"id": "a", "scope": "dependencies", "outcome": "corrected"},
        ]}]}
        with self.assertRaisesRegex(ValueError, "not content corrections"):
            progress.summarize(ledger, {"a": {}}, {"a": {}})

    def test_delimiter_inside_metadata_is_not_front_matter_boundary(self):
        self.assertEqual(progress.metadata('+++\nid="a"\nsummary="A +++ B"\n+++\nBody')['summary'], "A +++ B")
