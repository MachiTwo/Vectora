.PHONY: help build install build-all build-integrations build-vscode build-gemini test lint run clean docker-build k8s-deploy

# Configuration
BINARY_NAME=vectora
GEMINI_CLI_NAME=gemini-cli
BIN_DIR=bin
VERSION?=0.1.0
COMMIT=$(shell git rev-parse --short HEAD 2>/dev/null || echo "unknown")
DATE=$(shell date -u +'%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "unknown")

# OS Detection for proper binary extension
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    OS=linux
    EXT=
    OUT=$(BIN_DIR)/$(BINARY_NAME)
endif
ifeq ($(UNAME_S),Darwin)
    OS=macos
    EXT=
    OUT=$(BIN_DIR)/$(BINARY_NAME)
endif
ifeq ($(OS),)
    OS=windows
    EXT=.exe
    OUT=$(BIN_DIR)/$(BINARY_NAME).exe
endif

# LDFLAGS for versioning
LDFLAGS=-ldflags="-s -w -X github.com/Kaffyn/Vectora/internal/config.Version=$(VERSION) -X github.com/Kaffyn/Vectora/internal/config.Commit=$(COMMIT) -X github.com/Kaffyn/Vectora/internal/config.Date=$(DATE)"

help:
	@echo "Vectora Master Build System"
	@echo ""
	@echo "Main Targets:"
	@echo "  make build           - Build core vectora binary for $(OS)"
	@echo "  make build-all       - Build core + all integrations (Gemini, VSCode, etc)"
	@echo "  make build-vscode    - Build VSCode extension (.vsix)"
	@echo "  make build-gemini    - Build Gemini CLI binary"
	@echo "  make test            - Run core tests"
	@echo "  make clean           - Remove all binaries and artifacts"

build: install

install: clean
	@echo "Building $(BINARY_NAME) core for $(OS)..."
	@mkdir -p $(BIN_DIR)
	go build $(LDFLAGS) -o $(OUT) ./cmd/vectora
	@echo "✓ Core binary: $(OUT)"

build-all: install build-integrations
	@echo "🚀 Full Vectora ecosystem built successfully!"

build-integrations: build-gemini build-vscode

build-gemini:
	@echo "Building Gemini CLI..."
	@mkdir -p $(BIN_DIR)
	cd integrations/gemini && go build -o ../../$(BIN_DIR)/$(GEMINI_CLI_NAME)$(EXT) ./cmd/gemini-cli
	@echo "✓ Gemini CLI binary: $(BIN_DIR)/$(GEMINI_CLI_NAME)$(EXT)"

build-vscode:
	@echo "Building VSCode Extension UI (Vite)..."
	cd integrations/vscode && npm install && npm run build
	@echo "Packaging VSCode Extension (.vsix)..."
	cd integrations/vscode && npx @vscode/vsce package -o ../../$(BIN_DIR)/vectora-$(VERSION).vsix
	@echo "✓ VSCode Extension: $(BIN_DIR)/vectora-$(VERSION).vsix"

test:
	@echo "Running core tests..."
	go test -v ./...

lint:
	go fmt ./...
	go vet ./...

run:
	go run ./cmd/vectora server

clean:
	@echo "Cleaning up all artifacts..."
	@rm -rf $(BIN_DIR)
	@rm -f $(BINARY_NAME)
	@echo "Clean complete"
