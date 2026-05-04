---
title: Protocols
slug: protocols
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - concepts
  - fastapi
  - json-rpc
  - mcp
  - protocol
  - protocols
  - rest-api
  - acp
  - sub-agents
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

{{< section-toggle >}}

Vectora implementa três protocolos de comunicação: REST API (FastAPI endpoints HTTP padrão), MCP (Model Context Protocol para editores de AI) e JSON-RPC 2.0 (para integrações programáticas e editor plugins). Cada protocolo serve um caso de uso diferente.

## Protocolos Suportados

| Protocolo        | Caso de Uso                       | Status | Docs                          |
| ---------------- | --------------------------------- | ------ | ----------------------------- |
| **REST API**     | HTTP clients, scripts, CI/CD      | Stable | [Ver REST API](./rest-api.md) |
| **MCP**          | Claude Code, JetBrains, Zed       | Stable | [Ver MCP](./mcp.md)           |
| **JSON-RPC 2.0** | Editor plugins, integrações batch | Stable | [Ver JSON-RPC](./json-rpc.md) |
| **ACP**          | Agent-to-agent communication      | Beta   | [Ver ACP](./acp.md)           |

## REST API (FastAPI)

A REST API é o protocolo principal do Vectora. Exposta via FastAPI em `http://localhost:8000`, com documentação automática em `/docs` (Swagger UI) e `/redoc`.

Casos de uso:

- Scripts Python ou Shell
- CI/CD pipelines
- Integrações HTTP diretas
- Frontend React (via fetch ou axios)

**[Ver REST API](./rest-api.md)**

## MCP (Model Context Protocol)

MCP permite que editores de AI (Claude Code, JetBrains com plugin Vectora, Zed) chamem ferramentas do Vectora diretamente via stdin/stdout. Vectora expõe 8 ferramentas via MCP.

Casos de uso:

- VS Code + Claude Code
- JetBrains + plugin Vectora
- Zed + extensão Vectora
- Qualquer cliente MCP compatível

**[Ver MCP](./mcp.md)**

## JSON-RPC 2.0

JSON-RPC 2.0 é o protocolo para integrações programáticas com suporte a batch requests. Exposto em `/rpc`.

Casos de uso:

- Editor plugins (TypeScript, Kotlin)
- Batch queries em uma requisição
- Chamadas síncronas com controle explícito de ID

**[Ver JSON-RPC](./json-rpc.md)**

## ACP (Agent Communication Protocol)

ACP é usado para comunicação entre o agente principal e sub-agentes via stdin/stdout. Ideal para arquiteturas de multi-agent onde Vectora age como sub-agente especializado.

**Status:** Beta — disponível para integrações avançadas

**[Ver ACP](./acp.md)**

## Qual Protocolo Usar?

| Cenário                 | Protocolo Recomendado |
| ----------------------- | --------------------- |
| Claude Code / VS Code   | MCP                   |
| JetBrains / Zed         | MCP ou JSON-RPC       |
| Script Python/Shell     | REST API              |
| Frontend React          | REST API              |
| Multi-agent (sub-agent) | ACP                   |
| Batch queries           | JSON-RPC 2.0          |

## External Linking

| Conceito         | Recurso                              | Link                                                                                          |
| ---------------- | ------------------------------------ | --------------------------------------------------------------------------------------------- |
| **MCP**          | Model Context Protocol specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)        |
| **JSON-RPC 2.0** | JSON-RPC 2.0 specification           | [jsonrpc.org/specification](https://www.jsonrpc.org/specification)                            |
| **FastAPI**      | Modern Python web framework          | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)                                         |
| **OpenAPI**      | API specification format             | [swagger.io/specification](https://swagger.io/specification/)                                 |
| **ACP**          | Agent Communication Protocol         | [docs.langchain.com/oss/python/deepagents](https://docs.langchain.com/oss/python/deepagents/) |
