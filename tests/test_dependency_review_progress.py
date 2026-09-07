import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('dependency_review_progress', Path(__file__).parents[1] / 'scripts/dependency_review_progress.py')
progress = importlib.util.module_from_spec(spec)
spec.loader.exec_module(progress)


class ReviewProgressTests(unittest.TestCase):
    def test_current_versions_duplicates_and_redirects(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'current.md'
            source.write_text('current definition')
            digest = hashlib.sha256(source.read_bytes()).hexdigest()
            def record(kid, outcome='reviewed_unchanged', sha=digest):
                return dict(id=kid, outcome=outcome, source_sha256=sha, evidence='Specific review')
            (root / 'a.json').write_text(json.dumps({'reviews': [record('a', 'corrected'), record('old'), record('b', sha='old')]}))
            (root / 'z.json').write_text(json.dumps({'reviews': [record('a'), record('a', sha='old')]}))
            knowl = SimpleNamespace(source_path=source)
            registry = progress.compiler.AliasRegistry({'a': knowl, 'b': knowl, 'unreviewed': knowl}, {'old': 'a'})
            with patch.object(progress.compiler, 'read_toml', return_value={}), patch.object(progress.compiler, 'discover_package_knowls', return_value=([], [])), patch.object(progress.compiler, 'build_registry', return_value=(registry, [])):
                result = progress.summarize(root, root)
            self.assertEqual(result['counts'], dict(canonical_entries=3, corrected=1, reviewed_unchanged=0, blocked=0, stale=1, retired=1, reviewed_current=1, remaining_review=2))
            self.assertEqual(result['stale_ids'], ['b'])


if __name__ == '__main__':
    unittest.main()
