---
title: "Test Suite: Performance & Benchmarks"
slug: performance
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - benchmarks
  - concepts
  - context-engine
  - embeddings
  - performance
  - profiling
  - system
  - testing
  - vectora
---

{{< lang-toggle >}}

Vectora must meet all performance SLAs, with latency, throughput, resource utilization, and scalability proven through rigorous benchmarking. This suite validates that Vectora scales efficiently for 50+ concurrent users and maintains a p95 latency under 500ms.

By enforcing strict performance targets, we ensure that the Context Engine remains responsive even under heavy load or with very large codebases.

**Coverage**: 80+ tests | **Priority**: ALTA

## Query Latency Testing

Ensures that user requests are processed and returned within acceptable timeframes.

- **p50 Latency**: Target < 100ms for typical search queries (12 tests).
- **p95 Latency**: Target < 500ms to ensure a smooth experience for most users (12 tests).
- **p99 Latency**: Target < 1s to bound the worst-case response times (10 tests).
- **Warmup vs Cold Start**: Measures the performance impact of cache warming (8 tests).

**Target**: p95 < 500ms, p99 < 1s.

## Embedding & Rerank Latency

Monitors the performance of external API calls and their impact on the overall search cycle.

- **Single Query Embedding**: Target < 2s for a standard code snippet (8 tests).
- **Batch Embeddings**: Target < 5s for processing multiple chunks simultaneously (8 tests).
- **Reranking Latency**: Ensures that final result refinement takes less than 1s (8 tests).
- **Cache Hit Latency**: Validates that retrieved data from L1/L2 cache returns in < 50ms (8 tests).

**Target**: Single < 2s, Batch < 5s.

## Throughput Testing

Validates the system's ability to handle high volumes of concurrent requests.

- **Queries per Second**: Target > 100 sustained queries (10 tests).
- **Embeddings per Second**: Target > 50 chunks processed (8 tests).
- **Concurrent Users**: Validates stability with 50+ simultaneous active sessions (10 tests).
- **Sustained Load**: Tests system behavior under continuous load for 1+ hour (8 tests).

**Target**: > 100 queries/sec sustained.

## Resource Utilization

Ensures that the application remains efficient and does not exhaust host resources.

- **Memory Footprint**: Target < 500MB total RSS under normal load (8 tests).
- **CPU Usage**: Target < 50% average across available cores (8 tests).
- **Goroutine Stability**: Ensures that concurrent operations are cleaned up correctly (8 tests).

**Target**: < 500MB memory, < 50% CPU.

## Scalability Testing

Tests the system's response to rapid growth in request volume or data size.

- **100 Concurrent Requests**: Sudden burst handling (8 tests).
- **1000 Requests/min**: Sustained high-volume traffic (8 tests).
- **Large Result Handling**: Validates performance when returning > 1MB of JSON data (8 tests).

**Target**: 100+ concurrent users, 1000+ requests per minute.

## Performance SLAs

The following table summarizes the primary performance targets for the Vectora system.

| Metric               | Target            |
| :------------------- | :---------------- |
| **p50 Latency**      | < 100ms           |
| **p95 Latency**      | < 500ms           |
| **p99 Latency**      | < 1s              |
| **Throughput**       | > 100 queries/sec |
| **Memory Usage**     | < 500MB           |
| **CPU Usage**        | < 50%             |
| **Concurrent Users** | > 50              |

## External Linking

| Concept        | Resource                          | Link                                                                               |
| :------------- | :-------------------------------- | :--------------------------------------------------------------------------------- |
| **Profiling**  | Go pprof Documentation            | [pkg.go.dev/net/http/pprof](https://pkg.go.dev/net/http/pprof)                     |
| **Latency**    | Understanding Latency Percentiles | [robertovitillo.com/percentiles/](https://www.robertovitillo.com/percentiles/)     |
| **Benchmarks** | Go Benchmarking Best Practices    | [dave.cheney.net/high-performance-go](https://dave.cheney.net/high-performance-go) |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
