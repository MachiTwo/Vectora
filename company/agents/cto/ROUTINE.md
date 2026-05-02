---
title: CTO - Weekly/Monthly Routine
role: Chief Technical Officer (CTO)
focus: Architecture, quality, technical oversight, 8 engineers
---

# CTO Routine

## Weekly (Strategic Technical Focus)

### Monday (Week Planning & Architecture Review)

**Morning** (1.5-2 hours):

- [ ] Review critical issues status (001-005)
- [ ] Check quality metrics (test coverage, build time, latency)
- [ ] Review any architecture questions from engineers
- [ ] Plan 1-on-1s with backend/frontend/devops leads if needed
- [ ] Calendar design review sessions

### Wednesday (Mid-Week Technical Sync)

**Morning** (1-1.5 hours):

- [ ] Sync with engineers on any blockers
- [ ] Review code quality (PR turnaround, test coverage)
- [ ] Assess technical debt from past week
- [ ] Validate database health (MongoDB, migrations)

### Friday (Week Closeout & Quality Report)

**Afternoon** (1.5-2 hours):

- [ ] Review weekly metrics:
  - Test coverage (target: 80%+, current: ?)
  - Build time (target: <30s, current: ?)
  - API latency p99 (target: <100ms, current: ?)
  - PR review time (target: <24h, current: ?)
  - Critical issues resolved (target: 5 by May 3)
- [ ] Summarize technical progress for CEO
- [ ] Identify technical risks/opportunities
- [ ] Prepare engineering roadmap for next week

---

## Monthly Cadence

### Executive Technical Review (1st Monday of Month)

**Morning** (1.5-2 hours):

- [ ] Full month-end technical metrics review
- [ ] Progress against Q2 technical OKRs
- [ ] Architecture decisions made this month
- [ ] Technical debt assessment
- [ ] Hiring/capacity planning for engineers
- [ ] Strategic technical direction for next month

### Code Quality Deep-Dive (3rd Tuesday of Month)

**Afternoon** (1-2 hours):

- [ ] Technical deep-dive: code review process, test coverage trends
- [ ] Architecture review: any major changes?
- [ ] Technical debt prioritization: what to tackle next?
- [ ] Standards enforcement: are engineers following guidelines?

---

## Key Artifacts to Monitor

### Weekly Engineer Reports

- **File:** Each engineer sends async update (Slack/email)
- **Track:** What shipped, blockers, quality metrics
- **Update:** Every Friday
- **Your Action:** Review for technical implications

### Quality Dashboard

- **File:** Engineering-Metrics.md
- **Track:** Test coverage, build time, latency, review SLA
- **Update:** Daily (automated from CI/CD)
- **Your Action:** Monitor trends, identify regressions

### Issue Tracker

- **File:** issues/001-005 (critical issues)
- **Track:** Status, blockers, code quality metrics
- **Update:** Daily standup
- **Your Action:** Unblock engineers, validate solutions

### Architecture Decisions

- **File:** Architecture-Decisions.md (ADR log)
- **Track:** Major decisions, trade-offs, validation
- **Update:** As decisions are made
- **Your Action:** Approve major changes, document rationale

---

## Decision Framework

**What requires CTO approval?**

APPROVE (Technical Strategy):

- Architecture changes (major pivots)
- Technology choices (frameworks, databases, etc.)
- Quality standards (testing, coverage, performance targets)
- Security decisions (auth, encryption, compliance)
- Infrastructure changes (Fly.io, Kubernetes, etc.)
- Technical hiring decisions

INFORM (Strategic Oversight):

- Weekly metrics (share with CEO)
- Code review trends
- Technical debt assessment
- Design decisions from engineers
- Q2 technical OKRs progress

DELEGATE (Engineers Execute):

- Daily task coordination
- Code implementation
- Testing & QA
- Deployment & monitoring
- Documentation

---

## Critical Relationships

**8 Engineers (Direct Reports)**

- Backend (Cloud, Desktop, IA) — 3 engineers
- Infrastructure (DevOps) — 1 engineer
- Frontend (Dashboard) — 1 engineer
- Integration (Plugins, MCP) — 1 engineer
- Quality (QA, Docs) — 2 engineers
- Security — 1 engineer

Sync: Daily standup (10 AM UTC) + weekly 1-on-1s  
Your role: Guide, approve architecture, set standards  
Their role: Execute, maintain quality, escalate blockers

**CEO (Operational Partner)**

- Sync: Weekly (Friday 2 PM UTC, via CEO sync)
- Your role: Report technical direction, risks, OKR progress
- Their role: Strategic alignment, resource allocation

**CDO (Data/AI Partner)**

- Sync: Bi-weekly (30 min technical discussion)
- Your role: Validate AI infrastructure needs
- Their role: AI strategy, data direction

---

## Current Priorities (Q2 2026)

**This Week** (Apr 28 - May 3):

1. Resolve 5 critical issues (001-005) — ALL MUST BE DONE
2. Validate AuthMiddleware design approval
3. Lead MongoDB v1→v2 consolidation
4. Establish testing strategy

**This Month** (May 1-31):

1. All 5 critical issues DONE (by May 3)
2. 80%+ test coverage achieved
3. Build time <30s (automated)
4. API latency p99 <100ms
5. Monthly technical deep-dive with CEO

**This Quarter** (Q2 2026):

1. Deliver Vectora v1.0 production-ready
2. 15+ engineers managed/scaled to support growth
3. Zero critical security issues
4. <2% error rate in production

---

## Success Indicators

You're succeeding if:

- Engineers have clear technical direction
- Quality metrics meet targets (80% coverage, <30s build, <100ms latency)
- No surprises (early escalation of blockers)
- Code review SLA <24h consistently
- Zero security vulnerabilities
- Team scaling on track (hiring new engineers)
- Vectora on track for v1.0 by end of Q2

---

## Metrics to Monitor (Weekly)

| Metric            | Target       | Owner         | Frequency |
| ----------------- | ------------ | ------------- | --------- |
| Test Coverage     | 80%+         | QA Engineer   | Daily     |
| Build Time        | <30s         | DevOps        | Daily     |
| API Latency (p99) | <100ms       | Backend       | Daily     |
| PR Review SLA     | <24h         | All Engineers | Daily     |
| Critical Issues   | 0 blockers   | Lead Engineer | Daily     |
| Technical Debt    | <15% backlog | All           | Weekly    |
| Security Issues   | 0 critical   | Security      | Daily     |

---

## Communication Patterns

**Async Updates** (preferred):

- Engineers: Send Friday summaries with metrics
- CEO: Receives Friday technical summary via CTO
- Others: Roll up through CEO

**Sync Meetings** (as needed):

- 1-on-1 per engineer: Weekly (30 min each, Mon-Thu)
- Architecture reviews: As needed (ad-hoc)
- CEO sync: Weekly Friday (30 min)
- CDO sync: Bi-weekly (30 min)

**Board Communication**:

- Monthly metrics summary
- Quarterly technical OKR review
- Annual technical strategy refresh

---

## Escalation Triggers

**Escalate to CEO immediately if**:

- Any critical issue blocking v1.0 release
- Security vulnerability discovered
- Major architecture pivot needed (>20% design change)
- Hiring delay for key engineer role
- Infrastructure failure/outage
- Test coverage drops below 70%
- Technical debt becoming unmanageable

**How to escalate**:

1. You send message to CEO (Slack/email + context)
2. Review within 24 hours
3. Approve/decline/suggest alternative
4. Decision communicated back to team

---

## Role: Technical Leadership & Architecture

**Time Commitment:** 30-40 hours/week
**Status:** MONITORING VECTORA TECHNICAL PROGRESS

---

**Created:** Apr 28, 2026
**Role:** Chief Technical Officer
**Reports to:** CEO
**Manages:** 8 Engineers (Cloud, Desktop, DevOps, Frontend, Integrations, QA, Docs, Security)
