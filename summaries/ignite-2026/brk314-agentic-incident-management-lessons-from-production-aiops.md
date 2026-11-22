---
event: "Microsoft Ignite 2026"
title: "Agentic incident management: Lessons from production AIOps"
speaker: "Manjunath Gururaja, Sai Teja Nagamothu"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856620707001EyJO-1791588352983001C0oQ"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/4cf6c299-569e-4596-8ff4-ad54e231148d"
session_id: "BRK314"
session_type: "Breakout"
start: "2026-11-20T01:15:00Z"
level: "(200) Intermediate"
ignite_topics: ["Cloud & AI"]
topics: ["aiops", "incident-management", "agents", "orchestration", "reliability"]
categories: ["Cloud operations", "Security operations"]
---

# Agentic incident management: Lessons from production AIOps

**Speaker(s):** Manjunath Gururaja, Sai Teja Nagamothu

## Summary

Azure Engineering Operations describes agentic incident management after a reported 82% increase in critical incidents, choosing to fix operational demand with engineering and AI agents rather than hiring 50% more on-call engineers. A demo shows a fictional retailer's checkout outage (Sev1 503s) triaged agent-to-agent: the customer's agent sends alert context over an MCP session, Microsoft's agent checks App Service health, deployments and platform correlation, rules out the customer's code, and finds a West US 2 datacenter problem, recommending regional failover.

Design lessons include Incident Memory (facts travel with signal, resource and time) and durable execution (the agent decides, the engine executes with retries and saved steps), plus pre- and post-checks for caller scope and withholding raw logs. The session also covers security, evals and ROI, and three lessons from production.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856620707001EyJO-1791588352983001C0oQ
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/4cf6c299-569e-4596-8ff4-ad54e231148d
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/4cf6c299-569e-4596-8ff4-ad54e231148d
