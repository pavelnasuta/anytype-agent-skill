# Anytype Agent Skill

Portable operating rules for AI agents that build and maintain structured Anytype spaces.

It helps an agent choose the right Anytype primitive—Object, Type, Property, Template, Query, Collection, View, Block, File, Bookmark, or Embed—then make verified changes without turning a knowledge space into a flat file dump.

## What is included

- A canonical Hermes skill under `skills/anytype-knowledge-operations/`.
- Portable instruction adapters for agents that use `AGENTS.md`, `CLAUDE.md`, or `CODEX.md`.
- Rules for native card navigation, taxonomy, metadata, files, media, visual hierarchy, API safety, and audit checks.
- A local portability validator with no network dependency.

## What it is not

- A backup tool or a replacement for the source of record.
- A generic import script.
- Permission to move secrets, credentials, private keys, recovery phrases, or system logs into Anytype.

## Use with different agents

| Environment | Start here |
|---|---|
| Hermes Agent | `skills/anytype-knowledge-operations/SKILL.md` |
| Codex and compatible coding agents | `adapters/CODEX.md` |
| Claude Code | `adapters/CLAUDE.md` |
| Cursor, OpenCode, Cline, Windsurf and other AGENTS.md-aware tools | `adapters/AGENTS.md` |
| Any other assistant | Copy the contract from `adapters/AGENTS.md` into its project instructions. |

All adapters point to the same operating model. They should be treated as guidance for the agent, not as a claim that every Anytype UI action is available through every API.

## Core contract

1. Discover the target Space and existing model before writing.
2. Choose the data model before importing or creating content.
3. Use native Object cards for visible navigation; use Object-properties for semantic relationships.
4. Reuse files and Objects instead of copying them.
5. Apply governed metadata and semantic dates.
6. Validate every external change by reading the exact target back.
7. Stop rather than simulate a UI or API capability that is unavailable.

## Validation

```bash
python3 scripts/validate.py
python3 -m unittest tests/test_portability.py
```

## Status

This repository is private while the cross-agent adapters and examples are refined. It contains only portable guidance and synthetic examples.
