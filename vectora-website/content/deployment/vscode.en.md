---
title: "VS Code"
slug: vscode
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - auth
  - concepts
  - deployment
  - extension
  - integration
  - marketplace
  - mcp
  - protocol
  - tools
  - vectora
  - vscode
---

{{< lang-toggle >}}

The Vectora extension for Visual Studio Code is published on the Visual Studio Marketplace and the Open VSX Registry. Unlike the daemon's Go binary, the extension is built in TypeScript and acts as a visual interface that communicates with the local (Desktop) or remote (Cloud) MCP Server.

The extension deployment process involves compiling the source code, generating the VSIX file, and official publication through Microsoft's command-line tools.

## Microsoft Marketplace

The Visual Studio Marketplace is the primary showcase for VS Code extensions. To publish, you must have a developer account linked to an Azure DevOps organization and a Personal Access Token (PAT) with the appropriate permissions.

Publication is automated via CI/CD, but can be performed manually for preview releases or internal testing using the `vsce` tool.

## Compilation and Packaging

Before publishing, the extension must be compiled and packaged. This process removes development dependencies and optimizes the code for execution within VS Code.

```bash
# Navigate to the extension directory
cd integrations/packages/vscode

# Install dependencies
npm install

# Compile and generate the .vsix file
npx vsce package
```

## Publishing with vsce

Official publication is done using the `publish` command. Ensure that the version in `package.json` has been incremented following semantic versioning (SemVer) rules.

```bash
# Publish to the official Marketplace
npx vsce publish

# If you need to specify the token manually
npx vsce publish -p <YOUR_PAT_TOKEN>
```

## Release Cycle and Open VSX

In addition to the official Marketplace, Vectora is also published on the Open VSX Registry, which serves VS Code forks like VSCodium. The process uses the `ovsx` tool.

```bash
# Publish to Open VSX
npx ovsx publish <FILENAME>.vsix -p <OPEN_VSX_TOKEN>
```

Each new version of the extension must be accompanied by an updated `CHANGELOG.md`, describing improvements to the search engine and integration with the MCP Server.

## External Linking

| Concept            | Resource                                       | Link                                                                                   |
| ------------------ | ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| **MCP**            | Model Context Protocol Specification           | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**     | Go SDK for MCP (mark3labs)                     | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **TypeScript**     | Official TypeScript Handbook                   | [www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)                   |
| **GitHub Actions** | Automate your workflow from idea to production | [docs.github.com/en/actions](https://docs.github.com/en/actions)                       |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
