---
title: "Chains no LangChain"
slug: "langchain/chains"
description: "Compor workflows complexos com LCEL"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "chains", "lcel", "composition", "workflows"]
---

{{< lang-toggle >}}

Chains combinam múltiplos componentes em workflows estruturados usando LCEL.

## Basic Chain (Pipe)

Composição simples com `|`:

```python
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatAnthropic
from langchain.output_parsers import StringOutputParser

prompt = PromptTemplate.from_template(
    "Translate to French: {text}"
)
llm = ChatAnthropic()
parser = StringOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"text": "Hello"})
# "Bonjour"
```

## Sequential Chains

Executar chains em sequência:

```python
from langchain.runnables import RunnableSequence

chain1 = prompt1 | llm | parser1
chain2 = prompt2 | llm | parser2

combined = chain1 | chain2

result = combined.invoke(input_data)
```

## Parallel Chains

Executar chains em paralelo:

```python
from langchain.runnables import RunnableParallel

chain_a = prompt_a | llm | parser_a
chain_b = prompt_b | llm | parser_b

parallel = RunnableParallel(
    translation=chain_a,
    summary=chain_b
)

result = parallel.invoke({"text": "..."})
# {"translation": "...", "summary": "..."}
```

## Conditional Chains

Escolher caminho baseado em condição:

```python
from langchain.runnables import RunnableBranch

def route(x):
    if x.get("type") == "technical":
        return "technical"
    return "simple"

chain = RunnableBranch(
    (lambda x: x.get("type") == "technical", technical_chain),
    simple_chain
)
```

## Map & Reduce

Processar múltiplos inputs:

```python
# Map: aplicar a cada item
results = chain.batch(items)

# Custom map
mapped = {"original": chain_a, "modified": chain_b}
result = RunnableParallel(mapped).invoke(data)
```

## Debugging Chains

Ver o que acontece internamente:

```python
chain = prompt | llm | parser

# Ver etapas
print(chain.get_graph().draw_ascii())

# Rastrear execução
for event in chain.stream_events(input_data):
    print(event)
```

## Error Handling in Chains

Tratamento de erros:

```python
from langchain.runnables.utils import AddRunContext

chain = (
    prompt 
    | llm 
    | parser
)

# Com retry
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3))
def run_chain(input_data):
    return chain.invoke(input_data)
```

## Saving Chains

Persistir chains em JSON:

```python
from langchain.schema import runnable

# Export
chain_dict = chain.dict()

# Later: Import
chain = runnable.Runnable.load_config(chain_dict)
```

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| LCEL | LangChain Expression Language | [https://docs.langchain.com/oss/python/langchain/expression_language](https://docs.langchain.com/oss/python/langchain/expression_language) |
| Runnables | Runnable Interface | [https://docs.langchain.com/oss/python/langchain/runnables](https://docs.langchain.com/oss/python/langchain/runnables) |
| Composition | Composing Runnables | [https://docs.langchain.com/oss/python/langchain/runnable/composition](https://docs.langchain.com/oss/python/langchain/runnable/composition) |
| Parallel | Parallel Execution | [https://docs.langchain.com/oss/python/langchain/runnable/parallel](https://docs.langchain.com/oss/python/langchain/runnable/parallel) |
| Branching | Conditional Logic | [https://docs.langchain.com/oss/python/langchain/runnable/branching](https://docs.langchain.com/oss/python/langchain/runnable/branching) |
