---
event: ".NET Conf 2026"
title: "What's New in Aspire for .NET Developers"
speaker: "Maddy Montaquila, Damian Edwards"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk009"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/wVq9fIXsVWE"
session_id: "BRK009"
start: "2026-11-10T13:00:00-08:00"
topics: ["aspire", "dotnet-11", "cloud-native", "polyglot", "developer-experience"]
categories: ["Aspire"]
---

# What's New in Aspire for .NET Developers

**Speaker(s):** Maddy Montaquila, Damian Edwards

## Summary

Damian Edwards and Maddy Montaquila review a year of Aspire for .NET developers and preview Aspire 17, shipping the following week. Aspire is positioned as one code-first model to compose, run (aspire run), and observe (dashboard) an entire app, increasingly driven through the CLI by coding agents. Slides cite roughly 90k monthly engaged developers in Nov 2026 vs about 50k a year earlier, with the Aspire CLI (including coding agents) adding about 40k.

## Key points

- Shipped for .NET devs this year: file-based C# apps and AppHosts (a single .cs file), CLI bundle so the dashboard and DCP come from the CLI install, Blazor WebAssembly hosting with gateway (preview), EF Core migration management in the dashboard (preview), HTTPS certificate configuration for resources.
- Other big changes: much richer CLI (detached runs, ps/start/stop, logs, OpenTelemetry queries, diagnostics, secrets, docs lookup), isolated runs for parallel development, persistent dashboard telemetry and run history, Native AOT dashboard, interactive terminals/database REPLs and browser observability (preview), and an improved VS Code experience (one F5 for the whole app).
- Aspire 17: Aspire.Hosting.Dotnet goes stable with 'Project Resource v2' (AddProject and AddCSharpApp deprecated, not removed), AppHosts use plain Microsoft.NET.Sdk so upgrading is a package bump, path-based resources so the dashboard starts without the MSBuild graph, a NuGet overhaul, and attach-debugging of running .NET resources in VS Code. Possible extras: launch groups/tags, an experimental dashboard redesign, Git-backed team config and templates.
- Top five hosting integrations by usage: JavaScript, SQL Server, Redis, PostgreSQL, Azure Storage.

## From linked resources

- Aspire 13.6 (released Sept 29, 2026) per the release notes: persistent dashboard storing snapshots and telemetry in SQLite with up to ten revisitable completed runs, docked AppHost-owned terminals, the Native AOT dashboard with Fluent UI v5, first-party Java and Rust hosting, preview Azure Connector Namespace support and experimental Azure Container Apps Sandboxes as a deployment target, coordinated .NET builds, portable volume paths, TypeScript AppHost config from appsettings.json, a VS Code extension that agents can drive, and database/cache REPLs. Upgrade with aspire update --self then aspire update.
- The agent docs describe 'aspire agent init' to set up Aspire skills/plugins (microsoft/aspire-skills) for Copilot, Claude Code and OpenCode, with an optional MCP server; agent-friendly CLI commands include aspire start (--isolated for parallel worktrees), aspire wait, aspire describe, aspire logs and aspire docs search.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk009
- Recording: https://youtu.be/wVq9fIXsVWE
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK009/DotNetConf-2026-AspireForDotNetDevs.pptx
- AspiriFridays Bingo source code: https://github.com/maddymontaquila/aspirifridays
- Install the Aspire CLI: https://aspire.dev/get-started/install-cli/
- Build your first Aspire app: https://aspire.dev/get-started/first-app/
- Explore what's new in Aspire 13.6: https://aspire.dev/whats-new/aspire-13-6/
- Read the Aspire documentation: https://aspire.dev/docs/
- Explore the source and share feedback on GitHub: https://github.com/microsoft/aspire
- Join the Aspire community: https://aspire.dev/community/
- Chat with the Aspire community on Discord: https://aka.ms/aspire-discord
