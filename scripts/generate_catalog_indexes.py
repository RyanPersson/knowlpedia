#!/usr/bin/env python3
"""Regenerate the authored catalogue navigation from its sparse source shards."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import tomllib
from collections import defaultdict
from pathlib import Path


def metadata(path: Path) -> dict:
    match = re.match(r"\A\+\+\+\r?\n(.*?)\r?\n\+\+\+(?:\r?\n|\Z)", path.read_text(), re.S)
    if not match:
        raise ValueError(f"Missing front matter: {path}")
    return tomllib.loads(match.group(1))


def write_index(content: Path, knowl_id: str, title: str, summary: str, body: str) -> None:
    path = content / f"{knowl_id}.knowl.md"
    if path.exists() and metadata(path).get("generated_by") != "scripts/generate_catalog_indexes.py":
        raise ValueError(f"Refusing to overwrite an independently authored knowl: {path}")
    front = {
        "id": knowl_id, "title": title, "kind": "index", "summary": summary,
        "aliases": [], "domains": ["catalog"], "section_mode": "continuous",
        "prerequisites": [], "generated_by": "scripts/generate_catalog_indexes.py",
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("+++\n" + "".join(f"{k} = {json.dumps(v, ensure_ascii=False)}\n" for k, v in front.items())
                    + "+++\n\n" + body.strip() + "\n", encoding="utf-8")


def label(text: str) -> str:
    return text.replace("|", "&#124;").replace("\n", " ")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-package", type=Path, default=Path(__file__).resolve().parents[2] / "knowlpedia-content")
    parser.add_argument("--baseline", default="d1ad541e", help="Content revision before this batch")
    args = parser.parse_args()
    repo = args.content_package.resolve()
    content = repo / "content"
    shards = {p.stem: json.loads(p.read_text()) for p in sorted((content / "catalog/data").glob("*.json"))}
    objects = [o for shard in shards.values() for o in shard.get("objects", [])]
    categories = [c for shard in shards.values() for c in shard.get("categories", [])]
    relationships = [r for shard in shards.values() for r in shard.get("relationships", [])]
    morphisms = [m for shard in shards.values() for m in shard.get("morphism_spaces", [])]
    if len({o["id"] for o in objects}) != len(objects):
        raise ValueError("Duplicate catalogue object IDs")

    lane_labels = {
        "lie-groups": "Lie groups", "lie-algebras": "Lie algebras",
        "algebras": "Scalar, associative, and Jordan algebras", "arithmetic": "Fields, local objects, and orders",
        "magic-square": "Magic-square outputs and triality representations",
        "finite-sporadic": "Sporadic finite simple groups",
        "finite-lie-type": "Finite groups of Lie type",
        "finite-elementary": "Elementary finite groups and families",
    }
    unmapped = sorted(name for name, shard in shards.items()
                      if shard.get("objects") and name not in lane_labels)
    if unmapped:
        raise ValueError(f"Object shards need navigation labels before index generation: {', '.join(unmapped)}")
    links = []
    generated_count = 0
    for lane, title in lane_labels.items():
        lane_objects = shards.get(lane, {}).get("objects", [])
        finite_lane = lane.startswith("finite-")
        if finite_lane and not lane_objects:
            continue
        groups: dict[str, list] = defaultdict(list)
        for obj in lane_objects:
            groups[obj["family"]].append(obj)
        scope = ("Individual finite groups and constrained families retain distinct entries. "
                 "Orders are exact integers or formulas; simplicity is stated under each entry's parameter restrictions. "
                 if finite_lane else "Real and complex scalar choices have distinct entries. ")
        body = [f"{len(lane_objects)} separately identified objects and parameterized families. " + scope +
                "An isomorphism is a recorded relationship, not a reason to collapse the entries.\n\n"
                + ("[Open the finite-group table](/catalog/finite-groups/table/) · " if finite_lane else "")
                + "[Explore pairs and categories](/catalog/explorer/) · "
                "[[catalog|Catalogue overview]]\n"]
        for family, members in sorted(groups.items()):
            body += [f"\n## {family.replace('-', ' ').capitalize()}\n",
                     ("| Object | Order | Simplicity | Kind of entry |\n| --- | --- | --- | --- |" if finite_lane
                      else "| Object | Dimensions | Kind of entry |\n| --- | --- | --- |")]
            for obj in sorted(members, key=lambda o: o["id"]):
                status = "parameterized family" if obj["status"] == "family" else "specified object"
                if finite_lane:
                    finite = obj["properties"]["finite_group"]
                    order_tex = finite["order_tex"].replace("|", r"\vert")
                    simplicity = ("simple under the stated constraints" if finite["simple"] is True
                                  else "not simple" if finite["simple"] is False else "parameter-dependent")
                    body.append(f"| [[{obj['knowl']}|\\({obj['notation']}\\)]] | \\({order_tex}\\) | {simplicity} | {status} |")
                else:
                    dimensions = "; ".join(f"{k}: {v}" for k, v in obj["dimensions"].items()) or "not specified"
                    body.append(f"| [[{obj['knowl']}|\\({obj['notation']}\\)]] | {label(dimensions)} | {status} |")
        ident = f"catalog/{lane}-index"
        details = "orders, simplicity conditions, and category views" if finite_lane else "fields, dimensions, and category views"
        write_index(content, ident, title + " catalogue", f"A catalogue of {len(lane_objects)} objects with explicit {details}.", "\n".join(body))
        generated_count += 1
        links.append(f"- [[{ident}|{title} catalogue]] — {len(lane_objects)} entries.")

    body = [
        f"This catalogue contains **{len(objects)} separately identified objects and parameterized families**, "
        f"**{len(categories)} category conventions**, **{len(relationships)} recorded relationships**, and "
        f"**{len(morphisms)} Hom/End/Aut records**. Real and complex versions, split and compact forms, and the "
        "requested small sizes are explicit entries. A family entry states its parameter restrictions; "
        "it does not silently treat every parameter value as the same object.",
        "\n[Open the category explorer](/catalog/explorer/) · [[catalog/created-knowls|List of newly created knowls]]"
        + (" · [Explore the finite-group table](/catalog/finite-groups/table/)"
           if any("finite_group" in obj.get("properties", {}) for obj in objects) else ""),
        "\n## Long lists of objects\n", *links,
        "\n## How to compare objects\n",
        "[[catalog/morphisms/hom-end-aut-by-category|Hom, End, and Aut depend on the chosen category]]. "
        "Select two objects in the explorer, choose a shared category, then inspect the recorded maps. "
        "End and Aut use a single object with a specified structure. A missing entry means **not catalogued**, "
        "not that its Hom-set is empty. Complete and partial descriptions are labeled separately.",
        "\nA matrix Lie group such as \\(SL(2,\\mathbb C)\\) is not itself a vector space. "
        "Use smooth or holomorphic group maps for that object, and real-linear or complex-linear maps "
        "for its Lie algebra or a specified ambient vector space. Changing the algebra product is "
        "a construction, not merely a change of scalar field.",
        "\n## Worked comparisons\n",
        "- [[catalog/morphisms/jordan-unit-conventions|Jord, UJord, and Jord1: units change Hom and End]].",
        "- [[catalog/morphisms/jordan-maps-from-the-scalar-algebra|Jordan maps from the scalar algebra are idempotents]].",
        "- [[catalog/morphisms/complex-numbers-linear-versus-algebra-maps|The complex numbers as a real or complex vector space and algebra]].",
        "- [[catalog/morphisms/linear-endomorphisms-of-sl2-complex|Real and complex linear endomorphisms of sl(2,C)]].",
        "- [[catalog/morphisms/sl2-complex-real-versus-holomorphic-maps|Real versus holomorphic maps on SL(2,C)]].",
        "- [[catalog/morphisms/restriction-of-scalars-endomorphisms|K-linear, F-linear, K-algebra, and F-algebra endomorphisms]].",
        "- [[catalog/morphisms/gaussian-field-endomorphisms|Q(i): linear maps versus algebra maps]].",
        "- [[catalog/morphisms/finite-field-homomorphisms-by-category|Empty field Hom-sets versus the zero ring map]].",
        "- [[catalog/arithmetic/finite-field-linear-and-field-maps|Finite-field linear maps versus Frobenius automorphisms]].",
        "\n## Low dimensions and the magic square\n",
        "The [[catalog/relationships/compact-freudenthal-magic-square|compact real Freudenthal magic square]] "
        "is backed by all 16 data cells, with both input algebras and each output Lie algebra identified. "
        "Changing a composition algebra to a split form requires a new real-form calculation; "
        "the compact table is not presented as a table of all real forms.",
        "\nThe low-dimensional entries retain their own identities even when isomorphic. "
        "This records, for example, the distinctions between Spin groups and their orthogonal quotients, "
        "between one-dimensional Hermitian constructions, and between the three Spin(8) representations "
        "related by triality.",
        "\n## Category conventions\n",
    ]
    by_knowl: dict[str, list] = defaultdict(list)
    for category in categories:
        by_knowl[category["knowl"]].append(category["name"])
    for knowl, names in sorted(by_knowl.items()):
        title = metadata(content / f"{knowl}.knowl.md")["title"]
        body.append(f"- [[{knowl}|{title}]] — {label('; '.join(names))}.")
    body += [
        "\n## Data and proof status\n",
        "Each recorded relationship names its category or identifies itself as a construction, "
        "states its conditions, and carries evidence. The catalogue does not infer arbitrary compositions "
        "or inverses. The present evidence is mathematical exposition and checked literature, **not Lean proofs**. "
        "Formal-proof references are reserved for future verified declarations.",
        "\n[Download the indexed JSON](/indexes/catalog.json) · [Download the SQLite catalogue](/indexes/catalog.sqlite)",
        "\n## Separate algebra-class additions\n",
        "The [[knowlification/orders-and-fractional-ideals-index|orders and fractional ideals reading list]] "
        "covers the separate transcript request, including new definitions and existing prerequisites reused.",
    ]
    write_index(content, "catalog", "Mathematical object catalogue", "Objects, category-dependent morphisms, low-dimensional relationships, and the compact magic square.", "\n".join(body))

    baseline = set(subprocess.check_output(["git", "ls-tree", "-r", "--name-only", args.baseline, "--", "content"], cwd=repo, text=True).splitlines())
    new_pages = []
    for path in sorted((content / "catalog").rglob("*.knowl.md")):
        if path.relative_to(repo).as_posix() not in baseline and path.name != "created-knowls.knowl.md":
            new_pages.append(metadata(path))
    if "content/catalog.knowl.md" not in baseline:
        new_pages.append(metadata(content / "catalog.knowl.md"))
    listing_is_new = "content/catalog/created-knowls.knowl.md" not in baseline
    new_count = len(new_pages) + int(listing_is_new)
    grouped: dict[str, list] = defaultdict(list)
    for meta in new_pages:
        parts = meta["id"].split("/")
        group = parts[1] if len(parts) > 2 else "navigation"
        grouped[group].append(meta)
    listing = [f"This batch creates **{new_count} catalogue knowls and navigation pages**"
               + (", including this list. " if listing_is_new else ". ")
               + "Existing canonical knowls are reused by many additional object records; "
               "the [[catalog|object catalogue]] includes both new and reused entries.",
               "\n[Open the category explorer](/catalog/explorer/) · [[catalog|Catalogue overview]]",
               "\nThe separate [[knowlification/orders-and-fractional-ideals-index|orders and fractional ideals additions]] "
               "have their own list and are not counted here."]
    for group, pages in sorted(grouped.items()):
        listing.append(f"\n## {group.replace('-', ' ').capitalize()} ({len(pages)})\n")
        for meta in sorted(pages, key=lambda m: (m["title"].casefold(), m["id"])):
            listing.append(f"- [[{meta['id']}|{meta['title']}]]")
    write_index(content, "catalog/created-knowls", "New knowls in the catalogue batch", "The complete list of new catalogue definitions, examples, relationships, and navigation pages.", "\n".join(listing))
    print(f"Generated {generated_count + 2} indexes for {len(objects)} objects and {new_count} new catalogue pages.")


if __name__ == "__main__":
    main()
