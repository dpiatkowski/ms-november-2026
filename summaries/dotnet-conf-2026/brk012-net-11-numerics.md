---
event: ".NET Conf 2026"
title: ".NET 11 Numerics"
speaker: "Tanner Gooding"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk012"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/jSecTephxJc"
session_id: "BRK012"
start: "2026-11-10T14:30:00-08:00"
topics: ["numerics", "dotnet-11", "performance", "tensors", "generic-math"]
categories: ["C# and .NET runtime"]
---

# .NET 11 Numerics

**Speaker(s):** Tanner Gooding

## Summary

Tanner Gooding's tour of .NET 11 numerics along three themes: represent (new number formats), compose (generic math, Complex<T>) and execute (faster, well-defined tensors), with a short .NET 12 lookahead.

## Key points

- IEEE 754 decimal floating point: Decimal32/64/128 (7, 16 and 34 significant digits) with NaN, infinities, signed zero and quantum (1.0 vs 1.00 carry different intent, Quantize(1.235, 0.01) gives 1.24); distinct from System.Decimal. BFloat16 joins Half for 16-bit floats (Half has more precision near one, BFloat16 has float-like range).
- Complex<T> works over a choice of component types (float, double, even Decimal128), and one generic algorithm constrained by INumberBase<T> runs across all of them.
- Tensors: layout-aware paths for sliced or gapped data; slides record backport results such as dense float Add on 64x16 going from 16.37 us to 0.114 us and gapped-row FlattenTo from 7.92 us to 0.875 us. Correctness gets equal weight: shapes, broadcasting, empty tensors, slice overlap validation, NaN/tie/signed-zero results, and guaranteed fused multiply-add with a scalar fallback only for cancellation-sensitive vectors.
- Building blocks: generic Random methods (NextInteger<BigInteger>, NextBinaryFloat<Half>), partial parsing and UTF-8 conversion for BigInteger/Complex, hexadecimal float parsing. .NET 12 lookahead: more layout-aware tensor paths (Stack, Concatenate, Reverse) and fewer intermediate allocations.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk012
- Recording: https://youtu.be/jSecTephxJc
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/BRK012/DotNetConf-2026-Numerics.pptx
