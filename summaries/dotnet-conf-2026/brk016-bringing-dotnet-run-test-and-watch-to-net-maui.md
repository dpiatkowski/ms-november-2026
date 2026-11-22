---
event: ".NET Conf 2026"
title: "Bringing dotnet run, test, and watch to .NET MAUI"
speaker: "Jonathan Peppers"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk016"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/Lw7nN8sBZn0"
session_id: "BRK016"
start: "2026-11-10T16:30:00-08:00"
topics: ["maui", "dotnet-cli", "mobile", "testing", "hot-reload", "ci"]
categories: ["Desktop and mobile apps", "Testing and evaluation"]
---

# Bringing dotnet run, test, and watch to .NET MAUI

**Speaker(s):** Jonathan Peppers

## Summary

Jonathan Peppers shows how the .NET CLI gained first-class device support for MAUI and other mobile workloads in .NET 11: dotnet run, dotnet watch and dotnet test all build on one run pipeline (restore, select target, build, deploy, get run args, run). MAUI began IDE-first (F5); the VS Code era and coding agents make a scriptable CLI workflow important.

## Key points

- dotnet run adds device selection and deployment: pick a framework (-f net11.0-android), list devices (--list-devices) and choose one (--device). MSBuild is the contract between CLI and workload via three targets, including ComputeAvailableDevices (device IDs, names, status) and DeployToDevice.
- dotnet watch reuses dotnet run for launching and adds a code-update loop: a startup hook inside the app receives Hot Reload updates, and because a named pipe on the host can't reach a phone, it uses an authenticated WebSocket to the device app.
- dotnet test reuses the run pipeline to launch a mobile test app built on Microsoft.Testing.Platform, with platform test templates (e.g. dotnet new androidtest) and results returned to the terminal; without -f it runs all target frameworks and picks devices for each.
- One foundation, three workflows; a combined Android emulator demo closes the talk.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk016
- Recording: https://youtu.be/Lw7nN8sBZn0
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK016/DotNetConf-CLI-MAUI-NET11.pptx
