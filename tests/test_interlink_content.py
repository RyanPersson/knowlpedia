import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "interlink_content.py"
SPEC = importlib.util.spec_from_file_location("interlink_content", SCRIPT)
assert SPEC and SPEC.loader
interlink_content = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = interlink_content
SPEC.loader.exec_module(interlink_content)


def write_knowl(path: Path, knowl_id: str, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "+++\n"
        f'id = "{knowl_id}"\n'
        f'title = "{title}"\n'
        'kind = "definition"\n'
        "+++\n\n"
        f"{body}\n",
        encoding="utf-8",
    )


class InterlinkContentTests(unittest.TestCase):
    def test_scan_ignores_protected_regions_and_applies_selected_link(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            content = repo / "content"
            target = content / "algebra" / "module.knowl.md"
            source = content / "analysis" / "example.knowl.md"
            write_knowl(target, "algebra/module", "Algebraic module", "Definition.")
            write_knowl(
                source,
                "analysis/example",
                "Example",
                "An Algebraic module occurs here.\n"
                "`Algebraic module` is code.\n"
                r"\(Algebraic module\) is math." + "\n"
                "[Algebraic module](https://example.test) is already linked.\n"
                "## References\n"
                "Algebraic module in a citation title.",
            )

            knowls, by_path = interlink_content.load_knowls(content)
            terms = interlink_content.build_terms(
                knowls,
                include_aliases=False,
                include_plurals=False,
                allow_single_word=False,
            )
            terms_by_normalized = {
                term.normalized: term for term in terms
            }
            candidates = interlink_content.scan_file(
                source.resolve(),
                by_path[source.resolve()],
                terms_by_normalized,
                interlink_content.compile_term_pattern(terms),
                repo,
            )

            self.assertEqual(1, len(candidates))
            self.assertEqual("Algebraic module", candidates[0].surface)
            self.assertEqual("core", candidates[0].section)

            applied, changed = interlink_content.apply_candidates(
                repo, candidates, {candidates[0].candidate_id}
            )
            self.assertEqual((1, 1), (applied, changed))
            result = source.read_text(encoding="utf-8")
            self.assertIn(
                "[[algebra/module|Algebraic module]] occurs here", result
            )
            self.assertIn("`Algebraic module` is code", result)
            self.assertIn(r"\(Algebraic module\) is math", result)

    def test_ambiguous_surface_is_not_a_candidate_term(self):
        with tempfile.TemporaryDirectory() as directory:
            content = Path(directory) / "content"
            write_knowl(
                content / "one.knowl.md",
                "one",
                "Regular representation",
                "Definition.",
            )
            write_knowl(
                content / "two.knowl.md",
                "two",
                "Other",
                "Definition.",
            )
            second = content / "three.knowl.md"
            write_knowl(
                second,
                "three",
                "Another",
                "Definition.",
            )
            text = second.read_text(encoding="utf-8")
            second.write_text(
                text.replace(
                    'title = "Another"',
                    'title = "Another"\naliases = ["Regular representation"]',
                ),
                encoding="utf-8",
            )

            knowls, _ = interlink_content.load_knowls(content)
            terms = interlink_content.build_terms(
                knowls,
                include_aliases=True,
                include_plurals=False,
                allow_single_word=False,
            )
            self.assertNotIn(
                "regular representation",
                {term.normalized for term in terms},
            )


if __name__ == "__main__":
    unittest.main()
