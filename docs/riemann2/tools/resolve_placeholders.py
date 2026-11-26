#!/usr/bin/env python3
"""Resolve [[?c:name|text]] and [[?lean:Name|text]] placeholders under content/proofs (and new subject knowls).

registry.tsv: canonical-or-alias concept name <TAB> knowl id   (several names may map to one id)
Lean names come from the `lean = [...]` front matter of knowls under content/.
Usage: resolve_placeholders.py [--apply] [paths...]
Without --apply only reports. Unresolved placeholders are listed in unresolved-{c,lean}.tsv.
"""
import glob, os, re, sys, tomllib, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.normpath(os.path.join(ROOT, "..", "..", "knowlpedia-content", "content"))

def norm(name):
    s = name.strip().casefold().replace("–", "-").replace("—", "-").replace("’", "'")
    s = re.sub(r"\s+", " ", s)
    return re.sub(r"[^a-z0-9\-' ()/+,.]", "", s)

def variants(key):
    yield key
    if key.endswith("ies"): yield key[:-3] + "y"
    if key.endswith("es"): yield key[:-2]
    if key.endswith("s"): yield key[:-1]

def front(path):
    t = open(path, encoding="utf-8").read()
    if not t.startswith("+++\n"): return None, t
    e = t.find("\n+++\n", 4)
    return tomllib.loads(t[4:e]), t

def main():
    apply = "--apply" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = []
    for p in paths or [os.path.join(CONTENT, "proofs")]:
        files += glob.glob(os.path.join(p, "**", "*.knowl.md"), recursive=True) if os.path.isdir(p) else [p]
    reg = {}
    rp = os.path.join(ROOT, "registry.tsv")
    if os.path.exists(rp):
        for line in open(rp, encoding="utf-8"):
            f = line.rstrip("\n").split("\t")
            if len(f) >= 2 and f[0].strip() and f[1].strip():
                reg[norm(f[0])] = f[1].strip()
    ids = set()
    lean = {}
    dup = collections.defaultdict(set)
    for path in glob.glob(os.path.join(CONTENT, "**", "*.knowl.md"), recursive=True):
        try:
            meta, _ = front(path)
        except Exception as exc:
            print("BAD FRONT MATTER", path, exc); continue
        if not meta: continue
        ids.add(meta["id"])
        for name in meta.get("lean", []) or []:
            dup[name].add(meta["id"])
            lean.setdefault(name, meta["id"])
    # suffix index for lean names written without the full namespace
    suffix = collections.defaultdict(set)
    for name, kid in lean.items():
        parts = name.split(".")
        for i in range(len(parts)):
            suffix[".".join(parts[i:])].add(kid)
    unresolved_c, unresolved_l = collections.Counter(), collections.Counter()
    stats = collections.Counter()
    pat = re.compile(r"\[\[\?(c|lean):([^\]|]+)(\|([^\]]*))?\]\]")
    for path in files:
        meta, text = front(path)
        def sub(m):
            kind, name, text_ = m.group(1), m.group(2).strip(), m.group(4)
            shown = text_ if text_ is not None else name
            target = None
            if kind == "c":
                for v in variants(norm(name)):
                    if v in reg: target = reg[v]; break
                if target and target not in ids:
                    stats["c-target-missing-file"] += 1
                    unresolved_c[name + "  -> (no file) " + target] += 1
                    return m.group(0)
                if not target: unresolved_c[name] += 1
            else:
                cands = suffix.get(name) or suffix.get(name.removeprefix("New.")) or set()
                if not cands:
                    # the area may write D.foo for New.Data.foo
                    alt = re.sub(r"^D\.", "New.Data.", name)
                    alt = re.sub(r"^P\.", "New.Parameters.", alt)
                    cands = suffix.get(alt) or suffix.get(alt.removeprefix("New.")) or set()
                if len(cands) == 1: target = next(iter(cands))
                else: unresolved_l[name + ("  (ambiguous: %s)" % ", ".join(sorted(cands)) if cands else "")] += 1
            if not target:
                stats["unresolved-" + kind] += 1
                return m.group(0)
            stats["resolved-" + kind] += 1
            if meta and target == meta.get("id"):
                return shown
            return f"[[{target}|{shown}]]"
        new = pat.sub(sub, text)
        if apply and new != text:
            open(path, "w", encoding="utf-8").write(new)
    for kind, counter in (("c", unresolved_c), ("lean", unresolved_l)):
        with open(os.path.join(ROOT, f"unresolved-{kind}.tsv"), "w", encoding="utf-8") as fh:
            for name, n in counter.most_common():
                fh.write(f"{n}\t{name}\n")
    multi = {k: v for k, v in dup.items() if len(v) > 1}
    print(dict(stats), "| files", len(files), "| lean names", len(lean), "| lean names claimed by >1 knowl", len(multi),
          "| distinct unresolved c", len(unresolved_c), "lean", len(unresolved_l))

if __name__ == "__main__":
    main()
