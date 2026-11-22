---
event: ".NET Conf 2026"
title: "Post-Quantum Cryptography with .NET 11"
speaker: "Jeremy Barton"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk015"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/pLGVnUFQjfM"
session_id: "BRK015"
start: "2026-11-10T16:00:00-08:00"
topics: ["cryptography", "post-quantum", "security", "dotnet-11"]
categories: ["Security", ".NET"]
---

# Post-Quantum Cryptography with .NET 11

**Speaker(s):** Jeremy Barton

## Summary

Jeremy Barton explains why post-quantum cryptography matters (quantum computers break the hardness assumptions behind RSA and elliptic curves; encryption faces 'harvest now, decrypt later' while signatures mainly lose trust on 'Q day') and what .NET offers. .NET 10 added ML-DSA, SLH-DSA, Composite ML-DSA and ML-KEM (plus the TLS 1.3 hybrid KEM); .NET 11 adds more.

## Key points

- Composite ML-KEM pairs ML-KEM with a traditional algorithm so both must be broken to reveal the secret; the slides show the initiator and receiver flows (import encapsulation key, encapsulate; decapsulate with the private key, then derive an AES-GCM key).
- HPKE (RFC 9180) combines key establishment, nonce/IV management, AEAD tag verification and message ordering into one API based on a suite of KEM, KDF and AEAD (HpkeSender/HpkeRecipient). EnvelopedCms gains ML-KEM support; Composite ML-KEM there throws NotSupportedException in 11.0.0.
- Expected in 11.0.x: ML-KEM and hybrid ML-KEM in HPKE (draft-ietf-hpke-pq) and Composite ML-KEM in EnvelopedCms. Maybe .NET 12 or later, no promises: removing [Experimental] once RFCs publish and better multi-certificate TLS support.
- Non-PQC additions in .NET 11: X25519DiffieHellman and AES key wrap (EncryptKeyWrap/DecryptKeyWrap).

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk015
- Recording: https://youtu.be/pLGVnUFQjfM
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK015/PQC%20in%20.NET%2011.pptx
