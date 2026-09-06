import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_review_proposals import audit  # noqa: E402


class ReviewProposalAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "packets").mkdir()
        (self.root / "proposals").mkdir()
        self.source = self.root / "source.knowl.md"
        self.source.write_text("+++\nid = 'a'\n+++\n\nA definition.\n")

    def tearDown(self):
        self.tmp.cleanup()

    def row(self, node="a", before=None, count=0):
        digest = hashlib.sha256(self.source.read_bytes()).hexdigest()
        return {"id": node, "path": str(self.source), "before": before or [],
                "review_count_before": count, "sha256": digest}

    def write_registry_packet(self, rows):
        (self.root / "registry.json").write_text(json.dumps(rows))
        (self.root / "packets" / "1.json").write_text(json.dumps(rows))

    def write_proposal(self, reviews, **extra):
        data = {"reviews": reviews, "unresolved": [], "content_corrections": [],
                "cross_batch_dependencies": []}
        data.update(extra)
        (self.root / "proposals" / "1.json").write_text(json.dumps(data))

    def review(self, row, after=None):
        return {"id": row["id"], "before": row["before"],
                "after": row["before"] if after is None else after,
                "review_count_before": row["review_count_before"],
                "sha256": row["sha256"], "rationale": "definition ingredients",
                "core_summary": "read the displayed definition"}

    def test_valid_source_hash_and_new_knowl_are_in_graph(self):
        original = self.row()
        self.write_registry_packet([original])
        self.write_proposal([self.review(original)])
        new_source = self.root / "new.knowl.md"
        new_source.write_text("new")
        new = {"id": "new", "path": str(new_source), "before": ["a"],
               "review_count_before": 1,
               "sha256": hashlib.sha256(new_source.read_bytes()).hexdigest()}
        (self.root / "new_knowls.json").write_text(json.dumps([new]))
        result = audit(self.root)
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["new_knowls"], 1)
        self.assertEqual(result["nodes"], 2)

    def test_malformed_new_knowl_row_is_reported_without_crashing(self):
        original = self.row()
        self.write_registry_packet([original])
        self.write_proposal([self.review(original)])
        (self.root / "new_knowls.json").write_text(json.dumps(["not a row"]))
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("row must be an object" in e for e in result["errors"]))

    def test_unreviewed_registry_node_must_appear_in_exactly_one_packet(self):
        a = self.row("a")
        b = self.row("b")
        self.write_registry_packet([a, b])
        (self.root / "packets" / "1.json").write_text(json.dumps([a]))
        self.write_proposal([self.review(a)])
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("missing packet coverage" in e for e in result["errors"]))

    def test_packet_unknown_registry_id_is_rejected(self):
        original = self.row()
        self.write_registry_packet([original])
        unknown = self.row("unknown")
        (self.root / "packets" / "1.json").write_text(json.dumps([original, unknown]))
        self.write_proposal([self.review(original)])
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("not in registry" in e for e in result["errors"]))

    def test_new_knowl_missing_before_target_is_rejected(self):
        original = self.row()
        self.write_registry_packet([original])
        self.write_proposal([self.review(original)])
        new_source = self.root / "new.knowl.md"
        new_source.write_text("new")
        new = {"id": "new", "path": str(new_source), "before": ["missing"],
               "review_count_before": 1,
               "sha256": hashlib.sha256(new_source.read_bytes()).hexdigest()}
        (self.root / "new_knowls.json").write_text(json.dumps([new]))
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("new_knowls: new: missing prerequisite" in e for e in result["errors"]))

    def test_hash_mismatch_and_missing_required_keys_are_reported(self):
        original = self.row()
        broken = dict(original)
        broken.pop("sha256")
        self.write_registry_packet([broken])
        self.write_proposal([])
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("missing source keys" in e or "source hash" in e for e in result["errors"]))

    def test_missing_target_and_duplicate_packet_ids_are_reported(self):
        original = self.row()
        self.write_registry_packet([original])
        (self.root / "packets" / "1.json").write_text(json.dumps([original, original]))
        self.write_proposal([self.review(original, ["missing-node"])])
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("duplicate packet IDs" in e for e in result["errors"]))
        self.assertTrue(any("missing prerequisite" in e for e in result["errors"]))

    def test_cross_batch_suggestions_are_checked_for_global_cycles(self):
        a = self.row("a")
        b = self.row("b")
        registry = [a, b]
        (self.root / "registry.json").write_text(json.dumps(registry))
        for number, row in [("1", a), ("2", b)]:
            (self.root / "packets" / f"{number}.json").write_text(json.dumps([row]))
            (self.root / "proposals" / f"{number}.json").write_text(json.dumps({
                "reviews": [self.review(row, ["b" if row["id"] == "a" else "a"])], "unresolved": [],
                "content_corrections": [],
                "cross_batch_dependencies": [{"id": row["id"],
                                                "suggested_after": ["b" if row["id"] == "a" else "a"]}],
            }))
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(result["cycles"])

    def test_advisory_cross_batch_suggestion_does_not_change_graph(self):
        original = self.row()
        self.write_registry_packet([original])
        self.write_proposal([self.review(original)], cross_batch_dependencies=[
            {"id": "a", "suggested_after": ["a"]},
        ])
        result = audit(self.root)
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["cycles"], [])
        self.assertEqual(result["edges"], 0)

    def test_pending_and_unresolved_reviews_cannot_be_silent(self):
        original = self.row()
        self.write_registry_packet([original])
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertEqual(result["pending_batches"], ["1"])
        self.write_proposal([], unresolved=[{"id": "a", "reason": "ambiguous"}])
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertEqual(len(result["unresolved"]), 1)

    def test_proposal_without_packet_is_reported(self):
        original = self.row()
        self.write_registry_packet([original])
        self.write_proposal([self.review(original)])
        (self.root / "proposals" / "99.json").write_text("{}")
        result = audit(self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("proposal without packet" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
