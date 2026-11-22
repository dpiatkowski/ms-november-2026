# Keeping up with Microsoft in November 2026

Original editorial content and session summaries, to the extent protected by copyright and owned by the contributors, are made available under Creative Commons Attribution 4.0 International (CC BY 4.0).

Presentation titles, speaker names, and source links are provided for identification and attribution purposes.

All original conference materials, including session descriptions, videos, slides, and transcripts, remain the property of their respective copyright holders and are not relicensed by this project.

Summaries are generated with AI assistance from publicly available source materials. They are independent, unofficial interpretations and may contain inaccuracies.

This project is not affiliated with, endorsed by, or sponsored by Microsoft.

## Site

`pages/` holds the static site published to GitHub Pages (see `DESIGN.md`). `pages/sessions.json` is generated from the summary frontmatter:

```sh
python3 scripts/build-sessions.py
python3 -m http.server -d pages   # preview at http://localhost:8000
```
