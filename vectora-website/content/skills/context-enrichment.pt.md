---
title: "Enriquecimento de Contexto"
slug: context-enrichment
date: "2026-04-27T10:15:00-03:00"
draft: false
categories:
  - Skills
tags:
  - ai
  - analysis
  - architecture
  - ast-parsing
  - auth
  - concepts
  - context
  - context-engine
  - mcp
  - protocol
  - rag
  - skills
  - system
  - tools
  - vectora
type: docs
sidebar:
  open: true
---

{{< lang-toggle >}}

A skill de **Enriquecimento de Contexto** (Context Enrichment) permite que o Vectora eleve a compreensão do código através da injeção de metadados semânticos e relacionamentos profundos da base de código.

Diferente de uma busca textual simples, esta skill mapeia como os componentes interagem e fornece ao modelo de IA principal o conhecimento necessário para tomar decisões informadas sobre arquitetura e lógica.

## Capacidades

O Enriquecimento de Contexto foca em três pilares fundamentais:

1. **Relacionamentos Semânticos**: Identifica como funções e tipos se relacionam através do projeto, mesmo em arquivos distantes.
2. **Histórico de Decisões**: Recupera contexto de mudanças passadas e padrões estabelecidos na base de código.
3. **Mapeamento de Fluxo**: Ajuda a entender o caminho de execução de uma funcionalidade específica.

## Como Funciona

Quando ativada, a skill percorre o grafo de conhecimento gerado pelo Context Engine para encontrar conexões que não seriam visíveis em uma busca vetorial pura.

- **Análise AST**: Utiliza o Tree-sitter para entender a estrutura sintática.
- **Injeção de Metadados**: Adiciona informações sobre tipos, interfaces e implementações ao prompt.
- **Compacção Inteligente**: Garante que apenas o contexto mais relevante seja injetado, respeitando a janela de tokens.

## Ativação

Você pode ativar esta skill manualmente através do comando MCP ou via flags na CLI:

- **Ferramenta MCP**: `/context_enrichment`
- **Uso Automático**: O Vectora aciona esta skill quando detecta consultas que envolvem múltiplos módulos ou padrões arquiteturais complexos.

## Exemplo de Uso

```bash
# Solicita análise enriquecida de um módulo específico
vectora search "Como o sistema de autenticação lida com refresh tokens?" --enrich
```

## Benefícios

- **Redução de Alucinações**: Ao fornecer o contexto real, o modelo de IA especula menos sobre o funcionamento interno.
- **Respostas Precisas**: Sugestões de código que seguem exatamente os padrões já existentes no seu projeto.
- **Descoberta Acelerada**: Ideal para desenvolvedores que estão entrando em projetos novos e precisam entender a "big picture".

## External Linking

| Concept              | Resource                                                   | Link                                                                                   |
| -------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **AST Parsing**      | Tree-sitter Official Documentation                         | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)       |
| **MCP**              | Model Context Protocol Specification                       | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)                                 | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Anthropic Claude** | Claude Documentation                                       | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **RAG**              | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                           |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
