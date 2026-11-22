---
event: "Microsoft Ignite 2026"
title: "See how the Microsoft Copilot harness powers Copilot Studio"
speaker: "Alice Appleton"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856612459001EfZu-1791588174633001COAZ"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/57bd65b7-dce0-4d9d-9d20-70a3b284e9bd"
session_id: "BRK259"
session_type: "Breakout"
start: "2026-11-20T01:15:00Z"
level: "(200) Intermediate"
ignite_topics: ["Agent Platform", "Github Copilot", "Copilot studio"]
topics: ["copilot-studio", "copilot-harness", "multi-agent", "skills", "azure-containers"]
---

# See how the Microsoft Copilot harness powers Copilot Studio

**Speaker(s):** Alice Appleton

## Summary

The session explains why Copilot Studio was rebuilt on the Microsoft Copilot SDK harness. It traces the move from chat harnesses to reasoning harnesses that plan, call tools, check results and recover, and says the team chose to start fresh on the SDK rather than evolve the standard harness.

The new harness has an agentic loop, an Azure container sandbox with CLI tools and a file system, and a trust layer for DLP, sensitivity labels and auditing. It routes models and tools, manages context and memory, enforces limits and works across providers (Anthropic, OpenAI, Mistral and others) with Auto and three simple model tiers. On offline evals, the slides show quality gains of +11.9 to +47.5 points over the standard Copilot Studio harness across knowledge, code analysis, file analysis and multi-tool tasks, with lower input-token cost, all run on one model. The team also shows Copilot Studio built using its own agents.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856612459001EfZu-1791588174633001COAZ
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/57bd65b7-dce0-4d9d-9d20-70a3b284e9bd
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/57bd65b7-dce0-4d9d-9d20-70a3b284e9bd
