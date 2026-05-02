# VECTORA Phase 1 — Implementation Plan (MVP)

## 10-Week Timeline, Task Breakdown, Dependencies, Success Criteria

---

## Executive Summary

**Objetivo:** Implementar MVP funcional em 10 semanas (Phase 1)

**Entregáveis principais:**

1. ✅ Backend Go rodando em KVM1 (2 vCPU, 4GB RAM)
2. ✅ Frontend React com login + dashboard
3. ✅ CLI funcional (init, start, auth, dataset)
4. ✅ Vectora Cognitive Runtime decision engine (35MB ONNX, 4-8ms latência)
5. ✅ Docker Compose para local dev + VPS deployment
6. ✅ API REST funcional (Agent Mode + Tool Mode)
7. ✅ Documentação básica (setup guide, API ref)

**Stack Principal:**

```text
Backend:   Go 1.21+ | Echo/Chi | GORM | embedded-postgres
Frontend:  React 18 | Vite | TypeScript | TailwindCSS
CLI:       Go + Cobra + Viper
Vectora Cognitive Runtime:       Python 3.10 | PyTorch | ONNX INT4 (35MB)
DevOps:    Docker Compose | GitHub Actions | pre-commit
Database:  embedded-postgres (local file) + LanceDB + Redis
```

---

## Phase 1: 8-Week Timeline (Optimized MVP)

**Reductions from 10-week plan:**

- ✂️ Task compression: 1.5-2 day tasks → 1 day (focus on essentials)
- ✂️ Parallel testing: Unit tests embedded in final week (not separate)
- ✂️ Doc scope: Minimal (setup guide + API ref only, not architecture)
- ✂️ Vectora Cognitive Runtime scope: Core model training only, no advanced evaluation
- ✂️ Total person-weeks: 12.5 → 9.5 pw (1 dev = 8 weeks with 18% buffer)

### Week 1-2: Foundation & Architecture (Weeks 1-2)

**Frente 1.1: Backend Setup (Go Tier-Based)**

| Task                                                                   | Owner   | Duration | Dependencies | Success Criteria                          |
| ---------------------------------------------------------------------- | ------- | -------- | ------------ | ----------------------------------------- |
| **1.1.1** Init `vectora/backend` go.mod, setup Echo + config + logging | Backend | 0.5d     | -            | ✅ Backend starts, slog JSON output works |
| **1.1.2** Platform tier (bcrypt, crypto, JWT skeleton)                 | Backend | 1d       | 1.1.1        | ✅ Auth functions callable                |
| **1.1.3** Storage tier (embedded-postgres + GORM models)               | Backend | 1.5d     | 1.1.2        | ✅ DB starts, User/Dataset models compile |

**Output:** Backend skeleton com 4 tiers essenciais (config → platform → storage → [llm/core/api])
**Person-weeks:** 0.67

---

**Frente 1.2: Frontend Setup (React + Vite)**

| Task                                             | Owner    | Duration | Dependencies | Success Criteria                                 |
| ------------------------------------------------ | -------- | -------- | ------------ | ------------------------------------------------ |
| **1.2.1** Init Vite + React + Zustand + Tailwind | Frontend | 0.5d     | -            | ✅ Dev server starts, styling works              |
| **1.2.2** Login page + API client (SWR)          | Frontend | 1d       | 1.2.1        | ✅ Login form renders + can POST /api/auth/login |

**Output:** Frontend with login page, ready for API integration
**Person-weeks:** 0.38

---

**Frente 1.3: CLI Skeleton (Go + Cobra)**

| Task                                                          | Owner | Duration | Dependencies | Success Criteria                  |
| ------------------------------------------------------------- | ----- | -------- | ------------ | --------------------------------- |
| **1.3.1** Init CLI + `vectora init`, `vectora start` commands | CLI   | 1d       | -            | ✅ CLI can init and start backend |

**Output:** Minimal CLI (init + start), config via .env
**Person-weeks:** 0.25

---

### Week 3-4: Auth & API (Weeks 3-4)

**Frente 2.1: Auth & API Endpoints**

| Task                                                          | Owner    | Duration | Dependencies | Success Criteria                     |
| ------------------------------------------------------------- | -------- | -------- | ------------ | ------------------------------------ |
| **2.1.1** JWT + login endpoint (POST /api/v1/auth/login)      | Backend  | 1d       | 1.1.3        | ✅ Can login, JWT issued             |
| **2.1.2** Auth middleware + protected endpoints               | Backend  | 0.5d     | 2.1.1        | ✅ 401 without token                 |
| **2.1.3** Database migrations (users, datasets, chat_history) | Backend  | 1d       | 1.1.3        | ✅ Tables created, user_id isolation |
| **2.1.4** Settings + dataset endpoints (GET/POST)             | Backend  | 1d       | 2.1.3        | ✅ Settings update, list datasets    |
| **2.1.5** Error handling + standardized responses             | Backend  | 0.5d     | 2.1.4        | ✅ All errors {code, message}        |
| **2.1.6** Frontend login integration                          | Frontend | 0.5d     | 1.2.2        | ✅ Login→JWT stored→redirect         |

**Output:** Complete auth flow, core API, database
**Person-weeks:** 0.58

---

**Frente 2.2: Storage Layers (Vector + Cache)**

| Task                                        | Owner   | Duration | Dependencies | Success Criteria                     |
| ------------------------------------------- | ------- | -------- | ------------ | ------------------------------------ |
| **2.2.1** LanceDB init + vector schema      | Backend | 0.5d     | 1.1.3        | ✅ LanceDB starts, can create tables |
| **2.2.2** Redis connection + cache TTL 5min | Backend | 0.5d     | 2.2.1        | ✅ Redis SET/GET works               |

**Output:** Vector store + cache layer ready
**Person-weeks:** 0.25

---

### Week 5-6: RAG & LLM (Weeks 5-6)

**Frente 3.1: RAG + LLM Integration**

| Task                                                          | Owner   | Duration | Dependencies | Success Criteria                            |
| ------------------------------------------------------------- | ------- | -------- | ------------ | ------------------------------------------- |
| **3.1.1** Vector search + reranking (LanceDB + Voyage stub)   | Backend | 1.5d     | 2.2.1        | ✅ Search returns top-K, reranking callable |
| **3.1.2** RAG orchestrator (search→rerank→LLM)                | Backend | 1d       | 3.1.1        | ✅ Full pipeline works end-to-end           |
| **3.1.3** Claude API integration                              | Backend | 0.5d     | 3.1.2        | ✅ Can call Claude with context             |
| **3.1.4** OpenAI API integration                              | Backend | 0.5d     | 3.1.3        | ✅ Can call OpenAI API                      |
| **3.1.5** Tool Mode endpoints (knowledge.store, memory.query) | Backend | 0.5d     | 3.1.2        | ✅ Can store/query knowledge                |
| **3.1.6** LLM response caching (Redis)                        | Backend | 0.5d     | 2.2.2        | ✅ Same query returns cached response       |

**Output:** Complete RAG pipeline, Agent Mode + Tool Mode, multi-LLM
**Person-weeks:** 0.65

---

### Week 7-8: Vectora Cognitive Runtime & Dashboard (Weeks 7-8)

**Frente 4.1: Vectora Cognitive Runtime Decision Engine (Python)**

| Task                                                                                          | Owner                     | Duration | Dependencies | Success Criteria                                             |
| --------------------------------------------------------------------------------------------- | ------------------------- | -------- | ------------ | ------------------------------------------------------------ |
| **4.1.1** SmolLM2-135M setup + fine-tuning (PyTorch)                                          | Vectora Cognitive Runtime | 2d       | -            | ✅ Model trains, inference works                             |
| **4.1.2** ONNX export (INT4, < 35MB)                                                          | Vectora Cognitive Runtime | 1d       | 4.1.1        | ✅ ONNX model exports, size verified                         |
| **4.1.3** ONNX Runtime wrapper (Python)                                                       | Vectora Cognitive Runtime | 0.5d     | 4.1.2        | ✅ 4-8ms inference latency confirmed                         |
| **4.1.4** Vectora Cognitive Runtime service endpoint (REST /vectora-cognitive-runtime/decide) | Vectora Cognitive Runtime | 0.5d     | 4.1.3        | ✅ Backend can call Vectora Cognitive Runtime, get decisions |

**Output:** Trained Vectora Cognitive Runtime (35MB), integrated with backend
**Person-weeks:** 0.67

---

**Frente 4.2: Frontend Dashboard**

| Task                                                      | Owner    | Duration | Dependencies | Success Criteria                           |
| --------------------------------------------------------- | -------- | -------- | ------------ | ------------------------------------------ |
| **4.2.1** Dashboard + Settings + Memory Viewer (combined) | Frontend | 1d       | 1.2.2        | ✅ All pages render, settings update works |
| **4.2.2** Dataset Manager (list/install stubs)            | Frontend | 0.5d     | 4.2.1        | ✅ UI renders, API calls ready             |

**Output:** Complete dashboard UI, API integration ready
**Person-weeks:** 0.38

---

### Week 9: Integration, Testing, DevOps (Week 9)

**Frente 5.1: Docker & Basic Testing**

| Task                                                                           | Owner  | Duration | Dependencies | Success Criteria                            |
| ------------------------------------------------------------------------------ | ------ | -------- | ------------ | ------------------------------------------- |
| **5.1.1** Dockerfile + docker-compose.yml (backend, frontend, postgres, redis) | DevOps | 1.5d     | All prior    | ✅ `docker-compose up` starts all services  |
| **5.1.2** GitHub Actions (lint, test, build)                                   | DevOps | 1d       | 5.1.1        | ✅ CI runs on push, builds pass             |
| **5.1.3** Unit tests (backend core only)                                       | QA     | 0.5d     | 2.1.5        | ✅ Auth + storage tests pass                |
| **5.1.4** E2E test (login → query)                                             | QA     | 0.5d     | 5.1.1        | ✅ Basic flow works                         |
| **5.1.5** Pre-commit hooks + .env.example                                      | DevOps | 0.5d     | 5.1.1        | ✅ Hooks active, users have config template |

**Output:** Docker Compose working, CI/CD active, basic tests
**Person-weeks:** 0.65

---

**Frente 5.2: Documentation**

| Task                                                           | Owner | Duration | Dependencies | Success Criteria                |
| -------------------------------------------------------------- | ----- | -------- | ------------ | ------------------------------- |
| **5.2.1** Setup guide (local, Docker) + API reference skeleton | Docs  | 1d       | 5.1.1        | ✅ Users can follow setup steps |
| **5.2.2** Architecture overview + README updates               | Docs  | 0.5d     | -            | ✅ Tier-based design documented |

**Output:** Minimal docs (setup + architecture only)
**Person-weeks:** 0.38

---

## Critical Path & Dependencies

```
Week 1-2: Foundation (Parallel)
  ├─ 1.1 Backend Setup (0.67pw) ─→ 2.1 Auth (0.58pw)
  ├─ 1.2 Frontend Setup (0.38pw) ─→ 2.1 Login (0.58pw)
  └─ 1.3 CLI Skeleton (0.25pw)

Week 3-4: Auth & API (Sequential)
  └─ 2.1 Auth + API (0.58pw) ─→ 2.2 Storage (0.25pw) ─→ 3.1 RAG (0.65pw)

Week 5-6: RAG & LLM
  └─ 3.1 RAG (0.65pw) ─→ 4.2 Dashboard (0.38pw)

Week 7-8: Vectora Cognitive Runtime & Integration
  ├─ 4.1 Vectora Cognitive Runtime (0.67pw) ─────────┐
  └─ 4.2 Dashboard (0.38pw) ───┴→ 5.1 Docker (0.65pw)

Week 9: Final Testing & Docs
  └─ 5.1 Docker (0.65pw) ─→ 5.2 Docs (0.38pw)
```

**Critical Path:** 1.1 → 2.1 → 3.1 → 4.2 → 5.1 → 5.2
**Total Person-Weeks:** 9.5 pw (1 senior dev = 8 weeks with 18% buffer)

---

## Team Breakdown

**Minimal Team (Phase 1):**

- 1x Backend Engineer (Go) — 1.1, 2.1, 2.2, 2.3, 3.1, 3.2, 5.1.5
- 1x Frontend Engineer (React) — 1.2, 2.1.6, 4.2, 5.2.2
- 1x ML Engineer (Python) — 4.1, evaluation
- 1x DevOps / QA — 5.1.1-5.1.4, 5.2, 5.3, pre-commit

**Or:** 1-2 Senior Full-Stack + 1 ML Engineer

---

## Success Criteria by Milestone

### End of Week 2 (Foundation ✓)

- [ ] Backend starts with `go run ./cmd/vectora`
- [ ] Frontend loads on `http://localhost:5173`
- [ ] CLI `vectora init` and `vectora start` work
- [ ] No major build errors

### End of Week 4 (Auth ✓)

- [ ] User can register + login
- [ ] JWT token issued and validated
- [ ] Protected endpoints return 401 without token
- [ ] Settings page (password update) works

### End of Week 6 (RAG ✓)

- [ ] Vector search returns results in < 200ms
- [ ] Reranking scores documents correctly
- [ ] LLM integration works (at least Claude)
- [ ] Tool Mode endpoints functional

### End of Week 8 (Vectora Cognitive Runtime + Dashboard ✓)

- [ ] Vectora Cognitive Runtime model exports to 35MB ONNX
- [ ] Dashboard renders all pages
- [ ] Real-time updates work via WebSocket
- [ ] Chat history persists

### End of Week 10 (Final MVP ✓)

- [ ] `docker-compose up` starts everything
- [ ] E2E test (login → query → result) passes
- [ ] API docs auto-generated
- [ ] Setup guide works for new users
- [ ] Test coverage backend > 60%, frontend > 50%

---

## Metrics & Monitoring

**Latency Targets:**

- API response: < 500ms p95
- Vectora Cognitive Runtime decision: 4-8ms
- Vector search: 100-200ms
- Full RAG pipeline: < 1s

**Memory Footprint (KVM1 - 4GB):**

- PostgreSQL embedded: 200-300MB
- Redis: 100MB
- Backend Go: 200-300MB
- LanceDB: ~500MB (grows with vectors)
- **Total peak:** ~1.3-1.4GB (leaves 2.6GB buffer)

**Success Metrics:**

- ✅ MVP roda em KVM1 sem swap
- ✅ Test coverage backend > 60%
- ✅ E2E tests pass consistently
- ✅ Docs cobrindo setup, API, architecture
- ✅ Zero critical security issues

---

## Risk Mitigation

| Risk                                              | Probability | Mitigation                                    |
| ------------------------------------------------- | ----------- | --------------------------------------------- |
| Vectora Cognitive Runtime training takes too long | Medium      | Pre-train SmolLM2, use LoRA (smaller dataset) |
| Memory overrun in KVM1                            | Low         | Embedded-postgres instead of separate DB      |
| Docker Compose complexity                         | Low         | Provide working docker-compose.yml from day 1 |
| API design mismatch                               | Medium      | Sketch API endpoints in Week 2                |
| LLM API rate limits                               | Low         | Local caching (Redis)                         |

---

## Post-MVP (Phase 2-5 Overview)

### Phase 2 (Weeks 11-14): Stabilization

- Bug fixes + performance optimization
- Security audit (OWASP Top 10)
- User feedback incorporation
- Expanded test coverage (> 80%)

### Phase 3 (Weeks 15-26): Features & Integrations

- Agent integrations (Claude Code MCP, Gemini CLI, etc)
- Advanced Tool Mode
- Web search + fetch
- PAL Registry beta

### Phase 4 (Weeks 27-40): Performance & Polish

- Caching optimization
- Monitoring (Prometheus + Sentry)
- System Tray (Windows)
- Package manager distribution (brew, apt, winget)

### Phase 5 (Ongoing): Ecosystem

- PAL Registry live (community datasets)
- Advanced memory (knowledge graphs)
- Enterprise features (SSO, RBAC)

---

## Critical Files to Create (Phase 1)

### Backend (vectora/)

```
backend/
├── cmd/
│   ├── vectora/
│   │   ├── main.go
│   │   └── config.go
│   └── server/
│       └── main.go
├── internal/
│   ├── config/
│   │   ├── config.go
│   │   └── validation.go
│   ├── platform/
│   │   ├── logger/
│   │   ├── auth/
│   │   └── crypto/
│   ├── storage/
│   │   ├── db.go
│   │   ├── vector/
│   │   └── models/
│   ├── llm/
│   ├── core/
│   │   └── rag/
│   ├── api/
│   │   ├── router.go
│   │   ├── middleware/
│   │   └── handlers/
│   ├── mcp/
│   └── shared/
├── migrations/
├── go.mod
├── go.sum
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

### Frontend (vectora/)

```
frontend/
├── src/
│   ├── components/
│   │   ├── Login.tsx
│   │   ├── Dashboard.tsx
│   │   ├── Settings.tsx
│   │   ├── Memory.tsx
│   │   └── Datasets.tsx
│   ├── pages/
│   ├── store/
│   │   └── store.ts (Zustand)
│   ├── api/
│   │   └── client.ts
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.js
├── package.json
└── Dockerfile
```

### CLI (vectora/)

```
cmd/vectora/
├── main.go
├── config.go
└── commands/
    ├── init.go
    ├── start.go
    ├── auth.go
    └── dataset.go
```

### Vectora Cognitive Runtime (vectora-cognitive-runtime/ OR vectora/vectora-cognitive-runtime/)

```
vectora-cognitive-runtime/
├── src/
│   ├── train.py
│   ├── inference.py
│   ├── export_onnx.py
│   └── models/
├── data/
├── models/
│   ├── smollm2_135m.onnx (final, 35MB)
│   └── training_artifacts/
├── pyproject.toml
├── requirements.txt
└── README.md
```

### DevOps

```
vectora/
├── .github/
│   └── workflows/
│       ├── backend-ci.yml
│       ├── frontend-ci.yml
│       └── docker-publish.yml
├── .pre-commit-config.yaml
└── infra/
    ├── docker-compose.yml
    ├── Dockerfile
    └── scripts/
```

---

## Entry Points for Implementation

**Week 1, Day 1 Morning:**

```bash
# Backend
cd vectora
mkdir -p backend/{cmd/vectora,cmd/server,internal/{config,platform,storage,llm,core,api,mcp,shared}}
go mod init github.com/vectora/vectora
# Create main.go skeleton

# Frontend
cd frontend
npm create vite@latest . -- --template react-ts
npm install tailwindcss zustand swr

# CLI
cd ../cmd/vectora
touch main.go config.go
# Add Cobra skeleton

# Commit: "chore: init project structure"
```

**Week 1, Day 1 Afternoon:**

- Backend: Config tier (fail-fast validation)
- Frontend: Vite + TailwindCSS working
- CLI: Cobra command structure

---

## Communication Plan

**Async Updates (Daily):**

- Slack #vectora-dev: Daily standup (1 message per person, 2-3 blockers max)
- GitHub Issues: Track blockers, link to PRs

**Sync Meetings (Weekly):**

- Monday 10am: Sprint planning (30 min)
- Friday 4pm: Sprint review + demo (45 min)

**Document Changes:**

- Decisions logged in `DECISIONS.md`
- Architecture changes require plan update
- API changes auto-sync from OpenAPI spec

---

## Verification & Testing

**Daily Build:**

```bash
# Backend
cd backend
go build -o ../bin/vectora ./cmd/vectora
go test -race -cover ./...

# Frontend
cd ../frontend
npm run build
npm run test:ci

# Integration
docker-compose up --abort-on-container-exit
# curl http://localhost:3000/api/v1/health
```

**E2E Test (Week 10):**

```bash
# 1. Login
POST /api/v1/auth/login
# 2. Query
POST /api/v1/chat/message
# 3. Verify response
GET /api/v1/memory/query
```

**Performance Test:**

```bash
# k6 or similar
- Vector search: < 200ms p95
- Full RAG: < 1s p95
- Vectora Cognitive Runtime decision: 4-8ms
```

---

## Final Checklist (Week 10)

- [ ] Backend compiles, starts without errors
- [ ] Frontend loads, login works
- [ ] CLI init/start commands functional
- [ ] Docker Compose starts all services
- [ ] Auth flow (register → login → JWT) end-to-end
- [ ] Vector search + reranking working
- [ ] LLM integration (at least Claude)
- [ ] Vectora Cognitive Runtime model < 35MB, inference 4-8ms
- [ ] Test coverage backend > 60%, frontend > 50%
- [ ] Setup guide works for fresh user
- [ ] API docs auto-generated
- [ ] Memory footprint < 1.5GB on KVM1
- [ ] E2E test (login → query → result) passes
- [ ] All commits follow conventional commits
- [ ] README.md + CONTRIBUTING.md + ARCHITECTURE.md
- [ ] Pre-commit hooks active
- [ ] GitHub Actions CI passing
- [ ] No critical security issues (basic audit)

---

**Status:** ✅ Ready for implementation
**Start Date:** 2026-05-01
**End Date:** 2026-06-25 (8 weeks)
**Team:** 1 Backend (Go) + 1 Frontend (React) + 1 ML (Python) + 1 DevOps/QA
**Repository Structure:**

- vectora/ (backend Go + frontend React + CLI)
- vectora-cognitive-runtime/ (separate repo for Vectora Cognitive Runtime Python model)
- vectora-integrations/ (Turborepo for SDKs - Phase 3+)
- vectora-asset-library/ (GitHub registry - Phase 3+)
- vectora-website/ (Hugo docs - Phase 3+)
