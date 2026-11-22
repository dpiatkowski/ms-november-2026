---
event: ".NET Conf 2026"
title: "How Do AI Systems Like ChatGPT Work? A Clear Explanation for Everyone!"
speaker: "Otto Dobretsberger"
source_url: "https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk113"
source_type: "session-abstract+slides"
summary_type: "ai-generated"
video_url: "https://youtu.be/ZRovrZ_0hf0"
session_id: "BRK113"
start: "2026-11-12T14:30:00-08:00"
topics: ["ai", "llm", "fundamentals", "community-day"]
categories: ["AI applications"]
---

# How Do AI Systems Like ChatGPT Work? A Clear Explanation for Everyone!

**Speaker(s):** Otto Dobretsberger

## Summary

Otto Dobretsberger explains how ChatGPT-style systems work for a general audience, using the 'finish the sentence' idea and unpacking the name GPT (Generative Pre-trained Transformer) plus 'Chat', starting with a toy language model built by counting word pairs in 'Roses are red, violets are blue'.

## Key points

- Toy model: counting what follows each word generates text by dice rolls, but looking only one word back loops or loses the rhyme; widening the context explodes the table (50,000-word vocabulary needs 2.5 billion rows for 2 words context).
- Transformer pipeline: text, tokens with IDs, vectors (embeddings place similar tokens close together), layers of attention (which earlier words matter) plus neurons, repeated many times (96 layers in the example), scores for every token, then one token is picked.
- Generative: scores become probabilities via softmax, temperature controls randomness, and text is produced one token at a time in a loop. Pre-trained: parameters are like a recipe adjusted during training by guessing the next token of real text.
- Chat: tuning turns autocomplete into an assistant; the model actually reads a hidden system prompt plus the whole conversation again each turn; the talk closes with strengths (drafting, summarising, translating, code) and limits that follow from next-token prediction.

## References

- Session page: https://dotnet.microsoft.com/en-us/conf/2026/agenda/brk113
- Recording: https://youtu.be/ZRovrZ_0hf0
- Slides (read for this summary; published in the conference repo, not copied here): https://github.com/dotnetConf/2026/blob/main/Technical/CommunityDays/CD114/How%20Do%20AI%20Systems%20Like%20ChatGPT%20Work.pdf
