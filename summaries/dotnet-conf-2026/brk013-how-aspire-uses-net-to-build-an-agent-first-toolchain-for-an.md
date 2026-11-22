---
event: ".NET Conf 2026"
title: "How Aspire uses .NET to build an agent-first toolchain for any programming language"
speaker: "Maddy Montaquila, Jose Perez Rodriguez"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk013"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/tT-rgopqhsU"
session_id: "BRK013"
start: "2026-11-10T15:00:00-08:00"
topics: ["aspire", "agents", "native-aot", "blazor", "polyglot", "developer-tools"]
categories: ["Application architecture", "Web development"]
---

# How Aspire uses .NET to build an agent-first toolchain for any programming language

**Speaker(s):** Maddy Montaquila, Jose Perez Rodriguez

## Summary

Maddy Montaquila and Jose Perez Rodriguez show how Aspire uses .NET in three ways: as a polyglot host (author a C# API once and generate idiomatic SDKs for other AppHost languages), as a real-time application platform (the Blazor-based dashboard), and as a native toolchain (Native AOT so users don't need .NET installed).

## Key points

- Polyglot AppHosts: transpiling builder calls to C# worked until callbacks, so Aspire defines an Aspire Type System (ATS) contract from C# declarations (via Roslyn and the .NET runtime), generates guest-language SDKs (e.g. TypeScript: Task becomes Promise, callbacks stay callbacks, .NET objects stay in .NET behind handles), and dispatches calls by capability ID over JSON-RPC with a build-time-generated dispatch table. Integrations are written once in C#. Overloads collapse to one method per language; Go AppHosts are in preview in Aspire 17, with Python, Java and Rust behind feature flags.
- Dashboard: Blazor Server avoids a REST/DTO/client-model stack and API drift, built on Fluent UI Blazor v5 with Aspire branding. Via a custom Blazor build done with the Blazor team, it compiles with Native AOT: slides claim 3x faster and 40% smaller (startup 1,429 to 491 ms).
- Native toolchain: the CLI was already AOT but launched an 'aspire-managed' bundle on a JIT'd bundled runtime; pieces (dashboard, terminal host, AppHost server JSON-RPC) moved to AOT one by one, each waiting on its own dependencies. NuGet operations, integration loading and SDK generation are still managed; DCP is written in Go.
- Takeaway: Aspire is a .NET customer for compiler infrastructure (cross-language contracts), an application framework (live UI) and native compilation (distribution).

## From linked resources

- The Aspire team's dashboard blog post says Native AOT cut median page-visible startup time by 66% and removes the dashboard executable's dependency on an installed .NET runtime (enabling a slimmer container base). Previously the dashboard targeted .NET 8 and rolled forward, which caused bugs; getting to AOT took changes in the dashboard, Blazor, Fluent UI and Dapper.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk013
- Recording: https://youtu.be/tT-rgopqhsU
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK013/DotNetConf-2026-HowAspireUsesDotNet.pptx
- Aspire source code: https://github.com/microsoft/aspire
- Aspire Dashboard Native AOT: implementation and performance: https://devblogs.microsoft.com/aspire/aspire-dashboard-native-aot/
- Aspire Dashboard documentation: https://aspire.dev/dashboard/
- Install the Aspire CLI: https://aspire.dev/get-started/install-cli/
- Build your first Aspire app: https://aspire.dev/get-started/first-app/
- Set up Aspire for your coding agent: https://aspire.dev/get-started/ai-coding-agents/
- Read the Aspire documentation: https://aspire.dev/docs/
- Share feedback on GitHub: https://github.com/microsoft/aspire/issues
- Join the Aspire community: https://aspire.dev/community/
- Chat with the Aspire community on Discord: https://aka.ms/aspire-discord
