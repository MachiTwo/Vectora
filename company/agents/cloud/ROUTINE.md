---
title: Backend Engineer (Cloud) - Daily/Weekly Routine
role: Backend Engineer
focus: Cloud API, storage, authentication, gRPC
---

# Backend Engineer (Cloud) Routine

## Daily (10:00 AM UTC - Daily Standup)

**Before Standup** (5 min):

- [ ] Check GitHub notifications on assigned issues
- [ ] Note any test failures or linting issues
- [ ] Review PR feedback (if waiting for review)

**During Standup** (2 min):

- [ ] What did I accomplish yesterday?
- [ ] What am I working on today?
- [ ] Any blockers or help needed?

**After Standup** (as needed):

- [ ] Start coding on assigned subtask
- [ ] Test locally before pushing
- [ ] Open PR when ready for review

---

## Weekly Tasks

### Monday (Receive Assignment)

**Morning** (30 min):

- [ ] Meet with Lead Engineer (1-on-1)
- [ ] Clarify which issue/subtask to work on
- [ ] Review acceptance criteria
- [ ] Ask questions about design/requirements
- [ ] Check if TCO design review scheduled

**Afternoon**:

- [ ] Start subtask 1 of assigned issue
- [ ] Setup local environment if needed
- [ ] Create feature branch: `feature/issue-XXX-subtask-name`

### Daily (Mon-Fri)

**Morning** (6-7 hours coding):

- [ ] Work on assigned subtask
- [ ] Write tests as you code (TDD)
- [ ] Commit frequently (every 30-60 min)
- [ ] Keep local tests passing: `go test ./...`

**Afternoon** (1-2 hours):

- [ ] Code review: Review PRs from teammates
- [ ] Design feedback: Ask TCO questions if stuck
- [ ] PR management: Push code, request review
- [ ] Debugging: Fix any failing tests

**End of day** (15 min):

- [ ] Verify tests passing locally
- [ ] Commit any remaining changes
- [ ] Push to feature branch
- [ ] Update GitHub issue (comment on progress)

### Friday (Closeout)

**Afternoon** (1 hour):

- [ ] Finish all PRs (target: merged by EOD)
- [ ] Verify tests passing on CI/CD
- [ ] One-on-one debrief with Lead Engineer
  - What went well?
  - What was challenging?
  - What do you need next week?

---

## Current Assignment

### Issue #001: AuthMiddleware Implementation (6-8h total)

**Your Part**: All 4 subtasks (as primary owner)

| Subtask                | Duration | Status  | Target  |
| ---------------------- | -------- | ------- | ------- |
| 2.1: JWT Authenticator | 1.5h     | PENDING | Mon EOD |
| 2.2: API Key Validator | 1h       | PENDING | Tue AM  |
| 2.3: Update Middleware | 1.5h     | PENDING | Tue/Wed |
| 2.4: Register Routes   | 1h       | PENDING | Wed EOD |

**Daily Plan**:

- **Mon**: Complete 2.1 + 2.2 (JWT + API Key, with tests)
- **Tue**: Complete 2.3 (Middleware update, integration tests)
- **Wed**: Complete 2.4 (Route registration, full integration test)
- **Thu/Fri**: Code review + merge to main

---

## Technical Stack

**Language**: Go 1.22+
**Key Packages**:

- `github.com/golang-jwt/jwt/v5` (JWT)
- `net/http` (standard library)
- `context` (standard library)
- `sync.RWMutex` (thread safety)

**Local Setup**:

```bash
# Clone repo
git clone https://github.com/Kaffyn/Vectora.git
cd Vectora/cloud

# Install deps
go mod download
go mod tidy

# Run tests
go test ./...

# Build
go build -o ../bin/vectora-cloud ./cmd/vectora-cloud
```

---

## Code Quality Standards

**Before pushing code**:

- [ ] All tests pass: `go test ./...`
- [ ] No linting errors: `go fmt ./...` + `go vet ./...`
- [ ] No race conditions: `go test -race ./...`
- [ ] Code coverage good: `go test -cover ./...` (target: 80%+)
- [ ] Commit message clear: `[Issue #XXX.Y] Short description`

**PR Template**:

```markdown
## Issue

Closes #001 (AuthMiddleware Implementation)

## Changes

- Created JWT authenticator in cloud/internal/auth/jwt.go
- Created API Key validator in cloud/internal/auth/api_key.go
- Updated AuthMiddleware to validate both JWT and API Key

## Testing

- [ ] Added unit tests for JWT validation (3 cases)
- [ ] Added unit tests for API Key validation (2 cases)
- [ ] Integration test: request without auth → 401
- [ ] All tests pass: go test ./cloud/internal/auth/

## Notes

Ready for TCO design review. No external dependencies added.
```

---

## Testing Requirements

**Unit Tests** (required for each subtask):

- Happy path (valid input)
- Error cases (invalid input)
- Edge cases (empty strings, nil pointers, etc.)

**Integration Tests** (required):

- Full HTTP request flow with middleware
- Unauthenticated request → 401
- Authenticated request → proceeds

**Run before pushing**:

```bash
go test ./cloud/internal/auth/ -v
go test ./cloud/internal/api/middleware_test.go -v
go test ./... # Full project regression
```

---

## Design Guidance

**For Issue #001 (AuthMiddleware)**:

1. **JWT Validation**:

   - Extract "Bearer <token>" from Authorization header
   - Use golang-jwt/jwt to parse and validate
   - Return Claims struct with UserID, Role, etc.
   - Reject invalid signatures, expired tokens

2. **API Key Validation**:

   - Extract "ApiKey <key>" from Authorization header
   - Lookup key in in-memory map (thread-safe with RWMutex)
   - Return UserID and Role for key

3. **Middleware Integration**:

   - Try JWT first (Bearer tokens most common)
   - Fallback to API Key if JWT fails
   - Inject claims into request context (key: "claims")
   - Return 401 Unauthorized if both fail

4. **Test Coverage**:
   - Valid JWT → context populated
   - Valid API Key → context populated
   - Missing auth → 401
   - Invalid token → 401

---

## Communication

**Get help from**:

- **Design questions**: Escalate to TCO (Slack: @tco)
- **Blockers**: Tell Lead Engineer immediately (5 min conversation)
- **Code review**: Request from Lead Engineer or TCO
- **Testing help**: Pair with QA Engineer if stuck

**Post updates**:

- Daily standup (10 AM UTC)
- GitHub issue comments (progress, blockers, decisions)
- Friday 1-on-1 with Lead Engineer

---

## Metrics to Track

| Metric                | Target           | Progress |
| --------------------- | ---------------- | -------- |
| Issue #001 completion | 100% by Wed      | TBD      |
| Test coverage         | 80%+             | TBD      |
| PR review time        | < 24h            | TBD      |
| Code quality          | 0 linting errors | TBD      |
| Blockers resolved     | Same-day         | TBD      |

---

## Escalation

**If blocked**:

1. Spend 15 min debugging/researching
2. Ask Lead Engineer or TCO (Slack/quick sync)
3. If design unclear: Schedule 30 min sync with TCO
4. Never spin wheels > 30 min without asking for help

**If complexity higher than expected**:

- Tell Lead Engineer immediately
- Adjust timeline if needed
- May get help from Desktop Engineer or QA

---

## Resources

- **Code Reference**: `ISSUES.md` section #2 (lines 117-251)
- **Task Details**: `TASK-ANTIGRAVITY.md` section Task #2 (lines 47-309)
- **API Docs**: `docs/api.md` (when available)
- **JWT Guide**: https://jwt.io/introduction

---

**Start Date**: 2026-04-29 (Monday)
**Target Completion**: 2026-05-01 (Wednesday)
**Status**: PENDING START
