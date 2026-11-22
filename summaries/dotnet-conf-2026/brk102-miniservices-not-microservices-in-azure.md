---
event: ".NET Conf 2026"
title: "Miniservices not Microservices in Azure"
speaker: "Shawn Wildermuth"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk102"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/9UbzM5WbZkk"
session_id: "BRK102"
start: "2026-11-12T09:00:00-08:00"
topics: ["architecture", "azure", "microservices", "app-service", "azure-functions", "service-bus", "community-day"]
categories: ["Cloud infrastructure", "Application architecture"]
---

# Miniservices not Microservices in Azure

**Speaker(s):** Shawn Wildermuth

## Summary

Shawn Wildermuth argues for 'miniservices': small and mid-sized teams should match the platform to the team, not the trend, composing Azure PaaS services (App Service, Entra, App Configuration, Key Vault, hosted databases, Redis, managed identity) rather than defaulting to microservices on Kubernetes. Microservices and modular monoliths are fine when you have the size, budget and skills.

## Key points

- Azure options sit on a control-versus-operational-burden spectrum: App Service/Functions (lowest burden, Azure-specific), Azure Container Apps (managed platform with KEDA, Dapr, Envoy; portable containers; scales to zero), Container Instances (short jobs and bursts), AKS (managed control plane but you own nodes, networking, upgrades; most portable; requires a platform/SRE team).
- The composed PaaS approach wins for small and mid-sized teams without platform engineers, standard web/API workloads with a database and cache, faster time to production (patching, TLS and scaling handled for you), low or variable load cost and lower risk.
- Takeaways: start with the highest-level service that meets your needs and move down the stack only for a concrete reason.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk102
- Recording: https://youtu.be/9UbzM5WbZkk
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD103/mini-services-dotnetconf.pdf
- Slides: https://github.com/dotnetConf/2026/blob/3a6379141780d31d89a52d4fdf34d05b4eccec88/Technical/CommunityDays/CD103/mini-services-dotnetconf.pdf
- here: http://wildermuth.com/#contact
- https://wildermuth.com
