---
title: "Embeddings e Vector Stores no LangChain"
slug: "langchain/embeddings"
description: "Transformar texto em vetores e gerenciar vector stores"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "embeddings", "vectors", "voyage", "openai"]
---

{{< lang-toggle >}}

Embeddings convertem texto em vetores numéricos para busca semântica.

## Embedding Models

### Voyage Embeddings

Recomendado para melhor qualidade:

```python
from langchain.embeddings import VoyageEmbeddings

embeddings = VoyageEmbeddings(
    voyage_api_key="your_key",
    model="voyage-large"
)

# Embed text
vector = embeddings.embed_query("What is AI?")
# [0.123, -0.456, ...]

# Embed documents
vectors = embeddings.embed_documents([
    "First document",
    "Second document"
])
```

### OpenAI Embeddings

```python
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector = embeddings.embed_query("Your text here")
```

### LanceDB (Local)

Embeddings locais:

```python
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vector = embeddings.embed_query("Text to embed")
```

## Vector Stores

### LanceDB Vector Store

Local, embedded:

```python
from langchain.vectorstores import LanceDB
from langchain.document_loaders import TextLoader

# Load documents
loader = TextLoader("document.txt")
documents = loader.load()

# Create vector store
vectorstore = LanceDB(
    embedding=embeddings,
    table_name="documents"
)

# Add documents
vectorstore.add_documents(documents)

# Search
results = vectorstore.similarity_search(
    "What is AI?",
    k=5
)
```

### Pinecone

Cloud-hosted:

```python
from langchain.vectorstores import Pinecone
import pinecone

pinecone.init(api_key="key", environment="gcp-starter")

vectorstore = Pinecone.from_documents(
    documents,
    embeddings,
    index_name="vectora"
)

# Search
results = vectorstore.similarity_search("query")
```

### Chroma

Lightweight:

```python
from langchain.vectorstores import Chroma

vectorstore = Chroma.from_documents(
    documents,
    embeddings
)

results = vectorstore.similarity_search("query")
```

## Similarity Search with Score

Retornar também a relevância:

```python
results = vectorstore.similarity_search_with_score(
    "What is machine learning?",
    k=5
)

for doc, score in results:
    print(f"Score: {score}")
    print(f"Content: {doc.page_content}")
```

## MMR Search

Maximum Marginal Relevance (evita duplicatas):

```python
results = vectorstore.max_marginal_relevance_search(
    "query",
    k=5,
    fetch_k=20  # Fetch more then rerank
)
```

## Metadata Filtering

Buscar com filtros:

```python
results = vectorstore.similarity_search(
    "query",
    k=5,
    filter={"source": "document.pdf", "page": 0}
)
```

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| Embeddings | Embedding Models | [https://docs.langchain.com/oss/python/langchain/embeddings](https://docs.langchain.com/oss/python/langchain/embeddings) |
| Voyage Embeddings | Voyage AI Docs | [https://docs.voyage.ai/](https://docs.voyage.ai/) |
| Vector Stores | Vector Store Reference | [https://docs.langchain.com/oss/python/langchain/vectorstores](https://docs.langchain.com/oss/python/langchain/vectorstores) |
| LanceDB | LanceDB Documentation | [https://lancedb.com/](https://lancedb.com/) |
| Pinecone | Pinecone Vector DB | [https://www.pinecone.io/](https://www.pinecone.io/) |
