---
title: "Suite de Testes: Performance & Benchmarks"
slug: performance
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - benchmarks
  - concepts
  - context-engine
  - embeddings
  - performance
  - profiling
  - system
  - testing
  - vectora
---

{{< lang-toggle >}}

O Vectora deve atender a todos os SLAs de performance, com latência, throughput, utilização de recursos e escalabilidade comprovadas através de benchmarks rigorosos. Esta suite valida que o Vectora escala eficientemente para mais de 50 usuários simultâneos e mantém uma latência p95 inferior a 500ms.

Ao impor metas de performance estritas, garantimos que o Context Engine permaneça responsivo mesmo sob carga pesada ou com bases de código muito grandes.

**Cobertura**: 80+ testes | **Prioridade**: ALTA

## Testes de Latência de Query

Garante que as requisições dos usuários sejam processadas e retornadas dentro de prazos aceitáveis.

- **Latência p50**: Alvo < 100ms para consultas de busca típicas (12 testes).
- **Latência p95**: Alvo < 500ms para garantir uma experiência suave para a maioria dos usuários (12 testes).
- **Latência p99**: Alvo < 1s para limitar os tempos de resposta no pior caso (10 testes).
- **Warmup vs Cold Start**: Mede o impacto na performance do aquecimento de cache (8 testes).

**Alvo**: p95 < 500ms, p99 < 1s.

## Latência de Embedding & Rerank

Monitora a performance das chamadas de API externas e seu impacto no ciclo geral de busca.

- **Embedding de Query Única**: Alvo < 2s para um trecho de código padrão (8 testes).
- **Embeddings em Lote**: Alvo < 5s para processar múltiplos chunks simultaneamente (8 testes).
- **Latência de Reranking**: Garante que o refinamento final dos resultados leve menos de 1s (8 testes).
- **Latência de Hit no Cache**: Valida que dados recuperados do cache L1/L2 retornem em < 50ms (8 testes).

**Alvo**: Único < 2s, Lote < 5s.

## Testes de Throughput

Valida a habilidade do sistema em lidar com altos volumes de requisições concorrentes.

- **Consultas por Segundo**: Alvo > 100 consultas sustentadas (10 testes).
- **Embeddings por Segundo**: Alvo > 50 chunks processados (8 testes).
- **Usuários Concorrentes**: Valida a estabilidade com mais de 50 sessões ativas simultâneas (10 testes).
- **Carga Sustentada**: Testa o comportamento do sistema sob carga contínua por mais de 1 hora (8 testes).

**Alvo**: > 100 consultas/seg sustentadas.

## Utilização de Recursos

Garante que a aplicação permaneça eficiente e não exaura os recursos do hospedeiro.

- **Pegada de Memória**: Alvo < 500MB total RSS sob carga normal (8 testes).
- **Uso de CPU**: Alvo < 50% de média entre os núcleos disponíveis (8 testes).
- **Estabilidade de Goroutines**: Garante que operações concorrentes sejam limpas corretamente (8 testes).

**Alvo**: < 500MB de memória, < 50% de CPU.

## Testes de Escalabilidade

Testa a resposta do sistema ao crescimento rápido no volume de requisições ou tamanho dos dados.

- **100 Requisições Concorrentes**: Tratamento de picos repentinos (bursts) (8 testes).
- **1000 Requisições/min**: Tráfego de alto volume sustentado (8 testes).
- **Tratamento de Resultados Grandes**: Valida a performance ao retornar mais de 1MB de dados JSON (8 testes).

**Alvo**: 100+ usuários concorrentes, 1000+ requisições por minuto.

## SLAs de Performance

A tabela a seguir resume os principais alvos de performance para o sistema Vectora.

| Métrica                   | Alvo                |
| :------------------------ | :------------------ |
| **Latência p50**          | < 100ms             |
| **Latência p95**          | < 500ms             |
| **Latência p99**          | < 1s                |
| **Throughput**            | > 100 consultas/seg |
| **Uso de Memória**        | < 500MB             |
| **Uso de CPU**            | < 50%               |
| **Usuários Concorrentes** | > 50                |

## External Linking

| Conceito       | Recurso                              | Link                                                                               |
| :------------- | :----------------------------------- | :--------------------------------------------------------------------------------- |
| **Profiling**  | Documentação do pprof em Go          | [pkg.go.dev/net/http/pprof](https://pkg.go.dev/net/http/pprof)                     |
| **Latência**   | Entendendo Percentis de Latência     | [robertovitillo.com/percentiles/](https://www.robertovitillo.com/percentiles/)     |
| **Benchmarks** | Melhores Práticas de Benchmark em Go | [dave.cheney.net/high-performance-go](https://dave.cheney.net/high-performance-go) |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
