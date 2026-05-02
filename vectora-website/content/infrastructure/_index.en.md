---
title: "Infrastructure: Support Layer"
slug: infrastructure
date: 2026-04-25T23:00:00-03:00
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - concepts
  - embeddings
  - guardian
  - infrastructure
  - mongodb-atlas
  - multi-tenant
  - persistence
  - privacy
  - rag
  - reranker
  - security
  - state
  - trust-folder
  - vector-search
  - vectora
  - voyage
draft: false
---

{{< lang-toggle >}}

Infrastructure is everything needed to "run Vectora" — storage, data isolation, security, and persistence. It is the foundation that allows Core and Search to function reliably and securely.

By providing a robust and scalable environment, the Infrastructure layer ensures that your data is always accessible, protected, and properly contextualized.

## Principal Components

The infrastructure is built on several key components that manage data lifecycle and access control.

### Namespaces

Multi-tenant isolation at the vector index level. Each user namespace contains its projects (workspaces), preventing cross-contamination of data and ensuring strict privacy.

**Learn how**: [→ Namespaces](./namespaces.md)

### State Persistence

Short-term memory (current iterations) and long-term memory (history in MongoDB Atlas). It ensures that Vectora "remembers" the conversation context and learning over time.

**Learn how**: [→ State Persistence](./state-persistence.md)

### Trust Folder

Filesystem sandbox with directory traversal prevention, secret leakage protection, and path validation. The Guardian component validates every access attempt.

**Learn how**: [→ Trust Folder](./trust-folder.md)

## Storage Architecture

Vectora utilizes a hierarchical storage model to organize data efficiently and securely.

```text
MongoDB Atlas
├── Namespaces (multi-tenant isolation)
│   ├── Vectors (Voyage 4, HNSW indexed)
│   ├── Metadata (AST, dependencies, language)
│   ├── Operational State (sessions, memory)
│   └── Audit Logs (compliance, traceability)
```

## External Linking

| Concept               | Resource                            | Link                                                                                                       |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation   | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**       | Tree-sitter Official Documentation  | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **Secure Coding**     | OWASP Secure Coding Practices       | [owasp.org/www-project-secure-coding-practices/](https://owasp.org/www-project-secure-coding-practices/)   |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
