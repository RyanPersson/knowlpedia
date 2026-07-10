#!/usr/bin/env python3
"""Merge candidate-link adjudication and optionally apply accepted insertions."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def absolute_offset(text: str, line: int, column: int) -> int:
    lines = text.splitlines(keepends=True)
    if line < 1 or line > len(lines):
        raise ValueError(f"line {line} is outside file")
    return sum(len(value) for value in lines[: line - 1]) + column - 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", type=Path, required=True)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--adjudication", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    content_root = args.content_root.resolve()
    candidates = {item["candidate_id"]: item for item in load_jsonl(args.candidates)}
    review = json.loads(args.adjudication.read_text(encoding="utf-8"))
    reviewed_at = review.get("reviewed_at") or datetime.now(timezone.utc).isoformat()
    decided_by = review.get("decided_by", "unspecified")
    ledger: list[dict] = []
    accepted_by_path: dict[Path, list[dict]] = defaultdict(list)

    for candidate_id, decision in review["decisions"].items():
        if candidate_id not in candidates:
            raise ValueError(f"decision references absent candidate: {candidate_id}")
        item = dict(candidates[candidate_id])
        item.update(
            {
                "disposition": decision["disposition"],
                "reason_code": decision["reason_code"],
                "note": decision.get("note"),
                "decided_by": decided_by,
                "decided_at": reviewed_at,
            }
        )
        ledger.append(item)
        if item["disposition"] == "accept":
            if len(item["target_ids"]) != 1:
                raise ValueError(f"accepted candidate is ambiguous: {candidate_id}")
            accepted_by_path[content_root / item["source_path"]].append(item)

    ledger.sort(key=lambda item: (item["source_path"], item["line"], item["candidate_id"]))
    args.ledger.parent.mkdir(parents=True, exist_ok=True)
    args.ledger.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in ledger), encoding="utf-8")

    inserted = 0
    for path, items in sorted(accepted_by_path.items()):
        text = path.read_text(encoding="utf-8")
        source_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        expected_hashes = {item["source_sha256"] for item in items}
        if expected_hashes != {source_hash}:
            raise ValueError(f"stale candidates for {path}: expected {sorted(expected_hashes)}, found {source_hash}")
        replacements: list[tuple[int, int, str]] = []
        for item in items:
            start = absolute_offset(text, int(item["line"]), int(item["column"]))
            surface = str(item["surface"])
            if text[start : start + len(surface)] != surface:
                found = text[start : start + len(surface)]
                raise ValueError(f"span mismatch for {item['candidate_id']}: expected {surface!r}, found {found!r}")
            target = item["target_ids"][0]
            replacements.append((start, start + len(surface), f"[[{target}|{surface}]]"))
        for start, end, replacement in sorted(replacements, reverse=True):
            text = text[:start] + replacement + text[end:]
            inserted += 1
        if args.apply:
            path.write_text(text, encoding="utf-8")

    mode = "applied" if args.apply else "validated"
    print(f"{mode} {inserted} accepted links across {len(accepted_by_path)} files; ledger: {args.ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
