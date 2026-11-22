---
event: ".NET Conf 2026"
title: "Beyond Code Generation: Give AI Eyes and Hands for .NET MAUI"
speaker: "Gerald Versluis"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk026"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/-3ClD7BHbLU"
session_id: "BRK026"
start: "2026-11-11T13:30:00-08:00"
topics: ["maui", "ai", "copilot", "mcp", "devflow", "testing", "agents"]
categories: ["Desktop and mobile apps", "AI-assisted development", "AI apps and agents"]
---

# Beyond Code Generation: Give AI Eyes and Hands for .NET MAUI

**Speaker(s):** Gerald Versluis

## Summary

Gerald Versluis argues that an AI that writes XAML but has never seen the app run is limited, and demonstrates four MAUI Labs tools that give coding agents 'eyes and hands' on real devices, using Copilot to drive the .NET Conf app.

## Key points

- MAUI CLI: sets up SDKs, emulators and devices (maui doctor), the same commands for you and your agent; MAUI Sherpa desktop app for SDKs, emulators, certificates and inspecting a running app; maui ai init installs skills, custom agents and MCP config for Visual Studio, VS Code and others (skills cover layouts, accessibility, Blazor Hybrid and DevFlow).
- DevFlow: an MCP server (maui devflow mcp) plus broker and a Debug-only in-app agent (Microsoft.Maui.DevFlow.Agent, AddMauiDevFlowAgent) let the agent read the visual tree, taps controls by name, logs and network traffic; the tree is more reliable than a screenshot because it knows properties and survives layout shifts.
- Inspector and Mobile Canvas: a live view of what the agent sees (screenshot, visual tree, properties, logs) and a simulator/emulator inside the editor that you and Copilot drive together, reading the accessibility tree.
- Workflow: inspect, point at the wrong control, change, verify, with prompts that name the device, symptom and proof wanted; habits: start from a running app, ask for proof, review every diff before commit.

## From linked resources

- Mobile Canvas (Redth/mobile-canvas-ghcp, MIT): a Copilot plugin and VS Code extension that shows live iOS Simulators and Android emulators (H.264 at roughly 58 FPS on iOS and 50 FPS on Android) with real taps, drags and keyboard, and exposes mobile_device_* tools to the agent via MCP; everything runs on loopback. MAUI Sherpa is a free open-source desktop app (macOS, Windows, Linux) with an environment doctor, SDK/workload and emulator management and DevFlow inspectors.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk026
- Recording: https://youtu.be/-3ClD7BHbLU
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK026/dotnetconf26-maui-build-with-ai.pdf
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK026/dotnetconf26-maui-build-with-ai.pptx
- .NET MAUI Labs: https://github.com/dotnet/maui-labs
- MAUI CLI package: https://www.nuget.org/packages/Microsoft.Maui.Cli
- MAUI Sherpa: https://redth.github.io/MAUI.Sherpa
- Mobile Canvas: https://github.com/Redth/mobile-canvas-ghcp
- Source code: https://github.com/jfversluis/dotnetconf-app
- App Store: https://apps.apple.com/app/net-conf/id6820239033
- Google Play: https://play.google.com/store/apps/details?id=dev.jfversluis.dotnetconf
