import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.generate_content_review import modified_knowl_paths


class GenerateContentReviewTests(unittest.TestCase):
    def git(self, repo: Path, *args: str) -> None:
        subprocess.run(
            ["git", *args],
            cwd=repo,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def test_ref_comparison_selects_only_modified_existing_knowls(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test User")
            self.git(repo, "config", "user.email", "test@example.com")
            content = repo / "content"
            content.mkdir()
            existing = content / "existing.knowl.md"
            existing.write_text("old\n", encoding="utf-8")
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "baseline")
            self.git(repo, "branch", "baseline")

            existing.write_text("new\n", encoding="utf-8")
            (content / "added.knowl.md").write_text("added\n", encoding="utf-8")
            self.git(repo, "add", "content")
            self.git(repo, "commit", "-m", "changes")

            self.assertEqual(
                modified_knowl_paths(repo, "baseline", "HEAD"),
                ["content/existing.knowl.md"],
            )


if __name__ == "__main__":
    unittest.main()
