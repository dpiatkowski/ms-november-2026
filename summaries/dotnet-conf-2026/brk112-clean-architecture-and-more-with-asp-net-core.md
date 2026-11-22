---
event: ".NET Conf 2026"
title: "Clean Architecture AND MORE with ASP.NET Core"
speaker: "Ardalis"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk112"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/HK3IwBezg0w"
session_id: "BRK112"
start: "2026-11-12T14:00:00-08:00"
topics: ["architecture", "clean-architecture", "vertical-slices", "aspnet-core", "community-day"]
categories: ["Web development", "Application architecture"]
---

# Clean Architecture AND MORE with ASP.NET Core

**Speaker(s):** Ardalis

## Summary

Steve 'Ardalis' Smith traces architecture as a response to pain, from database-centric designs to modern modular monoliths, ending with 'know which pain your architecture solves, then pick the one with the least-worst trade-offs' (first law: it depends).

## Key points

- Testability thread: database-at-the-center layered apps (UI/BLL/DAL/DB) made tests slow and brittle, leading to domain-centric architectures (DDD, Hexagonal, Onion, Clean) where dependencies point toward the domain and the .NET project graph lets the compiler enforce the rule. From 2012 the database came home (LocalDB, Docker, SQLite, Testcontainers) so WebApplicationFactory can run the whole stack in-process.
- Ceremony backlash: four projects per endpoint and one-implementation interfaces led to vertical slice architecture (organize by feature), with dependency rules enforced inside one project using NsDepCop.
- Modularity thread: layers aren't boundaries and big balls of mud result; SOA and microservices add a network hop at every boundary (fallacies of distributed computing). Modular monoliths give modules their own data (schema or DbContext), encapsulated public APIs, and each module can pick its own shape (Clean Architecture, vertical slices or simple CRUD). Demos: ardalis/CleanArchitecture templates and the Riverbooks modular monolith sample.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk112
- Recording: https://youtu.be/HK3IwBezg0w
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD113/slides.pdf
- Ardalis: https://ardalis.com
- Clean Architecture Templates: https://github.com/ardalis/CleanArchitecture
- Modular Monoliths: https://ModularMonoliths.com
- Principles, Patterns, and More: https://DevIQ.com
