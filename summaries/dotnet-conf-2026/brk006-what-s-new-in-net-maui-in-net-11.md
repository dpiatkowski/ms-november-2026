---
event: ".NET Conf 2026"
title: "What's New in .NET MAUI in .NET 11"
speaker: "Gerald Versluis"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk006"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/fh0c-EBCifU"
session_id: "BRK006"
start: "2026-11-10T11:30:00-08:00"
topics: ["maui", "dotnet-11", "xaml", "coreclr", "hot-reload", "android", "ai-assisted-dev"]
---

# What's New in .NET MAUI in .NET 11

**Speaker(s):** Gerald Versluis

## Summary

Gerald Versluis' roundup of .NET MAUI 11: CoreCLR becomes the runtime on mobile, XAML gets source-generated and less verbose, a batch of new controls and platform features lands, and the CLI/AI tooling story (MAUI Labs) expands. Opens with ecosystem stats: merged PRs across the MAUI repos grew 4x in a year, with about 80% now Copilot-authored, plus contributions from partners such as Syncfusion and Uno Platform.

## Key points

- CoreCLR on mobile ('the biggest change you won't see, but will feel'), shown with BaristaNotes benchmarks of package size and startup on Pixel 5/Android 14 and iPhone 15 Pro/iOS 26 (.NET 11 RC2). Android NativeAOT is experimental; MAUI NativeAOT on iOS has an accepted compiler warning.
- XAML: every XAML file compiles to C# at build time (XAML source generation, with an opt-out to the old XamlC inflator), no more xmlns boilerplate on each page, and inline C# expressions in XAML that replace most value converters.
- New features: long-press gesture, tab and toolbar badges, passkeys (WebAuthn, Face ID/Windows Hello/biometrics), Material 3 on Android via UseMaterial3, map pin clustering and custom pins, per-animation cancellation, BoxView gradients, themed splash screens, system bar colors, and a C#-first UI template (--ui csharp).
- Tooling: dotnet run/test/watch target devices and emulators, XAML Incremental Hot Reload on by default in Debug, and the MAUI Inspector (visual tree, record/replay, Copilot via MCP).
- MAUI Labs (github.com/dotnet/maui-labs): MAUI CLI (maui doctor, SDK/emulator management, --json for CI), DevFlow (inspect and drive a running app, MCP server), Essentials.AI (on-device chat and embeddings via Microsoft.Extensions.AI), AI extensions, agent skills (maui ai init), Comet MVU, WPF and Linux (GTK) backends.
- Support policy: each MAUI version is patched for 18 months; MAUI 9 ended May 2026, MAUI 10 runs to May 2027, MAUI 11 to May 2028 assuming .NET 12 ships Nov 2027. The .NET Conf app itself (jfversluis/dotnetconf-app) is a MAUI 11 app on both stores.

## From linked resources

- Learn's what's-new page frames the .NET 11 focus as product quality. MAUI ships as a workload plus NuGet packages so projects can pin versions. CoreCLR became the default runtime in Preview 4; from Preview 7 it is the default for .NET 11 apps and NativeAOT is an opt-in publishing alternative. RC1 adds test project templates (androidtest, iostest, tvostest, macostest, maccatalysttest) that run on Microsoft.Testing.Platform via dotnet test.
- The MAUI Labs repo lists its products: maui CLI, Comet (MVU) and Go (single-file prototyping), DevFlow, AI Extensions, macOS AppKit and WPF backends, Essentials.AI, AppProjectReference and MAUI Testing. It stresses these are experimental and not covered by the MAUI support policy.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk006
- Recording: https://youtu.be/fh0c-EBCifU
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK006/dotnetconf26-maui-whatsnew.pdf
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK006/dotnetconf26-maui-whatsnew.pptx
- What's new in .NET MAUI for .NET 11: https://learn.microsoft.com/dotnet/maui/whats-new/dotnet-11
- .NET MAUI repository: https://github.com/dotnet/maui
- .NET MAUI Labs: https://github.com/dotnet/maui-labs
- .NET MAUI support policy: https://aka.ms/maui-support-policy
- Download .NET 11: https://get.dot.net
- Source code: https://github.com/jfversluis/dotnetconf-app
- App Store: https://apps.apple.com/app/net-conf/id6820239033
- Google Play: https://play.google.com/store/apps/details?id=dev.jfversluis.dotnetconf
