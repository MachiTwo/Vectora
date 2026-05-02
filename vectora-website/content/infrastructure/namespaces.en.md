---
title: "Namespaces"
slug: namespaces
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - cloud
  - concepts
  - config
  - embeddings
  - guardian
  - infrastructure
  - mcp
  - mongodb-atlas
  - namespaces
  - protocol
  - security
  - system
  - trust-folder
  - vector-search
  - vectora
  - yaml
---

{{< lang-toggle >}}

> [!NOTE] > **Namespaces is a feature of Vectora Cloud**. Vectora Desktop uses a **Trust Folder** (filesystem sandbox) instead of namespaces. If you are using the local Vectora CLI, see [Infrastructure → Trust Folder](./trust-folder.md).

Namespaces are **logical isolators** for vector indices within MongoDB Atlas. Each project, environment, or context runs in its own namespace, preventing results from different sources from contaminating each other.

By providing this isolation, Vectora ensures multi-tenant security and organizational clarity.

> [!IMPORTANT]
> A namespace acts like a "virtual database" within MongoDB Atlas Vector Search. Searches in one namespace NEVER return chunks from another, guaranteeing context isolation between different teams or projects.

## The Problem and the Solution

Without namespaces, a search for a common term like "login" could return results from dozens of different projects, leading to context leakage and making it impossible to manage indices per team.

With namespaces, search results are strictly isolated. A query for "login" returns results ONLY from the specific project namespace, allowing multiple teams to share a single MongoDB Atlas instance securely and efficiently.

## Naming & Conventions

Standardizing namespace names is essential for organization and automation in multi-tenant clusters.

### Recommended Pattern

It is best practice to follow a structured naming convention that includes the organization, project name, and environment.

```text
<org>-<project>-<environment>
```

**Examples:**

- `kaffyn-vectora-prod`
- `kaffyn-vectora-dev`
- `acme-backend-staging`

### Validation Rules

Namespaces must adhere to the following naming constraints to ensure compatibility with cloud infrastructure.

- Length: 3-63 characters.
- Characters: Lowercase letters, numbers, and hyphens `[a-z0-9-]`.
- Must start with a letter.
- No underscores, spaces, or special characters.

## Namespace Lifecycle

Managing a namespace involves its technical initialization, continuous indexing, and eventual secure data disposal.

### Creation Process

You can create a new namespace via the CLI or by defining it in your project configuration.

```bash
# Via CLI
vectora namespace create --name kaffyn-vectora-prod
```

When a namespace is created, MongoDB Atlas initializes a new collection and empty HNSW indices for embeddings, while the Guardian module registers the creation in the audit logs.

### Indexing and Search

Once created, the namespace accepts data chunks. Every chunk inserted into the system is tagged with its parent namespace. Consequently, every search request must specify the target namespace to ensure filtered and accurate results.

### Deletion & Cleanup

Deleting a namespace is a permanent action that cannot be undone. You can also reset the indices within a namespace if you need to perform a fresh indexing of the project.

## Multi-Tenancy Patterns

Namespaces allow for various isolation strategies depending on organizational requirements.

### Pattern 1: One Namespace per Project

This pattern provides complete isolation between projects, which is ideal for strictly separated teams or rigorous compliance requirements where data sharing between projects is strictly forbidden.

### Pattern 2: Environments in the Same Project

This is a common pattern where different namespaces represent development, staging, and production environments for the same project. It prevents development data from appearing in production search results.

### Pattern 3: Shared Services + Private Teams

In this architecture, some namespaces are shared (e.g., for general documentation or shared utilities) while other namespaces remain private to specific teams, allowing for a mix of shared and isolated context.

## Namespace Metrics & Observability

Observability is applied individually to each namespace, allowing for precise performance audits and usage tracking.

### Inspecting Health

You can retrieve detailed statistics for a specific namespace using the CLI.

```bash
vectora namespace info --name kaffyn-vectora-prod
```

The output includes the number of indexed chunks, the collection size on disk, search latency metrics (P99), and the total number of searches performed in the last 24 hours.

### Automated Alerts

The Agentic Framework can be configured to monitor namespace health and trigger alerts if latency exceeds thresholds or if indexing falls behind.

## Configuration Examples

Define your namespace settings in the `vectora.config.yaml` file to ensure the CLI and agents use the correct context.

```yaml
# vectora.config.yaml
project:
  name: "My Project"
  namespace: kaffyn-vectora-prod

# Advanced: Multiple namespaces
namespaces:
  default: kaffyn-vectora-prod
  fallback: kaffyn-vectora-backup
```

## External Linking

| Concept           | Resource                                                 | Link                                                                                                       |
| ----------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation                        | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**           | Model Context Protocol Specification                     | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)                               | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **Observability** | Control Theory and System Observability                  | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)                         |
| **HNSW**          | Efficient and robust approximate nearest neighbor search | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)                                               |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
