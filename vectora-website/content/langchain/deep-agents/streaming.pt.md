---
title: "Respostas com Streaming"
slug: "langchain/deep-agents/streaming"
description: "Resposta em tempo real com streaming"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "streaming", "real-time", "responses"]
---

{{< lang-toggle >}}

Deep Agents suporta streaming nativo para respostas em tempo real, ideal para UIs responsivas e LLMs com respostas longas.

## Streaming Básico

```python
from deepagents import Agent

agent = Agent(name="writer", model="claude-3-opus")

# Streaming via generator
for chunk in agent.stream("Escreva um artigo sobre IA"):
    print(chunk, end="", flush=True)
```

## Streaming com Tools

Streams enquanto executa tools:

```python
agent = Agent(
    tools=[search, summarize],
    stream_tool_calls=True
)

for event in agent.stream_events("Pesquise IA"):
    if event["type"] == "tool_call":
        print(f"[Tool] {event['tool']}: {event['input']}")
    elif event["type"] == "chunk":
        print(f"[Output] {event['text']}", end="", flush=True)
```

## Streaming em FastAPI

Integração com endpoint FastAPI:

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json

app = FastAPI()

@app.post("/agent/stream")
async def stream_agent(request: dict):
    agent = Agent(name="api_agent")

    async def generate():
        for chunk in agent.stream(request["input"]):
            yield json.dumps({"chunk": chunk}) + "\n"

    return StreamingResponse(generate())
```

Cliente:

```javascript
const response = await fetch("/agent/stream", {
  method: "POST",
  body: JSON.stringify({ input: "Pesquise IA" }),
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  const text = decoder.decode(value);
  const { chunk } = JSON.parse(text);
  console.log(chunk);
}
```

## WebSocket Streaming

Para conexões persistentes:

```python
from fastapi import WebSocket

@app.websocket("/ws/agent")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    agent = Agent(name="ws_agent")

    while True:
        data = await websocket.receive_json()
        for chunk in agent.stream(data["input"]):
            await websocket.send_json({"chunk": chunk})
```

## External Linking

| Conceito              | Recurso                 | Link                                                                                                                     |
| --------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Deep Agents Streaming | Streaming Guide         | [https://docs.langchain.com/oss/python/deepagents/streaming](https://docs.langchain.com/oss/python/deepagents/streaming) |
| LangChain Streaming   | Streaming Documentation | [https://docs.langchain.com/oss/python/langchain/](https://docs.langchain.com/oss/python/langchain/)                     |
| Real-time Responses   | Response Streaming      | [https://docs.langchain.com/oss/python/deepagents/](https://docs.langchain.com/oss/python/deepagents/)                   |
| FastAPI Streaming     | FastAPI Streaming       | [https://fastapi.tiangolo.com/advanced/streaming-response/](https://fastapi.tiangolo.com/advanced/streaming-response/)   |
| WebSocket             | WebSocket Support       | [https://fastapi.tiangolo.com/advanced/websockets/](https://fastapi.tiangolo.com/advanced/websockets/)                   |
