---
title: "Output Parsers no LangChain"
slug: "langchain/output-parsers"
description: "Estruturar e validar respostas de LLMs"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "parsing", "output", "structured", "validation"]
---

{{< lang-toggle >}}

Output Parsers convertem strings de LLMs em estruturas de dados Python.

## StringOutputParser

Mais simples - retorna string:

```python
from langchain.output_parsers import StringOutputParser
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatAnthropic

prompt = PromptTemplate.from_template("Translate to French: {text}")
llm = ChatAnthropic()
parser = StringOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"text": "Hello world"})
# "Bonjour le monde"
```

## PydanticOutputParser

Estruturar respostas com validação:

```python
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class Person(BaseModel):
    name: str = Field(description="Person's name")
    age: int = Field(description="Person's age")
    skills: List[str] = Field(description="List of skills")

parser = PydanticOutputParser(pydantic_object=Person)

prompt = PromptTemplate(
    template="Extract person info:\n{format_instructions}\n{text}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser

person = chain.invoke({"text": "John is 30 and knows Python, Go"})
# Person(name="John", age=30, skills=["Python", "Go"])
```

## JSONOutputParser

Parse JSON responses:

```python
from langchain.output_parsers import JSONOutputParser

parser = JSONOutputParser()

prompt = PromptTemplate(
    template="Return as JSON: {query}",
    input_variables=["query"]
)

chain = prompt | llm | parser

result = chain.invoke({"query": "List 3 fruits"})
# {"fruits": ["apple", "banana", "orange"]}
```

## CommaSeparatedListOutputParser

Parse comma-separated lists:

```python
from langchain.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()

prompt = PromptTemplate(
    template="List 5 {topic}: {topic}",
    input_variables=["topic"]
)

chain = prompt | llm | parser

result = chain.invoke({"topic": "programming languages"})
# ["Python", "JavaScript", "Go", "Rust", "Java"]
```

## Custom Parsers

Criar parser customizado:

```python
from langchain.schema import BaseOutputParser

class CustomParser(BaseOutputParser):
    def parse(self, text: str):
        lines = text.strip().split('\n')
        return {
            "title": lines[0],
            "points": lines[1:]
        }

parser = CustomParser()
result = parser.parse("My Title\n- Point 1\n- Point 2")
```

## Error Handling

Retry on parsing errors:

```python
from langchain.output_parsers import OutputFixingParser

parser = PydanticOutputParser(pydantic_object=Person)
fixing_parser = OutputFixingParser.from_llm(
    parser=parser,
    llm=llm
)

# Automatically fixes malformed JSON
```

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| Output Parsers | Parser Reference | [https://docs.langchain.com/oss/python/langchain/output_parsers](https://docs.langchain.com/oss/python/langchain/output_parsers) |
| Pydantic | Data Validation | [https://docs.pydantic.dev/](https://docs.pydantic.dev/) |
| JSON Parser | JSON Parsing | [https://docs.langchain.com/oss/python/langchain/output_parsers/json](https://docs.langchain.com/oss/python/langchain/output_parsers/json) |
| Custom Parsers | Creating Parsers | [https://docs.langchain.com/oss/python/langchain/output_parsers/custom](https://docs.langchain.com/oss/python/langchain/output_parsers/custom) |
| LCEL | Expression Language | [https://docs.langchain.com/oss/python/langchain/expression_language](https://docs.langchain.com/oss/python/langchain/expression_language) |
