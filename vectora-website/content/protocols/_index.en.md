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
  - integration
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

> [!IMPORTANT] > **MCP is ONLY for Vectora Desktop**. If you are using Vectora Cloud (SaaS/HTTP API), use the REST API or specific integrations (ChatGPT, Gemini). This document describes **Desktop** protocols: MCP (to IDEs) and ACP (to agents).

Vectora Desktop implements two communication protocols: MCP (Model Context Protocol) for integration with IDEs, and ACP (Agent Communication Protocol) for communication between sub-agents. Vectora Cloud uses an HTTP API with an OpenAPI schema.

The **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** acts as the compliance layer for all protocols. It intercepts and validates whether tool calls and message exchanges between agents adhere to structured policies, ensuring communication is secure and precise.

## Supported Protocols

| Protocol | Use Case                                 | Status | Docs              |
| -------- | ---------------------------------------- | ------ | ----------------- |
| **MCP**  | Connection with Claude Code, Cursor, Zed | Stable | [→ MCP](./mcp.md) |
| **ACP**  | Communication between Vectora and agents | Beta   | [→ ACP](./acp.md) |

## MCP (Model Context Protocol)

**The standard protocol for modern IDEs.**

MCP is an open protocol developed by Anthropic that allows LLMs to call tools on a computer in a structured way. Vectora offers 12 tools via MCP.

**Advantages:**

- Native in Claude Code and Cursor (zero extra config)
- Dynamic tool discovery
- Schema validation (ZOD)
- Automatic result caching
- Latency <10ms (local IPC)

## ACP (Agent Communication Protocol)

**For communication between Vectora and custom agents.**

ACP allows multiple agents to work together, sharing context and state. Ideal for distributed architectures where Vectora is a sub-agent of a larger system.

**Status:** Beta - Available for early adopters

## Which Protocol to Use?

- **Using Claude Code / Cursor / Zed?** → **MCP**
- **Integrating with custom agent in Python/Node/Go?** → **MCP** or REST API (beta)
- **Agent-to-agent communication?** → **ACP** (beta)

See [MCP](./mcp.md) for full implementation details.

---

> Next: [MCP Specification](./mcp.md)

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

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/) and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
