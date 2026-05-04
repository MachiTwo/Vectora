---
title: "DevOps: Infraestrutura e Deploy"
slug: devops
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ci-cd
  - devops
  - docker
  - infrastructure
  - jenkins
  - vectora
draft: false
---

{{< lang-toggle >}}

{{< section-toggle >}}

O Vectora usa Docker para containerização e Jenkins para CI/CD. A stack completa (FastAPI + PostgreSQL + Redis) roda via Docker Compose em desenvolvimento e pode ser implantada em qualquer host Linux via Docker em produção.

## Componentes de Infraestrutura

| Componente          | Tecnologia              | Responsabilidade                   |
| ------------------- | ----------------------- | ---------------------------------- |
| **Containerização** | Docker + Docker Compose | Empacotamento e orquestração local |
| **CI/CD**           | Jenkins                 | Pipeline de build, test e deploy   |
| **Runtime Python**  | uv + Python 3.12        | Gerenciamento de dependências      |
| **Banco de dados**  | PostgreSQL 16           | Dados relacionais (auth, sessões)  |
| **Cache**           | Redis 7                 | Embeddings, rate limiting          |
| **Vector store**    | LanceDB                 | Armazenado localmente em disco     |

## Docker Compose (Desenvolvimento)

O ambiente de desenvolvimento usa Docker apenas para PostgreSQL e Redis. O Vectora roda diretamente em Python local para facilitar o debug.

```yaml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: vectora
      POSTGRES_USER: vectora
      POSTGRES_PASSWORD: dev-password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U vectora"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --maxmemory 512mb --maxmemory-policy allkeys-lru
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

volumes:
  postgres_data:
```

Iniciar infraestrutura:

```bash
docker compose up -d postgres redis
uv run vectora serve
```

## CI/CD com Jenkins

O pipeline Jenkins é definido em `Jenkinsfile` na raiz do monorepo. Executa lint, testes e build em cada push para `master`.

Etapas do pipeline:

1. **Checkout** — clonar o repositório
2. **Lint** — `uv run ruff check .` e `uv run ruff format --check .`
3. **Test** — `uv run pytest tests/ -v --tb=short`
4. **Build Docker** — build da imagem de produção
5. **Deploy** — push para registro e restart do serviço

**[Ver CI/CD](./ci-cd/)**

## Multi-User

Para ambientes multi-usuário (times), o Vectora suporta deploy centralizado com autenticação RBAC. Cada usuário se autentica com JWT e opera dentro de suas permissões definidas.

**[Ver Multi-User](./multi-user/)**

## External Linking

| Conceito              | Recurso                   | Link                                                                                  |
| --------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| **Docker Compose**    | Compose file reference    | [docs.docker.com/compose/compose-file](https://docs.docker.com/compose/compose-file/) |
| **Jenkins**           | Jenkins documentation     | [jenkins.io/doc](https://www.jenkins.io/doc/)                                         |
| **uv**                | Python package manager    | [docs.astral.sh/uv](https://docs.astral.sh/uv/)                                       |
| **PostgreSQL Docker** | Official PostgreSQL image | [hub.docker.com/\_/postgres](https://hub.docker.com/_/postgres)                       |
| **Redis Docker**      | Official Redis image      | [hub.docker.com/\_/redis](https://hub.docker.com/_/redis)                             |
