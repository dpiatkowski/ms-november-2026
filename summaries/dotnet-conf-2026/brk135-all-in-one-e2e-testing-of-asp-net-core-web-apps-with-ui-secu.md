---
event: ".NET Conf 2026"
title: "All in one E2E testing of ASP.NET Core web apps with UI/security/accessibility tests and more"
speaker: "Zoltán Lehóczky"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk135"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/Xclc_0sYZ5A"
session_id: "BRK135"
start: "2026-11-13T16:30:00-08:00"
topics: ["testing", "e2e", "accessibility", "security-testing", "selenium", "aspnet-core", "community-day"]
categories: ["Web development", "Testing and evaluation", "Accessibility", "Application and agent security"]
---

# All in one E2E testing of ASP.NET Core web apps with UI/security/accessibility tests and more

**Speaker(s):** Zoltán Lehóczky

## Summary

Zoltán Lehóczky's talk shows end-to-end testing of an ASP.NET Core app that also covers UI, security and accessibility checks. E2E tests can uncover functional bugs, unwanted design changes, browser/OS/hosting incompatibilities, some concurrency/performance issues, and accessibility and security problems, but are slow and unspecific; a key design question is how far to go (mock everything but the UI, use a real but test-specific backend, or test the production app).

## Key points

- Tool stack in the demo: Orchard Core app, Lombiq UI Testing Toolbox, Selenium, xUnit, Axe (accessibility) and OWASP Zed Attack Proxy (security scanning).
- Topics left out for time: monitoring SQL queries, cross-browser testing, sending e-mails, visual verification, faking the camera, debugging tests.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk135
- Recording: https://youtu.be/Xclc_0sYZ5A
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD218/All%20in%20one%20E2E%20testing%20of%20ASP.NET%20Core%20web%20apps.pptx
- the repo: https://github.com/Lombiq/All-in-one-E2E-testing-of-ASP.NET-Core-web-apps-demo
- Lombiq UI Testing Toolbox for Orchard Core: https://github.com/Lombiq/UI-Testing-Toolbox
