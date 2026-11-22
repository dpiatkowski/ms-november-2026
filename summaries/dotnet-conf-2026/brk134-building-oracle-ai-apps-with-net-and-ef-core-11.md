---
event: ".NET Conf 2026"
title: "Building Oracle AI Apps with .NET and EF Core 11"
speaker: "Alex Keh"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk134"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/8vxdOlv-n9g"
session_id: "BRK134"
start: "2026-11-13T16:00:00-08:00"
topics: ["oracle", "ef-core", "vector-search", "agent-framework", "data", "community-day", "vendor"]
---

# Building Oracle AI Apps with .NET and EF Core 11

**Speaker(s):** Alex Keh

## Summary

Alex Keh (Oracle) covers what is new for Oracle Database with .NET 11 and EF Core 11, building AI apps on Oracle with Microsoft Agent Framework, and Oracle Deep Data Security. The deck includes a standard forward-looking safe-harbor statement, so roadmap items are not commitments.

## Key points

- ODP.NET Core 23.26.401 is certified with .NET 11; runtime async must be enabled explicitly (<Features>runtime-async=on</Features>); decimal/float/double now give correctly rounded results in OracleDecimal and related types.
- EF Core 11 for Oracle: complex types and JSON columns with TPT/TPC inheritance, keys and indexes on complex type properties, better SQL for to-one joins, FullJoin, MaxBy/MinBy, JsonPathExists, vector search and indexes (.WithApproximate(90)) with vector properties not loaded by default, one-step migrations.
- Oracle.VectorData: vector store connector (Oracle AI Database; schema auto-created from model classes, HNSW, IVF and hybrid indexes, semantic and keyword search, nine distance functions) that supports Microsoft Agent Framework 1.7+ and Oracle Database 19c+ (vector support in 23ai+); demo chat app uses Microsoft.Extensions.AI, Agent Framework and Foundry.
- Deep Data Security: agentic AI and prompt injection turn authorization gaps into data leaks, so policy is enforced in the database for every access path using the end user's identity; ODP.NET passes ASP.NET Core identity, claims and roles to the database via an EndUserSecurityContext provider with minimal code changes.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk134
- Recording: https://youtu.be/8vxdOlv-n9g
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD217/Building-Oracle-AI-Apps-with-.NET-Core-and-EF-Core-11.pdf
