---
event: "Microsoft Ignite 2026"
title: "Build with Web IQ: From API call to cited answer"
speaker: "Brian King, Deena Minwalla, Takahiro Tsuchiya"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856620560001E6PE-1791814921993001CD2x"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/3db0a967-9023-4766-86b6-b08faeaa8043"
session_id: "BRK313"
session_type: "Breakout"
start: "2026-11-20T01:15:00Z"
level: "(300) Advanced"
ignite_topics: ["Microsoft IQ"]
topics: ["web-iq", "grounding", "citations", "api", "tracing"]
categories: ["AI grounding and retrieval"]
---

# Build with Web IQ: From API call to cited answer

**Speaker(s):** Brian King, Deena Minwalla, Takahiro Tsuchiya

## Summary

The session is a developer walkthrough of Web IQ as a web-grounding API: it returns fresh, cited passages (title, URL, timestamps) at question time instead of answers frozen at the model's training cutoff. Web IQ Auto, generally available, turns agent intent into compact cited evidence in one call, adapting depth to the task and lowering token cost.

A first call is a REST (or MCP) request to a web search endpoint with parameters such as maxResults, contentFormat (passage) and maxLength. Returning only the query-relevant passage rather than the whole page is illustrated as about 750 versus 12,000 tokens (about 94% fewer, illustrative). Responses carry title, URL, content, crawledAt and a trace ID, and Toyota Motor Corporation shares its use.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856620560001E6PE-1791814921993001CD2x
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/3db0a967-9023-4766-86b6-b08faeaa8043
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/3db0a967-9023-4766-86b6-b08faeaa8043
