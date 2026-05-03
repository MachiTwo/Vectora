---
title: "Prompts e Templates no LangChain"
slug: "langchain/prompts"
description: "Construção e gerenciamento de prompts estruturados"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "prompts", "templates", "structured", "variables"]
---

{{< lang-toggle >}}

Prompts estruturados tornam fácil criar, gerenciar e compor instruções para LLMs.

## PromptTemplate Básico

Templates com variáveis:

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic", "tone"],
    template="""Write a {tone} essay about {topic}.
    
    Make sure it is informative and engaging."""
)

prompt = template.format(
    topic="Artificial Intelligence",
    tone="technical"
)
```

## ChatPromptTemplate

Para conversas multi-mensagem:

```python
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Python expert."),
    ("human", "I need help with {problem}"),
    ("ai", "I'd be happy to help! Let me understand better."),
    ("human", "{follow_up}")
])

prompt = template.format(
    problem="async programming",
    follow_up="How do I handle errors?"
)
```

## Few-shot Prompting

Exemplos para melhor performance:

```python
from langchain.prompts import FewShotPromptTemplate

examples = [
    {
        "input": "What is 2 + 2?",
        "output": "4"
    },
    {
        "input": "What is 5 + 3?",
        "output": "8"
    }
]

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate(
        input_variables=["input", "output"],
        template="Q: {input}\nA: {output}"
    ),
    suffix="Q: {question}\nA:",
    input_variables=["question"]
)
```

## Dynamic Prompts

Prompts que mudam baseado em contexto:

```python
from langchain.prompts import PromptTemplate

def get_prompt(language: str):
    if language == "python":
        return PromptTemplate(
            template="Write Python code for: {task}",
            input_variables=["task"]
        )
    else:
        return PromptTemplate(
            template="Write {language} code for: {task}",
            input_variables=["language", "task"]
        )
```

## Message Placeholders

Usar conteúdo dinâmico em messages:

```python
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])
```

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| PromptTemplate | Prompt Documentation | [https://docs.langchain.com/oss/python/langchain/prompts](https://docs.langchain.com/oss/python/langchain/prompts) |
| ChatPromptTemplate | Chat Prompts | [https://docs.langchain.com/oss/python/langchain/prompts/chat_prompt_template](https://docs.langchain.com/oss/python/langchain/prompts/chat_prompt_template) |
| Few-shot | Few-shot Learning | [https://docs.langchain.com/oss/python/langchain/prompts/few_shot_examples](https://docs.langchain.com/oss/python/langchain/prompts/few_shot_examples) |
| Prompt Engineering | Best Practices | [https://docs.langchain.com/oss/python/langchain/guides/prompt_engineering](https://docs.langchain.com/oss/python/langchain/guides/prompt_engineering) |
| LCEL | Expression Language | [https://docs.langchain.com/oss/python/langchain/expression_language](https://docs.langchain.com/oss/python/langchain/expression_language) |
