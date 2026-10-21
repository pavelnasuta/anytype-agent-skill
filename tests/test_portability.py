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


if __name__ == "__main__":
    unittest.main()
