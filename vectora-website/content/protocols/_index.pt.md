---
title: Protocols
slug: protocols
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - caching
  - chatgpt
  - claude
  - concepts
  - config
  - gemini
  - go
  - mcp
  - protocol
  - protocols
  - state
  - sub-agents
  - system
  - tools
  - typescript
  - vectora
  - zod
---

{{< lang-toggle >}}

> [!IMPORTANT] > **MCP é APENAS para Vectora Desktop**. Se você estiver usando Vectora Cloud (SaaS/HTTP API), use REST API ou integração específica (ChatGPT, Gemini). Este documento descreve protocolos de **Desktop**: MCP (to IDEs) e ACP (to agents).

O Vectora Desktop implementa dois protocolos de comunicação: MCP (Model Context Protocol) para integração com IDEs, e ACP (Agent Communication Protocol) para comunicação entre sub-agents. O Vectora Cloud usa HTTP API com OpenAPI schema.

O **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** atua como a camada de conformidade para todos os protocolos. Ele intercepta e valida se as chamadas de ferramentas e as trocas de mensagens entre agentes aderem às políticas estruturadas, garantindo que a comunicação seja segura e precisa.

## Protocolos Suportados

| Protocolo | Caso de Uso                          | Status | Docs              |
| --------- | ------------------------------------ | ------ | ----------------- |
| **MCP**   | Conexão com Claude Code, Cursor, Zed | Stable | [→ MCP](./mcp.md) |
| **ACP**   | Comunicação entre Vectora e agents   | Beta   | [→ ACP](./acp.md) |

## MCP (Model Context Protocol)

**O protocolo padrão para IDEs modernas.**

O MCP é um protocolo aberto desenvolvido pela Anthropic que permite que LLMs chamem ferramentas de um computador de forma estruturada. Vectora oferece 12 tools via MCP.

**Vantagens:**

- Nativo em Claude Code e Cursor (zero config a mais)
- Descoberta dinâmica de tools
- Schema validation (ZOD)
- Caching automático de resultados
- Latência <10ms (IPC local)

## ACP (Agent Communication Protocol)

**Para comunicação entre Vectora e agents customizados.**

ACP permite que múltiplos agents trabalhem juntos, compartilhando contexto e estado. Ideal para arquiteturas distribuídas onde Vectora é sub-agent de um sistema maior.

**Status:** Beta - Disponível para early adopters

## Qual Protocolo Usar?

- **Usando Claude Code / Cursor / Zed?** → **MCP**
- **Integrando com agent custom em Python/Node/Go?** → **MCP** ou REST API (beta)
- **Agent-to-agent communication?** → **ACP** (beta)

Veja [MCP](./mcp.md) para detalhes completos de implementação.

---

> Próximo: [MCP Specification](./mcp.md)

## External Linking

| Concept              | Resource                             | Link                                                                                   |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **Gemini AI**        | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**       | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **Zod**              | TypeScript-first schema validation   | [zod.dev/](https://zod.dev/)                                                           |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
