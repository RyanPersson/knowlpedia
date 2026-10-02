from __future__ import annotations

import copy
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "packages" / "compiler"))
import catalog
import knowl_compile as compiler


def evidence() -> dict:
    return {"status": "proved-in-text", "method": "Direct verification in the linked knowl.",
            "references": [], "lean": None}


def fixture() -> dict:
    data = {"schema_version": 1, **{key: [] for key in catalog.COLLECTIONS}}
    for category_id, scalar, unit in (("jord-r", "R", "arbitrary maps"), ("jord1-r", "R", "unit-preserving maps"),
                                     ("jord-c", "C", "arbitrary maps")):
        data["categories"].append({"id": category_id, "name": category_id, "knowl": "sample/category", "scalar": scalar,
                                   "object_axioms": ["Jordan identity"], "morphism_axioms": ["linear", "product-preserving"],
                                   "unit_policy": unit, "regularity": "algebraic"})
    for ident, categories in (("a", ["jord-r", "jord1-r"]), ("b", ["jord-r", "jord-c"])):
        data["objects"].append({"id": ident, "name": ident.upper(), "notation": ident.upper(), "kind": "jordan-algebra",
                                "family": "scalar", "parameters": {}, "knowl": "sample/object", "dimensions": {"real": 2},
                                "category_ids": categories, "constraints": [], "properties": {"unital": True},
                                "status": "defined", "references": []})
    data["views"].append({"id": "a-twisted", "object_id": "a", "category_id": "jord-r", "description": "Another named structure."})
    data["relationships"].append({"id": "a-b", "source": "a", "target": "b", "kind": "embedding", "category_id": "jord-r",
                                    "statement": "An embedding under the stated conventions.", "knowl": "sample/relation",
                                    "conditions": [], "evidence": evidence()})
    data["morphism_spaces"].append({"id": "hom-a-b", "source_view": "a@jord-r", "target_view": "b@jord-r", "operation": "hom",
                                      "description": "A recorded family, without a completeness claim.", "knowl": "sample/relation",
                                      "conditions": ["Chosen parameter"], "evidence": evidence()})
    data["morphism_spaces"].append({"id": "end-a", "source_view": "a@jord-r", "target_view": "a@jord-r", "operation": "end",
                                      "coverage": "complete", "description": "All endomorphisms under the conditions.",
                                      "knowl": "sample/relation", "conditions": [], "evidence": evidence()})
    return data


REGISTRY = {name: {"visibility": "production"} for name in ("sample/category", "sample/object", "sample/relation")}


class CatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def load(self, data: dict | None = None, registry: dict | None = None) -> dict:
        path = self.root / "shard.json"
        path.write_text(json.dumps(fixture() if data is None else data))
        return catalog.load_catalog([path], REGISTRY if registry is None else registry)

    def exported(self) -> Path:
        catalog.export_catalog(self.load(), self.root / "indexes")
        return self.root / "indexes" / "catalog.sqlite"

    def test_default_views_and_named_structures_are_distinct(self) -> None:
        data = self.load()
        views = {row["id"]: row for row in data["views"]}
        self.assertEqual(set(views), {"a@jord-r", "a@jord1-r", "b@jord-r", "b@jord-c", "a-twisted"})
        self.assertEqual(views["a@jord-r"]["scalar"], "R")
        self.assertEqual(views["b@jord-c"]["scalar"], "C")
        self.assertNotEqual(views["a-twisted"]["id"], views["a@jord-r"]["id"])

    def test_unknown_reference_diagnostics_identify_record(self) -> None:
        cases = [
            ("knowl", lambda d: d["objects"][0].update(knowl="missing/knowl")),
            ("unknown category", lambda d: d["objects"][0]["category_ids"].append("typo")),
            ("unknown source object", lambda d: d["relationships"][0].update(source="typo")),
            ("unknown target_view", lambda d: d["morphism_spaces"][0].update(target_view="typo")),
        ]
        for message, mutate in cases:
            with self.subTest(message=message):
                data = fixture()
                mutate(data)
                with self.assertRaisesRegex(catalog.CatalogValidationError, message) as caught:
                    self.load(data)
                self.assertIn("shard.json:", str(caught.exception))

    def test_duplicate_ids_across_shards_are_rejected(self) -> None:
        self.load()
        second = self.root / "second.json"
        second.write_text(json.dumps({"schema_version": 1, "objects": [fixture()["objects"][0]]}))
        with self.assertRaisesRegex(catalog.CatalogValidationError, "duplicate objects ID"):
            catalog.load_catalog([self.root / "shard.json", second], REGISTRY)

    def test_schema_required_fields_dimensions_and_status_are_checked(self) -> None:
        for field, value, message in (("dimensions", {"real": -1}, "nonnegative"), ("dimensions", {"real": True}, "nonnegative"),
                                      ("status", "complete", "defined or family"), ("status", [], "defined or family"),
                                      ("category_ids", ["jord-r", "jord-r"], "duplicate")):
            with self.subTest(field=field, value=value):
                data = fixture()
                data["objects"][0][field] = value
                with self.assertRaisesRegex(catalog.CatalogValidationError, message):
                    self.load(data)
        data = fixture()
        del data["objects"][0]["properties"]
        with self.assertRaisesRegex(catalog.CatalogValidationError, "missing required fields: properties"):
            self.load(data)
        data = fixture()
        data["objects"][0].update(status="family", dimensions={"real": "n^2"})
        with self.assertRaisesRegex(catalog.CatalogValidationError, "parameter domains"):
            self.load(data)
        data["objects"][0]["constraints"] = ["n >= 1 is an integer"]
        self.assertEqual(self.load(data)["objects"][0]["dimensions"], {"real": "n^2"})

    def test_cross_category_hom_and_cross_view_end_aut_are_rejected(self) -> None:
        data = fixture()
        data["morphism_spaces"][0]["target_view"] = "b@jord-c"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "same category"):
            self.load(data)
        for operation in ("end", "aut"):
            data = fixture()
            data["morphism_spaces"][0].update(operation=operation, target_view="a-twisted")
            with self.assertRaisesRegex(catalog.CatalogValidationError, "identical view"):
                self.load(data)

    def test_unital_objects_do_not_coerce_unit_preserving_morphisms(self) -> None:
        data = self.load()
        space = next(row for row in data["morphism_spaces"] if row["id"] == "hom-a-b")
        self.assertEqual(space["category_id"], "jord-r")
        self.assertEqual(space["coverage"], "partial")
        self.assertNotIn("jord1-r", data["indexes"]["morphism_lookup"])

    def test_views_cannot_claim_unlisted_memberships_or_steal_default_ids(self) -> None:
        data = fixture()
        data["views"][0]["category_id"] = "jord-c"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "declared category memberships"):
            self.load(data)
        data = fixture()
        data["views"][0].update(id="a@jord-r", object_id="b")
        with self.assertRaisesRegex(catalog.CatalogValidationError, "default view ID"):
            self.load(data)
        data = fixture()
        data["views"][0]["scalar"] = "C"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "view scalar disagrees"):
            self.load(data)

    def test_relationships_distinguish_structural_constructions_from_morphisms(self) -> None:
        for kind in catalog.STRUCTURAL_KINDS:
            data = fixture()
            data["relationships"][0]["kind"] = kind
            with self.assertRaisesRegex(catalog.CatalogValidationError, "structural relationship"):
                self.load(data)
        for kind in catalog.MORPHISM_KINDS:
            data = fixture()
            data["relationships"][0].update(kind=kind, category_id=None)
            with self.assertRaisesRegex(catalog.CatalogValidationError, "morphism relationship"):
                self.load(data)

    def test_duplicate_json_keys_nonfinite_numbers_and_unknown_collections_fail(self) -> None:
        path = self.root / "bad.json"
        for value, message in (('{"schema_version":1,"schema_version":1}', "duplicate JSON key"),
                               ('{"schema_version":1,"description":NaN}', "nonfinite JSON"),
                               ('{"schema_version":1,"objets":[]}', "unknown collections")):
            path.write_text(value)
            with self.assertRaisesRegex(catalog.CatalogValidationError, message):
                catalog.load_catalog([path], REGISTRY)

    def test_result_object_references_are_checked_and_reverse_indexed(self) -> None:
        data = fixture()
        data["morphism_spaces"][0]["result_object_ids"] = ["a"]
        normalized = self.load(data)
        self.assertEqual(normalized["indexes"]["morphism_results_by_object"]["a"], ["hom-a-b"])
        catalog.export_catalog(normalized, self.root / "indexes")
        with catalog.CatalogQuery(self.root / "indexes" / "catalog.sqlite") as query:
            self.assertEqual(query.connection.execute("SELECT morphism_id FROM morphism_results WHERE object_id = ?", ("a",)).fetchall(), [("hom-a-b",)])
        data["morphism_spaces"][0]["result_object_ids"] = ["missing"]
        with self.assertRaisesRegex(catalog.CatalogValidationError, "unknown result object"):
            self.load(data)

    def test_second_input_is_indexed_without_inventing_a_hom(self) -> None:
        data = fixture()
        data["relationships"][0].update(source="a", target="a", kind="construction", category_id=None,
                                         parameters={"other_input_id": "b"})
        normalized = self.load(data)
        self.assertEqual(normalized["indexes"]["construction_inputs"], {"a": ["a-b"], "b": ["a-b"]})
        catalog.export_catalog(normalized, self.root / "indexes")
        with catalog.CatalogQuery(self.root / "indexes" / "catalog.sqlite") as query:
            self.assertEqual([row["id"] for row in query.neighbors("b", direction="outgoing")], ["a-b"])
            self.assertEqual(len(query.neighbors("a")), 1)
            self.assertEqual(query.neighbors("b", direction="incoming"), [])
            self.assertEqual(query.neighbors("b", category_id="jord-r"), [])
            self.assertEqual(query.morphisms("b@jord-r", "a@jord-r")["status"], "not-catalogued")

    def test_evidence_and_future_proof_refs_are_explicit(self) -> None:
        data = fixture()
        data["relationships"][0]["evidence"]["status"] = "verified-by-lean"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "evidence status"):
            self.load(data)
        data = fixture()
        data["relationships"][0]["evidence"]["lean"] = "Some.theorem"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "proof reference"):
            self.load(data)
        data["relationships"][0]["evidence"]["lean"] = {"module": "Example", "declaration": "Example.result", "revision": "abc123"}
        self.load(data)

    def test_public_catalogue_cannot_export_private_or_development_knowl_refs(self) -> None:
        for visibility in ("private", "development"):
            registry = copy.deepcopy(REGISTRY)
            registry["sample/object"]["visibility"] = visibility
            with self.assertRaisesRegex(catalog.CatalogValidationError, "public knowls"):
                self.load(registry=registry)

    def test_redirect_knowl_ids_resolve_through_compiler_registry(self) -> None:
        class Registry(dict):
            def canonical_id(self, ident: str) -> str:
                return "sample/object" if ident == "old/object" else ident
        data = fixture()
        data["objects"][0]["knowl"] = "old/object"
        self.assertEqual(self.load(data, Registry(REGISTRY))["objects"][0]["knowl"], "sample/object")

    def test_deterministic_exports_and_indexed_queries(self) -> None:
        data = self.load()
        catalog.export_catalog(data, self.root / "one")
        reordered = fixture()
        for key in catalog.COLLECTIONS:
            reordered[key].reverse()
        catalog.export_catalog(self.load(reordered), self.root / "two")
        for filename in ("catalog.json", "catalog.sqlite"):
            self.assertEqual((self.root / "one" / filename).read_bytes(), (self.root / "two" / filename).read_bytes())
        with catalog.CatalogQuery(self.root / "one" / "catalog.sqlite") as query:
            self.assertEqual([row["id"] for row in query.common_categories("a", "b")], ["jord-r"])
            self.assertEqual([row["id"] for row in query.objects(category_id="jord1-r")], ["a"])
            self.assertEqual([row["id"] for row in query.neighbors("b", direction="incoming")], ["a-b"])
            self.assertEqual(query.neighbors("b", direction="outgoing"), [])
            self.assertEqual(query.morphisms("a@jord-r", "b@jord-r")["status"], "catalogued")
            self.assertEqual(query.morphisms("a@jord-r", "a@jord-r", "end")["records"][0]["coverage"], "complete")
            self.assertEqual(query.counts(), data["counts"])
            plan = query.connection.execute("EXPLAIN QUERY PLAN SELECT payload FROM morphism_spaces WHERE source_view = ? AND target_view = ? AND operation = ?", ("a@jord-r", "b@jord-r", "hom")).fetchall()
            self.assertTrue(any("morphisms_views" in row[-1] for row in plan), plan)
            plan = query.connection.execute("EXPLAIN QUERY PLAN SELECT payload FROM relationships WHERE target = ?", ("b",)).fetchall()
            self.assertTrue(any("relationships_target" in row[-1] for row in plan), plan)

    def test_missing_record_is_unknown_and_queries_do_not_create_pairs(self) -> None:
        with catalog.CatalogQuery(self.exported()) as query:
            before = query.counts()
            result = query.morphisms("b@jord-r", "a@jord-r")
            self.assertEqual(result["status"], "not-catalogued")
            self.assertEqual(result["records"], [])
            self.assertNotIn("empty", result)
            self.assertEqual(query.counts(), before)
            with self.assertRaises(sqlite3.OperationalError):
                query.connection.execute("DELETE FROM objects")
            with self.assertRaises(KeyError):
                query.common_categories("missing", "a")
            with self.assertRaises(ValueError):
                query.morphisms("a@jord-r", "b@jord-c")
            with self.assertRaises(ValueError):
                query.morphisms("a@jord-r", "a-twisted", "aut")

    def test_magic_square_complete_cell_coverage_and_typed_construction(self) -> None:
        data = fixture()
        data["relationships"][0].update(kind="construction", category_id=None)
        data["magic_squares"] = [{"id": "square", "name": "Small construction table", "knowl": "sample/relation",
                                  "field": "R", "form": "compact", "row_object_ids": ["a"], "column_object_ids": ["b"],
                                  "cells": [{"row_object_id": "a", "column_object_id": "b", "output_object_id": "b",
                                             "construction_relationship_ids": ["a-b"]}], "evidence": evidence()}]
        self.assertEqual(self.load(data)["counts"]["magic_squares"], 1)
        bad = copy.deepcopy(data)
        bad["magic_squares"][0]["cells"] = []
        with self.assertRaisesRegex(catalog.CatalogValidationError, "incomplete"):
            self.load(bad)
        bad = copy.deepcopy(data)
        bad["magic_squares"][0]["cells"][0]["output_object_id"] = "a"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "target the cell output"):
            self.load(bad)

    def test_compiler_optional_exports_and_validation_before_output_deletion(self) -> None:
        package = self.root / "package"
        package.mkdir()
        (package / "knowlpack.toml").write_text('id = "catalog-test"\ntitle = "Catalogue test"\ncontent_dir = "content"\n')
        content = package / "content"
        content.mkdir()
        for index, ident in enumerate(REGISTRY):
            (content / f"{index}.knowl.md").write_text(
                f'+++\nid = "{ident}"\ntitle = "Test {index}"\nkind = "definition"\nsummary = "Test."\n+++\nA definition.\n')
        output = self.root / "site"
        self.assertEqual(compiler.write_site(package, output, profile=compiler.BUILD_PROFILES["production"]), 0)
        self.assertFalse((output / "indexes" / "catalog.json").exists())
        shard_dir = content / "catalog" / "data"
        shard_dir.mkdir(parents=True)
        shard = shard_dir / "test.json"
        shard.write_text(json.dumps(fixture()))
        self.assertEqual(compiler.write_site(package, output, profile=compiler.BUILD_PROFILES["production"]), 0)
        self.assertTrue((output / "indexes" / "catalog.sqlite").is_file())
        original = (output / "indexes" / "catalog.json").read_bytes()
        bad = fixture()
        bad["objects"][0]["knowl"] = "missing"
        shard.write_text(json.dumps(bad))
        self.assertEqual(compiler.write_site(package, output, allow_validation_errors=True), 1)
        self.assertEqual((output / "indexes" / "catalog.json").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
