---
event: "Microsoft Ignite 2026"
title: "Securing coding agents and their code"
speaker: "Ricky Diep, Rohan Parakh"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856615724001Em6f-1791588336956001Cipr"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/b20544dd-c9fb-4b7e-a119-03982aa5f50d"
session_id: "BRK281"
session_type: "Breakout"
start: "2026-11-20T00:00:00Z"
level: "(300) Advanced"
ignite_topics: ["Agent Platform", "Github Copilot", "GitHub", "Model customization", "Observability and evaluation", "Developer Tools"]
topics: ["github", "security", "coding-agents", "sandboxing", "supply-chain"]
categories: ["Application and agent security", "Developer tools and delivery"]
---

# Securing coding agents and their code

**Speaker(s):** Ricky Diep, Rohan Parakh

## Summary

The session lists questions to answer before rolling out coding agents (who or what is acting, what it can read, change and execute, which credentials it uses, where it runs, whether its code is secure, what evidence is kept) and maps GitHub Copilot's built-in protections: limits on who can trigger agents and which branches they push to, a firewall on internet access, hidden-character filtering against prompt injection, signed commits with session and audit logs, and CodeQL, Advisory Database and secret scanning inside the agent loop.

Guidance includes baseline enterprise managed settings (deny destructive operations, ask for installs and network tools, restrict remote control, allowlist MCP servers and plugins, OpenTelemetry export), least-privilege secrets with owners and rotation, GitHub Copilot sandboxes (cloud and local, generally available), and observability via activity view, agent risk from Purview, Entra and Defender, and an agent map. It also covers securing the code agents write: injection and path-traversal patterns, risky or hallucinated dependencies, leaked secrets, code-quality debt and unauthorized changes, each backed by an automated gate.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856615724001Em6f-1791588336956001Cipr
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/b20544dd-c9fb-4b7e-a119-03982aa5f50d
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/b20544dd-c9fb-4b7e-a119-03982aa5f50d
