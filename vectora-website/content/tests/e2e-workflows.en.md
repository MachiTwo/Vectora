---
title: "Test Suite: End-to-End Workflows"
slug: e2e-workflows
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - auth
  - concepts
  - e2e
  - embeddings
  - errors
  - gemini
  - integration
  - mcp
  - mongodb-atlas
  - persistence
  - protocol
  - system
  - testing
  - tools
  - vector-search
  - vectora
  - workflows
---

{{< lang-toggle >}}

Complete end-to-end workflows must function correctly from initialization to final output, traversing multiple components and integrations without failure. This suite validates real-world user scenarios across the entire Vectora stack, ensuring that the system behaves as expected for the end user.

By testing the full lifecycle of a request, we ensure that individual components interact correctly and meet our performance targets.

**Coverage**: 100+ tests | **Priority**: ALTA

## Gemini CLI Complete Flow

Ensures that users can interact with Vectora seamlessly through the Gemini command-line interface.

- CLI initialization and authentication (8 tests)
- Querying Vectora context through Gemini (10 tests)
- Multi-turn conversation persistence (8 tests)
- Context awareness across session restarts (8 tests)
- Graceful error recovery on network failure (5 tests)

**SLA**: Complete query response in < 3 seconds.

## VS Code Extension Workflow

Validates the integrated development environment experience, ensuring tools are available right where the code is.

- Extension initialization and sidebar loading (8 tests)
- Code selection and contextual search (10 tests)
- Inline result display and navigation (8 tests)
- Application of suggested improvements/refactors (8 tests)
- Workflows spanning multiple open files (8 tests)

**SLA**: Results displayed in < 500ms from selection.

## MCP Protocol Flow

Tests the reliability of the Model Context Protocol implementation for external agent integration.

- Client connection and session establishment (8 tests)
- Tool listing and schema validation (5 tests)
- Tool invocation with various parameter sets (10 tests)
- Result delivery and serialization (8 tests)
- JSON-RPC error handling and protocol compliance (8 tests)

**SLA**: Tool invocation response in < 1 second.

## Data Persistence & Sync Flow

Ensures that data is correctly managed across local and cloud environments.

- Embedding creation and local storage (10 tests)
- Local cache hit/miss logic (8 tests)
- Background synchronization to MongoDB Atlas (8 tests)
- Offline query capability and later reconciliation (8 tests)

**SLA**: Sync completes in < 5s for 100+ documents.

## Multi-step Complex Queries

Tests the system's ability to handle advanced requests that require coordination between multiple tools.

- Deep dependency analysis and visualization (8 tests)
- Related test discovery for specific code blocks (8 tests)
- Automatic documentation generation from context (8 tests)
- Improvement suggestions based on project patterns (8 tests)

**SLA**: Complex query results delivered in < 2 seconds.

## E2E Service Level Agreements (SLAs)

The following table summarizes our performance targets for key user workflows.

| Workflow           | Target          |
| :----------------- | :-------------- |
| **CLI Query**      | < 3s (total)    |
| **VS Code Search** | < 500ms         |
| **MCP Tool Call**  | < 1s            |
| **Cache Sync**     | < 5s (100 docs) |
| **Complex Query**  | < 2s            |

## Testing Approach & Scenarios

Our E2E tests cover both "happy path" scenarios and various edge cases to ensure robustness.

- **Tools Used**: Integration testing with mocked providers, UI testing with Playwright for VS Code, and JSON-RPC compliance tests for MCP.
- **Scenarios**:
  - Partial failures (e.g., one secondary component offline).
  - Intermittent network connectivity.
  - Expired or invalid authentication tokens.
  - Rate limit and quota exhaustion handling.
  - Concurrent data modifications and conflict resolution.

## External Linking

| Concept           | Resource                             | Link                                                                                                       |
| ----------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**           | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **Gemini AI**     | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)                       |
| **Gemini API**    | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                                           |
| **JSON-RPC**      | JSON-RPC 2.0 Specification           | [www.jsonrpc.org/specification](https://www.jsonrpc.org/specification)                                     |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
