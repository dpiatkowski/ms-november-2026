---
event: ".NET Conf 2026"
title: "Killing Session Theft: Device Bound Session Credentials using ASP.NET Core"
speaker: "Wesley Cabus"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk107"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/QWj9aKirn6s"
session_id: "BRK107"
start: "2026-11-12T11:30:00-08:00"
topics: ["security", "authentication", "aspnet-core", "cookies", "dbsc", "community-day"]
categories: ["ASP.NET Core", "Security"]
---

# Killing Session Theft: Device Bound Session Credentials using ASP.NET Core

**Speaker(s):** Wesley Cabus

## Summary

Wesley Cabus explains Device Bound Session Credentials (DBSC) and how to adopt them in ASP.NET Core. Infostealer malware copies cookies, which are bearer tokens replayable from any device without a password, MFA prompt or passkey (MITRE T1539); DBSC makes stolen cookies useless within minutes.

## Key points

- How it works: the browser creates a key pair per session with the private key in the TPM (not exportable), the server issues a short-lived cookie (minutes), and to refresh it the browser signs a server challenge. Flow uses /.well-known/dbsc/registration and /.well-known/dbsc/refresh with Secure-Session-Registration, Secure-Session-Response and Sec-Secure-Session-Id headers.
- Limits: doesn't stop malware running on the device right now or theft during sign-in (phishing, keyloggers); browser support today is Chrome on Windows and macOS (Chromium-based may follow, not Firefox/Safari yet); in unsupported browsers the header is ignored and a regular cookie is used, so nothing breaks.
- ASP.NET Core (as presented; the package was later pulled from .NET 11, see linked-resource notes below): a prerelease package Microsoft.AspNetCore.Authentication.DeviceBoundSessions (a community package from Thorsten Sauter also exists) adds one line, .AddDeviceBoundSession("Application"), for cookie auth or Identity; it adds {scheme}.Dbsc.Session and {scheme}.Dbsc.Refresh cookie schemes and a policy scheme that prefers the bound cookie and falls back to the original. Demo repo: wcabus/dbsc-aspnetcore.

## From linked resources

- Important update (Maarten Balliauw's post, October 2026): DBSC was pulled from .NET 11 after RC1 because the ASP.NET Core team considered it incomplete, with the removal backported to RC2; the Microsoft.AspNetCore.Authentication.DeviceBoundSessions package will not ship with .NET 11 GA. It may be reworked and return in .NET 12 (tracked in dotnet/aspnetcore#66478). The code shown in the session only works against the RC1 package, so treat it as 'understand now, ship later'. Browser support is Chrome behind an experimental flag.
- Andrew Lock's posts explain DBSC as a progressive enhancement: servers ask for it and browsers that don't support it simply ignore it. A stolen short-lived cookie can be replayed only until it expires (perhaps ten minutes) but cannot be refreshed without the TPM-held key.
- Scott Helme's production lessons from shipping DBSC at Report URI: registration is a single round trip while refresh is two (the first POST gets a 403 with a Secure-Session-Challenge, which is the normal path); keep DBSC state in its own storage, because a concurrent post-login request rewriting the session blob can silently erase the binding and turn the session back into a bearer token; rotate both cookie value and challenge on every refresh; never send a challenge on the registration response; challenge TTL must exceed cookie lifetime.
- The spec is the W3C WebAppSec DBSC draft.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk107
- Recording: https://youtu.be/QWj9aKirn6s
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD108/slides.pdf
- Wesley Cabus: https://wesleycabus.be
- wcabus/dbsc-aspnetcore: https://github.com/wcabus/dbsc-aspnetcore
- https://w3c.github.io/webappsec-dbsc/
- https://scotthelme.co.uk/device-bound-session-credentials-making-stolen-cookies-useless/
- https://scotthelme.co.uk/everything-i-learned-shipping-device-bound-session-credentials/
- https://andrewlock.net/understanding-device-bound-session-credentials/
- https://andrewlock.net/exploring-the-dotnet-11-preview-8-experimental-support-for-device-bound-session-credentials-in-aspnetcore/
- https://blog.maartenballiauw.be/posts/2026-09-16-device-bound-session-credentials-in-aspnet-core/
