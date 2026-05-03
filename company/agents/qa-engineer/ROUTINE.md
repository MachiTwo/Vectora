---
title: QA Engineer - Daily/Weekly Routine
role: QA Engineer
focus: Testing, quality gates, coverage
---

# QA Engineer Routine

## Daily (10:00 AM UTC - Daily Standup)

**Before Standup** (5 min):

- [ ] Check test results from last day's CI/CD
- [ ] Review PR test coverage reports
- [ ] Note any regressions

**During Standup** (2 min):

- [ ] Status on testing work
- [ ] Help needed from engineers?
- [ ] Any test coverage gaps?

**After Standup**:

- [ ] Implement tests for completed subtasks
- [ ] Review test coverage changes
- [ ] Add regression tests if needed

---

## Weekly Tasks

### Monday (Test Planning)

**Morning** (1 hour):

- [ ] Review newly assigned issues (Issues #001-#005)
- [ ] Plan testing strategy for each issue
- [ ] Identify test gaps
- [ ] Coordinate with engineers on test requirements

**Afternoon**:

- [ ] Setup test infrastructure (if needed)
- [ ] Create test templates/fixtures
- [ ] Prepare mocking strategy

### Daily (Mon-Fri)

**Morning** (3-4 hours):

- [ ] Implement unit tests for completed subtasks
- [ ] Run `go test ./...` frequently
- [ ] Monitor test coverage (target: 80%+)
- [ ] Add integration tests for critical flows

**Afternoon** (2-3 hours):

- [ ] Code review: Verify engineer tests are complete
- [ ] Review test coverage reports
- [ ] Identify regression risks
- [ ] Help engineers debug failing tests

### Friday (Quality Summary)

**Afternoon** (1.5 hours):

- [ ] Generate final test coverage report
- [ ] Document test results
- [ ] Identify test gaps for next week
- [ ] One-on-one with Lead Engineer

---

## Current Assignment

### Issues #001-#005: Testing Strategy

**For Issue #001 (AuthMiddleware)**:

- [ ] Unit tests for JWT validation (3+ cases)
- [ ] Unit tests for API Key validation (2+ cases)
- [ ] Integration tests for middleware (4+ cases)
- [ ] Target coverage: 90%+ for auth package

**For Issue #002 (MongoDB Migration)**:

- [ ] Verify existing storage tests still pass
- [ ] Update tests for v2 API changes
- [ ] Add regression tests for SessionContext → context.Context
- [ ] Test on the backend path only

**For Issues #003-#005 (Config/Logging/GoMock)**:

- [ ] Unit tests per issue requirements
- [ ] Integration tests for startup/runtime behavior
- [ ] Performance tests if applicable

---

## Testing Framework & Tools

**Built-in Go Testing**:

- `testing` package (standard library)
- `go test ./...` to run all tests
- `-race` flag to detect race conditions
- `-cover` flag to measure coverage

**Testing Best Practices**:

```go
func TestJWTValidation(t *testing.T) {
    // Arrange: Setup test data
    authenticator := NewJWTAuthenticator("test-secret-that-is-long-enough")
    validToken := createTestToken("user-123", "admin")

    // Act: Execute function
    claims, err := authenticator.ValidateToken(validToken)

    // Assert: Verify results
    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }
    if claims.UserID != "user-123" {
        t.Errorf("got %s, want user-123", claims.UserID)
    }
}
```

**Test File Structure**:

- Store tests alongside source: `file.go` + `file_test.go`
- Use table-driven tests for multiple cases
- Use `testify/assert` for cleaner assertions (if preferred)

---

## Quality Metrics Dashboard

**Track Weekly** (update every Friday):

```text
Quality Metrics (Week of Apr 28)

Test Coverage:
- Backend: 70% (target: 80%)
  - auth: 90%
  - storage: 65%
  - api: 60%

Build Success Rate: 100% (all CI/CD runs pass)

Test Execution Time:
- Backend: 12s (target: < 20s)

Regression Tests: 0 failures (target: 0)

Code Review Feedback:
- Test quality: 8/10 (clear, thorough)
- Coverage gaps: 2 identified
- Next week: Improve storage test coverage
```

---

## Testing Checklist

**For each completed subtask**:

- [ ] Unit tests written (happy path + error cases)
- [ ] Tests pass locally: `go test ./...`
- [ ] No race conditions: `go test -race ./...`
- [ ] Coverage acceptable: `go test -cover ./...` (80%+)
- [ ] Mocks used appropriately (mock external deps, test behavior)
- [ ] Error handling tested
- [ ] Edge cases covered (nil, empty, out-of-range, etc.)

**Before code review**:

- [ ] Code review: Verify engineer's tests are thorough
- [ ] No duplicate/overlapping tests
- [ ] Test names are descriptive
- [ ] Comments explain complex test logic

---

## Code Review Feedback

**When reviewing engineer PRs**:

** Good test**:

```go
func TestValidateTokenWithExpiredToken(t *testing.T) {
    // Clear intent: expired token should fail
    authenticator := NewJWTAuthenticator(testSecret)
    expiredToken := createTestToken("user-123", "admin", -1 * time.Hour)

    _, err := authenticator.ValidateToken(expiredToken)

    if err == nil {
        t.Error("expected error for expired token, got nil")
    }
}
```

** Poor test**:

```go
func TestAuth(t *testing.T) {
    // Unclear what's being tested
    // Missing edge cases
    auth := NewJWTAuthenticator("secret")
    token, _ := auth.MakeToken("user", "admin")
    _, err := auth.ValidateToken(token)
    if err != nil {
        t.Fatal(err)
    }
}
```

---

## Mocking Strategy

**For Issue #005 (GoMock Integration)**:

**Your responsibility**:

- [ ] Ensure engineers use GoMock generated mocks
- [ ] Verify mock expectations are clear
- [ ] No manual mocks remain (except test fixtures)
- [ ] Mock usage is consistent across codebase

**Example with GoMock**:

```go
func TestDocumentCreation(t *testing.T) {
    ctrl := gomock.NewController(t)
    defer ctrl.Finish()

    mockDB := storagemocks.NewMockDatabase(ctrl)
    mockDB.EXPECT().
        InsertOne(gomock.Any(), "documents", gomock.Any()).
        Return("doc-123", nil).
        Times(1) // Verify called exactly once

    handler := NewDocumentHandler(mockDB)
    result, err := handler.Create(context.Background(), `{"name": "test"}`)

    // GoMock verifies expectations automatically
    if result != "doc-123" {
        t.Errorf("got %s, want doc-123", result)
    }
}
```

---

## Performance Testing

**For latency-sensitive code** (like API endpoints):

```go
func BenchmarkJWTValidation(b *testing.B) {
    authenticator := NewJWTAuthenticator(testSecret)
    token := createTestToken("user-123", "admin")

    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        _, _ = authenticator.ValidateToken(token)
    }
}

// Run: go test -bench=. ./backend/internal/auth/
// Target: < 1ms per validation
```

---

## Escalation

**If engineer's code is untestable**:

1. Ask engineer to refactor for testability (DI, interfaces)
2. Escalate to TCO if design needs feedback
3. Never accept code that can't be tested

**If test coverage dropping**:

1. Alert Lead Engineer
2. Require explanation in PR
3. Target: Maintain 80%+ coverage

**If tests are slow** (> 30s to run):

1. Identify slow tests
2. Consider parallelization or optimization
3. Mock external calls (DB, API) to speed up

---

## Resources

- **Go Testing**: https://pkg.go.dev/testing
- **GoMock**: https://github.com/uber-go/mock
- **Table-Driven Tests**: https://github.com/golang/go/wiki/TableDrivenTests
- **Test Best Practices**: https://golang.org/doc/effective_go#testing

---

## Success Metrics

| Metric               | Target                | Progress |
| -------------------- | --------------------- | -------- |
| Test Coverage        | 80%+                  | TBD      |
| Test Pass Rate       | 100%                  | TBD      |
| Build Success Rate   | 95%+                  | TBD      |
| Regression Tests     | 0 failures            | TBD      |
| Code Review Feedback | 0 test quality issues | TBD      |

---

**Start Date**: 2026-04-29 (Monday)
**Focus**: Support implementation of Issues #001-#005 with testing
**Status**: READY TO START
