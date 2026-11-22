---
event: ".NET Conf 2026"
title: "What NOT to AI: Hand-Crafting Your App's Core Foundation"
speaker: "Michael Washington"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk116"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/Hu0pDa0jwkM"
session_id: "BRK116"
start: "2026-11-12T16:00:00-08:00"
topics: ["ai", "vibe-coding", "architecture", "agentic-coding", "community-day"]
---

# What NOT to AI: Hand-Crafting Your App's Core Foundation

**Speaker(s):** Michael Washington

## Summary

Michael Washington's argument that AI can now write nearly all of an application, so the skill is knowing which decisions you must keep: design the application, choose the technology stack, and set the UI direction. His workflow is spec-first: you effectively 'code Markdown', and the agent writes the C#.

## Key points

- Workflow: reusable prompt template (by Saad Awais) that makes the agent research the codebase and interview you with options and recommended defaults, then a master .md describing the whole app end to end, sub .md files per area that you review, and only then code generated from those files. Don't 'vibe code' feature by feature: the agent can't see where the app is going and drifts into refactoring.
- Decide yourself: authentication, database and data access (expensive to reverse), and UI direction (mockups from Stitch with Google or Claude /design from an edited UI prompt, saved to docs/mockups; the agent builds to match and compares in a browser).
- Hand to the agent: coding, initial testing by running the app, security checks against the running app, fixing findings, the user guide, and deployment with Aspire to Azure Container Apps. AI code will contain bugs and security issues, so auditing and testing is crucial (example: an agent-written SecurityReview.md with 19 findings).
- Examples built in October 2026 with no hand-typed C#: Blazor Azure Inventory (Entra sign-in, Azure resource inventory, knowledge graph, AI chat) and Aspire Deploy Service (Windows app that deploys Aspire 13 solutions to Azure Container Apps).

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk116
- Recording: https://youtu.be/Hu0pDa0jwkM
- BlazorHelpWebsite.com: https://blazorhelpwebsite.com/ViewBlogPost/20094
- What-Not-To-AI-Animated.pptx: https://adefwebserver.com/download/What-Not-To-AI-Animated.pptx
- Blazor Azure Inventory: https://github.com/ADefWebserver/Blazor-Azure-Inventory
- Aspire Deploy Service: https://github.com/ADefWebserver/AspireDeployService
