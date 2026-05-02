---
title: "Trust Folder: Perímetro de Segurança Desktop"
slug: trust-folder
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - compliance
  - concepts
  - config
  - desktop
  - mongodb-atlas
  - rbac
  - security
  - system
  - trust-folder
  - vector-search
  - vectora
  - yaml
---

{{< lang-toggle >}}

> [!NOTE] > **O Trust Folder é um recurso exclusivo do Vectora Desktop**. O Vectora Cloud não utiliza o Trust Folder porque não possui acesso direto ao sistema de arquivos local — em seu lugar, utiliza o isolamento por **Namespaces** no MongoDB Atlas. Para saber mais sobre a segurança em nuvem, veja [Infraestrutura → Namespaces](../namespaces).

O Trust Folder é o **perímetro de segurança** que limita quais arquivos o Vectora Desktop pode indexar, ler e processar localmente. Ele funciona como um sandbox de caminhos, protegendo contra a leitura acidental ou maliciosa de arquivos sensíveis fora do escopo do projeto.

No ambiente Desktop, o Trust Folder é obrigatório para evitar que o agente indexe arquivos como `.env`, chaves privadas SSH ou dados pessoais do usuário.

## O Problema do Acesso Irrestrito

Sem a configuração de um Trust Folder, um agente de IA poderia potencialmente acessar qualquer arquivo no disco rígido.

- **Exposição de Segredos**: Indexação automática de `/etc/passwd`, `~/.ssh/id_rsa` ou arquivos `.env`.
- **Ataques de Traversal**: Vulnerabilidade a tentativas de acessar arquivos via caminhos relativos como `../../sensitive/file.txt`.
- **Falta de Auditoria**: Dificuldade em rastrear quais arquivos foram processados pelo motor de IA.

Com o Trust Folder, a indexação é confinada a diretórios específicos (ex: `./src`, `./docs`), bloqueando qualquer tentativa de "saída" do perímetro e gerando logs de auditoria detalhados para cada tentativa de leitura.

## Desktop vs Cloud: Trust Folder vs Namespace

A tabela abaixo compara os mecanismos de isolamento entre as versões Desktop e Cloud do Vectora.

| Aspecto        | Trust Folder (Desktop)             | Namespace (Cloud)               |
| :------------- | :--------------------------------- | :------------------------------ |
| **Escopo**     | Sistema de arquivos local          | Collections do MongoDB Atlas    |
| **Isolamento** | Baseado em caminhos (Path-based)   | Baseado em Workspace/Tenant     |
| **Controle**   | Configuração local (`config.yaml`) | Administrador Cloud / RBAC      |
| **Segurança**  | Bloqueia Path Traversal            | Bloqueia Query Isolation        |
| **Audit**      | Logs locais de filesystem          | Logs de auditoria Cloud (Atlas) |

## Configuração do Trust Folder

A configuração é feita através do arquivo `vectora.config.yaml`. Você pode definir um único diretório raiz ou uma lista de pastas confiáveis.

### Configuração Padrão (Raiz)

Por padrão, o Vectora confia na raiz do projeto onde foi inicializado.

```yaml
project:
  trust_folder: "." # Confia em tudo dentro do diretório atual e subpastas
```

### Configuração Explícita (Recomendada)

Para maior segurança, recomenda-se listar apenas as pastas necessárias para o funcionamento do agente.

```yaml
project:
  trust_folders:
    - "./src"
    - "./docs"
    - "./packages"
  # Pastas como node_modules, build e arquivos .env serão ignorados
```

## Resolução Segura de Caminhos

O Vectora resolve caminhos de forma segura, normalizando caminhos relativos para absolutos e bloqueando tentativas de sair do perímetro definido.

### Exemplo de Bloqueio de Path Traversal

Se o Trust Folder estiver definido como `./src` e houver uma tentativa de leitura para `../../../.env`:

1. O motor normaliza o caminho para `/absolute/path/.env`.
2. Verifica se este caminho está contido dentro de `/absolute/path/to/src`.
3. Caso negativo, a operação é **BLOQUEADA** e um evento de segurança é gerado.

## Cenários de Segurança (O que é prevenido)

O Trust Folder protege o desenvolvedor contra diversos vetores de ataque comuns em ambientes de IA.

- **Path Traversal Simples**: Impede que a LLM peça para ler arquivos sensíveis fora do projeto.
- **Symlink Escape**: Detecta e bloqueia symlinks que apontam para fora do diretório confiável.
- **Injeção via Contexto**: Bloqueia comandos de busca injetados no prompt que tentam acessar o sistema de arquivos do SO (ex: `/etc/passwd`).
- **Exposição em CI/CD**: Garante que runners de CI indexem apenas o código-fonte, ignorando segredos de infraestrutura presentes na máquina.

## Auditoria e Monitoramento

Todas as tentativas de acesso a arquivos, permitidas ou negadas, são registradas no log de auditoria do sistema.

```bash
# Verificar tentativas bloqueadas nas últimas 24 horas
vectora audit --since 24h --filter "DENIED"
```

O log gerado inclui o timestamp, o caminho solicitado, o caminho normalizado, o Trust Folder ativo e o motivo da negação (ex: `outside_trust_folder`).

## External Linking

| Concept            | Resource                                       | Link                                                                                                       |
| ------------------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**  | Atlas Vector Search Documentation              | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **RBAC**           | NIST Role-Based Access Control Standard        | [csrc.nist.gov/projects/rbac](https://csrc.nist.gov/projects/rbac)                                         |
| **Secure Coding**  | OWASP Secure Coding Practices                  | [owasp.org/www-project-secure-coding-practices/](https://owasp.org/www-project-secure-coding-practices/)   |
| **GitHub Actions** | Automate your workflow from idea to production | [docs.github.com/en/actions](https://docs.github.com/en/actions)                                           |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
