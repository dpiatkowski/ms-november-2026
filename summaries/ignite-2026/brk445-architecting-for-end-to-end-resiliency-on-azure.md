---
event: "Microsoft Ignite 2026"
title: "Architecting for end-to-end resiliency on Azure"
speaker: "Yuemin Lu, Sudha Mahajan, Rochak Mittal"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856640975001Eumd-1791588234558001Co4y"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/0c4b089c-03f4-477b-99f2-f1401adf3f35"
session_id: "BRK445"
session_type: "Breakout"
start: "2026-11-19T19:30:00Z"
level: "(300) Advanced"
ignite_topics: ["Cloud & AI"]
topics: ["resilience", "azure", "disaster-recovery", "architecture", "dependencies"]
categories: ["Operations and reliability"]
---

# Architecting for end-to-end resiliency on Azure

**Speaker(s):** Yuemin Lu, Sudha Mahajan, Rochak Mittal

## Summary

The session covers architecting for end-to-end resiliency on Azure as a shared responsibility: Microsoft provides a resilient platform (failure isolation, safe updates, clear incident communication), customers choose resilient architecture (independent failure domains, SKUs, recovery goals), and together they prove outcomes against RTO and RPO. The slides acknowledge two Azure incidents (September 30 and October 30, 2026: ExpressRoute disruption from an update surge, and emergency patching that bypassed maintenance windows) and commit to safer change, reliable recovery and timely communication.

Customer lessons from past incidents (a Front Door disruption, a Chicago ExpressRoute peering-site problem) are independent ingress with tested DNS cutover and diverse network paths. Design guidance for day 0 includes distributing resources across availability zones, keeping dependent resources in the same zone and using zone-spanning VM scale sets.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856640975001Eumd-1791588234558001Co4y
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/0c4b089c-03f4-477b-99f2-f1401adf3f35
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/0c4b089c-03f4-477b-99f2-f1401adf3f35
