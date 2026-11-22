---
event: "Microsoft Ignite 2026"
title: "Build self-optimizing AI agents with Azure Cosmos DB and Fabric"
speaker: "Stef Arroyo, Jai Maldonado, Mike Calvin"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856628645001Etkf-1791588243215001CYFH"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/38e10ff6-e36d-4a37-bb3d-94c4870015d6"
session_id: "BRK365"
session_type: "Breakout"
start: "2026-11-19T17:00:00Z"
level: "(300) Advanced"
ignite_topics: ["Data", "AI", "Agents", "Microsoft Foundry", "Azure Copilot"]
topics: ["cosmos-db", "fabric", "agents", "observability", "customer-story"]
---

# Build self-optimizing AI agents with Azure Cosmos DB and Fabric

**Speaker(s):** Stef Arroyo, Jai Maldonado, Mike Calvin

## Summary

The session builds a multi-agent travel-planning app (Cosmos Voyager) on Azure Cosmos DB and Microsoft Fabric to show how to capture, analyze and improve agent behavior without shipping code. A supervisor agent routes to specialist agents (place search with vector and full-text search, itinerary composition), with Foundry embeddings, and a single Cosmos DB database holds places, trips, chat turns, agent memory and an optimization policy.

The optimization loop mirrors agent turns to Fabric with zero-ETL mirroring to find where cost and latency are wasted, then updates a live policy document (for example, routing trivial, routine and complex requests to different models, with quality guardrails and versioned audit) that the supervisor reads before each turn. Kinectify shares production experience, and the slides cite that Cosmos DB underpins ChatGPT's storage at large scale (OpenAI-reported).

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856628645001Etkf-1791588243215001CYFH
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/38e10ff6-e36d-4a37-bb3d-94c4870015d6
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/38e10ff6-e36d-4a37-bb3d-94c4870015d6
