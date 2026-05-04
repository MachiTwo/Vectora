---
title: "Estratégias de Memória em Conversas Longas"
slug: "langchain/langgraph/memory-strategies"
description: "Truncate, Delete, Summarize para gerenciar contexto"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "memory", "context", "truncate", "summarize", "conversation"]
---

{{< lang-toggle >}}

Em conversas longas, o contexto cresce indefinidamente. LangGraph oferece **3 estratégias para compactar memória**: Truncate (descartar antigos), Delete (remover seletivo), e Summarize (compactar com resumo).

## Problema: Context Explosion

```
Turno 1:  User: "Oi"                          → Tokens: 50
Turno 2:  Full history + User: "Como vai?"    → Tokens: 100
Turno 3:  Full history + User: "O que é IA?"  → Tokens: 200
Turno 4:  Full history + User: "..."           → Tokens: 500
...
Turno 50: Full history + User: "..."           → Tokens: 50,000+ ❌
```

**Impacto:**

- Custo exponencial
- Latência aumenta
- Qualidade degrada

## Estratégia 1: Truncate (Descartar Antigos)

Manter apenas os últimos N mensagens:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class ConversationState(TypedDict):
    messages: list
    user_id: str

def truncate_messages(messages: list, max_messages: int = 10):
    """Manter apenas últimas N mensagens"""
    if len(messages) > max_messages:
        return messages[-max_messages:]
    return messages

def chat_node(state):
    # Truncar ANTES de chamar LLM
    truncated = truncate_messages(state["messages"], max_messages=10)

    response = llm.invoke(truncated)

    # Adicionar resposta E DEPOIS truncar para storage
    updated = state["messages"] + [{"role": "assistant", "content": response}]
    truncated_for_storage = truncate_messages(updated, max_messages=50)

    return {"messages": truncated_for_storage}

graph = StateGraph(ConversationState)
graph.add_node("chat", chat_node)
graph.add_edge(START, "chat")
graph.add_edge("chat", END)

app = graph.compile()
```

**Vantagens:**

- ✅ Simples
- ✅ Previsível
- ✅ Sem custo adicional

**Limitações:**

- ❌ Perde contexto antigo
- ❌ Sem conhecimento de longo prazo

**Quando usar:** Conversas curtas (< 50 turnos), chats de suporte, debugging.

## Estratégia 2: Delete (Remover Seletivamente)

Deletar mensagens específicas baseado em importância:

```python
def classify_importance(message: str, llm) -> str:
    """Classificar se mensagem é importante"""

    analysis = llm.invoke(f"""
    É importante manter esta mensagem para contexto futuro?
    Mensagem: {message}

    Responda apenas: "importante", "contextual", ou "trivial"
    """)

    return analysis.lower().strip()

def smart_delete(messages: list, llm, max_messages: int = 30):
    """Deletar mensagens triviais se necessário"""

    if len(messages) <= max_messages:
        return messages

    # Classificar cada mensagem
    classified = []
    for msg in messages:
        importance = classify_importance(msg["content"], llm)
        classified.append((msg, importance))

    # Deletar triviais primeiro
    important = [msg for msg, imp in classified if imp != "trivial"]
    contextual = [msg for msg, imp in classified if imp == "contextual"]
    trivial = [msg for msg, imp in classified if imp == "trivial"]

    # Manter importante + alguns contextual
    kept = important + contextual[:max(0, max_messages - len(important))]

    return kept[:max_messages]

def chat_node(state):
    # Aplicar seleção inteligente
    messages = smart_delete(state["messages"], llm, max_messages=30)

    response = llm.invoke(messages)

    return {"messages": state["messages"] + [{"role": "assistant", "content": response}]}
```

**Vantagens:**

- ✅ Retém contexto importante
- ✅ Remove ruído

**Limitações:**

- ❌ Custo de classificação (extra LLM call)
- ❌ Pode deletar mensagens valiosas por erro

**Quando usar:** Conversas com padrões de importância, análise multi-turno, pesquisa.

## Estratégia 3: Summarize (Compactar com Resumo)

Substituir mensagens antigas com resumos:

```python
import json
from typing import TypedDict

class ConversationState(TypedDict):
    messages: list
    summary: str
    user_id: str

def summarize_messages(messages: list, llm, num_to_summarize: int = 5):
    """Resumir N mensagens antigos em texto coerente"""

    if len(messages) < num_to_summarize:
        return None

    # Pegar primeiras N mensagens
    to_summarize = messages[:num_to_summarize]

    summary = llm.invoke(f"""
    Resuma concisamente esta conversação inicial (máx 100 tokens):

    {json.dumps([m['content'] for m in to_summarize], ensure_ascii=False)}

    Foque em: tópico principal, decisões tomadas, contexto necessário.
    """)

    return summary

def compact_with_summary(state):
    """Compactar histórico com resumo"""

    messages = state["messages"]
    existing_summary = state.get("summary", "")

    # Se > 30 mensagens, resumir primeiras 10
    if len(messages) > 30:
        new_summary = summarize_messages(messages[:10], llm, num_to_summarize=10)

        # Manter resumo anterior + novo resumo + últimas 20 mensagens
        compacted = [
            {"role": "system", "content": f"Resumo anterior:\n{existing_summary}\n\nResumo novo:\n{new_summary}"},
            *messages[10:]
        ]

        return {
            "messages": compacted[-20:],  # Manter últimas 20
            "summary": f"{existing_summary}\n{new_summary}"
        }

    return state

def chat_node(state):
    # Primeiro compactar se necessário
    state = compact_with_summary(state)

    response = llm.invoke(state["messages"])

    return {"messages": state["messages"] + [{"role": "assistant", "content": response}]}
```

**Implementação Avançada com LangGraph:**

```python
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage

class ConversationState(TypedDict):
    messages: list[BaseMessage]
    summary: str
    message_count: int

def summarize_node(state):
    """Nó que resume e compacta histórico"""

    if state["message_count"] < 20:
        return state

    # Resumir tudo em 1 summary
    full_conversation = "\n".join([m.content for m in state["messages"]])

    summary = llm.invoke(f"""
    Resuma tudo que aconteceu até agora:

    {full_conversation}
    """)

    # Manter apenas últimas 5 mensagens + summary
    return {
        "messages": [
            SystemMessage(content=f"Contexto anterior: {summary}"),
            *state["messages"][-5:]
        ],
        "summary": summary,
        "message_count": 5
    }

def chat_node(state):
    response = llm.invoke(state["messages"])

    return {
        "messages": state["messages"] + [response],
        "message_count": state["message_count"] + 1
    }

graph = StateGraph(ConversationState)
graph.add_node("summarize", summarize_node)
graph.add_node("chat", chat_node)

graph.add_edge(START, "chat")
graph.add_conditional_edges(
    "chat",
    lambda state: "summarize" if state["message_count"] > 20 else "chat",
    {"summarize": "summarize", "chat": "chat"}
)
graph.add_edge("summarize", "chat")

app = graph.compile()
```

**Vantagens:**

- ✅ Preserva contexto longo
- ✅ Escalável
- ✅ Reduz tokens efetivamente

**Limitações:**

- ❌ Extra custo de resumo
- ❌ Pode perder detalhes
- ❌ Mais complexo

**Quando usar:** Conversas muito longas (100+ turnos), customer success, pesquisa contínua.

## Comparação: Truncate vs Delete vs Summarize

| Aspecto                 | Truncate         | Delete         | Summarize        |
| ----------------------- | ---------------- | -------------- | ---------------- |
| **Complexidade**        | Baixa            | Média          | Alta             |
| **Custo**               | Mínimo           | Médio (LLM)    | Alto (LLM)       |
| **Contexto retido**     | Recente          | Importante     | Completo         |
| **Melhor para**         | Conversas curtas | Padrões claros | Conversas longas |
| **Perda de informação** | Alta             | Média          | Baixa            |

## Padrão Híbrido

Combinar estratégias:

```python
def hybrid_memory_strategy(state):
    """
    1. Truncate: Manter últimas 15 mensagens
    2. Delete: Remover triviais se > 20
    3. Summarize: Compactar se > 50
    """

    messages = state["messages"]

    # Nível 1: Sempre truncar para LLM (últimas 15)
    llm_input = messages[-15:]

    # Nível 2: Storage inteligente (< 50)
    if len(messages) > 50:
        # Nivel 3: Summarize
        old_summary = state.get("summary", "")
        new_summary = summarize_messages(messages[:25], llm)
        storage = [
            {"role": "system", "content": f"Contexto: {old_summary} {new_summary}"},
            *messages[25:]
        ]
    elif len(messages) > 20:
        # Nivel 2: Delete
        storage = smart_delete(messages, llm, max_messages=40)
    else:
        # Nivel 1: Full history
        storage = messages

    return {
        "llm_input_messages": llm_input,
        "storage_messages": storage
    }
```

## Integração com Vectora

```python
class VectoraMemoryAgent:
    def __init__(self, vectora_client, strategy="summarize"):
        self.vectora = vectora_client
        self.strategy = strategy

    async def process_message(self, user_id: str, message: str, state):
        # Aplicar estratégia de memória
        if self.strategy == "truncate":
            state["messages"] = state["messages"][-10:]
        elif self.strategy == "summarize":
            if len(state["messages"]) > 20:
                state = await self._summarize_state(state)

        # Executar com VCR
        analysis = await self.vectora.vcr.analyze(message)

        # Busca com contexto reduzido
        results = await self.vectora.search(
            message,
            context_messages=state["messages"][-5:]
        )

        return results

    async def _summarize_state(self, state):
        summary = await self.vectora.summarize(
            state["messages"]
        )
        state["summary"] = summary
        state["messages"] = state["messages"][-5:]
        return state
```

## External Linking

| Conceito         | Recurso          | Link                                                                                                                                                             |
| ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Context Windows  | Token Limits     | [https://platform.openai.com/docs/guides/tokens](https://platform.openai.com/docs/guides/tokens)                                                                 |
| Message Trimming | LangChain Guide  | [https://python.langchain.com/docs/modules/memory/](https://python.langchain.com/docs/modules/memory/)                                                           |
| Summarization    | LLM Summarize    | [https://python.langchain.com/docs/modules/chains/additional/summarize](https://python.langchain.com/docs/modules/chains/additional/summarize)                   |
| LangGraph State  | State Management | [https://langchain-ai.github.io/langgraph/concepts/low_level_concepts/#state](https://langchain-ai.github.io/langgraph/concepts/low_level_concepts/#state)       |
| Token Counting   | Exact Counts     | [https://js.langchain.com/docs/modules/model_io/models/llm/token_usage_tracking](https://js.langchain.com/docs/modules/model_io/models/llm/token_usage_tracking) |
