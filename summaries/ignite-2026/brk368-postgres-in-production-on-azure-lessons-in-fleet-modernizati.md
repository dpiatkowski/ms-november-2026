---
event: "Microsoft Ignite 2026"
title: "Postgres in production on Azure: Lessons in fleet modernization"
speaker: "Guy Bowerman, Danyal Bukhari, Sven Hubert"
source_url: "https://ignite.microsoft.com/en-US/sessions/1787856629108001E3Up-1791588323549001CZ65"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: null
ondemand_url: "https://medius.microsoft.com/Embed/video-nc/f15a59e7-e2c1-4c03-b39f-6244732c2cff"
session_id: "BRK368"
session_type: "Breakout"
start: "2026-11-19T19:30:00Z"
level: "(200) Intermediate"
ignite_topics: ["Data", "PostgreSQL", "Migration and modernization"]
topics: ["postgresql", "azure-database-for-postgresql", "elastic-clusters", "fleet-management", "backups"]
categories: ["Azure databases", "Migration and modernization"]
---

# Postgres in production on Azure: Lessons in fleet modernization

**Speaker(s):** Guy Bowerman, Danyal Bukhari, Sven Hubert

## Summary

The session covers modernizing a fleet of self-hosted PostgreSQL servers to Azure Database for PostgreSQL: managed high availability, backups and disaster recovery, Entra ID and Defender, confidential compute, customer-managed keys, 90+ extensions, in-place major version upgrades and adaptive autovacuum, with ongoing optimization as hardware, software and security demands change.

Wolters Kluwer Tax and Accounting Germany describes moving from self-managed PostgreSQL on three VMs (2 TB, manual upgrades, extra pgBouncer VM) to Flexible Server and then to an Elastic Cluster (six nodes with high availability, backups, horizontal scaling and time-series partitioning, under-30-minute restore) because its ORM already supported a compatible sharding model. Considerations include custom extension management such as pg_partman. Results are customer-reported.

## References

- Session page: https://ignite.microsoft.com/en-US/sessions/1787856629108001E3Up-1791588323549001CZ65
- On-demand recording (Microsoft-hosted): https://medius.microsoft.com/Embed/video-nc/f15a59e7-e2c1-4c03-b39f-6244732c2cff
- Slide deck (Microsoft-hosted, not copied here): https://medius.microsoft.com/video/asset/PPT/f15a59e7-e2c1-4c03-b39f-6244732c2cff
