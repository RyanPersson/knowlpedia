from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "generate_dependency_metadata.py"
SPEC = importlib.util.spec_from_file_location("generate_dependency_metadata", SCRIPT)
assert SPEC and SPEC.loader
dependency_metadata = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = dependency_metadata
SPEC.loader.exec_module(dependency_metadata)


def write_knowl(
    path: Path,
    knowl_id: str,
    body: str,
    *,
    kind: str = "definition",
    extra_meta: str = "",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "+++\n"
        f'id = "{knowl_id}"\n'
        f'title = "{knowl_id}"\n'
        f'kind = "{kind}"\n'
        'summary = "Summary."\n'
        'domains = ["sample"]\n'
        f"{extra_meta}"
        "+++\n\n"
        f"{body}\n",
        encoding="utf-8",
    )


def metadata(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    end = text.index("\n+++\n", 4)
    return tomllib.loads(text[4:end])


class DependencyMetadataTests(unittest.TestCase):
    def test_inference_uses_only_definition_core_and_ignores_code_math_and_self_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            content = Path(directory) / "content"
            source_path = content / "source.knowl.md"
            write_knowl(content / "a.knowl.md", "sample/a", "A.")
            write_knowl(content / "b.knowl.md", "sample/b", "B.")
            write_knowl(
                source_path,
                "sample/source",
                "A [[sample/a|first concept]] and [[sample/source|self]].\n"
                "`[[sample/b]]` and \\(R[[sample/b]]\\) are protected.\n\n"
                "## Remarks\n"
                "Later [[sample/b|related concept]].",
            )
            knowls = [dependency_metadata.split_source(path) for path in content.rglob("*.knowl.md")]
            source = next(knowl for knowl in knowls if knowl.id == "sample/source")
            self.assertEqual(
                dependency_metadata.infer_dependencies(source, {knowl.id for knowl in knowls}),
                ("sample/a",),
            )

    def test_apply_adds_provenance_and_zero_review_count_without_touching_body(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            content = root / "content"
            write_knowl(content / "base.knowl.md", "sample/base", "Base.")
            target = content / "target.knowl.md"
            body = "A [[sample/base|base]].\n\n## Examples\nExample."
            write_knowl(target, "sample/target", body)
            report = root / "report.jsonl"
            args = argparse.Namespace(
                content_root=content,
                report=report,
                sample_size=None,
                seed=1,
                paths_file=None,
                apply=True,
            )
            stats = dependency_metadata.run(args)
            self.assertEqual(stats["changed"], 2)
            target_meta = metadata(target)
            self.assertEqual(target_meta["prerequisites"], ["sample/base"])
            self.assertEqual(target_meta["dependency_review_count"], 0)
            self.assertEqual(target_meta["dependency_heuristic"], "definition-links-v1")
            self.assertIn(body, target.read_text(encoding="utf-8"))

    def test_reviewed_metadata_is_reported_but_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            content = root / "content"
            write_knowl(content / "base.knowl.md", "sample/base", "Base.")
            target = content / "target.knowl.md"
            write_knowl(
                target,
                "sample/target",
                "A [[sample/base|base]].",
                extra_meta='prerequisites = []\ndependency_review_count = 2\n',
            )
            original = target.read_text(encoding="utf-8")
            report = root / "report.jsonl"
            args = argparse.Namespace(
                content_root=content,
                report=report,
                sample_size=None,
                seed=1,
                paths_file=None,
                apply=True,
            )
            stats = dependency_metadata.run(args)
            row = next(json.loads(line) for line in report.read_text().splitlines() if "sample/target" in line)
            self.assertEqual(row["status"], "reviewed_preserved")
            self.assertEqual(stats["reviewed_preserved"], 1)
            self.assertEqual(target.read_text(encoding="utf-8"), original)

    def test_unreviewed_heuristic_metadata_refreshes_after_core_edit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            content = root / "content"
            write_knowl(content / "foundation.knowl.md", "sample/foundation", "A foundation.")
            target = content / "target.knowl.md"
            write_knowl(
                target,
                "sample/target",
                "A target with no remaining links.",
                extra_meta=(
                    'prerequisites = ["sample/foundation"]\n'
                    'dependency_heuristic = "definition-links-v1"\n'
                    "dependency_review_count = 0\n"
                ),
            )
            report = root / "report.jsonl"
            args = argparse.Namespace(
                content_root=content,
                report=report,
                sample_size=None,
                seed=1,
                paths_file=None,
                apply=True,
            )
            stats = dependency_metadata.run(args)
            self.assertEqual(metadata(target)["prerequisites"], [])
            self.assertEqual(stats["changed"], 2)

    def test_authored_lists_survive_repeated_runs_and_core_edits(self) -> None:
        for prerequisites in ('[]', '["sample/authored"]'):
            for provenance in ('', 'dependency_heuristic = "authored+definition-links-v1"\n'):
                with self.subTest(prerequisites=prerequisites, provenance=provenance), tempfile.TemporaryDirectory() as directory:
                    target = Path(directory) / "target.knowl.md"
                    write_knowl(
                        target,
                        "sample/target",
                        "A [[sample/inferred|candidate]].",
                        extra_meta=f"prerequisites = {prerequisites}\n{provenance}",
                    )
                    known_ids = {"sample/target", "sample/authored", "sample/inferred"}
                    for body_changed in (False, False, True):
                        if body_changed:
                            target.write_text(target.read_text().replace("[[sample/inferred|candidate]]", "concept"))
                        original = target.read_text()
                        proposal = dependency_metadata.propose(dependency_metadata.split_source(target), known_ids)
                        self.assertEqual(proposal.status, "authored_preserved")
                        self.assertEqual(proposal.inferred, () if body_changed else ("sample/inferred",))
                        self.assertFalse(dependency_metadata.apply_proposal(proposal))
                        self.assertEqual(target.read_text(), original)

    def test_sampling_is_deterministic(self) -> None:
        items = [
            dependency_metadata.SourceKnowl(str(index), str(index), "definition", Path(str(index)), {}, "", "", "")
            for index in range(20)
        ]
        first = [item.id for item in dependency_metadata.choose_sample(items, 5, 42)]
        second = [item.id for item in dependency_metadata.choose_sample(items, 5, 42)]
        self.assertEqual(first, second)
        self.assertEqual(len(first), 5)


if __name__ == "__main__":
    unittest.main()
