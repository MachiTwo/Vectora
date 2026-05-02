---
title: Context Engine
slug: context-engine
date: "2026-04-19T09:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - adk
  - agentic-framework
  - agents
  - ai
  - ast-parsing
  - auth
  - claude
  - concepts
  - config
  - context-engine
  - embeddings
  - go
  - guardian
  - jwt
  - mongodb-atlas
  - rag
  - reranker
  - search
  - semantic
  - tree-sitter
  - vector-db
  - vector-search
  - vectora
  - voyage
  - yaml
---

{{< lang-toggle >}}

O Context Engine é o coração da orquestração do Vectora. Ele decide **o quê, como e quando** buscar contexto em seu codebase, evitando ruído e overfetch.

> [!IMPORTANT] Context Engine não é apenas busca. É um pipeline inteligente: **Embed → Search → Rerank → Compose → Validate**.

## O Problema

Agents genéricos retornam 50 arquivos irrelevantes para uma query simples. O Context Engine filtra por relevância, reduzindo para 5-10 chunks altamente úteis.

## Estratégias de Busca

O Context Engine oferece três estratégias de busca independentes ou combinadas, dependendo do tipo de consulta e precisão desejada.

## Semântica

Usa embeddings para encontrar similaridade funcional. Ideal para "Como validar tokens?"

## Estrutural

Usa AST parsing para relações de código. Ideal para "Que funções chamam X?"

## Híbrida

Combina semântica + estrutura. Ideal para refatoração de módulos.

## Pipeline Orquestrado pelo Vectora Cognitive Runtime

O **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** orquestra cada etapa do pipeline do Context Engine, decidindo o roteamento dinâmico e validando a qualidade da saída.

1. **Embedding**: Query → vetor 1024D (Voyage 4).
2. **Search**: MongoDB Atlas com filters por namespace.
3. **Validação Tática (Vectora Cognitive Runtime)**: O Vectora Cognitive Runtime analisa se os candidatos iniciais justificam um reranking pesado.
4. **Reranking**: Voyage Rerank 2.5 refina top-50 para top-10.
5. **Compaction**: head/tail reduz tamanho sem perder contexto.
6. **Observação de Faithfulness (Vectora Cognitive Runtime)**: O Vectora Cognitive Runtime valida se o contexto final é fiel e suficiente para o Agentic Framework.

## Configuração

```yaml
context_engine:
  strategy: "auto"
  max_depth: 3
  compaction: true
  include_ast: true
  include_dependencies: true
```

## Exemplos Práticos

Abaixo estão dois exemplos detalhados mostrando como o Context Engine processa queries e retorna contexto estruturado.

## Exemplo 1: Busca Semântica

**Query**: "Como validar tokens?"

```text
Input:
  - Query: "Como validar tokens?"
  - Strategy: semantic
  - Namespace: seu-projeto
  - Top-k: 10

Processamento:
  1. Embed: Query → vetor 1536D via Voyage 4
  2. Search: HNSW busca 100 candidatos mais próximos
  3. Rerank: Voyage Rerank 2.5 refina para top-10
  4. Compaction: Reduz tamanho de 15KB → 4KB mantendo contexto
  5. Validate: Agentic Framework valida output, captura métricas

Output:
  chunks: [
    {file: "src/auth/jwt.ts", precision: 0.89, content: "...validateToken..."},
    {file: "src/auth/guards.ts", precision: 0.78, content: "...middleware..."},
    ...
  ]
  metadata: {
    retrieval_precision: 0.87,
    latency_ms: 234,
    total_searched: 3159,
    compaction_ratio: 0.27
  }
```

## Exemplo 2: Busca Estrutural

**Query**: "Quem chama getUserById?"

```text
Input:
  - Symbol: getUserById
  - Strategy: structural
  - Include indirect: true

Processamento:
  1. AST Parse: Analisa arquivo onde getUserById é definido
  2. Call Graph: Encontra todas as referências (diretas + indiretas)
  3. Context: Extrai linhas de contexto de cada chamada

Output:
  direct_calls: 47
  indirect_calls: 12
  callers: [
    {file: "src/middleware/auth.ts", line: 34, type: "direct"},
    {file: "src/routes/profile.ts", line: 12, type: "indirect via getUserData"},
    ...
  ]
```

## External Linking

| Concept               | Resource                            | Link                                                                                                       |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation   | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Anthropic Claude**  | Claude Documentation                | [docs.anthropic.com/](https://docs.anthropic.com/)                                                         |
| **AST Parsing**       | Tree-sitter Official Documentation  | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |

---

> **Próximo**: [Agentic Framework](./agentic-framework.md)

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
