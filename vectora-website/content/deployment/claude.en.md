---
title: "Claude"
slug: claude
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - anthropic
  - claude
  - concepts
  - config
  - deployment
  - integration
  - mcp
  - protocol
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

The integration of Vectora with Anthropic Claude is based on the Model Context Protocol (MCP), allowing Claude Desktop to use Vectora as a local semantic search tool. This integration is primarily focused on Desktop use, where Claude consumes data directly from the developer's local file system.

When deploying the Claude integration, Vectora acts as an MCP server that exposes code analysis and context retrieval tools to Anthropic's reasoning engine.

## Claude Desktop and MCP

Claude Desktop is the official client that natively supports the MCP protocol. Deployment consists of registering the Vectora binary in the Claude configuration file, allowing it to start the Vectora process automatically via stdio.

For users who prefer not to manage Go binaries manually, Vectora provides an NPM package (`@kaffyn/vectora-mcp`) that acts as a bridge to the main binary.

## claude_desktop_config.json Configuration

The Claude Desktop configuration file must be edited to include Vectora as an MCP server. The path to this file varies by operating system:

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "vectora": {
      "command": "npx",
      "args": ["-y", "@kaffyn/vectora-mcp", "start"]
    }
  }
}
```

## Installation via NPM

The official Vectora MCP NPM package facilitates deployment in environments where Node.js is already present. The package is published on the public NPM registry and can be installed globally or run via `npx`.

```bash
# Optional global installation
npm install -g @kaffyn/vectora-mcp

# Verify installation
vectora-mcp --version
```

## Updates and Versions

Since Claude Desktop manages the MCP server's lifecycle, Vectora updates are applied the next time Claude is restarted. We recommend using specific version tags in the configuration file if your workflow requires extreme stability.

Whenever a new tool is added to the Vectora engine, Claude will automatically detect it through the MCP protocol's tool discovery feature.

## External Linking

| Concept              | Resource                             | Link                                                                                   |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
