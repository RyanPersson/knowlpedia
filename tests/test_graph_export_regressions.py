import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "packages/compiler/knowl_compile.py"
SPEC = importlib.util.spec_from_file_location("knowl_compile_export", MODULE)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


def knowl(identifier, prerequisites=()):
    return compiler.knowl_from_meta(
        {"id": identifier, "title": identifier, "kind": "definition", "summary": "Summary.",
         "aliases": [], "domains": [], "prerequisites": list(prerequisites)},
        Path(identifier.replace("/", "-") + ".knowl.md"), "Body.", sections=[]
    )


class GraphExportRegressionTests(unittest.TestCase):
    def test_unreviewed_cycle_is_error_and_self_loop_export_is_rejected(self):
        item = knowl("sample/self", ["sample/self"])
        messages = compiler.validate({item.id: item})
        self.assertEqual([message.severity for message in messages if "cycle" in message.message], ["error"])
        with self.assertRaisesRegex(ValueError, "cyclic prerequisite"):
            compiler.dependency_graph_json({item.id: item})

    def test_export_deduplicates_edges_and_is_deterministic(self):
        base = knowl("sample/base")
        child = knowl("sample/child", ["sample/base", "sample/base#anchor", "sample/base"])
        first = compiler.dependency_graph_json({child.id: child, base.id: base})
        second = compiler.dependency_graph_json({base.id: base, child.id: child})
        self.assertEqual(first, second)
        self.assertEqual(len(first["edges"]), 1)

    def test_allow_validation_errors_does_not_export_cyclic_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "knowlpack.toml").write_text('id="sample"\ntitle="Sample"\ncontent_dir="content"\n')
            for identifier, prerequisite in (("a", "b"), ("b", "a")):
                (root / "content").mkdir(exist_ok=True)
                (root / "content" / f"{identifier}.knowl.md").write_text(
                    f'+++\nid="sample/{identifier}"\ntitle="{identifier}"\nkind="definition"\n'
                    f'summary="Summary"\nprerequisites=["sample/{prerequisite}"]\n+++\nBody.\n'
                )
            output = root / "public"
            self.assertEqual(compiler.write_site(root, output, allow_validation_errors=True), 1)
            self.assertFalse((output / "indexes/dependencies.json").exists())


if __name__ == "__main__":
    unittest.main()
