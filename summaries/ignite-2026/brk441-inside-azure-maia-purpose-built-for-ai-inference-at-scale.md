---
event: "Microsoft Ignite 2026"
title: "Inside Azure Maia: Purpose-built for AI inference at scale"
speaker: "Vikram Vemulapalli, Andrew Wall"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856640352001EpXn-1791588117452001CP9h"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/29479dec-c531-4dae-a112-74a383c37766"
session_id: "BRK441"
session_type: "Breakout"
start: "2026-11-18T00:30:00Z"
level: "(300) Advanced"
ignite_topics: ["Cloud & AI"]
topics: ["azure-maia", "ai-inference", "custom-silicon", "co-design"]
categories: ["Cloud infrastructure"]
---

# Inside Azure Maia: Purpose-built for AI inference at scale

**Speaker(s):** Vikram Vemulapalli, Andrew Wall

## Summary

The session goes inside Azure Maia, Microsoft's inference-first AI accelerator system. It argues token demand (agentic coding uses far more tokens per task than chat) breaks current math, so infrastructure is diversifying toward specialized accelerators. Maia 200 is described as production-proven and outperforming existing GPUs in the fleet, and Maia 300 as advancing the efficiency frontier with up to 7x generation-over-generation inference performance and 40% more tokens per megawatt, scaling to multi-gigawatt deployments from 2027 (Microsoft-reported).

Specs shown for Maia 300 versus Maia 200 include a multi-chiplet N2P process, 8 HBM4 stacks, 18 TB/s HBM bandwidth, 288 GB HBM and 3.2 TB/s scale-up bandwidth with Ethernet-based AI transport, at 950 W TDP, with rack-scale systems of 96-accelerator pods, liquid and air cooling and a software stack (SDK, compiler, kernel library, PyTorch integration). Building racks and software emulation before final silicon is also covered.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856640352001EpXn-1791588117452001CP9h
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/29479dec-c531-4dae-a112-74a383c37766
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/29479dec-c531-4dae-a112-74a383c37766
