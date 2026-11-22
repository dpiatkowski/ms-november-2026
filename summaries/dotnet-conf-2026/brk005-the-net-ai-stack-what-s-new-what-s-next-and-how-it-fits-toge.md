---
event: ".NET Conf 2026"
title: "The .NET AI Stack: What's New, What's Next, and How It Fits Together"
speaker: "Luis Quintanilla"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk005"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/ziD2ugBywDM"
session_id: "BRK005"
start: "2026-11-10T11:00:00-08:00"
topics: ["ai", "dotnet-ai", "agents", "rag", "local-inference", "architecture"]
categories: ["AI applications", "Architecture", "Blazor"]
---

# The .NET AI Stack: What's New, What's Next, and How It Fits Together

**Speaker(s):** Luis Quintanilla

## Summary

Luis Quintanilla walks the .NET AI stack by building one app, Media Studio, which turns a research paper PDF into a narrated explainer film, mapping each step to a layer: models, decisions, context, multimodal, tools, agents and experiences. A person stays in the loop and nothing is saved until they approve.

## Key points

- Shared foundations: Microsoft.Extensions.AI (model interaction, embeddings, tool definitions), Microsoft.Extensions.VectorData (vector storage/search abstractions) and Microsoft.Extensions.DataIngestion (preview). The demo uses MEAI and DataIngestion, not VectorData, because it works on a single document.
- What's new: official OpenAI and Anthropic SDKs plug into the MEAI contracts (starter kit at aka.ms/meai/start); DocumentExtractionClient (PDFs, images, tables); RoutingChatClient to choose a model per request with your own policies; the OpenAI Decisions API for typed choices/probabilities/scores, with decision abstractions in MEAI coming soon; AG-UI plus Blazor AI Components; MCP C# SDK 2.0. Several are preview or experimental.
- Contract-per-job map: IChatClient, RoutingChatClient, ITextToSpeechClient, IRealtimeClient, IImageGenerator, AIFunction/AIAgent, AgentBoundary and AG-UI for hosting agents in Blazor, with Microsoft.ML.Tokenizers and System.Numerics.Tensors underneath and cloud or local providers behind the same contracts.
- Message: add AI as another building block to an existing app (a Jellyfin semantic-search example), use AI where it adds value and plain code for deterministic steps.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk005
- Recording: https://youtu.be/ziD2ugBywDM
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK005/dotnet-ai-stack-dotnetconf-2026.pdf
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK005/dotnet-ai-stack-dotnetconf-2026.pptx
