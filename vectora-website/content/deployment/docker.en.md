---
title: "Docker"
slug: docker
date: "2026-04-18T22:30:00-03:00"
type: docs
tags:
  - ai
  - build
  - cloud
  - concepts
  - deployment
  - docker
  - guardian
  - mcp
  - mongodb-atlas
  - protocol
  - security
  - system
  - tools
  - trust-folder
  - vector-search
  - vectora
  - yaml
---

{{< lang-toggle >}}

Docker is the simplest way to run Vectora Cloud in an isolated environment or on servers that do not have the Go runtime installed. For Vectora Desktop users, it is recommended to install the binary directly on your machine.

Using containers ensures consistency across different environments and simplifies the management of dependencies like MongoDB.

> [!NOTE] > **Docker images are primarily for Vectora Cloud**. Vectora Desktop is installed as a local binary (`vectora` CLI + Systray). If you want to run it in Docker for local development testing, use the `vectora:dev-desktop` (beta) image.

## Official Images

The project maintains three types of Docker images, each optimized for specific use cases.

1. **`vectora-cloud:latest`**: Optimized for cloud APIs and HTTP MCP Servers. It uses MongoDB-only data access and is intended for PRODUCTION environments.
2. **`vectora-cloud:dev`**: A development version with verbose logging and automatic reload features.
3. **`vectora:dev-desktop`** (beta): Desktop mode for testing in a container environment (not recommended for production use).
4. **`vectora-cloud:managed`**: Premium version that includes pre-loaded SmolLM models for the Vectora Cognitive Runtime.

> [!IMPORTANT] > **ONNX Runtime**: All official Vectora images include the ONNX runtime necessary for the **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** to function. This allows the tactical brain to perform local inferences within the container without external calls.

## Running Vectora Cloud with Docker Compose

The recommended way to run Vectora Cloud locally with all its dependencies is by using Docker Compose. This allows you to manage the Vectora service and the MongoDB database as a single unit.

```yaml
version: "3.8"
services:
  vectora-cloud:
    image: vectora-cloud:latest
    ports:
      - "8080:8080"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - VOYAGE_API_KEY=${VOYAGE_API_KEY}
      - VECTORA_DB_URL=mongodb://mongo:27017/vectora
      - VECTORA_MODE=cloud
    depends_on:
      - mongo
  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db
volumes:
  mongo-data:
```

## Image Selection Guide

Choose the appropriate image based on your deployment strategy and data access requirements.

| Use Case                    | Image                  | Protocol        | Data Storage          |
| :-------------------------- | :--------------------- | :-------------- | :-------------------- |
| **Cloud Production**        | `vectora-cloud:latest` | HTTP MCP Server | MongoDB Atlas         |
| **Local Cloud Development** | `vectora-cloud:dev`    | HTTP + stdio    | Local MongoDB         |
| **Desktop in Container**    | `vectora:dev-desktop`  | stdio MCP       | Filesystem + BadgerDB |

## Manual Build

You can build the images locally using the provided `Makefile`. Ensure you are at the repository root before running these commands.

```bash
# Build the Cloud image
make docker-build-cloud

# Build the Desktop dev image
make docker-build-desktop
```

## Key Differences Between Modes

Vectora operates differently depending on whether it is deployed in Cloud or Desktop mode.

### Vectora Cloud (HTTP Server)

In Cloud mode, Vectora runs as an HTTP MCP Server on port 8080. It interacts exclusively with MongoDB for data storage and provides tools for workspace management and semantic search. Security is enforced through the Guardian API and strict namespace isolation.

### Vectora Desktop (stdio Client)

Desktop mode runs as a stdio MCP client, accessing the local filesystem and using BadgerDB for caching. It provides tools for file I/O, globbing, and local shell commands. Security is managed via the Trust Folder system.

## External Linking

| Concept           | Resource                             | Link                                                                                                       |
| ----------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Docker**        | Docker Documentation                 | [docs.docker.com/](https://docs.docker.com/)                                                               |
| **MCP**           | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
