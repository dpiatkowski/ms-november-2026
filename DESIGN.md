# Site design

A single-page, filterable list of the technical sessions summarized in this repository (.NET Conf 2026 and Microsoft Ignite 2026). Audience: developers and engineers who want to find recordings on a topic quickly.

This document covers information architecture, data model, visual design, and interaction. The tech stack (generator, build, hosting) is decided separately.

## Principles

- **Scan, then filter.** Hundreds of sessions are read as a dense list, narrowed by tags and search.
- **Tags are first-class.** Every row shows its tags; tags are the primary way to filter.
- **Nothing that isn't needed.** Rows carry title, tags, and links. No summaries, thumbnails, speakers, or dates on screen.
- **Neutral and unofficial.** Dev-tool / documentation look. No Microsoft branding, colours, or logos — the project is not affiliated with Microsoft.

## Information architecture

- One page. No per-event pages, no per-session detail pages.
- Both events appear in one combined list; event is a filter dimension, not a navigation level.
- Page regions: header (site name, search), sidebar (tag filters), result line, session list, footer.

## Data model

The markdown frontmatter under `summaries/<event-slug>/*.md` is the source of truth. The site consumes a derived, event-neutral **session record**:

| Field        | Type                                 | Source                                                                         | Use                         |
|--------------|--------------------------------------|--------------------------------------------------------------------------------|-----------------------------|
| `id`         | string                               | `<event-slug>/<session_id lowercased>`, e.g. `ignite-2026/brk101`              | Identity, keys              |
| `event`      | `{ slug, label }`                    | Folder name → event table                                                      | Muted label, event filter   |
| `sessionId`  | string                               | `session_id`, e.g. `BRK101`                                                    | Displayed in monospace      |
| `title`      | string                               | `title`                                                                        | Displayed, searched         |
| `tags`       | string[]                             | `categories`                                                                   | Displayed, filtered         |
| `videoUrl`   | string                               | `video_url` (.NET Conf, YouTube) · `ondemand_url` (Ignite, medius.microsoft.com) | **Watch** link            |
| `sessionUrl` | string                               | `source_url`                                                                   | **Session page** link       |
| `start`      | ISO 8601 string                      | `start`                                                                        | Sorting only, not displayed |
| `search`     | string[]                             | `topics` + speaker names (split from `speaker`)                                | Hidden search terms         |

Rules:

- **Identity.** `session_id` alone is not unique across events (`BRK101` exists in both), so `id` is always event-scoped. The event slug equals the folder name, so `id` maps directly to the summary file.
- **Event table.** A small fixed table maps slug → short label. Labels omit the year:
  - `dotnet-conf-2026` → `.NET Conf`
  - `ignite-2026` → `Ignite`
- **One video URL per session.** Every session has exactly one recording link. Which frontmatter field provides it depends on the event (see table).
- **Not exposed to the site:** `level`, `session_type`, `ignite_topics`, `summary_type`, `source_type`, and the summary body. They remain in the markdown.

### Tag vocabulary

- Tags come from **one controlled vocabulary shared across all events**, stored as a data file next to the summaries (not in this document).
- Definition (carried over from `summaries/dotnet-conf-2026-categories.md`): categories identify technologies a session starts from or teaches, and engineering practices it covers. A session can have several.
- Free-form `topics` and Ignite's `ignite_topics` are never shown as tags.
- **Prerequisite:** Ignite sessions currently have no `categories`. They must be categorized from the shared vocabulary (extending it where needed, e.g. Microsoft 365, Fabric) before the site can filter them meaningfully.
- Target size: roughly 20–40 tags in total, so the full list fits in the sidebar.

## Layout

### Desktop

```
┌──────────────────────────────────────────────────────────────────┐
│ Site name                                   [ / Search…        ] │
├───────────────┬──────────────────────────────────────────────────┤
│ Event         │ 128 of 836 sessions · Clear filters              │
│ ☐ .NET Conf 80│──────────────────────────────────────────────────│
│ ☐ Ignite  756 │ What's new in the MCP C# SDK                     │
│               │ .NET Conf BRK021  [MCP] [AI applications]        │
│ Tags          │                         Watch · Session page     │
│ ☐ .NET     28 │──────────────────────────────────────────────────│
│ ☑ Security  8 │ …                                                │
│ ☐ Testing   0 │                                                  │
│ …             │                                                  │
├───────────────┴──────────────────────────────────────────────────┤
│ Footer: disclaimer · license · repository                        │
└──────────────────────────────────────────────────────────────────┘
```

### Mobile

- Desktop-first, fully usable on phones.
- Sidebar collapses into a **Filters** disclosure above the list; its button shows the number of active filters.
- Rows stack: title, then meta + tags (wrapping), then links.
- No horizontal page scroll.

## Session row

Content, in order:

1. **Title** — primary text, the most prominent element in the row.
2. **Meta** — event label and session ID (ID in monospace), small and muted.
3. **Tags** — every tag on the session, as chips. Clicking a chip toggles that tag filter.
4. **Links** — `Watch` (→ `videoUrl`) and `Session page` (→ `sessionUrl`). Both open in a new tab and are marked as external.

Rows are compact (one to two lines on desktop), separated by hairline dividers. No cards, no thumbnails, no summaries.

## Filtering and search

- **Tags combine with AND.** Selecting several tags narrows the list to sessions that have all of them.
- **Event filter** works alongside tags (selecting both events, or none, means no event restriction).
- **Live counts.** Each tag and event shows how many sessions would match if it were added to the current filters.
- **Tag order** is alphabetical and never changes while filtering.
- **Zero-count tags** stay visible but are dimmed and disabled.
- **Search** is instant and client-side. It matches title, plus the hidden `search` terms (topics, speaker names). It combines with tag filters using AND.
- **Result line** above the list: `N of 836 sessions`. A **Clear filters** action appears only when a filter or search is active.
- **Empty state:** "No sessions match" plus the same Clear filters action.

### Order

Flat list, no group headers, no sort control. Sorted by event, then `start`, then `sessionId`.

### URL state

Search text and selections are mirrored in the query string so views can be bookmarked and shared, e.g. `?tags=security,mcp&event=ignite-2026&q=nuget`. Loading such a URL restores the view. Tag values in the URL use stable slugs of tag names.

## Visual design

- **Look:** neutral documentation / developer-tool. Restrained palette, plenty of whitespace between regions, density within the list.
- **Colour:** neutral greys for text, borders, and inactive chips. **One accent colour**, used for active filters, selected chips, focus rings, and links. Tags are not individually coloured.
- **Typography:** system UI font stack for text; system monospace stack for session IDs. No web fonts.
- **Themes:** light and dark. Follows `prefers-color-scheme` by default, with a manual toggle in the header that is remembered per browser. All colours are defined as tokens and redefined per theme.
- **Motion:** minimal; none beyond subtle state transitions, and none when `prefers-reduced-motion` is set.

## Accessibility

- WCAG 2.2 AA contrast in both themes, including muted meta text and dimmed tags.
- Fully keyboard operable. `/` focuses search; `Esc` clears and leaves search.
- Tag and event filters are real checkboxes (sidebar) or toggle buttons with `aria-pressed` (chips in rows).
- Visible focus indicators on every interactive element.
- The result count is announced via a polite live region when it changes.
- External links indicate that they open in a new tab.

## Footer

Minimal, repeating the README essentials:

- Not affiliated with, endorsed by, or sponsored by Microsoft.
- Original content is licensed CC BY 4.0; titles, speaker names, and links are included for identification and attribution; original conference materials remain their owners' property.
- Summaries are AI-assisted and may contain inaccuracies.
- Link to the repository.
