# AGENTS.md - Diretrizes do Vectora

Este arquivo fornece orientacoes para agentes de IA que trabalham neste monorepo.

## Visão Geral do Projeto

**Vectora** é um monorepo com estas áreas principais:

- `vectora/`: produto principal, incluindo backend Go, frontend React e CLI
- `vectora-asset-library/`: biblioteca/registry de assets e datasets
- `vectora-cognitive-runtime/`: VCR, o mecanismo de decisão em Python
- `vectora-integrations/`: integrações e SDKs em Turborepo
- `vectora-website/`: site oficial e documentação em Hugo/Hextra

IMPORTANTE: A documentação oficial vive em `vectora-website/content/` e deve seguir o formato Hugo/Hextra usado no site.

## Comandos Essenciais

```bash
# Desenvolvimento Go
go mod tidy
go test ./...
go build ./...

# Validação
pre-commit run --all-files
```

## Diretrizes de Comunicação e Idioma

- **Código**: todo o código-fonte Go e Python no monorepo deve estar em inglês (nomes de variáveis, comentários, docstrings).
- **Comentários no código**: sempre em inglês, sem exceções.
- **Documentação**: inicialmente primariamente em português (PT-BR canônico, arquivos `.pt.md`), com traduções em inglês (arquivos `.en.md`) quando existirem.
- **READMEs e docs públicas**: por enquanto podem começar em português, mas a base do projeto é open source e deve evoluir para inglês para ampliar a comunidade.
- **Conversas**: primariamente em português com o usuário.
- **Commits**: mensagens em português/inglês, priorizando português.
- **Racional de idioma**: o usuário prefere português; o projeto, o código e os comentários devem manter inglês para favorecer colaboração global futura.

## Estrutura de Conteúdo

- **`vectora/`**: produto principal com backend, frontend, CLI e documentação de aplicação.
- **`vectora-asset-library/`**: catálogo e governança de assets/datasets.
- **`vectora-cognitive-runtime/`**: runtime de decisão e inferência do VCR.
- **`vectora-integrations/`**: SDKs e adaptadores para agentes externos.
- **`vectora-website/`**: site oficial, documentação e guias.
- **`vectora-website/content/`**: fonte canônica da documentação Hugo/Hextra.

## Arquitetura de Documentação e Shortcodes (`vectora-website/content/`)

- **Tema**: Hextra v0.11.1
- **Multi-idioma**: português (canônico) e inglês (traduções).
- **Shortcodes obrigatórios (em todas as páginas de doc)**:
  - `{{< lang-toggle >}}`: deve estar no topo.
  - `{{< section-toggle >}}`: deve seguir o lang-toggle.

## Nomenclatura e Governança de Documentação

- **Nomes de arquivos**: kebab-case e nomes padronizados em inglês (ex: `vector-search.pt.md`).
- **Slugs**: devem corresponder ao nome do arquivo (ex: `slug: vector-search`).
- **Estrutura e fluxo de texto**:
  - **Sem empilhamento de títulos**: nunca coloque um cabeçalho (H2, H3) imediatamente após outro cabeçalho ou o título da página (H1 do frontmatter). Deve sempre haver um parágrafo descritivo entre eles.
  - **"Visão Geral" redundante**: remova cabeçalhos "## Visão Geral" ou "## Overview" se eles aparecerem logo após os shortcodes. Deixe o conteúdo fluir dinamicamente do topo.
  - **Hierarquia**: não pule do H1 diretamente para o H3. Siga um fluxo lógico: H1 -> Parágrafo -> H2 -> Parágrafo -> H3.
- **Governança**: a "Lei de Ferro" (H1 -> Parágrafo -> H2) nunca deve ser violada.
- **Formatação**: aplicam-se regras estritas de `markdownlint` e `prettier`.
- **Emojis**: absolutamente proibido em documentação técnica. Sem emojis decorativos. Apenas tabelas, código e texto simples.

## Política de Links Externos (`vectora-website/content/`)

Todas as páginas de documentação DEVEM incluir uma seção `## External Linking` ao final do conteúdo.

- **Requisito**: inclua de 3 a 5 links externos válidos e relevantes (ex: RFCs, docs oficiais, padrões relacionados).
- **Formato**: use uma tabela ou lista contendo o Conceito/Ferramenta, Descrição e Link.
- **Qualidade**: sem URLs de placeholder, sem links genéricos repetitivos e sem links sem contexto descritivo.
- **Exceção**: changelogs ou conteúdo temporal podem omitir esta seção, mas devem incluir o comentário HTML `<!-- External Linking omitido: conteúdo temporal -->`.

**Exemplo:**

> ## External Linking
>
> ### Autenticação e Segurança
>
> | Conceito      | Recurso         | Link                                                                  |
> | ------------- | --------------- | --------------------------------------------------------------------- |
> | **OAuth 2.0** | RFC 6749        | [ietf.org/rfc/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749) |
> | **JWT**       | JSON Web Tokens | [jwt.io](https://jwt.io/introduction)                                 |

## SEO e Metadados (`vectora-website/content/`)

- **Tags de frontmatter**: toda página de documentação DEVE incluir uma lista de `tags` no frontmatter para SEO.

  ```yaml
  tags:
    - ai
    - context-engine
    - mcp
    - vectora
  ```

## Fluxo de Trabalho de Implementação

1. Sempre escreva/atualize as versões PT e EN de um arquivo (ex: `index.pt.md` e `index.en.md`) dentro de `vectora-website/content/`.
2. Adira às convenções padrão do Go ao modificar o código em `vectora/` e às convenções de Python ao modificar `vectora-cognitive-runtime/`.
3. Documente mudanças arquiteturais ou de configuração apropriadamente nos arquivos README e na documentação técnica do site.

## Loop de Implementação Iterativo

O Vectora segue um processo de desenvolvimento iterativo rigoroso. Antes de transitar entre as fases de implementação, os agentes DEVEM:

1. **Reanalisar o Estado do Projeto**: ler a documentação relevante em `vectora-website/content/` e a lógica central nos diretórios do monorepo para garantir que não haja regressão ou desalinhamento.
2. **Execução em Fases**: dividir grandes tarefas em fases atômicas. Cada fase requer seu próprio sub-plano.
3. **Governança Git**: executar `git add .` e `git commit` ao final de cada fase com mensagens descritivas.
4. **Verificação**: executar testes (`go test ./...`) e linting (`pre-commit run --all-files`) após cada fase.
5. **Integração de Pesquisa**: consultar a documentação oficial (Gemini, Voyage, MongoDB Atlas), artigos acadêmicos (RAG, parsing AST) e melhores práticas para garantir uma implementação de última geração.
6. **Persistência do Loop**: continuar este ciclo até que a condição "100% Pronto" seja atingida, onde nenhuma melhoria ou correção adicional seja identificada.
