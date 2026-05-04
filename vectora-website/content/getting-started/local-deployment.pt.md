---
title: "Deploy Local do Vectora"
description: "Configuração completa para ambiente de desenvolvimento local com Docker, PostgreSQL e Redis"
slug: "local-deployment"
tags:
  - deployment
  - local
  - setup
  - development
  - docker
  - postgresql
  - redis
  - lancedb
date: 2026-05-03
weight: 2.3
---

{{< lang-toggle >}}

{{< section-toggle >}}

Vectora pode rodar completamente em sua máquina usando Docker Compose para orquestrar PostgreSQL, Redis e LanceDB. Este guia cobre as duas formas de rodar localmente: modo de desenvolvimento (Python direto) e modo containerizado (Docker Compose).

## Modo 1: Desenvolvimento Direto (Sem Docker)

Para desenvolvimento ativo, rode os serviços de infraestrutura no Docker e Vectora diretamente em Python:

### 1. Subir infraestrutura com Docker Compose

```bash
# Subir só PostgreSQL + Redis (sem LanceDB — LanceDB é arquivo local)
docker compose up -d postgres redis
```

Arquivo `docker-compose.dev.yml`:

```yaml
version: "3.9"
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: vectora
      POSTGRES_PASSWORD: vectora
      POSTGRES_DB: vectora
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

volumes:
  postgres_data:
  redis_data:
```

### 2. Configurar variáveis de ambiente

```bash
# .env (na raiz do projeto)
POSTGRES_URL=postgresql://vectora:vectora@localhost:5432/vectora
REDIS_URL=redis://localhost:6379
LANCEDB_PATH=./data/lancedb
VOYAGEAI_API_KEY=sk-voyage-xxx
ANTHROPIC_API_KEY=sk-ant-xxx  # Opcional
```

### 3. Inicializar banco de dados

```bash
# Criar tabelas PostgreSQL
uv run python -m vectora.db.migrations

# Confirmar tabelas criadas
uv run python -c "from vectora.db import check_health; check_health()"
```

### 4. Subir Vectora

```bash
uv run uvicorn vectora.api.main:app --reload --port 8000
```

## Modo 2: Docker Compose Completo

Para ambientes de teste ou produção local, rode toda a stack em Docker:

### docker-compose.yml

```yaml
version: "3.9"
services:
  vectora:
    build: .
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_URL=postgresql://vectora:vectora@postgres:5432/vectora
      - REDIS_URL=redis://redis:6379
      - LANCEDB_PATH=/data/lancedb
      - VOYAGEAI_API_KEY=${VOYAGEAI_API_KEY}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - lancedb_data:/data/lancedb
      - vcr_models:/app/models

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: vectora
      POSTGRES_PASSWORD: vectora
      POSTGRES_DB: vectora
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U vectora"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
  redis_data:
  lancedb_data:
  vcr_models:
```

### Subir toda a stack

```bash
# Copiar .env.example para .env e preencher
cp .env.example .env
# Editar .env com sua VOYAGEAI_API_KEY

# Subir todos os serviços
docker compose up -d

# Ver logs
docker compose logs -f vectora

# Verificar que está rodando
curl http://localhost:8000/health
```

## Verificação de Saúde

```bash
# Health check completo
curl http://localhost:8000/health

# Resposta esperada:
# {
#   "status": "healthy",
#   "components": {
#     "vcr": {"status": "running", "latency_ms": 7.4},
#     "lancedb": {"status": "running", "indices": 0},
#     "postgres": {"status": "connected"},
#     "redis": {"status": "connected"}
#   }
# }
```

## Estrutura de Dados

### PostgreSQL

Vectora usa PostgreSQL para:

- **Usuários e autenticação** (tabela `users`)
- **Sessões de agentes** (tabela `agent_sessions`)
- **Logs de decisão do VCR** (tabela `vcr_decisions`)
- **Configurações** (tabela `config`)

### Redis

Redis é usado para:

- **Cache de embeddings** (TTL 24h) — evita chamadas repetidas à VoyageAI
- **Cache de reranking** (TTL 1h) — resultados XLM-RoBERTa
- **Sessões de usuário** (TTL 8h)
- **Rate limiting** por IP e usuário

### LanceDB

LanceDB é armazenado localmente em disco (arquivo):

- **Índice de código** (tabela `code_chunks`) — chunks do seu codebase
- **Índice de docs** (tabela `doc_chunks`) — documentação indexada
- **Embeddings 1024D** — VoyageAI vectors

## Configuração Avançada

### Ajuste de Performance

```yaml
# .env para ambientes com mais recursos
LANCEDB_CACHE_SIZE=1024MB
REDIS_MAXMEMORY=512mb
POSTGRES_MAX_CONNECTIONS=50
VCR_BATCH_SIZE=32
VCR_NUM_THREADS=4
```

### SSL/TLS (Produção Local)

```bash
# Gerar certificado self-signed
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Subir com HTTPS
uv run uvicorn vectora.api.main:app --ssl-keyfile key.pem --ssl-certfile cert.pem --port 8443
```

## Troubleshooting

### Connection refused: postgres

```bash
docker compose ps
docker compose logs postgres
```

### Redis connection failed

```bash
# Testar conexão Redis
redis-cli -h localhost -p 6379 ping
# Resposta esperada: PONG
```

### LanceDB permission error (Windows)

```bash
mkdir data\lancedb
icacls data\lancedb /grant %USERNAME%:F
```

### VCR latência alta (acima de 20ms)

```bash
vectora vcr benchmark
# Se latência > 15ms, verificar processos em background
```

## External Linking

| Conceito              | Recurso                             | Link                                                            |
| --------------------- | ----------------------------------- | --------------------------------------------------------------- |
| **Docker Compose**    | Documentação oficial Docker Compose | [docs.docker.com/compose](https://docs.docker.com/compose/)     |
| **PostgreSQL Docker** | Imagem oficial PostgreSQL           | [hub.docker.com/\_/postgres](https://hub.docker.com/_/postgres) |
| **Redis Docker**      | Imagem oficial Redis                | [hub.docker.com/\_/redis](https://hub.docker.com/_/redis)       |
| **LanceDB**           | Setup e configuração LanceDB        | [lancedb.com/docs](https://lancedb.com/docs)                    |
| **uvicorn**           | ASGI server para FastAPI            | [uvicorn.org](https://www.uvicorn.org/)                         |
