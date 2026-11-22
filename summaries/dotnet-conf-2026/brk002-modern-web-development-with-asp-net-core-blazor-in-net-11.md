---
event: ".NET Conf 2026"
title: "Modern web development with ASP.NET Core & Blazor in .NET 11"
speaker: "Daniel Roth"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk002"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/19L2hdUs3_s"
session_id: "BRK002"
start: "2026-11-10T09:30:00-08:00"
topics: ["aspnet-core", "blazor", "dotnet-11", "minimal-apis", "signalr", "aspire", "agentic-ui", "observability"]
categories: ["ASP.NET Core", "Blazor", ".NET"]
---

# Modern web development with ASP.NET Core & Blazor in .NET 11

**Speaker(s):** Daniel Roth

## Summary

Daniel Roth frames ASP.NET Core and Blazor in .NET 11 as a platform you can trust to perform, protect and help teams deliver, backed by Microsoft-scale production workloads (e.g. an MSN feeds team reported 29% lower P95 GC pauses and 20% shorter thread-pool queues going from .NET 8 to .NET 10). The talk is demo-driven around an eShop customer-service sample app.

## Key points

- Performance: runtime async in framework libraries (app opt-in), JIT and allocation work, earlier HTTP/3 processing, and cheaper bad-request handling in Kestrel (parser returns an error result instead of throwing; roughly 30% higher bad-request throughput in a single-core benchmark).
- Security: automatic CSRF protection based on browser Fetch Metadata (Sec-Fetch-Site, Origin fallback) instead of antiforgery tokens, enabled by default; slides cite about 4x form-post requests/sec and about 65% less allocation per request versus token validation.
- SignalR authentication refresh lets a long-lived connection reauthenticate with fresh short-lived credentials without reconnecting (EnableAuthenticationRefresh / CloseOnAuthenticationExpiration on the hub, opt-in in the JS client, default in the .NET client). Blazor Server uses it so permission changes apply while unsaved work is preserved.
- Also covered: consistent authorization metadata across MVC/SignalR/Blazor, supported TLS channel binding, better CSP compatibility in Blazor templates; for Blazor smaller WebAssembly downloads, caching for static SSR and pausing idle server circuits.

## From linked resources

- The eShopCustomerService sample (.NET 11, Aspire CLI 13.6) is a fictional returns and customer-care scenario with local SQLite; non-AI flows need no containers or cloud, and the agent is enabled by configuring a Microsoft Foundry endpoint and model (the app starts with aspire start).

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk002
- Recording: https://youtu.be/19L2hdUs3_s
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK002/Modern%20web%20development%20with%20ASP.NET%20Core%20%26%20Blazor%20in%20.NET%2011.pptx
- eShop Customer Service sample code: https://github.com/danroth27/eShopCustomerService
- eShop device support sample code: https://github.com/danroth27/eShopDeviceSupport
