# VECTORA Phase 1 — Implementation Plan (MVP)

## 10-Week Timeline, Task Breakdown, Dependencies, Success Criteria

---

## Executive Summary

**Objetivo:** Implementar MVP funcional em 10 semanas (Phase 1)

**Entregáveis principais:**

1. Backend FastAPI (Python) rodando em qualquer máquina (1 vCPU, 2GB RAM mínimo)
2. CLI Python (Click/Typer) — comando padrão `vectora` inicia daemon (sem TUI, sem chat)
3. Vectora Cognitive Runtime (VCR) — XLM-RoBERTa-small + LoRA, pre-thinking layer
4. MCP Server — Claude Code chama Vectora via MCP (stdio JSON-RPC)
5. Agent Completo via LangChain — tools, memory, thinking integrado
6. Integração com databases embedded (PostgreSQL via pg8000-embedded, Redis, LanceDB)
7. Docker Compose para local dev + deployment
8. Documentação básica (setup guide, API ref, integration examples)

**Stack Principal:**

```text
Backend:   Python 3.11+ | FastAPI | SQLAlchemy | pg8000-embedded
Frontend:  React 18 | Vite | TypeScript | TailwindCSS
CLI:       Python | Click/Typer (comando: vectora)
VCR:       PyTorch | XLM-RoBERTa-small + LoRA | pre-thinking layer
LLM:       LangChain + Anthropic/OpenAI/Google APIs
Tools:     File system, terminal, Redis, PostgreSQL, LanceDB, MCPs
DevOps:    Docker Compose | GitHub Actions | pre-commit
Database:  PostgreSQL embedded (pg8000-embedded) + LanceDB + Redis embedded
Embeddings: VoyageAI
```

---

## Phase 1: 8-Week Timeline (Optimized MVP — Subagent Only)

**Scope & Removals:**

- ✂️ No Frontend (React/Vite) — Phase 1 é subagent only, chamado via Claude Code
- ✂️ No TUI/Chat — Vectora não tem interface própria (Phase 6+)
- ✂️ No Dashboard — Configuração via .env e CLI
- ✂️ Task compression: 1.5-2 day tasks → 1 day (focus on essentials)
- ✂️ Parallel testing: Unit tests embedded in final week (not separate)
- ✂️ Total person-weeks: ~10 pw (1 full-stack Python dev + 1 ML engineer, ~8 weeks)

### Week 1-2: Foundation & Architecture (Weeks 1-2)

**Frente 1.1: Backend Setup (Python FastAPI Tier-Based)**

| Task                                                                              | Owner   | Duration | Dependencies | Success Criteria                        |
| --------------------------------------------------------------------------------- | ------- | -------- | ------------ | --------------------------------------- |
| **1.1.1** Init `vectora/backend` pyproject.toml, setup FastAPI + logging + config | Backend | 0.5d     | -            | Backend starts, uvicorn runs, logs JSON |
| **1.1.2** Platform tier (bcrypt, JWT, crypto utils)                               | Backend | 0.75d    | 1.1.1        | Auth functions callable, tests pass     |
| **1.1.3** Storage tier (pg8000-embedded + SQLAlchemy models)                      | Backend | 1.5d     | 1.1.2        | DB embedded, User/Dataset models work   |
| **1.1.4** LLM tier skeleton (LangChain + VoyageAI stubs)                          | Backend | 0.75d    | 1.1.3        | LangChain imports, stubs callable       |

**Output:** Backend skeleton com tiers essenciais (config → platform → storage → llm → core → api)
**Person-weeks:** 0.70

---

**Frente 1.3: CLI Skeleton (Python Click/Typer)**

| Task                                                                           | Owner | Duration | Dependencies | Success Criteria                          |
| ------------------------------------------------------------------------------ | ----- | -------- | ------------ | ----------------------------------------- |
| **1.3.1** Init CLI package, `vectora` command (no args = start daemon)         | CLI   | 0.75d    | -            | `vectora` starts daemon, CLI parser works |
| **1.3.2** Add `vectora init`, `vectora config`, `vectora logs`, `vectora stop` | CLI   | 0.75d    | 1.3.1        | All subcommands callable, config via .env |

**Output:** Minimal CLI (init + config + logs + daemon mgmt), NO chat/TUI
**Person-weeks:** 0.38

---

### Week 3-4: Auth & API (Weeks 3-4)

**Frente 2.1: Auth & API Endpoints (FastAPI)**

| Task                                                                 | Owner    | Duration | Dependencies | Success Criteria                   |
| -------------------------------------------------------------------- | -------- | -------- | ------------ | ---------------------------------- |
| **2.1.1** JWT endpoints (POST /api/v1/auth/login, /refresh, /logout) | Backend  | 1d       | 1.1.3        | Can login, JWT issued + refresh    |
| **2.1.2** Auth middleware (Depends injection) + protected endpoints  | Backend  | 0.75d    | 2.1.1        | 401 without token, scope enforced  |
| **2.1.3** Alembic migrations (users, datasets, chats, memories)      | Backend  | 1d       | 1.1.3        | Tables created, user_id isolation  |
| **2.1.4** Settings + dataset endpoints (GET/POST/DELETE)             | Backend  | 1d       | 2.1.3        | CRUD works, filtering by user_id   |
| **2.1.5** Exception handlers + structured error responses            | Backend  | 0.5d     | 2.1.4        | {status, detail, timestamp, trace} |
| **2.1.6** Frontend login integration + JWT storage                   | Frontend | 0.5d     | 1.2.2        | Login→JWT stored→redirect          |

**Output:** Complete auth flow, FastAPI core API, database schemas
**Person-weeks:** 0.625

---

**Frente 2.2: Storage Layers (Vector + Cache)**

| Task                                        | Owner   | Duration | Dependencies | Success Criteria                  |
| ------------------------------------------- | ------- | -------- | ------------ | --------------------------------- |
| **2.2.1** LanceDB init + vector schema      | Backend | 0.5d     | 1.1.3        | LanceDB starts, can create tables |
| **2.2.2** Redis connection + cache TTL 5min | Backend | 0.5d     | 2.2.1        | Redis SET/GET works               |

**Output:** Vector store + cache layer ready
**Person-weeks:** 0.25

---

### Week 5-6: RAG & LLM (Weeks 5-6)

**Frente 3.1: Agent + LLM Integration (LangChain)**

| Task                                                                 | Owner   | Duration | Dependencies | Success Criteria                                |
| -------------------------------------------------------------------- | ------- | -------- | ------------ | ----------------------------------------------- |
| **3.1.1** VoyageAI embeddings integration + LanceDB vector store     | Backend | 1d       | 2.2.1        | Can embed, store, and search vectors            |
| **3.1.2** LangChain agent setup (tools, memory, LLM routing)         | Backend | 1.5d     | 3.1.1        | Agent planning works, tool selection functional |
| **3.1.3** Anthropic Claude integration (via LangChain)               | Backend | 0.75d    | 3.1.2        | Can call Claude with agent tools                |
| **3.1.4** OpenAI integration (via LangChain)                         | Backend | 0.5d     | 3.1.3        | Can route to OpenAI if preferred                |
| **3.1.5** Tool endpoints (tools.search, tools.store, tools.retrieve) | Backend | 1d       | 3.1.2        | External agents can call via /api/v1/tools/\*   |
| **3.1.6** Query response caching (Redis) + prompt optimization       | Backend | 0.75d    | 2.2.2        | Cache hit rate > 60%, reuse of contexts         |

**Output:** Full LangChain Agent integration, multi-LLM routing, tool system
**Person-weeks:** 0.80

---

### Week 7-8: VCR Pre-Thinking & Dashboard (Weeks 7-8)

**Frente 4.1: Vectora Cognitive Runtime (VCR) — Pre-Thinking Layer**

XLM-RoBERTa-small (24M params, multilingual) + LoRA fine-tuning (r=8, alpha=16) para enriquecimento contextual ANTES do LangChain processar. VCR decide quando fazer deep thinking, query rewriting, tool selection.

| Task                                                                           | Owner | Duration | Dependencies | Success Criteria                               |
| ------------------------------------------------------------------------------ | ----- | -------- | ------------ | ---------------------------------------------- |
| **4.1.1** XLM-RoBERTa-small + LoRA setup (PyTorch native, não ONNX em Phase 1) | ML    | 1.25d    | -            | Model trains, inference 4-8ms, accuracy >= 85% |
| **4.1.2** Synthetic data generation (context enrichment scenarios)             | ML    | 0.75d    | -            | 5K+ synthetic examples for fine-tuning         |
| **4.1.3** Pre-thinking layer (query→VCR→enriched context→LangChain)            | ML    | 1d       | 4.1.1        | VCR enriches context, passes to LangChain      |
| **4.1.4** VCR service (FastAPI endpoint, subprocess call, response caching)    | ML    | 0.75d    | 4.1.3        | Backend calls `/vcr/enrich`, caches results    |

**Output:** Trained VCR model, pre-thinking layer integrated, inference API ready
**Person-weeks:** 0.80

---

**Frente 4.2: Frontend Dashboard**

| Task                                                      | Owner    | Duration | Dependencies | Success Criteria                        |
| --------------------------------------------------------- | -------- | -------- | ------------ | --------------------------------------- |
| **4.2.1** Dashboard + Settings + Memory Viewer (combined) | Frontend | 1d       | 1.2.2        | All pages render, settings update works |
| **4.2.2** Dataset Manager (list/install stubs)            | Frontend | 0.5d     | 4.2.1        | UI renders, API calls ready             |

**Output:** Complete dashboard UI, API integration ready
**Person-weeks:** 0.38

---

### Week 9: Integration, Testing, DevOps (Week 9)

**Frente 5.1: Docker & Testing**

| Task                                                                               | Owner  | Duration | Dependencies | Success Criteria                        |
| ---------------------------------------------------------------------------------- | ------ | -------- | ------------ | --------------------------------------- |
| **5.1.1** Dockerfile (FastAPI) + docker-compose.yml (backend, frontend, db, redis) | DevOps | 1d       | All prior    | `docker-compose up` starts all services |
| **5.1.2** GitHub Actions (lint, test, build)                                       | DevOps | 1d       | 5.1.1        | CI runs: black, isort, pytest, npm lint |
| **5.1.3** Unit tests (backend: auth, storage, llm, vcr)                            | QA     | 1d       | 2.1.5        | Coverage > 60%, key paths tested        |
| **5.1.4** E2E test (CLI init → login → query → response)                           | QA     | 0.75d    | 5.1.1        | Full user flow works end-to-end         |
| **5.1.5** Pre-commit hooks + .env.example setup                                    | DevOps | 0.5d     | 5.1.1        | black, isort, mypy checks active        |

**Output:** Docker Compose working, CI/CD active, test coverage baseline
**Person-weeks:** 0.75

---

**Frente 5.2: Documentation**

| Task                                                           | Owner | Duration | Dependencies | Success Criteria             |
| -------------------------------------------------------------- | ----- | -------- | ------------ | ---------------------------- |
| **5.2.1** Setup guide (local, Docker) + API reference skeleton | Docs  | 1d       | 5.1.1        | Users can follow setup steps |
| **5.2.2** Architecture overview + README updates               | Docs  | 0.5d     | -            | Tier-based design documented |

**Output:** Minimal docs (setup + architecture only)
**Person-weeks:** 0.38

---

## Critical Path & Dependencies

```
Week 1-2: Foundation (Parallel)
  ├─ 1.1 Backend Setup (0.70pw) ─→ 2.1 Auth (0.625pw)
  ├─ 1.2 Frontend Setup (0.38pw) ─→ 2.1 Login (0.625pw)
  └─ 1.3 CLI Skeleton (0.38pw)

Week 3-4: Auth & API (Sequential)
  └─ 2.1 Auth + API (0.625pw) ─→ 2.2 Storage (0.25pw) ─→ 3.1 LangChain (0.80pw)

Week 5-6: LangChain Agent + Tools
  └─ 3.1 Agent (0.80pw) ─→ 4.2 Dashboard (0.38pw)

Week 7-8: VCR Pre-Thinking & Integration
  ├─ 4.1 VCR (0.80pw) ─────────┐
  └─ 4.2 Dashboard (0.38pw) ───┴→ 5.1 Docker (0.75pw)

Week 9: Final Testing & Docs
  └─ 5.1 Docker (0.75pw) ─→ 5.2 Docs (0.38pw)
```

**Critical Path:** 1.1 → 2.1 → 3.1 → 4.2 → 5.1 → 5.2
**Total Person-Weeks:** 10.0 pw (1 senior full-stack + 1 ML = 8 weeks with 25% buffer)

---

## Team Breakdown

**Minimal Team (Phase 1):**

- 1x Backend Engineer (Python/FastAPI) — 1.1, 2.1, 2.2, 3.1, 5.1.1-2, 5.1.5
- 1x Frontend Engineer (React) — 1.2, 2.1.6, 4.2, 5.2
- 1x ML Engineer (Python/PyTorch) — 1.3 (CLI), 4.1 (VCR), integration
- 1x DevOps / QA — 5.1.1-5.1.4, Docker setup, CI/CD

**Or:** 2 Senior Full-Stack (Python/React) + 1 ML Engineer (VCR specialist)

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

### End of Week 8 (VCR Pre-Thinking + Dashboard ✓)

- [ ] VCR (XLM-RoBERTa-small + LoRA) trains successfully
- [ ] Pre-thinking accuracy >= 85% on test set
- [ ] Pre-thinking latency 4-8ms (inference)
- [ ] VCR enriches context before LangChain processing
- [ ] Dashboard renders all pages
- [ ] Real-time updates work via WebSocket
- [ ] Chat history + memory persists

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

- MVP roda em KVM1 sem swap
- Test coverage backend > 60%
- E2E tests pass consistently
- Docs cobrindo setup, API, architecture
- Zero critical security issues

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
- VAL Registry beta

### Phase 4 (Weeks 27-40): Performance & Polish

- Caching optimization
- Monitoring (Prometheus + Sentry)
- System Tray (Windows)
- Package manager distribution (brew, apt, winget)

### Phase 5 (Ongoing): Ecosystem

- VAL Registry live (community datasets)
- Advanced memory (knowledge graphs)
- Enterprise features (SSO, RBAC)

---

## Critical Files to Create (Phase 1)

### Backend (`vectora/backend/`)

```
backend/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── platform/
│   │   ├── logger.py
│   │   ├── auth.py
│   │   ├── crypto.py
│   │   └── exceptions.py
│   ├── storage/
│   │   ├── db.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── dataset.py
│   │   │   └── chat.py
│   │   ├── vector/
│   │   │   └── lancedb_client.py
│   │   └── migrations/
│   ├── llm/
│   │   ├── langchain_agent.py
│   │   ├── voyage_embeddings.py
│   │   └── tool_registry.py
│   ├── core/
│   │   ├── agent_executor.py
│   │   └── memory_manager.py
│   ├── api/
│   │   ├── router.py
│   │   ├── middleware.py
│   │   ├── deps.py
│   │   └── endpoints/
│   │       ├── auth.py
│   │       ├── chat.py
│   │       └── tools.py
│   ├── vcr/
│   │   ├── service.py
│   │   └── inference.py
│   └── mcp/
│       └── server.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── alembic/
```

### Frontend (`vectora/frontend/`)

```
frontend/
├── src/
│   ├── components/
│   │   ├── Login.tsx
│   │   ├── Dashboard.tsx
│   │   ├── Chat.tsx
│   │   ├── Settings.tsx
│   │   ├── Memory.tsx
│   │   └── Datasets.tsx
│   ├── pages/
│   ├── store/
│   │   └── store.ts (Zustand)
│   ├── api/
│   │   └── client.ts
│   ├── hooks/
│   ├── types/
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.js
├── package.json
└── Dockerfile
```

### CLI (`vectora/cli/`)

```
cli/
├── main.py
├── commands/
│   ├── init.py
│   ├── auth.py
│   ├── start.py
│   └── dataset.py
├── utils/
│   └── config.py
├── pyproject.toml
└── requirements.txt
```

### VCR (`vectora-cognitive-runtime/`)

```
vcr/
├── src/
│   ├── train.py
│   ├── inference.py
│   ├── data_loader.py
│   └── models.py
├── data/
│   └── synthetic_examples.json
├── models/
│   └── xlm_roberta_lora.pth
├── pyproject.toml
├── requirements.txt
└── README.md
```

### DevOps (`vectora/.github/`)

```
vectora/
├── .github/
│   └── workflows/
│       ├── backend-ci.yml
│       ├── frontend-ci.yml
│       └── docker-publish.yml
├── .pre-commit-config.yaml
├── docker-compose.yml
└── Dockerfile
```

---

## Entry Points for Implementation

**Week 1, Day 1 Morning:**

```bash
# Backend
cd vectora/backend
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy pg8000 pydantic python-dotenv
# Create pyproject.toml, app/main.py skeleton

# Frontend
cd ../frontend
npm create vite@latest . -- --template react-ts
npm install tailwindcss zustand axios

# CLI
cd ../cli
pip install click typer
# Create main.py skeleton

# VCR
cd ../vcr
pip install torch transformers peft
# Create train.py skeleton

# Commit: "chore: init project structure with Python FastAPI stack"
```

**Week 1, Day 1 Afternoon:**

- Backend: FastAPI app boots, uvicorn serves on :8000
- Frontend: Vite dev server on :5173, TailwindCSS works
- CLI: `vectora --help` shows subcommands
- VCR: PyTorch imports, model stubs load

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
- [ ] Vectora Cognitive Runtime (XLM-RoBERTa-small + LoRA) accuracy >= 85%
- [ ] VCR subprocess interface working (backend → Python → decision)
- [ ] Test coverage backend > 60%, frontend > 50%
- [ ] Setup guide works for fresh user
- [ ] API docs auto-generated
- [ ] E2E test (login → query → result) passes
- [ ] All commits follow conventional commits
- [ ] README.md + CONTRIBUTING.md + ARCHITECTURE.md
- [ ] Pre-commit hooks active
- [ ] GitHub Actions CI passing
- [ ] No critical security issues (basic audit)

---

**Status:** Ready for implementation
**Start Date:** 2026-05-01
**End Date:** 2026-06-25 (8 weeks + buffer)
**Team:** 1 Full-Stack (Python/React) + 1 ML Engineer (VCR) + 1 DevOps/QA
**Repository Structure:**

- `vectora/` (backend FastAPI + frontend React + CLI + VCR)
- `vectora-asset-library/` (registry de assets e datasets)
- `vectora-integrations/` (SDKs - Phase 3+)
- `vectora-website/` (Hugo/Hextra docs)
