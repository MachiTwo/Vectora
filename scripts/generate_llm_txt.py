#!/usr/bin/env python3
"""
Generate llm.txt - LLM context file for Vectora project.
Auto-generates documentation about the project for AI assistants.
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path


def get_git_info():
    """Get git version and commit info."""
    try:
        version = subprocess.check_output(
            ["git", "describe", "--tags", "--always"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        version = "0.1.0"

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        commit = "unknown"

    return version, commit


def read_go_mod(path):
    """Parse go.mod to extract key dependencies."""
    try:
        with open(path, "r") as f:
            content = f.read()
            deps = []
            in_require = False
            for line in content.split("\n"):
                if line.startswith("require ("):
                    in_require = True
                    continue
                if in_require and line.strip() == ")":
                    break
                if in_require and line.strip() and not line.startswith("//"):
                    parts = line.split()
                    if len(parts) >= 2:
                        deps.append(f"- {parts[0]} {parts[1]}")
            return deps
    except Exception:
        return []


def count_files(pattern):
    """Count files matching pattern."""
    try:
        result = subprocess.check_output(
            ["find", ".", "-type", "f", "-name", pattern],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return len([line for line in result.split("\n") if line])
    except Exception:
        return 0


def generate_llm_txt():
    """Generate llm.txt content."""
    version, commit = get_git_info()

    # Count code files
    go_files = count_files("*.go")
    py_files = count_files("*.py")
    ts_files = count_files("*.ts")
    md_files = count_files("*.md")

    # Get dependencies
    cloud_deps = read_go_mod("cloud/go.mod")
    desktop_deps = read_go_mod("desktop/go.mod")

    content = f"""# Vectora

> Human control plane for AI-powered code orchestration and decision engines.

Vectora is an open-source platform that coordinates AI agents across code analysis, execution, and decision-making. Built with Go, Python, and TypeScript, it provides a unified interface for multi-LLM systems with built-in security, caching, and observability.

## Getting Started

GitHub: https://github.com/Kaffyn/Vectora

Build Vectora using the unified Task-based system:

```bash
# Install Task (cross-platform build tool)
# https://taskfile.dev/installation

# Build all components
task all

# Clean artifacts
task clean

# Run tests
task test:all
```

One-command setup with Task handles Desktop, Cloud, Vectora Cognitive Runtime, Integrations, Dashboard, and Docs.

## Architecture

Vectora consists of 6 tightly integrated components:

1. **Desktop (Go CLI)** - Local machine interface
   - System tray UI (Windows)
   - CLI commands (Cobra)
   - Local code analysis
   - Safe execution (Guardian + SafeFramework)

2. **Cloud (Go Server)** - Microservice API
   - HTTP (Chi router) + gRPC
   - JWT + API Key auth (custom implementation)
   - MongoDB persistence
   - OpenTelemetry tracing and metrics
   - Badger caching

3. **Vectora Cognitive Runtime (Python FastAPI)** - Vector/Decision Engine
   - ONNX model inference (SmolLM2-135M INT4 quantized)
   - Policy orchestration
   - MongoDB storage

4. **Integrations (Bun TypeScript)** - LLM & Tool Adapters
   - ChatGPT Plugin
   - VSCode Extension
   - Claude MCP Server
   - Codex wrapper
   - Gemini CLI
   - OpenAI Codex
   - Paperclip orchestration

5. **Dashboard (Next.js + React 19)** - Web Management UI
   - User accounts (NextAuth.js OAuth2)
   - Billing (Stripe + ASAAS + Google Pay)
   - Usage analytics (gRPC streaming)
   - Integration management
   - Deploy to: Vercel

6. **Documentation (Hugo)** - Static site
   - API reference
   - Architecture diagrams
   - Setup guides
   - Multi-language (PT-BR + EN)

## Build Output Structure

All components consolidate to a unified `bin/` directory:

```
bin/
├── vectora                    # Desktop CLI
├── vectora-cloud              # Cloud Server
├── models/
│   └── vectora-cognitive-runtime.onnx               # ONNX model (35MB, INT4 quantized)
├── servers/
│   ├── main.py (FastAPI)
│   ├── inference.py
│   └── requirements.txt
├── integrations/
│   ├── chatgpt/
│   ├── vscode/
│   ├── claude-mcp/
│   └── ...
├── dashboard/
│   └── .next/                 # Next.js build
└── docs/
    └── public/                # Hugo output
```

## Technology Stack

### Cloud
{chr(10).join(cloud_deps[:10])}

### Desktop
{chr(10).join(desktop_deps[:10])}

### Key Libraries
- **HTTP**: Chi v5 (both)
- **RPC**: gRPC + Protocol Buffers
- **Database**: MongoDB (v1 or v2, consolidating)
- **Cache**: Badger v3
- **Auth**: Custom JWT (cloud/pkg/auth/)
- **Logging**: slog (structured, JSON output)
- **Testing**: Testify (assertions + mocks)
- **Observability**: OpenTelemetry (tracing, metrics)

## Code Statistics

- Go files: {go_files}
- Python files: {py_files}
- TypeScript files: {ts_files}
- Documentation: {md_files} markdown files

## Current Status

**Version:** {version}
**Commit:** {commit}
**Generated:** {datetime.now().isoformat()}

### Build System
- ✅ Taskfile.yml (unified, cross-platform)
- ✅ Task v3.35.1 installed
- ✅ All 6 components buildable
- ✅ Consolidated bin/ output

### Components
- ✅ Desktop (Go CLI + system tray)
- ✅ Cloud (Go HTTP + gRPC server)
- ⏳ Vectora Cognitive Runtime (Python - inference mock, needs real ONNX)
- ✅ Integrations (TypeScript packages)
- ✅ Dashboard (Next.js - auth + billing pending)
- ✅ Docs (Hugo static site)

### Known Issues
- MongoDB version mismatch (v1 in Desktop, v2 in Cloud)
- Auth middleware TODO (Phase 4)
- Vectora Cognitive Runtime using mock inference instead of real ONNX
- Config validation missing
- No GoMock for test mocking

## Project Structure

```
Vectora/
├── cloud/                      # Cloud server (Go)
│   ├── cmd/vectora-cloud/
│   ├── internal/
│   │   ├── api/               # HTTP server + gRPC
│   │   ├── auth/              # JWT + API Key auth
│   │   ├── config/            # Configuration
│   │   ├── cache/             # Badger caching
│   │   └── telemetry/         # OpenTelemetry
│   └── pkg/
│       ├── auth/              # Authentication
│       └── mcp/               # MCP integration
│
├── desktop/                    # Desktop CLI (Go)
│   ├── cmd/vectora/           # Main entry point
│   ├── internal/
│   │   ├── cli/               # CLI commands
│   │   ├── server/            # HTTP server
│   │   ├── storage/           # MongoDB + Memory DB
│   │   ├── tray/              # Windows system tray
│   │   ├── engine/            # Search engine
│   │   ├── guardian/          # Path validation
│   │   └── agentic-framework/ # Safe agent execution
│   └── pkg/
│       ├── provider/          # LLM providers (Gemini, Voyage)
│       └── mcp/               # MCP tools
│
├── vectora-cognitive-runtime/                        # Vector Decision Engine (Python)
│   ├── server/                # FastAPI server
│   ├── models/                # ONNX models
│   ├── release/               # Metadata + checksums
│   └── tests/
│
├── integrations/               # Adapters (Bun/TypeScript)
│   └── packages/
│       ├── shared/            # Common utilities
│       ├── chatgpt-plugin/
│       ├── vscode-extension/
│       ├── claude-mcp/
│       ├── codex/
│       ├── gemini/
│       ├── openai-codex/
│       └── paperclip/
│
├── dashboard/                  # Web UI (Next.js)
│   ├── app/                    # App router
│   ├── components/
│   ├── lib/                    # Utilities
│   └── public/
│
├── docs/                       # Documentation (Hugo)
│   ├── content/
│   ├── themes/hextra/
│   └── config.toml
│
├── Taskfile.yml                # Build orchestration
├── BUILD.md                    # Build documentation
└── llm.txt                     # This file (auto-generated)
```

## Build Commands

```bash
# Build everything
task all

# Component-specific
task build:desktop             # Desktop CLI
task build:cloud               # Cloud server
task build:vectora-cognitive-runtime                 # Vectora Cognitive Runtime + copy ONNX
task build:integrations        # TypeScript packages
task build:dashboard           # Next.js
task build:docs                # Hugo

# Testing
task test:all                  # Run all tests
task test:desktop
task test:cloud
task test:vectora-cognitive-runtime
task test:integrations
task test:dashboard

# Linting
task lint:all                  # All linters
task lint:desktop
task lint:cloud
task lint:integrations

# CI/CD
task check                     # Strict mode (lint + test + build)

# Development
task dev:desktop               # Dev mode with hot reload
task dev:cloud
task dev:dashboard
task dev:docs

# Cleanup
task clean                     # Remove all artifacts
```

## Security & Observability

- **Auth**: JWT tokens with custom validation (TODO: implement validation)
- **Paths**: Guardian validates all file access (Desktop)
- **Execution**: SafeFramework sandboxes agent execution
- **Caching**: Badger for local caching layer
- **Tracing**: OpenTelemetry (Cloud only, Desktop pending)
- **Metrics**: Prometheus format (Cloud only)
- **Logging**: Structured JSON logs via slog

## What Vectora Is

- A distributed AI agent orchestration platform
- A multi-component system (CLI + Server + Engine + Integrations)
- An open-source, self-hosted alternative to enterprise AI platforms
- Built for developers who want full control over LLM workflows

## What Changes With Vectora

Without Vectora, you manage multiple AI tool integrations separately, lose context across agents, manually track execution, and risk runaway token costs.

With Vectora, agents are coordinated through a unified control plane, context flows automatically across components, execution is traced and sandboxed, costs are tracked per integration, and you get full observability.

## Deployment

- **Desktop**: Distribute `bin/vectora` binary
- **Cloud**: Deploy to Fly.io (Go binary + gRPC)
- **Vectora Cognitive Runtime**: Python FastAPI on any server
- **Dashboard**: Deploy to Vercel
- **Docs**: Publish to GitHub Pages

## Links

- GitHub: https://github.com/Kaffyn/Vectora
- Build System: Task (https://taskfile.dev)
- Status: {version} ({commit})
- Build Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}

---

Generated by `generate_llm_txt.py` - Run anytime to regenerate with current project state.
"""

    return content


def main():
    """Main entry point."""
    try:
        # Change to project root
        project_root = Path(__file__).parent
        os.chdir(project_root)

        # Generate content
        content = generate_llm_txt()

        # Write to llm.txt
        llm_path = project_root / "llm.txt"
        with open(llm_path, "w", encoding="utf-8") as f:
            f.write(content)

        print("[OK] Generated llm.txt ({} bytes)".format(len(content)))
        print("     Location: {}".format(llm_path))

    except Exception as e:
        print("[ERROR] {}".format(e))
        exit(1)


if __name__ == "__main__":
    main()
