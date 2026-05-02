---
title: "Namespaces"
slug: namespaces
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - cloud
  - concepts
  - config
  - embeddings
  - guardian
  - infrastructure
  - mcp
  - mongodb-atlas
  - namespaces
  - protocol
  - security
  - system
  - trust-folder
  - vector-search
  - vectora
  - yaml
---

{{< lang-toggle >}}

> [!NOTE] > **Namespaces é um recurso do Vectora Cloud**. O Vectora Desktop usa uma **Trust Folder** (sandbox do sistema de arquivos) em vez de namespaces. Se você estiver usando o CLI local do Vectora, consulte [Infrastructure → Trust Folder](./trust-folder.md).

Namespaces são **isoladores lógicos** para índices vetoriais dentro do MongoDB Atlas. Cada projeto, ambiente ou contexto roda em seu próprio namespace, evitando que resultados de diferentes fontes contaminem uns aos outros.

Ao fornecer este isolamento, o Vectora garante segurança multi-tenant e clareza organizacional.

> [!IMPORTANT]
> Um namespace atua como um "banco de dados virtual" dentro da Busca Vetorial do MongoDB Atlas. Buscas em um namespace NUNCA retornam chunks de outro, garantindo isolamento de contexto entre diferentes equipes ou projetos.

## O Problema e a Solução

Sem namespaces, uma busca por um termo comum como "login" poderia retornar resultados de dezenas de projetos diferentes, levando ao vazamento de contexto e impossibilitando o gerenciamento de índices por equipe.

Com namespaces, os resultados da busca são estritamente isolados. Uma consulta por "login" retorna resultados APENAS do namespace específico do projeto, permitindo que múltiplas equipes compartilhem uma única instância do MongoDB Atlas de forma segura e eficiente.

## Nomenclatura & Convenções

A padronização dos nomes de namespaces é essencial para a organização e automação em clusters multi-tenant.

### Padrão Recomendado

É uma melhor prática seguir uma convenção de nomenclatura estruturada que inclua a organização, o nome do projeto e o ambiente.

```text
<org>-<project>-<environment>
```

**Exemplos:**

- `kaffyn-vectora-prod`
- `kaffyn-vectora-dev`
- `acme-backend-staging`

### Regras de Validação

Os namespaces devem aderir às seguintes restrições de nomenclatura para garantir a compatibilidade com a infraestrutura em nuvem.

- Comprimento: 3-63 caracteres.
- Caracteres: Letras minúsculas, números e hifens `[a-z0-9-]`.
- Deve começar com uma letra.
- Sem sublinhados (underscores), espaços ou caracteres especiais.

## Ciclo de Vida do Namespace

Gerenciar um namespace envolve sua inicialização técnica, indexação contínua e eventual descarte seguro de dados.

### Processo de Criação

Você pode criar um novo namespace via CLI ou definindo-o na configuração do seu projeto.

```bash
# Via CLI
vectora namespace create --name kaffyn-vectora-prod
```

Quando um namespace é criado, o MongoDB Atlas inicializa uma nova coleção e índices HNSW vazios para embeddings, enquanto o módulo Guardian registra a criação nos logs de auditoria.

### Indexação e Busca

Uma vez criado, o namespace aceita chunks de dados. Cada chunk inserido no sistema é marcado com seu namespace pai. Consequentemente, cada requisição de busca deve especificar o namespace alvo para garantir resultados filtrados e precisos.

### Exclusão & Limpeza

Excluir um namespace é uma ação permanente que não pode ser desfeita. Você também pode resetar os índices dentro de um namespace se precisar realizar uma nova indexação do projeto.

## Padrões de Multi-Tenancy

Namespaces permitem diversas estratégias de isolamento, dependendo dos requisitos organizacionais.

### Padrão 1: Um Namespace por Projeto

Este padrão fornece isolamento completo entre projetos, o que é ideal para equipes estritamente separadas ou requisitos rigorosos de conformidade, onde o compartilhamento de dados entre projetos é proibido.

### Padrão 2: Ambientes no Mesmo Projeto

Este é um padrão comum onde diferentes namespaces representam ambientes de desenvolvimento, staging e produção para o mesmo projeto. Isso evita que dados de desenvolvimento apareçam nos resultados de busca de produção.

### Padrão 3: Serviços Compartilhados + Equipes Privadas

Nesta arquitetura, alguns namespaces são compartilhados (ex: para documentação geral ou utilitários compartilhados), enquanto outros namespaces permanecem privados para equipes específicas, permitindo uma mistura de contextos compartilhados e isolados.

## Métricas & Observabilidade de Namespace

A observabilidade é aplicada individualmente a cada namespace, permitindo auditorias precisas de performance e rastreamento de uso.

### Inspeção de Saúde

Você pode recuperar estatísticas detalhadas para um namespace específico usando o CLI.

```bash
vectora namespace info --name kaffyn-vectora-prod
```

A saída inclui o número de chunks indexados, o tamanho da coleção em disco, métricas de latência de busca (P99) e o número total de buscas realizadas nas últimas 24 horas.

### Alertas Automatizados

O Agentic Framework pode ser configurado para monitorar a saúde do namespace e disparar alertas se a latência exceder os limites ou se a indexação ficar atrasada.

## Exemplos de Configuração

Defina suas configurações de namespace no arquivo `vectora.config.yaml` para garantir que o CLI e os agentes usem o contexto correto.

```yaml
# vectora.config.yaml
project:
  name: "Meu Projeto"
  namespace: kaffyn-vectora-prod

# Avançado: Múltiplos namespaces
namespaces:
  default: kaffyn-vectora-prod
  fallback: kaffyn-vectora-backup
```

## External Linking

| Concept           | Resource                                                 | Link                                                                                                       |
| ----------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation                        | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**           | Model Context Protocol Specification                     | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)                               | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **Observability** | Control Theory and System Observability                  | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)                         |
| **HNSW**          | Efficient and robust approximate nearest neighbor search | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)                                               |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
