---
title: DevOps Engineer - Daily/Weekly Routine
role: DevOps/Infrastructure Engineer
focus: CI/CD, build pipeline, Fly.io deployment, monitoring
---

# DevOps Engineer Routine

## Daily (10:00 AM UTC - Daily Standup)

**Before Standup** (5 min):

- [ ] Check CI/CD pipeline status
- [ ] Verify all builds passing
- [ ] Note any infrastructure alerts

**During Standup** (2 min):

- [ ] CI/CD status (any failures?)
- [ ] Infrastructure health?
- [ ] Any deployment blockers?

---

## Weekly Tasks

### Monday (Infrastructure Check)

**Morning** (1 hour):

- [ ] Verify GitHub Actions workflows working
- [ ] Check Fly.io staging/prod status
- [ ] Review build logs for errors
- [ ] Confirm no secret leaks in CI output

### Wednesday (Optimization)

**Morning** (1-2 hours):

- [ ] Optimize build time (target: < 30s)
- [ ] Review test execution time
- [ ] Check for flaky tests in CI
- [ ] Improve pipeline efficiency

### Friday (Deployment Readiness)

**Afternoon** (1 hour):

- [ ] Prepare for potential prod deployment
- [ ] Verify health checks working
- [ ] Review monitoring/alerting setup
- [ ] Plan infrastructure improvements

---

## Current Tasks

### Support 5 Critical Issues (Apr 28 - May 3)

**Ensure**:

- [ ] CI/CD pipeline passes all tests
- [ ] Build artifacts generated correctly
- [ ] No flaky tests blocking merges
- [ ] Deployment to staging ready (for Issue #002 MongoDB)

### GitHub Actions Workflow

**Current state** (verify working):

```yaml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-go@v4
        with:
          go-version: "1.22"
      - run: go fmt ./...
      - run: go vet ./...
      - run: go test ./...

  build:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: go build -o bin/vectora-cloud ./cloud/cmd/vectora-cloud
      - run: go build -o bin/vectora ./desktop/cmd/vectora
```

**Improvements needed**:

- [ ] Add code coverage reporting
- [ ] Add security scanning (gosec)
- [ ] Cache Go modules for faster builds
- [ ] Parallel test execution
- [ ] Build time < 30 seconds total

---

## Fly.io Deployment

**Staging Environment** (for testing):

- [ ] Service running at staging.vectora.dev
- [ ] Health checks passing (/health/live, /health/ready)
- [ ] Logs accessible via `flyctl logs`
- [ ] Env vars configured (JWT_SECRET, DATABASE_URL, etc.)

**Production Environment** (later, Issue #018-#020):

- [ ] Service running at api.vectora.dev
- [ ] Auto-deploy on main branch merge
- [ ] Monitoring and alerting setup
- [ ] Backup and recovery procedures

---

## Monitoring & Observability

**Current Targets**:

- [ ] Build success rate: 95%+ (catch flaky tests)
- [ ] Test execution time: < 30 seconds
- [ ] API latency: p99 < 100ms (when deployed)
- [ ] Error rate: < 0.1% (when deployed)

**Alerts to setup** (later):

- Build failure (any branch)
- Test coverage drop (< 80%)
- Deployment failure
- High error rate (> 1%)
- High latency (p99 > 200ms)

---

## Build Optimization Checklist

- [ ] Use Go module caching in CI
- [ ] Run tests in parallel (`-parallel` flag)
- [ ] Cache test results where possible
- [ ] Separate lint, test, build stages
- [ ] Remove unnecessary dependencies

**Example optimized workflow**:

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: actions/setup-go@v4
    with:
      go-version: "1.22"
      cache: true # Cache Go modules

  - run: go test -parallel 4 ./... # Parallel tests
  - run: go build -o bin/vectora-cloud ./cloud/cmd/vectora-cloud
```

---

## Deployment Checklist (for future)

**Before deploying to prod**:

- [ ] All tests passing
- [ ] Code coverage > 80%
- [ ] No security warnings
- [ ] Configuration validated
- [ ] Database migrations tested
- [ ] Monitoring/alerting ready
- [ ] Rollback plan documented

---

## Resources

- **GitHub Actions**: https://docs.github.com/en/actions
- **Fly.io Docs**: https://fly.io/docs/
- **Go Build Optimization**: https://golang.org/doc/effective_go#build_optimization
- **Taskfile.yml**: Build orchestration (check project root)

---

**Availability**: Always (monitoring infrastructure)
**Priority**: HIGH (CI/CD enables all dev work)
**Status**: MONITORING PIPELINE, OPTIMIZING BUILD TIME
