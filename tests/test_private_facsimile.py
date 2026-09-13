from __future__ import annotations

import hashlib
import json
import unittest

import test_private_library as library_tests
from test_compiler import compiler
from test_check_rendering_errors import checker


class PrivateFacsimileTests(unittest.TestCase):
    """Exercise the new presentation using original, synthetic test content."""

    setUp = library_tests.PrivateLibraryTests.setUp

    def make_facsimile(self):
        image = self.private / "build/page.svg"
        image.parent.mkdir()
        image.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="300"><rect x="10" y="10" width="100" height="100" fill="white"/></svg>')
        first = 'The [[sample/group|group]] has a set.\nOriginal <notation> stays literal.'
        second = 'A [[documents/reading#note-local-symbol|local symbol]] and unchanged final words.'
        self.document.write_text(
            '+++\nid="documents/reading"\ntitle="PRIVATE_TITLE_SENTINEL"\nkind="document"\n'
            'summary="Private facsimile fixture"\nsection_mode="continuous"\n'
            'facsimile_manifest="metadata/pages.json"\n+++\n\n' + first + '\f' + second + '\n'
        )
        plain = [compiler.private_facsimile.LINK_RE.sub(lambda m: m[2], text) for text in (first, second)]
        self.manifest = {
            'version': 1,
            'pages': [
                {'page': n, 'width': 200, 'height': 300, 'image': 'build/page.svg',
                 'image_sha256': hashlib.sha256(image.read_bytes()).hexdigest(),
                 'text_sha256': hashlib.sha256(text.encode()).hexdigest(),
                 'links': [{'target': 'sample/group', 'label': 'group', 'rects': [[20, 30, 70, 45]]}],
                 'concepts': [{'target': 'sample/set', 'label': 'Set'}]}
                for n, text in enumerate(plain, 1)
            ],
            'bookmarks': [{'page': 2, 'label': 'Second part'}],
            'notes': {'local-symbol': {'title': 'Local symbol', 'body': 'A [[sample/set|set]] used in this source.', 'page': 2}},
        }
        self.manifest_path = self.private / 'metadata/pages.json'
        self.manifest_path.parent.mkdir()
        self.save_manifest()
        return image

    def save_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest))

    def test_page_images_transcript_overlays_and_local_notes_form_a_complete_reader(self):
        image = self.make_facsimile()
        original = self.document.read_bytes()
        self.assertEqual(compiler.write_site(self.public, self.output, private_package=self.private), 0)
        page = (self.output / 'documents/reading/index.html').read_text()
        self.assertIn('data-page-count="2"', page)
        self.assertIn('class="knowl document-term document-term-overlay"', page)
        self.assertIn('left:10.000000%;top:10.000000%;width:25.000000%;height:5.000000%;', page)
        self.assertIn('Original &lt;notation&gt; stays literal.', page)
        second = (self.output / 'documents/reading/pages/002/index.html').read_text()
        self.assertIn('data-knowl="/documents/reading/notes/local-symbol.html"', second)
        self.assertIn('unchanged final words.', second)
        note = (self.output / 'documents/reading/notes/local-symbol.html').read_text()
        self.assertIn('data-knowl="/fragments/sample/set/core.html"', note)
        for number in (1, 2):
            self.assertEqual((self.output / f'documents/reading/assets/page-{number:03d}.svg').read_bytes(), image.read_bytes())
            self.assertTrue((self.output / f'documents/reading/pages/{number:03d}/body.html').is_file())
        self.assertEqual(self.document.read_bytes(), original)
        for path in (self.output / 'documents/reading').rglob('*.html'):
            self.assertEqual(checker.scan_file(path, self.output), [], str(path))

    def test_tampered_transcript_is_rejected_before_touching_existing_output(self):
        self.make_facsimile()
        self.document.write_text(self.document.read_text().replace('unchanged final words', 'changed words'))
        self.output.mkdir()
        sentinel = self.output / 'keep.txt'
        sentinel.write_text('Existing output')
        with self.assertRaisesRegex(ValueError, 'transcript fidelity failed on page 2'):
            compiler.write_site(self.public, self.output, private_package=self.private)
        self.assertEqual(sentinel.read_text(), 'Existing output')

    def test_tampered_image_and_escaping_image_path_are_rejected(self):
        image = self.make_facsimile()
        image.write_text(image.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'image hash failed'):
            compiler.write_site(self.public, self.output, private_package=self.private)
        self.manifest['pages'][0]['image'] = '../outside.svg'
        (self.root / 'outside.svg').write_text('<svg/>')
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'escapes the private package'):
            compiler.write_site(self.public, self.output, private_package=self.private)
        self.assertFalse(self.output.exists())

    def test_active_or_external_svg_content_is_not_served(self):
        image = self.make_facsimile()
        for content in (
            '<script>alert(1)</script>',
            '<image href="https://example.com/pixel.png"/>',
            '<rect style="fill:url(https://example.com/color)"/>',
            '<style>@import "https://example.com/style.css";</style>',
        ):
            with self.subTest(content=content):
                image.write_text('<svg xmlns="http://www.w3.org/2000/svg">' + content + '</svg>')
                for page in self.manifest['pages']:
                    page['image_sha256'] = hashlib.sha256(image.read_bytes()).hexdigest()
                self.save_manifest()
                with self.assertRaises(ValueError):
                    compiler.write_site(self.public, self.output, private_package=self.private)
                self.assertFalse(self.output.exists())

    def test_production_rebuild_removes_facsimile_assets_and_reader_runtime(self):
        self.make_facsimile()
        compiler.write_site(self.public, self.output, private_package=self.private)
        self.assertTrue((self.output / 'assets/facsimile.js').exists())
        compiler.write_site(self.public, self.output, profile=compiler.BUILD_PROFILES['production'])
        self.assertFalse((self.output / 'documents').exists())
        self.assertFalse((self.output / 'assets/facsimile.js').exists())
        self.assertEqual(checker.check_build_profile(self.output, 'production'), [])

    def test_public_content_cannot_use_a_facsimile_manifest(self):
        public_file = self.public / 'content/group.knowl.md'
        public_file.write_text(public_file.read_text().replace('\n+++\n', '\nfacsimile_manifest="private.json"\n+++\n', 1))
        with self.assertRaisesRegex(ValueError, 'restricted to private document input'):
            compiler.write_site(self.public, self.output)

    def test_original_source_references_retain_page_position_and_external_url(self):
        self.make_facsimile()
        self.manifest['pages'][0]['references'] = [
            {'page': 2, 'y': 120.5, 'label': 'Equation (2)', 'rect': [100, 80, 150, 92]},
            {'url': 'https://example.org/source?a=1&b=2', 'label': 'Source', 'rect': [20, 170, 60, 184]},
        ]
        self.save_manifest()
        compiler.write_site(self.public, self.output, private_package=self.private)
        page = (self.output / 'documents/reading/index.html').read_text()
        self.assertIn('href="/documents/reading/pages/002/#at-120.5" data-document-page="2" data-document-y="120.5"', page)
        self.assertIn('href="https://example.org/source?a=1&amp;b=2"', page)
        self.assertIn('Source references on this page', page)

    def test_invalid_reference_targets_are_rejected_before_output(self):
        self.make_facsimile()
        for destination in ({'page': 3}, {'page': 2, 'y': float('nan')}, {'page': 2, 'y': 400}, {'url': 'javascript:alert(1)'}):
            with self.subTest(destination=destination):
                self.manifest['pages'][0]['references'] = [{'label': 'Reference', 'rect': [20, 30, 50, 45], **destination}]
                self.save_manifest()
                with self.assertRaises(ValueError):
                    compiler.write_site(self.public, self.output, private_package=self.private)
                self.assertFalse(self.output.exists())


if __name__ == '__main__':
    unittest.main()
