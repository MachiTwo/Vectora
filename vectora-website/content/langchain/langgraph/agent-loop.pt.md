---
title: "Agent Loop no LangGraph"
slug: "langchain/langgraph/agent-loop"
description: "Implementação do decision loop para agentes"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "agents", "decision-loop", "tool-use", "execution"]
---

{{< lang-toggle >}}

O agent loop é o coração de um agente inteligente. Ele percorre em loop: raciocínio → decisão → ação → observação → repeça.

## O Ciclo Padrão

```
1. LLM Reasoning
   - Observa estado e ferramentas disponíveis
   - Reasoning sobre próximo passo

2. Tool Selection
   - LLM decide qual ferramenta chamar
   - Ou termina se "final_answer"

3. Tool Execution
   - Executa ferramenta selecionada
   - Captura resultado/erro

4. State Update
   - Atualiza estado com resultado
   - Adiciona à message history

5. Loop or Finish
   - Se ferramenta retorna resultado, volta ao passo 1
   - Se "final_answer", termina
```

## Implementação em LangGraph

```python
def agent_node(state: State) -> State:
    messages = state["messages"]
    response = llm.invoke(messages, tools=tools)
    return {"messages": messages + [response]}

def tools_node(state: State) -> State:
    messages = state["messages"]
    last_msg = messages[-1]

    if last_msg.tool_calls:
        for tool_call in last_msg.tool_calls:
            tool_result = execute_tool(tool_call)
            messages.append(ToolMessage(...))

    return {"messages": messages}

def should_continue(state: State) -> str:
    messages = state["messages"]
    last_msg = messages[-1]

    if last_msg.tool_calls:
        return "tools"
    return "end"

graph = StateGraph(State)
graph.add_node("agent", agent_node)
graph.add_node("tools", tools_node)
graph.add_conditional_edges("agent", should_continue)
graph.add_edge("tools", "agent")
graph.set_entry_point("agent")
```

## Padrões Comuns

### Max Iterations

Prevenir loops infinitos:

```python
if state["iterations"] >= max_iterations:
    return "end"
```

### Error Handling

Recuperar de falhas de ferramentas:

```python
try:
    result = tool.invoke(input)
except Exception as e:
    result = f"Error: {str(e)}"
```

### Human Approval

Pausar para aprovação humana:

```python
if requires_approval(action):
    return "human_approval"
```

## External Linking

| Conceito         | Recurso                | Link                                                                                                                                                     |
| ---------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent Pattern    | Agent Design Pattern   | [https://docs.langchain.com/oss/python/langgraph/concepts/agentic_concepts/](https://docs.langchain.com/oss/python/langgraph/concepts/agentic_concepts/) |
| Tool Use         | Tools and Tool Calling | [https://docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools)                                           |
| LangGraph Agents | Agent Tutorials        | [https://docs.langchain.com/oss/python/langgraph/tutorials/](https://docs.langchain.com/oss/python/langgraph/tutorials/)                                 |
| State Updates    | Managing Agent State   | [https://reference.langchain.com/python/langgraph](https://reference.langchain.com/python/langgraph)                                                     |
| Execution        | Running Agents         | [https://docs.langchain.com/oss/python/langgraph/how-tos/](https://docs.langchain.com/oss/python/langgraph/how-tos/)                                     |
