---
title: "Error Handling e Recovery no LangGraph"
slug: "langchain/langgraph/error-handling"
description: "Tratamento de erros, retries e recuperação de falhas"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "error-handling", "recovery", "retries", "resilience"]
---

{{< lang-toggle >}}

Agentes falham. Tools podem timeout, APIs podem falhar, LLMs podem dar respostas inválidas. LangGraph fornece mecanismos para lidar com isso graciosamente.

## Estratégias de Retry

### Exponential Backoff

Aguarde mais tempo a cada retry:

```python
def execute_with_retry(fn, max_retries=3):
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as e:
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            time.sleep(wait_time)
            if attempt == max_retries - 1:
                raise
```

### Circuit Breaker

Pare de tentar se muitas falhas ocorrem:

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5):
        self.failures = 0
        self.threshold = failure_threshold
        self.open = False

    def execute(self, fn):
        if self.open:
            raise Exception("Circuit breaker is open")

        try:
            result = fn()
            self.failures = 0
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.threshold:
                self.open = True
            raise
```

## Error Recovery em Agentes

### Fallback Tools

Se ferramenta falha, use alternativa:

```python
def tools_node(state: State) -> State:
    try:
        result = primary_tool.invoke(input)
    except Exception:
        result = fallback_tool.invoke(input)

    return {"messages": [..., ToolMessage(result)]}
```

### User Escalation

Se erro crítico, peça ajuda:

```python
def should_escalate(error: Exception) -> bool:
    critical_errors = [TimeoutError, ConnectionError]
    return any(isinstance(error, e) for e in critical_errors)

if should_escalate(last_error):
    return "human_approval"
```

### State Rollback

Reverter ao estado anterior se passo falhar:

```python
previous_state = state.copy()

try:
    new_state = process(state)
except Exception:
    return previous_state  # Rollback
```

## Logging e Debugging

```python
import logging

logger = logging.getLogger(__name__)

def agent_node(state: State) -> State:
    logger.info(f"Agent processing, iteration: {state['iterations']}")

    try:
        response = llm.invoke(state["messages"])
        logger.debug(f"LLM response: {response}")
        return {"messages": [...]}
    except Exception as e:
        logger.error(f"Agent failed: {e}", exc_info=True)
        raise
```

## External Linking

| Conceito            | Recurso                   | Link                                                                                                                             |
| ------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Error Handling      | Error Handling Guide      | [https://docs.langchain.com/oss/python/langgraph/how-tos/](https://docs.langchain.com/oss/python/langgraph/how-tos/)             |
| Exponential Backoff | Retry Strategy            | [https://docs.aws.amazon.com/general/latest/gr/api-retries.html](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) |
| State Recovery      | Managing State            | [https://reference.langchain.com/python/langgraph](https://reference.langchain.com/python/langgraph)                             |
| LangChain Errors    | Error Types               | [https://docs.langchain.com/oss/python/langchain/](https://docs.langchain.com/oss/python/langchain/)                             |
| Exception Handling  | Python Exception Handling | [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)                                 |
