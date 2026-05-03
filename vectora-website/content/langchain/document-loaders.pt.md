---
title: "Document Loaders no LangChain"
slug: "langchain/document-loaders"
description: "Carregar dados de diferentes fontes"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "loaders", "documents", "pdf", "csv", "web"]
---

{{< lang-toggle >}}

Document Loaders carregam dados de várias fontes e convertem em documents.

## File Loaders

### PDF Loader

```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
documents = loader.load()

# documents = [Document(page_content="...", metadata={"page": 0})]
```

### CSV Loader

```python
from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="data.csv")
documents = loader.load()
```

### Text Loader

```python
from langchain.document_loaders import TextLoader

loader = TextLoader("file.txt")
documents = loader.load()
```

## Web Loaders

### Web URLs

```python
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    web_paths=["https://example.com/page"]
)
documents = loader.load()
```

### YouTube

```python
from langchain.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=...",
    add_video_info=True
)
documents = loader.load()
```

## API Loaders

### GitHub

```python
from langchain.document_loaders import GitHubFileLoader

loader = GitHubFileLoader(
    repo="langchain-ai/langchain",
    branch="master",
    file_path="docs/README.md"
)
documents = loader.load()
```

### Notion

```python
from langchain.document_loaders import NotionDatabaseLoader

loader = NotionDatabaseLoader(
    notion_token="your_token",
    database_id="your_database_id"
)
documents = loader.load()
```

## Generic Loader

Para cualquier arquivo:

```python
from langchain.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("any_file.pptx")
documents = loader.load()
```

## Processing Documents

Após carregamento:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("document.pdf")
documents = loader.load()

# Split en chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)
```

## Metadata

Documentos incluem metadata:

```python
for doc in documents:
    print(doc.page_content)
    print(doc.metadata)
    # {"source": "document.pdf", "page": 0}
```

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| Document Loaders | Loader Reference | [https://docs.langchain.com/oss/python/langchain/document_loaders](https://docs.langchain.com/oss/python/langchain/document_loaders) |
| PDF Loader | PyPDF Documentation | [https://docs.langchain.com/oss/python/langchain/document_loaders/pdf](https://docs.langchain.com/oss/python/langchain/document_loaders/pdf) |
| Web Loaders | URL Loading | [https://docs.langchain.com/oss/python/langchain/document_loaders/web](https://docs.langchain.com/oss/python/langchain/document_loaders/web) |
| Text Splitters | Chunking Documents | [https://docs.langchain.com/oss/python/langchain/text_splitters](https://docs.langchain.com/oss/python/langchain/text_splitters) |
| Unstructured | Unstructured Loader | [https://unstructured.io/](https://unstructured.io/) |
