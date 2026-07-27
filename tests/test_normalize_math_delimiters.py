from __future__ import annotations

import importlib.util
import sys
import tomllib
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "normalize_math_delimiters.py"
SPEC = importlib.util.spec_from_file_location("normalize_math_delimiters", MODULE_PATH)
assert SPEC and SPEC.loader
normalizer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = normalizer
SPEC.loader.exec_module(normalizer)


class NormalizeMathDelimitersTests(unittest.TestCase):
    def test_converts_inline_and_display_dollar_math(self) -> None:
        source = "Let $x \\in X$.\n\n$$\nx^2 + y^2\n$$\n"
        result = normalizer.normalize_text(source)
        self.assertEqual(
            result.text,
            "Let \\(x \\in X\\).\n\n\\[\nx^2 + y^2\n\\]\n",
        )
        self.assertEqual(result.inline_count, 1)
        self.assertEqual(result.display_count, 1)

    def test_preserves_existing_tex_delimiters_and_escaped_dollars(self) -> None:
        source = r"Keep \(x\), \[y\], and \$5."
        self.assertEqual(normalizer.normalize_text(source).text, source)

    def test_preserves_inline_and_fenced_code(self) -> None:
        source = (
            "Use `$value` beside $x$.\n\n"
            "```python\n"
            'price = "$5"\n'
            "formula = '$x$'\n"
            "```\n"
        )
        expected = source.replace("beside $x$.", r"beside \(x\).")
        self.assertEqual(normalizer.normalize_text(source).text, expected)

    def test_is_idempotent(self) -> None:
        once = normalizer.normalize_text("Inline $x$ and display $$y$$.").text
        self.assertEqual(normalizer.normalize_text(once).text, once)

    def test_normalizes_toml_strings_with_valid_escaping(self) -> None:
        source = (
            "+++\n"
            'title = "Maps $f\\\\colon X \\\\to Y$"\n'
            "summary = 'An element $x$.'\n"
            'aliases = ["Price $5", "Formula $y$"]\n'
            "+++\n\n"
            "Body $z$.\n"
        )
        result = normalizer.normalize_knowl_source(source)
        closing = result.text.find("\n+++")
        metadata = tomllib.loads(result.text[4:closing])
        self.assertEqual(metadata["title"], r"Maps \(f\colon X \to Y\)")
        self.assertEqual(metadata["summary"], r"An element \(x\).")
        self.assertEqual(metadata["aliases"], ["Price $5", r"Formula \(y\)"])
        self.assertIn(r"Body \(z\).", result.text)


if __name__ == "__main__":
    unittest.main()
