---
title: "Vectora Skills"
slug: skills
date: "2026-04-24T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - architecture
  - concepts
  - config
  - gemini
  - integration
  - mcp
  - protocol
  - rag
  - rbac
  - security
  - skills
  - state
  - tools
  - vectora
  - yaml
---

{{< lang-toggle >}}

Vectora Skills are specialized behavior modules that transform Vectora from a simple search engine into an intelligent copilot that works alongside the primary model (Claude, Gemini, etc.). These skills provide deep analysis and real-time validation across various dimensions of development.

By utilizing specialized skills, Vectora can provide more targeted assistance, moving beyond general search toward active participation in the software development lifecycle.

## What is a Skill?

A **Skill** is a specialized behavior pattern that Vectora offers through its MCP tools. Unlike generic search tools, skills are:

- **Context-Aware**: They understand the entire project, not just isolated search results.
- **Validators**: They check code quality, security, and performance in real-time.
- **Interactive**: They maintain a continuous dialogue with the primary AI model.
- **Traceable**: They generate auditable reports of decisions and suggestions.

## The 11 Core Skills

Vectora is organized into eleven distinct skill areas to provide comprehensive coverage of development tasks.

### 1. [Pair Programming](./pair-programming/)

Vectora acts as a principal engineer, assisting and validating code as it is written.
**Activation**: `/pair_programming`

### 2. [Context Enrichment](./context-enrichment/)

Automatically injects relevant context from the codebase before the model generates a response.
**Activation**: `/enrich_context`

### 3. [Dependency Analysis](./dependency-analysis/)

Analyzes relationships between modules, detects cycles, and identifies orphan code.
**Activation**: `/analyze_dependencies`

### 4. [Security Audit](./security-audit/)

Validates code against security standards, detecting secrets and vulnerabilities.
**Activation**: `/security_audit`

### 5. [Performance Analysis](./performance-analysis/)

Analyzes latency, throughput, and resource usage for code and queries.
**Activation**: `/analyze_performance`

### 6. [Test Coverage](./test-coverage/)

Identifies untested code and generates suggestions for comprehensive test cases.
**Activation**: `/analyze_test_coverage`

### 7. [Architecture Validation](./architecture-validation/)

Ensures that code adheres to design principles (SOLID, Clean Architecture).
**Activation**: `/validate_architecture`

### 8. [Documentation Generation](./documentation-generation/)

Automatically generates technical docs, Mermaid diagrams, and ADRs.
**Activation**: `/generate_documentation`

### 9. [Refactoring Suggestions](./refactoring-suggestions/)

Analyzes code to suggest improvements in maintainability and clarity (DRY).
**Activation**: `/suggest_refactoring`

### 10. [Risk Assessment](./risk-assessment/)

Evaluates the potential impact and regression risk of proposed changes.
**Activation**: `/assess_risk`

### 11. [Web Search Integration](./web-search/)

Integrates real-time web search for technical research and external documentation lookup.
**Activation**: `/web_search`

## Skill Layer Architecture

Vectora's skill layer sits between the primary AI model and the core search engine.

```mermaid
graph TD
    A["Primary AI Model (Claude/Gemini)"] -- "MCP Protocol" --> Vectora Cognitive Runtime["Vectora Cognitive Runtime: Tactical Orchestrator"]
    Vectora Cognitive Runtime -- "Selects Skill" --> B["Vectora MCP Server"]
    subgraph "Skill Layer"
        B -- "Processes" --> C["Pair Programming"]
        B -- "Processes" --> D["Security Audit"]
        B -- "Processes" --> E["Web Search"]
        B -- "Processes" --> F["...Other Skills"]
    end
    C & D & E & F -- "Queries" --> G["Vectora Core (Search, RAG)"]
```

The **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** is the tactical brain that resides between the primary AI model and the tools. It analyzes the user prompt and the current state to decide **which skill** should be activated, ensuring the agent uses the most precise tool for each task.

## Project Configuration

Enable and configure specific skills in your `vectora.config.yaml` file.

```yaml
skills:
  enabled: true
  pair_programming:
    enabled: true
    validation_level: "strict"
  security_audit:
    enabled: true
    fail_on_critical: true
```

## External Linking

| Concept        | Resource                                                   | Link                                                                                   |
| -------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **MCP**        | Model Context Protocol Specification                       | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK** | Go SDK for MCP (mark3labs)                                 | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Gemini AI**  | Google DeepMind Gemini Models                              | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API** | Google AI Studio Documentation                             | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **RBAC**       | NIST Role-Based Access Control Standard                    | [csrc.nist.gov/projects/rbac](https://csrc.nist.gov/projects/rbac)                     |
| **RAG**        | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                           |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
