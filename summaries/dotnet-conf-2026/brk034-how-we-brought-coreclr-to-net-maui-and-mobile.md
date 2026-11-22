---
event: ".NET Conf 2026"
title: "How We Brought CoreCLR to .NET MAUI and Mobile"
speaker: "Jonathan Peppers"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk034"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/fa_rzHLYU_E"
session_id: "BRK034"
start: "2026-11-10T17:00:00-08:00"
topics: ["maui", "coreclr", "mono", "native-aot", "mobile", "performance", "trimming"]
categories: [".NET", "Mobile devices", "Performance"]
---

# How We Brought CoreCLR to .NET MAUI and Mobile

**Speaker(s):** Jonathan Peppers

## Summary

A deep dive into why and how .NET MAUI moved from Mono to CoreCLR: the history (Xamarin to unified .NET), how an Android/iOS app starts and hosts the runtime, how code is compiled (Mono AOT vs ReadyToRun), NativeAOT as a separate model, measured results, and a migration checklist.

## Key points

- Timeline: .NET 10 offered experimental CoreCLR on Android (UseMonoRuntime=false); in .NET 11 Preview 4 CoreCLR became the default for Debug and Release on Android, iOS, Mac Catalyst and tvOS, and from Preview 6 selecting Mono for a net11.0 mobile target gives NETSDK1242 (target .NET 10 if Mono is required).
- Architecture: Android owns the process, the .NET SDK supplies the bootstrap, and the host talks to CoreCLR through a narrow hosting API instead of the many Mono embedding APIs. A shared runtime means shared diagnostics (debugger, profiler, crash reports) with server/desktop.
- Compilation: runtime and compilation are separate choices; Android Release uses Mono AOT before and ReadyToRun (partial, profile-guided via .mibc, or full composite) now. NativeAOT is a third model (no JIT, no dynamic loading, trimming and source-generated JSON needed) and not part of the CoreCLR migration.
- Results (Oct 27 report, one device per platform, mean of 10 runs, three apps): CoreCLR started faster than Mono on iPhone XR for all three apps, and on Samsung Galaxy A16 default (partial R2R) CoreCLR beat Mono for all; full R2R helped the larger app but was slower for the small templates. APK size was app-dependent (default CoreCLR slightly larger for the templates, smaller for the large app; full R2R bigger), and logical iOS bundle size was smaller with CoreCLR. Measure your own app.
- Migration checklist: test Release builds on real devices for startup, memory and size; run existing tests; verify debugging and crash reporting.

## From linked resources

- Learn's .NET MAUI for .NET 11 page confirms the timeline: CoreCLR default on all MAUI platforms from Preview 4 with Mono still available, and from Preview 7 CoreCLR default with NativeAOT as an opt-in publish alternative; the stated benefits are unified debugging, profiling, Hot Reload, app size and performance.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk034
- Recording: https://youtu.be/fa_rzHLYU_E
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK034/CoreCLR-MAUI-NET11.pptx
