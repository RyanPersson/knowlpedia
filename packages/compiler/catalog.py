"""Validate and index the sparse, category-aware mathematical catalogue.

This module uses only the standard library. Source JSON is data, never code;
unknown Hom spaces remain unknown and no composition or inverse is inferred.
"""

from __future__ import annotations

import copy
import json
import re
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any, Iterable, Mapping
from urllib.parse import urlparse


SCHEMA_VERSION = 1
COLLECTIONS = ("objects", "categories", "views", "relationships", "morphism_spaces", "magic_squares")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
VIEW_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._@-]*$")
RELATION_KINDS = frozenset({
    "isomorphism", "embedding", "quotient", "covering", "scalar-restriction",
    "complexification", "lie-algebra", "derivation-algebra", "automorphism-group",
    "construction", "representation",
})
STRUCTURAL_KINDS = frozenset({"construction", "scalar-restriction", "complexification", "lie-algebra",
                              "derivation-algebra", "automorphism-group"})
MORPHISM_KINDS = frozenset({"isomorphism", "embedding", "quotient", "covering"})
EVIDENCE_STATUSES = frozenset({"definition", "proved-in-text", "literature", "conjectural"})
OPERATIONS = frozenset({"hom", "end", "aut"})


class CatalogValidationError(ValueError):
    """An authoring error with a stable, source-qualified diagnostic."""


def _require(condition: bool, location: str, message: str) -> None:
    if not condition:
        raise CatalogValidationError(f"{location}: {message}")


def _text(value: Any, location: str, *, nullable: bool = False) -> None:
    _require((nullable and value is None) or (isinstance(value, str) and bool(value.strip())),
             location, "expected a nonempty string" + (" or null" if nullable else ""))


def _strings(value: Any, location: str, *, unique: bool = False) -> None:
    _require(isinstance(value, list), location, "expected an array of strings")
    for index, item in enumerate(value):
        _text(item, f"{location}[{index}]")
    if unique:
        _require(len(value) == len(set(value)), location, "duplicate entries")


def _required(record: dict[str, Any], names: str, location: str) -> None:
    missing = sorted(set(names.split()) - record.keys())
    _require(not missing, location, "missing required fields: " + ", ".join(missing))


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"nonfinite JSON number {value!r}")


def _references(value: Any, location: str) -> None:
    _require(isinstance(value, list), location, "expected an array of references")
    for index, item in enumerate(value):
        loc = f"{location}[{index}]"
        _require(isinstance(item, dict), loc, "expected a reference object")
        _required(item, "url title locator", loc)
        for key in ("url", "title", "locator"):
            _text(item[key], f"{loc}.{key}")
        try:
            parsed = urlparse(item["url"])
        except ValueError as exc:
            raise CatalogValidationError(f"{loc}.url: invalid reference URL: {exc}") from exc
        _require(parsed.scheme in {"http", "https"} and bool(parsed.netloc), loc + ".url",
                 "expected an absolute http(s) reference URL")


def _evidence(value: Any, location: str) -> None:
    _require(isinstance(value, dict), location, "expected an evidence object")
    _required(value, "status method references lean", location)
    _require(isinstance(value["status"], str) and value["status"] in EVIDENCE_STATUSES, location + ".status", "unknown evidence status")
    _text(value["method"], location + ".method")
    _references(value["references"], location + ".references")
    if value["lean"] is not None:
        lean = value["lean"]
        _require(isinstance(lean, dict), location + ".lean", "expected null or a proof reference")
        _required(lean, "module declaration revision", location + ".lean")
        for key in ("module", "declaration", "revision"):
            _text(lean[key], location + ".lean." + key)


def _knowl(record: dict[str, Any], registry: Mapping[str, Any], location: str) -> None:
    value = record["knowl"]
    _text(value, location + ".knowl")
    _require("#" not in value, location + ".knowl", "use a knowl ID, not a section anchor")
    canonical = registry.canonical_id(value) if hasattr(registry, "canonical_id") else value
    _require(canonical in registry, location + ".knowl", f"unknown knowl ID {value!r}")
    knowl = registry[canonical]
    visibility = knowl.get("visibility", "production") if isinstance(knowl, dict) else getattr(knowl, "visibility", "production")
    _require(visibility == "production", location + ".knowl", "catalogue data must reference public knowls")
    record["knowl"] = canonical


def _shape(record: dict[str, Any], collection: str, registry: Mapping[str, Any], location: str) -> None:
    if collection == "objects":
        _required(record, "name notation kind family parameters knowl dimensions category_ids constraints properties status references", location)
        for key in ("name", "notation", "kind", "family"):
            _text(record[key], location + "." + key)
        for key in ("parameters", "dimensions", "properties"):
            _require(isinstance(record[key], dict), location + "." + key, "expected an object")
        for key, value in record["dimensions"].items():
            _text(key, location + ".dimensions")
            _require((type(value) is int and value >= 0) or (isinstance(value, str) and bool(value.strip())),
                     location + ".dimensions." + key, "expected a nonnegative integer or formula string")
        _strings(record["category_ids"], location + ".category_ids", unique=True)
        _strings(record["constraints"], location + ".constraints")
        _require(isinstance(record["status"], str) and record["status"] in {"defined", "family"}, location + ".status", "expected defined or family")
        if record["status"] == "family":
            _require(bool(record["constraints"]), location + ".constraints", "symbolic families must state parameter domains")
        _references(record["references"], location + ".references")
        if "related_ids" in record:
            _strings(record["related_ids"], location + ".related_ids", unique=True)
    elif collection == "categories":
        _required(record, "name knowl scalar object_axioms morphism_axioms unit_policy regularity", location)
        for key in ("name", "unit_policy", "regularity"):
            _text(record[key], location + "." + key)
        _text(record["scalar"], location + ".scalar", nullable=True)
        for key in ("object_axioms", "morphism_axioms"):
            _strings(record[key], location + "." + key)
    elif collection == "views":
        _required(record, "object_id category_id", location)
        for key in ("object_id", "category_id"):
            _text(record[key], location + "." + key)
        if "scalar" in record:
            _text(record["scalar"], location + ".scalar", nullable=True)
        if "parameters" in record:
            _require(isinstance(record["parameters"], dict), location + ".parameters", "expected an object")
        if "constraints" in record:
            _strings(record["constraints"], location + ".constraints")
    elif collection == "relationships":
        _required(record, "source target kind category_id statement knowl conditions evidence", location)
        for key in ("source", "target", "statement"):
            _text(record[key], location + "." + key)
        _text(record["category_id"], location + ".category_id", nullable=True)
        _require(isinstance(record["kind"], str) and record["kind"] in RELATION_KINDS, location + ".kind", "unknown relationship kind")
        if record["kind"] in STRUCTURAL_KINDS:
            _require(record["category_id"] is None, location, "structural relationship must have category_id null")
        if record["kind"] in MORPHISM_KINDS:
            _require(record["category_id"] is not None, location, "morphism relationship must specify category_id")
        if "parameters" in record:
            _require(isinstance(record["parameters"], dict), location + ".parameters", "expected an object")
    elif collection == "morphism_spaces":
        _required(record, "source_view target_view operation description knowl conditions evidence", location)
        for key in ("source_view", "target_view", "description"):
            _text(record[key], location + "." + key)
        _require(isinstance(record["operation"], str) and record["operation"] in OPERATIONS, location + ".operation", "expected hom, end, or aut")
        record.setdefault("coverage", "partial")
        _require(isinstance(record["coverage"], str) and record["coverage"] in {"complete", "partial"},
                 location + ".coverage", "expected complete or partial")
        if "result_object_ids" in record:
            _strings(record["result_object_ids"], location + ".result_object_ids", unique=True)
    elif collection == "magic_squares":
        _required(record, "name knowl field form row_object_ids column_object_ids cells evidence", location)
        for key in ("name", "field", "form"):
            _text(record[key], location + "." + key)
        for key in ("row_object_ids", "column_object_ids"):
            _strings(record[key], location + "." + key, unique=True)
            _require(bool(record[key]), location + "." + key, "axis cannot be empty")
        _require(isinstance(record["cells"], list), location + ".cells", "expected an array")
    if "knowl" in record:
        _knowl(record, registry, location)
    if "conditions" in record:
        _strings(record["conditions"], location + ".conditions")
    if "evidence" in record:
        _evidence(record["evidence"], location + ".evidence")


def load_catalog(paths: Iterable[Path], registry: Mapping[str, Any]) -> dict[str, Any]:
    """Load shards, resolve knowls and validate all links before exporting.

    A missing catalogue is represented by the caller not invoking this method.
    Each source collection is independently ID-unique across all shards.
    """
    records: dict[str, dict[str, dict[str, Any]]] = {name: {} for name in COLLECTIONS}
    locations: dict[tuple[str, str], str] = {}
    for path in sorted(paths):
        try:
            shard = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_json_object,
                               parse_constant=_reject_json_constant)
        except (OSError, ValueError) as exc:
            raise CatalogValidationError(f"{path}: {exc}") from exc
        _require(isinstance(shard, dict), str(path), "expected a JSON object")
        _require(type(shard.get("schema_version")) is int and shard["schema_version"] == SCHEMA_VERSION,
                 str(path), f"schema_version must be {SCHEMA_VERSION}")
        unknown = shard.keys() - set(COLLECTIONS) - {"schema_version", "description"}
        _require(not unknown, str(path), "unknown collections: " + ", ".join(sorted(unknown)))
        for collection in COLLECTIONS:
            values = shard.get(collection, [])
            _require(isinstance(values, list), f"{path}:{collection}", "expected an array")
            for index, source in enumerate(values):
                location = f"{path}:{collection}[{index}]"
                _require(isinstance(source, dict), location, "expected an object")
                record = copy.deepcopy(source)
                ident = record.get("id")
                pattern = VIEW_ID_RE if collection == "views" else ID_RE
                _require(isinstance(ident, str) and bool(pattern.fullmatch(ident)), location, "invalid or missing id")
                location += f" ({ident})"
                _require(ident not in records[collection], location, f"duplicate {collection} ID {ident!r}")
                _shape(record, collection, registry, location)
                records[collection][ident] = record
                locations[collection, ident] = location

    objects, categories, views = (records[key] for key in ("objects", "categories", "views"))
    for obj in objects.values():
        loc = locations["objects", obj["id"]]
        for category_id in obj["category_ids"]:
            _require(category_id in categories, loc, f"unknown category {category_id!r}")
            ident = f'{obj["id"]}@{category_id}'
            if ident in views:
                explicit = views[ident]
                _require(explicit["object_id"] == obj["id"] and explicit["category_id"] == category_id,
                         locations["views", ident], "default view ID belongs to a different object/category")
            else:
                views[ident] = {"id": ident, "object_id": obj["id"], "category_id": category_id}
            locations.setdefault(("views", ident), loc + f" default view {ident}")
        for related in obj.get("related_ids", []):
            _require(related in objects, loc, f"unknown related object {related!r}")
    for view in views.values():
        loc = locations["views", view["id"]]
        _require(view["object_id"] in objects, loc, f'unknown object {view["object_id"]!r}')
        _require(view["category_id"] in categories, loc, f'unknown category {view["category_id"]!r}')
        _require(view["category_id"] in objects[view["object_id"]]["category_ids"], loc,
                 "view category is not in its object's declared category memberships")
        view.setdefault("scalar", categories[view["category_id"]]["scalar"])
        if categories[view["category_id"]]["scalar"] is not None:
            _require(view["scalar"] == categories[view["category_id"]]["scalar"], loc,
                     "view scalar disagrees with category scalar")

    for rel in records["relationships"].values():
        loc = locations["relationships", rel["id"]]
        for endpoint in ("source", "target"):
            _require(rel[endpoint] in objects, loc, f"unknown {endpoint} object {rel[endpoint]!r}")
        category_id = rel["category_id"]
        if category_id is not None:
            _require(category_id in categories, loc, f"unknown category {category_id!r}")
            for endpoint in ("source", "target"):
                _require(category_id in objects[rel[endpoint]]["category_ids"], loc,
                         f"{endpoint} object does not belong to category {category_id!r}")
        parameters = rel.get("parameters", {})
        if "other_input_id" in parameters:
            _text(parameters["other_input_id"], loc + ".parameters.other_input_id")
            _require(parameters["other_input_id"] in objects, loc, "unknown other_input_id")
            _require(rel["kind"] == "construction", loc, "other_input_id is only valid for a construction")
        if "square_id" in parameters:
            _text(parameters["square_id"], loc + ".parameters.square_id")
            _require(parameters["square_id"] in records["magic_squares"], loc, "unknown square_id")
        if "transposed_relationship_id" in parameters:
            _text(parameters["transposed_relationship_id"], loc + ".parameters.transposed_relationship_id")
            _require(parameters["transposed_relationship_id"] in records["relationships"], loc,
                     "unknown transposed_relationship_id")
        if "cell" in parameters:
            cell = parameters["cell"]
            _require(isinstance(cell, list) and len(cell) == 2 and all(type(i) is int and i >= 0 for i in cell),
                     loc, "cell must be two nonnegative zero-based integer indices")
            if "square_id" in parameters:
                square = records["magic_squares"][parameters["square_id"]]
                _require(cell[0] < len(square["row_object_ids"]) and cell[1] < len(square["column_object_ids"]),
                         loc, "cell indices outside square axes")

    for space in records["morphism_spaces"].values():
        loc = locations["morphism_spaces", space["id"]]
        for endpoint in ("source_view", "target_view"):
            _require(space[endpoint] in views, loc, f"unknown {endpoint} {space[endpoint]!r}")
        source, target = views[space["source_view"]], views[space["target_view"]]
        _require(source["category_id"] == target["category_id"], loc, "Hom endpoints must belong to the same category")
        if space["operation"] in {"end", "aut"}:
            _require(source["id"] == target["id"], loc, "End/Aut endpoints must be the identical view")
        # Derived fields cannot be used to smuggle a different category or carrier.
        for key, value in (("category_id", source["category_id"]), ("source_object_id", source["object_id"]),
                           ("target_object_id", target["object_id"])):
            _require(key not in space or space[key] == value, loc, f"{key} disagrees with view endpoints")
            space[key] = value
        for ident in space.get("result_object_ids", []):
            _require(ident in objects, loc, f"unknown result object {ident!r}")

    for square in records["magic_squares"].values():
        loc = locations["magic_squares", square["id"]]
        for ident in square["row_object_ids"] + square["column_object_ids"]:
            _require(ident in objects, loc, f"unknown input object {ident!r}")
        occupied: set[tuple[str, str]] = set()
        for index, cell in enumerate(square["cells"]):
            cell_loc = f"{loc}.cells[{index}]"
            _require(isinstance(cell, dict), cell_loc, "expected a cell object")
            _required(cell, "row_object_id column_object_id output_object_id construction_relationship_ids", cell_loc)
            for key in ("row_object_id", "column_object_id", "output_object_id"):
                _text(cell[key], cell_loc + "." + key)
            pair = cell["row_object_id"], cell["column_object_id"]
            _require(pair[0] in square["row_object_ids"] and pair[1] in square["column_object_ids"], cell_loc, "cell input not on its axis")
            _require(pair not in occupied, cell_loc, "duplicate cell")
            occupied.add(pair)
            _require(cell["output_object_id"] in objects, cell_loc, "unknown output object")
            _strings(cell["construction_relationship_ids"], cell_loc + ".construction_relationship_ids", unique=True)
            _require(bool(cell["construction_relationship_ids"]), cell_loc, "cell must cite its construction relationships")
            for ident in cell["construction_relationship_ids"]:
                _require(ident in records["relationships"], cell_loc, f"unknown construction relationship {ident!r}")
                rel = records["relationships"][ident]
                _require(rel["kind"] == "construction" and rel["target"] == cell["output_object_id"], cell_loc,
                         "construction relationship must target the cell output")
                _require(rel["source"] in pair, cell_loc, "construction relationship source must be a cell input")
                parameters = rel.get("parameters", {})
                if "other_input_id" in parameters:
                    _require({rel["source"], parameters["other_input_id"]} == set(pair), cell_loc,
                             "construction inputs disagree with the cell axes")
                if "square_id" in parameters:
                    _require(parameters["square_id"] == square["id"], cell_loc, "construction cites a different square")
                if "cell" in parameters:
                    i, j = parameters["cell"]
                    _require(i < len(square["row_object_ids"]) and j < len(square["column_object_ids"]),
                             cell_loc, "construction cell coordinates outside axes")
                    _require(square["row_object_ids"][i] == pair[0] and square["column_object_ids"][j] == pair[1],
                             cell_loc, "construction cell coordinates disagree with axes")
        _require(len(occupied) == len(square["row_object_ids"]) * len(square["column_object_ids"]), loc, "incomplete magic-square cells")

    normalized = {"schema_version": SCHEMA_VERSION}
    for name in COLLECTIONS:
        normalized[name] = [records[name][ident] for ident in sorted(records[name])]
    normalized["counts"] = {name: len(records[name]) for name in COLLECTIONS}
    normalized["indexes"] = build_indexes(normalized)
    return normalized


def discover_catalog(content_roots: Iterable[Path], registry: Mapping[str, Any]) -> dict[str, Any] | None:
    paths = {path for root in content_roots for path in (root / "catalog" / "data").glob("*.json")}
    return load_catalog(paths, registry) if paths else None


def build_indexes(data: dict[str, Any]) -> dict[str, Any]:
    """Linear-size browser indexes. Values point into sorted collection arrays."""
    indexes: dict[str, Any] = {
        "by_id": {name: {row["id"]: index for index, row in enumerate(data[name])} for name in COLLECTIONS},
        "objects_by_category": {}, "objects_by_kind": {}, "objects_by_family": {},
        "views_by_object": {}, "views_by_category": {},
        "relationships_from": {}, "relationships_to": {}, "relationships_by_category": {},
        "construction_inputs": {},
        "morphisms_by_source": {}, "morphisms_by_target": {}, "morphism_lookup": {},
        "morphism_results_by_object": {},
    }

    def append(name: str, key: str, ident: str) -> None:
        indexes[name].setdefault(key, []).append(ident)

    for obj in data["objects"]:
        append("objects_by_kind", obj["kind"], obj["id"])
        append("objects_by_family", obj["family"], obj["id"])
        for category in obj["category_ids"]:
            append("objects_by_category", category, obj["id"])
    for view in data["views"]:
        append("views_by_object", view["object_id"], view["id"])
        append("views_by_category", view["category_id"], view["id"])
    for rel in data["relationships"]:
        append("relationships_from", rel["source"], rel["id"])
        append("relationships_to", rel["target"], rel["id"])
        if rel["category_id"] is not None:
            append("relationships_by_category", rel["category_id"], rel["id"])
        if rel["kind"] == "construction":
            for ident in sorted({rel["source"], rel.get("parameters", {}).get("other_input_id", rel["source"])}):
                append("construction_inputs", ident, rel["id"])
    for space in data["morphism_spaces"]:
        append("morphisms_by_source", space["source_view"], space["id"])
        append("morphisms_by_target", space["target_view"], space["id"])
        lookup = indexes["morphism_lookup"].setdefault(space["source_view"], {}).setdefault(space["target_view"], {})
        lookup.setdefault(space["operation"], []).append(space["id"])
        for ident in space.get("result_object_ids", []):
            append("morphism_results_by_object", ident, space["id"])
    return indexes


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


SQL_SCHEMA = """
PRAGMA foreign_keys = ON;
PRAGMA user_version = 1;
CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE objects (id TEXT PRIMARY KEY, name TEXT NOT NULL, kind TEXT NOT NULL, family TEXT NOT NULL,
                      knowl TEXT NOT NULL, status TEXT NOT NULL, payload TEXT NOT NULL);
CREATE INDEX objects_kind ON objects(kind, id);
CREATE INDEX objects_family ON objects(family, id);
CREATE TABLE categories (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
CREATE TABLE object_categories (object_id TEXT NOT NULL REFERENCES objects(id), category_id TEXT NOT NULL REFERENCES categories(id),
                                PRIMARY KEY(object_id, category_id));
CREATE INDEX object_categories_category ON object_categories(category_id, object_id);
CREATE TABLE views (id TEXT PRIMARY KEY, object_id TEXT NOT NULL REFERENCES objects(id),
                    category_id TEXT NOT NULL REFERENCES categories(id), payload TEXT NOT NULL);
CREATE INDEX views_object_category ON views(object_id, category_id, id);
CREATE INDEX views_category ON views(category_id, id);
CREATE TABLE relationships (id TEXT PRIMARY KEY, source TEXT NOT NULL REFERENCES objects(id),
                           target TEXT NOT NULL REFERENCES objects(id), kind TEXT NOT NULL,
                           category_id TEXT REFERENCES categories(id), payload TEXT NOT NULL);
CREATE INDEX relationships_source ON relationships(source, category_id, kind, id);
CREATE INDEX relationships_target ON relationships(target, category_id, kind, id);
CREATE INDEX relationships_category ON relationships(category_id, kind, id);
CREATE TABLE construction_inputs (relationship_id TEXT NOT NULL REFERENCES relationships(id),
    object_id TEXT NOT NULL REFERENCES objects(id), role TEXT NOT NULL CHECK(role IN ('source','other_input')),
    PRIMARY KEY(relationship_id, role));
CREATE INDEX construction_inputs_object ON construction_inputs(object_id, relationship_id);
CREATE TABLE morphism_spaces (id TEXT PRIMARY KEY, source_view TEXT NOT NULL REFERENCES views(id),
    target_view TEXT NOT NULL REFERENCES views(id), source_object_id TEXT NOT NULL REFERENCES objects(id),
    target_object_id TEXT NOT NULL REFERENCES objects(id), category_id TEXT NOT NULL REFERENCES categories(id),
    operation TEXT NOT NULL CHECK(operation IN ('hom','end','aut')), payload TEXT NOT NULL,
    CHECK(operation = 'hom' OR source_view = target_view));
CREATE INDEX morphisms_views ON morphism_spaces(source_view, target_view, operation, id);
CREATE INDEX morphisms_objects_category ON morphism_spaces(source_object_id, target_object_id, category_id, operation, id);
CREATE INDEX morphisms_target ON morphism_spaces(target_view, id);
CREATE INDEX morphisms_category ON morphism_spaces(category_id, operation, id);
CREATE TABLE morphism_results (morphism_id TEXT NOT NULL REFERENCES morphism_spaces(id),
    object_id TEXT NOT NULL REFERENCES objects(id), PRIMARY KEY(morphism_id, object_id));
CREATE INDEX morphism_results_object ON morphism_results(object_id, morphism_id);
CREATE TABLE magic_squares (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
"""


def export_catalog(data: dict[str, Any], output_dir: Path) -> None:
    """Write deterministic browser JSON and a freshly constructed SQLite file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path, database_path = output_dir / "catalog.json", output_dir / "catalog.sqlite"
    temporary = output_dir / "catalog.sqlite.tmp"
    temporary.unlink(missing_ok=True)
    try:
        with closing(sqlite3.connect(temporary)) as connection:
            connection.executescript(SQL_SCHEMA)
            connection.execute("INSERT INTO metadata VALUES (?, ?)", ("schema_version", str(SCHEMA_VERSION)))
            connection.execute("INSERT INTO metadata VALUES (?, ?)", ("counts", _json(data["counts"])))
            for name in ("categories", "magic_squares"):
                connection.executemany(f"INSERT INTO {name} VALUES (?, ?)", ((row["id"], _json(row)) for row in data[name]))
            connection.executemany("INSERT INTO objects VALUES (?, ?, ?, ?, ?, ?, ?)", (
                (row["id"], row["name"], row["kind"], row["family"], row["knowl"], row["status"], _json(row)) for row in data["objects"]))
            connection.executemany("INSERT INTO object_categories VALUES (?, ?)", (
                (row["id"], category) for row in data["objects"] for category in sorted(row["category_ids"])))
            connection.executemany("INSERT INTO views VALUES (?, ?, ?, ?)", (
                (row["id"], row["object_id"], row["category_id"], _json(row)) for row in data["views"]))
            connection.executemany("INSERT INTO relationships VALUES (?, ?, ?, ?, ?, ?)", (
                (row["id"], row["source"], row["target"], row["kind"], row["category_id"], _json(row)) for row in data["relationships"]))
            for row in data["relationships"]:
                if row["kind"] == "construction":
                    connection.execute("INSERT INTO construction_inputs VALUES (?, ?, ?)", (row["id"], row["source"], "source"))
                    other = row.get("parameters", {}).get("other_input_id")
                    if other is not None:
                        connection.execute("INSERT INTO construction_inputs VALUES (?, ?, ?)", (row["id"], other, "other_input"))
            connection.executemany("INSERT INTO morphism_spaces VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
                (row["id"], row["source_view"], row["target_view"], row["source_object_id"], row["target_object_id"],
                 row["category_id"], row["operation"], _json(row)) for row in data["morphism_spaces"]))
            connection.executemany("INSERT INTO morphism_results VALUES (?, ?)", (
                (row["id"], ident) for row in data["morphism_spaces"] for ident in sorted(row.get("result_object_ids", []))))
            connection.commit()
        # Close all SQLite handles before replacing an earlier export.
        temporary.replace(database_path)
        json_path.write_text(_json(data) + "\n", encoding="utf-8")
    finally:
        temporary.unlink(missing_ok=True)


class CatalogQuery:
    """Read-only indexed query interface; use as a context manager."""

    def __init__(self, database: Path):
        self.connection = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
        version = self.connection.execute("PRAGMA user_version").fetchone()[0]
        if version != SCHEMA_VERSION:
            self.connection.close()
            raise ValueError(f"Unsupported catalogue database version {version}")
        self.connection.execute("PRAGMA query_only = ON")

    def __enter__(self) -> CatalogQuery:
        return self

    def __exit__(self, *_: Any) -> None:
        self.connection.close()

    def _rows(self, sql: str, parameters: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
        return [json.loads(row[0]) for row in self.connection.execute(sql, parameters)]

    def get(self, collection: str, ident: str) -> dict[str, Any]:
        if collection not in COLLECTIONS:
            raise ValueError(f"Unknown collection {collection!r}")
        values = self._rows(f"SELECT payload FROM {collection} WHERE id = ?", (ident,))
        if not values:
            raise KeyError(f"Unknown {collection} ID {ident!r}")
        return values[0]

    def objects(self, *, category_id: str | None = None, kind: str | None = None,
                family: str | None = None) -> list[dict[str, Any]]:
        clauses, parameters = [], []
        if category_id is not None:
            self.get("categories", category_id)
            clauses.append("id IN (SELECT object_id FROM object_categories WHERE category_id = ?)")
            parameters.append(category_id)
        for key, value in (("kind", kind), ("family", family)):
            if value is not None:
                clauses.append(f"{key} = ?")
                parameters.append(value)
        where = " WHERE " + " AND ".join(clauses) if clauses else ""
        return self._rows("SELECT payload FROM objects" + where + " ORDER BY id", tuple(parameters))

    def views(self, object_id: str) -> list[dict[str, Any]]:
        self.get("objects", object_id)
        return self._rows("SELECT payload FROM views WHERE object_id = ? ORDER BY category_id, id", (object_id,))

    def common_categories(self, source: str, target: str) -> list[dict[str, Any]]:
        self.get("objects", source)
        self.get("objects", target)
        return self._rows("""SELECT c.payload FROM object_categories a
            JOIN object_categories b ON a.category_id = b.category_id
            JOIN categories c ON c.id = a.category_id
            WHERE a.object_id = ? AND b.object_id = ? ORDER BY c.id""", (source, target))

    def neighbors(self, object_id: str, *, direction: str = "both", category_id: str | None = None,
                  kind: str | None = None) -> list[dict[str, Any]]:
        self.get("objects", object_id)
        if direction not in {"both", "outgoing", "incoming"}:
            raise ValueError("direction must be both, outgoing, or incoming")
        if category_id is not None:
            self.get("categories", category_id)
        result = {}
        for endpoint in (("source", "target") if direction == "both" else (("source",) if direction == "outgoing" else ("target",))):
            clauses, parameters = [f"{endpoint} = ?"], [object_id]
            for key, value in (("category_id", category_id), ("kind", kind)):
                if value is not None:
                    clauses.append(f"{key} = ?")
                    parameters.append(value)
            for row in self._rows("SELECT payload FROM relationships WHERE " + " AND ".join(clauses), tuple(parameters)):
                result[row["id"]] = row
        if direction in {"both", "outgoing"} and kind in {None, "construction"}:
            clauses, parameters = ["inputs.object_id = ?"], [object_id]
            if category_id is not None:
                clauses.append("r.category_id = ?")
                parameters.append(category_id)
            for row in self._rows("SELECT r.payload FROM construction_inputs inputs JOIN relationships r "
                                  "ON r.id = inputs.relationship_id WHERE " + " AND ".join(clauses), tuple(parameters)):
                result[row["id"]] = row
        return [result[ident] for ident in sorted(result)]

    def morphisms(self, source_view: str, target_view: str, operation: str = "hom") -> dict[str, Any]:
        if operation not in OPERATIONS:
            raise ValueError("operation must be hom, end, or aut")
        source, target = self.get("views", source_view), self.get("views", target_view)
        if source["category_id"] != target["category_id"]:
            raise ValueError("Hom endpoints must belong to the same category")
        if operation != "hom" and source_view != target_view:
            raise ValueError("End/Aut endpoints must be the identical view")
        rows = self._rows("""SELECT payload FROM morphism_spaces
            WHERE source_view = ? AND target_view = ? AND operation = ? ORDER BY id""",
                          (source_view, target_view, operation))
        return {"status": "catalogued" if rows else "not-catalogued", "source_view": source_view,
                "target_view": target_view, "category_id": source["category_id"], "operation": operation, "records": rows}

    def counts(self) -> dict[str, int]:
        return json.loads(self.connection.execute("SELECT value FROM metadata WHERE key = 'counts'").fetchone()[0])
