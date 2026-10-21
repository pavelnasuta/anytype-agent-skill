# Operating Model

## Object First

Every useful item in Anytype is an Object. A Page, Task, Bookmark, Image, PDF, and custom record can be connected from multiple contexts without copying it. Navigation is a reading layer, not a folder system.

## Model Selection

| Use | When |
|---|---|
| Page | A readable document, section, or dashboard |
| Custom Type | A stable, repeated entity that needs a shared schema |
| Property | A reusable attribute, controlled classification, date, file, or Object link |
| Template | The starting structure for new Objects of a Type, Query, Collection, or View |
| Query | A result set that should update automatically from rules |
| Collection | A manually curated, mixed set without one durable rule |
| View | A filter, sort, layout, or grouping over existing Objects |
| Bookmark | A web source that should retain title, preview, tags, and links |
| File Object | An image, video, audio, PDF, or attachment that can be reused |

Do not create a Type for a one-off page. Do not use a Collection where a Query can express the rule. Do not create a Query just to replace a useful Type View.

## Properties

Use Text for free context, Number for numeric values, Date for business-relevant time, Select for exactly one controlled value, Multi-select for independent controlled tags, Checkbox for durable true/false state, Object for relationships, and File & Media for attachments.

A Property exists independently from a Type. Reuse an existing Property when its meaning is identical; do not invent parallel concepts such as Status, Stage, and Phase without an explicit migration.

## Page Blocks

Use headings and a table of contents for long material; toggles for secondary detail; callouts for rules; code blocks for code; and a table block only for a local comparison. A table block is not a database: it does not provide typed Select cells, reliable filters, or Query support.

Use a To-do block for an action inside one page. Use a Checkbox Property for durable, filterable state across Objects.

## Files, Media, Bookmarks, and Embeds

Upload a file once as a File Object, then link or embed the same Object where needed. Use a Bookmark when a URL is a source to find, tag, connect, and revisit. Use an Embed only for a currently supported service and only when live rendering adds value.

Supported services and API capabilities vary by Anytype version and client. Before an automated media or embed workflow, inspect the current API schema and test one harmless Object. If a service cannot embed, use a Bookmark or Link; do not pretend it is embedded.

## Templates and Views

Templates standardize blocks, Properties, defaults, icon policy, and layout for new Objects. They do not retrofit old Objects. Views change presentation without duplicating data; use Grid for operational metadata, Gallery for visual materials, Calendar for meaningful dates, and Kanban only when a Select lifecycle supports it.
