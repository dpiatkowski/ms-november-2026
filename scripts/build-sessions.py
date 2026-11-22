#!/usr/bin/env python3
"""Build pages/sessions.json from the frontmatter in summaries/<event-slug>/*.md.

Implements the session record described in DESIGN.md ("Data model").
Run from anywhere: python3 scripts/build-sessions.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARIES = ROOT / "summaries"
OUT = ROOT / "pages" / "sessions.json"

EVENTS = {
    "dotnet-conf-2026": ".NET Conf",
    "ignite-2026": "Ignite",
}

LINE = re.compile(r"^([a-z_]+):\s*(.*)$")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: no frontmatter")
    block = text[4 : text.index("\n---", 4)]
    data = {}
    for raw in block.splitlines():
        if not raw.strip():
            continue
        m = LINE.match(raw)
        if not m:
            raise ValueError(f"{path}: cannot parse line {raw!r}")
        key, value = m.groups()
        # Values are written as JSON literals (quoted strings, arrays, null).
        data[key] = json.loads(value)
    return data


def split_speakers(speaker) -> list[str]:
    if not speaker:
        return []
    return [s.strip() for s in re.split(r",|&|\band\b", speaker) if s.strip()]


def record(slug: str, fm: dict, path: Path) -> dict:
    video = fm.get("video_url") or fm.get("ondemand_url")
    if not video:
        print(f"warning: {path.relative_to(ROOT)} has no video URL", file=sys.stderr)
    return {
        "id": f"{slug}/{fm['session_id'].lower()}",
        "event": {"slug": slug, "label": EVENTS[slug]},
        "sessionId": fm["session_id"],
        "title": fm["title"],
        "tags": fm.get("categories") or [],
        "videoUrl": video,
        "sessionUrl": fm.get("source_url"),
        "start": fm.get("start"),
        "search": (fm.get("topics") or []) + split_speakers(fm.get("speaker")),
    }


def main() -> None:
    sessions = []
    for slug in EVENTS:
        for path in sorted((SUMMARIES / slug).glob("*.md")):
            sessions.append(record(slug, frontmatter(path), path))

    order = {slug: i for i, slug in enumerate(EVENTS)}
    sessions.sort(key=lambda s: (order[s["event"]["slug"]], s["start"] is None, s["start"] or "", s["sessionId"]))

    ids = [s["id"] for s in sessions]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"duplicate ids: {sorted(dupes)}")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(sessions, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tags = {t for s in sessions for t in s["tags"]}
    print(f"wrote {len(sessions)} sessions, {len(tags)} tags -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
