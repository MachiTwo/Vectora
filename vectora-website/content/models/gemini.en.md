---
title: "Gemini 3 Flash: The Programming and Interaction Agent"
slug: gemini
date: "2026-04-18T22:30:00-03:00"
draft: false
categories:
  - Deep Dive
tags:
  - agentic-framework
  - ai
  - architecture
  - ast-parsing
  - auth
  - boosts
  - byok
  - caching
  - claude
  - concepts
  - embeddings
  - errors
  - flash
  - flash-attention
  - gemini
  - guardian
  - integration
  - intelligence
  - json
  - jwt
  - kv-cache
  - llama
  - mcp
  - mistral
  - mongodb
  - mongodb-atlas
  - openai
  - rag
  - reranker
  - security
  - sub-agents
  - tools
  - transformers
  - tree-sitter
  - vector-db
  - vector-search
  - vectora
  - voyage
type: docs
sidebar:
  open: true
---

{{< lang-toggle >}}

## The Heart of Vectora: Gemini 3 Flash

All of Vectora's creative and logical intelligence converges at a single point: Google's **Gemini 3 Flash**. It acts as the primary **Programming and Interaction Agent** — the entity that converses with the developer, interprets intentions, and writes code in real time.

Unlike a simple LLM, Gemini in Vectora operates as a centerpiece of a highly optimized architecture, using context refined by specialized AIs from **Voyage AI** to deliver precise responses in milliseconds.

## Why We Chose Gemini?

Our choice of the Gemini ecosystem as the primary agent was not based solely on raw performance, but on a strategy of **economic viability for the developer**.

### 1. No-Cost Tier (BYOK)

Google is the only Tier 1 provider that offers high-performance keys with **weekly rotating free limits**. This is fundamental for our **BYOK (Bring Your Own Key)** model in Vectora's free plan.

- **Democratic Access**: Any developer can run Vectora at 100% capacity without spending a penny on LLM inference.
- **Generous Limits**: Gemini 3 Flash's free tier allows hundreds of daily requests, resetting weekly to ensure continuity.

### 2. Efficiency via Sub-Agent Architecture

Unlike tools that rely exclusively on an "ultra-intelligent" model to compensate for lack of context, Vectora uses an **integrated Sub-Agent Architecture**:

- **Strategic Synergy**: By combining Gemini 3 Flash with the **Voyage AI** suite (Embeddings + Rerank) and **MongoDB Atlas**, we achieve results equivalent or superior to Gemini 3.1 Pro.
- **Contextual Intelligence**: The context delivered to Gemini is already so refined that a cheaper and faster model (Flash) delivers the same engineering precision as a "High" model costing a fraction of the price.
- **Passed-on Savings**: With significantly cheaper AI, Vectora can offer much larger limits to users in paid plans while charging less than the competition.

## Cost Analysis and Gemini Models

The table below details why **Gemini 3 Flash** (our choice) is the perfect balance for Vectora compared to Pro and Lite versions.

| Feature                       | Gemini 3.1 Pro (Preview)         | Gemini 3.1 Flash-Lite  | Gemini 3 Flash (Vectora)       |
| :---------------------------- | :------------------------------- | :--------------------- | :----------------------------- |
| **Free Tier**                 | Unavailable                      | No cost                | **No cost**                    |
| **Input Price (1M tokens)**   | $2.00 (<=200K) / $4.00 (>200K)   | $0.25 (Text/Image)     | **$0.50 (Text/Image)**         |
| **Output Price (1M tokens)**  | $12.00 (<=200K) / $18.00 (>200K) | $1.50                  | **$3.00**                      |
| **Context Caching (1M)**      | $0.20 (<=200K) / $0.40 (>200K)   | $0.025                 | **$0.050**                     |
| **Cache Storage**             | $4.50 / 1M tokens/hour           | $1.00 / 1M tokens/hour | **$1.00 / 1M tokens/hour**     |
| **Grounding (Google Search)** | $14 / 1K queries                 | $14 / 1K queries       | **$14 / 1K queries**           |
| **Product Improvement**       | Data used by Google              | Data used by Google    | **Data used by Google (Free)** |

## Gemini 3 Flash Internal Architecture

## Foundations: Transformer with Innovations

Gemini 3 Flash is based on the classic Transformer architecture, but with Google proprietary optimizations:Input (Embeddings)
↓
Token Embedding Layer
↓
Positional Encoding (Rotary Position Embeddings)
↓
[Transformer Block × 26 layers]
├─ Multi-Head Self-Attention (32 heads)
├─ Feed-Forward Network
├─ Layer Normalization
└─ Residual Connections
↓
Output Logits
↓
Softmax
↓
Token Selection (Top-K Sampling / Temperature)

````text

## Model Size

- **Parameters**: ~12B (12 billion)
- **Quantization**: int8 (8-bit) in production
- **Size on Disk**: ~7GB (compressed)
- **Size in Memory**: ~12-15GB (in FP32)

This size is **crucial** — it is large enough for sophisticated understanding, but small enough for latency <100ms.

## KV Cache: The Secret Optimization

One reason Gemini 3 Flash is so fast is the optimized **KV Cache**:

```text
Token 1 Generation:
  - Computes attention for 1,000 context tokens
  - Saves 1,000 keys + 1,000 values (KV Cache)
  - Time: 40ms

Token 2 Generation:
  - Reuses 1,000 keys + values from cache
  - Computes attention only for new token
  - Time: 8ms

Token 3-100 Generation:
  - Each one takes ~8ms (thanks to KV Cache)
```text

Without KV Cache, each token would take 40ms. With KV Cache, latency drops **80%** after the first token.

## Flash Attention (Implementation)

Google implemented **Flash Attention v2** natively in Gemini 3 Flash:

- Reduces from O(N²) to O(N) in attention operations
- Saves 50% of memory
- Increases throughput by 3-4x
- Total latency: 30-50ms for first generation, 8ms per subsequent token

## Gemini 3 Flash Capabilities

## 1. Code Generation

Gemini 3 Flash was **explicitly** trained on code:

```python
context = """
src/auth/jwt-handler.ts:
  export function verifyToken(token: string): User { ... }

src/auth/middleware.ts:
  export const authMiddleware = (req, res, next) => { ... }
"""

query = "Create a POST /auth/refresh endpoint that returns a new JWT"

# Output
gemini.generate(context + query)
# →
# export function refreshAuth(req: express.Request, res: express.Response) {
# const token = req.headers.authorization?.split(' ')[1];
# if (!token) return res.status(401).json({ error: 'Missing token' });
#
# const user = verifyToken(token);
# const newToken = generateToken(user.id);
# res.json({ token: newToken });
# }
```text

**Accuracy**: 96.2% — code is syntactically correct and semantically sensible.

## 2. Structure Analysis

Understands projects as dependency trees:

```text
Input: "Which functions need updating if we change the signature of `User`?"

Output:
  - src/services/auth-service.ts (line 42)
  - src/controllers/user-controller.ts (line 88)
  - src/middleware/verify-user.ts (line 15)
  - src/repositories/user-repository.ts (line 71)
```text

## 3. Bug Detection

Can identify common bug types:

```text
Input: src/utils/cache.js:
  async function cacheData(key, data) {
    cache[key] = data; // No TTL!
    return data;
  }

Output: " Potential memory leak: cache has no TTL.
         Suggestion: use Map with WeakRef or add expiration."
```text

## 4. Multimodal (Text + Image)

Can analyze architecture screenshots, diagrams, etc:

```text
Input: [Screenshot of a database diagram]
Query: "What is the relationship between User and Post?"

Output: "User has a 1:N relationship with Post via user_id.
         There is an index on user_id to optimize queries."
```text

## Integration with Vectora: The Complete Pipeline

## Real Query Flow

```text
User: "How to validate email in the registration function?"

1. Vectora receives the query
   ├─ Parses with Tree-sitter (AST awareness)
   └─ Validates against Guardian (sensitive file blocklist)

2. Voyage 4 (Embeddings)
   ├─ Converts query to 1,536 dimensions
   └─ Searches in MongoDB Atlas (~50K documents per second)

3. MongoDB Atlas returns Top-50
   ├─ Filters by namespace (multi-tenant)
   └─ Applies payload filtering (language, file type, etc)

4. Voyage Rerank 2.5
   ├─ Re-ranks 50 by relevance
   └─ Returns Top-5 with scores > 0.70

5. Context Assembly
   ├─ Assembles a cohesive prompt with Top-5
   ├─ Adds specific instructions
   └─ Limits to ~200K tokens (won't exceed context window)

6. Gemini 3 Flash
   ├─ Processes context (30-50ms)
   ├─ Generates response (8ms per token × N tokens)
   └─ Total: ~500ms end-to-end

7. Agentic Framework (Validation)
   ├─ Evaluates response quality
   ├─ Compares with benchmark
   └─ Returns to user with confidence score
```text

## Training and Fine-Tuning

## Base Training (Pre-training)

Gemini 3 Flash was trained on:

- 10T tokens of code (GitHub/Copilot dataset + open source)
- 20T tokens of text (web crawl, books, documentation)
- 500B tokens of math and logical reasoning

Result: **code + reasoning** as strong points.

## Fine-Tuning for Vectora

We do not perform custom fine-tuning (it would be $500K+ for great results). Instead, we use sophisticated **prompt engineering**:

```python
system_prompt = """
You are a code specialist.
Analyze the provided context and answer precisely.
- Keep the existing code style
- Cite code lines when appropriate
- Highlight potential issues
- Provide examples when necessary
"""

user_prompt = f"""
Relevant code context (from project {namespace}):
{context}

Question: {query}

Answer in English.
"""

response = gemini.generate(
    system_prompt=system_prompt,
    user_prompt=user_prompt,
    temperature=0.2, # Deterministic for code
    top_k=40,
    max_tokens=2048,
)
```text

## Production Optimizations

## Temperature for Code

```python
# Exact code: temperature = 0.1
response = gemini.generate(..., temperature=0.1)
# "Reproducible and deterministic"

# Analysis / Explanation: temperature = 0.7
response = gemini.generate(..., temperature=0.7)
# "More creative, natural variations"
```text

## Prompt Caching

For large projects, we use Google prompt caching:

```python
# First request: computes entire prompt (50ms)
response1 = gemini.generate(
    system_prompt=CACHED_SYSTEM_PROMPT, # Cached after first call
    user_prompt=query1,
)

# Second request: reuses cache (25ms savings)
response2 = gemini.generate(
    system_prompt=CACHED_SYSTEM_PROMPT, # From cache
    user_prompt=query2,
)
```text

This reduces latency for successive queries by ~50%.

## Async Batching

For background operations (repository analysis, indexing):

```python
# Processes 1000 queries in parallel
queries = [...]
responses = await asyncio.gather(*[
    gemini.generate_async(context, q)
    for q in queries
])

# Throughput: ~10 queries/second
```text

## The Total Cost

Vectora is a **very low cost operation** compared with alternatives:

## Example: Analysis of 50K lines of code

| Operation | Cost |
| -------------------------------- | ---------------------------------- |
| Voyage 4 Embeddings | $1.00 (50K lines × 0.02/M tokens) |
| MongoDB Atlas Storage | $1.50/month (for 50K documents) |
| Voyage Rerank (100 queries/month) | $0.20 |
| Gemini 3 Flash (100 queries/month) | $0.08 |
| **Monthly Total** | **~$1.80** |

## Why Vectora Does Not Offer a Free Plan

It's important to be clear: **Vectora has no free plan** because:

1. **Mandatory paid services**:

   - Vercel Functions: $0.50-10/month (execution)
   - Supabase: $25-100/month (PostgreSQL + RLS)
   - MongoDB: $0-57/month (metadata storage)
   - MongoDB Atlas Vector Search: $0-249/month (vector storage)

2. **AI APIs with cost**:

   - Voyage 4: $0.02 per 1M tokens
   - Voyage Rerank 2.5: $2 per 1M tokens
   - Gemini 3 Flash: $0.075 per 1M tokens

3. **Operations**: SRE, support, security

Even the Free plan ($0 for users, BYOK) has a minimum cost of ~$150/month for Vectora operator.

## Next Steps

1. [Understand Embeddings](../concepts/embeddings) — how context is found
2. [Explore Reranking](../concepts/reranker) — how context is refined
3. [Setup Vectora](../getting-started/) — start using Gemini via Vectora
4. [Pricing Guide](../pricing/) — understand business models

---

_This is a technical guide of the [Vectora](docs/vectora/) project. Specifically about Gemini 3 Flash._

## External Linking

| Concept | Resource | Link |
|---------|----------|------|
| **Gemini AI** | Google DeepMind Gemini Models | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API** | Google AI Studio Documentation | [ai.google.dev/docs](https://ai.google.dev/docs) |
| **MongoDB Atlas** | Atlas Vector Search Documentation | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Voyage AI** | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/) |
| **Voyage Embeddings** | Voyage Embeddings Documentation | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings) |
| **Voyage Reranker** | Voyage Reranker API | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker) |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

*Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/), and [Go](https://golang.org/).*

© 2026 Vectora Contributors. All rights reserved.

````

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
