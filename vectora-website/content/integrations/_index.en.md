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

Connect Vectora with your favorite tools and IDEs. Choose between generic integration (MCP Protocol) or proprietary apps with customized UX.

## Which Integration to Choose?

| IDE/App          | Recommendation           | Setup Time | Mode    | Docs                                                          |
| ---------------- | ------------------------ | ---------- | ------- | ------------------------------------------------------------- |
| **Claude Code**  | Native MCP               | 1 min      | Desktop | [MCP Protocol](./mcp-protocol.md)                             |
| **Cursor**       | Native MCP               | 1 min      | Desktop | [MCP Protocol](./mcp-protocol.md)                             |
| **Zed**          | Native MCP               | 2 min      | Desktop | [MCP Protocol](./mcp-protocol.md)                             |
| **VS Code**      | Extension Native UI      | 2 min      | Desktop | [VS Code Extension](./vscode-extension.md)                    |
| **ChatGPT**      | Custom GPT Plugin        | 5 min      | Cloud   | [ChatGPT Plugin](./chatgpt-plugin.md)                         |
| **Paperclip AI** | Multi-Agent Orchestrator | 3 min      | Cloud   | [Paperclip Plugin](./paperclip.md)                            |
| **Gemini**       | REST API or CLI          | 3 min      | Both    | [Gemini API](./gemini-api.md) / [Gemini CLI](./gemini-cli.md) |
| **Custom Agent** | REST API (beta)          | 5 min      | Cloud   | [Custom Agents](./custom-agents.md)                           |

> [!TIP] > **Desktop**: Vectora CLI installed locally + MCP stdio protocol for IDEs.
> **Cloud**: Vectora SaaS (HTTP API) running in the cloud, accessible via REST.
> **Both**: Works in both modes (e.g. Gemini can use Desktop or Cloud backend).

## Generic Integration

## MCP (Model Context Protocol)

**Best for**: Modern IDEs (Claude Code, Cursor, Zed)

Open standard protocol that allows IDEs to call tools from the computer. Vectora offers 12 tools via MCP.

- Setup: 1-2 lines in the IDE config
- Latency: <10ms (local IPC)
- Discovery: Automatic tool discovery

[→ MCP Protocol](./mcp-protocol.md)

## Custom UI Integrations

## VS Code Extension

**Best for**: VS Code developers

Native UI with sidebar, integrated commands, and syntax highlighting for found code.

[→ VS Code Extension](./vscode-extension.md)

## ChatGPT Plugin

**Best for**: Using Vectora inside ChatGPT

Custom GPT Plugin with support for analysis, documentation, and code review via ChatGPT.

[→ ChatGPT Plugin](./chatgpt-plugin.md)

## Gemini API Integration

**Best for**: Workflows with Google Gemini

REST + CLI integration for code analysis, review, and generation with Vectora context.

[→ Gemini API](./gemini-api.md)

## Advanced Integrations

## Paperclip Plugin

**Best for**: Multi-Agent Orchestration

Native integration of events and context (Vectora Cognitive Runtime) for Paperclip AI workflows.

[→ Paperclip Plugin](./paperclip.md)

## Custom Agents & REST API

Build agents in Python, Node.js, Go, or any language. Call Vectora via REST API (beta).

[→ Custom Agents](./custom-agents.md)

## Quick Start by Use Case

**"I want to use it in Claude Code"**
→ [MCP Protocol Quickstart](../getting-started/quickstart-mcp.md)

**"I want to use it in VS Code"**
→ [VS Code Extension](./vscode-extension.md)

**"I want to integrate it into my app"**
→ [Custom Agents](./custom-agents.md)

**"I want to use it with ChatGPT"**
→ [ChatGPT Plugin](./chatgpt-plugin.md)

---

> Didn't find your IDE? [Open an Issue](https://github.com/Kaffyn/Vectora/issues)

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

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/) and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
