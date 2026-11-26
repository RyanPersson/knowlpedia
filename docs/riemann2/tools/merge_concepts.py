#!/usr/bin/env python3
"""Merge the per-area concept sidecars into one list, grouped by normalised name."""
import csv, glob, os, re, sys, collections, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def norm(name: str) -> str:
    s = name.strip().casefold()
    s = s.replace("–", "-").replace("—", "-").replace("’", "'")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9\-' ()/+,.]", "", s)
    return s

def main():
    groups = collections.OrderedDict()
    bad = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "concepts", "*.tsv"))):
        area = os.path.basename(path)[:-4]
        for ln, line in enumerate(open(path, encoding="utf-8"), 1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            f = line.split("\t")
            if len(f) < 5:
                bad += 1
                print(f"short row {path}:{ln}: {line[:80]}", file=sys.stderr)
                f += [""] * (7 - len(f))
            f += [""] * (7 - len(f))
            name, kind, existing, subject, definition, prereqs, lean = f[:7]
            g = groups.setdefault(norm(name), {"names": collections.Counter(), "kinds": collections.Counter(),
                "existing": collections.Counter(), "subjects": collections.Counter(), "defs": [], "prereqs": set(), "lean": set(), "areas": set()})
            g["names"][name.strip()] += 1
            g["kinds"][kind.strip()] += 1
            if existing.strip():
                g["existing"][existing.strip()] += 1
            if subject.strip():
                g["subjects"][subject.strip()] += 1
            g["defs"].append((area, definition.strip()))
            g["prereqs"].update(p.strip() for p in prereqs.split(";") if p.strip())
            g["lean"].update(p.strip() for p in re.split(r"[;,]", lean) if p.strip())
            g["areas"].add(area)
    out = []
    for key, g in groups.items():
        out.append({"key": key, "name": g["names"].most_common(1)[0][0], "names": dict(g["names"]),
                    "kind": g["kinds"].most_common(1)[0][0], "existing": dict(g["existing"]),
                    "subjects": dict(g["subjects"]), "defs": g["defs"], "prereqs": sorted(g["prereqs"]),
                    "lean": sorted(g["lean"]), "areas": sorted(g["areas"])})
    json.dump(out, open(os.path.join(ROOT, "concepts-merged.json"), "w"), indent=1, ensure_ascii=False)
    new = [o for o in out if not any(k != "NEW" for k in o["existing"])]
    print(f"{len(out)} distinct concepts, {len(new)} with no existing id claimed, {bad} malformed rows")

if __name__ == "__main__":
    main()
