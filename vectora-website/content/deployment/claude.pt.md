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
  - mcp
  - protocol
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

A integração do Vectora com o Anthropic Claude é baseada no Model Context Protocol (MCP), permitindo que o Claude Desktop utilize o Vectora como uma ferramenta de busca semântica local. Esta integração é primordialmente voltada para o uso Desktop, onde o Claude consome os dados diretamente do sistema de arquivos local do desenvolvedor.

Ao implantar a integração com o Claude, o Vectora atua como um servidor MCP que expõe ferramentas de análise de código e recuperação de contexto para o motor de raciocínio da Anthropic.

## Claude Desktop e MCP

O Claude Desktop é o cliente oficial que suporta o protocolo MCP nativamente. A implantação consiste em registrar o binário do Vectora no arquivo de configuração do Claude, permitindo que ele inicie o processo do Vectora automaticamente via stdio.

Para usuários que preferem não gerenciar binários Go manualmente, o Vectora disponibiliza um pacote NPM (`@kaffyn/vectora-mcp`) que atua como um bridge para o binário principal.

## Configuração do claude_desktop_config.json

O arquivo de configuração do Claude Desktop deve ser editado para incluir o Vectora como um servidor MCP. O caminho deste arquivo varia de acordo com o sistema operacional:

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

## Instalação via NPM

O pacote NPM oficial do Vectora MCP facilita a implantação em ambientes onde o Node.js já está presente. O pacote é publicado no registro público do NPM e pode ser instalado globalmente ou executado via `npx`.

```bash
# Instalação global opcional
npm install -g @kaffyn/vectora-mcp

# Verificar instalação
vectora-mcp --version
```

## Atualizações e Versões

Como o Claude Desktop gerencia o ciclo de vida do servidor MCP, as atualizações do Vectora são aplicadas na próxima vez que o Claude for reiniciado. Recomendamos o uso de tags de versão específicas no arquivo de configuração caso seu fluxo de trabalho exija estabilidade extrema.

Sempre que uma nova ferramenta for adicionada ao motor do Vectora, o Claude a detectará automaticamente através da funcionalidade de descoberta de ferramentas do protocolo MCP.

## External Linking

| Concept              | Resource                             | Link                                                                                   |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
