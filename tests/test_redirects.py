from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "packages" / "compiler" / "knowl_compile.py"
SPEC = importlib.util.spec_from_file_location("knowl_compile_redirects", MODULE_PATH)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


def write_doc(path: Path, front: str, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"+++\n{front}\n+++\n{body}\n", encoding="utf-8")


class RedirectTests(unittest.TestCase):
    def package(self, root: Path) -> None:
        (root / "knowlpack.toml").write_text('id = "test"\ntitle = "Test"\n', encoding="utf-8")

    def test_redirect_preserves_page_core_and_section_paths_and_deduplicates_indexes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, out = Path(tmp), Path(tmp) / "public"
            self.package(root)
            write_doc(root / "content" / "new.knowl.md", 'id="new"\ntitle="New"\nkind="definition"\nsummary="Canonical"', "New body.\n\n## Example\nA worked example.")
            write_doc(root / "content" / "old.knowl.md", 'id="old"\ntitle="Old"\nkind="definition"\nsummary="Moved"\nredirect_to="new"\nredirect_sections={old-example="example"}')
            self.assertEqual(0, compiler.write_site(root, out, allow_validation_errors=False))
            self.assertTrue((out / "old" / "index.html").is_file())
            self.assertIn('/new/', (out / "old" / "index.html").read_text())
            self.assertIn("New body", (out / "fragments" / "old" / "core.html").read_text())
            self.assertIn("worked example", (out / "fragments" / "old" / "sections" / "old-example.html").read_text())
            search = json.loads((out / "indexes" / "search.json").read_text())
            self.assertEqual(["new"], [item["id"] for item in search])
            self.assertIn("old", json.loads((out / "indexes" / "registry.json").read_text())["new"]["aliases"])
            links = json.loads((out / "indexes" / "links.json").read_text())
            self.assertTrue(all(link["target"] != "old" for link in links))
            selected = Path(tmp) / "selected"
            self.assertEqual(0, compiler.write_site(root, selected, only_ids={"old"}))
            self.assertTrue((selected / "old" / "index.html").is_file())
            self.assertTrue((selected / "new" / "index.html").is_file())

    def test_chains_resolve_and_missing_or_cycles_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.package(root)
            write_doc(root / "content" / "canonical.knowl.md", 'id="canonical"\ntitle="Canonical"\nkind="definition"\nsummary="x"', "x")
            write_doc(root / "content" / "middle.knowl.md", 'id="middle"\ntitle="Middle"\nkind="definition"\nsummary="x"\nredirect_to="canonical"')
            write_doc(root / "content" / "old.knowl.md", 'id="old"\ntitle="Old"\nkind="definition"\nsummary="x"\nredirect_to="middle"\n')
            knowls, _ = compiler.discover_package_knowls(root, compiler.read_toml(root / "knowlpack.toml"), compiler.BUILD_PROFILES["development"])
            registry = compiler.AliasRegistry({k.id: k for k in knowls if not k.redirect_to}, {"middle": "canonical", "old": "canonical"})
            self.assertEqual("canonical", registry.canonical_id("old"))
            write_doc(root / "content" / "missing.knowl.md", 'id="missing"\ntitle="Missing"\nkind="definition"\nsummary="x"\nredirect_to="gone"')
            self.assertNotEqual(0, compiler.write_site(root, root / "out", allow_validation_errors=False))

    def test_cycle_is_rejected_during_real_build(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.package(root)
            write_doc(root / "content" / "a.knowl.md", 'id="a"\ntitle="A"\nkind="definition"\nsummary="x"\nredirect_to="b"')
            write_doc(root / "content" / "b.knowl.md", 'id="b"\ntitle="B"\nkind="definition"\nsummary="x"\nredirect_to="a"')
            self.assertNotEqual(0, compiler.write_site(root, root / "out", allow_validation_errors=False))

    def test_chained_sections_and_dependency_exports_use_canonical_ids(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, out = Path(tmp), Path(tmp) / "out"
            self.package(root)
            write_doc(root / "content/new.knowl.md", 'id="new"\ntitle="New"\nkind="definition"\nsummary="x"', "Definition.\n\n## Final\nFinal example.")
            write_doc(root / "content/middle.knowl.md", 'id="middle"\ntitle="Middle"\nkind="definition"\nsummary="x"\nredirect_to="new"\nredirect_sections={intermediate="final"}')
            write_doc(root / "content/old.knowl.md", 'id="old"\ntitle="Historical wording"\nkind="definition"\nsummary="x"\naliases=["Historical synonym"]\nredirect_to="middle"\nredirect_sections={original="intermediate"}')
            write_doc(root / "content/reader.knowl.md", 'id="reader"\ntitle="Reader"\nkind="definition"\nsummary="x"\nprerequisites=["old"]', "See [[old#section.original|historical example]].")
            self.assertEqual(0, compiler.write_site(root, out))
            self.assertIn('/new/#section.final', (out / "reader/index.html").read_text())
            self.assertIn("Final example", (out / "fragments/old/sections/original.html").read_text())
            index = json.loads((out / "indexes/registry.json").read_text())
            self.assertEqual(["new"], index["reader"]["prerequisites"])
            self.assertIn("Historical synonym", index["new"]["aliases"])
            self.assertIn('"original":"final"', (out / "old/index.html").read_text())
