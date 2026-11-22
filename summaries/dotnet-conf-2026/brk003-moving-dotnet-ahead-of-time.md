---
event: ".NET Conf 2026"
title: "Moving `dotnet` Ahead (of Time)!"
speaker: "Chet Husk"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk003"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/d_2bTXnJQqQ"
session_id: "BRK003"
start: "2026-11-10T10:00:00-08:00"
topics: ["dotnet-cli", "native-aot", "performance", "dotnet-11", "tooling"]
categories: [".NET", "Performance"]
---

# Moving `dotnet` Ahead (of Time)!

**Speaker(s):** Chet Husk

## Summary

Chet Husk explains how the .NET CLI is being moved to Native AOT to cut startup cost, since CLI usage keeps growing and every tool builds on it. The dotnet muxer loads an AOT-compiled SDK library that handles eligible commands natively and falls back to the managed CLI in the same process (via hostfxr) for everything else.

## Key points

- Measured on macOS arm64 with .NET 11.0.100 (medians of 40 runs): dotnet --version ~118 ms managed vs ~33 ms AOT; a chain of three inspection commands 374 ms vs 118 ms (-68.6%).
- Already migrated: built-in diagnostics (--version, --info), solution commands (sln list/migrate/remove), tool management (local list/run/uninstall/search), external command launch from PATH, and narrow cached file-based-app runs and build-free MTP tests. Build commands, tool install/restore and dotnet new are the next work areas; not a delivery promise.
- Code had to change: reflection-based discovery replaced with generated metadata or explicit registration, no runtime code generation on the native path, accurate trim/AOT annotations plus reachability tests. Libraries needed AOT-friendly seams too (NuGet, source-generated COM, MSBuild analysis).
- Gotchas: Environment.ProcessPath, AppContext.BaseDirectory and Assembly.Location don't mean what executable-hosted code assumes inside a library; telemetry storage paths had to be unified across the native/managed bridge.
- Cost/benefit: external-command resolution added ~2.2 MiB (+14.9%) to the win-x64 image, build-free MTP testing ~1 MiB (+5.8%). Size is judged with tooling (sizoscope/sizospy) and by looking at the SDK as a whole (about 53 MB compressed of duplicate files in the Linux x64 tarball). Costly patterns: XML parsing pulling in networking, embedded resources, builder-style broad APIs, runtime capability checks.
- Testing guidance: test the real muxer/library/bridge path per target, check parity between managed and AOT modes, and assert tests were actually discovered.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk003
- Recording: https://youtu.be/d_2bTXnJQqQ
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK003/native-aot-dotnet-cli.pptx
