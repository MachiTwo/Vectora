---
title: "Estrutura de Aplicação em LangGraph"
slug: "langchain/langgraph/application-structure"
description: "langgraph.json, layout de diretórios, deploy"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "structure", "configuration", "deployment", "project-layout"]
---

{{< lang-toggle >}}

Uma aplicação LangGraph bem estruturada requer: **langgraph.json** para configuração, organização clara de código, e suporte a persistência e deployments.

## Arquivo de Configuração: langgraph.json

```json
{
  "graphs": {
    "agent": {
      "path": "src/agent.py:graph",
      "description": "Main agent with VCR integration"
    },
    "rag_pipeline": {
      "path": "src/rag.py:rag_graph",
      "description": "RAG pipeline with Vectora search"
    }
  },
  "env": ".env.local",
  "python_version": "3.11",
  "dependencies": {
    "langgraph": ">=0.1.0",
    "langchain": ">=0.1.0",
    "langchain-anthropic": ">=0.1.0",
    "pydantic": ">=2.0"
  }
}
```

**Campos obrigatórios:**

| Campo         | Tipo   | Descrição                                                    |
| ------------- | ------ | ------------------------------------------------------------ |
| `graphs`      | object | Mapear nome → path do grafo compilado                        |
| `path`        | string | Caminho ao arquivo Python e nome do grafo `file.py:variable` |
| `description` | string | Descrição breve do grafo                                     |

**Campos opcionais:**

| Campo            | Tipo   | Descrição               |
| ---------------- | ------ | ----------------------- |
| `env`            | string | Arquivo `.env` padrão   |
| `python_version` | string | Versão Python requerida |
| `dependencies`   | object | Dependências explícitas |

## Layout de Diretório Recomendado

```
my_langgraph_app/
├── langgraph.json                 # Configuração
├── pyproject.toml                 # Dependencies
├── .env.example                   # Template de variáveis
├── .env.local                     # Variáveis locais (gitignore)
│
├── src/
│   ├── __init__.py
│   │
│   ├── agent.py                   # Grafo principal
│   ├── rag_pipeline.py            # Grafo RAG
│   ├── vectora_tools.py           # Ferramentas Vectora
│   │
│   ├── nodes/                     # Nós reutilizáveis
│   │   ├── __init__.py
│   │   ├── llm_nodes.py           # LLM reasoning
│   │   ├── tool_nodes.py          # Tool execution
│   │   └── vcr_nodes.py           # VCR analysis
│   │
│   ├── tools/                     # Definições de tools
│   │   ├── __init__.py
│   │   ├── search.py              # Search tool
│   │   ├── retrieve.py            # Retrieve tool
│   │   └── execute.py             # Execute tool
│   │
│   ├── state/                     # State definitions
│   │   ├── __init__.py
│   │   ├── agent_state.py         # AgentState TypedDict
│   │   └── rag_state.py           # RAGState TypedDict
│   │
│   ├── config/                    # Configurações
│   │   ├── __init__.py
│   │   ├── settings.py            # Pydantic settings
│   │   └── constants.py           # Constantes
│   │
│   └── storage/                   # Armazenamento
│       ├── __init__.py
│       └── checkpointer.py        # Setup de persistência
│
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_rag_pipeline.py
│   └── fixtures/                  # Test fixtures
│       ├── mock_vectora.py
│       └── sample_documents.py
│
├── deploy/
│   ├── Dockerfile                 # Container
│   ├── docker-compose.yml         # Local services
│   └── k8s/                       # Kubernetes
│       ├── deployment.yaml
│       ├── service.yaml
│       └── configmap.yaml
│
└── scripts/
    ├── run_local.py               # Executar localmente
    ├── setup_db.py                # Setup persistência
    └── export_graph.py            # Exportar grafo para deploy
```

## Exemplo Completo: Estrutura Prática

### langgraph.json

```json
{
  "graphs": {
    "vectora_agent": {
      "path": "src/agent.py:create_vectora_agent",
      "description": "Agente com VCR e busca Vectora"
    }
  },
  "env": ".env.local",
  "python_version": "3.11",
  "dependencies": {
    "langgraph": ">=0.1.0",
    "langchain-anthropic": ">=0.1.0",
    "pydantic-settings": ">=2.0"
  }
}
```

### src/config/settings.py

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # LLM
    anthropic_api_key: str

    # Vectora
    vectora_api_key: str
    vectora_bucket: str = "knowledge"

    # Storage
    postgres_uri: str = "postgresql://user:pass@localhost/langgraph"

    # App
    debug: bool = False

    class Config:
        env_file = ".env.local"

settings = Settings()
```

### src/state/agent_state.py

```python
from typing import TypedDict, Optional, Annotated
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    # Entrada
    user_input: str
    user_id: str

    # Histórico
    messages: list[BaseMessage]

    # VCR analysis
    intent: str
    entities: list[str]
    confidence: float

    # Search results
    retrieved_docs: list[dict]

    # Saída
    response: str
    metadata: dict
```

### src/nodes/vcr_nodes.py

```python
from src.state.agent_state import AgentState
from src.config.settings import settings

async def vcr_analyze_node(state: AgentState) -> AgentState:
    """Analisar intenção com VCR"""

    from vectora import VectoraClient

    client = VectoraClient(api_key=settings.vectora_api_key)

    analysis = await client.vcr.analyze(state["user_input"])

    return {
        "intent": analysis.intent,
        "entities": analysis.entities,
        "confidence": analysis.confidence,
        **state
    }

async def search_node(state: AgentState) -> AgentState:
    """Buscar documentos no Vectora"""

    from vectora import VectoraClient

    client = VectoraClient(api_key=settings.vectora_api_key)

    results = await client.search(
        query=state["user_input"],
        bucket=settings.vectora_bucket,
        top_k=5
    )

    return {
        "retrieved_docs": results,
        **state
    }
```

### src/agent.py (Grafo Principal)

```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver
from src.state.agent_state import AgentState
from src.nodes.vcr_nodes import vcr_analyze_node, search_node
from src.nodes.llm_nodes import respond_node
from src.config.settings import settings

def create_vectora_agent():
    """Criar grafo do agente Vectora"""

    graph = StateGraph(AgentState)

    # Adicionar nós
    graph.add_node("vcr_analyze", vcr_analyze_node)
    graph.add_node("search", search_node)
    graph.add_node("respond", respond_node)

    # Adicionar edges
    graph.add_edge(START, "vcr_analyze")
    graph.add_edge("vcr_analyze", "search")
    graph.add_edge("search", "respond")
    graph.add_edge("respond", END)

    # Compilar com persistência
    checkpointer = PostgresSaver(
        conn_string=settings.postgres_uri
    )

    return graph.compile(checkpointer=checkpointer)

# Exportar para langgraph.json
graph = create_vectora_agent()
```

## Deploy: Estrutura para Produção

### docker-compose.yml

```yaml
version: "3.8"

services:
  langgraph_app:
    build: .
    ports:
      - "8000:8000"
    environment:
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
      VECTORA_API_KEY: ${VECTORA_API_KEY}
      POSTGRES_URI: postgresql://postgres:password@postgres:5432/langgraph
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: langgraph
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

# Copiar código
COPY src/ src/
COPY langgraph.json .
COPY .env.example .env

# Comando padrão: LangGraph API
CMD ["langgraph", "up"]
```

## Executar Localmente

### scripts/run_local.py

```python
import asyncio
from src.agent import graph
from src.config.settings import settings

async def main():
    # Thread ID para persistência
    thread_id = "dev-session"
    config = {"configurable": {"thread_id": thread_id}}

    # Executar agente
    result = await graph.ainvoke(
        {
            "user_input": "O que é IA?",
            "user_id": "user-123",
            "messages": [],
            "intent": "",
            "entities": [],
            "confidence": 0.0,
            "retrieved_docs": [],
            "response": "",
            "metadata": {}
        },
        config
    )

    print("Response:", result["response"])

if __name__ == "__main__":
    asyncio.run(main())
```

## Estrutura Ideal: Resumo

```
Camada de Configuração (langgraph.json)
           ↓
Camada de Estado (src/state/)
           ↓
Camada de Nós (src/nodes/)
           ↓
Camada de Ferramentas (src/tools/)
           ↓
Camada de Grafo (src/agent.py)
           ↓
Camada de Armazenamento (src/storage/)
           ↓
Camada de Deploy (deploy/)
```

## External Linking

| Conceito          | Recurso           | Link                                                                                                                                                                                               |
| ----------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LangGraph Config  | Configuration     | [https://langchain-ai.github.io/langgraph/how-tos/manage-agent-state/](https://langchain-ai.github.io/langgraph/how-tos/manage-agent-state/)                                                       |
| Project Structure | Best Practices    | [https://python-poetry.org/docs/basic-usage/](https://python-poetry.org/docs/basic-usage/)                                                                                                         |
| Docker Deployment | Container Guide   | [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)                                                                                                                       |
| Kubernetes        | K8s Deploy        | [https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/) |
| Testing           | LangGraph Testing | [https://langchain-ai.github.io/langgraph/how-tos/test-stream/](https://langchain-ai.github.io/langgraph/how-tos/test-stream/)                                                                     |
