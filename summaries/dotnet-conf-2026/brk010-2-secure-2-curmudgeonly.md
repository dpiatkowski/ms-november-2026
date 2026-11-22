---
event: ".NET Conf 2026"
title: "2 Secure 2 Curmudgeonly"
speaker: "Barry Dorrans"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk010"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/VExpC7L9mAQ"
session_id: "BRK010"
start: "2026-11-10T13:30:00-08:00"
topics: ["security", "vulnerabilities", "dotnet", "secure-coding"]
categories: ["Application and agent security"]
---

# 2 Secure 2 Curmudgeonly

**Speaker(s):** Barry Dorrans

## Summary

Barry Dorrans' annual .NET security review: vocabulary (CVE, CVSS, CWE; CVSS measures worst-case severity, not risk), the year's numbers, and a tour of notable vulnerabilities with the lesson from each. Slides show 2,622 MSRC cases in 2026 (vs 84 in 2025 as labelled on the slide) and bounties of about $1.01M (up from about $636k). Not every valid report gets a CVE; CVEs are issued for medium CVSS and above.

## Key points

- Out-of-band patches: a Brotli out-of-bounds write classified RCE (not realistically reachable in .NET since decompression is opt-in; lesson: watch dependencies, the CVE process doesn't always work), and the MSQuic RCE that scored 9.8 because it runs in the Windows kernel but less so when .NET runs it in-process (CVSS is a poor severity metric).
- Denial of service: recursive EncryptedXml key decryption, SignedCms rebuilding the certificate set per signer (a 108 KB message stalls a service for seconds), and a crash via a certificate SAN extension through the OpenSSL PAL.
- RCE: WPF/XPS Frame navigation creating nested frames without the unsafe marking, and the .NET SDK workload integrity repair not enforcing NuGet package source mapping. Information disclosure: SocketsHttpHandler kept Proxy-Authorization on an HTTPS redirect (lesson: cover all redirect flows).
- ASP.NET: a data-protection bug where an all-zero MAC validated, Kestrel HTTP/2 HPACK/trailer newline injection enabling request smuggling and auth bypass, and the Negotiate handler's LDAP lookup elevation of privilege; the speaker's view is that 'Windows auth on Linux' was a bad promise and teams should move to OAuth.
- Aspire (not .NET but still covered): four CVEs including RCE from cookie replay and from a planted Directory.Build.rsp.
- Reporting: send vulnerabilities to MSRC, not GitHub issues; check any AI-found results before reporting; grounding docs for AI agents at aka.ms/dotnet/securityfoundations; bounty info at aka.ms/dotnet/bounty.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk010
- Recording: https://youtu.be/VExpC7L9mAQ
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK010/The%20year%20in%20.NET%20Security%20.pptx
