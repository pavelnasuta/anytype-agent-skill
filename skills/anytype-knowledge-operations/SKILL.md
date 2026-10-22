---
name: anytype-knowledge-operations
description: Build verified, structured knowledge spaces in Anytype.
version: 1.1.0
author: Pavel Nasuta, Hermes Agent
license: Private
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [anytype, knowledge-management, data-modeling, local-api]
    related_skills: []
---

# Anytype Knowledge Operations

Use this skill to create, organize, import, audit, or automate an Anytype space. The goal is a connected, readable knowledge system—not a flat list of uploaded files.

## Before Writing

1. Identify one target Space and confirm access.
2. Read existing Objects, Types, Properties, navigation, Views, and duplicates.
3. Choose the model before creating anything.
4. Do not import secrets, passwords, recovery phrases, private keys, API tokens, credential files, or system logs.

## Choose the Right Primitive

| Need | Use |
|---|---|
| A document or navigation page | Page / Object |
| A repeated entity with one schema | Type |
| An attribute or semantic relationship | Property |
| A repeatable starting layout | Template |
| A living rule-based result set | Query |
| A hand-curated mixed set | Collection |
| Another presentation of the same data | View |
| A visible child in a page tree | Native Object link card |
| An external source | Bookmark |
| A reusable upload | File Object |

## Non-Negotiable Rules

- Do not use hierarchy, Types, Properties, Queries, and Collections as interchangeable substitutes.
- Use native card links for visible child pages; a plain URL is not a card.
- Reuse the same Object or File Object in multiple places instead of duplicating it.
- Name Objects for meaning. Store meaningful dates in Date Properties, not merely in titles.
- Govern tag and Select vocabularies; do not create synonyms casually.
- A parent navigation page needs an icon and a concise Description. Top-level entry pages may additionally have covers.
- Every external mutation needs an exact read-back. Do not claim a visual state that was not verified.

## References

- `references/operating-model.md` — Objects, Types, Properties, Templates, Queries, Collections, Views, files, media, and embeds.
- `references/visual-navigation.md` — parent pages, card links, icons, descriptions, covers, and visual taxonomy.
- `references/api-safety.md` — discovery, dry runs, concurrency, and verification.
- `references/retrieval-and-precise-edits.md` — full-text/semantic discovery, schema snapshots, and minimal long-page edits.

## User Report

Report only the outcome, the verification that matters, and one genuine blocker or requested action. Do not expose tokens, object IDs, API headers, or raw logs.
