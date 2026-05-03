---
title: "Chat Models no LangChain"
slug: "langchain/chat-models"
description: "Integração com LLMs via chat interface"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "chat-models", "llm", "claude", "gpt", "gemini"]
---

{{< lang-toggle >}}

Chat Models são a interface padrão do LangChain para trabalhar com LLMs. Eles seguem um padrão de chat (user/assistant/system messages).

## Provedores Suportados

### Anthropic Claude

Recomendado para máxima performance:

```python
from langchain.chat_models import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3-opus",
    api_key="your_key",
    temperature=0.7,
    max_tokens=2048
)

response = llm.invoke([
    HumanMessage("What is AI?")
])
```

### OpenAI

GPT-4 e GPT-3.5:

```python
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.5
)
```

### Google Gemini

```python
from langchain.chat_models import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-pro"
)
```

## Tipos de Messages

```python
from langchain.schema import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Hello!"),
    AIMessage(content="Hi! How can I help?"),
    HumanMessage(content="Tell me about AI")
]

response = llm.invoke(messages)
```

## Streaming Responses

Respostas em tempo real:

```python
for chunk in llm.stream([HumanMessage("Write a poem")]):
    print(chunk.content, end="", flush=True)
```

## Function Calling

LLMs podem chamar funções:

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search the web",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                }
            }
        }
    }
]

response = llm.invoke(
    [HumanMessage("Search for AI news")],
    tools=tools
)
```

## Batch Processing

Processar múltiplas queries eficientemente:

```python
queries = [
    [HumanMessage("What is AI?")],
    [HumanMessage("What is ML?")],
    [HumanMessage("What is DL?")]
]

responses = llm.batch(queries)
```

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| Chat Models | Chat Model Reference | [https://docs.langchain.com/oss/python/langchain/chat_models](https://docs.langchain.com/oss/python/langchain/chat_models) |
| Claude API | Anthropic Documentation | [https://docs.anthropic.com/](https://docs.anthropic.com/) |
| OpenAI API | OpenAI Chat Completions | [https://platform.openai.com/docs/guides/gpt](https://platform.openai.com/docs/guides/gpt) |
| Gemini API | Google AI Studio | [https://ai.google.dev/docs](https://ai.google.dev/docs) |
| Streaming | Real-time Responses | [https://docs.langchain.com/oss/python/langchain/](https://docs.langchain.com/oss/python/langchain/) |
