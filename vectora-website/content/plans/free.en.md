---
title: "Free Plan"
slug: free
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - byok
  - concepts
  - config
  - desktop
  - embeddings
  - free
  - gemini
  - guardian
  - integration
  - mcp
  - open-source
  - pricing
  - protocol
  - rag
  - reranker
  - security
  - system
  - tools
  - troubleshooting
  - trust-folder
  - vectora
  - voyage
---

{{< lang-toggle >}}

> [!NOTE] > **Free Plan is for Vectora Desktop**. If you are looking for Vectora Cloud (SaaS), please see the Cloud Pricing section. Desktop Free is open-source and has no time limits, while Cloud tiers follow a subscription model.

The **Free** plan of Vectora is fully **open-source** and has no time expiration. You can use the Desktop version locally on any codebase without cost. It is designed for individual developers, small teams, educational projects, and rapid prototyping.

By using the Free plan, you maintain full control over your data while leveraging advanced AI-assisted code analysis.

## Desktop Free vs Cloud Tiers

The following table compares the local Desktop version with the various cloud-managed tiers offered by Vectora.

| Feature           | Desktop Free | Cloud Free    | Cloud Plus    | Cloud Team |
| :---------------- | :----------- | :------------ | :------------ | :--------- |
| **Installation**  | Local Binary | SaaS          | SaaS          | SaaS       |
| **Cost**          | Free         | Free\*        | $20/month     | Custom     |
| **Indexing**      | Unlimited    | Up to 10 docs | Unlimited     | Unlimited  |
| **Workspaces**    | 1 (Local)    | 1             | Unlimited     | Unlimited  |
| **Users**         | 1 (You)      | 1             | Up to 5       | Up to 100  |
| **Searches/day**  | Unlimited    | 100           | 10K           | Unlimited  |
| **External APIs** | With BYOK    | Limited       | Full (50K/mo) | Full       |
| **Protocol**      | stdio MCP    | HTTP API      | HTTP API      | HTTP API   |

_\*Cloud Free: 60 req/min Gemini, 50 req/min Voyage. BYOK = Bring Your Own Keys._

## What is Included (Desktop Free)

The Free tier provides access to the core engine of Vectora, enabling high-quality semantic analysis.

### Core Engine Features

- **Semantic Search**: Full access to vector-based code retrieval.
- **Dependency Analysis**: Advanced symbol relationship mapping.
- **Full Indexing**: No artificial limits on local project indexing.
- **Trust Folder & Guardian**: Standard security and sandbox features.
- **Full CLI Access**: Complete command-line tool suite.
- **Vectora Cognitive Runtime (Decision Engine)**: Local tactical brain via ONNX Runtime for routing and orchestration.
- **Agentic Framework**: Integrated support for autonomous agents.

### IDE & Platform Support

- **Claude Code (MCP)**: Native integration via stdio.
- **Cursor (MCP)**: Full support for the AI-enhanced editor.
- **VS Code Extension**: Access to the dedicated semantic search panel.
- **Vectora CLI**: Complete control over your project index.

## AI Models (BYOK)

In the Free plan, you bring your own API keys for the major AI providers, allowing you to use your existing credits or free tiers.

| Component     | Recommended Option  | Cost   |
| :------------ | :------------------ | :----- |
| **Embedding** | Voyage 4            | Free\* |
| **Reranking** | Voyage Rerank 2.5   | Free\* |
| **LLM**       | Gemini 1.5 Flash    | Free\* |
| **Local**     | Ollama (all-MiniLM) | Free   |

_\*Free tiers from providers typically have limits: 60 req/min for Gemini and 50 req/min for Voyage._

## Usage Limits & Performance

While indexing is unlimited, the local server is optimized for single-user development workflows.

### System Limits

- **Concurrent Users**: 1 (optimized for single developer).
- **Searches per Day**: 1,000 (recommended local threshold).
- **Embeddings Cache**: 500MB local storage.
- **Logs Retention**: 30 days of audit history.

### Performance Targets

- **Search Latency**: Typically <2s for local queries.
- **Max File Size**: 100MB per file for indexing.
- **Max Chunks per Search**: Returns up to 20 relevant snippets.

## Getting Started

Follow these quick steps to get Vectora up and running on your local machine.

### Installation

```bash
npm install -g @kaffyn/vectora

# Verify installation
vectora --version
```

### Initial Setup

1. **Initialize Project**: Navigate to your project root and run `vectora init --name "My Project"`.
2. **Obtain Keys**: Get your free keys from Google AI Studio and Voyage AI.
3. **Configure**: Use `vectora config set` to provide your API keys to the system.
4. **Index**: Run `vectora index` to build your first semantic map.
5. **Search**: Start querying with `vectora search "How does login work?"`.

## Troubleshooting

If you encounter issues during use, consider the following common scenarios.

### "Quota Exceeded"

This means you have reached the monthly free limit of your AI provider (Gemini or Voyage). You can wait for the reset on the first of the month or upgrade your provider account.

### "Rate Limit Exceeded"

You have made too many requests in a single minute. Try adding a small delay between your queries or automated scripts.

### "Concurrent Users Exceeded"

The Free tier is designed for a single active instance (one IDE or one CLI process at a time). Ensure you don't have multiple editors trying to access the same local server simultaneously.

## External Linking

| Concept               | Resource                             | Link                                                                                   |
| --------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **Voyage AI**         | High-performance embeddings for RAG  | [www.voyageai.com/](https://www.voyageai.com/)                                         |
| **Voyage Embeddings** | Voyage Embeddings Documentation      | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)         |
| **Voyage Reranker**   | Voyage Reranker API                  | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)             |
| **Gemini AI**         | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**        | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **MCP**               | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
