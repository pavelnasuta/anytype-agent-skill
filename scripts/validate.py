#!/usr/bin/env python3
"""Offline checks for the portable Anytype skill package."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "anytype-knowledge-operations" / "SKILL.md"
REQUIRED = [
    ROOT / "README.md",
    SKILL,
    ROOT / "skills" / "anytype-knowledge-operations" / "references" / "operating-model.md",
    ROOT / "skills" / "anytype-knowledge-operations" / "references" / "visual-navigation.md",
    ROOT / "skills" / "anytype-knowledge-operations" / "references" / "api-safety.md",
    ROOT / "adapters" / "AGENTS.md",
    ROOT / "adapters" / "CLAUDE.md",
    ROOT / "adapters" / "CODEX.md",
]
FORBIDDEN = [
    re.compile(r"/root/"),
    re.compile(r"participant-[A-Za-z0-9_-]+"),
    re.compile(r"anytype_[0-9A-Za-z]{20,}"),
    re.compile(r"gho_[0-9A-Za-z]+"),
    re.compile(r"НИИ МОЗГИ"),
]


def main() -> None:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.is_file()]
    assert not missing, f"missing required files: {missing}"

    skill = SKILL.read_text(encoding="utf-8")
    assert skill.startswith("---\n"), "SKILL.md must begin with YAML frontmatter"
    assert "\n---\n" in skill[4:], "SKILL.md frontmatter is not closed"
    assert "name: anytype-knowledge-operations" in skill
    assert "description:" in skill

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path == Path(__file__):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN:
            assert not pattern.search(text), f"portable package contains private data pattern {pattern.pattern} in {path.relative_to(ROOT)}"

    print("portable skill package: valid")


if __name__ == "__main__":
    main()
