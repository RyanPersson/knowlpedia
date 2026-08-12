from pathlib import Path
import tempfile
import unittest

from scripts import audit_knowl_scope as audit


class KnowlScopeAuditTests(unittest.TestCase):
    def make_root(self) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        return Path(directory.name)

    def write_knowl(
        self,
        root: Path,
        name: str,
        knowl_id: str,
        title: str,
        body: str,
        *,
        aliases: tuple[str, ...] = (),
        kind: str = "definition",
    ) -> Path:
        path = root / f"{name}.knowl.md"
        alias_text = ", ".join(f'"{alias}"' for alias in aliases)
        path.write_text(
            "+++\n"
            f'id = "{knowl_id}"\n'
            f'title = "{title}"\n'
            f'kind = "{kind}"\n'
            'summary = "Fixture."\n'
            f"aliases = [{alias_text}]\n"
            "+++\n\n"
            f"{body}\n",
            encoding="utf-8",
        )
        return path

    def load_all(self, root: Path) -> list[audit.SourceKnowl]:
        return [audit.load_knowl(path) for path in audit.knowl_paths([root])]

    def test_comparison_key_handles_common_mathematical_plurals(self) -> None:
        self.assertEqual(audit.comparison_key("tori"), "tori")
        self.assertEqual(audit.comparison_key("torus"), "torus")
        self.assertEqual(audit.comparison_key("classes"), "class")
        self.assertEqual(audit.comparison_key("matrices"), "matrix")

    def test_known_global_local_pattern_is_high_confidence(self) -> None:
        root = self.make_root()
        self.write_knowl(
            root,
            "fields",
            "fields",
            "Global and local fields; completions",
            "A **global field** is one of two kinds.\n\n"
            "A **place** \\(v\\) is an equivalence class.\n\n"
            "## Local fields\n\n"
            "A **local field** is a nondiscrete locally compact field.",
        )
        self.write_knowl(
            root,
            "consumer",
            "consumer",
            "Consumer",
            "Let \\(F\\) be a [[fields|local field]].",
        )

        findings = audit.audit(self.load_all(root))
        ownership = [item for item in findings if item["rule"] == "multiple_concept_ownership"]
        self.assertEqual(len(ownership), 1)
        self.assertEqual(ownership[0]["severity"], "high")
        self.assertEqual(
            {item["normalized"] for item in ownership[0]["definition_subjects"]},
            {"global field", "place", "local field"},
        )
        self.assertIn("independent_section_definition", ownership[0]["signals"])

    def test_single_concept_with_pedagogical_sections_is_not_flagged(self) -> None:
        root = self.make_root()
        self.write_knowl(
            root,
            "module",
            "module",
            "Module",
            "A **module** is an abelian group with scalar multiplication.\n\n"
            "## Examples\n\nFree modules are examples.\n\n"
            "## Properties\n\nSubmodules inherit addition.\n\n"
            "## References\n\nA **ring** is discussed in the cited book.",
        )
        self.assertEqual(audit.audit(self.load_all(root)), [])

    def test_compound_title_is_weak_unless_requested(self) -> None:
        root = self.make_root()
        self.write_knowl(
            root,
            "theorem",
            "theorem",
            "Existence and uniqueness theorem",
            "Every object has a unique envelope.",
        )
        knowls = self.load_all(root)
        self.assertEqual(audit.audit(knowls), [])
        findings = audit.audit(knowls, include_weak=True)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "review")

    def test_exact_label_owner_exposes_stale_target(self) -> None:
        root = self.make_root()
        self.write_knowl(
            root,
            "global",
            "global-field",
            "Global field",
            "A **global field** is an arithmetic field.",
        )
        self.write_knowl(
            root,
            "local",
            "local-field",
            "Local field",
            "A **local field** is locally compact.",
        )
        self.write_knowl(
            root,
            "consumer",
            "consumer",
            "Consumer",
            "Let \\(F\\) be a [[global-field|local field]].",
        )
        mismatches = [
            item
            for item in audit.audit(self.load_all(root))
            if item["rule"] == "exact_label_target_mismatch"
        ]
        self.assertEqual(len(mismatches), 1)
        self.assertEqual(mismatches[0]["unique_label_owner"], "local-field")

    def test_secondary_concept_alias_does_not_hide_section_definition(self) -> None:
        root = self.make_root()
        self.write_knowl(
            root,
            "measure",
            "measure",
            "Canonical measure",
            "The construction gives the canonical measure.\n\n"
            "## Associated number\n\n"
            "The **canonical number** is its total volume.",
            aliases=("canonical number",),
        )
        findings = audit.audit(self.load_all(root))
        ownership = [
            item
            for item in findings
            if item["rule"] == "multiple_concept_ownership"
        ]
        self.assertEqual(len(ownership), 1)
        self.assertIn("independent_section_definition", ownership[0]["signals"])

    def test_wrapped_bold_definiendum_is_detected(self) -> None:
        root = self.make_root()
        self.write_knowl(
            root,
            "filtration",
            "filtration",
            "Canonical filtration",
            "A **canonical filtration** is an ordered family.\n\n"
            "## Associated truncation\n\n"
            "This **canonical\ntruncation** is the resulting open condition.",
        )
        findings = audit.audit(self.load_all(root))
        ownership = [
            item
            for item in findings
            if item["rule"] == "multiple_concept_ownership"
        ]
        self.assertEqual(len(ownership), 1)
        self.assertEqual(
            {item["normalized"] for item in ownership[0]["definition_subjects"]},
            {"canonical filtration", "canonical truncation"},
        )

    def test_container_and_protected_regions_do_not_claim_concepts(self) -> None:
        root = self.make_root()
        self.write_knowl(
            root,
            "document",
            "document",
            "Transcript and glossary",
            "`A **code object** is not prose.`\n\n"
            "```text\nA **fenced object** is not prose.\n```\n\n"
            "A **first concept** is prose. A **second concept** is prose.",
            kind="document",
        )
        self.assertEqual(audit.audit(self.load_all(root)), [])


if __name__ == "__main__":
    unittest.main()
