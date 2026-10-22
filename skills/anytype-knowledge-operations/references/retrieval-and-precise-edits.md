# Retrieval and Precise Edits

## Search before writing

Search is a discovery operation, not a reason to mutate a Space.

1. Confirm the target Space and inspect the current API schema. Do not assume full-text or semantic search is available because another Anytype client supports it.
2. If the current API schema confirms full-text search, start with it for names, distinctive wording, or a known source. Use semantic search only when the current API exposes it and the request is conceptual, thematic, or poorly phrased for literal search. If the available API provides no suitable search, state the capability boundary; do not infer absence or create a potential duplicate.
3. Return a compact candidate set: Object name, Type, short relevant excerpt, and why it matched. Fetch full Objects only for the candidates needed to answer or to prepare an explicitly approved edit.
4. Treat an empty result as an outcome, not evidence that the material does not exist. Broaden the query or explain the capability boundary before creating a duplicate.
5. Do not expose credentials, raw traces, Object IDs, or unrelated snippets in a user-facing report.

## Schema snapshot before mutation

Before creating or changing an Object in an existing Type:

1. Read the current Type definition, global Properties and their formats, current Select/Multi-select options, and one representative Object when one exists.
2. Build a short schema snapshot: resolved Type, reusable Properties, allowed controlled values, required relationships, and relevant visual or navigation rules.
3. Compare the requested data with that snapshot. Reuse an equivalent Property or option; do not silently create synonyms, parallel statuses, or an incompatible Property format.
4. If the requested schema conflicts with existing meaning, stop and propose the smallest explicit migration or new Property. Do not auto-prefix a conflicting Property merely to make a write succeed.
5. After an approved mutation, verify the exact target with an exact read-back.

## Precise editing of long pages

Prefer a minimal, identifiable change over a whole-page replacement.

1. Fetch the exact target immediately before the edit, including current blocks, block IDs, and concurrency information when available.
2. Identify one unique semantic target: a block ID, heading plus nearby text, or another unambiguous anchor. If it has zero or multiple matches, stop and ask for a narrower target rather than guessing.
3. Use minimal block operations where the API supports them. If a Markdown or text bridge is unavoidable, replace only the uniquely matched fragment; never re-send the entire page to alter one section.
4. Use ETag/If-Match and an idempotency key when the endpoint supports them. On a conflict, re-read, compare concurrent work, and rebuild only the intended minimal edit.
5. Confirm the changed fragment and preservation of adjacent content through an exact read-back. Report a failed or ambiguous edit as failed; do not claim a plausible result.

## Boundaries

These workflows do not authorize bulk export, hidden indexing, deletion, archival, permission changes, or schema redesign. Those actions require explicit approval and their own verification.
