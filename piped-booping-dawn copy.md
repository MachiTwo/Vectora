# VECTORA — AI Knowledge Agent + Memory System

## Roadmap, Architecture & Implementation Plan

---

## Executive Summary

**Vectora** é um subagent **installable** e open-source que gerencia conhecimento vetorizado com reranking local, web search, e acesso direto à memória para múltiplos agents (Claude Code, Gemini CLI, Paperclip, etc).

**Não é:** App standalone, SaaS, ou chat interface.
**É:** Knowledge hub inteligente com 2 modos operacionais.

---

## Mapa Mental (Vision)

```
┌─────────────────────────────────────────────────────────────┐
│                    VECTORA                                   │
│            Knowledge Memory System                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    ┌───▼──┐       ┌──▼──┐       ┌──▼────────┐
    │Agent │       │Tool │       │Dashboard  │
    │Mode  │       │Mode │       │(Config)   │
    │(LLM) │       │     │       │Always On  │
    └───┬──┘       └──┬──┘       └──┬────────┘
        │              │             │
        └──────────────┼─────────────┘
                       │
        ┌──────────────▼──────────────┐
        │   VECTORA Backend (Go)       │
        │                             │
        │  ├─ Vector Search (LanceDB) │
        │  ├─ Rerank (Voyage v2.5)    │
        │  ├─ Web Search + Fetch      │
        │  ├─ LLM Integration         │
        │  ├─ Knowledge Storage       │
        │  ├─ Memory Access (direct)  │
        │  └─ MCP Protocol            │
        └────┬────────────────────┬───┘
             │                    │
        ┌────▼──┐          ┌──────▼────┐
        │LanceDB│          │PostgreSQL │
        │Vector │          │SQLite     │
        │Store  │          │Metadata   │
        └───────┘          └────┬──────┘
                                │
                           ┌────▼─────┐
                           │Voyage API │
                           │(embed +   │
                           │rerank)    │
                           └───────────┘
```

---

## Operacional Modes (2 Modos Principais)

### Mode 1: Agent Mode (Full RAG)

```
External Query
    ↓
Vectora receives: POST /api/v1/chat/message
    ↓
[Vector Search in LanceDB]
    ↓
[Rerank with Voyage v2.5]
    ↓
[Web Search (if needed)]
    ↓
[Pass context to LLM]
    ↓
[LLM responds]
    ↓
Response + store in memory

Example:
Claude Code: "Help with React hooks"
→ Vectora searches knowledge
→ Reranks top-5 docs
→ Calls Claude with context
→ Responds + saves to memory
```

### Mode 2: Tool Mode (Structured Integration)

```
External Agent (Claude Code, Gemini, etc)
    ↓
JSON-RPC calls to Vectora:
    ├─ knowledge.store (save analyzed results)
    ├─ memory.query (search without LLM)
    ├─ tools.websearch (fetch + analyze)
    ├─ tools.rerank (rerank documents)
    └─ tools.list (list available tools)
    ↓
Agent uses responses in own reasoning
(Vectora = dumb storage + retrieval, Agent = smart analysis)

Example:
Claude Code queries own sources
→ Sends structured data to Vectora: knowledge.store
→ Later: queries Vectora memory for similar context
→ Uses in own analysis (no LLM layer)
```

---

## Dashboard (Interface de Configuração - Sempre Ativa)

Dashboard NÃO é um modo operacional, é a interface de **configuração** do Vectora que funciona em paralelo com ambos os modos:

```
Sempre Ativo em Paralelo:
    ↓
User accesses: https://app.fly.dev/vectora
    ↓
Login (email + password hash)
    ↓
Dashboard:
├─ Settings (API keys, password)
├─ Memory Viewer
│  ├─ Chat History (past queries)
│  ├─ Vector Memory (embeddings, docs indexed)
│  └─ Execution Logs
└─ Dataset Manager
   ├─ Browse PAL registry
   ├─ Install/uninstall datasets
   └─ Version management

Dashboard permite ao usuário:
- Configurar chaves de API (Voyage, Claude, OpenAI, etc)
- Visualizar histórico de memória
- Gerenciar datasets instalados
- Alterar senha e preferências
- Monitorar execução de queries (Agent Mode e Tool Mode)
```

---

## Integrations (Turborepo Monorepo Separado)

**Estrutura:** Repositório separado (`vectora-integrations`) usando Turborepo com packages compartilhados

### Agents Suportados & Padrão de Integração

| Agent            | Protocolo                    | Tipo     | Repo                       |
| ---------------- | ---------------------------- | -------- | -------------------------- |
| **Claude Code**  | MCP (Model Context Protocol) | Native   | `packages/claude-code`     |
| **Gemini CLI**   | REST API wrapper             | Adapter  | `packages/gemini-cli`      |
| **Paperclip**    | REST + MCP                   | Hybrid   | `packages/paperclip`       |
| **Hermes**       | REST API                     | Adapter  | `packages/hermes`          |
| **Custom Agent** | REST endpoint template       | Template | `packages/custom-template` |

### Padrão de Integração

Cada integração segue este padrão:

```
┌─────────────────────────────────┐
│     Agent (Claude Code, etc)    │
└────────────────┬────────────────┘
                 │
    ┌────────────▼─────────────┐
    │  Integration Package     │
    │  (@vectora/sdk-{agent})   │
    │                          │
    │  ├─ Client code          │
    │  ├─ Type definitions     │
    │  ├─ Protocol handlers    │
    │  └─ Examples             │
    └────────────┬─────────────┘
                 │
    ┌────────────▼─────────────────────────────┐
    │  Shared Packages (@vectora/shared)        │
    │  ├─ Types & interfaces                   │
    │  ├─ Auth helpers (JWT, encryption)       │
    │  ├─ HTTP client utilities                │
    │  ├─ Error handling                       │
    │  └─ Constants & config                   │
    └────────────┬─────────────────────────────┘
                 │
         ┌───────▼────────┐
         │                │
    ┌────▼────┐    ┌─────▼──┐
    │Vectora   │    │PAL     │
    │Backend  │    │Registry│
    │(REST)   │    │(API)   │
    └─────────┘    └────────┘
```

### Estrutura do Turborepo (vectora-integrations)

```
vectora-integrations/
├── packages/
│   ├── shared/                     # Shared utilities
│   │   ├── src/
│   │   │   ├── types/
│   │   │   │   ├── vectora.ts      # Vectora API types
│   │   │   │   ├── agents.ts      # Agent types
│   │   │   │   └── auth.ts        # Auth types
│   │   │   ├── auth/
│   │   │   │   ├── jwt.ts
│   │   │   │   └── encryption.ts
│   │   │   ├── http/
│   │   │   │   └── client.ts
│   │   │   ├── errors/
│   │   │   │   └── index.ts
│   │   │   └── constants.ts
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   ├── claude-code/                # Claude Code integration (MCP)
│   │   ├── src/
│   │   │   ├── mcp/
│   │   │   │   ├── server.ts       # MCP protocol server
│   │   │   │   ├── handlers.ts     # Tool handlers
│   │   │   │   └── types.ts
│   │   │   ├── client.ts           # Vectora client wrapper
│   │   │   ├── tools/
│   │   │   │   ├── search.ts       # Vector search tool
│   │   │   │   ├── rerank.ts       # Reranking tool
│   │   │   │   ├── websearch.ts    # Web search tool
│   │   │   │   └── knowledge.ts    # Knowledge store tool
│   │   │   └── index.ts
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   ├── gemini-cli/                 # Gemini CLI integration
│   │   ├── src/
│   │   │   ├── client.ts           # Gemini client wrapper
│   │   │   ├── vectora-adapter.ts   # REST adapter to Vectora
│   │   │   ├── tools.ts            # Tool definitions
│   │   │   └── index.ts
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   ├── paperclip/                  # Paperclip integration
│   │   ├── src/
│   │   │   ├── plugin.ts           # Paperclip plugin
│   │   │   ├── mcp-bridge.ts       # MCP protocol bridge
│   │   │   ├── rest-bridge.ts      # REST API bridge
│   │   │   └── index.ts
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   ├── hermes/                     # Hermes agent integration
│   │   ├── src/
│   │   │   ├── client.ts           # Hermes client
│   │   │   ├── vectora-adapter.ts   # REST adapter
│   │   │   └── index.ts
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   └── custom-template/            # Template para custom agents
│       ├── src/
│       │   ├── client.ts
│       │   ├── adapter.ts
│       │   └── index.ts
│       ├── package.json
│       └── README.md
│
├── apps/
│   └── docs/                       # Shared integration docs
│       ├── content/
│       ├── package.json
│       └── next.config.js
│
├── turbo.json
├── package.json (root)
├── pnpm-workspace.yaml (ou yarn workspaces)
├── tsconfig.base.json
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── build.yml
│       └── publish.yml
├── .gitignore
├── README.md
└── LICENSE (Apache 2.0)
```

### Como Funciona Cada Integração

#### Claude Code (MCP Protocol)

```
Claude Code
    ↓ (calls MCP server)
Vectora Integration (@vectora/claude-code)
    ├─ Expõe tools via MCP protocol:
    │  ├─ vectora.search (vector search)
    │  ├─ vectora.rerank (local reranking)
    │  ├─ vectora.websearch (web search + fetch)
    │  └─ vectora.store (knowledge storage)
    ↓
Vectora Backend (/api/v1/*)
```

#### Gemini CLI (REST Adapter)

```
Gemini CLI
    ↓ (calls REST endpoint)
Vectora Integration (@vectora/gemini-cli)
    ├─ Wraps Gemini client
    ├─ Translates Gemini tools to Vectora API
    │  ├─ Gemini function_calling → /api/v1/tools/*
    │  ├─ Gemini context → /api/v1/memory/query
    ├─ Returns results back to Gemini
    ↓
Vectora Backend (/api/v1/*)
```

#### Paperclip (Hybrid MCP + REST)

```
Paperclip
    ├─ Via MCP: expõe Vectora tools direto
    └─ Via REST: chamadas síncronas para Vectora
        ↓
Vectora Integration (@vectora/paperclip)
    ├─ MCP bridge (protocol handler)
    ├─ REST bridge (HTTP client)
    ↓
Vectora Backend (/api/v1/*)
```

### Shared Package (@vectora/shared)

Todas as integrações dependem de `@vectora/shared` que fornece:

```typescript
// types
export interface VectoraClient {
  chat(query: string, dataset: string): Promise<Response>;
  knowledgeStore(data: KnowledgeData): Promise<void>;
  memoryQuery(query: string): Promise<SearchResults>;
  tools: {
    websearch(query: string): Promise<SearchResults>;
    rerank(docs: Document[], query: string): Promise<RankedDocs>;
  };
}

// auth
export { encryptAPIKey, decryptAPIKey };
export { generateJWT, verifyJWT };

// http client
export { createVectoraClient };

// errors
export { VectoraError, ValidationError, AuthError };

// constants
export { VECTORA_API_VERSION, ENDPOINTS };
```

### Build & Publish

```bash
# Turborepo handles building all packages
turbo build

# Publish individual packages to npm
pnpm publish --filter=@vectora/shared
pnpm publish --filter=@vectora/claude-code
pnpm publish --filter=@vectora/gemini-cli
# etc...
```

---

## Complete Architecture

```
┌──────────────────────────────────────────────────────────────┐
│              INTEGRATION LAYER (Turborepo)                   │
│  @vectora/claude-code │ @vectora/gemini-cli                    │
│  @vectora/paperclip   │ @vectora/hermes │ @vectora/shared       │
│        (MCP)         │     (REST)              (Types)       │
└────────────┬─────────────────┬────────────────────────────────┘
             │                 │
             └────────┬────────┘
                      │
   ┌──────────────────▼──────────────────┐
   │  VECTORA BACKEND (Go - Echo/Gin)     │
   │                                     │
   │  API Endpoints (2 Modos):           │
   │  ├─ /api/v1/chat/*                  │
   │  │  └─ Agent Mode (LLM decision)    │
   │  ├─ /api/v1/knowledge/*             │
   │  ├─ /api/v1/memory/*                │
   │  ├─ /api/v1/tools/*                 │
   │  │  └─ Tool Mode (no LLM layer)     │
   │  ├─ /api/v1/datasets/*              │
   │  ├─ /api/v1/auth/*                  │
   │  └─ /api/v1/settings/*              │
   │                                     │
   │  Core Services:                     │
   │  ├─ RAG Orchestrator                │
   │  │  ├─ Vector Search (LanceDB)      │
   │  │  ├─ Reranker (Voyage v2.5)       │
   │  │  └─ Context Builder              │
   │  ├─ LLM Integration                 │
   │  │  ├─ Claude, OpenAI, Google       │
   │  ├─ Tools                           │
   │  │  ├─ Web Search & Fetch           │
   │  │  ├─ Reranking                    │
   │  ├─ User Management & Auth          │
   │  └─ MCP Protocol Handler            │
   └────┬──────────────────────┬─────────┘
        │                      │
   ┌────▼──┐            ┌─────▼──────┐
   │LanceDB │            │PostgreSQL  │
   │Vectors │            │ / SQLite   │
   │(local) │            │(metadata)  │
   └────────┘            └────────────┘

┌──────────────────────────────────────────────────────────────┐
│  VECTORA DASHBOARD (React + Vite) — Sempre Ativa              │
│  Interface de Configuração: https://app.fly.dev/vectora       │
│                                                              │
│  ├─ Login Page                                              │
│  ├─ Settings (API keys, password, preferências)             │
│  ├─ Memory Viewer (histórico, embeddings, logs)             │
│  └─ Dataset Manager (browse PAL, instalar/desinstalar)      │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  VECTORA CLI (Go + Cobra)                                     │
│  $ vectora init / start / dataset install / ...               │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  External Services                                           │
│  ├─ Voyage AI SDK (embeddings + reranking)                   │
│  └─ Web Search API (SerpAPI ou Google Search)                │
└──────────────────────────────────────────────────────────────┘
```

---

## Complete API Endpoints

```
╔═══════════════════════════════════════════════════════╗
║              AGENT MODE ENDPOINTS                    ║
╚═══════════════════════════════════════════════════════╝

POST   /api/v1/chat/message
  Query + dataset selection
  → Search + Rerank + LLM → Response

╔═══════════════════════════════════════════════════════╗
║              TOOL MODE ENDPOINTS                     ║
╚═══════════════════════════════════════════════════════╝

POST   /api/v1/knowledge/store
  Save analyzed results from external agent

GET    /api/v1/memory/query
  Search embeddings without LLM layer

POST   /api/v1/tools/websearch
  Search + fetch web content

POST   /api/v1/tools/rerank
  Rerank documents locally

GET    /api/v1/tools/list
  List available tools

╔═══════════════════════════════════════════════════════╗
║           DATASET MANAGEMENT ENDPOINTS               ║
╚═══════════════════════════════════════════════════════╝

GET    /api/v1/datasets
  List installed datasets

POST   /api/v1/datasets/install
  Install from PAL registry

DELETE /api/v1/datasets/{name}
  Uninstall dataset

GET    /api/v1/datasets/registry/browse
  Browse PAL (Vectora Asset Library)

╔═══════════════════════════════════════════════════════╗
║              AUTH & SETTINGS                         ║
╚═══════════════════════════════════════════════════════╝

POST   /api/v1/auth/login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh

GET    /api/v1/settings
POST   /api/v1/settings/api-keys
POST   /api/v1/settings/password

╔═══════════════════════════════════════════════════════╗
║              ADMIN/LOGS                              ║
╚═══════════════════════════════════════════════════════╝

GET    /api/v1/logs/chat
GET    /api/v1/logs/execution
GET    /api/v1/memory/stats
```

---

## Technology Stack (Final)

| Layer                | Technology                        | Purpose                                      |
| -------------------- | --------------------------------- | -------------------------------------------- |
| **Frontend**         | React 18 + Vite                   | Admin dashboard (settings, memory, datasets) |
| **Styling**          | TailwindCSS                       | UI/UX                                        |
| **State**            | Zustand                           | Client-side state                            |
| **Data Fetch**       | SWR/Fetch API                     | REST client                                  |
| **Backend**          | Go (Echo/Gin)                     | REST API + MCP                               |
| **Vector Store**     | LanceDB                           | Local embeddings                             |
| **Database**         | PostgreSQL / SQLite               | Metadata + chat history                      |
| **Embeddings**       | Voyage AI SDK (Go)                | Embedding generation                         |
| **Reranking**        | Voyage Reranker v2.5              | Local reranking                              |
| **LLM Integration**  | Multiple (Claude, OpenAI, Google) | LLM calls                                    |
| **CLI**              | Go + Cobra                        | Command-line interface                       |
| **Web Search**       | SerpAPI / Google Search API       | Web search + fetch                           |
| **Auth**             | bcrypt                            | Password hashing                             |
| **Crypto**           | AES-256                           | API key encryption                           |
| **Deployment**       | Docker Compose                    | Local + VPS                                  |
| **Package Managers** | brew, apt, winget, pacman         | Distribution                                 |

---

## Configuration Management (Fail-Fast + Smart Defaults)

```go
// config/config.go
type Config struct {
    Server   ServerConfig
    Database DatabaseConfig
    Vector   VectorConfig
    Auth     AuthConfig
    LLM      LLMConfig
    Services ServicesConfig
    Logging  LoggingConfig
}

// Validation: CRITICAL fields (fail-fast), OPTIONAL fields (defaults)
func (c Config) Validate() error {
    // CRITICAL - No defaults, must be provided
    if c.Database.DSN == "" {
        return fmt.Errorf("DATABASE_URL: required, use postgresql://user:pass@localhost:5432/vectora")
    }
    if len(c.Auth.JWTSecret) < 32 {
        return fmt.Errorf("JWT_SECRET: must be >= 32 chars for security")
    }

    // OPTIONAL - Use defaults if not provided
    if c.Server.Port == 0 {
        c.Server.Port = 3000
    }
    if c.Logging.Level == "" {
        c.Logging.Level = "info"
    }

    // Validation de ranges
    if c.Server.Port < 1 || c.Server.Port > 65535 {
        return fmt.Errorf("SERVER_PORT: must be 1-65535")
    }

    return nil
}

// Load: godotenv + env vars + validation
func Load() (*Config, error) {
    godotenv.Load(".env")

    cfg := &Config{
        Server: ServerConfig{
            Port: envInt("SERVER_PORT", 0),  // 0 = use default
            Host: envStr("SERVER_HOST", "0.0.0.0"),
        },
        Database: DatabaseConfig{
            DSN: envStr("DATABASE_URL", ""),  // REQUIRED
        },
        Auth: AuthConfig{
            JWTSecret: envStr("JWT_SECRET", ""),  // REQUIRED (>= 32 chars)
        },
        Logging: LoggingConfig{
            Level: envStr("LOG_LEVEL", "info"),  // default: info
        },
    }

    if err := cfg.Validate(); err != nil {
        return nil, err  // Exit with clear error message
    }

    return cfg, nil
}
```

**.env.example:**

```
# CRITICAL (required, no defaults)
DATABASE_URL=postgresql://user:password@localhost:5432/vectora
JWT_SECRET=your-secret-min-32-chars-change-in-production

# LLM API Keys (at least one required for Agent Mode)
CLAUDE_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...

# Tools (optional, but recommended for web search)
VOYAGE_API_KEY=...
SERPAPI_API_KEY=...

# OPTIONAL (have sensible defaults)
SERVER_PORT=3000
SERVER_HOST=0.0.0.0
LOG_LEVEL=info
DATABASE_SSL_MODE=disable
LANCE_DB_PATH=/data/vectordb

# Advanced (optional)
SENTRY_DSN=
PROMETHEUS_ENABLED=true
AUTH_TOKEN_TTL=3600
AUTH_REFRESH_TTL=604800
```

---

## Logging System (slog + JSON + Runtime Control)

```go
// platform/logger/init.go
func Init(level string) error {
    logLevel := parseLevel(level)  // debug|info|warn|error

    opts := &slog.HandlerOptions{
        Level:     logLevel,
        AddSource: true,  // Include file:line in logs
    }

    // JSON output (parseable for observability)
    handler := slog.NewJSONHandler(os.Stdout, opts)
    slog.SetDefault(slog.New(handler))

    return nil
}

// Runtime log level change (for debugging in production)
// PUT /debug/loglevel?level=debug (requires auth)
func SetLogLevel(ctx context.Context, level string) error {
    newLevel := parseLevel(level)
    // slog implementation allows runtime level changes
    slog.SetDefault(slog.New(
        slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
            Level:     newLevel,
            AddSource: true,
        }),
    ))
    return nil
}
```

**Log Output (JSON):**

```json
{
  "time": "2026-05-01T10:30:45.123Z",
  "level": "INFO",
  "source": "internal/api/handlers/chat.go:42",
  "msg": "Chat request processed",
  "user_id": "user-123",
  "query_length": 125,
  "duration_ms": 345,
  "status": "success"
}
```

---

## Database Schema (PostgreSQL / SQLite)

```sql
-- Users & Auth
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- API Keys (encrypted)
CREATE TABLE api_keys (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  voyage_key BYTEA,  -- AES-256 encrypted
  openai_key BYTEA,
  claude_key BYTEA,
  google_key BYTEA,
  created_at TIMESTAMP
);

-- Datasets
CREATE TABLE datasets (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  name VARCHAR(255),
  version VARCHAR(50),
  source VARCHAR(100),  -- 'local', 'pal_registry', 'web_search'
  local_path TEXT,
  metadata JSONB,
  installed_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Chat History
CREATE TABLE chat_history (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  query TEXT NOT NULL,
  response TEXT,
  datasets_used TEXT[],  -- array of dataset names
  model_used VARCHAR(100),
  context_used JSONB,
  timestamp TIMESTAMP
);

-- Execution Logs
CREATE TABLE execution_logs (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  action VARCHAR(100),
  status VARCHAR(20),
  details JSONB,
  error_message TEXT,
  duration_ms INT,
  timestamp TIMESTAMP
);

-- Memory Metadata (Vector references)
CREATE TABLE memory_metadata (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  source_type VARCHAR(50),  -- 'dataset', 'web_search', 'user_stored'
  source_reference TEXT,
  lance_db_id TEXT,  -- reference to LanceDB vector
  title TEXT,
  url TEXT,
  created_at TIMESTAMP
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_api_keys_user_id ON api_keys(user_id);
CREATE INDEX idx_datasets_user_id ON datasets(user_id);
CREATE INDEX idx_chat_user_id ON chat_history(user_id);
CREATE INDEX idx_logs_user_id ON execution_logs(user_id);
CREATE INDEX idx_memory_user_id ON memory_metadata(user_id);
```

---

## Multi-User Isolation

```go
// Every request enforced by middleware
middleware.RequireAuth(c)
userId := c.Get("user_id")  // from JWT token

// All queries filtered by user_id
db.Where("user_id = ?", userId).Find(&results)

// API keys encrypted per user
keys := getAPIKeys(userId)  // AES-256 decrypt on-demand
```

**Encryption:**

- Password: bcrypt (cost 12, salted)
- API Keys: AES-256 at rest
- Tokens: JWT (short-lived)

---

## Installation Methods

### Package Managers (Primary)

```bash
# macOS
brew install vectora

# Ubuntu/Debian
apt install vectora

# Windows
winget install vectora

# Arch Linux
pacman -S vectora
```

### Direct Binary

```bash
curl -L https://releases.vectora.ai/vectora-latest-linux-x64.tar.gz | tar xz
./vectora init
./vectora start
```

### Docker (VPS)

```bash
docker run -d \
  -e DATABASE_URL=postgresql://... \
  -p 3000:3000 \
  vectora:latest
```

---

## PAL (Vectora Asset Library)

**Registry API (hosted by Vectora team):**

```
GET    /api/registry/v1/datasets             # List
GET    /api/registry/v1/datasets/{name}      # Get info
GET    /api/registry/v1/datasets/{name}/download
POST   /api/registry/v1/datasets/publish     # Community upload
```

**Dataset Package Format:**

```
godot-4.6-docs-v1.tar.gz
├── vectors.lance              # LanceDB format
├── AGENTS.md                  # System prompt
├── metadata.json
│   ├── version: "4.6.1"
│   ├── vectors: 10000
│   ├── size_mb: 500
│   └── checksum: "sha256:..."
├── examples/
└── docs/
```

**Community Contribution:**

```bash
# User creates dataset
vectora dataset create --name godot-4.6-docs
# Adds docs, configs, etc
# Publishes
vectora dataset publish --name godot-4.6-docs
# Available in PAL registry for others
```

---

## Frentes de Trabalho (10 Frentes no Monorepo)

### `vectora/` (6 Frentes)

1. **Frente 1: Backend Core (Go Tier-Based)**
   - Tier-based architecture (8 camadas)
   - RAG orchestrator, vector search, reranking
   - LLM integration (Claude, OpenAI, Google)
   - User management, multi-user isolation
   - Repo: `vectora/backend`

2. **Frente 2: Storage Layer (LanceDB + PostgreSQL)**
   - LanceDB integration (vector storage)
   - PostgreSQL/SQLite schema
   - Database migrations
   - Per-user namespace isolation
   - Repo: `vectora/backend/internal/storage` + `migrations/`

3. **Frente 3: API Layer (REST + MCP)**
   - REST API handlers (Agent Mode, Tool Mode, etc)
   - 6+ middlewares (auth, logging, recovery, cors, rate_limit, request_id)
   - MCP protocol handler
   - WebSocket support (real-time updates)
   - Repo: `vectora/backend/internal/api` + `mcp/`

4. **Frente 4: Frontend Dashboard (React + Vite)**
   - Login, settings, memory viewer, dataset manager
   - Analytics dashboard (real-time metrics)
   - Real-time WebSocket updates
   - Zustand state management
   - Repo: `vectora/frontend`

5. **Frente 5: CLI (Go + Cobra)**
   - `vectora init`, `vectora start`, `vectora auth`, `vectora dataset`, `vectora memory`
   - Configuration management
   - Local daemon/service management
   - Repo: `vectora/cli`

6. **Frente 6: DevOps & Infrastructure**
   - Docker Compose (local dev)
   - GitHub Actions CI/CD (lint, test, build, publish)
   - Pre-commit hooks (gofmt, golangci-lint, go vet)
   - Multi-platform builds (linux, macos, windows)
   - Repo: `vectora/infra` + `.github/workflows`

---

### `vectora-asset-library/` (1 Frente)

7. **Frente 7: PAL Registry (Dataset Management)**
   - Dataset structure validation
   - Auto-index generation (index.json)
   - Community contribution workflow
   - Registry API (https://registry.vectora.ai)
   - Repo: `vectora-asset-library/`

---

### `vectora-integrations/` (2 Frentes - Turborepo)

8. **Frente 8: Shared SDK**
   - @vectora/shared (types, auth, HTTP client, errors)
   - Common utilities para todas integrações
   - Type definitions centralizadas
   - Repo: `vectora-integrations/packages/shared`

9. **Frente 9: Agent Integrations**
   - @vectora/sdk-claude-code (MCP protocol)
   - @vectora/sdk-openai (REST)
   - @vectora/sdk-chatgpt (Plugin)
   - @vectora/sdk-gemini-cli (REST)
   - @vectora/sdk-vscode (VSCode extension)
   - @vectora/sdk-hermes (REST)
   - @vectora/sdk-codex (REST)
   - @vectora/sdk-openclaw (REST)
   - @vectora/template (Custom agent template)
   - Repo: `vectora-integrations/packages/{sdk-*}/`

---

### `vectora-website/` (1 Frente)

10. **Frente 10: Website & Documentation**
    - Home page (vectora.ai)
    - Getting started (local, Docker, VPS)
    - API documentation (auto-gen from OpenAPI)
    - Integration guides (para cada SDK)
    - Architecture docs
    - Contributing guide
    - Tech: Hugo + Hextra (multilingual: en, pt-br)
    - Repo: `vectora-website/`

---

## Implementation Roadmap (5 Fases)

### Phase 1: Foundation (8-10 weeks)

**Goal: MVP operacional com arquitetura tier-based**

**Backend:**

- ✅ Go project com tier-based architecture (8 camadas)
- ✅ Config validation (fail-fast críticos, defaults opcionais)
- ✅ slog + JSON logging + runtime changes (/debug/loglevel)
- ✅ PostgreSQL schema + LanceDB integration
- ✅ User auth (bcrypt + JWT)
- ✅ API key encryption (AES-256)
- ✅ RAG orchestrator (Agent Mode: search + rerank + LLM)
- ✅ Memory persistence (per-user isolation)
- ✅ Basic Tool Mode (knowledge.store, memory.query)
- ✅ MCP protocol handler
- ✅ 6+ middlewares (auth, logging, recovery, cors, rate_limit, request_id)

**Frontend:**

- ✅ React + Vite setup (não Next.js)
- ✅ Login page (email + password)
- ✅ Settings (API keys, password)
- ✅ Memory Viewer (basic - chat history)
- ✅ Dataset Manager (browse, install)

**CLI:**

- ✅ `vectora init` (setup local)
- ✅ `vectora start` (start server)
- ✅ `vectora auth --set-password`
- ✅ `vectora dataset list/install`

**DevOps:**

- ✅ Docker Compose (PostgreSQL, LanceDB, Vectora)
- ✅ CI/CD básico (lint, test, build)
- ✅ Pre-commit hooks (gofmt, golangci-lint, go vet)

**Docs:**

- ✅ Setup guide (local, Docker)
- ✅ Architecture overview
- ✅ API reference (auto-gen from OpenAPI)

---

### Phase 2: Stabilization (3-4 weeks)

**Goal: Testar MVP, coletar feedback, bugfixes**

- ✅ Testes end-to-end (E2E)
- ✅ Load testing (k6 ou similar)
- ✅ Bugfixes baseados em early feedback
- ✅ Documentação melhorada (user guides)
- ✅ Performance profiling inicial
- ✅ Security audit (OWASP Top 10)

---

### Phase 3: Features & Integrations (6-8 weeks)

**Goal: Multi-agent support + Tool mode completo + Agent Integrations**

**Backend Enhancements:**

- ✅ Tool Mode completo (tools.websearch, tools.rerank)
- ✅ Web search integration (SerpAPI ou Google Search API)
- ✅ Multi-LLM support (Claude, OpenAI, Google selection)
- ✅ Advanced memory (vector memory visualization, execution logs)
- ✅ Dataset management (PAL registry integration)

**Agent Integrations (vectora-integrations turborepo):**

- ✅ @vectora/claude-code (MCP protocol)
- ✅ @vectora/gemini-cli (REST adapter)
- ✅ @vectora/paperclip (Hybrid MCP + REST)
- ✅ @vectora/shared (shared types, auth, HTTP client)
- ✅ @vectora/hermes (REST adapter)

**Frontend Enhancements:**

- ✅ Analytics dashboard (real-time metrics)
- ✅ Advanced Memory Viewer (vector visualization)
- ✅ Execution Logs viewer

---

### Phase 4: Performance & Polish (4-6 weeks)

**Goal: Produção-ready, otimizações, monitoring**

- ✅ Caching (vector search results, LLM responses)
- ✅ Rate limiting (per-user + global)
- ✅ Monitoring (Prometheus, Sentry, health checks)
- ✅ Advanced CI/CD (multi-stage builds, container registry)
- ✅ Performance optimizations (indexing, batch processing)
- ✅ System Tray (Windows - fase 2 desse, não MVP)
- ✅ Package manager distribution (brew, apt, winget)

---

### Phase 5: Ecosystem & Community (ongoing)

**Goal: Open-source ecosystem, community datasets, enterprise features**

- ✅ PAL Registry (community uploads, versioning, ratings)
- ✅ Advanced features (multi-dataset queries, knowledge graphs)
- ✅ Enterprise features (SSO, SAML, advanced RBAC)
- ✅ More agent integrations (custom template support)
- ✅ Community documentation
- ✅ Auto-updates (binary + CLI)

---

## Backend Architecture: Tier-Based (8 Camadas)

```
vectora/backend/internal/

├── Tier 1: config/              # Configuration + Validation
│   ├── config.go               # Centralized config (fail-fast críticos, defaults opcionais)
│   ├── validation.go           # Config validation
│   └── secrets.go              # Secret management (AES-256)
│
├── Tier 2: platform/            # Platform Abstraction
│   ├── crypto/
│   │   ├── encrypt.go
│   │   └── decrypt.go
│   ├── auth/
│   │   ├── jwt.go
│   │   ├── password.go         # bcrypt
│   │   └── mfa.go              # 2FA (Phase 2+)
│   └── logger/                 # slog + JSON + runtime changes
│       ├── init.go
│       └── hooks.go
│
├── Tier 3: storage/             # Persistence Layer
│   ├── db.go                   # PostgreSQL/SQLite abstraction
│   ├── vector/
│   │   ├── store.go            # LanceDB
│   │   ├── search.go
│   │   └── namespace.go        # Per-user isolation
│   └── models/
│       ├── user.go
│       ├── dataset.go
│       ├── chat.go
│       └── execution_log.go
│
├── Tier 4: llm/                 # LLM Integration
│   ├── claude/
│   ├── openai/
│   ├── google/
│   └── base.go                 # LLM interface
│
├── Tier 5: core/                # Core Business Logic
│   ├── rag/                     # RAG + Tools Orchestration
│   │   ├── orchestrator.go      # Agent Mode + Tool Mode
│   │   ├── search.go            # Vector search
│   │   ├── rerank.go            # Reranking (Voyage v2.5)
│   │   ├── context.go           # Context building
│   │   ├── websearch.go         # Web search + fetch
│   │   ├── executor.go          # Tool executor (with retry)
│   │   └── circuit_breaker.go   # Resilience
│   └── memory/                  # Memory Management
│       ├── manager.go           # Memory lifecycle
│       ├── persistence.go       # Save to storage
│       └── isolation.go         # Per-user isolation
│
├── Tier 6: api/                 # HTTP API Layer
│   ├── router.go                # Chi router setup
│   ├── middleware/              # 6+ middlewares
│   │   ├── auth.go
│   │   ├── logging.go
│   │   ├── recovery.go
│   │   ├── cors.go
│   │   ├── rate_limit.go
│   │   ├── request_id.go
│   │   └── validation.go
│   ├── handlers/
│   │   ├── chat.go              # Agent Mode
│   │   ├── knowledge.go         # Tool Mode
│   │   ├── memory.go
│   │   ├── datasets.go
│   │   ├── auth.go
│   │   ├── settings.go
│   │   └── debug.go             # /debug/loglevel (runtime)
│   └── response.go              # Standardized responses
│
├── Tier 7: mcp/                 # MCP Protocol Handler
│   ├── server.go
│   ├── handlers.go
│   ├── tools.go
│   └── protocol.go
│
└── Tier 8: shared/              # Shared Utilities
    ├── errors/
    │   ├── vectora_error.go
    │   ├── validation_error.go
    │   └── auth_error.go
    ├── constants/
    │   └── constants.go
    └── types/
        ├── types.go
        └── enums.go
```

## Repo Structure (2 Repositórios)

### `vectora/` (Principal)

```
vectora/
├── backend/                    # Go backend
│   ├── cmd/
│   │   ├── vectora/            # CLI entry point
│   │   │   ├── main.go
│   │   │   └── config.go
│   │   └── server/            # Server entry point
│   │       └── main.go
│   ├── internal/               # Tier-based (8 camadas)
│   │   ├── config/
│   │   ├── platform/
│   │   ├── storage/
│   │   ├── llm/
│   │   ├── core/
│   │   ├── api/
│   │   ├── mcp/
│   │   └── shared/
│   ├── migrations/             # SQL migrations (Alembic style)
│   ├── go.mod
│   ├── go.sum
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .pre-commit-config.yaml
│
├── frontend/                   # React + Vite
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.tsx
│   │   │   ├── Settings.tsx
│   │   │   ├── MemoryViewer.tsx
│   │   │   ├── DatasetManager.tsx
│   │   │   └── Layout.tsx
│   │   ├── pages/
│   │   │   ├── auth.tsx
│   │   │   ├── dashboard.tsx
│   │   │   └── datasets.tsx
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   └── useAPI.ts
│   │   ├── store/
│   │   │   └── store.ts       # Zustand store
│   │   ├── api/
│   │   │   └── client.ts      # API client
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   ├── index.html
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── tsconfig.json
│   ├── package.json
│   └── Dockerfile
│
├── cli/                        # Go CLI
│   ├── cmd/
│   │   └── main.go
│   ├── internal/
│   │   ├── commands/
│   │   ├── config/
│   │   └── client/
│   ├── go.mod
│   ├── Dockerfile
│   └── Makefile
│
├── docs/                       # Documentation
│   ├── content/
│   ├── static/
│   └── config.toml
│
├── infra/
│   ├── docker-compose.yml
│   ├── Dockerfile.base
│   └── scripts/
│
├── .github/
│   └── workflows/
│
├── .gitignore
├── README.md
└── LICENSE (Apache 2.0)
```

### `vectora-integrations/` (Turborepo)

```
vectora-integrations/
├── packages/
│   ├── shared/                 # Shared types & utilities
│   │   ├── src/
│   │   │   ├── types/
│   │   │   ├── auth/
│   │   │   ├── http/
│   │   │   ├── errors/
│   │   │   └── constants.ts
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   ├── claude-code/            # Claude Code integration (MCP)
│   │   ├── src/
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   ├── gemini-cli/             # Gemini CLI integration
│   │   ├── src/
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   ├── paperclip/              # Paperclip integration
│   │   ├── src/
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   ├── hermes/                 # Hermes integration
│   │   ├── src/
│   │   ├── examples/
│   │   ├── package.json
│   │   └── README.md
│   │
│   └── custom-template/        # Template para custom agents
│       ├── src/
│       ├── package.json
│       └── README.md
│
├── apps/
│   └── docs/                   # Integration docs
│       ├── content/
│       └── package.json
│
├── turbo.json
├── pnpm-workspace.yaml
├── tsconfig.base.json
├── package.json
├── .github/
│   └── workflows/
├── .gitignore
├── README.md
└── LICENSE (Apache 2.0)
```

---

## Key Implementation Notes

### Vector Store (LanceDB)

- Per-user isolation: namespace or separate collections
- Metadata indexed alongside vectors
- Reranker receives top-K from search, returns reranked

### Reranker Local

- Voyage v2.5 SDK (Go)
- Processes search results locally
- No additional API calls (already have API key)
- Returns scored documents

### Web Search Integration

- SerpAPI or Google Search API
- Fetch full page content
- Parse and embed
- Store in LanceDB with metadata

### Tool Mode Flow

```
External Agent:
  → POST /api/v1/knowledge/store
  → {query, results, analysis, metadata}
  → Vectora embeds and stores
  → Next query can access

Later:
  → GET /api/v1/memory/query?q=...
  → Returns embeddings without LLM
  → Agent uses in own reasoning
```

### Auth & Isolation

- Session management: JWT tokens
- User context in middleware
- All DB queries filtered by user_id
- API keys encrypted at rest

---

## Comparativo: Original vs Melhorado (com Vectora Patterns)

| Aspecto              | Original         | Melhorado                                                                 |
| -------------------- | ---------------- | ------------------------------------------------------------------------- |
| **Arquitetura**      | Flat `internal/` | Tier-based (8 camadas)                                                    |
| **Config**           | Simples          | Fail-fast críticos + defaults opcionais                                   |
| **Logging**          | Básico (stdout)  | slog + JSON + runtime changes                                             |
| **Validation**       | Limited          | Comprehensive (fail-fast)                                                 |
| **Middlewares**      | Basic            | 6+ (auth, logging, recovery, cors, rate_limit, request_id)                |
| **Error Handling**   | Simples          | Custom error types (VectoraError, ValidationError, AuthError)             |
| **Memory Isolation** | Simples          | Per-user namespaces em LanceDB + metadata em PostgreSQL                   |
| **System Tray**      | ❌               | ✅ Fase 2+ (Windows)                                                      |
| **Dashboard**        | Básico           | Com analytics (memory usage, query latency, tool success rate)            |
| **CI/CD**            | Simples          | Multi-stage (lint → test → build → publish)                               |
| **Pre-commit**       | ❌               | ✅ (gofmt, golangci-lint, go vet)                                         |
| **Docs**             | Markdown         | Hugo + Hextra (structured, searchable)                                    |
| **Roadmap**          | 3 fases          | 5 fases (Foundation → Stabilization → Features → Performance → Ecosystem) |
| **DB**               | SQLite           | PostgreSQL (default) + SQLite (fallback)                                  |
| **Deployment**       | Docker only      | Docker + package managers (brew, apt, winget)                             |

---

## Success Metrics by Phase

✅ **Phase 1 (Foundation) - Week 10:**

- Tier-based architecture implementada
- Config validation (fail-fast)
- RAG orchestrator funcionando
- Agent Mode + Tool Mode básico
- Dashboard com login + settings
- CLI funcional (init, start, auth)

✅ **Phase 2 (Stabilization) - Week 14:**

- 0 critical bugs
- E2E tests passing
- Load test results OK
- Early user feedback incorporated
- Security audit completed

✅ **Phase 3 (Features) - Week 22:**

- Multiple agents can use
- Web search integrated
- Agent integrations (Claude Code, Gemini)
- PAL registry live
- Multi-LLM support
- Analytics dashboard

✅ **Phase 4 (Performance) - Week 28:**

- Performance optimized (search < 200ms)
- Caching implemented
- Monitoring live (Prometheus)
- System tray (Windows)
- Package manager distribution ready

✅ **Phase 5 (Ecosystem) - Ongoing:**

- Community datasets in PAL
- Multiple agent integrations
- Enterprise features
- 1k+ GitHub stars

---

## Decisões Arquiteturais (Melhorias com Vectora)

### 1. Tier-Based Architecture (8 Camadas)

**Decisão:** Usar arquitetura tier-based simplificada, **NÃO** separar `core/rag` de `tools/`

- ✅ Tiers: config → platform → storage → llm → core (rag+tools) → api → mcp → shared
- ✅ Evita separação desnecessária que aumentaria imports
- ✅ `core/rag` orquestra tudo (Agent Mode, Tool Mode, Web Search)
- ✅ Suporta escalabilidade a 50+ engenheiros

### 2. Config Validation (Fail-Fast Inteligente)

**Decisão:** Fail-fast apenas para campos CRÍTICOS, defaults sensatos para OPCIONAIS

- ✅ CRÍTICOS (sem defaults): DATABASE_URL, JWT_SECRET (>= 32 chars)
- ✅ OPCIONAIS (com defaults): SERVER_PORT=3000, LOG_LEVEL=info
- ✅ Validation no startup previne erros silenciosos em runtime
- ✅ .env.example como template

### 3. Logging Robusto (slog + JSON)

**Decisão:** slog com output JSON + mudança de log level em runtime

- ✅ JSON estruturado (parseável para observabilidade)
- ✅ Source location (file:line) automático
- ✅ PUT /debug/loglevel?level=debug (sem reiniciar servidor)
- ✅ Essencial para debugging em produção

### 4. Memory Isolation (Per-User Namespaces)

**Decisão:** Per-user isolation em LanceDB + metadata em PostgreSQL

- ✅ LanceDB: namespace separado por user_id
- ✅ PostgreSQL: memory_metadata tabela com índices user_id
- ✅ Query forcing: `WHERE user_id = ?` em todas as queries
- ✅ Segurança e performance garantidas

### 5. RAG Orchestrator Unificado

**Decisão:** Um orchestrator que suporte ambos Agent Mode e Tool Mode

- ✅ Agent Mode: search → rerank → web search → LLM → response
- ✅ Tool Mode: search → rerank (sem LLM)
- ✅ Shared pipeline (search, rerank)
- ✅ Simpler code, menos duplicação

### 6. Rodmap: 5 Fases vs 3

**Decisão:** 5 fases com Stabilization como fase dedicada (Phase 2)

- ✅ Phase 1: Foundation (8-10w) - MVP com arquitetura tier-based
- ✅ Phase 2: Stabilization (3-4w) - Testes, bugfixes, feedback
- ✅ Phase 3: Features (6-8w) - Agent integrations + Tool Mode completo
- ✅ Phase 4: Performance (4-6w) - Caching, rate limiting, monitoring
- ✅ Phase 5: Ecosystem (ongoing) - PAL registry, community

### 7. System Tray (Windows)

**Decisão:** Deixar para Phase 2+ (não MVP)

- ✅ MVP: CLI + Dashboard suficientes
- ✅ System Tray em Phase 4 (quando performance + polish)
- ✅ Reduce MVP scope, focus on core features

### 8. Dashboard com Analytics

**Decisão:** Não é "modo", é interface de configuração sempre ativa + analytics

- ✅ Real-time memory usage (vectors indexed, size in GB)
- ✅ Query performance (latency p50/p95/p99)
- ✅ Tool execution stats (websearch success rate, errors)
- ✅ API usage (requests/min, Agent vs Tool mode split)
- ✅ System health (CPU, memory, DB connections)

### 9. CI/CD Multi-Stage

**Decisão:** lint → test → build → publish (como Vectora)

- ✅ Lint: golangci-lint, gofmt, go vet
- ✅ Test: go test -race -cover + Codecov
- ✅ Build: multi-platform (linux, macos, windows)
- ✅ Publish: npm, PyPI, Docker Hub, GitHub Releases

### 10. Docs: Hugo + Hextra

**Decisão:** Não Markdown plano, usar Hugo + Hextra theme

- ✅ Structured (content/, static/, themes/)
- ✅ Searchable (built-in search)
- ✅ Multilingual (en/, pt-br/)
- ✅ Open-source friendly (não SaaS)

---

## Estrutura do Monorepo

### `vectora/`

**URL:** `github.com/vectora/vectora`

Produto principal para uso local:

- Backend Go (tier-based)
- Frontend React + Vite
- CLI (Cobra)
- Docker Compose

### `vectora-asset-library/`

**URL:** `github.com/vectora/vectora-asset-library`

Registry público de datasets e assets da comunidade:

- Datasets estruturados (vectors.lance + metadata.json)
- Contributing guide
- Validação automática (CI/CD)

**API:** `https://registry.vectora.ai/api/v1/datasets`

### `vectora-integrations/`

**URL:** `github.com/vectora/vectora-integrations`

Monorepo Turborepo com todos os SDKs e adaptadores:

**Packages (NPM):**

- `@vectora/shared` - shared types, auth, HTTP client
- `@vectora/sdk-claude-code` - Claude Code integration (MCP)
- `@vectora/sdk-openai` - OpenAI integration (REST)
- `@vectora/sdk-chatgpt` - ChatGPT plugin
- `@vectora/sdk-gemini-cli` - Gemini CLI (REST)
- `@vectora/sdk-vscode` - VSCode extension
- `@vectora/sdk-hermes` - Hermes agent (REST)
- `@vectora/sdk-codex` - Codex integration (REST)
- `@vectora/sdk-openclaw` - OpenClaw integration (REST)
- `@vectora/template` - custom agent template

### `vectora-website/`

**URL:** `github.com/vectora/vectora-website`

Site público + documentação completa:

- Home page (vectora.ai)
- Getting started guides (local, Docker, VPS)
- API documentation (auto-gen from OpenAPI)
- Integration guides (para cada SDK)
- Architecture deep-dive
- Contributing guide
- Blog (future)

**Tech:** Hugo + Hextra theme (multilingual)
---

## Matriz de Dependências

```
vectora-website
  ├─ Documentação do vectora (links, setup guides)
  ├─ Guias de integração (links para vectora-integrations)
  └─ Links para PAL registry (vectora-asset-library)

vectora-integrations (@vectora/*)
  ├─ Depende de @vectora/shared (types, auth, http client)
  ├─ Usa Vectora Backend API (vectora/backend)
  └─ Documentação em vectora-website

vectora (Frontend + Backend + CLI)
  ├─ Backend expõe REST API + MCP protocol
  ├─ Frontend consome Backend API
  ├─ CLI interage com Backend
  ├─ PAL Registry client (busca datasets)
  └─ Documentado em vectora-website

vectora-asset-library
  └─ Host público para datasets (acessado por Vectora)
```

---

## CI/CD Strategy por Repositório

### vectora

- Lint: golangci-lint (backend), eslint (frontend)
- Test: go test (backend), jest (frontend)
- Build: multi-platform binaries, Docker image
- Publish: GitHub Releases, Docker Hub, npm (package manager)

### vectora-integrations (Turborepo)

- Lint: eslint, prettier
- Test: jest
- Build: turbo build (all packages)
- Publish: pnpm publish (all @vectora/\* packages to npm)

### vectora-website

- Build: hugo build
- Deploy: Netlify / GitHub Pages / Fly.io
- Auto-deploy on merge to main

### vectora-asset-library

- Validate: dataset structure, checksum validation
- Auto-index: generate registry index.json
- Publish: datasets available on registry.vectora.ai

---

## Decisões Ainda em Aberto

1. **Search Provider:** SerpAPI vs Google Search API? (SerpAPI mais simples, escolher in Phase 3)
2. **Cache Backend:** Redis vs in-memory? (in-memory MVP, Redis Phase 4)
3. **Monitoring Stack:** Prometheus + Sentry? (sim, Phase 4)
4. **Database:** PostgreSQL default ou SQLite default? (PostgreSQL default, SQLite fallback)
