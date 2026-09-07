import sys
from pathlib import Path
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_missing_links import audit
from link_review_progress import summarize


class MissingLinkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'content').mkdir()
        (self.root / 'knowlpack.toml').write_text('id="test"\ncontent_dir="content"\n')

    def knowl(self, key, title, body, extra=''):
        (self.root / 'content' / (key+'.knowl.md')).write_text(
            f'+++\nid="{key}"\ntitle="{title}"\nkind="definition"\nsummary="Test"\n{extra}+++\n{body}\n')

    def test_multiline_core_is_not_suppressed_by_later_link(self):
        self.knowl('target', 'Vector space', 'Definition.')
        self.knowl('source', 'Example', 'A vector\nspace appears.\n## Examples\n[[target|vector space]]')
        report = audit(self.root)
        found = [f for f in report['findings'] if f['source_id']=='source']
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['surface'], 'vector\nspace')
        self.assertEqual(found[0]['section'], 'core')
        text = (self.root/'content/source.knowl.md').read_text()
        self.assertEqual(text.splitlines()[found[0]['line']-1][found[0]['column']-1:], 'vector')

    def test_protected_text_and_paragraph_boundaries(self):
        self.knowl('target', 'Vector space', 'Definition.')
        self.knowl('source', 'Example', '`vector space`\n\\[vector space\\]\n'
                   '~~~python\nvector space\n~~~\n<!-- vector space -->\n'
                   '[vector space](https://example.com)\nvector\n\nspace\n'
                   '## References\nvector space')
        self.assertFalse(audit(self.root)['findings'])

    def test_ambiguity_redirects_and_self_mentions(self):
        self.knowl('one', 'Vector space', '**Vector space**.', 'aliases=["shared term"]\n')
        self.knowl('two', 'Linear space', 'Definition.', 'aliases=["shared term"]\n')
        self.knowl('old', 'Retired space', '', 'redirect_to="one"\n')
        self.knowl('source', 'Example', 'shared term; [[old|vector space]]; vector space.')
        found = audit(self.root)['findings']
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['kind'], 'ambiguous_phrase')
        self.assertEqual(found[0]['targets'], ['one', 'two'])

    def test_unknown_phrases_and_broken_dependencies(self):
        self.knowl('one', 'First', 'Poincaré disk. Mystery bundle.', 'prerequisites=["absent"]\n')
        self.knowl('two', 'Second', 'Mystery bundle. [[absent|missing]]')
        report = audit(self.root, min_sources=2, seeds=['Poincaré disk'])
        groups = {g['phrase']: g for g in report['possible_missing_definitions']}
        self.assertEqual(groups['poincaré disk']['source_count'], 1)
        self.assertEqual(groups['mystery bundle']['source_count'], 2)
        self.assertEqual(report['counts']['broken_link'], 1)
        self.assertEqual(report['counts']['missing_prerequisite_target'], 1)

    def test_unknown_surface_suggests_longer_existing_title(self):
        self.knowl('target', 'Tensor product of modules', 'Definition.')
        self.knowl('source', 'Example', 'A tensor product occurs here.')
        groups = audit(self.root, min_sources=1)['possible_missing_definitions']
        group = next(g for g in groups if g['phrase']=='tensor product')
        self.assertIn('target', group['related_targets'])

    def test_profile_excludes_development_targets(self):
        self.knowl('source', 'Example', 'Exotic bundle.')
        testing = self.root / 'testing'
        testing.mkdir()
        self.knowl('target', 'Exotic bundle', 'Definition.')
        (self.root / 'content/target.knowl.md').rename(testing / 'target.knowl.md')
        (self.root / 'knowlpack.toml').write_text('id="test"\ncontent_dir="content"\ndevelopment_content_dirs=["testing"]\n')
        self.assertEqual(audit(self.root)['counts']['unlinked_phrase'], 0)
        self.assertEqual(audit(self.root, profile='development')['counts']['unlinked_phrase'], 1)

    def test_stale_reviews_do_not_count_as_completed(self):
        self.knowl('one', 'First', 'Definition.')
        report = audit(self.root)
        entry = dict(id='one', outcome='corrected', evidence='Checked definitions and conventions.', source_sha256=report['inventory'][0]['source_sha256'])
        self.assertEqual(summarize(report, {'reviews':[entry]})['reviewed_current'], 1)
        self.knowl('one', 'First', 'Changed definition.')
        stats = summarize(audit(self.root), {'reviews':[entry]})
        self.assertEqual(stats['reviewed_current'], 0)
        self.assertEqual(stats['stale_reviews'], 1)
        self.assertEqual(stats['remaining_review'], 1)


if __name__ == '__main__':
    unittest.main()
