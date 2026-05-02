---
title: "Connected RAG: The Power of Structured Context"
slug: rag
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - auth
  - concepts
  - config
  - context-engine
  - embeddings
  - rag
  - reranker
  - system
  - vectora
  - voyage
---

{{< lang-toggle >}}

Have you ever asked an AI agent about a function in your project, and it replied with something that looked right but completely ignored how that function was used in the rest of the system? This is the classic symptom of **fragmented RAG**.

Vectora solves this problem through **Connected RAG**, an approach that doesn't just search for text snippets, but reconstructs the logical and structural relationships of your code before sending them to the language model.

## What is RAG?

RAG (Retrieval-Augmented Generation) is the technique of providing external data (like your code files) to an LLM at the time of the query. Instead of the model "guessing" based on what it learned during training, it consults your documents and answers based on them.

```text
Query ("How to authenticate?")
    ↓
Retrieval (Search in codebase)
    ↓
Augmentation (Enriches prompt with context)
    ↓
Generation (LLM responds based on context)
```

While it sounds perfect, traditional RAG is dangerous when applied to software development because it ignores the interconnected nature of code.

## The Problem: Traditional RAG vs. Code

Unlike simple text documents, code has implicit dependencies and data flows that cannot be captured solely by simple semantic similarity of words.

| Aspect       | Traditional RAG            | Problem for Code                          |
| :----------- | :------------------------- | :---------------------------------------- |
| **Search**   | Simple semantic similarity | Ignores dependencies and cross-references |
| **Context**  | Isolated text fragments    | LLM doesn't see the full execution flow   |
| **Result**   | "Top 5 text blocks"        | The model loses architectural vision      |
| **Accuracy** | Adequate for documents     | Frequently generates incomplete code      |

In traditional RAG, if you search for "login," the system might return the `loginUser` function but forget the authentication middleware, the unit tests, and the secret configuration necessary for the function to work.

## The Solution: Connected RAG (Context Engine)

In Vectora, RAG is orchestrated by a **Context Engine** that understands the decision tree and the project structure.

### 1. Multimodal Search

We combine three different strategies to ensure nothing is missed:

- **Embeddings (Voyage 4)**: Captures the semantic intent of the query.
- **AST Analysis**: Uses Tree-sitter to understand the syntactic structure (who calls whom).
- **Keyword Grep**: Ensures that specific technical terms are located accurately.

### 2. Multi-hop Reasoning

The context engine doesn't just do one search. It performs logical "hops" to find related information. If the initial search finds an interface, the engine automatically searches for its implementations and dependencies, reconstructing the knowledge graph necessary for the task.

### 3. Structured Composition

The context returned to the agent is not just a list of strings. It is an organized object containing the main file, its direct dependencies, usage locations, and related tests, allowing the LLM to make decisions with architectural awareness.

## Why Does Connected RAG Matter?

When context is properly connected, the results are drastically superior.

- **Reduced Hallucinations**: The agent stops inventing imports or functions that do not exist.
- **Token Savings**: Instead of sending entire files (dump), we send only the surgical snippets needed.
- **Consistency**: Refactoring suggestions respect the design patterns already established in the project.

## External Linking

| Concept               | Resource                                                   | Link                                                                             |
| --------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **RAG**               | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                     |
| **AST Parsing**       | Tree-sitter Official Documentation                         | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/) |
| **Voyage AI**         | High-performance embeddings for RAG                        | [www.voyageai.com/](https://www.voyageai.com/)                                   |
| **Voyage Embeddings** | Voyage Embeddings Documentation                            | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)   |
| **Voyage Reranker**   | Voyage Reranker API                                        | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)       |
| **REST API Design**   | RESTful API Best Practices                                 | [restfulapi.net/](https://restfulapi.net/)                                       |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
