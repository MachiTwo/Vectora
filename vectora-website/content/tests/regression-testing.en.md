---
title: "Test Suite: Regression Testing"
slug: regression-testing
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - ast-parsing
  - auth
  - ci-cd
  - concepts
  - config
  - integration
  - mongodb-atlas
  - persistence
  - regression
  - system
  - testing
  - vector-search
  - vectora
---

{{< lang-toggle >}}

Bugs that have been fixed must not reappear, and known edge cases must continue to function correctly as the project evolves. This suite is continuous, executed with every commit to validate that fixes remain in place and that new changes do not reintroduce old problems.

By maintaining a robust regression suite, we ensure the long-term stability and reliability of the Vectora platform.

**Coverage**: Continuous | **Priority**: CRITICAL

## Previously Fixed Bugs

Every bug reported in issues that has been closed must have a corresponding regression test.

1. **Reproduction**: The test must be able to reproduce the original bug (before the fix).
2. **Validation**: The test must confirm that the fix is working as intended (after the fix).
3. **Persistence**: The test remains in the suite to prevent future regressions.

### Example Case Study: Issue #42

Consider a bug where search returns empty for special characters.

```text
Issue #42: "Search returns empty for special characters"

Test: TestSpecialCharacterSearch_Issue42
├─ Setup: Query with "C++", "C#", ".NET"
├─ Call: search_context("C++")
├─ Assert: Results returned (not empty)
└─ Rerun: Verified on every commit
```

## Common Integration Issues

We monitor several recurring technical challenges to ensure they do not degrade over time.

- Cache invalidation race conditions (5 tests).
- MongoDB connection pool exhaustion under load (5 tests).
- JWT token expiration during long-running queries (3 tests).
- Concurrent write conflicts and document versioning (5 tests).
- Detection of goroutine leaks in background workers (5 tests).

## Known Edge Cases

A dedicated set of tests for scenarios that are rare but critical for system robustness.

- Empty query and malformed intent handling (3 tests).
- Extremely large payloads (> 100MB) processing (2 tests).
- Deeply nested AST structures and circular dependencies (3 tests).
- Deleted files remaining in the vector index (2 tests).
- Concurrent namespace modifications and lock safety (3 tests).

## Compatibility & Maintenance

Ensures that Vectora remains stable across different versions and configuration formats.

- **Deprecated Features**: Validates that old endpoints or flags still function (with warnings).
- **Version Compatibility**: Checks for forward and backward compatibility of data formats.
- **Performance Baselines**: Monitors query latency and memory usage to detect performance regressions.

## CI/CD Integration

The regression suite is integrated into our automated development workflow.

### Pre-commit Verification

Ensures that major regressions are caught before the code even leaves the developer's machine.

```bash
pre-commit run regression-tests --all-files
```

### Automated Pipeline

Every commit pushed to the repository triggers the full regression suite.

```bash
# Regression tests must pass before merge
go test -race ./tests/regression/... -timeout 10m
```

### Weekly Stress Testing

An extended run designed to catch rare race conditions or memory leaks that only appear under prolonged load.

```bash
# Weekly extended regression testing
go test -race ./tests/regression/... -timeout 1h -stress
```

## Regression Test Criteria

The following table summarizes the primary targets for the regression testing suite.

| Criterion                  | Target         |
| :------------------------- | :------------- |
| **Coverage of Fixed Bugs** | 100%           |
| **Edge Cases Covered**     | > 90%          |
| **Performance Baseline**   | Maintained     |
| **Pass Rate**              | 100%           |
| **Execution Time (CI)**    | < 5 min        |
| **Stability**              | No flaky tests |

## External Linking

| Concept            | Resource                                       | Link                                                                                                       |
| ------------------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**  | Atlas Vector Search Documentation              | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**    | Tree-sitter Official Documentation             | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **JWT**            | RFC 7519: JSON Web Token Standard              | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                     |
| **GitHub Actions** | Automate your workflow from idea to production | [docs.github.com/en/actions](https://docs.github.com/en/actions)                                           |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
