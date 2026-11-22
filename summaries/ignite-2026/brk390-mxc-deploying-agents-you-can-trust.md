---
event: "Microsoft Ignite 2026"
title: "MXC: Deploying Agents You Can Trust"
speaker: "Demitrius Nelon, Stuart Schaefer, David Wiesen"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856632584001E5Dw-1791588154118001C10P"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/4fc7562b-4700-4652-9fa2-923cf6b2a254"
session_id: "BRK390"
session_type: "Breakout"
start: "2026-11-18T19:30:00Z"
level: "(400) Expert"
ignite_topics: ["Windows", "Identity and network access", "AI controls", "Agents", "Windows", "Windows Developer", "Governance", "Azure Copilot", "Secure AI"]
topics: ["windows", "agents", "sandboxing", "microsoft-execution-containers", "security"]
categories: ["AI governance and safety", "Application and agent security", "Endpoint management"]
---

# MXC: Deploying Agents You Can Trust

**Speaker(s):** Demitrius Nelon, Stuart Schaefer, David Wiesen

## Summary

The session argues agents cannot be their own security authority: a prompt is not an observable boundary, and one broad container forces maximal scope. It frames three needs (containment, identity, governance) and says least privilege needs more than one sandbox, with process, session, VM/WSL, microVM and cloud boundaries chosen per task rather than as a strongest-to-weakest ladder. Policy sits outside the agent and the OS enforces it; unsupported policy should be surfaced, not silently weakened.

Demos on Microsoft Execution Containers (MXC) show scoping a Windows tool call (shared kernel, so containing one tool does not contain the whole agent), giving an agent its own Windows identity in a separate session and profile, running OpenCode in a local microVM (experimental backend with a separate guest kernel) and a cloud microVM via Azure Container Instances. Automatic sandbox routing is described as future work.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856632584001E5Dw-1791588154118001C10P
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/4fc7562b-4700-4652-9fa2-923cf6b2a254
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/4fc7562b-4700-4652-9fa2-923cf6b2a254
