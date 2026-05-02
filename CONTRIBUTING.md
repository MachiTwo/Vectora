# Contributing to Vectora

Thank you for your interest in contributing to Vectora! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Getting Started

### Prerequisites

- Go 1.22 or later
- Git
- Make (optional, but recommended)

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/Kaffyn/Vectora.git
cd Vectora

# Install dependencies
go mod download
go mod tidy

# Build
make build

# Run tests
make test

# Format code
make fmt
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming convention:

- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation
- `refactor/` for refactoring
- `test/` for test improvements

### 2. Make Changes

- Follow Go conventions and best practices
- Write clear, concise code
- Add comments for complex logic
- Keep functions small and focused

### 3. Write Tests

All code should have tests:

```bash
go test -v ./...
go test -v -race ./...
go test -coverprofile=coverage.out ./...
```

Aim for at least 80% code coverage.

### 4. Format and Lint

```bash
make fmt
go vet ./...
golangci-lint run ./...
```

### 5. Commit

```bash
git add .
git commit -m "fix: description of fix

Optional longer explanation of the change.
"
```

Commit message format:

- `fix:` for bug fixes
- `feat:` for new features
- `refactor:` for code refactoring
- `docs:` for documentation
- `test:` for test additions
- `ci:` for CI/CD changes

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a PR on GitHub with:

- Clear title describing the change
- Description of what was changed and why
- Link to any related issues
- Screenshots if UI changes

## Project Structure

```text
internal/
  ├── server/ HTTP MCP server
  ├── cli/ CLI commands (Cobra)
  ├── cache/ Caching layer
  ├── engine/ Search engine
  ├── config/ Configuration
  ├── tray/ Windows system tray
  └── ...

pkg/
  ├── mcp/ MCP protocol (public API)
  ├── provider/ LLM/embedding providers
  ├── i18n/ Localization
  └── ...

cmd/
  └── vectora/ Single unified binary
```

## Key Design Principles

1. **Single Binary**: Vectora compiles to one binary that acts as both server and CLI
2. **Pure Go**: No C dependencies (zero CGO)
3. **Security First**: Path validation, JWT auth, RBAC
4. **Multi-Provider**: Support multiple LLM providers
5. **Hybrid Caching**: L1 (LRU) + L2 (BadgerDB) for performance

## Testing

### Unit Tests

```bash
make test-unit
```

### Integration Tests

```bash
go test -v -run Integration ./...
```

### Coverage Report

```bash
make test-coverage
open coverage.html
```

## Documentation

- Write clear commit messages
- Update relevant markdown files
- Add code comments for complex logic
- Keep README.md current

## Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Add yourself to CONTRIBUTORS.md if first contribution
4. Code review approval required
5. Must pass CI checks before merging

## Code Style

### Go Conventions

- Use `gofmt` for formatting
- Use `go vet` for static analysis
- Follow [Effective Go](https://golang.org/doc/effective_go)
- Use meaningful variable names
- Keep functions under 50 lines when possible

### Comments

- Comments should be English
- Explain the "why", not the "what"
- Only include necessary comments
- Keep comments short and clear

Example:

```go
// checkCache verifies if request is cached.
// Returns early if L1 hit to avoid L2 lookup.
func (c *Cache) checkCache(key string) (interface{}, bool) {
    // ...
}
```

## Release Process

1. Update version in `internal/config/config.go`
2. Update CHANGELOG.md
3. Create tag: `git tag -a v0.1.0 -m "Release v0.1.0"`
4. Push tag: `git push origin v0.1.0`
5. GitHub Actions will build and release automatically

## Performance

- Aim for <100ms latency for common operations
- Monitor memory usage with pprof
- Profile hot paths with benchmarks
- Cache results appropriately

## Security

- Never commit secrets (.env files)
- Use environment variables for sensitive data
- Validate all user inputs
- Follow security best practices
- Report security issues privately to maintainers

## Questions?

- Open an issue for bugs
- Start a discussion for questions
- Check existing issues before creating new ones
- Be descriptive and include reproduction steps

## License

By contributing, you agree that your contributions will be licensed under the same MIT license.

---

**Thank you for contributing to Vectora! **
