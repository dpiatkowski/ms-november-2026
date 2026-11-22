---
event: "Microsoft Ignite 2026"
title: "Winning the Race Against Time with Autonomous Protection"
speaker: "Noam Hadash, Raviv Tamir, Ken Robb"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856621042001EDGy-1791588155309001C8PS"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/f65dde26-b5cc-4857-af86-3cdfb7039bea"
session_id: "BRK316"
session_type: "Breakout"
start: "2026-11-18T19:30:00Z"
level: "(400) Expert"
ignite_topics: ["Security", "Security", "Azure Cosmos DB", "AI Security", "Agents", "Defend with AI", "Data protection", "Defend with agents"]
topics: ["security", "autonomous-protection", "exposure", "threat-response"]
categories: ["Microsoft Defender", "Security operations"]
---

# Winning the Race Against Time with Autonomous Protection

**Speaker(s):** Noam Hadash, Raviv Tamir, Ken Robb

## Summary

The session introduces Defender vulnerability shielding (preview): targeted, temporary protection on vulnerable systems until a patch lands, chosen by AI to be the narrowest control that keeps the business running. It is motivated by attacker speed (the slides cite 3.6x more CVEs reported in 2026 than in 2021 and shrinking time to exploit) and slow patching.

Shielding runs in two modes: attack disruption (on by default, shielding vulnerabilities in an attacker's path and retiring once the attacker is removed) and a Risk Reduction Agent that investigates each vulnerability and recommends a plan you approve, with shields retiring automatically after patching. The slides state about 70% of distinct high-severity CVEs seen in the last 30 days were shield-able (third-party apps, OS and open source). It is enabled by signals and context plus actuators (reducing network reachability, restricting access paths, tightening permissions) and is not a replacement for patching.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856621042001EDGy-1791588155309001C8PS
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/f65dde26-b5cc-4857-af86-3cdfb7039bea
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/f65dde26-b5cc-4857-af86-3cdfb7039bea
- Microsoft Perception Site: https://aka.ms/PerceptionWeb
- Microsoft Perception Blog: https://aka.ms/PerceptionBlog
- Vulnerability Shielding Blog: https://aka.ms/vulnerabilityshielding
- Microsoft Defender Ignite Blog: https://aka.ms/Defender_Ignite26
- Vulnerability Shielding Sizzle Video: https://aka.ms/vulnerabilityshielding-sizzle
