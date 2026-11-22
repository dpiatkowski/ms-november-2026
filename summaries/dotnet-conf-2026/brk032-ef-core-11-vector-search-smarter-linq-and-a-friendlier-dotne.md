---
event: ".NET Conf 2026"
title: "EF Core 11: Vector Search, Smarter LINQ, and a Friendlier dotnet ef"
speaker: "Jiri Cincura"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk032"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/dgd37KXqcEQ"
session_id: "BRK032"
start: "2026-11-11T16:30:00-08:00"
topics: ["ef-core", "data", "vector-search", "sql-server", "linq", "cosmos-db", "dotnet-11"]
categories: ["Databases and analytics"]
---

# EF Core 11: Vector Search, Smarter LINQ, and a Friendlier dotnet ef

**Speaker(s):** Jiri Cincura

## Summary

Jiří Činčura's EF Core 11 tour (ships with .NET 11): AI/search features, many LINQ and SQL translation improvements, simpler migrations and a friendlier dotnet ef, with lots of community contributions.

## Key points

- LINQ/SQL: vector search with DiskANN and full-text search support, translation for FullJoin, MaxBy/MinBy and List<T>.Exists, pruning of unnecessary joins, EF.Functions.JsonContains, simpler CASE, SqlVector properties not loaded by default, GroupBy aggregate lifting.
- Modeling: complex types and JSON columns for TPC and TPT, temporal period properties mapped to CLR properties, indexes in complex properties.
- Migrations: one-step migrations, ExcludeForeignKeyFromMigrations, skipping ALTER COLUMN when only the CLR type changes, -NoBuild for PMC, bundles with Central Package Management, Migrate/EnsureCreated retry via the execution strategy. dotnet ef: .config/dotnet-ef.json and file-based apps (--file, --startup-file).
- Providers: SQL Server default compatibility level 160 and Microsoft.Data.SqlClient 7.0; Cosmos DB transactional batches, bulk execution, session tokens and System.Text.Json replacing Newtonsoft; SQLite adds Half and targets only .NET 10+. Analyzers EF1003 (string.Format/Concat in raw SQL) and EF1004 (ToAsyncEnumerable vs AsAsyncEnumerable).

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk032
- Recording: https://youtu.be/dgd37KXqcEQ
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK032/EFCore11.pptx
- What's New in EF Core 11: https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-11.0/whatsnew
- Breaking changes in EF Core 11 (EF11): https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-11.0/breaking-changes
