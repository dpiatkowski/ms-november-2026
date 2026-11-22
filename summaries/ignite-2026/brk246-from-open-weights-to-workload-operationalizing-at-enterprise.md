---
event: "Microsoft Ignite 2026"
title: "From open weights to workload: Operationalizing at enterprise scale"
speaker: "Manoj Bableshwar, Gulsimo Osimi, Miguel Armenta, Pavan Tagirisa"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856610499001EA0J-1791588200189001CaK0"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/aec447c9-a65b-42c9-a4ae-ddca25246a38"
session_id: "BRK246"
session_type: "Breakout"
start: "2026-11-18T21:45:00Z"
level: "(200) Intermediate"
ignite_topics: ["Agent Platform", "Microsoft Foundry", "Customer"]
topics: ["foundry", "open-weight-models", "managed-compute", "gpu", "customer-story"]
---

# From open weights to workload: Operationalizing at enterprise scale

**Speaker(s):** Manoj Bableshwar, Gulsimo Osimi, Miguel Armenta, Pavan Tagirisa

## Summary

The session explains how to run open and custom models in Microsoft Foundry without operating the serving stack. It cites the rise of open models in production traffic (open-router market-share data) and how agentic workloads change inference: longer prompts (about 1.5K to over 6K tokens on average), more reasoning-model traffic, and tool and state requirements.

Foundry Models offers 11,000+ models and several deployment economics (batch at 50% off, flex, standard, priority at a 75% premium, provisioned and managed compute). Managed Compute is presented as GPU platform-as-a-service: pick a model, a template (context length and serving shape), an accelerator (A100, H100, H200 or MI300X) and replicas, and Foundry resolves GPU topology, runtime and routing, replacing days or weeks of DIY deployment. A secure publishing pipeline checks models and runtimes for supply-chain risk, and supported architectures can be available from Hugging Face on day 0.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856610499001EA0J-1791588200189001CaK0
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/aec447c9-a65b-42c9-a4ae-ddca25246a38
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/aec447c9-a65b-42c9-a4ae-ddca25246a38
