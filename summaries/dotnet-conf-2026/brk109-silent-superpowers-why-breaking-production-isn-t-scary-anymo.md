---
event: ".NET Conf 2026"
title: "Silent Superpowers: Why Breaking Production Isn't Scary Anymore"
speaker: "André Silva"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk109"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/u_4fVzO7ESg"
session_id: "BRK109"
start: "2026-11-12T12:30:00-08:00"
topics: ["feature-flags", "deployment", "progressive-delivery", "devops", "community-day"]
---

# Silent Superpowers: Why Breaking Production Isn't Scary Anymore

**Speaker(s):** André Silva

## Summary

André Silva (OpenFeature maintainer) introduces feature flags and OpenFeature through a maturity model, arguing that decoupling release from deployment makes breaking production less scary, including in the age of AI agents.

## Key points

- Maturity model: level 0 environment-variable flags (redeploy to change, no context or telemetry); level 1 dynamic configuration (change without deploy, but evaluation logic is copied into each service); level 2 dynamic evaluation (provider evaluates with context, rules live in one place, experiments without code changes, traces and metrics show which variant was served and why); level 3 operationalised flags (open to product, marketing and support with guardrails, drive experiments, canary and percentage rollouts).
- Flags work with agents: agents ship dark behind flags and humans decide when to go live. The linked sample is askpt/openfeature-aspire-sample.

## From linked resources

- The sample (askpt/openfeature-aspire-sample) is a Le Mans winners app in .NET, Python, Go and React on Aspire, using OpenFeature with the OFREP remote evaluation protocol and flagd, with kill switches, real-time flag updates and an AI chatbot (Phi-4-mini via Foundry Local in development) whose prompts are chosen by flags.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk109
- Recording: https://youtu.be/u_4fVzO7ESg
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD110/CD110.pdf
- OpenFeature Aspire Demo: https://github.com/askpt/openfeature-aspire-sample
