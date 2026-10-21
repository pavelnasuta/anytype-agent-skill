# Visual Navigation and Governance

## Parent Pages and Native Cards

A navigation parent is any Page containing child Object links—not only a first-level home page. Build a readable branch such as Home → Area → Section → Material, while preserving the fact that an Object can appear in more than one useful context.

A visible child page must be a native Object link card. When the API exposes block fields, use a link block with a target Object, card style, and a visible small icon. Do not replace this with Markdown, a plain URL, or copied text.

## Parent Page Standard

Every parent navigation page has:

1. A semantic title.
2. An icon.
3. A concise Description stored on the Object.
4. Native child link cards.
5. A clear role and controlled tags when it carries meaningful content.

A top-level entry page may additionally have a cover. Do not display a cover placeholder when no intentional cover exists.

## Card Standard

Every navigation card shows the child icon. A card leading to another parent page also shows the target Object Description, but only after both pieces are true: the Object has a Description and the card is configured to show it. Content cards show a Description only when it helps a reader choose among similar materials.

Card background is a sparse semantic signal, not decoration. Keep one short palette per Space and preserve deliberate user choices. Suggested meaning: teal for working areas, blue for reference/system, yellow for product/focus, gray for tests or neutral material, green for completion, orange for drafts, and red only for risk or urgency.

## Taxonomy and Color

Keep controlled tag and Select vocabularies small, singular, and free of accidental synonyms. Assign a stable color to a stable option; color helps scanning but must never be the only meaning. Before changing options or colors, inspect the existing vocabulary and use only a capability confirmed in the current API or UI.

## Dates and Names

A title answers “what is this?” A Date Property answers “when?”. Use a date in a title only when it is part of the identity, such as an issue, release, or archival snapshot. Do not encode a deadline in a title.

## Audit Checklist

- Every parent page has icon and Description.
- Every navigation link is a native card and shows the icon.
- Cards that lead to parent pages show the target Description.
- Meaningful Objects have governed tags and appropriate roles.
- Meaningful dates are Properties.
- Select/Multi-select options are reused, not duplicated.
- Covers and colors match a documented visual purpose.
