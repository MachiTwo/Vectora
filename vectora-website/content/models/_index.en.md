---
title: Models
slug: models
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - byok
  - concepts
  - config
  - embeddings
  - gemini
  - models
  - privacy
  - rag
  - reranker
  - vectora
  - voyage
---

{{< lang-toggle >}}

Vectora works with specific and optimized AI models for programming, user interaction, semantic search, and tactical decisions.

## Vectora Decision Engine (Vectora Cognitive Runtime)

Vectora's local decisive intelligence. Based on SmolLM with proprietary fine-tuning, Vectora Cognitive Runtime runs via **ONNX Runtime** directly on the user's desktop. It decides tactical query routing with zero latency, resorting to the cloud only for specific integrations that do not allow local execution.

## Gemini 3 Flash

Vectora's Programming and Interaction Agent. It is the engine that converses with the developer, writes, refactors, and analyzes code in real time. Gemini 3 Flash utilizes specialized Voyage AIs to retrieve the exact context needed for each task, ensuring precise technical responses in milliseconds.

## Voyage AI

The Voyage suite (Voyage 4 and Rerank 2.5) provides the specialized AIs used by Gemini for RAG (Retrieval-Augmented Generation). The Voyage 4 model is AST-aware, ensuring that searches find logically related functionality rather than just similar text.

## Operation Modes

| Feature             | BYOK Mode (Free)                | Managed Mode (Plus)      |
| :------------------ | :------------------------------ | :----------------------- |
| **Standard Models** | Gemini + Voyage                 | Gemini + Voyage          |
| **Key Management**  | You provide (BYOK)              | Managed by Vectora       |
| **AI Cost**         | Paid to provider (or Free tier) | Included in Vectora plan |
| **Configuration**   | Manual (`vectora config`)       | Automatic (Zero Config)  |
| **Privacy**         | Local keys                      | Managed keys             |

## Next Readings

- [Vectora Cognitive Runtime Architecture](./vectora-decision-engine.md) — SmolLM + ONNX
- [Gemini Configuration](./gemini.md) — Setup Google AI
- [Voyage Configuration](./voyage.md) — Setup Voyage AI
- [Concepts](../concepts/embeddings.md) — How embeddings work

---

## External Linking

| Concept               | Resource                            | Link                                                                                 |
| --------------------- | ----------------------------------- | ------------------------------------------------------------------------------------ |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                       |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)       |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)           |
| **Gemini AI**         | Google DeepMind Gemini Models       | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API**        | Google AI Studio Documentation      | [ai.google.dev/docs](https://ai.google.dev/docs)                                     |
| **Anthropic Claude**  | Claude Documentation                | [docs.anthropic.com/](https://docs.anthropic.com/)                                   |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/), and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
