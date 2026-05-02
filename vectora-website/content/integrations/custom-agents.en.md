---
title: Custom Agents
slug: custom-agents
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - auth
  - concepts
  - custom
  - go
  - integration
  - json
  - jwt
  - mcp
  - nodejs
  - protocol
  - reference
  - vectora
---

{{< lang-toggle >}}

Integrate Vectora with custom agents in Python, Node.js, Go, or any language that supports HTTP.

## Integration Options

| Method         | Use Case                              | Complexity |
| -------------- | ------------------------------------- | ---------- |
| **MCP**        | Agent runs locally in Go/Rust         | [x]        |
| **REST API**   | Remote agent in Python/Node/Go        | [x]        |
| **ACP (Beta)** | Distributed inter-agent communication | Beta       |

## REST API (Recommended to Start)

Vectora exposes a REST API (beta) that any agent can call:

```bash
curl -X POST https://vectora.app/api/search \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How to validate JWT tokens?",
    "namespace": "your-project",
    "top_k": 5
  }'
```

## MCP for Custom Agents

If your agent is written in Go/Rust, you can use MCP directly:

```text
Your Agent (Python/Node) ↔ MCP Client ↔ Vectora MCP Server
```

See [MCP Integration](./mcp-protocol.md) for details.

## Get Started

1. Obtain an **API token** at console.vectora.app
2. Configure your agent to call `/api/search`
3. Test locally with `curl`
4. Integrate into your workflow

## Full Reference

- REST API Reference (beta): `/api/docs`
- MCP Spec: [Model Context Protocol](https://modelcontextprotocol.io)
- ACP (Beta): [GitHub Discussions](https://github.com/Kaffyn/Vectora/discussions)

---

> Need a specific integration? [Open an Issue](https://github.com/Kaffyn/Vectora/issues)

## External Linking

| Concept              | Resource                             | Link                                                                                   |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **REST API Design**  | RESTful API Best Practices           | [restfulapi.net/](https://restfulapi.net/)                                             |
| **JWT**              | RFC 7519: JSON Web Token Standard    | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519) |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/), and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
