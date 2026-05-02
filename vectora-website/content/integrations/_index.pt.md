---
title: Integrations
slug: integrations
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - chatgpt
  - claude
  - concepts
  - config
  - gemini
  - gemini-cli
  - go
  - integration
  - integrations
  - mcp
  - nodejs
  - openai
  - plugins
  - protocol
  - tools
  - vectora
  - vscode
---

{{< lang-toggle >}}

Conecte Vectora com suas ferramentas e IDEs preferidas. Escolha entre integração genérica (MCP Protocol) ou apps proprietários com UX customizada.

## Qual Integração Escolher?

| IDE/App          | Recomendação              | Tempo Setup | Modo    | Docs                                                          |
| ---------------- | ------------------------- | ----------- | ------- | ------------------------------------------------------------- |
| **Claude Code**  | MCP Nativo                | 1 min       | Desktop | [MCP Protocol](./mcp-protocol.md)                             |
| **Cursor**       | MCP Nativo                | 1 min       | Desktop | [MCP Protocol](./mcp-protocol.md)                             |
| **Zed**          | MCP Nativo                | 2 min       | Desktop | [MCP Protocol](./mcp-protocol.md)                             |
| **VS Code**      | Extension Native UI       | 2 min       | Desktop | [VS Code Extension](./vscode-extension.md)                    |
| **ChatGPT**      | Plugin Custom GPT         | 5 min       | Cloud   | [ChatGPT Plugin](./chatgpt-plugin.md)                         |
| **Paperclip AI** | Orquestrador Multi-Agente | 3 min       | Cloud   | [Paperclip Plugin](./paperclip.md)                            |
| **Gemini**       | API REST ou CLI           | 3 min       | Both    | [Gemini API](./gemini-api.md) / [Gemini CLI](./gemini-cli.md) |
| **Agent Custom** | REST API (beta)           | 5 min       | Cloud   | [Custom Agents](./custom-agents.md)                           |

> [!TIP] > **Desktop**: Vectora CLI instalado localmente + MCP stdio protocol para IDEs.
> **Cloud**: Vectora SaaS (HTTP API) rodando na nuvem, acessível via REST.
> **Both**: Funciona em ambos os modos (ex: Gemini pode usar Desktop ou Cloud backend).

## Integração Genérica

## MCP (Model Context Protocol)

**Melhor para**: IDEs modernas (Claude Code, Cursor, Zed)

Protocolo padrão aberto que permite que IDEs chamem tools do computador. Vectora oferece 12 tools via MCP.

- Setup: 1-2 linhas no config da IDE
- Latência: <10ms (IPC local)
- Descoberta: Automática de tools

[→ MCP Protocol](./mcp-protocol.md)

## Integrações com UI Customizada

## VS Code Extension

**Melhor para**: Desenvolvedores VS Code

UI nativa com sidebar, comandos integrados, syntax highlighting de código encontrado.

[→ VS Code Extension](./vscode-extension.md)

## ChatGPT Plugin

**Melhor para**: Usar Vectora dentro do ChatGPT

Custom GPT Plugin com suporte a análise, documentação, code review via ChatGPT.

[→ ChatGPT Plugin](./chatgpt-plugin.md)

## Gemini API Integration

**Melhor para**: Workflows com Google Gemini

Integração REST + CLI para análise de código, revisão, geração com contexto Vectora.

[→ Gemini API](./gemini-api.md)

## Integrações Avançadas

## Paperclip Plugin

**Melhor para**: Orquestração Multi-Agente

Integração nativa de eventos e contexto (Vectora Cognitive Runtime) para workflows do Paperclip AI.

[→ Paperclip Plugin](./paperclip.md)

## Custom Agents & REST API

Construa agents em Python, Node.js, Go ou qualquer linguagem. Chame Vectora via REST API (beta).

[→ Custom Agents](./custom-agents.md)

## Quick Start por Caso de Uso

**"Quero usar em Claude Code"**
→ [MCP Protocol Quickstart](../getting-started/quickstart-mcp.md)

**"Quero usar em VS Code"**
→ [VS Code Extension](./vscode-extension.md)

**"Quero integrar em meu app"**
→ [Custom Agents](./custom-agents.md)

**"Quero usar com ChatGPT"**
→ [ChatGPT Plugin](./chatgpt-plugin.md)

---

> Não achou sua IDE? [Abra uma Issue](https://github.com/Kaffyn/Vectora/issues)

## External Linking

| Concept              | Resource                             | Link                                                                                   |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Gemini AI**        | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**       | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **REST API Design**  | RESTful API Best Practices           | [restfulapi.net/](https://restfulapi.net/)                                             |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
