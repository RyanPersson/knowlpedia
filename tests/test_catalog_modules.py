"""Regression tests against the authored M_2(R) regular-module example.

Run with the companion content checkout (or KNOWLPEDIA_CONTENT_PACKAGE).
Matrix-unit checks determine bilinear identities over R; no floats are used.
"""
import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'packages/compiler'))
import catalog
import knowl_compile as compiler


def mul(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) for i in range(2) for j in range(2))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


class RegularModuleTests(unittest.TestCase):
    def test_matrix_units_detect_sidedness_and_composition(self):
        basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
        identity = (1, 0, 0, 1)
        for a in basis:
            for b in basis:
                for x in basis:
                    # R_a is left-linear; L_a is right-linear.
                    self.assertEqual(mul(mul(b, x), a), mul(b, mul(x, a)))
                    self.assertEqual(mul(a, mul(x, b)), mul(mul(a, x), b))
                    # End multiplication is composition, first b, then a.
                    self.assertEqual(mul(mul(x, b), a), mul(x, mul(b, a)))
                    self.assertEqual(mul(a, mul(b, x)), mul(mul(a, b), x))
                    self.assertEqual(mul(x, add(a, b)), add(mul(x, a), mul(x, b)))
                    self.assertEqual(mul(add(a, b), x), add(mul(a, x), mul(b, x)))
            self.assertEqual(mul(identity, a), a)
            self.assertEqual(mul(a, identity), a)
        a, b = basis[1], basis[2]
        self.assertEqual(mul(a, b), basis[0])
        self.assertEqual(mul(b, a), basis[3])
        self.assertNotEqual(mul(mul(identity, b), a), mul(mul(identity, a), b))
        self.assertNotEqual(mul(a, mul(b, identity)), mul(b, mul(a, identity)))
        # A noncentral unit and its inverse give module automorphisms.
        u, inverse = (1, 1, 0, 1), (1, -1, 0, 1)
        self.assertEqual(mul(u, inverse), identity)
        self.assertEqual(mul(inverse, u), identity)

    def test_authored_views_exports_and_sparse_queries(self):
        root = Path(os.environ.get('KNOWLPEDIA_CONTENT_PACKAGE', Path(__file__).resolve().parents[2] / 'knowlpedia-content'))
        if not root.exists():
            self.skipTest('Companion content checkout required; set KNOWLPEDIA_CONTENT_PACKAGE')
        package = compiler.read_toml(root / 'knowlpack.toml')
        knowls, roots = compiler.discover_package_knowls(root, package, compiler.BUILD_PROFILES['production'])
        registry, _ = compiler.build_registry(knowls)
        data = catalog.discover_catalog((p for p, visibility in roots if visibility == 'production'), registry)
        left = 'assoc-m-2-r@left-modules-m-2-r'
        right = 'assoc-m-2-r@right-modules-m-2-r'
        with tempfile.TemporaryDirectory() as tmp:
            catalog.export_catalog(data, Path(tmp))
            exported = json.loads((Path(tmp) / 'catalog.json').read_text())
            views = {v['id']: v for v in exported['views']}
            self.assertEqual(views[left]['notation'], r'{}_A A')
            self.assertEqual(views[right]['notation'], r'A_A')
            with catalog.CatalogQuery(Path(tmp) / 'catalog.sqlite') as query:
                for side, view, result, formula in [('left', left, 'assoc-m-2-r-op', r'R_a\circ R_b=R_{ba}'), ('right', right, 'assoc-m-2-r', r'L_a\circ L_b=L_{ab}')]:
                    self.assertEqual(query.get('views', view), views[view])
                    for operation in ['hom', 'end', 'aut']:
                        records = query.morphisms(view, view, operation)['records']
                        self.assertEqual(len(records), 1)
                        self.assertEqual(records[0]['id'], f'{operation}-m-2-r-{side}-regular')
                        self.assertEqual(records[0]['coverage'], 'complete')
                        self.assertIn(formula, records[0]['description'])
                        if operation != 'aut':
                            self.assertEqual(records[0]['result_object_ids'], [result])
                for source, target in [(left, right), (right, left)]:
                    with self.assertRaisesRegex(ValueError, 'same category'):
                        query.morphisms(source, target)
                unknown = query.morphisms('assoc-m-2-r@real-vector-spaces', 'assoc-m-2-r-op@real-vector-spaces')
                self.assertEqual(unknown['status'], 'not-catalogued')
                self.assertEqual(unknown['records'], [])
        # Same carrier does not allow cross-sided Hom records at validation time.
        raw = {'schema_version': 1, **{key: copy.deepcopy(data[key]) for key in catalog.COLLECTIONS}}
        record = next(r for r in raw['morphism_spaces'] if r['id'] == 'hom-m-2-r-left-regular')
        record['target_view'] = right
        with tempfile.TemporaryDirectory() as tmp:
            shard = Path(tmp) / 'bad.json'
            shard.write_text(json.dumps(raw))
            with self.assertRaisesRegex(catalog.CatalogValidationError, 'same category'):
                catalog.load_catalog([shard], registry)


if __name__ == '__main__':
    unittest.main()
