---
title: "Search: Pipeline de Busca Semântica"
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

O Search é como o Vectora entende "o que você está procurando" e encontra o código mais relevante no repositório do usuário. Ele implementa um pipeline de 4 estágios: Embedding → Busca Vetorial → Reranking → Composição.

Ao processar consultas em linguagem natural em representações matemáticas, o Vectora consegue unir a intenção humana com a realidade do código-fonte.

## Componentes Principais

O motor de busca do Vectora é composto por camadas especializadas que filtram e refinam as informações em cada etapa do processo de recuperação.

### Embeddings

Representação vetorial de código usando o Voyage 4, treinado especificamente em código-fonte real. Diferente de modelos genéricos, o Voyage captura a semântica intrínseca de programas.

**Saiba como**: [→ Embeddings](./embeddings.md)

### Vector Search

Busca de alta dimensionalidade usando HNSW (Hierarchical Navigable Small World) no MongoDB Atlas. Retorna os 100 candidatos mais similares em milissegundos.

**Saiba como**: [→ Vector Search](./vector-search.md)

### Reranker

O Voyage Rerank 2.5 refina os 100 candidatos para os 10 mais relevantes, aumentando significativamente a precisão. Utiliza um modelo cross-encoder para comparação semântica profunda.

**Saiba como**: [→ Reranker](./reranker.md)

### Reranker Local

Alternativa sem dependência de banco de dados vetorial: busca determinística combinada com reranking semântico local. Ideal para dados mutáveis ou dinâmicos.

**Saiba como**: [→ Reranker Local](./reranker-local.md)

## Fluxo do Pipeline Orquestrado pelo Vectora Cognitive Runtime

O **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** orquestra o pipeline de busca, decidindo se deve usar busca semântica profunda, busca estrutural ou uma combinação de ambas baseada na intenção do usuário.

```text
Query
  ↓
Vectora Cognitive Runtime: Tactical Routing Decision
  ↓
Embeddings (Voyage 4) → 1536D vector
  ↓
Vector Search (HNSW) → 100 candidatos
  ↓
Reranking (Voyage Rerank) → 10 resultados relevantes
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

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
