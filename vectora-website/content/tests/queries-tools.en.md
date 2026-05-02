---
title: "Test Suite: Queries & Tools"
slug: queries-tools-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - ast-parsing
  - concepts
  - context-engine
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

Every query and tool in Vectora must function correctly, return accurate results, and execute within our performance SLAs. This suite is the functional heart of Vectora, testing all 12+ MCP tools and their deep integrations with search engines, embeddings, and reranking providers.

By verifying the core tools, we ensure that AI agents receiving data from Vectora can rely on its precision and context.

**Coverage**: 150+ tests | **Priority**: CRITICAL

## Principal Tools

The following tools form the backbone of the Vectora context engine and are rigorously tested for reliability.

1. `search_context`: Contextual search within the codebase.
2. `search_tests`: Discovery of related tests for specific code paths.
3. `find_similar_code`: Retrieval of structurally or algorithmically similar snippets.
4. `analyze_dependencies`: Mapping of symbol and package relationships.
5. `get_file_structure`: Hierarchical visualization of the project layout.
6. `validate_query`: Pre-flight check for query clarity and syntax.
7. `get_metrics`: Real-time server performance and health data.

## Test Segments

The following sections detail the specific test cases and scenarios covered by this suite.

### 1. Search Context (30 tests)

Validates the primary semantic search functionality across large-scale repositories.

- **Basic Execution**: Ensures queries return the top-K results with scores above 0.7 in under 300ms.
- **Semantic Accuracy**: Verifies that requests for concepts (e.g., "auth validation") return relevant code even without exact keyword matches.
- **Large Result Sets**: Tests pagination and accuracy consistency when handling 1000+ matching chunks.
- **Context Windows**: Confirms that each result includes surrounding lines to provide necessary context for LLMs.

### 2. Search Tests (25 tests)

Ensures that developers can easily find how a specific feature is verified within the project.

- **Test Discovery**: Identifies unit, integration, and E2E tests related to a specific functional area.
- **Relationship Mapping**: Traces connections between a function and the tests that exercise it (directly or indirectly).
- **Gap Detection**: Identifies functions or classes that lack associated test coverage and suggests creation.

### 3. Find Similar Code (30 tests)

Tests the system's ability to recognize patterns, algorithms, and structural similarities.

- **Structural Similarity**: Finds patterns like "reduce-based summation" even if variable names differ.
- **Algorithm Recognition**: Identifies different implementations of the same algorithm (e.g., BFS) across languages.
- **Anti-Pattern Detection**: Verifies the ability to find all instances of a specific coding anti-pattern across the codebase.

### 4. Dependency Analysis (25 tests)

Maps the complex web of relationships that define a modern software project.

- **Direct Dependencies**: Identifies called functions, used libraries, and external API integrations.
- **Transitive Chains**: Maps deep call stacks and detects potential circular dependency risks.
- **Breaking Change Impact**: Analyzes the codebase to identify which components will be affected by a library update.

### 5. File Structure & Validation (15 tests each)

Validates the utility tools that help agents navigate and understand the repository layout.

- **Tree Generation**: Confirms accurate JSON visualization of the file hierarchy with metadata (sizes, line counts).
- **Query Validation**: Analyzes natural language queries for ambiguity and suggests refinements to improve search quality.

## Performance SLAs

The following table summarizes the expected performance targets for our primary tools.

| Tool                     | p95 Latency | p99 Latency | Cache Target |
| :----------------------- | :---------- | :---------- | :----------- |
| **search_context**       | < 300ms     | < 500ms     | 70%+ hit     |
| **search_tests**         | < 200ms     | < 300ms     | 80%+ hit     |
| **find_similar_code**    | < 500ms     | < 1s        | 60%+ hit     |
| **analyze_dependencies** | < 200ms     | < 400ms     | 75%+ hit     |
| **validate_query**       | < 100ms     | < 150ms     | 90%+ hit     |

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

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
