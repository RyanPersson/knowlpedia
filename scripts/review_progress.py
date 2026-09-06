#!/usr/bin/env python3
"""Report recorded editorial progress against a fixed Git corpus baseline."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import subprocess
import tarfile
import tomllib
from pathlib import Path


def metadata(text: str) -> dict:
    if not text.startswith("+++\n") or (end := text.find("\n+++\n", 4)) < 0:
        raise ValueError("missing or unterminated TOML front matter")
    return tomllib.loads(text[4:end])


def inventory(repo: Path, ref: str | None = None) -> dict[str, dict]:
    if ref:
        archive = subprocess.check_output(["git", "archive", ref, "content"], cwd=repo)
        with tarfile.open(fileobj=io.BytesIO(archive)) as tree:
            sources = [(item.name, tree.extractfile(item).read()) for item in tree
                       if item.isfile() and item.name.endswith(".knowl.md")]
    else:
        sources = [(str(p.relative_to(repo)), p.read_bytes()) for p in (repo / "content").rglob("*.knowl.md")]
    result = {}
    for path, source in sources:
        meta = metadata(source.decode())
        knowl_id = meta["id"]
        if knowl_id in result:
            raise ValueError(f"duplicate source ID: {knowl_id}")
        result[knowl_id] = {**meta, "path": path, "sha256": hashlib.sha256(source).hexdigest()}
    return result


def summarize(ledger: dict, baseline: dict, current: dict) -> dict:
    full_reviews = {}
    corrected = set()
    batch_ids = set()
    for batch in ledger["batches"]:
        if batch["id"] in batch_ids:
            raise ValueError(f"duplicate batch: {batch['id']}")
        batch_ids.add(batch["id"])
        seen = set()
        for entry in batch["entries"]:
            knowl_id = entry["id"]
            if knowl_id in seen or knowl_id not in baseline.keys() | current.keys():
                raise ValueError(f"duplicate or unknown knowl in batch: {knowl_id}")
            seen.add(knowl_id)
            scope, outcome = entry["scope"], entry["outcome"]
            if scope not in {"targeted", "full", "dependencies"}:
                raise ValueError(f"invalid review scope: {scope}")
            if outcome not in {"corrected", "reviewed_unchanged", "redirected", "new"}:
                raise ValueError(f"invalid outcome: {outcome}")
            if scope == "dependencies" and outcome != "reviewed_unchanged":
                raise ValueError("dependency-only edits are not content corrections")
            if outcome == "corrected":
                corrected.add(knowl_id)
            if scope == "full":
                if not entry.get("source_sha256") or not entry.get("evidence"):
                    raise ValueError(f"full review needs source hash and evidence: {knowl_id}")
                full_reviews[knowl_id] = entry
    valid = {knowl_id for knowl_id, entry in full_reviews.items()
             if current.get(knowl_id, {}).get("sha256") == entry["source_sha256"]}
    baseline_ids = set(baseline)
    completed = valid & baseline_ids
    redirects = {knowl_id for knowl_id, meta in current.items() if meta.get("redirect_to")}
    return {
        "baseline_ref": ledger["baseline_content_ref"],
        "baseline_knowls": len(baseline),
        "baseline_corrected": len(corrected & baseline_ids),
        "baseline_fully_reviewed": len(completed),
        "baseline_remaining": len(baseline_ids - completed),
        "baseline_redirected": len(redirects & baseline_ids),
        "stale_full_reviews": len(set(full_reviews) - valid),
        "current_sources": len(current),
        "current_canonical_knowls": len(current) - len(redirects),
        "new_knowls": len(set(current) - baseline_ids),
        "current_prerequisite_lists_reviewed": sum(
            meta.get("dependency_review_count", 0) > 0 for key, meta in current.items() if key not in redirects
        ),
        "remaining_ids": sorted(baseline_ids - completed),
        "fully_reviewed_ids": sorted(completed),
    }


def markdown(stats: dict) -> str:
    labels = {
        "baseline_knowls": "Knowls in the fixed starting corpus",
        "baseline_corrected": "Starting knowls with a recorded content correction",
        "baseline_fully_reviewed": "Starting knowls fully reviewed at their current source revision",
        "baseline_remaining": "Starting knowls still requiring full review",
        "baseline_redirected": "Starting knowls consolidated into compatibility redirects",
        "stale_full_reviews": "Full reviews invalidated by subsequent source changes",
        "current_canonical_knowls": "Current canonical knowls (including collections)",
        "new_knowls": "New knowls added since the baseline",
        "current_prerequisite_lists_reviewed": "Current prerequisite lists with a recorded review",
    }
    rows = "\n".join(f"| {label} | {stats[key]:,} |" for key, label in labels.items())
    return (
        "# Refactor progress\n\n"
        f"Fixed content baseline: `{stats['baseline_ref']}`. Counts come from the review ledger and Git sources.\n\n"
        "| Measure | Count |\n|---|---:|\n" + rows + "\n\n"
        "Corrections, full reviews, prerequisite reviews, and consolidations overlap; do not add them together. "
        "A targeted correction does not complete a full review. Metadata-only changes do not count as corrected content. "
        "New knowls do not reduce the fixed backlog. A full review counts only while its recorded source hash matches; "
        "later edits return it to the pending queue. These are recorded AI editorial reviews, not mathematical certification.\n\n"
        "Regenerate with `python3 scripts/review_progress.py --output docs/refactor-progress.md`. "
        "Use `--json` for the exact pending/reviewed ID lists. The evidence ledger is "
        "`../knowlpedia-content/reviews/refactor-ledger.json`.\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-repo", type=Path, default=Path(__file__).resolve().parents[2] / "knowlpedia-content")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    repo = args.content_repo.resolve()
    ledger = json.loads((repo / "reviews/refactor-ledger.json").read_text())
    stats = summarize(ledger, inventory(repo, ledger["baseline_content_ref"]), inventory(repo))
    text = json.dumps(stats, indent=2) + "\n" if args.json else markdown(stats)
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
