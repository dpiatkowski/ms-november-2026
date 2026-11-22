---
event: ".NET Conf 2026"
title: "Test Smarter: AI-Assisted Testing for Modern .NET"
speaker: "McKenna Barlow"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk038"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/fKnZotxlEec"
session_id: "BRK038"
start: "2026-11-11T18:00:00-08:00"
topics: ["testing", "ai", "mstest", "microsoft-testing-platform", "copilot"]
categories: ["GitHub Copilot", "Agentic engineering", "Testing"]
---

# Test Smarter: AI-Assisted Testing for Modern .NET

**Speaker(s):** McKenna Barlow

## Summary

McKenna Barlow's session on AI-assisted testing for .NET: AI makes it easier to work in unfamiliar code, delegate larger changes and generate tests, but a green result is evidence, not a verdict (it doesn't show the right behavior was checked, important cases were included, or that tests would catch regressions).

## Key points

- Tooling: Visual Studio Test Explorer and VS Code with C# Dev Kit for discovering, running and debugging tests; the command line and CI for everything else.
- AI help: the Test Agent (GitHub Copilot testing for .NET) generates tests, builds and runs them and iterates on results; dotnet/skills provides focused testing guidance for compatible coding agents, including examining test quality.
- Foundation: MSTest (attributes, assertions, analyzers, code fixes) and Microsoft.Testing.Platform (MTP), where the test project is an app you can run and debug directly; MTP supports coverage, crash/hang diagnostics, extensions, hot reload for supported edits and rerunning. The demo shows MTP hot reload, Test Agent generation and test quality review.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk038
- Recording: https://youtu.be/fKnZotxlEec
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK038/test-smarter-ai-powered-testing-for-dotnet.pptx
