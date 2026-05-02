---
title: Vector Search
slug: vector-search
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - concepts
  - embeddings
  - mongodb-atlas
  - rag
  - reranker
  - security
  - vector-search
  - vectora
  - voyage
---

{{< lang-toggle >}}

Vector search is the core mechanism that allows Vectora to retrieve semantically relevant context in complex codebases. Unlike traditional keyword-based text searches, vector search operates in semantic space, capturing functional similarity between code concepts.

By transforming code snippets into mathematical vectors, we can find relationships that go beyond literal syntax, identifying equivalent logic written in different ways.

## Vector Search Fundamentals

The vector search process in Vectora follows a rigorous pipeline to ensure accuracy and speed.

1. **Embedding**: Code is transformed into numerical vectors using the `voyage-4` model.
2. **Indexing**: Vectors are stored in MongoDB Atlas with an HNSW (Hierarchical Navigable Small World) index.
3. **Query**: The user's query is converted into an embedding and compared against the index.
4. **Filtering**: Results are filtered by namespace and metadata before being delivered to the agent.

```mermaid
graph LR
    A[Source Code] --> B[AST Parser + Chunking]
    B --> C[Embedding via Voyage 4]
    C --> D[HNSW Index in MongoDB Atlas]
    E[User Query] --> F[Query Embedding]
    F --> D
    D --> G[Namespace Filtering]
    G --> Vectora Cognitive Runtime[Vectora Cognitive Runtime: Tactical Validation]
    Vectora Cognitive Runtime --> H[Context for LLM]
```

The **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** intercepts vector search results to perform **Tactical Validation** (meta-cognition). It analyzes whether the retrieved snippets are indeed relevant to the user's intent, discarding noise and preventing context hallucinations before injection into the LLM.

## Why Vector Search for Code

Lexical searches fail in software engineering scenarios because terms like `validateToken` and `checkJWT` are semantically identical but textually different.

Especially with the `voyage-4` model, we capture:

- **Functional Similarity**: Different implementations that solve the same problem.
- **Architectural Patterns**: Relationships between services, controllers, and models.
- **Semantic Context**: The real meaning behind comments and docstrings.

## Search Architecture in Vectora

We use MongoDB Atlas as a unified backend for vectors and metadata, ensuring atomic consistency and high scalability.

| Component        | Implementation           | Benefit                             |
| :--------------- | :----------------------- | :---------------------------------- |
| **Vector Index** | HNSW with cosine metric  | ANN search with sub-50ms latency    |
| **Filtering**    | Native payload filtering | Strict isolation between namespaces |
| **Scalability**  | Automatic Atlas sharding | Supports billions of code vectors   |

## Indexing Pipeline

Before indexing, Vectora performs **AST-Guided Chunking** using Tree-sitter to identify coherent semantic units, such as entire functions and classes, avoiding breaks in the middle of logic.

### Embedding Generation

Each chunk is processed by the Voyage AI API, generating a 1024-dimensional vector optimized for code comprehension. These vectors are then inserted into Atlas in atomic operations along with their structural metadata.

### Query Flow

When an agent requests context, the query passes through an embedding cache before hitting MongoDB. The `ef_search` parameter is adjusted dynamically: critical refactoring queries use maximum precision, while general navigation prioritizes latency.

## Isolation and Security

Namespace isolation is guaranteed at the vector query level. All searches include mandatory filters that prevent data from different projects from mixing, even in multi-tenant environments.

## External Linking

| Concept               | Resource                                                 | Link                                                                                                       |
| --------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation                        | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**       | Tree-sitter Official Documentation                       | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **Voyage AI**         | High-performance embeddings for RAG                      | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation                          | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                                      | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **HNSW**              | Efficient and robust approximate nearest neighbor search | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)                                               |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
