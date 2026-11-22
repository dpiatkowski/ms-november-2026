---
event: ".NET Conf 2026"
title: "Beyond Localhost: .NET Agents in Foundry"
speaker: "Bruno Capuano"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk031"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/Dq8fcig5-Gk"
session_id: "BRK031"
start: "2026-11-11T17:00:00-08:00"
topics: ["foundry", "agents", "hosted-agents", "azure", "dotnet-ai"]
categories: ["Azure", "AI applications"]
---

# Beyond Localhost: .NET Agents in Foundry

**Speaker(s):** Bruno Capuano

## Summary

Bruno Capuano takes one small .NET agent from 'dotnet run' on a laptop to a Foundry hosted agent in five demos, with the point that hosting changes where an agent runs, not its code, and that hosting equals a protocol plus an identity.

## Key points

- Demo 01-02: a minimal console agent with Microsoft Agent Framework and a Foundry chat model, then the same agent with hosting registrations so it answers requests like a service locally.
- Foundry Hosted Agents: managed hosting with the platform running it, scale to zero, persistent session state, its own Entra agent identity and an OpenAI-compatible endpoint; choose the Responses protocol (managed history) or Invocations (raw HTTP control), or expose both; if unsure start with Responses. The portal shows agents, a Playground and versions with rollback.
- An agent doesn't need an LLM to work: demo 04 routes a support ticket to a team with a decision model (Decision-1, built on Qwen3.5-9B, no chat call) and a person confirms. Demo 05 runs the same decision hosted in Foundry, switching AzureCliCredential locally to ManagedIdentityCredential (the agent's own identity).
- Takeaways: same agent, new home; hosting is protocol plus identity; an agent needs its own logic, which may or may not use an LLM.

## From linked resources

- The demo repo notes that the local demos target .NET 11 while some hosted-agent projects keep a .NET 10 target for the Foundry hosted runtime; it also includes a hosted Kimi tool-calling agent demo (10).

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk031
- Recording: https://youtu.be/Dq8fcig5-Gk
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK031/beyond-localhost-dotnet-agents-in-foundry-v08.pdf
- Demo repository: https://github.com/elbruno/26-11-DotNetConf-Beyond-Localhost-DotNet-Agents-in-Foundry-public
- 01: Console agent: https://github.com/elbruno/26-11-DotNetConf-Beyond-Localhost-DotNet-Agents-in-Foundry-public/tree/main/demos/01-console-agent
- 02: Host-ready agent: https://github.com/elbruno/26-11-DotNetConf-Beyond-Localhost-DotNet-Agents-in-Foundry-public/tree/main/demos/02-host-ready-agent
- 03: Foundry-hosted agent: https://github.com/elbruno/26-11-DotNetConf-Beyond-Localhost-DotNet-Agents-in-Foundry-public/tree/main/demos/03-foundry-hosted-agent
- 04: Local decision agent: https://github.com/elbruno/26-11-DotNetConf-Beyond-Localhost-DotNet-Agents-in-Foundry-public/tree/main/demos/04-local-decision-agent
- 05: Foundry-hosted decision agent: https://github.com/elbruno/26-11-DotNetConf-Beyond-Localhost-DotNet-Agents-in-Foundry-public/tree/main/demos/05-foundry-hosted-decision-agent
- 10: Foundry-hosted Kimi agent: https://github.com/elbruno/26-11-DotNetConf-Beyond-Localhost-DotNet-Agents-in-Foundry-public/tree/main/demos/10-foundry-hosted-kimi-agent
