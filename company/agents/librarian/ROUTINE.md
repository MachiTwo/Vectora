---
title: Librarian (Docs Engineer) - Daily/Weekly Routine
role: Documentation Engineer
focus: Technical documentation, Hugo/Hextra site, SEO
---

# Librarian Routine

## Daily (10:00 AM UTC - Daily Standup)

**Before Standup** (5 min):
- [ ] Check for docs-related PRs/issues
- [ ] Note any new features needing documentation

**During Standup** (1 min):
- [ ] Any new docs needed from engineers?
- [ ] Blockers on documentation?

---

## Weekly Tasks

### Monday (Documentation Planning)

**Morning** (1 hour):
- [ ] Review completed code (PRs merged)
- [ ] Identify docs needed
- [ ] Prioritize docs by importance
- [ ] Plan which docs to write this week

### Daily (Mon-Fri)

**Morning** (2-3 hours):
- [ ] Write/update technical documentation
- [ ] Create code examples (tested)
- [ ] Update API reference
- [ ] Improve SEO metadata

**Afternoon** (1-2 hours):
- [ ] Review docs site (check links, formatting)
- [ ] Update external linking sections
- [ ] Respond to documentation questions
- [ ] Maintain documentation quality

### Friday (Docs Review)

**Afternoon** (1 hour):
- [ ] Publish final docs for the week
- [ ] Verify site builds without errors
- [ ] Check for broken links
- [ ] Update documentation index

---

## Current Q2 Focus

### High Priority

**MongoDB v2 Migration Guide** (after Issue #002):
- [ ] Document breaking changes (v1 → v2)
- [ ] Before/after code examples
- [ ] Common pitfalls and solutions
- [ ] Migration checklist

**API Documentation** (from Issues #001-#005):
- [ ] AuthMiddleware design and usage
- [ ] JWT vs API Key authentication
- [ ] Configuration environment variables
- [ ] Logging configuration
- [ ] GoMock testing patterns

### Medium Priority

**Getting Started Guides**:
- [ ] Set up local development environment
- [ ] Run tests locally
- [ ] Build Desktop and Cloud binaries
- [ ] Deploy to Fly.io (later)

### Low Priority

**Advanced Topics**:
- [ ] System architecture deep-dive
- [ ] Performance optimization
- [ ] Security hardening
- [ ] Scaling considerations

---

## Documentation Template

**Each technical doc should follow**:

```markdown
---
title: [Feature Name]
slug: [kebab-case-name]
tags: [relevant, tags, for, SEO]
---

{{< lang-toggle >}}

[Intro paragraph describing what this is]

## Objective

[What problem does this solve?]

## How It Works

[Technical explanation with diagrams/examples]

### Example

\`\`\`go
// Working code example
\`\`\`

## Configuration

[Environment variables, settings, etc.]

## Best Practices

[Tips for using this effectively]

## External Linking

[3-5 relevant external links with context]
```

---

## Documentation Standards

**Quality Checklist**:
- [ ] No H1 duplication (title is H1, no "# Title" in body)
- [ ] No consecutive headers (paragraph between them)
- [ ] Code examples are tested and working
- [ ] External links valid and relevant (3-5 links)
- [ ] SEO tags included
- [ ] Proper formatting (markdownlint, prettier)
- [ ] No emojis in technical docs (text only)
- [ ] Grammar and spelling checked

**File Structure**:
- `docs/feature-name.pt.md` — Portuguese (canonical)
- `docs/feature-name.en.md` — English translation (later)
- File names: kebab-case, descriptive, English

---

## Site Building

**Hugo/Hextra Setup**:
```bash
cd docs
hugo server  # Live preview at http://localhost:1313
hugo build   # Generate static site

# Check for errors:
hugo check   # Verify all links, markup
```

**Deployment** (later, Issue #018-#020):
- Hosted on [docs.vectora.dev](https://docs.vectora.dev)
- Auto-deploy on main branch merge
- CI/CD verifies Hugo build succeeds

---

## SEO Best Practices

**For each doc**:
- [ ] Title is descriptive (40-60 chars)
- [ ] Slug matches file name
- [ ] Tags relevant to content (3-5 tags)
- [ ] H1 title + intro paragraph
- [ ] Internal links to related docs
- [ ] External links to authoritative sources
- [ ] Proper heading hierarchy (H1 → H2 → H3, no jumps)

**Example tags**:
```yaml
tags:
  - api
  - authentication
  - jwt
  - security
  - vectora
```

---

## Content Calendar (Q2 2026)

**Week 1** (Apr 28 - May 3):
- [ ] MongoDB v2 migration guide (support Issue #002)
- [ ] AuthMiddleware documentation (support Issue #001)
- [ ] Configuration reference (support Issue #003)

**Week 2-3** (May 6-17):
- [ ] Logging configuration guide (support Issue #004)
- [ ] GoMock testing patterns (support Issue #005)
- [ ] Getting started guide (developer onboarding)

**Week 4+** (May 20+):
- [ ] API reference (complete)
- [ ] Deployment guide (Fly.io)
- [ ] System architecture
- [ ] Performance tuning

---

## External Link Requirements

**Every doc needs 3-5 relevant external links**:

Examples:
- Official library docs (golang-jwt/jwt)
- RFC standards (JWT RFC 7519)
- Best practices (OWASP, Peter Bourgon)
- Tool documentation (MongoDB, Fly.io)
- Related articles/tutorials

**Acceptable link types**:
- ✅ Official documentation
- ✅ RFC standards
- ✅ Reputable blogs (Medium, Dev.to)
- ✅ Official tool sites
- ❌ Spam/SEO farms
- ❌ Broken links
- ❌ 404 placeholder URLs

---

## Writing Guidelines

**Style**:
- Clear, concise, technical
- Active voice preferred
- Code examples for complex concepts
- Beginner-friendly when possible

**Tone**:
- Professional but approachable
- Assume reader is smart developer
- Explain "why" not just "how"
- Provide context and motivation

---

## Metrics to Track

| Metric | Target | Current |
|--------|--------|---------|
| Docs published | 20+ by June 30 | TBD |
| External links | 3-5 per doc | TBD |
| Site load time | < 1s | TBD |
| Broken links | 0 | TBD |
| Doc coverage | 90% of APIs | TBD |
| SEO ranking | Top 3 for "Vectora" | TBD |

---

## Resources

- **Hugo Docs**: https://gohugo.io/documentation/
- **Hextra Theme**: https://imfing.github.io/hextra/
- **Markdown Lint**: https://github.com/igorshubovych/markdownlint-cli
- **Technical Writing**: https://developers.google.com/tech-writing

---

**Start Date**: 2026-04-28 (start with planning)
**Focus**: Support 5 critical issues with documentation
**Status**: READY TO START
