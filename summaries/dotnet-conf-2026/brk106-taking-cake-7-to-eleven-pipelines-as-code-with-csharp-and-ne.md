---
event: ".NET Conf 2026"
title: "Taking Cake 7 to Eleven: Pipelines as Code with C# and .NET 11"
speaker: "Mattias Karlsson"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk106"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/uszy8DGurcs"
session_id: "BRK106"
start: "2026-11-12T11:00:00-08:00"
topics: ["cake", "ci-cd", "pipelines", "csharp", "devops", "dotnet-11", "community-day"]
categories: ["Developer tools and delivery"]
---

# Taking Cake 7 to Eleven: Pipelines as Code with C# and .NET 11

**Speaker(s):** Mattias Karlsson

## Summary

Mattias Karlsson shows Cake 7 on .NET 11 as a way to write CI/CD pipelines in C# instead of vendor YAML, using Cake.Sdk file-based apps (a single cake.cs with '#:sdk Cake.Sdk@7.0.0') that run identically locally, in containers and on GitHub Actions, Azure Pipelines and GitLab CI. Cake is a 12-year-old open-source build orchestration framework (tasks and dependencies, aliases, addins, modules, tool acquisition).

## Key points

- Pipeline as code: Restore/Build/Test/Pack/Publish tasks map one-to-one from YAML steps to C# tasks; debug locally in VS Code (cake.cs) or Visual Studio (cake.csproj, since VS doesn't yet support file-based programs); run via dotnet cake.cs, or ./cake.cs with a shebang on Unix.
- Build anywhere: build and publish a container image from the cake file (archive, registry or local registry), run it as a GitHub Actions step; new Cake.Template 'cakeci' templates for GitHub, Azure DevOps and GitLab.
- Structure and reuse: multi-file builds with the new .NET 11 '#:include' directive, testable build logic (records, typed configuration), preprocessor directives (#:sdk, #:property, #:package, #:project, #:include).
- Since last year: Cake 6.1-6.3 (formattable logging, InstallTool for any NuGet package, RWX provider, NuGet trusted publishing, OIDC to Azure without secrets). Cake 7: targets net11.0/C# 15, drops .NET 8 and 9, unified dependency graph and DI across Tool, Frosting and Sdk, DSL improvements, new aliases and .NET 11 process APIs.

## From linked resources

- The sample repo (azurevoodoo/dotnetconf2026) holds a complete clean/restore/build/test/pack/publish pipeline as one cake.cs that runs unchanged locally and on GitHub Actions, Azure Pipelines, AppVeyor, Bitbucket Pipelines and RWX; with no --target it detects the CI provider and picks the matching target so the CI YAML stays minimal, and the default package version is UTC date-based.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk106
- Recording: https://youtu.be/uszy8DGurcs
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD107/TakingCake7toEleven.pptx
- azurevoodoo/dotnetconf2026: https://github.com/azurevoodoo/dotnetconf2026
- https://dotnetconf2026.azurevoodoo.net/
- https://cakebuild.net/
