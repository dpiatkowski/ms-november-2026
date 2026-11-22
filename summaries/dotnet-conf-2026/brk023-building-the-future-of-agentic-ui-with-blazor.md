---
event: ".NET Conf 2026"
title: "Building the future of agentic UI with Blazor"
speaker: "Daniel Roth"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk023"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/KTq7jpv2Eik"
session_id: "BRK023"
start: "2026-11-11T12:00:00-08:00"
topics: ["blazor", "agentic-ui", "ag-ui", "agent-framework", "foundry", "aspire", "human-in-the-loop"]
---

# Building the future of agentic UI with Blazor

**Speaker(s):** Daniel Roth

## Summary

Daniel Roth shows how to make an existing Blazor app agentic without losing its rich UI: users get direct UI plus goal-based collaboration with an agent, demonstrated in the eShop service-desk sample (investigate a delayed delivery, shape a resolution together, approve an action).

## Key points

- AG-UI (agent-to-application-UI protocol: text, tool activity, shared state, human decisions) complements MCP (agent to tools and context). There is an official open-source AG-UI SDK for .NET (AGUI.Client consumes endpoints as IChatClient; AGUI.Server exposes an IChatClient as AG-UI) with first-class Microsoft Agent Framework integration.
- Blazor AI components (experimental, built on IChatClient): ChatPage for a ready-made chat, BlockRenderer<TBlock> to customize rich content such as tools and approvals; backend tools configured on the agent and frontend tools exposed by the Blazor app (UIAgent<TState>).
- Shared workspace: current app state goes out with each request and tool-result snapshots come back in the response stream (no multi-browser sync); edits can be previewed provisionally and accepted or discarded.
- Human in the loop: pause a tool call, show details, resume with the user's decision. Getting started: aka.ms/blazor/ai-components.

## From linked resources

- The eShopCustomerService sample (.NET 11, Aspire CLI 13.6) is a fictional returns and customer-care scenario with local SQLite; non-AI flows need no containers or cloud, and the agent is enabled by configuring a Microsoft Foundry endpoint and model (the app starts with aspire start).

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk023
- Recording: https://youtu.be/KTq7jpv2Eik
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK023/Building%20the%20future%20of%20agentic%20UI%20with%20Blazor.pptx
- eShop Customer Service sample code: https://github.com/danroth27/eShopCustomerService
