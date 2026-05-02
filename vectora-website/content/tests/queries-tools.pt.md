---
title: "Suite de Testes: Consultas & Ferramentas"
slug: queries-tools-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - ast-parsing
  - concepts
  - embeddings
  - integration
  - mcp
  - mongodb-atlas
  - protocol
  - queries
  - rag
  - search
  - system
  - testing
  - tools
  - vector-search
  - vectora
  - voyage
---

{{< lang-toggle >}}

Toda consulta (query) e ferramenta (tool) do Vectora deve funcionar corretamente, retornar resultados precisos e executar dentro dos nossos SLAs de performance. Esta suite é o coração funcional do Vectora, testando todos os mais de 12 ferramentas MCP e suas integrações profundas com motores de busca, provedores de embeddings e reranking.

Ao verificar as ferramentas principais, garantimos que os agentes de IA que recebem dados do Vectora possam confiar em sua precisão e contexto.

**Cobertura**: 150+ testes | **Prioridade**: CRÍTICA

## Principais Ferramentas

As seguintes ferramentas formam a espinha dorsal do motor de contexto do Vectora e são rigorosamente testadas quanto à confiabilidade.

1. `search_context`: Busca contextual dentro da base de código.
2. `search_tests`: Descoberta de testes relacionados para caminhos de código específicos.
3. `find_similar_code`: Recuperação de trechos estruturalmente ou algoritmicamente similares.
4. `analyze_dependencies`: Mapeamento de relações entre símbolos e pacotes.
5. `get_file_structure`: Visualização hierárquica do layout do projeto.
6. `validate_query`: Verificação prévia da clareza e sintaxe da consulta.
7. `get_metrics`: Dados de performance e saúde do servidor em tempo real.

## Segmentos de Testes

As seções a seguir detalham os casos de teste específicos e os cenários cobertos por esta suite.

### 1. Busca de Contexto (30 testes)

Valida a funcionalidade primária de busca semântica em repositórios de larga escala.

- **Execução Básica**: Garante que as consultas retornem os top-K resultados com scores acima de 0.7 em menos de 300ms.
- **Precisão Semântica**: Verifica se pedidos por conceitos (ex: "validação de auth") retornam código relevante mesmo sem correspondência exata de palavras-chave.
- **Conjuntos de Resultados Grandes**: Testa a paginação e a consistência da precisão ao lidar com mais de 1000 chunks correspondentes.
- **Janelas de Contexto**: Confirma que cada resultado inclui linhas adjacentes para fornecer o contexto necessário para os LLMs.

### 2. Busca de Testes (25 testes)

Garante que os desenvolvedores possam encontrar facilmente como uma funcionalidade específica é verificada no projeto.

- **Descoberta de Testes**: Identifica testes unitários, de integração e E2E relacionados a uma área funcional específica.
- **Mapeamento de Relações**: Rastreia conexões entre uma função e os testes que a exercitam (direta ou indiretamente).
- **Detecção de Gaps**: Identifica funções ou classes que carecem de cobertura de teste associada e sugere sua criação.

### 3. Encontrar Código Similar (30 testes)

Testa a habilidade do sistema em reconhecer padrões, algoritmos e similaridades estruturais.

- **Similaridade Estrutural**: Encontra padrões como "soma baseada em reduce" mesmo se os nomes das variáveis forem diferentes.
- **Reconhecimento de Algoritmo**: Identifica diferentes implementações do mesmo algoritmo (ex: BFS) entre várias linguagens.
- **Detecção de Anti-padrões**: Verifica a habilidade de encontrar todas as instâncias de um anti-padrão de código específico em toda a base.

### 4. Análise de Dependências (25 testes)

Mapeia a complexa teia de relacionamentos que define um projeto de software moderno.

- **Dependências Diretas**: Identifica funções chamadas, bibliotecas usadas e integrações de APIs externas.
- **Cadeias Transitivas**: Mapeia call stacks profundas e detecta potenciais riscos de dependência circular.
- **Impacto de Breaking Changes**: Analisa a base de código para identificar quais componentes serão afetados por uma atualização de biblioteca.

### 5. Estrutura de Arquivos & Validação (15 testes cada)

Valida as ferramentas utilitárias que ajudam os agentes a navegar e entender o layout do repositório.

- **Geração de Árvore**: Confirma a visualização JSON precisa da hierarquia de arquivos com metadados (tamanhos, contagem de linhas).
- **Validação de Consulta**: Analisa consultas em linguagem natural em busca de ambiguidades e sugere refinamentos para melhorar a qualidade da busca.

## SLAs de Performance

A tabela a seguir resume as metas de performance esperadas para nossas principais ferramentas.

| Ferramenta               | Latência p95 | Latência p99 | Alvo de Cache |
| :----------------------- | :----------- | :----------- | :------------ |
| **search_context**       | < 300ms      | < 500ms      | 70%+ hit      |
| **search_tests**         | < 200ms      | < 300ms      | 80%+ hit      |
| **find_similar_code**    | < 500ms      | < 1s         | 60%+ hit      |
| **analyze_dependencies** | < 200ms      | < 400ms      | 75%+ hit      |
| **validate_query**       | < 100ms      | < 150ms      | 90%+ hit      |

## External Linking

| Concept               | Resource                             | Link                                                                                                       |
| --------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**               | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**        | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **AST Parsing**       | Tree-sitter Official Documentation   | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **Voyage AI**         | High-performance embeddings for RAG  | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation      | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
