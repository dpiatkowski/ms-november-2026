---
event: ".NET Conf 2026"
title: "Less Chat, More Action: AI-Powered .NET MAUI Apps"
speaker: "Gerald Versluis"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk033"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/FYGBT08-N48"
session_id: "BRK033"
start: "2026-11-11T17:30:00-08:00"
topics: ["maui", "ai", "microsoft-extensions-ai", "tool-calling", "mobile"]
---

# Less Chat, More Action: AI-Powered .NET MAUI Apps

**Speaker(s):** Gerald Versluis

## Summary

Gerald Versluis argues users want apps that act, not another chatbot: phones already hold the context (camera, microphone, location, calendar, health), so AI should find things and do things ('Save all the Aspire sessions', 'Blazor talks on Thursday') inside the .NET Conf app. He walks through the building blocks of an AI-powered MAUI app.

## Key points

- One IChatClient (Microsoft.Extensions.AI) for cloud, local and on-device models, with tool calling and telemetry as middleware; three swappable packages: your app, AI attributes and Microsoft.Extensions.AI/Essentials.AI.
- Essentials.AI (preview) does for models what Xamarin.Essentials did for sensors: built-in OS models behind IChatClient (Apple Intelligence on iOS/macOS/Mac Catalyst, Gemini Nano on Android, Windows AI), nothing to ship and nothing leaving the device, or bundled/cloud models (Foundry, OpenAI). Choose per feature, check the model is available, and note on-device is private, offline and free per token but smaller.
- AI attributes: [ExportAIFunction] with [Description] turns methods into tools via a source generator (no reflection); [AIToolSource] collects them. Tools only stage actions, and the app runs them through the same view models and services as the UI.
- Keeping users in control: ApprovalRequired = true so the model can propose but never execute (confirming runs plain C#), validate tool arguments like user input, confirm destructive actions. On-device embeddings give semantic search. Ideas: AI wayfinding (draft PR in maui-labs) and UI that adapts to intent.

## From linked resources

- Learn overview of Microsoft.Maui.Essentials.AI (experimental; using it raises diagnostic MAUIAI0001 that must be suppressed): IChatClient and IEmbeddingGenerator on built-in platform models; chat via Apple Intelligence on iOS/Mac Catalyst 26+ (tools and structured output), Windows AI on Copilot+ PCs (Windows 11 24H2+, structured output) and Gemini Nano on Android API 26+ (tools on capable models); text embeddings on Apple platforms (version 27+ via Apple Natural Language); prompts and responses never leave the device.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk033
- Recording: https://youtu.be/FYGBT08-N48
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK033/dotnetconf26-brk033-less-chat-more-action.pdf
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK033/dotnetconf26-brk033-less-chat-more-action.pptx
- AI in .NET MAUI documentation: https://learn.microsoft.com/dotnet/maui/ai
- .NET MAUI Labs: https://github.com/dotnet/maui-labs
- Microsoft.Maui.Essentials.AI: https://www.nuget.org/packages/Microsoft.Maui.Essentials.AI
- Microsoft.Maui.AI.Attributes: https://www.nuget.org/packages/Microsoft.Maui.AI.Attributes
- BaristaNotes sample: https://github.com/davidortinau/BaristaNotes
- Source code: https://github.com/jfversluis/dotnetconf-app
- App Store: https://apps.apple.com/app/net-conf/id6820239033
- Google Play: https://play.google.com/store/apps/details?id=dev.jfversluis.dotnetconf
