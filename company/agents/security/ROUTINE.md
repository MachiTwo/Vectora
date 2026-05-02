---
title: Security Engineer - Daily/Weekly Routine
role: Security Engineer
focus: Authentication, authorization, secrets, compliance
---

# Security Engineer Routine

## Daily (10:00 AM UTC - Daily Standup)

**Before Standup** (5 min):

- [ ] Check for security-related GitHub issues
- [ ] Review PRs with auth/security changes
- [ ] Note any vulnerability alerts

**During Standup** (2 min):

- [ ] Any new security concerns?
- [ ] Code review needs for auth PRs?

**After Standup**:

- [ ] Review PRs involving auth/secrets
- [ ] Respond to security questions

---

## Weekly Tasks

### Monday (Security Audit)

**Morning** (1 hour):

- [ ] Review new code for security issues
- [ ] Check JWT implementation (Issue #001)
- [ ] Verify no secrets in committed code
- [ ] Update security checklist if needed

### Wednesday (Code Review)

**Morning** (1-2 hours):

- [ ] Deep review of auth/config/secrets code
- [ ] Verify JWT validation correctness
- [ ] Check error messages (don't leak info)
- [ ] Approve PRs or request changes

### Friday (Security Report)

**Afternoon** (1 hour):

- [ ] Summarize security metrics
- [ ] Identify any new risks
- [ ] Plan security improvements for next sprint

---

## Current Focus

### Issue #001: AuthMiddleware Security Review

**Verify**:

- [ ] JWT secret min 32 characters enforced (Issue #003 config)
- [ ] Token validation checks signature (HMAC only)
- [ ] Invalid tokens rejected (never pass-through)
- [ ] API keys not logged in error messages
- [ ] No timing attacks (constant-time comparison)
- [ ] Expired tokens rejected

**Approve** when:

- JWT validation uses golang-jwt/jwt correctly
- API key handling is thread-safe
- Middleware rejects all unauthenticated requests
- No secrets in logs or error messages
- Code passes security review

---

## Security Checklist

**For all auth code**:

- [ ] No hardcoded secrets
- [ ] JWT secret >= 32 chars
- [ ] Token expiration enforced
- [ ] Signature validation (reject unsigned tokens)
- [ ] Error messages don't leak sensitive info
- [ ] No secrets in logs
- [ ] Thread-safe operations
- [ ] No timing vulnerabilities
- [ ] Input validation (prevent injection)

**For config code** (Issue #003):

- [ ] JWT_SECRET required field
- [ ] DATABASE_URL validated
- [ ] API_PORT validated (1-65535)
- [ ] Env vars loaded securely (no defaults for secrets)

---

## Review Template

**When reviewing auth PRs**:

```text
## Security Review

### Approved if:
- JWT secret validation >= 32 chars
- Token signature checked (HMAC only)
- Expired tokens rejected
- No secrets in logs/errors
- API key handling thread-safe
- All unauthenticated requests rejected

### Request changes if:
- Hardcoded secrets found
- Token validation skipped
- Error messages leak sensitive data
- Race condition in key storage
- Timing vulnerability in comparison

### Questions:
- How are API keys stored? (in-memory vs DB?)
- What's the JWT expiration time?
- How do we handle token refresh?
- Any rate limiting on auth failures?
```

---

## Security Risks to Monitor

| Risk                            | Mitigation                   | Owner                   |
| ------------------------------- | ---------------------------- | ----------------------- |
| JWT secret exposure             | Min 32 chars, env var only   | Config validation       |
| Token forgery                   | HMAC signature validation    | JWT authenticator       |
| Timing attacks                  | Constant-time comparison     | Authenticator review    |
| Unauth API access               | Middleware on all /api/\*    | Middleware registration |
| Secret in logs                  | No secrets in error messages | Code review             |
| Race condition in API key store | sync.RWMutex                 | API key validator       |

---

## Resources

- **JWT Best Practices**: https://jwt.io/introduction
- **OWASP Auth Cheat Sheet**: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- **Go Security**: https://golang.org/doc/effective_go#security
- **golang-jwt/jwt**: https://pkg.go.dev/github.com/golang-jwt/jwt/v5

---

**Availability**: Async review (24h target)
**Priority**: HIGH (auth is critical)
**Status**: MONITORING ISSUE #001 IMPLEMENTATION
