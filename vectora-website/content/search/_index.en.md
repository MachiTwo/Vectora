---
title: "Search: Semantic Search Pipeline"
slug: search
date: 2026-04-25T23:00:00-03:00
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - concepts
  - embeddings
  - mongodb-atlas
  - rag
  - reranker
  - search
  - semantic-search
  - vector-search
  - vectora
  - voyage
draft: false
---

{{< lang-toggle >}}

Search is how Vectora understands "what you are looking for" and finds the most relevant code in the user's repository. It implements a 4-stage pipeline: Embedding → Vector Search → Reranking → Composition.

By processing natural language queries into mathematical representations, Vectora can bridge the gap between human intent and source code reality.

## Principal Components

Vectora's search engine is composed of specialized layers that filter and refine information at every step of the retrieval process.

### Embeddings

Vector representation of code using Voyage 4, trained specifically on real-world source code. Unlike generic models, Voyage captures "code-ness" — the semantic structure of programs.

**Learn how**: [→ Embeddings](./embeddings.md)

### Vector Search

High-dimensional search using HNSW (Hierarchical Navigable Small World) in MongoDB Atlas. It returns the top 100 most similar candidates in milliseconds.

**Learn how**: [→ Vector Search](./vector-search.md)

### Reranker

Voyage Rerank 2.5 refines the 100 candidates to the top 10 most relevant ones, increasing precision significantly. It uses a cross-encoder model for deep semantic comparison.

**Learn how**: [→ Reranker](./reranker.md)

### Local Reranker

An alternative without vector DB dependency: deterministic search combined with local semantic reranking. Ideal for mutable or dynamic data.

**Learn how**: [→ Reranker Local](./reranker-local.md)

## Vectora Cognitive Runtime-Orchestrated Pipeline Flow

The **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** orchestrates the search pipeline, deciding whether to use deep semantic search, structural search, or a combination of both based on the user's intent.

```text
Query
  ↓
Vectora Cognitive Runtime: Tactical Routing Decision
  ↓
Embeddings (Voyage 4) → 1536D vector
  ↓
Vector Search (HNSW) → 100 candidates
  ↓
Reranking (Voyage Rerank) → 10 relevant results
  ↓
Vectora Cognitive Runtime: Faithfulness Validation
  ↓
Context Composition
```

## External Linking

| Concept               | Resource                                                   | Link                                                                                                       |
| --------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation                          | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Voyage AI**         | High-performance embeddings for RAG                        | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation                            | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                                        | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **RAG**               | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                                               |
| **HNSW**              | Efficient and robust approximate nearest neighbor search   | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)                                               |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
