# VAL -Vectora Asset Library (Registry de Datasets)

VAL é um registry público de datasets vetorizados para Vectora, semelhante a npm registry para packages. Comunidade contribui datasets (documentação, code samples, etc), que são validados, indexados, e disponibilizados para instalação via `vectora dataset install`. Cada dataset é um package com vectors.lance (LanceDB format), metadata.json, documentação, e exemplos. Hosted em GitHub com releases para distribution.

## Stack

VAL é puramente GitHub nativo: repositories como storage, releases como artifact distribution, GitHub Actions para validation. Nenhuma infra extra. Validação é Go script (checksum, structure validation). Index é um simples JSON file (index.json) que cataloga todos os datasets. REST API é served via GitHub raw content. Community contribui via pull requests + GitHub Discussions.

- Repository: GitHub (public)
- Storage: GitHub Releases (artifacts)
- Index: JSON file (index.json in repo)
- Validation: Go script (validate-dataset.go)
- Distribution: GitHub raw content CDN
- Community: GitHub Discussions + Issues
- License: Apache 2.0

## Mapa Mental

Workflow: developer cria dataset (docs + embeddings) -> commits to vectora-asset-library repo -> runs validation CI -> generates index -> pushes release -> dataset available on registry. User installs via `vectora dataset install godot-4.6-docs` -> CLI downloads from GitHub release -> extracts vectors.lance + metadata -> indexed in LanceDB.

```
Developer creates dataset
    |
    +-- docs/*.md
    +-- vectors.lance (LanceDB format)
    +-- metadata.json
    +-- examples/
    |
    V
Git push to vectora-asset-library
    |
    V
GitHub Actions CI
    |
    +-- Validate structure
    +-- Check checksums
    +-- Generate metadata
    +-- Update index.json
    |
    V
Create GitHub Release
    |
    +-- Upload vectors.lance + metadata.json
    +-- Tag v1.0.0
    |
    V
Registry available: registry.vectora.ai
    |
    V
User: vectora dataset install godot-4.6-docs
    |
    +-- CLI downloads from GitHub release
    +-- Extracts to ~/.vectora/datasets/
    +-- Registers in LanceDB
    |
    V
User can now query godot docs via Vectora
```

## Estrutura

Root repository com datasets/ folder contendo cada dataset como subfolder. index.json na root cataloga tudo. .github/workflows/ roda validation e auto-indexing. README documenta como contribuir.

```
vectora-asset-library/
├── datasets/                                (Dataset packages)
│   ├── godot-4.6-docs/
│   │   ├── vectors.lance                    (LanceDB format)
│   │   ├── metadata.json
│   │   │   ├── name: "godot-4.6-docs"
│   │   │   ├── version: "4.6.1"
│   │   │   ├── description: "Official Godot Engine 4.6 documentation"
│   │   │   ├── vectors_count: 10000
│   │   │   ├── size_mb: 500
│   │   │   ├── checksum: "sha256:abc123..."
│   │   │   ├── created_at: "2026-05-01T00:00:00Z"
│   │   │   ├── tags: ["godot", "game-dev", "documentation"]
│   │   │   └── author: "Godot Foundation"
│   │   ├── README.md
│   │   ├── AGENTS.md                        (System prompt for agents)
│   │   └── examples/
│   │       ├── 01-basic-node.md
│   │       └── 02-signals-connections.md
│   │
│   ├── react-19-docs/
│   │   ├── vectors.lance
│   │   ├── metadata.json
│   │   ├── README.md
│   │   ├── AGENTS.md
│   │   └── examples/
│   │
│   ├── kubernetes-1.30-docs/
│   │   ├── vectors.lance
│   │   ├── metadata.json
│   │   ├── README.md
│   │   ├── AGENTS.md
│   │   └── examples/
│   │
│   └── ... (more datasets)
│
├── index.json                               (Registry catalog)
│   ├── version: "1.0"
│   ├── generated_at: "2026-05-01T12:00:00Z"
│   ├── datasets: [
│   │   {
│   │     "name": "godot-4.6-docs",
│   │     "version": "4.6.1",
│   │     "url": "https://github.com/.../releases/tag/godot-4.6-docs-v1.0.0",
│   │     "description": "...",
│   │     "vectors": 10000,
│   │     "size_mb": 500,
│   │     "checksum": "sha256:abc123...",
│   │     "tags": ["godot", "game-dev"],
│   │     "author": "Godot Foundation",
│   │     "rating": 4.8
│   │   },
│   │   ...
│   │ ]
│   └─ total_datasets: 42
│
├── scripts/
│   ├── validate_dataset.go                  (Validation script)
│   └── generate_index.go                    (Generate index.json)
│
├── .github/
│   └── workflows/
│       ├── validate.yml                     (CI: validate on PR)
│       ├── publish.yml                      (CI: create release on merge)
│       └── index.yml                        (CI: auto-generate index.json)
│
├── CONTRIBUTING.md                          (Guide for contributors)
├── README.md
├── LICENSE (Apache 2.0)
└── .gitignore
```

---

## Contributing a Dataset

1. Fork repository
2. Create folder in datasets/{your-dataset-name}/
3. Add vectors.lance (LanceDB format)
4. Add metadata.json with name, version, description, tags
5. Add README.md with details
6. Add AGENTS.md with system prompt for agents
7. Add examples/ folder with sample queries
8. Create PR
9. CI validates structure + checksums
10. On merge, GitHub Actions creates release + updates index
11. Dataset available on registry

## Installing from VAL

```bash
# List available datasets
vectora dataset list

# Install a dataset
vectora dataset install godot-4.6-docs

# Uninstall
vectora dataset uninstall godot-4.6-docs

# Query via Vectora (automatic after install)
# Dataset vectors indexed in LanceDB, ready to use
```

## API

Registry API (served via GitHub raw content):

```
GET https://registry.vectora.ai/index.json
  Returns full index of all datasets

GET https://registry.vectora.ai/datasets/{name}/metadata.json
  Returns metadata for specific dataset

GET https://github.com/vectora/vectora-asset-library/releases/tag/{dataset-version}
  Download vectors.lance + files
```

## Rating & Feedback

Community rates datasets via GitHub Reactions on PRs. Popular datasets appear first in `vectora dataset list`.

## License

Apache 2.0
