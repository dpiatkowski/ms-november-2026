---
event: ".NET Conf 2026"
title: "Give Your .NET Agent a Face: Building an AI Desk Companion with M5Stack"
speaker: "Bruno Capuano"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk040"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/7EXrTrcJ7zA"
session_id: "BRK040"
start: "2026-11-11T19:00:00-08:00"
topics: ["iot", "agents", "aspire", "robotics", "embedded", "dotnet-11"]
categories: ["Edge AI and devices", "AI apps and agents"]
---

# Give Your .NET Agent a Face: Building an AI Desk Companion with M5Stack

**Speaker(s):** Bruno Capuano

## Summary

Bruno Capuano gives a .NET agent a face, voice and movement with M5Stack's StackChan desk robot, and shows a second custom-firmware robot with a .NET backend.

## Key points

- Robot 1 (StackChan factory firmware): the manufacturer's cloud handles conversation, and a custom C# MCP server (MCP SDK console app) connects outbound over a secure WebSocket so the robot's conversation can invoke your tools; demoed with eShopLite (outdoor gear shop with semantic search, run with Aspire). The token stays private and the connection is prepared ahead of the session.
- Robot 2 ('New Year, New Bot'): custom C/C++ firmware and an animated .NET avatar on private Wi-Fi, talking over HTTP on a trusted LAN to an ASP.NET Core / .NET 11 backend (RobotHub with behavior and notification policy). The work agent (Microsoft Agent Framework with Foundry) is disabled by default and opt-in with synthetic data; GitHub Copilot SDK, Microsoft 365 and WorkIQ MCP integrations are planned. Live demo sends a notification that arrives on the desk. See aka.ms/newyearnewbot.

## From linked resources

- The New Year, New Bot repo adds a standalone file-based C# sample, 'Which device is on this COM port?', that inspects USB serial device metadata and watches plug/unplug events without opening a port, with self-tests needing no hardware; the project hub is aka.ms/newyearnewbot.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk040
- Recording: https://youtu.be/7EXrTrcJ7zA
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK040/give-your-dotnet-agent-a-face-v07.pdf
- Project repository: https://github.com/elbruno/new-year-new-bot
- serial-port device inspection sample: https://github.com/elbruno/new-year-new-bot/tree/main/tools/serial-ports
