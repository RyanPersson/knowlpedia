#!/usr/bin/env python3
"""Report-only audit of a Knowlpedia prerequisite graph."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

COMPILER_DIR = Path(__file__).resolve().parents[1] / "packages" / "compiler"
sys.path.insert(0, str(COMPILER_DIR))
import knowl_compile as compiler  # noqa: E402
from graph_algorithms import cycle_witnesses, topological_order  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-package", type=Path,
        default=Path(__file__).resolve().parents[1].parent / "knowlpedia-content",
        help="Content package directory (default: sibling knowlpedia-content)",
    )
    parser.add_argument("--profile", choices=compiler.PROFILE_NAMES, default="development")
    parser.add_argument("--report", type=Path, help="Write JSON report here instead of stdout")
    return parser.parse_args()


def audit(package_dir: Path, profile_name: str) -> dict[str, object]:
    package_dir = package_dir.resolve()
    package = compiler.read_toml(package_dir / "knowlpack.toml")
    knowls, _ = compiler.discover_package_knowls(
        package_dir, package, compiler.BUILD_PROFILES[profile_name]
    )
    registry, messages = compiler.build_registry(knowls)
    prerequisites = {
        knowl_id: [compiler.split_target(compiler.canonical_target(registry, target))[0] for target in knowl.prerequisites
                   if compiler.split_target(compiler.canonical_target(registry, target))[0] in registry]
        for knowl_id, knowl in registry.items()
    }
    missing = sorted({
        target for knowl in registry.values() for target in knowl.prerequisites
        if compiler.split_target(compiler.canonical_target(registry, target))[0] not in registry
    })
    invalid = sorted({
        message.source for message in messages
        if message.severity == "error" and "prerequisite cycle" not in message.message
    })
    cycles = [list(cycle) for cycle in cycle_witnesses(prerequisites)]
    order = topological_order(prerequisites)
    return {
        "version": 1,
        "profile": profile_name,
        "counts": {
            "nodes": len(registry),
            "edges": sum(len(set(values)) for values in prerequisites.values()),
            "missing_targets": len(missing),
            "invalid": len(invalid),
            "cycles": len(cycles),
        },
        "topological_order": list(order) if order is not None and not missing else None,
        "missing_targets": missing,
        "invalid_sources": invalid,
        "cycle_witnesses": cycles,
    }


def main() -> int:
    args = parse_args()
    try:
        report = audit(args.content_package, args.profile)
        rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
    except (OSError, ValueError, KeyError, compiler.tomllib.TOMLDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    counts = report["counts"]
    return 1 if counts["cycles"] or counts["missing_targets"] or counts["invalid"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
