---
title: "Suite de Testes: Caching & Hybrid Search"
slug: caching-hybrid-search
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - caching
  - concepts
  - embeddings
  - mongodb-atlas
  - performance
  - persistence
  - security
  - system
  - testing
  - tools
  - vector-search
  - vectora
---

{{< lang-toggle >}}

O sistema híbrido de cache (L1 local + L2 cloud) deve otimizar a performance, reduzir a latência e manter taxas de acerto (hit rates) acima de 70%. Esta suite valida o aquecimento de cache, preloading, busca híbrida com estratégias de fallback e sincronização inteligente.

Estes testes garantem que o Vectora permaneça responsivo mesmo com grandes bases de código e consultas frequentes.

**Cobertura**: 120+ testes | **Prioridade**: ALTA

## Camadas de Cache

A arquitetura de cache é dividida em múltiplos níveis para equilibrar velocidade e persistência.

### 1. Cache L1 (Memória Local)

Validado através de testes focados em acesso imediato e gestão de armazenamento volátil.

- Inicialização e capacidade máxima (5 testes)
- TTL (Time To Live) e expiração (8 testes)
- Políticas de expulsão (LRU, LFU) (8 testes)
- Rastreamento de taxa hit/miss (5 testes)
- Segurança de acesso concorrente (5 testes)

**SLA**: Hit rate > 70%, latência p95 < 50ms

### 2. Cache L2 (Disco Persistente/Cloud)

Foca no armazenamento de longo prazo e na sincronização entre diferentes ambientes.

- Serialização e desserialização (10 testes)
- Sincronização Local/Cloud (12 testes)
- Compressão de valores (8 testes)
- Data roaming entre dispositivos (10 testes)
- Recuperação de falhas (8 testes)

**SLA**: Hit rate > 50%, sincronização em < 5s

### 3. Cache Warming & Preloading

Garante que o contexto relevante esteja disponível antes mesmo de ser explicitamente solicitado pelo agente.

- Estratégias de aquecimento (8 testes)
- Preloading baseado em padrões (8 testes)
- Atualizações incrementais (8 testes)

### 4. Orquestração de Busca Híbrida

Valida a coordenação entre a recuperação em cache e o motor de busca vetorial primário.

- Orquestração cache → busca (15 testes)
- Estratégias de fallback (10 testes)
- Latência p95 < 100ms (10 testes)
- Throughput > 500 queries/seg (5 testes)

### 5. Integração com o Engine

Garante que todas as ferramentas de busca utilizem corretamente as camadas de cache disponíveis.

- Cache em `search_context()` (8 testes)
- Cache de embeddings (8 testes)
- Cache de reranking (8 testes)
- Invalidação inteligente (8 testes)

## SLAs de Performance

A tabela a seguir resume as metas de performance para o sistema de cache.

| Métrica                 | Alvo    |
| :---------------------- | :------ |
| **Hit Rate L1**         | > 70%   |
| **Hit Rate L2**         | > 50%   |
| **Latência p50 (hit)**  | < 10ms  |
| **Latência p95 (hit)**  | < 50ms  |
| **Latência p50 (miss)** | < 100ms |
| **Pegada de Memória**   | < 500MB |

## External Linking

| Concept           | Resource                          | Link                                                                                                       |
| ----------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
