---
title: "Test Suite: Caching & Hybrid Search"
slug: caching-hybrid-search
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - caching
  - concepts
  - embeddings
  - integration
  - mongodb-atlas
  - performance
  - persistence
  - system
  - testing
  - tools
  - vector-search
  - vectora
---

{{< lang-toggle >}}

The hybrid caching system (L1 local + L2 cloud) must optimize performance, reduce latency, and maintain hit rates above 70%. This suite validates cache warming, preloading, hybrid search with fallback strategies, and intelligent synchronization.

These tests ensure that Vectora remains responsive even with large codebases and frequent queries.

**Coverage**: 120+ tests | **Priority**: HIGH

## Cache Layers

The caching architecture is divided into multiple tiers to balance speed and persistence.

### 1. L1 Cache (Local Memory)

Validated through tests focusing on immediate access and volatile storage management.

- Initialization and maximum capacity (5 tests)
- TTL (Time To Live) and expiration (8 tests)
- Eviction policies (LRU, LFU) (8 tests)
- Hit/miss ratio tracking (5 tests)
- Concurrent access safety (5 tests)

**SLA**: Hit rate > 70%, p95 latency < 50ms

### 2. L2 Cache (Persistent Disk/Cloud)

Focuses on long-term storage and synchronization across different environments.

- Serialization and deserialization (10 tests)
- Local/Cloud synchronization (12 tests)
- Value compression (8 tests)
- Data roaming between devices (10 tests)
- Failure recovery (8 tests)

**SLA**: Hit rate > 50%, synchronization in < 5s

### 3. Cache Warming & Preloading

Ensures that relevant context is available before it is explicitly requested by the agent.

- Warming strategies (8 tests)
- Pattern-based preloading (8 tests)
- Incremental updates (8 tests)

### 4. Hybrid Search Orchestration

Validates the coordination between cache retrieval and the primary vector search engine.

- Cache → search orchestration (15 tests)
- Fallback strategies (10 tests)
- p95 latency < 100ms (10 tests)
- Throughput > 500 queries/sec (5 tests)

### 5. Engine Integration

Ensures that all search tools correctly utilize the available caching layers.

- Cache in `search_context()` (8 tests)
- Embedding cache (8 tests)
- Reranking cache (8 tests)
- Intelligent invalidation (8 tests)

## Performance SLAs

The following table summarizes the performance targets for the caching system.

| Metric                 | Target  |
| :--------------------- | :------ |
| **L1 Hit Rate**        | > 70%   |
| **L2 Hit Rate**        | > 50%   |
| **p50 Latency (hit)**  | < 10ms  |
| **p95 Latency (hit)**  | < 50ms  |
| **p50 Latency (miss)** | < 100ms |
| **Memory Footprint**   | < 500MB |

## External Linking

| Concept           | Resource                          | Link                                                                                                       |
| ----------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
