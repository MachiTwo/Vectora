---
title: Backend Engineer - Daily/Weekly Routine
role: Backend Engineer
focus: APIs, storage, reliability, performance
---

# Backend Engineer Routine

## Daily (10:00 AM UTC - Daily Standup)

**Before Standup** (5 min):

- [ ] Check GitHub notifications on assigned issues
- [ ] Verify local build and tests are green
- [ ] Note any regressions or blockers

**During Standup** (2 min):

- [ ] Quick status: what was delivered, what is next, blockers

**After Standup**:

- [ ] Continue work on assigned subtask
- [ ] Test and commit frequently

---

## Weekly Assignment

### Week Planning

**Primary Focus**: Core backend delivery

**Your Subtasks**:

- API endpoints and request handling
- Storage and persistence changes
- Auth, validation, and middleware updates
- Performance and reliability improvements

**Timeline**:

- **Mon**: Review assigned issues and implementation plan
- **Tue/Wed**: Build and integrate backend changes
- **Wed/Thu**: Testing and verification
- **Fri**: PR ready for merge

---

## Technical Stack

**Language**: Go 1.22+
**Key Packages**:

- `context` (standard library)
- `database/sql` and storage drivers
- `net/http` / router stack used by the project

**Local Setup**:

```bash
cd backend
go mod download
go mod tidy
go build ./...
go test ./...
```

---

## Focus Areas

1. Keep backend code simple and testable
2. Prefer small, incremental changes
3. Preserve backward compatibility where possible
4. Coordinate with QA on regression coverage
5. Escalate architectural concerns to CTO early

---

## Testing Strategy

**Unit Tests**:

- Core storage operations
- Auth and validation logic
- API handlers and middleware

**Integration Tests**:

- Full request flow: create -> read -> update -> delete
- Error handling and edge cases

**Commands**:

```bash
go test ./backend/... -v
go test ./... # Full regression
go test -race ./... # Race detection
```

---

## Code Quality

**Before pushing**:

- [ ] `go test ./...` passes
- [ ] `go fmt ./...` clean
- [ ] `go vet ./...` no issues
- [ ] `go test -race ./...` passes

**Commit message**:

```text
feat(backend): implement backend improvement
```

---

## Collaboration

**Paired with CTO** on architecture decisions:

- Backend leads implementation
- CTO validates design and quality
- QA verifies regression coverage
- CDO may request docs updates after changes

---

## Resources

- [CONTRIBUTORS-PROMPTS.md](../../CONTRIBUTORS-PROMPTS.md) - System prompts completos
- [CONTRIBUTORS.md](../../CONTRIBUTORS.md) - Team structure
