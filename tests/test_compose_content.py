from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "compose_content.py"
SPEC = importlib.util.spec_from_file_location("compose_content", MODULE_PATH)
assert SPEC and SPEC.loader
composer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(composer)


def write_package(root: Path, content_dir: str = "content") -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "knowlpack.toml").write_text(
        'id = "test"\n'
        'title = "Test"\n'
        f'content_dir = "{content_dir}"\n',
        encoding="utf-8",
    )


class ComposeContentTests(unittest.TestCase):
    def test_composes_primary_and_contributor_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            primary = root / "primary"
            contributor = root / "contributor"
            output = root / "output"
            write_package(primary)
            (primary / "content").mkdir()
            (primary / "content" / "definition.knowl.md").write_text("definition", encoding="utf-8")
            (contributor / "content" / "problems").mkdir(parents=True)
            (contributor / "content" / "problems" / "open.knowl.md").write_text(
                "problem", encoding="utf-8"
            )

            manifest = composer.compose(primary, [contributor], output)

            self.assertEqual(manifest["total_content_files"], 2)
            self.assertEqual((output / "content" / "definition.knowl.md").read_text(), "definition")
            self.assertEqual(
                (output / "content" / "problems" / "open.knowl.md").read_text(), "problem"
            )
            recorded = json.loads((output / composer.MANIFEST_NAME).read_text())
            self.assertEqual(len(recorded["sources"]), 2)

    def test_rejects_relative_path_collisions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            primary = root / "primary"
            contributor = root / "contributor"
            output = root / "output"
            write_package(primary)
            for package in (primary, contributor):
                (package / "content").mkdir(parents=True)
                (package / "content" / "same.knowl.md").write_text("same", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "content path collision"):
                composer.compose(primary, [contributor], output)
            self.assertFalse(output.exists())

    def test_uses_contributor_package_content_dir(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            primary = root / "primary"
            contributor = root / "contributor"
            output = root / "output"
            write_package(primary)
            write_package(contributor, "knowls")
            (primary / "content").mkdir()
            (contributor / "knowls").mkdir()
            (contributor / "knowls" / "extra.knowl.md").write_text("extra", encoding="utf-8")

            composer.compose(primary, [contributor], output)

            self.assertTrue((output / "content" / "extra.knowl.md").is_file())

    def test_exact_source_guard_rejects_local_contributor_in_production(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            primary = root / "primary"
            contributor = root / "conjectures-catalog"
            manifest = {
                "sources": [
                    {"source": str(primary)},
                    {"source": str(contributor)},
                ]
            }
            with self.assertRaisesRegex(ValueError, "unexpected.*conjectures-catalog"):
                composer.verify_source_set(manifest, [primary])


if __name__ == "__main__":
    unittest.main()
