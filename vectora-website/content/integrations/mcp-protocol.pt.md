---
title: "Model Context Protocol (MCP): Conecte o Vectora a Qualquer IDE"
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
  - integration
  - mcp
  - mongodb-atlas
  - protocol
  - protocolo
  - system
  - tools
  - vector-search
  - vectora
---

{{< lang-toggle >}}

O **Model Context Protocol (MCP)** é um padrão aberto que permite que IDEs e aplicações de IA se conectem a servidores de ferramentas externas via **JSON-RPC 2.0 sobre stdio**. Ao usar o MCP, o Vectora pode fornecer contexto profundo da base de código para vários agentes de IA executados em seu ambiente de desenvolvimento local.

Este protocolo garante que suas ferramentas e contexto sejam desacoplados de modelos de IA específicos, permitindo um fluxo de trabalho de desenvolvimento mais flexível e modular.

> [!NOTE] > **O MCP é especificamente para o Vectora Desktop**:
>
> - **Modo Desktop (MCP stdio)**: Executado localmente com latência ultra-baixa (<10ms) e acesso total ao seu sistema de arquivos e instância local do MongoDB.
> - **Modo Cloud (API HTTP)**: Um serviço SaaS gerenciado para integrações com plataformas baseadas na web, como o ChatGPT e a API do Gemini.

## Como Funciona: O Fluxo MCP

A arquitetura MCP usa entrada/saída padrão (stdio) para comunicação, criando uma ponte segura e performática entre sua IDE e o servidor Vectora.

```mermaid
graph LR
    A[Usuário escreve na IDE] -->|@vectora search_context| B[IDE]
    B -->|JSON-RPC 2.0 via stdio| C["Servidor MCP Vectora<br/>(processo local)"]
    C -->|Embedding da consulta| D["MongoDB Atlas<br/>Busca Vetorial"]
    D -->|Chunks relevantes| C
    C -->|JSON de resultado da tool| B
    B -->|Exibe no contexto| A
```

### Sequência de Comunicação

1. **Inicialização da IDE**: A IDE lê a configuração MCP e inicia o servidor Vectora através do comando `vectora mcp --stdio`.
2. **Handshake & Descoberta**: Ocorre um handshake JSON-RPC, onde o Vectora revela suas ferramentas disponíveis (ex: `search_context`, `analyze_dependencies`).
3. **Execução de Ferramenta**: Quando o usuário aciona um comando, a IDE envia uma requisição para o Vectora, que processa a busca e retorna os resultados para exibição na IDE.

## Configuração Passo a Passo por IDE

A configuração varia ligeiramente dependendo de qual editor aprimorado por IA você está usando.

### IDE 1: Claude Code (Recomendado)

1. **Pré-requisitos**: Certifique-se de que o Claude Code e o CLI do Vectora estejam instalados globalmente.
2. **Localizar Configuração**: Encontre seu arquivo `claude_desktop_config.json`. No Windows, ele geralmente fica em `%APPDATA%\Claude\`.
3. **Adicionar Servidor Vectora**: Edite o arquivo para incluir a configuração do servidor MCP do Vectora com suas variáveis de ambiente.

```json
{
  "mcpServers": {
    "vectora": {
      "command": "vectora",
      "args": ["mcp", "--stdio"],
      "env": {
        "GEMINI_API_KEY": "sua-chave",
        "VOYAGE_API_KEY": "sua-chave",
        "VECTORA_NAMESPACE": "seu-projeto"
      }
    }
  }
}
```

### IDE 2: Cursor

1. **Localizar Configuração**: Navegue até o diretório de configurações do Cursor (geralmente `%APPDATA%\Cursor\User\`).
2. **Configurar**: Use a mesma estrutura JSON da configuração do Claude Code.
3. **Reiniciar**: Feche e reabra o Cursor completamente para inicializar a conexão.

## 12 Ferramentas MCP Disponíveis

O Vectora expõe um conjunto abrangente de ferramentas através da interface MCP, categorizadas por sua funcionalidade.

### Busca Core & Análise

- **`search_context`**: Busca semântica por chunks de código e documentação.
- **`search_tests`**: Encontra casos de teste relevantes baseados na sua consulta.
- **`analyze_dependencies`**: Gera um grafo de chamadas de símbolos usando parsing AST.
- **`find_similar_code`**: Identifica implementações de código semelhantes a um snippet fornecido.

### Sistema & Metadados

- **`get_file_structure`**: Retorna a estrutura interna (funções, classes) de um arquivo.
- **`list_files`**: Lista todos os arquivos indexados no namespace atual.
- **`get_namespace_stats`**: Fornece metadados sobre o tamanho do índice e saúde do projeto.
- **`get_metrics`**: Exibe métricas de execução, incluindo taxas de acerto de cache e latências.

## Workflows Práticos

Estes fluxos demonstram o poder de integrar o Vectora diretamente ao seu agente de codificação de IA.

- **Onboarding**: Pergunte "Explique o sistema de autenticação neste projeto". A IDE usa `search_context` para encontrar a lógica relevante e fornece um tour guiado.
- **Depuração**: Pergunte "Por que este teste está falhando?". O agente usa `search_tests` e `analyze_dependencies` para identificar a causa raiz em múltiplos arquivos.
- **Consistência**: Pergunte "Revise esta nova função". O agente usa `find_similar_code` para garantir que sua nova implementação corresponda aos padrões existentes do projeto.

## Configuração Avançada

Você pode personalizar ainda mais o comportamento do servidor MCP adicionando variáveis de ambiente à sua configuração.

- **`VECTORA_NAMESPACE`**: Use namespaces diferentes para ambientes de staging ou produção.
- **`VECTORA_LOG_LEVEL`**: Defina como `debug` para investigar problemas de comunicação.
- **`VECTORA_LOG_FILE`**: Redirecione os logs para um arquivo específico para facilitar a auditoria.

## Solução de Problemas

Se a IDE falhar ao se comunicar com o Vectora, verifique o seguinte:

- **Comando não encontrado**: Certifique-se de que o `vectora` esteja no PATH do seu sistema ou use um caminho absoluto na config.
- **Erros de Handshake**: Teste o servidor manualmente enviando uma mensagem de inicialização JSON-RPC para `vectora mcp --stdio`.
- **Problemas com Chaves de API**: Verifique se suas chaves estão configuradas corretamente no bloco `env` do arquivo de configuração.

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

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
