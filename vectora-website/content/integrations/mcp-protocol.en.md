---
title: "Model Context Protocol (MCP): Connect Vectora to Any IDE"
slug: mcp-protocol
date: "2026-04-19T10:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - chatgpt
  - claude
  - concepts
  - config
  - cursor
  - embeddings
  - errors
  - gemini
  - ide
  - mcp
  - mongodb-atlas
  - protocol
  - system
  - tools
  - troubleshooting
  - vector-search
  - vectora
---

{{< lang-toggle >}}

The **Model Context Protocol (MCP)** is an open standard that enables IDEs and AI applications to connect with external tool servers via **JSON-RPC 2.0 over stdio**. By using MCP, Vectora can provide deep codebase context to various AI agents running in your local development environment.

This protocol ensures that your tools and context are decoupled from specific AI models, allowing for a more flexible and modular development workflow.

> [!NOTE] > **MCP is specifically for Vectora Desktop**:
>
> - **Desktop Mode (MCP stdio)**: Runs locally with ultra-low latency (<10ms) and full access to your filesystem and local MongoDB instance.
> - **Cloud Mode (HTTP API)**: A managed SaaS service for integrations with web-based platforms like ChatGPT and the Gemini API.

## How It Works: The MCP Flow

The MCP architecture uses standard input/output (stdio) for communication, creating a secure and performant bridge between your IDE and the Vectora server.

```mermaid
graph LR
    A[User writes in IDE] -->|@vectora search_context| B[IDE]
    B -->|JSON-RPC 2.0 via stdio| C["Vectora MCP Server<br/>(local process)"]
    C -->|Query embedding| D["MongoDB Atlas<br/>Vector Search"]
    D -->|Relevant chunks| C
    C -->|Tool result JSON| B
    B -->|Show in context| A
```

### Communication Sequence

1. **IDE Startup**: The IDE reads the MCP configuration and launches the Vectora server via `vectora mcp --stdio`.
2. **Handshake & Discovery**: A JSON-RPC handshake occurs, where Vectora reveals its available tools (e.g., `search_context`, `analyze_dependencies`).
3. **Tool Execution**: When the user triggers a command, the IDE sends a request to Vectora, which processes the search and returns the results for display in the IDE.

## Step-by-Step Setup by IDE

Configuration varies slightly depending on which AI-enhanced editor you are using.

### IDE 1: Claude Code (Recommended)

1. **Prerequisites**: Ensure Claude Code and the Vectora CLI are installed globally.
2. **Locate Configuration**: Find your `claude_desktop_config.json` file. On Windows, this is typically in `%APPDATA%\Claude\`.
3. **Add Vectora Server**: Edit the file to include the Vectora MCP configuration with your environment variables.

```json
{
  "mcpServers": {
    "vectora": {
      "command": "vectora",
      "args": ["mcp", "--stdio"],
      "env": {
        "GEMINI_API_KEY": "your-key",
        "VOYAGE_API_KEY": "your-key",
        "VECTORA_NAMESPACE": "your-project"
      }
    }
  }
}
```

### IDE 2: Cursor

1. **Locate Configuration**: Navigate to the Cursor settings directory (typically `%APPDATA%\Cursor\User\`).
2. **Configure**: Use the same JSON structure as the Claude Code setup.
3. **Restart**: Fully close and reopen Cursor to initialize the connection.

## 12 Available MCP Tools

Vectora exposes a comprehensive suite of tools via the MCP interface, categorized by their functionality.

### Core Search & Analysis

- **`search_context`**: Semantic search for code chunks and documentation.
- **`search_tests`**: Finds relevant test cases based on your query.
- **`analyze_dependencies`**: Generates a symbol call graph using AST parsing.
- **`find_similar_code`**: Identifies code implementations similar to a provided snippet.

### System & Metadata

- **`get_file_structure`**: Returns the internal structure (functions, classes) of a file.
- **`list_files`**: Lists all indexed files within the current namespace.
- **`get_namespace_stats`**: Provides metadata about the index size and project health.
- **`get_metrics`**: Displays execution metrics, including cache hit rates and latencies.

## Practical Workflows

These workflows demonstrate the power of integrating Vectora directly into your AI coding agent.

- **Onboarding**: Ask "Explain the auth system in this project." The IDE uses `search_context` to find the relevant logic and provides a guided tour.
- **Debugging**: Ask "Why is this test failing?" The agent uses `search_tests` and `analyze_dependencies` to identify the root cause across multiple files.
- **Consistency**: Ask "Review this new function." The agent uses `find_similar_code` to ensure your new implementation matches existing project patterns.

## Advanced Configuration

You can further customize the MCP server behavior by adding environment variables to your configuration.

- **`VECTORA_NAMESPACE`**: Use different namespaces for staging or production environments.
- **`VECTORA_LOG_LEVEL`**: Set to `debug` to investigate communication issues.
- **`VECTORA_LOG_FILE`**: Redirect logs to a specific file for easier auditing.

## Troubleshooting

If the IDE fails to communicate with Vectora, verify the following:

- **Command Not Found**: Ensure `vectora` is in your system PATH or use an absolute path in the config.
- **Handshake Errors**: Test the server manually by piping a JSON initialization message into `vectora mcp --stdio`.
- **API Key Issues**: Verify that your keys are correctly set in the `env` block of the configuration file.

## External Linking

| Concept              | Resource                             | Link                                                                                                       |
| -------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **MongoDB Atlas**    | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                                         |
| **AST Parsing**      | Tree-sitter Official Documentation   | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **JSON-RPC**         | JSON-RPC 2.0 Specification           | [www.jsonrpc.org/specification](https://www.jsonrpc.org/specification)                                     |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
