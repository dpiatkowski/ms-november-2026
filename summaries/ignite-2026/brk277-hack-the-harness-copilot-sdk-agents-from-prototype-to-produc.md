---
event: "Microsoft Ignite 2026"
title: "Hack the harness: Copilot SDK agents from prototype to production"
speaker: "Patrick Nikoletich, Steve Sanderson"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856615129001ELFm-1791588322657001CZrz"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/6a20d667-bc1c-4d81-812a-6cd1df0a4fb3"
session_id: "BRK277"
session_type: "Breakout"
start: "2026-11-18T23:00:00Z"
level: "(300) Advanced"
ignite_topics: ["Agent Platform", "Github Copilot", "Microsoft Entra", "GitHub", "MCP", "Developer Tools"]
topics: ["copilot-sdk", "agent-harness", "orchestration", "architecture"]
---

# Hack the harness: Copilot SDK agents from prototype to production

**Speaker(s):** Patrick Nikoletich, Steve Sanderson

## Summary

This session continues BRK276 on taking Copilot SDK agents from prototype to production. SDK 2.0's multi-tenant support enables five architectures based on where the agent runs: isolated (a sandbox per session for coding agents), shared (support assistants on a shared runtime), promotable (start shared, move to a sandbox when files are needed), direct (shared agent, isolated tools such as code interpreters) and delegate or mixed (coordinators starting worker agents, as in software factories).

Using the managed-copilot-sdk reference implementation, the same CopilotClient/CopilotSession code moves from running locally to a deployed platform, with environment types (shared, isolated, promotable, orchestrator) declared once in an Aspire AppHost. The reference implementation is not a new SDK; it shows placement, sandboxes, policy, secrets and durable work that platform teams must build.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856615129001ELFm-1791588322657001CZrz
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/6a20d667-bc1c-4d81-812a-6cd1df0a4fb3
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/6a20d667-bc1c-4d81-812a-6cd1df0a4fb3
