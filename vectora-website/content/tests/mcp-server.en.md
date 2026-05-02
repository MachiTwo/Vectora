---
title: "Test Suite: MCP Server"
slug: mcp-server-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - compliance
  - concepts
  - errors
  - json-rpc
  - mcp
  - protocol
  - testing
  - tools
  - vectora
---

{{< lang-toggle >}}

The MCP server must be robust, fast, reliable, and 100% compliant with the JSON-RPC 2.0 specification. It must support concurrent requests, large payloads, and graceful error recovery. This suite validates the complete implementation of the Model Context Protocol in Vectora.

By verifying protocol compliance, we ensure that Vectora integrates seamlessly with a wide range of external agents and tools.

**Coverage**: 80+ tests | **Priority**: ALTA

## Test Segments

The following sections detail the specific test cases and scenarios covered by this suite.

### 1. JSON-RPC 2.0 Compliance (20 tests)

Ensures that the server strictly adheres to the JSON-RPC 2.0 standard for all communication.

- **Valid Request Format**: Confirms that correctly formatted requests are parsed and responded to with matching IDs.
- **Invalid Request Rejection**: Verifies that malformed requests are rejected with the correct error codes (-32600).
- **Notification Handling**: Ensures that requests without an ID are processed correctly without a response.
- **Batch Requests**: Validates that multiple requests in a single payload are processed and returned in an array.

### 2. Tool Operations (25 tests)

Validates the core functionality of exposing and invoking tools through the MCP interface.

- **Tool Discovery**: Confirms that `tools/list` returns the correct schemas, descriptions, and parameter sets for all tools.
- **Tool Invocation**: Verifies that `tools/call` triggers the intended logic and returns results in the specified format.
- **Parameter Validation**: Ensures that incorrect parameter types or missing required parameters trigger validation errors.

### 3. Performance & Concurrency (15 tests)

Monitors the responsiveness and stability of the server under various load conditions.

- **Low Latency Response**: Targets an average response time of less than 100ms for simple requests.
- **Concurrent Requests**: Validates that the server can handle 10+ simultaneous requests without performance degradation.
- **Large Payload Handling**: Ensures that large JSON payloads (up to 10MB) are processed correctly without memory leaks.

### 4. Reliability & Resilience (20 tests)

Tests the server's ability to maintain operations and recover from unexpected conditions.

- **Connection Resilience**: Verifies that the server detects intermittent network issues and allows for reconnection.
- **Error Recovery**: Ensures that a failure in a single tool call does not crash the entire server process.
- **Graceful Degradation**: Confirms that if one tool becomes unavailable, others continue to function correctly.

## Performance SLAs

The following table summarizes the performance targets for the MCP server.

| Metric                  | Target  |
| :---------------------- | :------ |
| **p50 Latency**         | < 50ms  |
| **p95 Latency**         | < 200ms |
| **p99 Latency**         | < 500ms |
| **Concurrent Requests** | 100+    |
| **Success Rate**        | 99.9%   |

## Execution Guide

To run the MCP server compliance and performance tests, use the following commands:

```bash
# Run all MCP tests
go test -v ./tests/mcp-server/...

# Run JSON-RPC compliance specifically
go test -v -run JSONRPCCompliance ./tests/mcp-server/...

# Run with race detection
go test -v -race ./tests/mcp-server/...
```

## External Linking

| Concept        | Resource                             | Link                                                                                   |
| -------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**        | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK** | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **JSON-RPC**   | JSON-RPC 2.0 Specification           | [www.jsonrpc.org/specification](https://www.jsonrpc.org/specification)                 |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
