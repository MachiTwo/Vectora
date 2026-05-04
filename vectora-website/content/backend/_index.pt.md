---
title: "Backend: Arquitetura de Dados"
slug: backend
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - backend
  - lancedb
  - postgresql
  - redis
  - storage
  - vectora
draft: false
---

{{< lang-toggle >}}

{{< section-toggle >}}

O backend do Vectora usa três bancos de dados com responsabilidades distintas: PostgreSQL para dados relacionais (usuários, sessões, logs do VCR), Redis para cache em memória (embeddings, rate limiting) e LanceDB para índices vetoriais (chunks de código). Nenhum dado de código sai da máquina local.

## Três Bancos, Três Responsabilidades

A separação por tipo de dado elimina a necessidade de um banco multi-propósito. Cada tecnologia é usada para o que faz melhor.

| Banco          | Tipo       | Responsabilidade             | Persistência    |
| -------------- | ---------- | ---------------------------- | --------------- |
| **PostgreSQL** | Relacional | Auth, sessões, logs VCR      | Disco (durável) |
| **Redis**      | In-memory  | Cache embeddings, rate limit | RAM (TTL)       |
| **LanceDB**    | Vetorial   | Índices de código (HNSW)     | Disco (local)   |

## PostgreSQL

Banco relacional principal. Armazena usuários, tokens JWT, permissões RBAC, histórico de sessões e logs de decisão do VCR. Usa o driver `pg8000` (Python puro, sem dependência de libpq).

Schemas principais:

- `users` — credenciais, roles, configurações
- `sessions` — tokens de acesso, refresh tokens, expiração
- `vcr_logs` — decisões do VCR com faithfulness score, strategy usada, latência
- `agent_runs` — histórico de execuções do agente com steps e metadados

**[Ver PostgreSQL](./postgresql.md)**

## Redis

Cache in-memory com TTL configurável. Responsabilidade principal: armazenar embeddings VoyageAI por 24h para evitar chamadas repetidas à API. Também gerencia rate limiting por usuário e tokens de sessão de curta duração.

Prefixos de chave:

- `embed:{sha256}` — embedding de texto (TTL: 86400s)
- `rate:{user_id}` — contador de requests (TTL: 60s)
- `session:{token_id}` — dados de sessão temporária (TTL: 3600s)

**[Ver Redis](./redis.md)**

## LanceDB

Banco vetorial local. Armazena os embeddings 1024D dos chunks de código com índice HNSW para busca por similaridade. Roda completamente em disco sem servidor externo — os dados do codebase nunca saem da máquina.

Tabelas principais:

- `code_chunks` — chunks de código com embedding, path, language, content
- `doc_chunks` — chunks de documentação e comentários

**[Ver LanceDB](./lancedb.md)**

## Stack de Acesso

```python
# PostgreSQL
import pg8000.native

conn = pg8000.native.Connection(
    host="localhost",
    database="vectora",
    user="vectora",
    password="...",
)

# Redis
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

# LanceDB
import lancedb

db = lancedb.connect("./data/lancedb")
```

## Configuração via .env

```bash
# PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=vectora
POSTGRES_USER=vectora
POSTGRES_PASSWORD=sua-senha

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# LanceDB
LANCEDB_PATH=./data/lancedb
```

## External Linking

| Conceito       | Recurso                                | Link                                                          |
| -------------- | -------------------------------------- | ------------------------------------------------------------- |
| **PostgreSQL** | PostgreSQL 16 documentation            | [postgresql.org/docs/16](https://www.postgresql.org/docs/16/) |
| **pg8000**     | Python PostgreSQL driver               | [github.com/tlocke/pg8000](https://github.com/tlocke/pg8000)  |
| **Redis**      | Redis 7 documentation                  | [redis.io/docs](https://redis.io/docs/)                       |
| **LanceDB**    | Vector database local para RAG         | [lancedb.com/docs](https://lancedb.com/docs)                  |
| **HNSW**       | Efficient approximate nearest neighbor | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)  |
