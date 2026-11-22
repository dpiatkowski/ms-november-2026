---
event: ".NET Conf 2026"
title: "Eliminating Hidden Dangers to Your Applications: Patterns for Reliable Systems"
speaker: "Barry Stahl"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk121"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/wIlPm6XhRPQ"
session_id: "BRK121"
start: "2026-11-13T09:30:00-08:00"
topics: ["reliability", "dual-writes", "outbox", "distributed-systems", "architecture", "community-day"]
categories: ["Application architecture", "Operations and reliability"]
---

# Eliminating Hidden Dangers to Your Applications: Patterns for Reliable Systems

**Speaker(s):** Barry Stahl

## Summary

Barry Stahl explains the dual-writes anti-pattern: it is impossible to reliably make two changes (e.g. update a database and send a message) in one execution context, so failures show up as duplicate, missing or incomplete data that is hard to detect, remediate or replicate. The talk covers patterns to avoid it, using a bus-maintenance domain (telemetry creating a work order and notifying the manufacturer).

## Key points

- Why it breaks: sending then committing or committing then sending each have failure windows (a Two Generals problem); acknowledgements can't give certainty. Two changes are only safe in one context if the first is idempotent and the second is allowed to be unreliable. Making the service idempotent is the simplest fix but often not possible.
- Isolation patterns: Transactional Outbox (one atomic write stores the data change and a command; at-least-once delivery, but hard to scale and uses the DB as a queue), Change-Data-Capture (e.g. Cosmos DB change feed; easy to scale and fan out, but some implementations don't capture every update) and Data Streaming (persist the message first; reliability depends on the stream's persistence). All are typically at-least-once; the speaker has never found exactly-once strictly necessary.
- Coordination: Sagas by orchestration (central controller/workflow, can reverse actions) or choreography (each service does one thing from events); he prefers choreography of services isolated with CDC and streaming.
- Summary: persist first then act, prefer CDC or streaming for fan-out, use idempotence whenever possible, avoid 'add-ons', consider sagas for complex interactions.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk121
- Recording: https://youtu.be/wIlPm6XhRPQ
- Eliminating Hidden Dangers - Short Session - Slide Deck: https://cognitiveinheritance.com/Presentations/ShortSession/EliminatingHiddenDangers/index.html
- AZGiveCamp: https://www.azgivecamp.org/
- Cognitive Inheritance: https://cognitiveinheritance.com/
- @bsstahl@cognitiveinheritance.com: https://fosstodon.org/@Bsstahl
