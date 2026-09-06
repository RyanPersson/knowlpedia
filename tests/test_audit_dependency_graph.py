import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts/audit_dependency_graph.py"
SPEC = importlib.util.spec_from_file_location("audit_dependency_graph", SCRIPT)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


def source(identifier, prerequisites=()):
    return ("+++\n" f'id="{identifier}"\n' f'title="{identifier}"\n'
            'kind="definition"\nsummary="Summary"\n'
            f'prerequisites={json.dumps(list(prerequisites))}\n+++\nBody.\n')


class DependencyAuditTests(unittest.TestCase):
    def test_missing_target_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            (package / "knowlpack.toml").write_text('id="x"\ntitle="X"\ncontent_dir="content"\n')
            (package / "content").mkdir()
            (package / "content/a.knowl.md").write_text(source("sample/a", ["sample/missing"]))
            report = audit.audit(package, "production")
            self.assertEqual(report["counts"]["missing_targets"], 1)
            self.assertIsNone(report["topological_order"])

    def test_duplicate_ids_are_not_silently_dropped(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            (package / "knowlpack.toml").write_text('id="x"\ntitle="X"\ncontent_dir="content"\n')
            (package / "content").mkdir()
            (package / "content/a.knowl.md").write_text(source("sample/same"))
            (package / "content/b.knowl.md").write_text(source("sample/same"))
            with self.assertRaisesRegex(ValueError, "Duplicate knowl ids"):
                audit.audit(package, "production")


if __name__ == "__main__":
    unittest.main()
