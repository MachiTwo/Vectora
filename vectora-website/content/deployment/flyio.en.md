---
title: "Fly.io"
slug: flyio
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - chatgpt
  - cloud
  - concepts
  - config
  - deployment
  - embeddings
  - flyio
  - gemini
  - mcp
  - mongodb-atlas
  - persistence
  - protocol
  - rag
  - reference
  - security
  - vector-search
  - vectora
  - voyage
---

{{< lang-toggle >}}

Fly.io is the recommended platform for deploying Vectora Cloud due to its low global latency and native support for Docker containers. This deployment option is exclusive to the Cloud version of Vectora, allowing you to run a managed MCP server with automatic scaling.

By deploying on Fly.io, Vectora leverages edge infrastructure to ensure that vector searches and context processing are executed as close as possible to your users or your CI/CD infrastructure.

## Deployment Overview

Deployment on Fly.io uses the `fly.toml` file to define the service configuration and the `fly deploy` command to push the Docker image to the platform's servers.

Unlike Desktop mode, the Fly.io instance operates as an MCP server via HTTP, requiring an active connection to MongoDB Atlas for data persistence and vector storage.

## fly.toml Configuration

The `fly.toml` file in the project root must be configured to expose port 8080, which is the default port where Vectora Cloud listens for MCP connections.

```toml
app = "vectora-cloud"
primary_region = "gru"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 1
  processes = ["app"]

[env]
  VECTORA_MODE = "cloud"
```

## Secrets and Security

Since Vectora depends on AI providers (Google Gemini and Voyage AI), you must configure API keys as secrets in Fly.io to ensure they are not exposed in the source code.

Use the `fly secrets set` command to configure the mandatory variables:

```bash
fly secrets set GOOGLE_API_KEY=your_key_here
fly secrets set VOYAGE_API_KEY=your_key_here
fly secrets set VECTORA_DB_URL=mongodb+srv://user:pass@cluster.mongodb.net/vectora
```

## Deployment Process

Once the API keys and database URL are configured, you can deploy the application. Fly.io will build the Docker image using the `Dockerfile` present in the repository root.

```bash
# Start app configuration (first time only)
fly launch

# Deploy the new version
fly deploy
```

After deployment, your Vectora Cloud instance will be available at `https://vectora-cloud.fly.dev`, ready to receive connections from integrations like VS Code or ChatGPT.

## External Linking

| Concept           | Resource                             | Link                                                                                                       |
| ----------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**           | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **Gemini AI**     | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)                       |
| **Gemini API**    | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                                           |
| **Docker**        | Docker Documentation                 | [docs.docker.com/](https://docs.docker.com/)                                                               |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
