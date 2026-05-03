# Vectora: Agent Complete Local-First para Engenharia de Software

## O que é o Vectora

Vectora é um **Agent Complete** local-first projetado especificamente para engenharia de software. Ele opera como um agente autônomo acessível via MCP (Model Context Protocol) e ACP (Agent Client Protocol), permitindo integração com IDEs (Claude Code, Cursor, JetBrains) e orquestração por sistemas multi-agent (Paperclip). 

Vectora combine três capacidades principais:
1. **Contexto Governado** - Recuperação de conhecimento vetorizado via LanceDB + Voyage
2. **Decisão Tática** - Pré-processamento via VCR (XLM-RoBERTa-small + LoRA fine-tuning)
3. **Execução Confiável** - Framework LangChain + LangGraph para orquestração de agentes

Diferentemente de sub-agentes, Vectora funciona como um agente principal que coordena suas próprias decisões e pode ser acionado por outros agentes via protocolo padrão.

## Objetivo

O objetivo do Vectora é eliminar alucinações e vazamentos de dados em operações de engenharia de software, fornecendo uma infraestrutura de decisão fundamentada em contexto real e governada por políticas locais. Através de embeddings precisos (Voyage), pré-pensamento especializado (VCR) e orquestração ativa (LangChain + Deep Agents), o Vectora transforma LLMs genéricas em agentes capazes de operar em repositórios complexos com precisão e segurança.

---

## O Ecossistema Vectora

### Backend (Python FastAPI)

Camada principal executando em Python via FastAPI. Responsável por:
- APIs REST autenticadas (JWT + RBAC com 5 roles e 15 permissões)
- Autenticação multi-user (local + VPS)
- Roteamento inteligente
- Integração com LangChain/LangGraph para orquestração
- Middleware stack (CORS, rate limiting, security headers)

### Storage Layer

Persistência em três camadas:
- **PostgreSQL** - Dados estruturados (sessões, users, metadata)
- **Redis** - Cache e sessões em tempo real
- **LanceDB** - Vector storage com formato .lance

### AI/Embeddings (Voyage)

Camada de recuperação de contexto:
- **Voyage** para geração de embeddings (prime embedding model)
- **Voyage Reranking** (remote ou local) para refinamento de resultados
- Integração com LanceDB para vector search
- Suporte a reranker-local (Voyage aplicado a arquivos locais vs dados do banco)

### Vectora Cognitive Runtime (VCR)

O pré-processador especializado do sistema:
- Modelo **XLM-RoBERTa-small** como base
- Fine-tuning via **LoRA** em traces reais
- Execução local para validação de contexto
- Aplicação de regras de governança antes da decisão principal

### LangChain Ecosystem

Framework de orquestração:
- **LangChain** - Framework unificado para chains e tools
- **LangGraph** - Stateful agents com decision loops
- **LangSmith** - Observability e tracing em produção
- **Deep Agents** - CLI + TUI para execução

### Integrations (@vectora-integrations Monorepo)

SDKs TypeScript independentes para conectar diferentes agentes:
- **@vectora/sdk-claude-code** - VSCode extension via MCP
- **@vectora/sdk-gemini-cli** - Google Gemini CLI adapter
- **@vectora/sdk-paperclip** - Paperclip agent plugin
- **@vectora/sdk-hermes** - Hermes agent adapter
- **@vectora/shared** - Types, auth, HTTP client compartilhado

### VAL (Vectora Asset Library)

Registry público de datasets vetorizados:
- Repositório GitHub com datasets
- Releases para distribuição via npm/pip
- CLI commands: `vectora val download <dataset-name>`
- Comunidade contribui datasets (docs, code samples, etc)
- Indexação automática via GitHub Actions

### Multi-User & Agent Orchestration

Suporte para deployments escaláveis:
- Autenticação JWT com token generation por user/agent
- VPS deployment com múltiplos usuários
- Integração com Paperclip para orquestração de múltiplos agents
- Buckets públicos e privados por sessão

### Documentation

Base de conhecimento em português (PT-BR):
- Site oficial em Hugo/Markdown
- Guias técnicos completos (65+ docs)
- Arquitetura, patterns, deployment, development
- Asset library guides
- Integrations e SDKs documentation
