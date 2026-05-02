# AGENTS.md - Diretrizes do Vectora

Este arquivo fornece orientações para agentes de IA que trabalham neste repositório.

## Visão Geral do Projeto

**Vectora** é um sistema construído em Go. Este repositório contém o código-fonte Go (`internal/`, `pkg/`) e a documentação técnica (`docs/`).

IMPORTANTE: O diretório `docs/` é a documentação oficial do **Vectora** (construído com **Hugo** e **Hextra**). Portanto, toda a documentação DEVE seguir o formato específico do site Hugo/Hextra.

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

- **Código**: TODO o código-fonte Go (`internal/`, `pkg/`) DEVE estar em **inglês** (nomes de variáveis, comentários, docstrings).
- **Documentação**: PRIMARIAMENTE em **português** (PT-BR canônico, arquivos `.pt.md`), com traduções em inglês (arquivos `.en.md`).
- **Conversas**: PRIMARIAMENTE em **português** com o usuário.
- **Commits**: Mensagens em português/inglês (priorizar português).

## Estrutura de Conteúdo

- **`docs/`**: Documentação técnica (sincronizada com o site Hugo).
- **`internal/`**: Código privado da aplicação (cache, cli, config, engine, server, storage, etc.).
- **`pkg/`**: Código de biblioteca público/compartilhado (i18n, mcp, provider, etc.).
- **`pkg/`**: Código de biblioteca público/compartilhado (i18n, mcp, provider, etc.).

## Arquitetura de Documentação e Shortcodes (docs/)

- **Tema**: Hextra v0.11.1
- **Multi-idioma**: Português (canônico) e Inglês (traduções).
- **Shortcodes Obrigatórios (em todas as páginas de doc)**:
  - `{{< lang-toggle >}}`: Deve estar no topo.
  - `
`: Deve seguir o lang-toggle.

## Nomenclatura e Governança de Documentação

- **Nomes de Arquivos**: Kebab-case e nomes padronizados em inglês (ex: `vector-search.pt.md`).
- **Slugs**: Devem corresponder ao nome do arquivo (ex: `slug: vector-search`).
- **Estrutura e Fluxo de Texto**:
  - **Sem Empilhamento de Títulos**: NUNCA coloque um cabeçalho (H2, H3) imediatamente após outro cabeçalho ou o título da página (H1 do frontmatter). Deve SEMPRE haver um parágrafo descritivo entre eles.
  - **"Visão Geral" Redundante**: Remova cabeçalhos "## Visão Geral" ou "## Overview" se eles aparecerem logo após os shortcodes. Deixe o conteúdo fluir dinamicamente do topo.
  - **Hierarquia**: Não pule do H1 diretamente para o H3. Siga um fluxo lógico: H1 -> Parágrafo -> H2 -> Parágrafo -> H3.
- **Governança**: A "Lei de Ferro" (H1 -> Parágrafo -> H2) nunca deve ser violada.
- **Formatação**: Aplicam-se regras estritas de `markdownlint` e `prettier`.
- **Emojis**: **ABSOLUTAMENTE PROIBIDO** em documentação técnica. Sem emojis decorativos (, , etc.). Apenas tabelas, código, texto simples.

## Política de Links Externos (docs/)

Todas as páginas de documentação DEVEM incluir uma seção `## External Linking` ao final do conteúdo.

- **Requisito**: Inclua de 3 a 5 links externos válidos e relevantes (ex: RFCs, docs oficiais, padrões relacionados).
- **Formato**: Use uma tabela ou lista contendo o Conceito/Ferramenta, Descrição e Link.
- **Qualidade**: Sem URLs de placeholder, sem links genéricos repetitivos e sem links sem contexto descritivo.
- **Exceção**: Changelogs ou conteúdo temporal podem omitir esta seção, mas devem incluir o comentário HTML `<!-- External Linking omitido: conteúdo temporal -->`.

**Exemplo:**

> ## External Linking
>
> ### Autenticação e Segurança
>
> | Conceito      | Recurso         | Link                                                                  |
> | ------------- | --------------- | --------------------------------------------------------------------- |
> | **OAuth 2.0** | RFC 6749        | [ietf.org/rfc/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749) |
> | **JWT**       | JSON Web Tokens | [jwt.io](https://jwt.io/introduction)                                 |

## SEO e Metadados (docs/)

- **Tags de Frontmatter**: Toda página de documentação DEVE incluir uma lista de `tags` no frontmatter para SEO.

  ```yaml
  tags:
    - ai
    - context-engine
    - mcp
    - vectora
  ```

## Fluxo de Trabalho de Implementação

1. Sempre escreva/atualize as versões PT e EN de um arquivo (ex: `index.pt.md` e `index.en.md`) dentro de `docs/`.
2. Adira às convenções padrão do Go ao modificar `internal/` e `pkg/`.
3. Documente mudanças arquiteturais ou de configuração apropriadamente nos arquivos README e documentação técnica.

## Loop de Implementação Iterativo

O Vectora segue um processo de desenvolvimento iterativo rigoroso. Antes de transitar entre as fases de implementação, os agentes DEVEM:

1. **Reanalisar o Estado do Projeto**: Ler toda a documentação relevante (`docs/`) e a lógica central (`internal/`, `pkg/`) para garantir que não haja regressão ou desalinhamento.
2. **Execução em Fases**: Dividir grandes tarefas em fases atômicas. Cada fase requer seu próprio sub-plano.
3. **Governança Git**: Executar `git add .` e `git commit` ao final de cada fase com mensagens descritivas.
4. **Verificação**: Executar testes (`go test ./...`) e linting (`pre-commit run --all-files`) após cada fase.
5. **Integração de Pesquisa**: Consultar a documentação oficial (Gemini, Voyage, MongoDB Atlas), artigos acadêmicos (RAG, parsing AST) e melhores práticas para garantir uma implementação de última geração.
6. **Persistência do Loop**: Continuar este ciclo até que a condição "100% Pronto" seja atingida, onde nenhuma melhoria ou correção adicional seja identificada.
