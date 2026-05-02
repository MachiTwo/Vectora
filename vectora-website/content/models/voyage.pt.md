---
title: "Voyage AI: A Precisão por Trás do Vectora"
slug: voyage
date: "2026-04-18T22:30:00-03:00"
draft: false
categories:
  - Deep Dive
tags:
  - ai
  - architecture
  - ast-parsing
  - auth
  - byok
  - concepts
  - config
  - embeddings
  - flash
  - gemini
  - go
  - guardian
  - inteligência
  - mcp
  - mongodb-atlas
  - rag
  - reranker
  - state
  - tree-sitter
  - vector-db
  - vector-search
  - vectora
  - voyage
  - yaml
type: docs
sidebar:
  open: true
---

{{< lang-toggle >}}

Enquanto o **Gemini 3 Flash** atua como o agente de programação e interação, a precisão cirúrgica da busca do Vectora depende das IAs especializadas do **Voyage AI**. Utilizamos o **Voyage 4** para embeddings e o **Voyage Rerank 2.5** para garantir que apenas o contexto mais relevante alcance o motor principal.

## A Infraestrutura de Recuperação: Voyage 4 & Rerank 2.5

Vectora utiliza estas IAs especializadas para garantir que o contexto enviado ao Gemini seja o mais preciso possível, minimizando alucinações e otimizando o consumo de tokens.

## Por que usamos Voyage AI?

A nossa escolha pelo Voyage AI reside na sua superioridade técnica em ambientes de desenvolvimento e sua integração nativa com o fluxo de trabalho do Gemini no Vectora.

### 1. Especialização em Código e AST

Diferente de modelos de uso geral, o Voyage 4 foi treinado especificamente em vastos repositórios de código-fonte. Ele compreende sintaxes complexas e é **AST-aware** (ciente de estruturas de árvores sintáticas), permitindo que o Vectora encontre funcionalidades logicamente relacionadas mesmo quando a nomenclatura é diferente.

### 2. Pipeline de Recuperação em Duas Etapas

O Voyage fornece a suite completa para o nosso pipeline de alta precisão:

- **Etapa 1 (Embedding)**: O Voyage 4 converte pedaços de código em vetores de alta dimensão, armazenados no MongoDB Atlas.
- **Etapa 2 (Reranking)**: O Voyage Rerank 2.5 atua como um filtro final, reclassificando os resultados para que apenas os 5 pedaços mais pertinentes cheguem ao Gemini.

### 3. Eficiência para o Gemini 3 Flash

O Voyage Rerank 2.5 é fundamental para a eficiência do Gemini. Ao filtrar ruídos e garantir que "verdadeiros positivos" cheguem ao agente, reduzimos drasticamente o desperdício de janela de contexto e aumentamos a qualidade das respostas técnicas.

## Arquitetura: O Fluxo de Vetores

1. **Fragmentação (Chunking)**: O código é dividido com reconhecimento de AST via Tree-sitter.
2. **Transformação**: O Voyage 4 converte esses fragmentos em vetores de 1.536 dimensões.
3. **Indexação**: Vetores são persistidos no MongoDB Atlas HNSW.
4. **Refinamento**: Durante a consulta, o Voyage Rerank 2.5 reavalia os principais vizinhos encontrados, garantindo relevância contextual absoluta.

## Configuração

Para o correto funcionamento do pipeline no modo BYOK, seu `vectora.config.yaml` deve referenciar as chaves do Voyage:

```yaml
providers:
  embedding:
    name: "voyage"
    model: "voyage-4"
    api_key: "${VOYAGE_API_KEY}"

  reranker:
    name: "voyage"
    model: "voyage-rerank-2.5"
    api_key: "${VOYAGE_API_KEY}"
```

## Preços & Viabilidade

O Voyage AI é extremamente econômico, mantendo o custo operacional do Vectora no plano gratuito (BYOK) em patamares baixíssimos:

| Modelo                | Custo (por 1M tokens) | Papel no Vectora                 |
| :-------------------- | :-------------------- | :------------------------------- |
| **Voyage 4**          | $0.02                 | Busca Semântica Inicial          |
| **Voyage Rerank 2.5** | $2.00                 | Filtro de Precisão para o Gemini |

A maioria dos projetos custa menos de **$1/mês** em taxas de API do Voyage, permitindo que o usuário usufrua de uma busca de nível empresarial com investimento mínimo.

## External Linking

| Concept               | Resource                            | Link                                                                                                       |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **MongoDB Atlas**     | Atlas Vector Search Documentation   | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**       | Tree-sitter Official Documentation  | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **Gemini AI**         | Google DeepMind Gemini Models       | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)                       |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
