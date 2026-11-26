#!/usr/bin/env python3
"""Package a pinned readable grh-lean checkout and its kernel dependency graph.

Run lake build +Main:olean in grh/, then lake env lean --run
/path/to/grh_lean_dependencies.lean Main <the five names in ROOTS> > graph.ndjson.
Run this script with --edition grh --graph graph.ndjson --toolchain <Lean prefix>
--output <content package>/content/grh-lean/declarations.zip.
"""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOTS = ["riemannHypothesis", "riemannZeta_eq_zero_re", "LFunction_ne_zero_of_half_lt_re",
         "LFunction_eq_zero_re", "LFunction_eq_zero_re_of_isPrimitive"]
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
LEAN_REV = "eb6cafb7290e8bd5f2937522d8d804f58f02bafc"  # Lean 4.35.0
SOURCE_DIGEST = "66a5fd841a06a1beb45acbea4960dd5f47d2ebe9022b9364428cc57211a7ee57"
CHUNK = 256


def json_bytes(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()


def write_item(archive, name, data):
    member = zipfile.ZipInfo(name)
    member.external_attr = 0o644 << 16
    archive.writestr(member, data)


def write_json_gz(archive, name, value):
    write_item(archive, name, gzip.compress(json_bytes(value), compresslevel=6, mtime=0))


def lean_module(path):
    return ".".join(path.with_suffix("").parts)


def source_name(module):
    return module.replace(".", "/") + ".lean"


def source_occurrences(ilean, by_name):
    """Keep Lean's resolved constant usages, including notation, with LSP UTF-16 ranges."""
    result = {}
    for key, uses in json.loads(ilean.read_bytes())["references"].items():
        target = json.loads(key).get("c", {}).get("n")
        if target not in by_name:
            continue
        for first, left, last, right, *_ in uses["usages"]:
            if first == last and left < right:
                result.setdefault(first, []).append([left, right, by_name[target]])
    return {line: sorted(set(tuple(item) for item in spans)) for line, spans in result.items()}


def build(edition, graph_path, toolchain, output):
    src = edition / "src"
    source_files = {lean_module(p.relative_to(src)): p for p in sorted(src.rglob("*.lean"))}
    if len(source_files) != 803 or (edition/"lean-toolchain").read_text().strip() != "leanprover/lean4:v4.35.0":
        raise ValueError("Expected the pinned 803-module readable edition and Lean v4.35.0")
    digest = hashlib.sha256()
    files = list(source_files.values()) + [edition/name for name in (
        "lake-manifest.json", "lean-toolchain", "LICENSE", "NOTICE", "ATTRIBUTION.md")]
    for file in sorted(files):
        digest.update(file.relative_to(edition).as_posix().encode() + b"\0" + hashlib.sha256(file.read_bytes()).digest())
    if digest.hexdigest() != SOURCE_DIGEST:
        raise ValueError("The source, license or package pins differ from the published readable edition")
    pins = json.loads((edition / "lake-manifest.json").read_text())["packages"]
    packages = {"grh": ["https://github.com/lsernau/grh-lean", REVISION, "grh/src/"],
                "Lean": ["https://github.com/leanprover/lean4", LEAN_REV, "src/"]}
    module_roots = {}
    for package in pins:
        name = package["name"]
        packages[name] = [package["url"].removesuffix(".git"), package["rev"], ""]
        package_dir = edition / ".lake/packages" / name / ".lake/build/lib/lean"
        if package_dir.is_dir():
            for child in package_dir.iterdir():
                if child.is_dir() or child.suffix == ".ilean":
                    module_roots[child.stem] = (name, package_dir)
    if packages["mathlib"][1] != "56a005855ea17e0b0958f73ec801ae140b0a1679":
        raise ValueError("Unexpected Mathlib revision")
    graph = {}
    for line in graph_path.open():
        name, mod, kind, deps, block = json.loads(line)
        if name in graph or not mod:
            raise ValueError(f"Duplicate or unattributed constant {name}")
        graph[name] = [mod, kind, deps, block]
    if not all(root in graph for root in ROOTS):
        raise ValueError("The graph does not include all five roots")
    axioms = {n for n, row in graph.items() if row[1] == "axiom"}
    if axioms != AXIOMS:
        raise ValueError(f"Unexpected axioms: {sorted(axioms)}")

    project_ilean = edition / ".lake/build/lib/lean"
    lean_ilean = toolchain / "lib/lean"
    metadata = {}
    positions = {}
    source_only = {}
    by_module = set(source_files) | {row[0] for row in graph.values()}
    for mod in sorted(by_module):
        if mod in source_files:
            repo, directory = "grh", project_ilean
        else:
            repo, directory = module_roots.get(mod.split(".")[0], ("Lean", lean_ilean))
        ilean = directory / Path(source_name(mod)).with_suffix(".ilean")
        imports = []
        if ilean.is_file():
            lsif = json.loads(ilean.read_bytes())
            imports = [v[0] for v in lsif["directImports"]]
            for name, span in lsif.get("decls", {}).items():
                if name in graph and graph[name][0] == mod:
                    positions[name] = span
                elif repo == "grh" and name not in graph:
                    # Named source declarations supplied for browsing even when the kernel
                    # does not use them in any of the five statements.
                    positions[name] = span
                    source_only[name] = mod
        elif repo == "grh":
            raise ValueError(f"Build the source module {mod} before generating the index")
        metadata[mod] = [repo, imports]

    project_names = sorted({n for n, row in graph.items() if row[0] in source_files} | source_only.keys())
    library_names = sorted(n for n, row in graph.items() if row[0] not in source_files)
    names = project_names + library_names
    by_name = {n: i for i, n in enumerate(names)}
    module_names = sorted(metadata, key=lambda n: (n not in source_files, n))
    by_module = {n: i for i, n in enumerate(module_names)}
    members = [[] for _ in module_names]
    kinds = sorted({x[1] for x in graph.values()} | {"source declaration"})
    rows = []
    for i, name in enumerate(names):
        if name in graph:
            mod, kind, deps, block = graph[name]
        else:
            mod, kind, deps, block = source_only[name], "source declaration", [], []
        mi = by_module[mod]
        members[mi].append(i)
        span = positions.get(name, [])
        # Library source has a permalink. For project source preserve the complete
        # declaration and identifier ranges for both code and explanatory comments.
        rows.append([mi, kinds.index(kind), 0, span if mod in source_files else span[:1],
                     sorted(by_name[n] for n in deps), sorted(by_name[n] for n in block)])
    for j, root in enumerate(ROOTS):
        bit = 1 << j
        pending = [by_name[root]]
        while pending:
            i = pending.pop()
            row = rows[i]
            if row[2] & bit:
                continue
            row[2] |= bit
            pending.extend(row[4])
            pending.extend(row[5])
    if sum(bool(row[2]) for row in rows) != len(graph):
        raise ValueError("Unreachable constants in the supplied graph")

    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(".zip.tmp")
    with zipfile.ZipFile(temp, "w") as archive:
        for doc in ["LICENSE", "NOTICE", "ATTRIBUTION.md"]:
            write_item(archive, doc, (edition/doc).read_bytes())
        for k in range(0, len(names), CHUNK):
            write_json_gz(archive, f"records/{k//CHUNK}.json.gz", rows[k:k+CHUNK])
        modules = []
        for mod in module_names:
            mi = by_module[mod]
            repo, imports = metadata[mod]
            modules.append([mod, repo, imports, members[mi]])
            if repo == "grh":
                code = source_files[mod].read_text()
                ilean = project_ilean / Path(source_name(mod)).with_suffix(".ilean")
                write_json_gz(archive, f"source/{mi}.json.gz", {
                    "lines": code.splitlines(), "uses": source_occurrences(ilean, by_name)})
        write_json_gz(archive, "modules.json.gz", modules)
        write_json_gz(archive, "project.json.gz", project_names)
        write_json_gz(archive, "libraries.json.gz", library_names)

        index = {"version": 1, "revision": REVISION, "sourceDigest": SOURCE_DIGEST, "toolchain": "Lean 4.35.0",
                 "chunk": CHUNK, "projectCount": len(project_names), "count": len(names),
                 "closure": len(graph), "sourceModules": len(source_files), "kinds": kinds,
                 "roots": [by_name[r] for r in ROOTS], "rootNames": ROOTS,
                 "axioms": sorted(AXIOMS), "packages": packages}
        write_item(archive, "manifest.json", json_bytes(index))
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode="wb", mtime=0) as handle:
            handle.write(b"name\tmodule\tkind\tpublic_theorem_roots\texpression_dependencies\tkernel_block_members\n")
            for name, row in zip(names, rows):
                if not row[2]:
                    continue
                fields = [name, module_names[row[0]], kinds[row[1]],
                          json.dumps([r for j,r in enumerate(ROOTS) if row[2] & (1 << j)]),
                          json_bytes([names[i] for i in row[4]]).decode(),
                          json_bytes([names[i] for i in row[5]]).decode()]
                handle.write(("\t".join(fields)+"\n").encode())
        write_item(archive, "dependencies.tsv.gz", buffer.getvalue())
    temp.replace(output)
    print(f"{len(graph):,} reachable declarations, {len(source_only):,} additional source declarations, "
          f"{len(source_files)} project modules, {output.stat().st_size:,} archive bytes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for arg in ("edition", "graph", "toolchain", "output"):
        parser.add_argument("--"+arg, required=True, type=Path)
    args = parser.parse_args()
    build(args.edition.resolve(), args.graph, args.toolchain.resolve(), args.output)
