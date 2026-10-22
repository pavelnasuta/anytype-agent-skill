from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PortabilityTests(unittest.TestCase):
    def test_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("valid", result.stdout)

    def test_adapters_point_to_canonical_skill(self) -> None:
        for name in ("AGENTS.md", "CLAUDE.md", "CODEX.md"):
            text = (ROOT / "adapters" / name).read_text(encoding="utf-8")
            self.assertIn("anytype-knowledge-operations", text)

    def test_retrieval_and_precise_edits_reference_is_present(self) -> None:
        reference = ROOT / "skills" / "anytype-knowledge-operations" / "references" / "retrieval-and-precise-edits.md"
        self.assertTrue(reference.is_file())
        text = reference.read_text(encoding="utf-8")
        for required_heading in (
            "## Search before writing",
            "## Schema snapshot before mutation",
            "## Precise editing of long pages",
            "exact read-back",
        ):
            self.assertIn(required_heading, text)


if __name__ == "__main__":
    unittest.main()
