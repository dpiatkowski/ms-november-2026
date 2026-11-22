---
event: "Microsoft Ignite 2026"
title: "Secure the CI pipeline: Practical defenses for GitHub Actions"
speaker: "Steve Glass, Jeff Martin"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856616477001EQQz-1791588353428001C9Vo"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/4ba88e4f-5c6c-4e41-bda9-5f9891326739"
session_id: "BRK286"
session_type: "Breakout"
start: "2026-11-20T01:15:00Z"
level: "(300) Advanced"
ignite_topics: ["Agent Platform", "Security", "GitHub", "Developer Tools"]
topics: ["github-actions", "ci-security", "supply-chain", "hardening"]
---

# Secure the CI pipeline: Practical defenses for GitHub Actions

**Speaker(s):** Steve Glass, Jeff Martin

## Summary

The session explains practical defenses for GitHub Actions using an example of two repositories and three workflows, walking five attack stages across three trust boundaries: pull request to workflow, shared state to trusted workflow, and released Action to consumers. Stages shown: a "pwn request" where pull_request_target checks out fork code, cache poisoning that escalates into a privileged release workflow, mutable release tags such as @v3 delivering new code to consumers, and further stages.

For each stage it shows the new default or control that breaks it, including safer checkout that refuses fork-head code in pull_request_target workflows, a read-only cache default and a cache mode setting (none or read) for privileged workflows. It also covers agents in CI inheriting Actions protections, running in your Azure network, and what is free, what ships and what depends on your plan.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856616477001EQQz-1791588353428001C9Vo
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/4ba88e4f-5c6c-4e41-bda9-5f9891326739
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/4ba88e4f-5c6c-4e41-bda9-5f9891326739
