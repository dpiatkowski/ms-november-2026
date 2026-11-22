---
event: ".NET Conf 2026"
title: "Azure's new lineup for .NET developers (Part 1)"
speaker: "Matt Soucoup, Paul Yuknewicz"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk028"
source_type: "session-abstract+references"
summary_type: "ai-generated"
video_url: "https://youtu.be/o6hODySxDTA"
session_id: "BRK028"
start: "2026-11-11T14:30:00-08:00"
topics: ["azure", "container-apps", "ai-gateway", "sre-agent", "copilot", "agents"]
categories: ["Cloud infrastructure", "AI-assisted development"]
---

# Azure's new lineup for .NET developers (Part 1)

**Speaker(s):** Matt Soucoup, Paul Yuknewicz

## Summary

Live tour of new Azure capabilities for .NET developers: Azure Container Apps sandboxes for running untrusted code, AI Gateway for governing model and tool calls, SRE Agent for operations, Azure Functions Hosted Skills, and Copilot canvases (the microsoft/azure-dev-tools plugins) in the developer workflow. The session's slide deck is truncated in the conference repo (the file cuts off at 4 MiB and cannot be opened), so details below come from the linked materials.

## Key points

- Sandbox demo (paulyuk/aca-sandboxes-dotnet-demo): an agent has a model but its document-processing tool does not; the tool runs inside a .NET 10 Container Apps sandbox with default-deny egress, no model key and no Azure identity, while the host uses the new Sandbox .NET SDK to create the sandbox, upload files, run the tool, inspect egress decisions and clean up. Models are reached through an Azure AI Gateway.
- Azure Functions Hosted Skills 'Dynamic Workflows' (public preview, Python 3.13+): an LLM reads an event once and writes a typed DAG plan; the embedded Durable Functions engine executes it outside the reasoning loop (fan-out/fan-in, retries, timeouts, for_each/when control flow, sub agents, durable timers), so intermediate results don't flow back through the LLM, cutting tokens and latency; enabled with workflows.enabled: true in the .agent.md front matter.
- microsoft/azure-dev-tools: GitHub Copilot plugins/canvases for Azure cost health, Functions, Hosted Skills, Resource Graph queries, SRE Agent, Storage and containers.

## From linked resources

- Azure Container Apps Sandboxes are generally available per the Azure docs: microVM isolation with their own kernel, an egress proxy with deny policies and allowlists, snapshots and sub-second resume, and CLI/SDK/REST control, which is the capability the loan-application demo relies on.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk028
- Recording: https://youtu.be/o6hODySxDTA
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK028/BRK028-029.pptx
- Azure Container Apps sandboxes .NET demo: https://github.com/paulyuk/aca-sandboxes-dotnet-demo/blob/main/README.md
- Get Azure Canvases: https://github.com/microsoft/azure-dev-tools
- Azure sandboxes documentation: https://sandboxes.azure.com/docs/sandboxes/
- Deterministic workflow with Azure Functions Hosted Skills: https://devblogs.microsoft.com/azure-sdk/dynamic-workflows-azure-functions-hosted-skills/
