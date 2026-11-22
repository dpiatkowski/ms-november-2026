---
event: ".NET Conf 2026"
title: "No XAML Required: Native Windows Apps in Pure C#"
speaker: "Alexandre Zollinger Chohfi"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk027"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/stj-kD2qu4E"
session_id: "BRK027"
start: "2026-11-11T14:00:00-08:00"
topics: ["winui", "csharp", "mvu", "file-based-apps", "analyzers", "experimental"]
categories: ["Desktop and mobile apps"]
---

# No XAML Required: Native Windows Apps in Pure C#

**Speaker(s):** Alexandre Zollinger Chohfi

## Summary

Alexandre Zollinger Chohfi presents Microsoft.UI.Reactor, an experimental MIT-licensed C# framework for WinUI that brings Model-View-Update (MVU) UI: UI is a function of state, rendered with real WinUI controls (no new renderer, no fork). A whole app can be one .cs file run with dotnet run counter.cs, or a full project scaffolded with winapp new -t reactor.

## Key points

- State lives in hooks (UseState, UseReducer with record-based actions and pure, unit-testable reducers). Hooks are tracked by call order so they must not be called conditionally; an analyzer (REACTOR_HOOKS_001) enforces it, as part of 60+ analyzers (missing .WithKey, hard-coded colors instead of theme tokens, icon-only buttons without accessibility labels).
- Lists need keys: without them items are matched by position and rewritten when one is inserted at the top; early samples reconciled badly, so there is now a keyed diff plus analyzers. Profiling real apps pointed at short-lived allocations from modifier chains rather than diffing.
- XAML is not going away: interop runs both ways in one process and one visual tree, and the advice is not to migrate but to add Reactor to one small new screen.
- Tooling: winapp run --watch with hot reload that keeps state, DevTools to inspect components with their source lines and live state; a Reactor Gallery of 93 pages. Used in production in a Windows companion chat app; also running on Uno Platform (macOS, Linux, WebAssembly). Repo: github.com/microsoft/microsoft-ui-reactor.

## From linked resources

- The Reactor README (status: experimental, April 2026) stresses it is not a new UI platform: it describes WinUI content via a virtual element tree and reconciler, hooks, a typed C# DSL and higher-level building blocks (flex layout, charting, navigation, data grid), many of which are candidates to migrate back into WinUI.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk027
- Recording: https://youtu.be/stj-kD2qu4E
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK027/Reactor-DotNetConf-2026.pptx
- Microsoft.UI.Reactor on GitHub: https://github.com/microsoft/microsoft-ui-reactor
