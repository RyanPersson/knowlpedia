from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit_subject_pages.py"
SPEC = importlib.util.spec_from_file_location("audit_subject_pages", MODULE_PATH)
assert SPEC and SPEC.loader
audit_module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit_module
SPEC.loader.exec_module(audit_module)


class AuditSubjectPagesTests(unittest.TestCase):
    def run_audit(self, pages: dict[str, tuple[str, str] | tuple[str, str, str]]) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for knowl_id, page in pages.items():
                kind, body, *rest = page
                extra = f'redirect_to = "{rest[0]}"\n' if rest else ""
                path = root / f"{knowl_id}.knowl.md"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(
                    f'+++\nid = "{knowl_id}"\ntitle = "{knowl_id}"\nkind = "{kind}"\nsummary = "s"\n{extra}+++\n\n{body}\n',
                    encoding="utf-8",
                )
            return {report.subject: report for report in audit_module.audit(audit_module.load_knowls(root))}

    def missing(self, report: object) -> list[str]:
        return [item["id"] for item in report.missing]

    def test_flags_an_unlisted_knowl(self) -> None:
        reports = self.run_audit(
            {"s": ("section", "- [[s/listed|Listed]]"), "s/listed": ("definition", "x"), "s/lost": ("definition", "x")}
        )
        self.assertEqual(self.missing(reports["s"]), ["s/lost"])

    def test_knowl_listed_on_a_reachable_sub_index_is_found(self) -> None:
        reports = self.run_audit(
            {"s": ("index", "[[s/sub-index|Sub]]"), "s/sub-index": ("index", "- [[s/deep|Deep]]"), "s/deep": ("definition", "x")}
        )
        self.assertEqual(self.missing(reports["s"]), [])
        self.assertEqual(reports["s"].unreached_hubs, [])

    def test_sub_index_nothing_links_to_does_not_count(self) -> None:
        reports = self.run_audit(
            {"s": ("section", "None."), "s/orphan-index": ("index", "- [[s/deep|Deep]]"), "s/deep": ("definition", "x")}
        )
        self.assertEqual(reports["s"].unreached_hubs, ["s/orphan-index"])
        self.assertEqual(self.missing(reports["s"]), ["s/deep", "s/orphan-index"])

    def test_links_from_ordinary_knowls_do_not_count(self) -> None:
        reports = self.run_audit(
            {"s": ("section", "- [[s/a|A]]"), "s/a": ("definition", "See [[s/b|B]]."), "s/b": ("definition", "x")}
        )
        self.assertEqual(self.missing(reports["s"]), ["s/b"])

    def test_site_path_links_count_and_redirects_resolve(self) -> None:
        reports = self.run_audit(
            {
                "s": ("section", "[A](/s/a/) and [[s/old|B]]"),
                "s/a": ("definition", "x"),
                "s/old": ("definition", "x", "s/b"),
                "s/b": ("definition", "x"),
            }
        )
        self.assertEqual(self.missing(reports["s"]), [])

    def test_links_in_code_do_not_count(self) -> None:
        reports = self.run_audit({"s": ("section", "`[[s/a|A]]`"), "s/a": ("definition", "x")})
        self.assertEqual(self.missing(reports["s"]), ["s/a"])

    def test_subject_without_a_landing_page_is_reported(self) -> None:
        reports = self.run_audit({"s/a": ("definition", "x")})
        self.assertFalse(reports["s"].has_landing_page)
        self.assertEqual(self.missing(reports["s"]), ["s/a"])

    def test_collections_are_skipped(self) -> None:
        self.assertNotIn("shale-paper", self.run_audit({"shale-paper/a": ("definition", "x")}))


if __name__ == "__main__":
    unittest.main()
