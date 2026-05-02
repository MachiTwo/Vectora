---
title: Paperclip Integration
slug: paperclip
description: Vectora plugin for multi-agent orchestration with Paperclip
keywords: [paperclip, agent orchestration, integration, plugin, vectora]
tags: [integration, plugin, orchestration, paperclip, ai-agent]
---

{{< lang-toggle >}}

The **Paperclip Integration** connects the Vectora Decision Engine (Vectora Cognitive Runtime) to Paperclip, an open-source multi-agent AI orchestration platform. Through the `@vectora/plugin-paperclip` plugin, Vectora Cognitive Runtime functions as an intelligent policy orchestrator within Paperclip-managed multi-agent environments.

## Integration Architecture

```text
Paperclip Agent (orchestrates)
    ↓
[Vectora Cognitive Runtime Policy Router] ← Make intelligent routing decisions
    ↓
[Vectora Tools]
  - vectora_search (semantic search)
  - vectora_explain (code explanation)
  - vectora_suggest (AI-powered suggestions)
  - vectora_health_check (monitoring)
    ↓
[Decision Log] ← Auditable, structured JSON
```

## Core Components

### 1. Plugin Manifest

The `src/manifest.ts` file declares:

- **ID**: `@vectora/plugin-paperclip`
- **Version**: 0.1.0
- **Capabilities**: agent.tools.register, http.outbound, events.subscribe, ui.dashboardWidget, state, activity.log.write

### 2. Worker RPC

The `src/worker.ts` implements handlers for:

- Initialization with configuration validation
- Tool registration
- Event subscription (task.created, task.completed)
- Bidirectional context synchronization

### 3. Registered Tools

#### vectora_search

Semantic search in the Vectora knowledge base with context support.

**Input:**

```typescript
{
  query: string; // Required: search query
  context?: string; // Optional: context to guide search
  top_k?: number; // Optional: number of results (default: 5)
}
```

**Output:**

```typescript
{
  results: [{
    id: string;
    content: string;
    score: number;
    metadata?: Record<string, unknown>;
  }];
  total: number;
  query: string;
}
```

#### vectora_explain

Detailed explanation of code snippets.

**Input:**

```typescript
{
  code: string; // Required: code to explain
  language?: string; // Optional: language (typescript, python, go, etc)
}
```

**Output:**

```typescript
{
  explanation: string;
  complexity: "simple" | "moderate" | "complex";
  language: string;
  estimatedReadTime: number;
}
```

#### vectora_suggest

AI-powered code completion suggestions.

**Input:**

```typescript
{
  partial: string; // Required: partial code
  count?: number; // Optional: number of suggestions (default: 3)
}
```

**Output:**

```typescript
[{
  code: string;
  description: string;
  confidence: number;
}]
```

#### vectora_health_check

Vectora Cognitive Runtime health status and connectivity.

**Output:**

```typescript
{
  healthy: boolean;
  timestamp: string;
  apiUrl: string;
  latency: number;
}
```

## Configuration

The plugin requires the following variables:

| Field               | Type    | Required | Default | Description                             |
| ------------------- | ------- | -------- | ------- | --------------------------------------- |
| `vectora_api_url`   | string  | Yes      | -       | Base URL of Vectora API                 |
| `vectora_api_key`   | string  | Yes      | -       | Authentication token                    |
| `auto_sync_context` | boolean | No       | true    | Automatically sync context              |
| `decision_logging`  | boolean | No       | true    | Log Vectora Cognitive Runtime decisions |
| `agent_timeout_ms`  | number  | No       | 30000   | Timeout for operations (5000-120000)    |

### Initialization Example

```typescript
import { worker } from "@vectora/paperclip";

await worker.init({
  vectora_api_url: "https://api.vectora.cloud",
  vectora_api_key: process.env.VECTORA_API_KEY,
  auto_sync_context: true,
  decision_logging: true,
  agent_timeout_ms: 30000,
});
```

## Context Synchronization

The integration provides **bidirectional** synchronization between:

- **Paperclip Projects** (orchestrator side)
- **Vectora Namespaces** (knowledge base side)

When enabled (`auto_sync_context: true`):

1. Paperclip project context is captured
2. Mapped to Vectora namespace
3. Metadata and embeddings synchronized
4. Operations logged for audit trail

### Synchronized Data Structure

```typescript
interface ContextSyncData {
  projectId: string;
  namespace: string;
  metadata: Record<string, unknown>;
  lastSyncAt: string;
}
```

## Decision Logging

When `decision_logging: true`, each Vectora Cognitive Runtime decision is logged with structure:

```json
{
  "traceId": "vectora-cognitive-runtime_20260427_abc123",
  "timestamp": "2026-04-27T15:30:01Z",
  "decision": {
    "action": "dispatch_to_gemini",
    "target": "gemini",
    "parameters": {
      "temperature": 0.2,
      "max_tokens": 1500
    },
    "confidence": 0.91
  },
  "observation": {
    "contextSufficiency": 0.94,
    "hallucinationRisk": 0.07
  }
}
```

Logs are:

- Written to Paperclip's activity log
- Persisted for post-implementation analysis
- Available via audit API
- Encrypted at rest

## Monitoring and Observability

### Health Checks

The plugin provides health checks via `vectora_health_check`:

```typescript
const health = await worker.healthCheck();

if (health.healthy) {
  console.log(`Latency: ${health.latency}ms`);
}
```

**Tracked metrics:**

- Vectora API connectivity
- Inference latency
- Operation success rate
- Errors by type

### Monitored Events

The plugin subscribes to Paperclip events:

- `agent.task.created` - New task created
- `agent.task.completed` - Task completed

## Troubleshooting

### Plugin fails to initialize

Check:

1. Vectora API URL is correct and accessible
2. API key has valid permissions
3. Network connectivity to Vectora Cloud
4. Configuration matches schema

### Tool calls timeout

If `agent_timeout_ms` is exceeded:

1. Increase timeout (up to 120000ms)
2. Check network latency
3. Check API Vectora status at `/health/ready`

### Context sync failures

Ensure:

1. `auto_sync_context` is enabled
2. Project IDs match Vectora namespace IDs
3. Sufficient permissions in API key
4. Disk space available

## Use Cases

### Multi-Agent Company with Vectora Cognitive Runtime

```typescript
// Paperclip orchestrates multiple agents
// Vectora Cognitive Runtime as policy coordinator (intelligent router)
const company = await paperclip.createCompany({
  name: "AI Engineering Team",
  agents: [
    { role: "code_reviewer", model: "gemini" },
    { role: "architect", model: "voyage" },
    { role: "tester", model: "claude" },
  ],
  policyCoordinator: vectoraVectora Cognitive Runtime,
});

// Vectora Cognitive Runtime automatically decides which agent to use based on query
```

### Search Augmentation Workflow

```typescript
// User query
const query = "how to validate JWT in Go?";

// Vectora Cognitive Runtime enriches with search
const searchResults = await worker.vectoraSearch(query, "security context", 5);

// Pass to Gemini with augmented context
const response = await gemini.generate({
  prompt: query,
  context: searchResults.results.map((r) => r.content).join("\n"),
});
```

### Code Generation with Suggestions

```typescript
// User partial code
const partial = "const validateEmail = (email: string) => {";

// Vectora Cognitive Runtime suggests completions
const suggestions = await worker.vectoraSuggest(partial, 3);

// Present options to user
suggestions.forEach((s) => {
  console.log(` ${s.code} (confidence: ${s.confidence})`);
});
```

## Future Roadmap

### Phase 10: Continuous Training Loop

- Automatic production trace collection
- Monthly retraining with new data
- A/B testing of new policies

### Phase 11: Real-Time Observability

- Grafana dashboard with Vectora Cognitive Runtime metrics
- Automatic alerts (hallucination_rate > 5%)
- Breakdown by decision_type

### Phase 12: Multi-Tenant Policy Variants

- Custom policies per enterprise customer
- Domain-specific fine-tuning (healthcare, finance)

## External Linking

| Concept             | Resource                                | Link                                                                                   |
| ------------------- | --------------------------------------- | -------------------------------------------------------------------------------------- |
| **TypeScript**      | Official TypeScript Handbook            | [www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)                   |
| **Gemini AI**       | Google DeepMind Gemini Models           | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**      | Google AI Studio Documentation          | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **Observability**   | Control Theory and System Observability | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)     |
| **JWT**             | RFC 7519: JSON Web Token Standard       | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519) |
| **REST API Design** | RESTful API Best Practices              | [restfulapi.net/](https://restfulapi.net/)                                             |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
