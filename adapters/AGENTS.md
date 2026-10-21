# Anytype Agent Contract

Use `skills/anytype-knowledge-operations/` as the canonical procedure.

Before changing Anytype, discover the target Space and existing data model. Select the right primitive before writing: Object/Page for knowledge, Type for repeated entities, Property for attributes and relationships, Query for living rule-based results, Collection for manual curation, View for alternate presentations, Bookmark for external sources, and File Object for reusable uploads.

Build visible hierarchy with native Object link cards, not Markdown or plain URLs. Treat every parent Page with child cards as a navigation page: it requires an icon and concise Description. Make each navigation card show its target icon; show the target Description when the target is another navigation parent.

Never import secrets, passwords, recovery phrases, private keys, tokens, credential files, or system logs. Reuse Objects and File Objects instead of copying them. Use governed tags and semantic Date Properties.

Before external writes, inspect live capabilities and use a dry run where available. After every write, read back the exact Object. On conflicts, re-read and rebuild the smallest safe update. Never simulate unavailable UI/API behavior.
