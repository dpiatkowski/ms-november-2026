---
event: ".NET Conf 2026"
title: "Blazor Server in .NET 11: Fast, resilient, and scalable"
speaker: "Daniel Roth"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk036"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/FyQGh9uFMW0"
session_id: "BRK036"
start: "2026-11-11T10:30:00-08:00"
topics: ["blazor", "aspnet-core", "dotnet-11", "ssr", "scalability", "state-management"]
categories: ["Web development", "Performance"]
---

# Blazor Server in .NET 11: Fast, resilient, and scalable

**Speaker(s):** Daniel Roth

## Summary

Daniel Roth covers Blazor Server and server rendering in .NET 11 under three headings, fast, resilient and scalable, with demos in the eShop customer-service app.

## Key points

- Static SSR is more capable: smooth navigation, QuickGrid sort/page links, client-side validation and state across requests, so useful pages need no circuit. Interactive SSR prerenders HTML first and [PersistentState] reuses the prerendered data so it's loaded once, not twice.
- Resilient: a disconnected circuit stays for reconnection; after a while Blazor persists selected state before evicting the circuit and restores it into a new circuit on reconnect. New in .NET 11: circuit.RequestCircuitPauseAsync (via CircuitHandler) to pause circuits during planned interruptions, enabling graceful deployments (drain, pause, replace the server process, resume) without losing drafts.
- Scalable: Auto Pause (Microsoft.AspNetCore.Components.Server.AutoPause package, opt-in with a policy) releases eligible circuits when a browser tab is hidden, freeing server resources for active users, then resumes the workspace when the user returns.

## From linked resources

- The eShopCustomerService sample (.NET 11, Aspire CLI 13.6) is a fictional returns and customer-care scenario with local SQLite; non-AI flows need no containers or cloud, and the agent is enabled by configuring a Microsoft Foundry endpoint and model (the app starts with aspire start).

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk036
- Recording: https://youtu.be/FyQGh9uFMW0
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK036/Blazor%20Server%20in%20.NET%2011%20-%20Fast%2C%20resilient%2C%20and%20scalable.pptx
- eShop Customer Service sample code: https://github.com/danroth27/eShopCustomerService
