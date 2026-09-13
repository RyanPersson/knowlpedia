from __future__ import annotations

import hashlib
import json
import unittest

import test_private_library as library_tests
from test_compiler import compiler, write_knowl
from test_check_rendering_errors import checker


class PrivateMarkdownTests(unittest.TestCase):
    setUp = library_tests.PrivateLibraryTests.setUp

    def make_document(self):
        figure = self.private / 'build/figure.svg'
        figure.parent.mkdir()
        figure.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="40" height="30"><circle cx="20" cy="15" r="10"/></svg>')
        self.manifest = {'version': 1, 'pages': 2, 'source_url': 'https://example.org/source.pdf',
            'figures': {'figures/figure-1.svg': {'path': 'build/figure.svg', 'sha256': hashlib.sha256(figure.read_bytes()).hexdigest()}},
            'notes': {'symbol': {'title': 'Local symbol', 'page': 2, 'body': 'A [[sample/set|set]] with $x^2$.'}}}
        self.manifest_path = self.private / 'metadata/reading.json'
        self.manifest_path.parent.mkdir()
        self.save_manifest()
        self.document.write_text(
            '+++\nid="documents/reading"\ntitle="PRIVATE_TITLE_SENTINEL"\nkind="document"\n'
            'summary="Private Markdown fixture"\nsection_mode="continuous"\n'
            'reading_manifest="metadata/reading.json"\n+++\n\n'
            '<!-- anchor: page-1 -->\n\n## First part\n\n'
            'PRIVATE_BODY_SENTINEL. A [[sample/group|group]] and $x^2$.\n\n'
            '$$\n\\frac{a}{b}=c\n$$\n\n![Original diagram](figures/figure-1.svg)\n\n'
            '<!-- anchor: page-2 -->\n\n## Second part\n\n'
            'The [[documents/reading#note-symbol|local symbol]] has a definition.\n'
        )
        return figure

    def save_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest))

    def test_flowing_markdown_mathjax_notes_and_original_figures(self):
        figure = self.make_document()
        original = self.document.read_bytes()
        self.assertEqual(compiler.write_site(self.public, self.output, private_package=self.private), 0)
        page = (self.output / 'documents/reading/index.html').read_text()
        self.assertIn('class="knowl-page document-markdown"', page)
        self.assertIn('<h2>First part</h2>', page)
        self.assertIn('<h2>Second part</h2>', page)
        self.assertIn('data-document-math="true">\\(x^2\\)', page)
        self.assertIn('\\[\\frac{a}{b}=c\\]', page)
        self.assertIn('/assets/mathjax/tex-chtml.js', page)
        self.assertIn('data-knowl="/documents/reading/notes/symbol.html"', page)
        self.assertNotIn('document-concept-drawer', page)
        self.assertNotIn('document-term', page)
        self.assertNotIn('document-transcript', page)
        self.assertIn('id="page-2"', page)
        self.assertEqual((self.output / 'documents/reading/figures/figure-1.svg').read_bytes(), figure.read_bytes())
        note = (self.output / 'documents/reading/notes/symbol.html').read_text()
        self.assertIn('data-knowl="/fragments/sample/set/core.html"', note)
        self.assertIn('/documents/reading/#page-2', note)
        self.assertEqual(self.document.read_bytes(), original)
        self.assertFalse(any(self.output.rglob('*.pdf')))
        group = (self.output / 'fragments/sample/group/core.html').read_text()
        self.assertNotIn('data-document-math', group)

    def test_production_removes_private_markdown_and_mathjax_assets(self):
        self.make_document()
        compiler.write_site(self.public, self.output, private_package=self.private)
        self.assertTrue((self.output / 'assets/mathjax/tex-chtml.js').is_file())
        compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES['production'])
        for relative in ('documents', 'library', 'assets/mathjax', 'assets/document-math.js'):
            self.assertFalse((self.output / relative).exists(), relative)
        self.assertEqual(checker.check_build_profile(self.output, 'production'), [])

    def test_bad_figure_hash_and_escaping_path_fail_before_output(self):
        self.make_document()
        self.manifest['figures']['figures/figure-1.svg']['sha256'] = 'bad'
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'figure hash mismatch'):
            compiler.write_site(self.public, self.output, private_package=self.private)
        self.assertFalse(self.output.exists())
        self.manifest['figures']['figures/figure-1.svg']['path'] = '../outside.svg'
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'escapes the private package'):
            compiler.write_site(self.public, self.output, private_package=self.private)

    def test_source_anchor_duplicates_and_missing_note_targets_are_detected(self):
        self.make_document()
        self.document.write_text(self.document.read_text() + '\n<!-- anchor: page-1 -->\n')
        with self.assertRaisesRegex(ValueError, 'Duplicate private Markdown anchor'):
            compiler.write_site(self.public, self.output, private_package=self.private)
        self.document.write_text(self.document.read_text().rsplit('\n<!-- anchor: page-1 -->', 1)[0])
        self.manifest['notes']['symbol']['body'] = '[[sample/missing|Missing definition]]'
        self.save_manifest()
        self.assertNotEqual(compiler.write_site(self.public, self.output, private_package=self.private), 0)

    def test_public_corpus_cannot_supply_a_reading_manifest(self):
        self.make_document()
        path = self.public / 'content/copied.knowl.md'
        write_knowl(path, 'sample/copied', 'Copied')
        path.write_text(path.read_text().replace('+++\n', '+++\nreading_manifest="metadata/reading.json"\n', 1))
        with self.assertRaisesRegex(ValueError, 'Reading manifests are restricted'):
            compiler.write_site(self.public, self.output)

    def test_source_hash_guide_and_same_document_navigation(self):
        self.make_document()
        self.document.write_text(self.document.read_text()+'\n[Second part](#page-2)\n')
        body=self.document.read_text().split('\n+++\n',1)[1]
        plain=compiler.private_markdown.LINK_RE.sub(lambda m:m[2],body).strip()
        self.manifest['markdown_body_sha256']=hashlib.sha256(plain.encode()).hexdigest()
        self.manifest['guide_note']='symbol'
        self.save_manifest()
        self.assertEqual(compiler.write_site(self.public,self.output,private_package=self.private),0)
        page=(self.output/'documents/reading/index.html').read_text()
        self.assertIn('href="#page-2">Second part</a>',page)
        self.assertIn('data-reading-manifest-sha256=',page)
        self.document.write_text(self.document.read_text().replace('PRIVATE_BODY_SENTINEL','Changed source wording'))
        with self.assertRaisesRegex(ValueError,'source fidelity check failed'):
            compiler.write_site(self.public,self.output,private_package=self.private)


if __name__ == '__main__':
    unittest.main()
