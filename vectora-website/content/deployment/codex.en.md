---
title: "Codex"
slug: codex
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - codex
  - concepts
  - config
  - deployment
  - gemini
  - integration
  - mcp
  - npm
  - openai
  - protocol
  - tools
  - vectora
  - voyage
---

{{< lang-toggle >}}

The Vectora integration with OpenAI Codex provides support for legacy code analysis models that are still used in specific automation pipelines. This integration acts as a translator between Vectora's context tools and the Codex completion interface, allowing older scripts to leverage the new semantic search engine.

Deployment of the Codex adapter is performed through a Node.js package that encapsulates API calls and ensures format compatibility between systems.

## Legacy Support and REST APIs

OpenAI Codex was a pioneer in AI code analysis, and many internal systems still depend on its response structure. Vectora Cloud exposes a compatibility endpoint that simulates Codex behavior but uses Gemini and Voyage models internally for higher precision.

This compatibility bridge is deployed as part of the core Vectora Cloud service, requiring no additional infrastructure beyond the main instance.

## Endpoint Configuration

For your legacy applications to use Vectora as if it were OpenAI Codex, you must change the API base URL in your SDK settings. Vectora emulates the original Codex `/completions` and `/edits` routes.

```javascript
const openai = new OpenAI({
  apiKey: "VECTORA_TOKEN",
  baseURL: "https://api.vectora.app/v1/adapters/codex",
});
```

## Publication via NPM

The Codex adapter client library for Vectora is published on NPM under the name `@kaffyn/vectora-codex-adapter`. It provides helpers to facilitate the migration of existing code to the Vectora ecosystem without the need for deep refactoring.

The publication of this package follows Vectora's standard continuous integration flow, ensuring that new search engine features are safely exposed to Codex.

## Limitations and Performance

While the adapter provides a compatibility layer, we recommend that new integrations use the MCP protocol or the native Gemini API directly. Codex mode has inherent limitations due to its fixed prompt format, which can reduce the effectiveness of dynamic search tools.

In terms of performance, the translation layer adds minimal latency (<20ms), making it viable for use in CI pipelines where format stability is more critical than absolute speed.

## External Linking

| Concept             | Resource                             | Link                                                                                   |
| ------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **OpenAI**          | OpenAI API Documentation             | [platform.openai.com/docs/](https://platform.openai.com/docs/)                         |
| **MCP**             | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**      | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Gemini AI**       | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**      | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **REST API Design** | RESTful API Best Practices           | [restfulapi.net/](https://restfulapi.net/)                                             |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
