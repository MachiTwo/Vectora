# Issues - Quality and Delegation Standard

This file defines the standard for creating, documenting, and delegating issues in Vectora.

---

## File Standard

### Naming

- Format: `NNN-title-in-lowercase-with-hyphens.md`
- Number: 3 digits, increasing order
- Title: lowercase, hyphen-separated, concise, and descriptive
- Example: `001-implement-authmiddleware.md`

### Required Structure

```markdown
# [NNN] Issue Title

**Number:** NNN
**Status:** OPEN / IN_PROGRESS / BLOCKED / REVIEW / DONE
**Priority:** CRITICAL / HIGH / MEDIUM / LOW
**Assigned to:** [ROLE]
**Estimated effort:** X-Y hours
**Deadline:** Date
**Created at:** Date
**Updated at:** Date

---

## Description

[Clear paragraph describing the problem, context, and impact]

---

## Goal

[What needs to be done and why]

---

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Code review approved
```

---

## Delegation Map

### Leadership

- CEO - hiring, strategy, OKRs, go-to-market
- CTO - architecture reviews, code quality, standards
- CDO - documentation ownership, AI/ML strategy, data governance
- CMO - positioning, community, announcements

### Engineering

- Backend Engineer - APIs, databases, scaling
- AI Backend Engineer - runtime, retrieval, inference
- AI/ML Engineer - models, quantization, optimization
- Security Engineer - auth, encryption, audit
- DevOps Engineer - CI/CD, infrastructure, monitoring
- QA Engineer - testing, coverage, validation
- Frontend Engineer - UI, dashboard, web interactions
- Integrations Engineer - plugins, extensions, external tool connectors

### Other

- Community and hiring support can be routed through CEO or CMO when needed.

---

## Lifecycle

OPEN -> IN_PROGRESS -> REVIEW -> DONE

BLOCKED returns to IN_PROGRESS when the blocker is resolved.

---

## Update Protocol

- Update issue status weekly.
- Record progress whenever status changes.
- Keep the delegation target explicit.

---

## Quality Rules

- Always assign a specific role.
- Use measurable acceptance criteria.
- Include dependencies when relevant.
- Keep deadlines explicit.

---

**Last update:** 2026-05-03
**Maintained by:** CTO / CDO
