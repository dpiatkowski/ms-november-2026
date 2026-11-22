---
event: ".NET Conf 2026"
title: "More Processes, More Problems - how to speed up your builds with Multithreaded MSBuild"
speaker: "Chet Husk"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk008"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/9WDTK828qtg"
session_id: "BRK008"
start: "2026-11-10T12:30:00-08:00"
topics: ["msbuild", "build-performance", "dotnet-cli", "tooling"]
---

# More Processes, More Problems - how to speed up your builds with Multithreaded MSBuild

**Speaker(s):** Chet Husk

## Summary

Chet Husk introduces multithreaded MSBuild (-mt), shipping opt-in with .NET 11, which runs project builds as threads inside one engine process instead of many worker processes. Gains depend on the solution and tasks, and the slides stress the numbers are single paired development-toolchain observations rather than GA benchmarks.

## Key points

- Orchard Core results (SDK 11.0.100-rtm, MSBuild 18.13): cold full build 116.05 s to 88.74 s on Windows (-23.5%) and 96.15 s to 84.74 s on Linux (-11.9%); warm incremental after a source edit 54.58 s to 17.36 s on Windows (-68.2%) and 25.47 s to 22.13 s on Linux (-13.1%).
- Mechanism: today a scheduler plus worker processes keep per-configuration state (a configuration is project path plus global properties, not just Debug/Release) and talk over IPC; -mt brings those nodes into one process with thread nodes, cutting duplicated engine work, task handoffs and IPC.
- Task authors: one process means one current directory, so tasks must resolve paths via TaskEnvironment rather than the process. Mark tasks [MSBuildMultiThreadableTask]; unmarked tasks are isolated in a sidecar TaskHost process, so migration can be incremental. Typed file items (ITaskItem<FileInfo>) replace string path handling.
- Help for migrating: Microsoft.Build.TaskAuthoring.Analyzer (NuGet), a migration guide on Learn, and an agent skill in dotnet/msbuild (plugins/mt-migration).
- Plan per the speaker's roadmap: try dotnet build -mt now; default-on planned for SDK 11.0.200 in early 2027 (the slides note this wasn't independently confirmed publicly). -mt does not parallelize tasks within one target; ordering of target/task dependencies is preserved.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk008
- Recording: https://youtu.be/9WDTK828qtg
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK008/multithreaded-msbuild.pptx
