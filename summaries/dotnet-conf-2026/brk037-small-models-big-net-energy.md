---
event: ".NET Conf 2026"
title: "Small Models, Big .NET Energy"
speaker: "Bruno Capuano"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk037"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/ongDevKLRxM"
session_id: "BRK037"
start: "2026-11-10T18:30:00-08:00"
topics: ["ai", "local-models", "foundry-local", "small-language-models", "dotnet-ai"]
categories: ["AI apps and agents", "Game development"]
---

# Small Models, Big .NET Energy

**Speaker(s):** Bruno Capuano

## Summary

Bruno Capuano shows that focused small models run locally can make a small task feel like a complete product feature, building up from speech to text, cleanup and bounded decisions to a local .NET game.

## Key points

- Speech to text with Foundry Local (Nemotron speech model): stream live text segments and read the final transcript after Stop; the same code works with a file or a live microphone.
- Cleanup with a small local model (S1-Mini): removes fillers and self-corrections, fixes punctuation and number formats with explicit styling/structure/context settings, but doesn't fix misheard words or translate; Foundry Local manages both models (speech unloads before S1-Mini loads).
- Decision models choose one answer from options your app supplies and return a confidence and a probability per option (e.g. route a ticket to billing or support); available in Ollama today, coming to Foundry Local and Microsoft.Extensions.AI; demo uses nimble:latest.
- Layers: runtimes (Foundry Local, Ollama), task-specific models, and application frameworks (MEAI abstractions, Agent Framework). Finale: a .NET game with local decisions choosing among five legal moves, validated by the app, plus voice control, all local.

## From linked resources

- The demo repo has six independent projects (Foundry Local speech-to-text from file and microphone, S1-Mini cleanup via library and via Foundry Local, a bounded Ollama Decisions call reporting distribution and latency, and a local-model side-scroller game) with a helper tool that prepares the speech model; no recordings or model weights are included.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk037
- Recording: https://youtu.be/ongDevKLRxM
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK037/small-models-big-dotnet-energy-v09.pdf
- Demo repository: https://github.com/elbruno/26-11-DotNetConf-Small-Models-Big-DotNet-Energy-public
- 01: Local speech to text: https://github.com/elbruno/26-11-DotNetConf-Small-Models-Big-DotNet-Energy-public/tree/main/demos/01-foundry-speech-to-text
- 02: Live speech to text: https://github.com/elbruno/26-11-DotNetConf-Small-Models-Big-DotNet-Energy-public/tree/main/demos/02-foundry-live-speech-to-text
- 03: Transcript cleanup with S1-Mini: https://github.com/elbruno/26-11-DotNetConf-Small-Models-Big-DotNet-Energy-public/tree/main/demos/03-speech-s1mini-library-cleanup
- 04: Speech and cleanup with Foundry Local: https://github.com/elbruno/26-11-DotNetConf-Small-Models-Big-DotNet-Energy-public/tree/main/demos/04-speech-s1mini-foundry-local
- 05: Decisions with Ollama: https://github.com/elbruno/26-11-DotNetConf-Small-Models-Big-DotNet-Energy-public/tree/main/demos/05-decisions-ollama
- 06: Local-model game: https://github.com/elbruno/26-11-DotNetConf-Small-Models-Big-DotNet-Energy-public/tree/main/demos/06-local-model-game
