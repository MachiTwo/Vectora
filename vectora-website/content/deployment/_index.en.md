---
title: Deployment
slug: deployment
date: "2026-04-18T22:30:00-03:00"
type: docs
tags:
  - adk
  - agents
  - ai
  - chatgpt
  - claude
  - cloud
  - concepts
  - config
  - deployment
  - docker
  - embeddings
  - gemini
  - go
  - integration
  - mcp
  - mongodb
  - mongodb-atlas
  - openai
  - persistence
  - plugins
  - rag
  - reference
  - reranker
  - vector-search
  - vectora
  - voyage
---

{{< lang-toggle >}}

Vectora was designed to be deployed flexibly, from local machines to cloud-managed instances (Fly.io).

The `vectora-cloud` binary is optimized for container environments, removing graphical interface dependencies and focusing on API and search engine performance.

## Infrastructure Options

Choose the technological base to run or distribute the main Vectora engine:

- [**Fly.io**](./flyio.md): Recommended for cloud production with auto-scaling.
- [**Docker**](./docker.md): Ideal for isolated environments and containerized Desktop support.
- [**Homebrew**](./homebrew.md): Native installation and management for macOS users.
- [**GitHub Releases**](./github-releases.md): Manual binaries for Windows, Linux and macOS.
- **Native Binary**: For direct local use via CLI and Systray (Desktop).

## Integration Deployment

Each Vectora integration has its own deployment and publication flow:

- [**VS Code**](./vscode.md): Publication on Visual Studio Marketplace and Open VSX.
- [**ChatGPT**](./chatgpt.md): Plugin and Manifest configuration for OpenAI.
- [**Claude**](./claude.md): Integration via MCP and registration in Claude Desktop.
- [**Codex**](./codex.md): Deployment of the compatibility adapter via NPM.
- [**Gemini**](./gemini.md): Context bridge deployment on Google Cloud Run.

## Infrastructure Requirements

For a stable deployment, make sure you have:

- **MongoDB Atlas**: Recommended for vector and metadata persistence.
- **API Keys**: `GOOGLE_API_KEY` (Gemini) and `VOYAGE_API_KEY` (Voyage AI).
- **Vectora Cognitive Runtime (ONNX Runtime)**: The decision engine requires the ONNX runtime for low-latency local inference.
- **Resources**: Minimum 512MB RAM and 0.5 CPU per instance.

## External Linking

| Concept               | Resource                            | Link                                                                                                       |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation   | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Anthropic Claude**  | Claude Documentation                | [docs.anthropic.com/](https://docs.anthropic.com/)                                                         |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **Docker**            | Docker Documentation                | [docs.docker.com/](https://docs.docker.com/)                                                               |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/) and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
