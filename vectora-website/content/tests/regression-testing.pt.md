---
title: "Suite de Testes: Testes de Regressão"
slug: regression-testing
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - ast-parsing
  - auth
  - ci-cd
  - concepts
  - config
  - mongodb-atlas
  - persistence
  - regression
  - security
  - system
  - testing
  - vector-search
  - vectora
---

{{< lang-toggle >}}

Bugs que foram corrigidos não devem reaparecer, e casos de borda (edge cases) conhecidos devem continuar funcionando conforme o projeto evolui. Esta suite é contínua, executada com cada commit para validar que as correções permaneçam e que novas mudanças não reintroduzam problemas antigos.

Ao manter uma suite de regressão robusta, garantimos a estabilidade e a confiabilidade de longo prazo da plataforma Vectora.

**Cobertura**: Contínua | **Prioridade**: CRÍTICA

## Bugs Corrigidos Anteriormente

Cada bug reportado em issues que foi fechado deve ter um teste de regressão correspondente.

1. **Reprodução**: O teste deve ser capaz de reproduzir o bug original (antes da correção).
2. **Validação**: O teste deve confirmar que a correção está funcionando conforme o pretendido (após a correção).
3. **Persistência**: O teste permanece na suite para prevenir regressões futuras.

### Exemplo de Caso de Estudo: Issue #42

Considere um bug onde a busca retorna vazio para caracteres especiais.

```text
Issue #42: "Busca retorna vazio para caracteres especiais"

Teste: TestSpecialCharacterSearch_Issue42
├─ Setup: Query com "C++", "C#", ".NET"
├─ Chamada: search_context("C++")
├─ Assert: Resultados retornados (não vazio)
└─ Rerun: Verificado em cada commit
```

## Problemas de Integração Comuns

Monitoramos vários desafios técnicos recorrentes para garantir que eles não degradem com o tempo.

- Condições de corrida na invalidação de cache (5 testes).
- Exaustão do pool de conexões do MongoDB sob carga (5 testes).
- Expiração de token JWT durante consultas de longa duração (3 testes).
- Conflitos de escrita concorrente e versionamento de documentos (5 testes).
- Detecção de vazamentos de goroutines em trabalhadores de background (5 testes).

## Casos de Borda Conhecidos

Um conjunto dedicado de testes para cenários que são raros, mas críticos para a robustez do sistema.

- Tratamento de consultas vazias e intenções malformadas (3 testes).
- Processamento de payloads extremamente grandes (> 100MB) (2 testes).
- Estruturas AST profundamente aninhadas e dependências circulares (3 testes).
- Arquivos deletados que permanecem no índice vetorial (2 testes).
- Modificações de namespace concorrentes e segurança de travas (3 testes).

## Compatibilidade & Manutenção

Garante que o Vectora permaneça estável através de diferentes versões e formatos de configuração.

- **Funcionalidades Depreciadas**: Valida que endpoints ou flags antigos ainda funcionem (com avisos).
- **Compatibilidade de Versão**: Verifica a compatibilidade direta e reversa dos formatos de dados.
- **Baselines de Performance**: Monitora a latência de consulta e o uso de memória para detectar regressões de performance.

## Integração CI/CD

A suite de regressão está integrada ao nosso fluxo de trabalho de desenvolvimento automatizado.

### Verificação Pré-commit

Garante que as principais regressões sejam capturadas antes mesmo do código sair da máquina do desenvolvedor.

```bash
pre-commit run regression-tests --all-files
```

### Pipeline Automatizado

Cada commit enviado ao repositório aciona a suite completa de regressão.

```bash
# Testes de regressão devem passar antes do merge
go test -race ./tests/regression/... -timeout 10m
```

### Teste de Estresse Semanal

Uma execução estendida projetada para capturar condições de corrida raras ou vazamentos de memória que só aparecem sob carga prolongada.

```bash
# Teste de regressão estendido semanal
go test -race ./tests/regression/... -timeout 1h -stress
```

## Critérios de Teste de Regressão

A tabela a seguir resume os principais alvos para a suite de testes de regressão.

| Critério                         | Alvo                         |
| :------------------------------- | :--------------------------- |
| **Cobertura de Bugs Corrigidos** | 100%                         |
| **Casos de Borda Cobertos**      | > 90%                        |
| **Baseline de Performance**      | Mantido                      |
| **Taxa de Aprovação**            | 100%                         |
| **Tempo de Execução (CI)**       | < 5 min                      |
| **Estabilidade**                 | Sem testes instáveis (flaky) |

## External Linking

| Concept            | Resource                                       | Link                                                                                                       |
| ------------------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**  | Atlas Vector Search Documentation              | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**    | Tree-sitter Official Documentation             | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **JWT**            | RFC 7519: JSON Web Token Standard              | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                     |
| **GitHub Actions** | Automate your workflow from idea to production | [docs.github.com/en/actions](https://docs.github.com/en/actions)                                           |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
