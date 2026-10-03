from __future__ import annotations

import copy
import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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


def finite_fixture() -> dict:
    data = fixture()
    for ident in ("sets", "groups", "finite-groups", "finite-simple-groups"):
        data["categories"].append({"id": ident, "name": ident, "knowl": "sample/category", "scalar": None,
                                   "object_axioms": [], "morphism_axioms": [], "unit_policy": "group identity",
                                   "regularity": "algebraic"})
    data["objects"].append({
        "id": "fg-example", "name": "Cyclic group of order six", "notation": "C_6", "kind": "finite-group",
        "family": "cyclic", "parameters": {"n": 6}, "knowl": "sample/object", "dimensions": {},
        "category_ids": ["sets", "groups", "finite-groups"], "constraints": [], "status": "defined", "references": [],
        "properties": {"finite_group": {
            "table_role": "example", "section": "familiar", "order_tex": "6", "order_decimal": "6", "simple": False,
            "simple_condition": "This group is not simple because its order is composite.",
            "parameter_summary": "A fixed cyclic group.", "construction_summary": "Integers modulo six under addition.",
            "order_factors": [[2, 1], [3, 1]],
        }},
    })
    return data


def lie_fixture(*, complex_group: bool = False) -> dict:
    data = fixture()
    data["categories"].append({
        "id": "real-lie-groups", "name": "Real Lie groups", "knowl": "sample/category", "scalar": None,
        "object_axioms": [], "morphism_axioms": [], "unit_policy": "group identity", "regularity": "smooth",
    })
    data["objects"].append({
        "id": "lg-su-n", "name": "Special unitary groups", "notation": "SU(n)", "kind": "lie-group",
        "family": "special-unitary", "parameters": {"n": "integer"}, "knowl": "sample/object",
        "dimensions": {"real": "n^2-1"}, "category_ids": ["real-lie-groups"],
        "constraints": ["n >= 2"], "status": "family", "references": [],
        "properties": {"compact": True, "connected": True, "lie_group": {
            "section": "classical", "form": "compact", "parameter_summary": "Integer n >= 2.",
            "construction_summary": "Unitary matrices of determinant one.",
            "global_form_summary": "The simply connected compact matrix group SU(n).",
            "classification_cells": [{
                "series": "A", "form": "compact", "notation": "SU(r+1)",
                "dimension_tex": "r(r+2)", "dimension_field": "real", "parameter_summary": "Integer r >= 1.",
                "specialization": "Set n = r+1.", "global_form": "The simply connected compact group SU(r+1).",
            }],
        }},
    })
    if complex_group:
        data["categories"].append({
            "id": "complex-lie-groups", "name": "Complex Lie groups", "knowl": "sample/category", "scalar": None,
            "object_axioms": [], "morphism_axioms": [], "unit_policy": "group identity", "regularity": "holomorphic",
        })
        obj = data["objects"][-1]
        obj.update(id="lg-sl-n-c", name="Complex special linear groups", notation=r"SL(n,\mathbb C)",
                   family="special-linear", dimensions={"real": "2*(n^2-1)", "complex": "n^2-1"})
        obj["category_ids"].append("complex-lie-groups")
        obj["properties"]["compact"] = False
        metadata = obj["properties"]["lie_group"]
        metadata.update(form="complex", construction_summary="Complex matrices of determinant one.",
                        global_form_summary="The simply connected complex matrix group SL(n,C).")
        metadata["classification_cells"][0].update(
            form="complex", notation=r"SL(r+1,\mathbb C)", dimension_field="complex",
            global_form="The simply connected complex group SL(r+1,C).")
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

    def test_lie_group_partial_cells_and_metadata_survive_both_exports(self) -> None:
        data = lie_fixture()
        metadata = data["objects"][-1]["properties"]["lie_group"]
        metadata["display_order"] = 0
        normalized = self.load(data)
        catalog.export_catalog(normalized, self.root / "lie")
        browser = json.loads((self.root / "lie" / "catalog.json").read_text())
        obj = browser["objects"][browser["indexes"]["by_id"]["objects"]["lg-su-n"]]
        self.assertEqual(obj["properties"]["lie_group"], metadata)
        self.assertEqual(obj["dimensions"], {"real": "n^2-1"})
        with catalog.CatalogQuery(self.root / "lie" / "catalog.sqlite") as query:
            self.assertEqual(query.get("objects", "lg-su-n")["properties"]["lie_group"], metadata)
        # Display-only metadata and entirely unannotated Lie groups remain valid.
        del metadata["classification_cells"]
        del metadata["display_order"]
        self.load(data)
        del data["objects"][-1]["properties"]["lie_group"]
        self.load(data)

    def test_lie_group_metadata_requires_exact_types_known_fields_and_scope(self) -> None:
        cases = [
            ("section", "finite", "unknown Lie-group section"), ("section", [], "nonempty string"),
            ("form", "split", "unknown Lie-group form"), ("form", {}, "nonempty string"),
            ("parameter_summary", " ", "nonempty string"), ("construction_summary", None, "nonempty string"),
            ("global_form_summary", 1, "nonempty string"), ("global_form", "SU(n)", "unknown Lie-group fields"),
            *[("display_order", value, "nonnegative integer") for value in (-1, False, True, 0.0, "0", None)],
            *[("classification_cells", value, "nonempty array") for value in ([], {}, None, "A")],
        ]
        for key, value, message in cases:
            with self.subTest(key=key, value=value):
                data = lie_fixture()
                data["objects"][-1]["properties"]["lie_group"][key] = value
                with self.assertRaisesRegex(catalog.CatalogValidationError, message):
                    self.load(data)
        for metadata in (None, [], "compact"):
            data = lie_fixture()
            data["objects"][-1]["properties"]["lie_group"] = metadata
            with self.assertRaisesRegex(catalog.CatalogValidationError, "metadata object"):
                self.load(data)
        data = lie_fixture()
        del data["objects"][-1]["properties"]["lie_group"]["global_form_summary"]
        with self.assertRaisesRegex(catalog.CatalogValidationError, "missing required fields: global_form_summary"):
            self.load(data)
        for field, value in (("kind", "lie-algebra"), ("category_ids", [])):
            data = lie_fixture()
            data["objects"][-1][field] = value
            with self.assertRaisesRegex(catalog.CatalogValidationError, "requires kind lie-group and real-lie-groups"):
                self.load(data)

    def test_lie_classification_cells_validate_fields_and_dimension_convention(self) -> None:
        cases = [
            ("series", "A2", "unknown Dynkin series"), ("series", [], "nonempty string"),
            ("form", "real", "unknown classification form"), ("form", False, "nonempty string"),
            ("dimension_field", "complex", "compact column requires real dimension"),
            ("dimension_tex", "$r(r+2)$", "without math delimiters"),
            ("notation", r"\(SU(r+1)\)", "without math delimiters"),
            ("dimension_tex", r"\[r(r+2)\]", "without math delimiters"),
            ("parameter_summary", "", "nonempty string"), ("specialization", {}, "nonempty string"),
            ("global_form", None, "nonempty string"), ("rank", 1, "unknown classification-cell fields"),
        ]
        for key, value, message in cases:
            with self.subTest(key=key, value=value):
                data = lie_fixture()
                data["objects"][-1]["properties"]["lie_group"]["classification_cells"][0][key] = value
                with self.assertRaisesRegex(catalog.CatalogValidationError, message):
                    self.load(data)
        data = lie_fixture()
        cells = data["objects"][-1]["properties"]["lie_group"]["classification_cells"]
        cells[0]["form"] = "complex"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "complex column requires complex dimension"):
            self.load(data)
        data = lie_fixture(complex_group=True)
        cells = data["objects"][-1]["properties"]["lie_group"]["classification_cells"]
        self.load(data)
        del cells[0]["global_form"]
        with self.assertRaisesRegex(catalog.CatalogValidationError, "missing required fields: global_form"):
            self.load(data)
        cells[0] = []
        with self.assertRaisesRegex(catalog.CatalogValidationError, "expected a classification cell object"):
            self.load(data)

    def test_lie_classification_dimension_matches_owning_object_structure(self) -> None:
        for complex_group, dimension in ((False, "real"), (True, "complex")):
            data = lie_fixture(complex_group=complex_group)
            del data["objects"][-1]["dimensions"][dimension]
            with self.assertRaisesRegex(catalog.CatalogValidationError, f"must declare a {dimension} dimension"):
                self.load(data)
        data = lie_fixture(complex_group=True)
        data["objects"][-1]["category_ids"].remove("complex-lie-groups")
        with self.assertRaisesRegex(catalog.CatalogValidationError, "requires complex-lie-groups membership"):
            self.load(data)

    def test_lie_classification_cells_are_unique_within_and_across_shards(self) -> None:
        data = lie_fixture()
        cells = data["objects"][-1]["properties"]["lie_group"]["classification_cells"]
        cells.append(copy.deepcopy(cells[0]))
        with self.assertRaisesRegex(catalog.CatalogValidationError, "duplicate Lie-group classification cell"):
            self.load(data)
        data = lie_fixture()
        self.load(data)
        other = copy.deepcopy(data["objects"][-1])
        other["id"] = "lg-another-global-form"
        second = self.root / "second.json"
        second.write_text(json.dumps({"schema_version": 1, "objects": [other]}))
        with self.assertRaisesRegex(catalog.CatalogValidationError, "duplicate Lie-group classification cell") as caught:
            catalog.load_catalog([self.root / "shard.json", second], REGISTRY)
        self.assertIn("shard.json:", str(caught.exception))
        self.assertIn("second.json:", str(caught.exception))
        self.assertIn("lg-another-global-form", str(caught.exception))

    def test_finite_group_exact_order_survives_both_exports(self) -> None:
        data = finite_fixture()
        finite = data["objects"][-1]["properties"]["finite_group"]
        exact_order = str(2 ** 90 * 3 ** 7)
        finite.update(order_decimal=exact_order, order_tex=r"2^{90}3^7", order_factors=[[2, 90], [3, 7]], display_order=0)
        normalized = self.load(data)
        catalog.export_catalog(normalized, self.root / "finite")
        browser = json.loads((self.root / "finite" / "catalog.json").read_text())
        obj = browser["objects"][browser["indexes"]["by_id"]["objects"]["fg-example"]]
        self.assertEqual(obj["properties"]["finite_group"]["order_decimal"], exact_order)
        self.assertEqual(obj["properties"]["finite_group"]["display_order"], 0)
        with catalog.CatalogQuery(self.root / "finite" / "catalog.sqlite") as query:
            self.assertEqual(query.get("objects", "fg-example")["properties"]["finite_group"]["order_decimal"], exact_order)
            self.assertEqual(query.get("objects", "fg-example")["properties"]["finite_group"]["display_order"], 0)

    def test_finite_group_display_order_is_optional_and_accepts_positive_integers(self) -> None:
        data = finite_fixture()
        self.load(data)
        data["objects"][-1]["properties"]["finite_group"]["display_order"] = 7
        self.load(data)

    def test_finite_group_metadata_requires_exact_types_and_known_fields(self) -> None:
        cases = [
            ("order_decimal", 6, "positive decimal string"), ("order_decimal", 6.0, "positive decimal string"),
            ("order_decimal", "0", "positive decimal string"), ("order_decimal", "06", "positive decimal string"),
            ("order_decimal", "1e6", "positive decimal string"), ("simple", 1, "boolean or null"),
            ("simple", None, "parameter-dependent simplicity requires a family"),
            ("simple", "false", "boolean or null"), ("table_role", "atomic", "unknown table role"),
            ("section", "pariah", "unknown table section"), ("order_tex", "$6$", "without math delimiters"),
            ("simple_condition", "", "nonempty string"), ("sporadic_cluster", "mathieu", "sporadic entry"),
            ("rank_label", "", "nonempty string"), ("exactorder_decimal", "6", "unknown finite-group fields"),
            *[("display_order", value, "nonnegative integer") for value in (-1, False, True, 0.0, 1.5, "0", None)],
        ]
        for key, value, message in cases:
            with self.subTest(key=key, value=value):
                data = finite_fixture()
                data["objects"][-1]["properties"]["finite_group"][key] = value
                with self.assertRaisesRegex(catalog.CatalogValidationError, message):
                    self.load(data)
        data = finite_fixture()
        del data["objects"][-1]["properties"]["finite_group"]["construction_summary"]
        with self.assertRaisesRegex(catalog.CatalogValidationError, "missing required fields: construction_summary"):
            self.load(data)

    def test_finite_group_factor_structure_and_exact_product_are_checked(self) -> None:
        for factors, message in (([[True, 1]], "integer entries"), ([[2, True]], "integer entries"),
                                  ([[2, 0]], "integer entries"), ([[1, 3]], "integer entries"),
                                  ([[2, 1], [2, 2]], "duplicate factor"), ([[2, 2], [3, 1]], "does not match"),
                                  ([[2, 1000000000]], "does not match")):
            with self.subTest(factors=factors):
                data = finite_fixture()
                data["objects"][-1]["properties"]["finite_group"]["order_factors"] = factors
                with self.assertRaisesRegex(catalog.CatalogValidationError, message):
                    self.load(data)
        data = finite_fixture()
        data["objects"][-1]["properties"]["finite_group"].update(order_decimal="1", order_tex="1", order_factors=[])
        self.load(data)

    def test_finite_group_roles_and_simplicity_agree_with_memberships(self) -> None:
        data = finite_fixture()
        obj = data["objects"][-1]
        obj["category_ids"].remove("groups")
        with self.assertRaisesRegex(catalog.CatalogValidationError, "must declare sets, groups"):
            self.load(data)
        for simple, membership in ((True, False), (False, True), (None, True)):
            data = finite_fixture()
            obj = data["objects"][-1]
            obj["properties"]["finite_group"]["simple"] = simple
            if membership:
                obj["category_ids"].append("finite-simple-groups")
            with self.assertRaisesRegex(catalog.CatalogValidationError, "must agree"):
                self.load(data)
        data = finite_fixture()
        obj = data["objects"][-1]
        finite = obj["properties"]["finite_group"]
        obj["category_ids"].append("finite-simple-groups")
        obj.update(status="family", constraints=["p is prime"], parameters={"p": "prime"})
        finite.update(table_role="simple-family", section="cyclic", simple=True, order_tex="p", order_decimal=None)
        del finite["order_factors"]
        self.load(data)
        obj["status"] = "defined"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "simple-family requires family"):
            self.load(data)
        finite.update(table_role="tits", section="exceptional", order_tex="17971200", order_decimal="17971200")
        self.load(data)
        finite["section"] = "sporadic"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "tits entries require section"):
            self.load(data)
        finite.update(table_role="sporadic", sporadic_cluster="mathieu")
        self.load(data)
        finite["sporadic_cluster"] = "tits"
        with self.assertRaisesRegex(catalog.CatalogValidationError, "recognized cluster"):
            self.load(data)

    def test_finite_navigation_uses_order_and_preserves_generated_guard(self) -> None:
        repo = self.root / "navigation-package"
        content = repo / "content"
        data_dir = content / "catalog" / "data"
        data_dir.mkdir(parents=True)
        (content / "seed.md").write_text("Initial content package.\n")
        for args in (("init",), ("config", "user.name", "Test User"),
                     ("config", "user.email", "test@example.com"), ("add", "content"),
                     ("commit", "-m", "baseline")):
            subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)
        (data_dir / "finite-elementary.json").write_text(json.dumps({
            "schema_version": 1, "objects": [finite_fixture()["objects"][-1]],
        }))
        # Category-only supplemental shards require no object navigation lane.
        (data_dir / "finite-core.json").write_text(json.dumps({"schema_version": 1, "objects": []}))
        script = Path(__file__).resolve().parents[1] / "scripts" / "generate_catalog_indexes.py"
        command = [sys.executable, str(script), "--content-package", str(repo), "--baseline", "HEAD"]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertIn("Generated 8 indexes for 1 objects", result.stdout)
        index = content / "catalog" / "finite-elementary-index.knowl.md"
        rendered = index.read_text()
        self.assertIn("| Object | Order | Simplicity | Kind of entry |", rendered)
        self.assertIn(r"| \(6\) | not simple |", rendered)
        self.assertNotIn("Dimensions", rendered)
        self.assertIn("/catalog/finite-groups/table/", (content / "catalog.knowl.md").read_text())
        self.assertFalse((content / "catalog" / "finite-sporadic-index.knowl.md").exists())
        for args in (("add", "content"), ("commit", "-m", "generated catalogue")):
            subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)
        subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertIn("**0 catalogue knowls", (content / "catalog" / "created-knowls.knowl.md").read_text())
        authored = index.read_text().replace('generated_by = "scripts/generate_catalog_indexes.py"\n', "")
        index.write_text(authored)
        refused = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(refused.returncode, 0)
        self.assertIn("Refusing to overwrite an independently authored knowl", refused.stderr)
        self.assertEqual(index.read_text(), authored)

    def test_lie_navigation_links_table_only_with_display_metadata(self) -> None:
        repo = self.root / "lie-navigation-package"
        content = repo / "content"
        data_dir = content / "catalog" / "data"
        data_dir.mkdir(parents=True)
        (content / "seed.md").write_text("Initial content package.\n")
        for args in (("init",), ("config", "user.name", "Test User"),
                     ("config", "user.email", "test@example.com"), ("add", "content"),
                     ("commit", "-m", "baseline")):
            subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)
        shard = data_dir / "lie-groups.json"
        obj = lie_fixture()["objects"][-1]
        metadata = obj["properties"].pop("lie_group")
        shard.write_text(json.dumps({"schema_version": 1, "objects": [obj]}))
        script = Path(__file__).resolve().parents[1] / "scripts" / "generate_catalog_indexes.py"
        command = [sys.executable, str(script), "--content-package", str(repo), "--baseline", "HEAD"]
        subprocess.run(command, check=True, capture_output=True, text=True)
        indexes = [content / "catalog.knowl.md", content / "catalog" / "lie-groups-index.knowl.md"]
        for index in indexes:
            self.assertNotIn("/catalog/lie-groups/table/", index.read_text())
        obj["properties"]["lie_group"] = metadata
        shard.write_text(json.dumps({"schema_version": 1, "objects": [obj]}))
        subprocess.run(command, check=True, capture_output=True, text=True)
        for index in indexes:
            self.assertIn("/catalog/lie-groups/table/", index.read_text())
        self.assertIn("| Object | Dimensions | Kind of entry |", indexes[1].read_text())

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
        self.assertFalse((output / "catalog" / "finite-groups" / "table" / "index.html").exists())
        self.assertFalse((output / "assets" / "finite-groups.js").exists())
        self.assertFalse((output / "catalog" / "lie-groups" / "table" / "index.html").exists())
        self.assertFalse((output / "assets" / "lie-groups.js").exists())
        original = (output / "indexes" / "catalog.json").read_bytes()
        bad = fixture()
        bad["objects"][0]["knowl"] = "missing"
        shard.write_text(json.dumps(bad))
        self.assertEqual(compiler.write_site(package, output, allow_validation_errors=True), 1)
        self.assertEqual((output / "indexes" / "catalog.json").read_bytes(), original)

    def test_compiler_emits_finite_table_only_while_metadata_is_present(self) -> None:
        package = self.root / "finite-package"
        shard_dir = package / "content" / "catalog" / "data"
        shard_dir.mkdir(parents=True)
        (package / "knowlpack.toml").write_text('id = "finite-test"\ntitle = "Finite test"\ncontent_dir = "content"\n')
        for index, ident in enumerate(REGISTRY):
            (package / "content" / f"{index}.knowl.md").write_text(
                f'+++\nid = "{ident}"\ntitle = "Test {index}"\nkind = "definition"\nsummary = "Test."\n+++\nA definition.\n')
        shard = shard_dir / "test.json"
        shard.write_text(json.dumps(finite_fixture()))
        output = self.root / "finite-site"
        self.assertEqual(compiler.write_site(package, output, profile=compiler.BUILD_PROFILES["production"]), 0)
        table = output / "catalog" / "finite-groups" / "table" / "index.html"
        self.assertTrue(table.is_file())
        self.assertIn("/indexes/catalog.json", table.read_text())
        self.assertIn("/assets/finite-groups.js", table.read_text())
        self.assertTrue((output / "assets" / "finite-groups.js").is_file())
        self.assertTrue((output / "assets" / "finite-groups.css").is_file())
        if '/assets/katex.min.js' in table.read_text():
            self.assertTrue((output / "assets" / "katex.min.js").is_file())
        shard.write_text(json.dumps(fixture()))
        self.assertEqual(compiler.write_site(package, output, profile=compiler.BUILD_PROFILES["production"]), 0)
        self.assertFalse(table.exists())
        self.assertFalse((output / "assets" / "finite-groups.js").exists())

    def test_compiler_emits_lie_table_and_assets_only_while_metadata_is_present(self) -> None:
        package = self.root / "lie-package"
        shard_dir = package / "content" / "catalog" / "data"
        shard_dir.mkdir(parents=True)
        (package / "knowlpack.toml").write_text('id = "lie-test"\ntitle = "Lie test"\ncontent_dir = "content"\n')
        for index, ident in enumerate(REGISTRY):
            (package / "content" / f"{index}.knowl.md").write_text(
                f'+++\nid = "{ident}"\ntitle = "Test {index}"\nkind = "definition"\nsummary = "Test."\n+++\nA definition.\n')
        shard = shard_dir / "test.json"
        data = lie_fixture()
        shard.write_text(json.dumps(data))
        output = self.root / "lie-site"
        self.assertEqual(compiler.write_site(package, output, profile=compiler.BUILD_PROFILES["production"]), 0)
        table = output / "catalog" / "lie-groups" / "table" / "index.html"
        rendered = table.read_text()
        self.assertIn("/indexes/catalog.json", rendered)
        self.assertIn("/assets/lie-groups.js", rendered)
        self.assertIn("/assets/lie-groups.css?v=" + compiler.runtime_asset_version(), rendered)
        self.assertTrue((output / "assets" / "lie-groups.js").is_file())
        self.assertTrue((output / "assets" / "lie-groups.css").is_file())
        self.assertFalse((output / "catalog" / "finite-groups" / "table" / "index.html").exists())
        if '/assets/katex.min.js' in rendered:
            self.assertTrue((output / "assets" / "katex.min.js").is_file())
        with patch.object(compiler, "find_katex_assets_dir", return_value=None):
            self.assertEqual(compiler.write_site(package, output, profile=compiler.BUILD_PROFILES["production"]), 0)
        self.assertNotIn("/assets/katex.min.js", table.read_text())
        del data["objects"][-1]["properties"]["lie_group"]
        shard.write_text(json.dumps(data))
        self.assertEqual(compiler.write_site(package, output, profile=compiler.BUILD_PROFILES["production"]), 0)
        self.assertFalse(table.exists())
        self.assertFalse((output / "assets" / "lie-groups.js").exists())
        self.assertFalse((output / "assets" / "lie-groups.css").exists())
        self.assertTrue((output / "catalog" / "explorer" / "index.html").is_file())


if __name__ == "__main__":
    unittest.main()
