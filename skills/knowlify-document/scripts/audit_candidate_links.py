#!/usr/bin/env python3
"""Find likely omitted Knowlpack links without modifying source files."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from inventory_knowls import inventory, read_frontmatter


WIKILINK = re.compile(r"\[\[([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)(?:#[^|\]]+)?\|(?:(?!\]\]).)*\]\]", re.DOTALL)
PROTECTED = re.compile(
    r"(\[\[(?:(?!\]\]).)*\]\]|```.*?```|`[^`\n]*`|\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)|\[[^\]\n]+\]\([^\)\n]+\)|<[^>\n]+>)",
    re.DOTALL,
)
GENERIC = {
    "cover", "covers", "function", "functions", "map", "maps", "object", "objects",
    "point", "points", "set", "sets", "space", "spaces", "topology",
}
COMPOUND_PREFIXES = {"affine", "algebraic", "base", "closed", "constant", "étale", "etale", "finite", "generic", "group", "local", "principal", "projective", "proper", "small"}
COMPOUND_SUFFIXES = {"algebra", "bundle", "condition", "corollary", "extension", "field", "group", "lemma", "morphism", "point", "ring", "scheme", "site", "space", "theorem", "topology"}
IRREGULAR_PLURALS = {
    "analysis": "analyses", "basis": "bases", "category": "categories", "index": "indices",
    "matrix": "matrices", "simplex": "simplices", "vertex": "vertices",
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).casefold()


def pluralize(term: str) -> str | None:
    words = term.split()
    if not words or not re.fullmatch(r"[A-Za-z][A-Za-z'-]*", words[-1]):
        return None
    last = words[-1]
    low = last.casefold()
    if low in IRREGULAR_PLURALS:
        words[-1] = IRREGULAR_PLURALS[low]
        return " ".join(words)
    if low.endswith("ies") or low.endswith("ses") or low.endswith("xes") or low.endswith("ches") or low.endswith("shes"):
        return None
    if low.endswith("y") and len(last) > 1 and low[-2] not in "aeiou":
        words[-1] = last[:-1] + "ies"
    elif low.endswith(("s", "x", "z", "ch", "sh")):
        words[-1] = last + "es"
    else:
        words[-1] = last + "s"
    return " ".join(words)


def body_and_offset(text: str) -> tuple[str, int]:
    if not text.startswith("+++\n"):
        return text, 0
    end = text.find("\n+++\n", 4)
    if end < 0:
        raise ValueError("missing closing TOML front matter")
    start = end + 5
    return text[start:], text[:start].count("\n")


def mask_protected(text: str) -> str:
    chars = list(text)
    for match in PROTECTED.finditer(text):
        for index in range(match.start(), match.end()):
            if chars[index] != "\n":
                chars[index] = " "
    return "".join(chars)


def source_files(scopes: list[Path], content_root: Path) -> list[Path]:
    paths: set[Path] = set()
    for scope in scopes or [content_root]:
        scope = scope if scope.is_absolute() else content_root / scope
        scope = scope.resolve()
        if not scope.exists():
            raise ValueError(f"scope does not exist: {scope}")
        if scope.is_file() and scope.name.endswith(".knowl.md"):
            paths.add(scope)
        elif scope.is_dir():
            paths.update(path.resolve() for path in scope.rglob("*.knowl.md"))
    if scopes and not paths:
        raise ValueError("explicit scopes contained no .knowl.md files")
    return sorted(paths)


def load_decisions(path: Path | None) -> dict[str, dict]:
    if not path or not path.exists():
        return {}
    decisions: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            item = json.loads(line)
            decisions[str(item["candidate_id"])] = item
    return decisions


def build_lexicon(records: list[dict]) -> dict[str, list[dict]]:
    lexicon: dict[str, list[dict]] = {}
    for record in records:
        surfaces: dict[str, tuple[str, int]] = {record["title"]: ("exact_title", 30)}
        for alias in record["aliases"]:
            alias = alias.strip()
            if not alias or ("-" in alias and " " not in alias):
                continue
            surfaces.setdefault(alias, ("curated_alias", 25))
        plural = pluralize(record["title"])
        if plural:
            surfaces.setdefault(plural, ("generated_inflection", 28))
        for surface, (origin, base_score) in surfaces.items():
            key = normalize(surface)
            if len(key) < 3:
                continue
            lexicon.setdefault(key, []).append(
                {"surface": surface, "target_id": record["id"], "origin": origin, "base_score": base_score,
                 "target_kind": record["kind"]}
            )
    return lexicon


def compile_pattern(lexicon: dict[str, list[dict]]) -> re.Pattern[str]:
    surfaces = sorted(lexicon, key=lambda value: (-len(value), value))
    return re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(value) for value in surfaces) + r")(?![\w-])", re.IGNORECASE)


def context_for(body: str, start: int, end: int) -> str:
    left = max(body.rfind("\n", 0, start), body.rfind(". ", 0, start))
    right_newline = body.find("\n", end)
    right_period = body.find(". ", end)
    rights = [value for value in (right_newline, right_period + 1 if right_period >= 0 else -1) if value >= 0]
    right = min(rights) if rights else len(body)
    return re.sub(r"\s+", " ", body[left + 1:right].strip())[:300]


def candidate_id(source_id: str, normalized_surface: str, targets: list[str]) -> str:
    payload = "\0".join([source_id, normalized_surface, *targets])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:20]


def audit_file(path: Path, content_root: Path, lexicon: dict[str, list[dict]], pattern: re.Pattern[str],
               decisions: dict[str, dict], min_score: int, include_suppressed: bool) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    meta = read_frontmatter(path)
    source_id = str(meta["id"])
    body, line_offset = body_and_offset(text)
    masked = mask_protected(body)
    linked_targets = set(WIKILINK.findall(body))
    source_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    source_domain = source_id.split("/", 1)[0]
    emitted_targets: set[tuple[str, ...]] = set()
    output: list[dict] = []

    for match in pattern.finditer(masked):
        key = normalize(match.group(0))
        options = lexicon[key]
        targets = sorted({str(option["target_id"]) for option in options})
        target_key = tuple(targets)
        if source_id in targets or target_key in emitted_targets:
            continue
        emitted_targets.add(target_key)
        already_linked = any(target in linked_targets for target in targets)
        ambiguous = len(targets) > 1
        best = max(options, key=lambda option: int(option["base_score"]))
        score = int(best["base_score"])
        features = [str(best["origin"]), "first_occurrence"]
        score += 10
        if len(key.split()) > 1:
            score += 12
            features.append("multiword")
        if any(target.split("/", 1)[0] == source_domain for target in targets):
            score += 15
            features.append("same_domain")
        if any("foundations" in target or target.startswith("shared-foundations/") for target in targets):
            score += 5
            features.append("foundational_target")
        if key in GENERIC:
            score -= 25
            features.append("generic_single_word")
        if ambiguous:
            score -= 30
            features.append("ambiguous_target")
        if already_linked:
            score -= 20
            features.append("target_already_linked")
        before = re.search(r"([A-Za-zÀ-ž-]+)\s+$", masked[: match.start()])
        after = re.match(r"\s+([A-Za-zÀ-ž-]+)", masked[match.end() :])
        if ((before and normalize(before.group(1)) in COMPOUND_PREFIXES) or
                (after and normalize(after.group(1)) in COMPOUND_SUFFIXES)):
            score -= 30
            features.append("partial_compound")
        if (score < min_score or already_linked) and not include_suppressed:
            continue

        line = line_offset + body.count("\n", 0, match.start()) + 1
        column = match.start() - body.rfind("\n", 0, match.start())
        stable_id = candidate_id(source_id, key, targets)
        prior = decisions.get(stable_id)
        current_context = context_for(body, match.start(), match.end())
        disposition = "pending"
        reason_code = None
        note = None
        stale_decision = False
        decision_rebased = False
        if prior:
            stale_decision = prior.get("source_sha256") != source_hash
            if stale_decision and prior.get("context") == current_context and prior.get("surface") == body[match.start():match.end()] and prior.get("target_ids") == targets:
                stale_decision = False
                decision_rebased = True
            if not stale_decision:
                disposition = prior.get("disposition", "pending")
                reason_code = prior.get("reason_code")
                note = prior.get("note")
        output.append(
            {
                "candidate_id": stable_id,
                "source_id": source_id,
                "source_path": str(path.relative_to(content_root)),
                "line": line,
                "column": column,
                "surface": body[match.start():match.end()],
                "normalized_surface": key,
                "target_ids": targets,
                "match_origin": best["origin"],
                "score": score,
                "features": features,
                "context": current_context,
                "disposition": disposition,
                "reason_code": reason_code,
                "note": note,
                "source_sha256": source_hash,
                "stale_decision": stale_decision,
                "decision_rebased": decision_rebased,
            }
        )
    return output


def write_markdown(candidates: list[dict], output: Path) -> None:
    lines = ["# Candidate knowl links", "", f"Candidates: {len(candidates)}", ""]
    for item in candidates:
        targets = ", ".join(f"`{target}`" for target in item["target_ids"])
        lines.extend(
            [
                f"## `{item['source_path']}:{item['line']}` — {item['surface']}", "",
                f"- Candidate: `{item['candidate_id']}`",
                f"- Target: {targets}",
                f"- Score: {item['score']} ({', '.join(item['features'])})",
                f"- Decision: **{item['disposition']}**",
                f"- Context: {item['context']}", "",
            ]
        )
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", type=Path, required=True)
    parser.add_argument("--scope", type=Path, action="append", default=[])
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--format", choices=("json", "jsonl", "markdown"), default="jsonl")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--min-score", type=int, default=40)
    parser.add_argument("--include-suppressed", action="store_true")
    parser.add_argument("--fail-on-pending-high", type=int)
    args = parser.parse_args()

    content_root = args.content_root.resolve()
    records = inventory(content_root)
    lexicon = build_lexicon(records)
    pattern = compile_pattern(lexicon)
    decisions = load_decisions(args.decisions.resolve() if args.decisions else None)
    try:
        files = source_files(args.scope, content_root)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    candidates = [
        item
        for path in files
        for item in audit_file(path, content_root, lexicon, pattern, decisions, args.min_score, args.include_suppressed)
    ]
    candidates.sort(key=lambda item: (item["source_path"], item["line"], -item["score"], item["surface"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.format == "json":
        args.output.write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    elif args.format == "jsonl":
        args.output.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in candidates), encoding="utf-8")
    else:
        write_markdown(candidates, args.output)
    pending_high = [item for item in candidates if item["disposition"] == "pending" and args.fail_on_pending_high and item["score"] >= args.fail_on_pending_high]
    print(f"Scanned {len(files)} files; emitted {len(candidates)} candidates; pending high: {len(pending_high)}")
    return 2 if pending_high else 0


if __name__ == "__main__":
    raise SystemExit(main())
