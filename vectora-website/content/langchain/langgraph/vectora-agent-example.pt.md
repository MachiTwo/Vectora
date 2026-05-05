---
title: "Exemplo: Agente Vectora com LangGraph"
slug: "langchain/langgraph/vectora-agent-example"
description: "Implementação prática de um agente Vectora usando LangGraph"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "vectora", "agent", "example", "tutorial"]
---

{{< lang-toggle >}}

Exemplo completo de um agente Vectora que usa LangGraph para orquestração, Voyage AI para embeddings e VCR para pré-pensamento.

## Arquitetura

```text
User Query
    ↓
[VCR Pre-thinking]  ← Análise contextual
    ↓
[LangGraph Agent Loop]
├─ [LLM Reasoning] + Vectora Search
├─ [Tool Selection]
├─ [Execution]
└─ [Output Formatting]
    ↓
Response
```

## Implementação

```python
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import ChatAnthropic
from typing import TypedDict, Annotated
import anthropic

# Estado do agente
class AgentState(TypedDict):
    messages: list
    vectora_context: str
    current_tool: str

# Conectar ao Vectora MCP
vectora_client = anthropic.Anthropic(
    api_key="your_api_key"
)

# 1. VCR Pre-thinking
def vcr_prethink(state: AgentState) -> AgentState:
    """Usar VCR para analisar intenção e enriquecer contexto"""
    query = state["messages"][-1].content

    # Análise de intenção
    analysis = vectora_client.messages.create(
        model="claude-haiku-4-5-20251001",
        messages=[{
            "role": "user",
            "content": f"Analise a intenção desta query: {query}"
        }],
        max_tokens=500
    )

    return {
        **state,
        "vectora_context": analysis.content[0].text
    }

# 2. LLM Node
def agent_node(state: AgentState) -> AgentState:
    llm = ChatAnthropic(model="claude-sonnet-4-6")

    response = llm.invoke(
        state["messages"],
        tools=[search_tool, calculate_tool]
    )

    return {
        **state,
        "messages": state["messages"] + [response]
    }

# 3. Tools Node
def tools_node(state: AgentState) -> AgentState:
    messages = state["messages"]
    last_msg = messages[-1]

    if last_msg.tool_calls:
        for tool_call in last_msg.tool_calls:
            if tool_call.name == "search":
                result = vectora_search(tool_call.args["query"])
            else:
                result = execute_tool(tool_call)

            messages.append(ToolMessage(result))

    return {"messages": messages}

# 4. Construir grafo
graph = StateGraph(AgentState)
graph.add_node("vcr", vcr_prethink)
graph.add_node("agent", agent_node)
graph.add_node("tools", tools_node)

graph.add_edge(START, "vcr")
graph.add_edge("vcr", "agent")
graph.add_conditional_edges(
    "agent",
    lambda x: "tools" if x["messages"][-1].tool_calls else "end"
)
graph.add_edge("tools", "agent")
graph.add_edge("agent", END)

app = graph.compile()

# Usar
result = app.invoke({
    "messages": [HumanMessage("Pesquise IA")],
    "vectora_context": "",
    "current_tool": ""
})
```

## Integração com Vectora MCP

```python
# Via MCP bridge
from vectora import MCP

vectora_mcp = MCP(
    uri="http://localhost:8000",
    token="vectora_token"
)

# Usar dentro do agent
def search_tool(query: str):
    results = vectora_mcp.search(
        query=query,
        bucket="knowledge",
        top_k=5
    )
    return results
```

## External Linking

| Conceito           | Recurso                        | Link                                                                                                                         |
| ------------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| LangGraph Tutorial | Official Tutorials             | [https://docs.langchain.com/oss/python/langgraph/tutorials/](https://docs.langchain.com/oss/python/langgraph/tutorials/)     |
| LangChain Tools    | Tool Implementation            | [https://docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools)               |
| Vectora Docs       | Vectora Documentation          | [https://vectora.dev/docs](https://vectora.dev/docs)                                                                         |
| GitHub Examples    | LangGraph Examples             | [https://github.com/langchain-ai/langgraph/tree/main/examples](https://github.com/langchain-ai/langgraph/tree/main/examples) |
| RAG Pattern        | Retrieval Augmented Generation | [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                                                         |
