---
title: "Persistência em LangGraph"
slug: "langchain/langgraph/persistence"
description: "Threads, checkpoints, snapshots, e estratégias de armazenamento"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "persistence", "threads", "checkpoints", "state", "storage"]
---

{{< lang-toggle >}}

LangGraph oferece **persistência automática de estado** para agentes conversacionais. Através de threads e checkpoints, agentes podem manter histórico, recuperar-se de falhas, e implementar padrões de human-in-the-loop.

## Conceitos Fundamentais

### Thread

Uma **thread é um identificador único** que agrupa todas as execuções relacionadas a uma conversa ou sessão:

```python
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.graph import StateGraph, START, END

# Cada conversa tem uma thread_id
thread_id = "user-123-conversation"

config = {"configurable": {"thread_id": thread_id}}

# Primeira execução salva state
result1 = graph.invoke({"input": "Hello"}, config)

# Segunda execução com mesma thread recupera contexto
result2 = graph.invoke({"input": "What did I say?"}, config)
```

**Benefícios:**

- Múltiplas conversas independentes
- Recuperação após crash
- Auditoria completa
- Human-in-the-loop entre turnos

### Checkpoint

Um **checkpoint é um snapshot do estado** salvo em um ponto no tempo:

```python
# Cada step da execução cria checkpoint
Checkpoint 1: Input recebido → {"input": "...", "step": 0}
Checkpoint 2: LLM respondeu → {"input": "...", "output": "...", "step": 1}
Checkpoint 3: Tool executou → {"input": "...", "tool_result": "...", "step": 2}
```

**Estrutura de um Checkpoint:**

```python
{
    "ts": "2026-05-03T10:00:00Z",      # Timestamp
    "id": "1714741200000-0",            # ID único
    "checkpoint": {
        "input": "User message",
        "state": {...},
        "step": 2
    },
    "metadata": {
        "source": "loop",
        "writes": {"node_name": {...}}
    }
}
```

### Memory Store

Um **armazenamento de threads e checkpoints** (PostgreSQL, Redis, SQLite):

```python
from langgraph.checkpoint.postgres import PostgresSaver

checkpointer = PostgresSaver(
    conn_string="postgresql://user:pass@localhost/langgraph"
)

# Compilar grafo com persistência
app = graph.compile(
    checkpointer=checkpointer,
    interrupt_before=["human_review"]
)
```

## Implementação Prática

### Conversa Multi-Turn com Persistência

```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict

class State(TypedDict):
    messages: list
    user_id: str

def chat_node(state):
    # Recupera histórico (automático via thread_id)
    messages = state["messages"]

    response = llm.invoke(messages)

    # Adiciona resposta ao state
    return {"messages": messages + [{"role": "assistant", "content": response}]}

graph = StateGraph(State)
graph.add_node("chat", chat_node)
graph.add_edge(START, "chat")
graph.add_edge("chat", END)

app = graph.compile(checkpointer=MemorySaver())

# Thread ID mantém conversa persistente
thread_id = "user-456"
config = {"configurable": {"thread_id": thread_id}}

# Turno 1
result1 = app.invoke({
    "messages": [{"role": "user", "content": "Qual é meu nome?"}],
    "user_id": "456"
}, config)

# Turno 2 (histórico recuperado automaticamente)
result2 = app.invoke({
    "messages": [{"role": "user", "content": "Qual era a primeira coisa que perguntei?"}],
    "user_id": "456"
}, config)
```

### Recuperação de Checkpoint

```python
# Listar todos os checkpoints de uma thread
checkpoints = list(app.get_state_history(
    {"configurable": {"thread_id": "user-123"}}
))

for cp in checkpoints:
    print(f"Step {cp.metadata['step']}: {cp.values}")

# Recuperar checkpoint específico
state = app.get_state(
    {"configurable": {"thread_id": "user-123", "checkpoint_id": "1714741200000-0"}}
)

# Continuar de um checkpoint anterior
app.invoke(
    {"input": "Continuar de onde parou"},
    {"configurable": {
        "thread_id": "user-123",
        "checkpoint_id": "1714741200000-0"
    }}
)
```

## Human-in-the-Loop

Pausar execução para intervenção humana:

```python
from langgraph.graph import StateGraph, START, END

class ReviewState(TypedDict):
    query: str
    initial_response: str
    human_feedback: str
    final_response: str

def generate_response(state):
    response = llm.invoke(state["query"])
    return {"initial_response": response}

def review_node(state):
    # Pausa aqui - aguarda human_feedback
    return state

def finalize_response(state):
    if state["human_feedback"] == "approved":
        return {"final_response": state["initial_response"]}
    else:
        response = llm.invoke(
            f"Corrija: {state['human_feedback']}"
        )
        return {"final_response": response}

graph = StateGraph(ReviewState)
graph.add_node("generate", generate_response)
graph.add_node("review", review_node)
graph.add_node("finalize", finalize_response)

graph.add_edge(START, "generate")
graph.add_edge("generate", "review")
graph.add_edge("review", "finalize")
graph.add_edge("finalize", END)

app = graph.compile(
    checkpointer=PostgresSaver(...),
    interrupt_before=["review"]  # Pausa ANTES de review
)

# Executar até interrupção
config = {"configurable": {"thread_id": "task-789"}}
result = app.invoke({"query": "Resuma estes documentos"}, config)
# Estado salvo, aguardando human_feedback

# Humano aprova/rejeita
state = app.get_state(config)
state.values["human_feedback"] = "approved"
app.update_state(config, {"human_feedback": "approved"})

# Continuar execução
result = app.invoke(None, config)  # Continua de "review"
```

## Estratégias de Armazenamento

### In-Memory (Desenvolvimento)

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
# Perdido ao reiniciar, não use em produção
```

### PostgreSQL (Produção)

```python
from langgraph.checkpoint.postgres import PostgresSaver

checkpointer = PostgresSaver(
    conn_string="postgresql://user:pass@localhost:5432/langgraph_db"
)

app = graph.compile(checkpointer=checkpointer)
```

### SQLite (Local)

```python
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver(db_path="./langgraph.db")

app = graph.compile(checkpointer=checkpointer)
```

## Gerenciamento de Threads

### Listar Conversas de um Usuário

```python
# Threads são identificadas por thread_id
# Você pode implementar índice por user_id
user_id = "user-123"

# Buscar no database
threads = db.query(
    "SELECT thread_id FROM threads WHERE user_id = ?",
    (user_id,)
)

for thread_id in threads:
    state = app.get_state(
        {"configurable": {"thread_id": thread_id}}
    )
    print(f"Thread {thread_id}: {state.values['messages'][-1]}")
```

### Limpeza de Threads Antigas

```python
import datetime

# Implementar política de retenção
max_age = datetime.timedelta(days=90)

def cleanup_old_threads(db, max_age):
    cutoff_date = datetime.datetime.now() - max_age

    db.execute(
        "DELETE FROM checkpoints WHERE ts < ?",
        (cutoff_date.isoformat(),)
    )
```

## Integração com Vectora

```python
class VectoraPersistenceAgent:
    def __init__(self, vectora_client, db_uri):
        self.vectora = vectora_client

        from langgraph.checkpoint.postgres import PostgresSaver
        self.checkpointer = PostgresSaver(db_uri)

        self.graph = self._build_graph()
        self.app = self.graph.compile(checkpointer=self.checkpointer)

    def _build_graph(self):
        # Grafo com VCR + persistência
        graph = StateGraph(AgentState)

        graph.add_node("vcr_analyze", self._vcr_analyze)
        graph.add_node("search_knowledge", self._search_knowledge)
        graph.add_node("respond", self._respond)

        graph.add_edge(START, "vcr_analyze")
        graph.add_edge("vcr_analyze", "search_knowledge")
        graph.add_edge("search_knowledge", "respond")
        graph.add_edge("respond", END)

        return graph

    async def chat(self, user_id: str, message: str):
        config = {"configurable": {"thread_id": f"user-{user_id}"}}

        return await self.app.ainvoke({
            "messages": [{"role": "user", "content": message}],
            "user_id": user_id
        }, config)
```

## External Linking

| Conceito              | Recurso            | Link                                                                                                                                                     |
| --------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LangGraph Persistence | Official Guide     | [https://langchain-ai.github.io/langgraph/concepts/persistence/](https://langchain-ai.github.io/langgraph/concepts/persistence/)                         |
| Threads               | Thread Concepts    | [https://langchain-ai.github.io/langgraph/concepts/persistence/#threads](https://langchain-ai.github.io/langgraph/concepts/persistence/#threads)         |
| Checkpointing         | Checkpoint Details | [https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints) |
| Memory Store          | Storage Options    | [https://langchain-ai.github.io/langgraph/reference/checkpointers/](https://langchain-ai.github.io/langgraph/reference/checkpointers/)                   |
| Human-in-the-Loop     | Interrupts Guide   | [https://langchain-ai.github.io/langgraph/how-tos/human-in-the-loop/](https://langchain-ai.github.io/langgraph/how-tos/human-in-the-loop/)               |
