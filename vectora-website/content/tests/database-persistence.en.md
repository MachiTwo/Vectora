---
title: "Test Suite: Database & Persistence"
slug: database-persistence-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - concepts
  - context-engine
  - database
  - embeddings
  - mongodb
  - mongodb-atlas
  - persistence
  - security
  - state
  - testing
  - vector-search
  - vectora
---

{{< lang-toggle >}}

This suite validates that Vectora persists data correctly, retrieves it efficiently, and synchronizes between local and cloud environments without loss of integrity. Ensuring data reliability is critical for maintaining an accurate and helpful context engine.

By verifying the persistence layer, we guarantee that indexed code and user session state remain consistent across restarts and multiple devices.

**Coverage**: 80+ tests | **Priority**: CRITICAL

## Tested Components

The persistence testing strategy covers all data-related modules within the Vectora architecture.

- MongoDB Atlas connection and pooling.
- Embedding storage and vector retrieval.
- Code chunk persistence and metadata integrity.
- API key management and security.
- Hybrid local/cloud cache synchronization.
- Data roaming and cross-device consistency.
- Vector indexing performance and accuracy.

## Test Segments

The following sections detail the specific test cases and scenarios covered by this suite.

### 1. MongoDB Connectivity (15 tests)

Ensures that the application can reliably communicate with the database under various network conditions.

- **Connection Establishment**: Validates that connections are established within 2 seconds with proper pooling.
- **Retry Logic**: Verifies exponential backoff and automatic recovery when the database goes offline.
- **Connection Pooling**: Ensures efficient resource usage under high concurrent load (50+ simultaneous requests).
- **Timeouts**: Validates that hung connections are terminated gracefully after 30 seconds.

### 2. CRUD Operations with Embeddings (20 tests)

Focuses on the lifecycle of vector data and its associated metadata in the documents collection.

- **Insert Vector**: Validates that 384-dimensional embeddings are saved with unique IDs and full metadata.
- **Search Vector**: Verifies that cosine similarity search returns the top-K relevant results in under 200ms.
- **Update Vector**: Ensures that modifications to code chunks correctly recalculate indices and increment versions.
- **Batch Operations**: Tests the atomic insertion of 500+ documents with reliable rollback on failure.

### 3. Chunk Persistence (15 tests)

Validates the relationship between raw code snippets and their processed representation.

- **Chunk Storage**: Each chunk must have a unique ID, embedding, line range, and file path.
- **Structural Retrieval**: Verifies that chunks can be retrieved based on their AST relationship (e.g., finding the parent class).
- **Integrity**: Ensures no circular references exist in the chunk dependency graph.

### 4. Data Roaming & Sync (15 tests)

Ensures a seamless experience when using Vectora across different machines or in offline mode.

- **Local Cache Sync**: Validates that offline searches are queued and merged with the cloud when a connection is restored.
- **Conflict Resolution**: Implements "last-write-wins" or automatic merge strategies for simultaneous updates.
- **Encryption at Rest**: Ensures that local data in `AppData` is encrypted using AES-256 with user-specific keys.

### 5. Vector Indexing (10 tests)

Monitors the performance and accuracy of the HNSW indices in MongoDB Atlas.

- **Index Creation**: Validates that indices for 10k+ documents are built incrementally without downtime.
- **Search Accuracy**: Compares HNSW results against brute-force search to ensure >= 95% precision.

## Acceptance Criteria

| Criterion                | Target                          |
| :----------------------- | :------------------------------ |
| **Success Rate**         | 100%                            |
| **MongoDB Coverage**     | > 90%                           |
| **Query Latency (p95)**  | < 300ms                         |
| **Insert Latency (p95)** | < 200ms                         |
| **Cache Hit Rate**       | > 70%                           |
| **Sync Time**            | < 5s for 1000+ docs             |
| **Data Integrity**       | Zero data loss in all scenarios |

## Execution Guide

To run the database and persistence tests, use the following commands:

```bash
# Run all persistence tests
go test -v ./tests/database/...

# Run with race detection
go test -v -race ./tests/database/...

# Run with coverage report
go test -v -cover ./tests/database/...
```

## External Linking

| Concept                 | Resource                                                 | Link                                                                                                                     |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **MongoDB Atlas**       | Atlas Vector Search Documentation                        | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/)               |
| **AST Parsing**         | Tree-sitter Official Documentation                       | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                                         |
| **HNSW**                | Efficient and robust approximate nearest neighbor search | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)                                                             |
| **REST API Design**     | RESTful API Best Practices                               | [restfulapi.net/](https://restfulapi.net/)                                                                               |
| **Exponential Backoff** | AWS Retry Strategy Guide                                 | [docs.aws.amazon.com/general/latest/gr/api-retries.html](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
