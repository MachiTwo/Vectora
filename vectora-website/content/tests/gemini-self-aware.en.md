---
title: "Test Suite: Gemini Self-Awareness"
slug: gemini-self-aware-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - ast-parsing
  - concepts
  - config
  - context-engine
  - errors
  - gemini
  - integration
  - knowledge
  - mcp
  - protocol
  - rag
  - system
  - testing
  - tools
  - vectora
---

{{< lang-toggle >}}

Gemini must be completely self-aware of Vectora: knowing its identity, capabilities, public documentation, and when to use Vectora to solve complex problems. This suite ensures that Gemini functions as an integrated specialist within the Vectora ecosystem, providing accurate and contextual assistance.

By verifying this self-awareness, we ensure that the AI is not just a tool caller but a knowledgeable partner that understands the system's strengths and limitations.

**Coverage**: 60+ tests | **Priority**: CRITICAL

## Core Principle

> **"Gemini is not just a client that calls Vectora. Gemini UNDERSTANDS Vectora as a superior tool and knows exactly when and how to use it."**

## Test Segments

The following sections detail the specific test cases and scenarios covered by this suite.

### 1. Identity & Description (10 tests)

Ensures that Gemini can accurately describe what Vectora is and how it fits into the broader software landscape.

- **Identity Description**: Validates that Gemini identifies Vectora as a semantic search engine for code with dependency analysis and multi-LLM support.
- **Comparative Knowledge**: Checks if Gemini can explain the differences between Vectora and general-purpose search tools like Elasticsearch or grep.
- **Founding Principles**: Verifies awareness of Vectora's core values, such as "local-first experience" and "intelligent hybrid caching."

### 2. Capabilities & Features (15 tests)

Tests Gemini's knowledge of the specific technical features and tools available within the Vectora platform.

- **Core Feature Awareness**: Lists and explains the Context Engine, Hybrid Search, Reranking, and AST parsing capabilities.
- **Tool Knowledge**: Verifies that Gemini is familiar with the available MCP tools (`search_context`, `analyze_dependencies`, etc.) and their intended use.
- **Configuration Guidance**: Ensures Gemini can provide correct instructions for setting up environment variables and configuration files.

### 3. Documentation Knowledge (15 tests)

Validates that Gemini can cite official documentation correctly and guide users to the right resources.

- **Resource Access**: Ensures Gemini knows where the official website and GitHub repository are located.
- **Accurate Citation**: Checks if Gemini can provide source URLs and mention specific versions/timestamps when explaining a feature.
- **Setup Guide Proficiency**: Verifies that Gemini can walk a user through a complete installation and initial setup process.

### 4. Decision Intelligence (15 tests)

Focuses on the AI's ability to recommend Vectora at the right moment based on the user's task.

- **Recommendation Logic**: Gemini should suggest using Vectora for code navigation, bug investigation, and dependency mapping tasks.
- **Rejection Logic**: Ensures Gemini does not unnecessarily mention Vectora for non-code-related queries.
- **Error Recognition**: Validates that Gemini can detect malformed tool calls and suggest the correct syntax based on the documentation.

### 5. Integration Scenarios (10 tests)

Simulates complex workflows where Gemini uses Vectora to provide high-level analysis and suggestions.

- **Code Review**: Gemini uses Vectora to find similar patterns and compare a user's snippet against project best practices.
- **Bug Investigation**: Searches for similar historical bugs and analyzes related dependencies to provide a diagnosis.
- **Documentation Generation**: Examines existing project patterns to generate consistent and accurate documentation for new functions.

## Acceptance Criteria

| Criterion                     | Target             |
| :---------------------------- | :----------------- |
| **Accuracy of Description**   | 100%               |
| **Tool Knowledge Accuracy**   | > 90%              |
| **Citation of Documentation** | 100% when relevant |
| **Decision Intelligence**     | 90%+ accuracy      |
| **Zero Hallucination**        | 100% on features   |

## External Linking

| Concept         | Resource                                                   | Link                                                                                   |
| --------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Gemini AI**   | Google DeepMind Gemini Models                              | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**  | Google AI Studio Documentation                             | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **AST Parsing** | Tree-sitter Official Documentation                         | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)       |
| **MCP**         | Model Context Protocol Specification                       | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**  | Go SDK for MCP (mark3labs)                                 | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **RAG**         | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                           |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
