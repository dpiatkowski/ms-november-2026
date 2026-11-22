---
event: ".NET Conf 2026"
title: "Protect your PC from AI coding agents while modernising legacy .NET apps"
speaker: "Justin Yoo"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk035"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/OoALkRag2tY"
session_id: "BRK035"
start: "2026-11-11T18:30:00-08:00"
topics: ["agents", "sandboxing", "security", "modernization", "devcontainers"]
categories: ["Web development", "AI-assisted development", "Application and agent security", "Migration and modernization"]
---

# Protect your PC from AI coding agents while modernising legacy .NET apps

**Speaker(s):** Justin Yoo

## Summary

Justin Yoo argues that approving agent actions is not the same as isolating them ('copilot --allow-all' hands over files, network and credentials), and demonstrates three execution boundaries for running a coding agent while modernising a legacy app (ContosoUniversity, ASP.NET MVC 5 on .NET Framework 4.8). The three things to protect are the host PC, the authority (credentials) and the repo, starting from a sanitized clone.

## Key points

- Local sandbox: the CLI stays on the host and enforcement depends on the tool (policy checks for built-in file tools); inspect /sandbox policy, test inside and outside file writes, and grant per task rather than the whole machine; a real denial is information, not something to solve with a blanket grant.
- Docker Sandboxes: move the agent into a microVM (sbx run --clone); clone mode changes when edits reach the host, not what the repo can reveal; fetch then review changes.
- Azure Container Apps (Azure sandboxes): move execution off your PC to a Linux microVM, still with explicit authority and network controls; the three are different places the same agent runs, not a safety ranking.
- Choose by task constraints (e.g. keep Windows tooling local); a hybrid is a recommendation, not a measured result. Mantra: constrain, observe, review.

## From linked resources

- Azure Container Apps Sandboxes are now generally available per the docs: isolated microVMs with their own kernel, built-in egress proxy with deny policies, host allowlists and credential injection, sub-second start, suspend/resume with memory and disk snapshots, bring-your-own container images, programmable from CLI, Python SDK or REST, with stopped sandboxes incurring no compute charges.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk035
- Recording: https://youtu.be/OoALkRag2tY
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK035/sandboxing-app-modernisation.pdf
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK035/sandboxing-app-modernisation.pptx
- GitHub Copilot Sandbox: https://gh.io/sandboxes
- Docker Sandboxes: https://docs.docker.com/ai/sandboxes/
- Azure Container Apps Sandboxes: https://sandboxes.azure.com
