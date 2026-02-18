---
name: python-pyproject
description: Manage Python pyproject.toml files. Use when creating new Python projects, adding dependencies, updating dependencies, or configuring Python tools like black, flake8, pytest, bandit, vulture.
---

# Python pyproject.toml Management

## When To Use

- Creating a new Python project
- Adding or updating dependencies
- Configuring code quality tools (black, flake8, bandit, vulture)
- Configuring pytest
- Validating pyproject.toml structure

## Template Reference

See [pyproject-template.toml](pyproject-template.toml) for the standard template.

## Key Rules

### Version Matching

Always use `~=X.Y` (compatible release) unless there's a specific reason:

| Specifier | Meaning | Use When |
|-----------|---------|----------|
| `~=X.Y` | >=X.Y, <X+1.0 | **Default choice** |
| `>=X.Y` | Minimum only | Rare, when upper bound unknown |
| `==X.Y.Z` | Exact | Known compatibility issues only |

### Dependency Sections

- `dependencies` - Production requirements
- `[project.optional-dependencies] dev` - Development tools (testing, linting)

### Adding Dependencies

1. Check latest version: `./.venv/bin/pip index versions <package>`
2. Add with `~=` matching: `"package~=X.Y"`
3. Install: `./.venv/bin/pip install -e ".[dev]"`

### Tool Configuration Sections

All tools must be configured in pyproject.toml (not separate files):

- `[tool.black]` - Formatter
- `[tool.flake8]` - Linter (requires flake8-pyproject)
- `[tool.bandit]` - Security scanner
- `[tool.vulture]` - Dead code detection
- `[tool.pytest.ini_options]` - Test runner
- `[tool.coverage.run]` and `[tool.coverage.report]` - Coverage

## Validation

After any changes:
```bash
# Verify TOML syntax
./.venv/bin/python -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))"

# Verify installable
./.venv/bin/pip install -e ".[dev]"
```

## Common Issues

### flake8 ignores pyproject.toml
Add `flake8-pyproject~=1.2` to dev dependencies.

### pytest-asyncio deprecation warnings
Set `asyncio_mode = "auto"` in `[tool.pytest.ini_options]`.

### Coverage not finding source
Ensure `[tool.coverage.run] source = ["src/project_name"]` matches your actual source directory.
