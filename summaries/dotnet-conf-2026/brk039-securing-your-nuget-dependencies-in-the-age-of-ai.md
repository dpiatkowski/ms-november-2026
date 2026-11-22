---
event: ".NET Conf 2026"
title: "Securing Your NuGet Dependencies in the Age of AI"
speaker: "Jon Douglas"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk039"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/H54iAyM08VM"
session_id: "BRK039"
start: "2026-11-10T18:00:00-08:00"
topics: ["nuget", "supply-chain", "security", "ai", "agents"]
---

# Securing Your NuGet Dependencies in the Age of AI

**Speaker(s):** Jon Douglas

## Summary

Jon Douglas lays out how NuGet is hardening the supply chain, for developers and for their AI agents: client-side protections, nuget.org publishing controls, and agent-focused features (Secure My Supply Chain MCP tool, skills shipped in packages).

## Key points

- Client: package 'cooldown' keeps freshly published versions out of add/update (e.g. a 3-day property; skipped a 6-hour-old version in the example), planned for .NET 11.2 CLI and VS 18.14 (property name TBD); Visual Studio 18.14 no longer auto-runs init.ps1/install.ps1 scripts; staged publishing from the CLI (push a group, check status, publish and list at once; flags TBD); a warning for non-ASCII look-alike package IDs (e.g. Cyrillic 'e') in .NET 12 Preview 1.
- nuget.org: Trusted Publishing from CI with no long-lived API key (41% of monthly publishes today, target 70%; GitHub Actions and GitLab available, Azure DevOps coming); new API keys last 30 days or less and from Nov 1 existing longer keys expire, so move CI off long-lived keys before then; staged publishing with malware scanning and proof of presence before packages go live; faster takedown of confirmed-malicious packages.
- AI agents: 'Secure My Supply Chain' NuGet MCP tool in Visual Studio (Installed tab, Package Sources settings, Error List) — slides claim up to 88% less time and 67% fewer AI credits than model-led research; .NET 11 lets packages ship a SKILL.md that teaches agents how to use them.
- In design: package end-of-life status, NuGet Signing v2 (detached signatures), 'updates available' notices in CLIs, better third-party vulnerability reporting. Do this week: turn on cooldown and move publishing to Trusted Publishing.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk039
- Recording: https://youtu.be/H54iAyM08VM
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK039/DotNetConf-2026-NuGet.pptx
