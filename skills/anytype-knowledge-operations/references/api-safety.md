# API Safety and Verification

## Discovery Before Mutation

Confirm the target Space, current role, existing Objects, Types, Properties, navigation, and the exact API schema before writing. Do not infer a feature from a menu label or from a previous API version.

## Safe Writes

- Use dry-run for a new or complex operation when it is available.
- Read the target Object immediately before PATCH.
- Use the server-returned block IDs exactly as returned.
- Use an idempotency key for repeatable mutations.
- Use an available concurrency precondition for every mutation of an existing resource.
- Batch related edits atomically where the API supports it.
- Read the exact target back after every mutation.

## Conflict Handling

On a conflict, stop. Re-read the Object, compare concurrent changes, and rebuild only the minimal intended update. Never blindly retry an old write, remove a concurrency guard, or overwrite another editor's work.

## Capability Boundaries

A feature can exist in the desktop UI without being available to the Local API. If the API offers only read access to an option, do not claim that the agent changed it. State the smallest manual UI step instead.

Do not expose credentials, bearer values, raw API headers, object IDs, or service logs in a user-facing report.
