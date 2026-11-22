---
event: "Microsoft Ignite 2026"
title: "Building agentic retrieval: From DIY to Foundry IQ"
speaker: "Pamela Fox, Matt Gotteiner"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856618592001EPDX-1791588235919001CbbF"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/b575c273-cf0d-44d5-b578-3d7e52783cfb"
session_id: "BRK300"
session_type: "Breakout"
start: "2026-11-19T22:45:00Z"
level: "(200) Intermediate"
ignite_topics: ["Microsoft IQ", "Foundry IQ", "Knowledge retrieval", "Model customization"]
topics: ["foundry-iq", "agentic-retrieval", "azure-ai-search", "rag", "performance"]
categories: ["AI apps and agents", "AI grounding and retrieval"]
---

# Building agentic retrieval: From DIY to Foundry IQ

**Speaker(s):** Pamela Fox, Matt Gotteiner

## Summary

The session compares a hand-built retrieval loop with Foundry IQ, using a fictional chocolate maker whose answers require evidence from documents across the business. A baseline combines keyword and vector search with semantic ranking; it can miss part of a compound question when a single query returns lopsided results. The DIY approach adds query planning, parallel searches and reflection to find missing evidence, at the cost of more model calls, routing logic and tuning.

Foundry IQ Auto starts with a search and, when the evidence is insufficient, can use Microsoft Retriever 1 to search again or escalate to an Azure OpenAI model. The agent receives evidence to use in its answer; teams still own their knowledge sources and answer evaluation. In the presenters' example, Auto reduced median retrieval time from 4.46 to 0.76 seconds and Azure OpenAI token use by 69%, while evidence recall fell from 69% to 64%. These are the session's evaluation results, not universal performance guarantees.

The comparison also shows that managed retrieval is not always cheaper: the compound-question example cost more with Foundry IQ Auto, while the simple and multi-hop examples cost less. The slides provide sample code for both approaches and an agentic search option on an existing search index.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856618592001EPDX-1791588235919001CbbF
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/b575c273-cf0d-44d5-b578-3d7e52783cfb
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/b575c273-cf0d-44d5-b578-3d7e52783cfb
