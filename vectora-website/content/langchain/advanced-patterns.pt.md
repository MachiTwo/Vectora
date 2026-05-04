---
title: "Padrões Avançados de Integração"
slug: "langchain/advanced-patterns"
description: "VCR, routing multi-LLM, composição de tools"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "patterns", "advanced", "vcr", "routing", "composition"]
---

{{< lang-toggle >}}

Padrões avançados que combinam LangChain com Vectora, roteamento inteligente de modelos e composição sofisticada de ferramentas.

## Padrão 1: VCR Pre-thinking

Usar **VCR (Vectora Cognitive Runtime)** para análise de contexto antes do agente principal agir.

**Fluxo:**

```
User Query
    ↓
[VCR Pre-thinking]  ← Análise de intenção, contexto, entidades
    ↓
[Query Optimization] ← Reformular query
    ↓
[Tool Selection]    ← Selecionar melhores tools
    ↓
[LLM Agent]         ← Agente principal com contexto rico
    ↓
Response
```

**Implementação:**

```python
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatAnthropic
from langchain.runnables import RunnableSequence

class VCRPrethinkingChain:
    def __init__(self, vectora_client):
        self.vcr = vectora_client.vcr
        self.llm = ChatAnthropic()

    async def analyze_query(self, user_query: str) -> dict:
        """VCR analisa intenção e contexto"""
        analysis = await self.vcr.analyze(user_query)

        return {
            "intent": analysis.intent,
            "entities": analysis.entities,
            "confidence": analysis.confidence,
            "suggested_tools": analysis.suggested_tools,
            "context_summary": analysis.context_summary
        }

    async def optimize_query(self,
                            user_query: str,
                            analysis: dict) -> str:
        """Reformular query para melhor resultado"""

        prompt = PromptTemplate.from_template("""
        Original query: {original}
        Analysis: {analysis}

        Rewrite the query to be more specific and actionable:
        """)

        chain = prompt | self.llm
        optimized = await chain.apredict(
            original=user_query,
            analysis=analysis
        )

        return optimized

    async def invoke(self, user_query: str):
        # 1. VCR Analysis
        analysis = await self.analyze_query(user_query)

        # 2. Query Optimization
        optimized_query = await self.optimize_query(user_query, analysis)

        # 3. Tool Selection (já feito por VCR)
        tools = self.get_tools_by_names(analysis["suggested_tools"])

        # 4. Agent com contexto rico
        response = await self.agent.apredict(
            query=optimized_query,
            tools=tools,
            context=analysis["context_summary"]
        )

        return response

# Usar
vcr_chain = VCRPrethinkingChain(vectora_client)
result = await vcr_chain.invoke("What are the latest AI trends?")
```

## Padrão 2: Multi-LLM Routing

**Rotear para o melhor modelo** baseado na complexidade da tarefa.

```python
from langchain.runnables import RunnableBranch

def classify_complexity(user_query: str) -> str:
    """Classificar complexidade da query"""

    # Heurísticas simples
    keywords_simple = ["hello", "what", "how much"]
    keywords_complex = ["analyze", "compare", "research", "comprehensive"]

    query_lower = user_query.lower()

    if any(k in query_lower for k in keywords_complex):
        return "complex"
    elif any(k in query_lower for k in keywords_simple):
        return "simple"
    else:
        return "medium"

# Models com diferentes custo/performance
models = {
    "simple": ChatAnthropic(model="claude-3-haiku"),    # Fast, cheap
    "medium": ChatAnthropic(model="claude-3-sonnet"),   # Balanced
    "complex": ChatAnthropic(model="claude-3-opus")     # Powerful
}

# Router dinâmico
router = RunnableBranch(
    (lambda x: classify_complexity(x["query"]) == "complex",
     models["complex"]),
    (lambda x: classify_complexity(x["query"]) == "medium",
     models["medium"]),
    models["simple"]
)

# Usar
response = await router.apredict(query="Analyze supply chain optimization")
```

## Padrão 3: Composição Sofisticada de Tools

Agendar e coordenar **múltiplas ferramentas** em sequência.

````python
from langchain.tools import tool
from langchain.runnables import RunnableSequence

@tool
async def search_knowledge(query: str) -> str:
    """Busca na base de conhecimento Vectora"""
    results = await vectora.search(query, top_k=5)
    return "\n".join([r.content for r in results])

@tool
async def analyze_sentiment(text: str) -> dict:
    """Analisa sentimento do texto"""
    return {"sentiment": "positive", "score": 0.85}

@tool
async def summarize_text(text: str) -> str:
    """Sumariza texto longo"""
    return await llm.predict(f"Summarize: {text}")

@tool
async def format_markdown(text: str) -> str:
    """Formata como markdown"""
    return f"```\n{text}\n```"

# Composição: Search → Summarize → Sentiment → Format
tool_chain = RunnableSequence([
    ("search", search_knowledge),
    ("summarize", summarize_text),
    ("sentiment", analyze_sentiment),
    ("format", format_markdown)
])

# Executar cadeia
results = await tool_chain.apredict(
    query="What's the latest on AI?"
)
````

## Padrão 4: Contexto Enriquecido com RAG

Integrar busca vetorial com **reranking local**:

```python
from langchain.retrievers import MultiQueryRetriever
from langchain.retrievers.re_rank import RerankRetriever

async def rag_with_local_reranking(query: str):
    # 1. Busca inicial no Vectora
    initial_results = await vectora.search(query, top_k=20)

    # 2. Reranking local com Voyage
    reranked = await vectora.reranker.rank(
        query,
        [r.content for r in initial_results],
        top_k=5
    )

    # 3. Formatar contexto
    context = "\n\n".join([
        f"Source: {r['source']}\n{r['content']}"
        for r in reranked
    ])

    # 4. Passar ao agent
    response = await llm.predict(f"""
    Context:
    {context}

    Question: {query}
    """)

    return response
```

## Padrão 5: Validação em Múltiplos Níveis

**Validar resposta em cada etapa**:

```python
from langchain.runnables import RunnablePassthrough

async def validated_pipeline(user_query: str):
    # Nível 1: Validação de input
    if not is_valid_query(user_query):
        raise ValueError("Invalid query")

    # Nível 2: VCR Analysis
    analysis = await vcr.analyze(user_query)
    if analysis.confidence < 0.5:
        return "I'm not confident enough to answer this"

    # Nível 3: Tool Execution
    tool_results = []
    for tool in analysis.suggested_tools:
        try:
            result = await tool.apredict(user_query)
            tool_results.append(result)
        except Exception as e:
            logger.error(f"Tool failed: {e}")

    # Nível 4: LLM Response
    response = await llm.predict(f"""
    Tools returned: {tool_results}
    Generate response.
    """)

    # Nível 5: Validação de saída
    if not is_safe_response(response):
        return "Response blocked by guardrails"

    return response
```

## Padrão 6: Caching Inteligente

Cache de resultados **por similaridade semântica**:

```python
class SemanticCache:
    def __init__(self, vectora_client):
        self.vectora = vectora_client
        self.cache = {}

    async def get_or_compute(self, query: str, compute_fn):
        """
        Retorna resultado em cache se query similar existe
        Senão, computa e salva
        """

        # Buscar queries similares no cache
        query_embedding = await self.vectora.embed(query)

        similar = self.vectora.search_cache(
            query_embedding,
            threshold=0.95
        )

        if similar:
            return similar[0]["result"]

        # Computar novo resultado
        result = await compute_fn(query)

        # Salvar em cache
        self.cache[query] = {
            "embedding": query_embedding,
            "result": result,
            "timestamp": time.time()
        }

        return result

# Usar
cache = SemanticCache(vectora_client)
result = await cache.get_or_compute(
    "What is the capital of France?",
    lambda q: llm.predict(q)
)
```

## External Linking

| Conceito          | Recurso                   | Link                                                                                                                                     |
| ----------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| VCR Integration   | Vectora Cognitive Runtime | [https://vectora.dev/docs/vcr](https://vectora.dev/docs/vcr)                                                                             |
| Multi-LLM Routing | Router Pattern            | [https://docs.langchain.com/oss/python/langchain/runnable/branching](https://docs.langchain.com/oss/python/langchain/runnable/branching) |
| Tool Composition  | Complex Tools             | [https://docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools)                           |
| RAG Patterns      | Retrieval Augmented       | [https://docs.langchain.com/oss/python/langchain/retrieval](https://docs.langchain.com/oss/python/langchain/retrieval)                   |
| Caching           | Semantic Caching          | [https://docs.langchain.com/oss/python/langchain/caching](https://docs.langchain.com/oss/python/langchain/caching)                       |
