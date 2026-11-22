---
event: ".NET Conf 2026"
title: ".NET + Foundry: Better Together"
speaker: "Bruno Capuano"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk007"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/o2RUf9npgns"
session_id: "BRK007"
start: "2026-11-11T16:00:00-08:00"
topics: ["foundry", "ai", "dotnet-ai", "azure", "models"]
categories: ["Azure", "AI applications"]
---

# .NET + Foundry: Better Together

**Speaker(s):** Bruno Capuano

## Summary

Bruno Capuano's map of how .NET and Microsoft Foundry fit together: .NET gives the application its shape and Foundry brings AI capabilities, with a stable app contract and verification of each deployment's actual support.

## Key points

- Layers: Microsoft.Extensions.AI (IChatClient: one chat contract across providers) for model access vs Microsoft Agent Framework (AIAgent: instructions, tools, sessions, workflows) for agent behavior.
- Three Foundry paths: direct model call via IChatClient, app-owned agents (AIAgent in your process using a Foundry model deployment), and service-managed agents (prompt agents or hosted agents called from a .NET client). Consuming an agent is different from deploying one (prompt agent = model + instructions + tools; hosted code = custom runtime + protocol). One call doesn't mean identical support: model availability, Responses/tool support and output behavior vary per deployment.
- Where agent code runs: Foundry hosted agents (agent-specific managed hosting, built-in endpoint and identity), Azure Container Apps (container flexibility, less platform work) or AKS (Kubernetes control, AKS Automatic reduces operations).
- Reliable agents need boundaries: toolboxes with narrow permissions, guardrails, minimal memory, tracing, identity (AzureCliCredential locally, DefaultAzureCredential hosted) and per-deployment provider fit. Demo repo has model comparison, prompt/code/hosted agents, bounded decisions, toolbox discovery, guardrails and tool evaluation.

## From linked resources

- The demo repo lists eleven numbered demos: model comparison across GPT, Grok and Kimi through one IChatClient call site, a versioned prompt agent, a code-defined agent, hosting through the Foundry Responses protocol (with and without tools), native Decisions models for bounded support routing (direct, as an agent, and hosted), toolbox discovery, offline guardrails and tool evaluation; it requires the .NET 11.0.100 SDK.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk007
- Recording: https://youtu.be/o2RUf9npgns
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK007/dotnet-foundry-better-together-v07.pdf
- Demo repository: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public
- 01: Model comparison: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/01-model-comparison
- 02: Prompt agent: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/02-prompt-agent
- 03: Code agent: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/03-code-agent
- 04: Hosted agent: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/04-hosted-agent
- 05: Hosted agent with tools: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/05-hosted-agent-tools
- 10: Bounded decisions: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/10-bounded-decisions
- 11: Bounded decisions agent: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/11-bounded-decisions-agent
- 12: Hosted bounded decisions agent: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/12-bounded-decisions-agent-hosted
- 20: Toolbox discovery: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/20-toolbox-discovery
- 21: Application guardrails: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/21-application-guardrails
- 22: Tool evaluation: https://github.com/elbruno/26-11-DotNetConf-DotNet-Foundry-Better-Together-public/tree/main/demos/22-tool-evaluation
