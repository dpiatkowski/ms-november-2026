---
event: ".NET Conf 2026"
title: "AI Journey with Telerik UI for Blazor: From Developer Productivity to Intelligent User Experiences"
speaker: "Maya Mateva"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk101"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/q3R0Jpv42ag"
session_id: "BRK101"
start: "2026-11-12T08:30:00-08:00"
topics: ["blazor", "ai", "mcp", "ui-components", "community-day", "vendor"]
categories: ["Web development", "AI apps and agents", "AI-assisted development"]
---

# AI Journey with Telerik UI for Blazor: From Developer Productivity to Intelligent User Experiences

**Speaker(s):** Maya Mateva

## Summary

Maya Mateva (Progress) presents an AI journey with Telerik UI for Blazor in two acts: AI for the developer experience and AI for the end-user experience, with human ownership remaining.

## Key points

- Developer side: a better prompt isn't enough; agents need project context, framework knowledge (correct Telerik APIs), design context and task capabilities, delivered through a Telerik Blazor MCP server and plugin (e.g. generating pages, custom themes, upgrades).
- User side: let users ask instead of click (e.g. filter a grid by asking); WebMCP exposes UI actions as tools, with a free Blazor.WebMcpKit NuGet package (WebMcpComponentBase, [WebMcpTool]) to expose tools from your own components.
- Generative UI: DataInsights Composer lets users generate charts and data views from approved datasets while developers control access and governance; interactive responses (A2UI) beat a wall of text. Slides map which layer (MCP, WebMCP, A2UI, Microsoft Agent Framework, AI components) solves which problem.

## From linked resources

- Telerik docs: WebMCP is an experimental browser standard available behind a feature flag in some Chromium browsers, and the Telerik integration is a preview; components register operations (sort, filter, navigate, set values) as tools an agent can call, so 'show only orders from last month' filters the Grid. The Agentic UI Generator is the development-time counterpart: the Telerik Blazor MCP server (via CLI, AI plugin or manual configuration) generates pages and components and aligns with the Progress Design System; don't configure the plugin and the MCP server together.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk101
- Recording: https://youtu.be/q3R0Jpv42ag
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD102/TelerikUIBlazor_DotNetConf_2026.pdf
- Telerik MCP/Agentic UI Generator: https://www.telerik.com/blazor-ui/documentation/ai/agentic-ui-generator/overview
- Telerik WebMcpKit: https://www.telerik.com/blazor-ui/documentation/ai/web-mcp/overview
- Blazor.WebMcpKit on NuGet: https://www.nuget.org/packages/Blazor.WebMcpKit/1.0.0-preview.1
- Telerik WebMCP Extension: https://demos.telerik.com/blazor-ui/marketing-campaigns/webmcp-operations-hub
- Telerik DatAInsights Composer: https://www.telerik.com/datainsights-composer
- A2UI, AGUI, MAF Integration, Telerik UI for Blazor: https://demos.telerik.com/blazor-ui/a2ui/ai-a2ui
- Progress: https://www.telerik.com/contact
