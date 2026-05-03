# VECTORA — Executive Overview

## O que é, Como Funciona, Por que Importa

---

## O que é VECTORA?

**VECTORA** é um **knowledge hub inteligente open-source** que gerencia processamento e análise de dados com:

- 🧠 **Vector Search** — busca semântica em documentos (LanceDB + Voyage embeddings)
- 🎯 **Reranking Local** — reordena resultados localmente (Voyage v2.5, sem API adicional)
- 🔍 **Web Search** — integra resultados da web (SerpAPI)
- 🤖 **LLM Integration** — funciona com Claude, OpenAI, Google (Agent Mode)
- 💾 **Memory System** — persiste conhecimento em vector db + PostgreSQL
- 🔌 **Multi-Agent Compatible** — integra com Claude Code, Gemini CLI, Paperclip, etc

**NÃO é:**

- ❌ SaaS proprietary
- ❌ Chat interface genérica
- ❌ Apenas wrapper de RAG
- ❌ Dependente de nuvem

**É:**

- ✅ Open-source, rode localmente em KVM1 (2 vCPU, 4GB RAM)
- ✅ Knowledge hub — inteligência reutilizável
- ✅ Orquestrador — suporta 2 modos operacionais
- ✅ Extensível — integra com qualquer agent

---

## Mapa Mental Completo

```
┌─────────────────────────────────────────────────────────────┐
│                     VECTORA                                  │
│          Knowledge Hub Inteligente                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    ┌───▼──┐       ┌──▼──┐       ┌──▼────────┐
    │AGENT │       │TOOL │       │DASHBOARD  │
    │MODE  │       │MODE │       │ & CONFIG  │
    │(LLM) │       │     │       │           │
    │      │       │     │       │(Web UI)   │
    └───┬──┘       └──┬──┘       └──┬────────┘
        │              │             │
        └──────────────┼─────────────┘
                       │
   ┌───────────────────▼────────────────────┐
   │    VECTORA Backend (Go)                 │
   │                                        │
   │  ┌─────────────────────────────────┐   │
   │  │   RAG Orchestrator              │   │
   │  │  ├─ Vector Search (LanceDB)     │   │
   │  │  ├─ Rerank (Voyage v2.5)        │   │
   │  │  ├─ Web Search (SerpAPI)        │   │
   │  │  └─ LLM Integration (multi)     │   │
   │  └─────────────────────────────────┘   │
   │                                        │
   │  ┌─────────────────────────────────┐   │
   │  │   Memory Management             │   │
   │  │  ├─ Knowledge Storage           │   │
   │  │  ├─ Context Building            │   │
   │  │  └─ Per-user Isolation          │   │
   │  └─────────────────────────────────┘   │
   │                                        │
   │  ┌─────────────────────────────────┐   │
   │  │   Protocol Handlers             │   │
   │  │  ├─ REST API (/api/v1/*)        │   │
   │  │  ├─ MCP (Model Context Proto)   │   │
   │  │  └─ WebSocket (real-time)       │   │
   │  └─────────────────────────────────┘   │
   └────────┬────────────────────┬──────────┘
            │                    │
      ┌─────▼──┐          ┌──────▼────┐
      │LanceDB │          │PostgreSQL │
      │Vectors │          │Metadata   │
      │(local) │          │+ Cache    │
      └────────┘          └───────────┘
            ▲                    ▲
            │                    │
      ┌─────┴────────────────────┴─────────┐
      │                                    │
   ┌──▼──┐  ┌───────────┐  ┌──────────┐  │
   │Redis│  │Voyage API │  │SerpAPI   │  │
   │Pub/ │  │(Embed +   │  │(Web      │  │
   │Sub  │  │Rerank)    │  │Search)   │  │
   └─────┘  └───────────┘  └──────────┘  │
            │                             │
            └─────────────────────────────┘
```

---

## 2 Modos Operacionais

### Mode 1: Agent Mode (Full RAG — Modo Orquestrador)

```
┌─────────────────────────────────┐
│  Agente Externo (Claude Code)   │
│  "Ajude com React hooks"         │
└──────────────┬──────────────────┘
               │ POST /api/v1/chat/message
               │
   ┌───────────▼──────────────┐
   │  VECTORA Backend          │
   │                          │
   │  1. Vector Search        │
   │     └─ encontra docs     │
   │                          │
   │  2. Rerank               │
   │     └─ ordena top-5      │
   │                          │
   │  3. Web Search           │
   │     └─ se necessário     │
   │                          │
   │  4. Build Context        │
   │     └─ prepara prompt    │
   │                          │
   │  5. Call LLM             │
   │     └─ Claude/OpenAI     │
   │                          │
   │  6. Return Response      │
   │     └─ + save to memory  │
   └───────────┬──────────────┘
               │
   ┌───────────▼──────────────────────┐
   │ Response: JSON com resposta       │
   │ + contexto + metadata             │
   │                                  │
   │ {                                │
   │   "response": "React hooks ...",  │
   │   "sources": [...],              │
   │   "confidence": 0.92,            │
   │   "tools_used": ["search"]       │
   │ }                                │
   └──────────────────────────────────┘
```

**Quando usar Agent Mode:**

- Agent precisa de resposta completa + contexto
- Decisão é crítica (precisa de LLM)
- Quer que Vectora decida qual LLM usar (routing)
- Resultado é único e determinístico

**Exemplo:**

```
Claude Code: "O que é o padrão Observer em TypeScript?"
→ Vectora busca docs de design patterns
→ Reranqueia, pega top-3
→ Chama Claude API com contexto
→ Responde com explicação + exemplos
→ Salva em memory para futuras queries
```

---

### Mode 2: Tool Mode (Structured Integration — Modo Ferramenta)

```
┌─────────────────────────────────┐
│  Agente Externo (Claude Code)   │
│  (análise própria)              │
└──────────────┬──────────────────┘
               │
     ┌─────────┴─────────┬───────────┬──────────┐
     │                   │           │          │
   ┌─▼──┐          ┌────▼──┐   ┌────▼───┐  ┌──▼──────┐
   │POST │          │GET    │   │POST    │  │GET      │
   │knowledge       │memory │   │tools/  │  │tools/   │
   │/store          │/query │   │rerank  │  │websearch│
   └─┬──┘          └────┬──┘   └────┬───┘  └──┬──────┘
     │                  │           │         │
   [1]              [2]           [3]       [4]
   Save            Query          Rerank    Web
   analyzed        embeddings     documents Search
   results         (sem LLM)      locally   + Fetch

     │                  │           │         │
     └──────────────────┴───────────┴─────────┘
                        │
       ┌────────────────▼────────────────┐
       │   Agent usa resultados          │
       │   em sua própria análise        │
       │                                │
       │   (Vectora = storage +           │
       │    retrieval, não decisão)      │
       └────────────────────────────────┘
```

**Quando usar Tool Mode:**

- Agent tem sua própria inteligência (faz análise)
- Agent precisa **armazenar** conhecimento (knowledge.store)
- Agent quer **buscar** contexto sem decisão (memory.query)
- Agent quer **reranquear** documentos localmente
- Agent quer **buscar na web** sem passar por LLM

**Exemplo:**

```
Claude Code (análise própria):
  1. Analisa código do usuário
  2. POST /api/v1/knowledge/store
     └─ salva "padrão Observer detectado em UserObserver.ts"
  3. Depois, GET /api/v1/memory/query?q=observer
     └─ encontra análise anterior
  4. Usa contexto na próxima análise
  5. POST /api/v1/tools/websearch?q=observer pattern
     └─ busca web, fetch conteúdo, armazena
```

---

## Dashboard — Interface de Configuração (Sempre Ativa)

Dashboard NÃO é um "modo", é a **interface de gerenciamento** que funciona **em paralelo** com ambos os modos:

```
┌──────────────────────────────────────────────────────┐
│       VECTORA DASHBOARD                               │
│    https://localhost:3000 (ou VPS)                   │
│                                                      │
│  ┌─────────────────────────────────────────────┐    │
│  │ Login (email + password)                    │    │
│  └─────────────────────────────────────────────┘    │
│                       │                             │
│  ┌────────────────────▼───────────────────────┐    │
│  │ Main Dashboard                             │    │
│  │                                            │    │
│  │  📊 Stats & Analytics:                     │    │
│  │  ├─ Queries today: 42                      │    │
│  │  ├─ Avg latency: 234ms                     │    │
│  │  ├─ Cache hit rate: 73%                    │    │
│  │  ├─ Vectors indexed: 15K                   │    │
│  │  └─ Storage used: 2.3GB / 50GB             │    │
│  │                                            │    │
│  │  🛠️ Quick Actions:                         │    │
│  │  ├─ [Index New Dataset]                    │    │
│  │  ├─ [Clear Cache]                          │    │
│  │  └─ [Export Memory]                        │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │ Settings & Configuration                   │    │
│  │                                            │    │
│  │  🔑 API Keys:                              │    │
│  │  ├─ Claude API Key: [••••••••••]           │    │
│  │  ├─ OpenAI API Key: [••••••••••]           │    │
│  │  ├─ Voyage API Key: [••••••••••]           │    │
│  │  └─ SerpAPI Key: [••••••••••]              │    │
│  │                                            │    │
│  │  🔒 Security:                              │    │
│  │  ├─ Change Password                        │    │
│  │  ├─ Session Timeout: 30 min                │    │
│  │  └─ Two-Factor Auth: OFF                   │    │
│  │                                            │    │
│  │  ⚙️ Preferences:                           │    │
│  │  ├─ Default LLM: Claude                    │    │
│  │  ├─ Cache TTL: 5 min                       │    │
│  │  └─ Log Level: info                        │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │ Memory Viewer                              │    │
│  │                                            │    │
│  │  📚 Indexed Documents:                     │    │
│  │  ├─ Godot 4.6 Docs (installed)             │    │
│  │  ├─ React Hooks Guide (installed)          │    │
│  │  ├─ Web search results (temp, auto-clean)  │    │
│  │  └─ Custom docs (uploaded)                 │    │
│  │                                            │    │
│  │  💬 Chat History:                          │    │
│  │  ├─ "What is Observer pattern?" (3h ago)   │    │
│  │  ├─ "How to use hooks?" (2h ago)           │    │
│  │  └─ "Best practices..." (1h ago)           │    │
│  │                                            │    │
│  │  📈 Execution Logs:                        │    │
│  │  ├─ [View recent queries]                  │    │
│  │  ├─ [Download logs]                        │    │
│  │  └─ [Clear old logs]                       │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │ Dataset Manager (PAL Registry)             │    │
│  │                                            │    │
│  │  📦 Installed Datasets:                    │    │
│  │  ├─ godot-4.6-docs (v4.6.1)                │    │
│  │  │  └─ [Uninstall] [Update] [Details]      │    │
│  │  ├─ react-hooks-guide (v2.1.0)             │    │
│  │  │  └─ [Uninstall] [Update] [Details]      │    │
│  │  └─ custom-company-docs (v1.0.0)           │    │
│  │     └─ [Uninstall] [Update] [Details]      │    │
│  │                                            │    │
│  │  🌐 Browse PAL Registry:                   │    │
│  │  ├─ [Search available datasets]            │    │
│  │  ├─ [Featured this month]                  │    │
│  │  └─ [Community contributions]              │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  [Logout]  [Help]  [GitHub]  [Docs]                 │
└──────────────────────────────────────────────────────┘
```

**Dashboard permite:**

- ✅ Configurar chaves de API (sem exigir código)
- ✅ Visualizar histórico de memory
- ✅ Gerenciar datasets (install, uninstall, update)
- ✅ Monitorar performance (queries/min, latência)
- ✅ Alterar senha e preferências
- ✅ Tudo via interface web (não requer CLI)

**Por que Dashboard é importante:**

- 🎯 Usuários non-technical podem usar Vectora
- 🔒 Configuração segura (sem expor chaves em código)
- 📊 Visibilidade de o que está acontecendo
- 🔧 Gerenciamento sem terminal

---

## Stack Técnico (Simplificado)

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  Frontend (User-Facing)                             │
│  ├─ React 18 + Vite (dashboard)                     │
│  ├─ TypeScript (type safety)                        │
│  └─ TailwindCSS (styling)                           │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Backend (Core Logic)                               │
│  ├─ Go 1.21+ (performance, concurrency)             │
│  ├─ Echo/Chi (HTTP router)                          │
│  ├─ GORM (database ORM)                             │
│  └─ Cobra (CLI framework)                           │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Vector & Memory                                    │
│  ├─ LanceDB (vector search, local)                  │
│  ├─ PostgreSQL embedded (metadata)                  │
│  ├─ Redis (cache + Pub/Sub)                         │
│  └─ Voyage AI SDK (embeddings + rerank)             │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ML/AI                                              │
│  ├─ Python 3.10+ (Vectora Cognitive Runtime separate repo)                │
│  ├─ PyTorch (model training)                        │
│  ├─ ONNX (model export, 35MB)                       │
│  └─ ONNX Runtime (4-8ms inference)                  │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  DevOps & Distribution                              │
│  ├─ Docker Compose (local development)              │
│  ├─ GitHub Actions (CI/CD)                          │
│  ├─ Package managers (brew, apt, winget)            │
│  └─ Pre-commit hooks (code quality)                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Por que esse stack?**

- **Go:** Rápido, concorrente, binário único (CLI perfeito)
- **React:** Interativo, modern, comunidade grande
- **LanceDB:** Vector search local, zero config
- **PostgreSQL embedded:** Robusto, sem servidor separado
- **Python (Vectora Cognitive Runtime):** ML libraries maduras, training rápido
- **ONNX:** Modelo pequeno (35MB), portável, rápido

---

## Estrutura do Monorepo

O workspace do Vectora está organizado nestas pastas:

- `vectora/`: produto principal com backend Go, frontend React e CLI
- `vectora-asset-library/`: registry público de assets e datasets
- `vectora-cognitive-runtime/`: VCR, o engine de decisão em Python
- `vectora-integrations/`: Turborepo com SDKs e adaptadores
- `vectora-website/`: site oficial e documentação Hugo/Hextra

**Por que esse formato?**

- **Separação clara:** cada domínio evolui no seu próprio diretório
- **Publicação independente:** cada área pode ter release/versionamento próprio
- **Desenvolvimento paralelo:** times trabalham sem acoplamento desnecessário
- **Documentação centralizada:** o conteúdo oficial vive em `vectora-website/content/`

---

## Fluxo de Dados (End-to-End)

```
USUARIO (Claude Code)
  │
  │ "Ajude com React hooks"
  │
  ├──────────────────┐
  │                  │
  │ Agent Mode       │ Tool Mode
  │ (full RAG)       │ (structured)
  │                  │
  └────────┬─────────┴────────────────┐
           │                         │
    POST /api/v1/          POST /api/v1/knowledge/store
    chat/message           GET /api/v1/memory/query
           │               POST /api/v1/tools/websearch
           │               POST /api/v1/tools/rerank
           │                         │
           │                         │
    ┌──────▼───────────────────────────┐
    │  VECTORA BACKEND                  │
    │                                  │
    │  RAG ORCHESTRATOR:               │
    │  1. Vector Search (LanceDB)      │
    │     └─ top-10 resultados         │
    │                                  │
    │  2. Rerank (Voyage v2.5)         │
    │     └─ top-5 reordenados         │
    │                                  │
    │  3. Optional: Web Search         │
    │     └─ se query não encontrado   │
    │                                  │
    │  4. Build Context (Agent Mode)   │
    │     └─ prepara prompt            │
    │                                  │
    │  5. Call LLM (Agent Mode only)   │
    │     └─ Claude/OpenAI             │
    │                                  │
    │  6. Store in Memory              │
    │     └─ LanceDB + PostgreSQL      │
    └──────┬───────────────────────────┘
           │
    ┌──────▼──────────────────────────┐
    │  RESPONSE (JSON)                 │
    │  ├─ result / response            │
    │  ├─ context_used (docs)          │
    │  ├─ sources (URLs)               │
    │  ├─ confidence (0-1)             │
    │  └─ metadata                     │
    └──────┬──────────────────────────┘
           │
    CLAUDE CODE (Recebe resposta)
    ├─ Usa no contexto
    ├─ Apresenta ao usuário
    └─ Opcionalmente armazena análise
       (POST /api/v1/knowledge/store)
```

---

## Key Features by Priority

### Phase 1 (MVP — 8 weeks)

- ✅ User authentication (email + password)
- ✅ RAG orchestrator (search + rerank + LLM)
- ✅ Agent Mode (chat → LLM → response)
- ✅ Tool Mode (knowledge.store, memory.query)
- ✅ Dashboard (settings, memory viewer)
- ✅ CLI (init, start, auth, dataset)
- ✅ Docker Compose (local dev)

### Phase 2 (Stabilization — 4 weeks)

- ✅ Comprehensive testing (E2E, load, security)
- ✅ Performance baselines
- ✅ Bug fixes + user feedback

### Phase 3 (Ecosystem — 8 weeks)

- ✅ Claude Code MCP integration
- ✅ Gemini CLI adapter
- ✅ Web search integration (SerpAPI)
- ✅ PAL Registry (community datasets)
- ✅ Monitoring (Prometheus + Sentry)

### Phase 4 (Enterprise — 6 weeks)

- ✅ Caching optimization
- ✅ System Tray (Windows)
- ✅ Package manager distribution
- ✅ RBAC + multi-user
- ✅ Auto-updates

### Phase 5 (Ongoing)

- ✅ Knowledge graphs
- ✅ Multi-agent orchestration
- ✅ SSO/SAML (enterprise)
- ✅ Plugin ecosystem
- ✅ Community growth

---

## Constraints & Guarantees

### Must-Have (Non-Negotiable)

- ✅ Roda em KVM1: 2 vCPU, 4GB RAM, 50GB NVMe
- ✅ Open-source (Apache 2.0)
- ✅ Zero vendor lock-in
- ✅ Multi-agent compatible
- ✅ RAG + LLM agnostic

### Performance Targets

- ✅ API response < 500ms p95
- ✅ Vector search < 150ms p95
- ✅ Vectora Cognitive Runtime inference 4-8ms
- ✅ Memory usage < 1.5GB peak

### Security

- ✅ Per-user data isolation
- ✅ Encryption at rest (AES-256)
- ✅ JWT for auth
- ✅ bcrypt for passwords
- ✅ No secrets in logs

### Scalability

- ✅ Suporta 100+ users localmente
- ✅ 1M+ vectors em LanceDB
- ✅ Goroutines para concorrência
- ✅ Redis Pub/Sub para invalidation

---

## Why VECTORA Matters

### Problem it Solves

- 🎯 Agents isolated = cada um guarda seu conhecimento
- 🔄 Código repetido = pattern, insight, análise são perdidos
- 📚 Sem memória = agent repete análise mesma coisa n vezes
- 🤖 Multi-agent ineficiente = agents não compartilham contexto

### VECTORA Solution

- 🧠 **Shared Memory** — todos agents acessam mesmo knowledge base
- 🔍 **Semantic Search** — encontra contexto relevante automaticamente
- 🎯 **Intelligence Reuse** — análise anterior reutilizada
- 🤝 **Agent Orchestration** — múltiplos agents colaboram
- 💾 **Persistent Learning** — sistema aprende ao longo do tempo

### For Who

- **Developers** — integram Vectora em seus agents/tools
- **Companies** — deploy local, zero cloud lock-in
- **Communities** — podem contribuir datasets + integrações
- **Enterprise** — self-hosted, RBAC, audit logs

---

## Quick Start (Depois de implementação)

```bash
# Install
brew install vectora  # ou apt, winget, etc

# Initialize
vectora init
# → cria ~/.vectora (config + embeddings)
# → inicia PostgreSQL embedded
# → inicia Redis
# → pronto para usar

# Start
vectora start
# → servidor roda em http://localhost:3000
# → dashboard em web browser
# → aguardando queries

# Use via CLI
vectora query "What is React hooks?"
# → busca docs, reranqueia, chama Claude
# → retorna resposta + sources

# Use via Dashboard
# → Abre browser, login, settings, memory viewer

# Use via Agent (Claude Code)
# → Claude Code chama /api/v1/chat/message
# → ou /api/v1/knowledge/store (Tool Mode)
```

---

## Comparison: VECTORA vs Alternatives

| Feature                | VECTORA           | LangChain         | RAGstack    | Llamaindex       |
| ---------------------- | ----------------- | ----------------- | ----------- | ---------------- |
| **Local-first**        | ✅ Yes            | ❌ Cloud-oriented | ✅ Yes      | ❌ Cloud-focused |
| **Multi-agent**        | ✅ Native         | ⚠️ Possible       | ⚠️ Possible | ❌ Single agent  |
| **Zero config**        | ✅ Docker Compose | ❌ Complex setup  | ⚠️ Moderate | ⚠️ Moderate      |
| **KVM1 viable**        | ✅ Yes (<1.5GB)   | ⚠️ Borderline     | ✅ Yes      | ⚠️ Tight         |
| **Open-source**        | ✅ Apache 2.0     | ✅ MIT            | ✅ Various  | ✅ MIT           |
| **Dashboard**          | ✅ Built-in       | ❌ No             | ⚠️ External | ❌ No            |
| **Package mgrs**       | ✅ (Phase 4)      | ❌ pip/npm        | ❌ No       | ❌ pip only      |
| **Community datasets** | ✅ PAL Registry   | ❌ No             | ❌ No       | ❌ No            |
| **Cost**               | 🆓 Free           | 🆓 Free           | 🆓 Free     | 🆓 Free          |
| **Maturity**           | 🚀 Pre-release    | ✅ Mature         | ⚠️ Alpha    | ✅ Mature        |

---

## Roadmap Visual

```
2026
 Q2 [Phase 1: MVP]      [Phase 2: Stabilize]
    May    Jun         July      Aug
    ├─────────────────────────────┤
    │ Backend ││ Testing
    │ Frontend││ Feedback
    │ CLI     ││ Optimization
    │ Docker  ││

 Q3 [Phase 3: Features]          [Phase 4: Enterprise]
    Sep    Oct         Nov      Dec    Jan
    ├─────────────────────────────┤
    │ Integrations │ Performance
    │ PAL Registry │ Package mgrs
    │ Web Search   │ System Tray

 2027 [Phase 5: Ecosystem — Ongoing]
    │ Community │ Advanced │ Enterprise │
    │ Growth    │ Features │ Support    │
```

---

## Contact & Community

- 📧 **GitHub:** github.com/vectora/vectora
- 💬 **Discord:** discord.gg/vectora (Phase 5)
- 📚 **Docs:** vectora.ai (Phase 3)
- 🤝 **Contributing:** github.com/vectora/vectora/CONTRIBUTING.md

---

## tl;dr

**VECTORA** = 🧠 Knowledge hub inteligente que:

- Busca semanticamente (Vector search)
- Reordena localmente (Reranking)
- Integra com LLMs (Agent Mode)
- Funciona como ferramenta (Tool Mode)
- Persiste memória (Multi-user isolation)
- Funciona em KVM1 (2 vCPU, 4GB RAM)
- Roda localmente (Open-source, zero cloud)
- Integra agentes (Claude Code, Gemini, etc)

**Próximos passos:**

1. Implementar Phase 1 (8 semanas)
2. Testar com usuários reais (Phase 2)
3. Expandir integrations (Phase 3)
4. Otimizar performance (Phase 4)
5. Crescer comunidade (Phase 5 — ongoing)

🚀 **Let's build the future of AI agents together!**

---

**Document Version:** 1.0
**Last Updated:** 2026-05-01
**Status:** ✅ Approved for Implementation
