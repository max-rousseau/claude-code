---
name: repo-setup
description: Set up repository with opinionated quality guardrails (git hooks, GitHub Actions). Run after creating pyproject.toml with /python-pyproject.
allowed-tools: Bash(python3:*), Bash(git config:*)
---

# Repository Setup

Sets up opinionated quality guardrails for Python repositories:
- Git hooks (pre-commit, pre-push) in `scripts/hooks/`
- GitHub Actions workflow in `.github/workflows/quality.yml`
- Verifies local pipx tools are installed

## Prerequisites

1. Repository must have `pyproject.toml` with tool sections configured
2. Run `/python-pyproject` first if pyproject.toml is missing or incomplete

## Execution

```bash
python3 ~/.claude/skills/repo-setup/setup.py
```

## What Gets Created

### Git Hooks (`scripts/hooks/`)

**pre-commit** (fast, every commit):
- `black --check` - formatting check
- `flake8` - style violations

**pre-push** (thorough, before push):
- `bandit` - security scan
- `vulture` - dead code detection
- `pytest` - test execution

### GitHub Actions (`.github/workflows/quality.yml`)

Mirrors the same checks as git hooks, runs on:
- Push to main/master
- Pull requests to main/master

## Configuration Source

All tools read their configuration from `pyproject.toml`:
- `[tool.black]`
- `[tool.flake8]` (requires flake8-pyproject)
- `[tool.bandit]`
- `[tool.vulture]`
- `[tool.pytest.ini_options]`

See [pyproject-template.toml](../python-pyproject/pyproject-template.toml) for reference.
