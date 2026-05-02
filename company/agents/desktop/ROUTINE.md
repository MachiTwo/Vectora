---
title: Desktop Engineer - Daily/Weekly Routine
role: Desktop Engineer
focus: Desktop daemon, system tray, MCP client
---

# Desktop Engineer Routine

## Daily (10:00 AM UTC - Daily Standup)

**Before Standup** (5 min):

- [ ] Check GitHub notifications on assigned issues
- [ ] Test locally that code still builds/runs
- [ ] Note any test failures

**During Standup** (2 min):

- [ ] Quick status: What did I do? What's next? Blockers?

**After Standup**:

- [ ] Continue work on assigned subtask
- [ ] Test and commit frequently

---

## Weekly Assignment

### Week of Apr 28 - May 3

**Primary Focus**: Issue #002 (MongoDB v1 → v2 Migration)

**Your Subtasks**:

- 1.1: Update `desktop/go.mod` to v2.5.1 (1h)
- 1.2: Migrate storage imports to v2 APIs (2-3h)
- 1.3: Verify Desktop storage compliance (team effort with Backend)

**Timeline**:

- **Mon**: Update go.mod, identify all imports needing migration
- **Tue/Wed**: Execute migration (imports, SessionContext → context.Context)
- **Wed/Thu**: Testing and verification
- **Fri**: PR ready for merge

---

## Technical Stack

**Language**: Go 1.22+
**Key Packages**:

- `go.mongodb.org/mongo-driver/v2` (MongoDB driver v2)
- `context` (standard library)
- `os` / `sys` (Windows system APIs)

**Local Setup**:

```bash
cd desktop
go mod download
go get -u go.mongodb.org/mongo-driver@v2.5.1
go mod tidy
go build ./...
go test ./...
```

---

## Issue #002 Details

**What to do**:

1. Update MongoDB driver from v1.17.9 to v2.5.1
2. Update all import paths in storage code
3. Replace `mongo.SessionContext` → `context.Context`
4. Run tests to catch any issues

**Key Changes**:

```go
// BEFORE (v1)
import "go.mongodb.org/mongo-driver/mongo"
import "go.mongodb.org/mongo-driver/bson"

func (s *Store) Insert(ctx mongo.SessionContext, doc interface{}) error {
    // ...
}

// AFTER (v2)
import "go.mongodb.org/mongo-driver/v2/mongo"
import "go.mongodb.org/mongo-driver/v2/bson"

func (s *Store) Insert(ctx context.Context, doc interface{}) error {
    // ...
}
```

**Files to modify**:

- `desktop/go.mod` — Update MongoDB version
- `desktop/internal/storage/*.go` — Update imports + SessionContext
- `desktop/internal/storage/*_test.go` — Update tests

---

## Migration Checklist

- [ ] `go get -u go.mongodb.org/mongo-driver@v2.5.1`
- [ ] `go mod tidy`
- [ ] Find all files with `mongo-driver` imports
- [ ] Update `go.mongodb.org/mongo-driver` → `go.mongodb.org/mongo-driver/v2`
- [ ] Update `mongo-driver/bson` → `mongo-driver/v2/bson`
- [ ] Replace `mongo.SessionContext` → `context.Context`
- [ ] Replace `mongo.Session` → context + custom middleware
- [ ] Update `InsertMany` return type handling
- [ ] Run `go test ./...` (all tests pass)
- [ ] Run `go build ./...` (no errors)
- [ ] Code review + merge

---

## Testing Strategy

**Unit Tests**:

- Storage operations (Insert, Find, Delete) still work
- Use mocks for MongoDB (or testcontainers)

**Integration Tests**:

- Full workflow: Create → Read → Delete

**Commands**:

```bash
go test ./desktop/internal/storage/ -v
go test ./... # Full regression
go test -race ./... # Race detection
```

---

## Code Quality

**Before pushing**:

- [ ] `go test ./...` passes
- [ ] `go fmt ./...` clean
- [ ] `go vet ./...` no issues
- [ ] `-race` flag: `go test -race ./...`

**Commit message**:

```text
[Issue #002.2] Migrate Desktop storage to MongoDB v2 APIs

- Update imports to go.mongodb.org/mongo-driver/v2
- Replace SessionContext with context.Context
- Update BSON import paths
- All storage tests passing
```

---

## Collaboration

**Paired with Backend Engineer** on MongoDB migration:

- Backend leads the strategy
- Desktop executes Desktop-specific changes
- Sync mid-week (Wed) to verify approach consistency
- Backend will handle Cloud storage (you do Desktop)

**Support available**:

- **Design questions**: Ask Backend or TCO
- **Blockers**: Tell Lead Engineer
- **Test help**: Pair with QA Engineer

---

## Escalation

**If MongoDB v2 API confusing**:

1. Check official docs: https://pkg.go.dev/go.mongodb.org/mongo-driver/v2
2. Ask Backend Engineer (they're doing same work)
3. Escalate to TCO if design question

**If bigger than expected**:

- Tell Lead Engineer ASAP
- May get help from Backend Engineer
- Adjust timeline if needed

---

## Resources

- **Issue Details**: `ISSUES.md` section #1 (lines 23-110)
- **Task Breakdown**: `TASK-ANTIGRAVITY.md` Task #1 (lines 311-482)
- **MongoDB v2 Docs**: https://pkg.go.dev/go.mongodb.org/mongo-driver/v2
- **Breaking Changes**: https://docs.mongodb.com/drivers/go/current/upgrade/

---

## Next Week

**Week of May 6-10**:

- **If #001 + #002 complete**: Start Issue #005 (GoMock) or support Issues #003/#004
- **If #002 delayed**: Continue migration work + testing
- **New engineer onboarding support** (if hired)

---

**Start Date**: 2026-04-29 (Monday)
**Target Completion**: 2026-05-02 (Thursday)
**Status**: PENDING START
