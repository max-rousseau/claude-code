# Claude Code Configuration

Opinionated Claude Code configuration for Python development. Clone this repository to `~/.claude` to get a batteries-included setup with skills, commands, agents, and sensible defaults.

## Quick Start

```bash
# Backup existing config if you have one
mv ~/.claude ~/.claude.bak

# Clone this repository
git clone https://github.com/max-rousseau/claude-code.git ~/.claude
```

Restart Claude Code to pick up the new configuration.

## What's Included

### CLAUDE.md - Global Instructions

The main configuration file that shapes Claude's behavior across all projects:

- **Persona**: Tech priest aesthetic with senior engineer competence
- **Prime Directives**: Simplicity over complexity, code reuse, clean refactoring
- **Coding Standards**: PEP8, type annotations, virtual environment usage
- **Security Standards**: No hardcoded secrets, .env file patterns
- **Heretical Patterns**: Things Claude must never do (silent fallbacks, dead code, etc.)

### settings.json - Permissions & Hooks

Pre-configured permissions and automation:

**Auto-approved Operations:**
- Read/Write/Edit files in projects
- Virtual environment operations (`.venv/bin/python`, `.venv/bin/pip`, `.venv/bin/pytest`)
- Git operations (add, commit, push, pull, checkout)
- GitHub CLI (pr create, pr view)
- Quality tools (black, flake8, bandit, vulture)

**Hooks:**
- `PreToolUse`: Logs all bash commands
- `PostToolUse`: Auto-formats Python files with black after edits
- `Notification`: Desktop notification when Claude awaits input

**Denied Operations:**
- Reading `.env` files (security)
- Running quality tools via `.venv/bin/` (forces use of skills instead)

### Skills (invoke with `/skill-name`)

| Skill | Description |
|-------|-------------|
| `/quality-checks` | Runs black, flake8, and vulture with pyproject.toml config |
| `/security-review` | Security audit of branch changes (bandit + manual review) |
| `/repo-setup` | Installs git hooks and GitHub Actions workflow |
| `/python-pyproject` | Creates/validates pyproject.toml with tool configs |
| `/library-updater` | Upgrades project dependencies to latest versions |

### Commands (invoke with `/command-name`)

| Command | Description |
|---------|-------------|
| `/commit` | Creates thoughtful git commits with version bumps |
| `/ship` | Full deployment pipeline: security, quality, tests, docs, PR |
| `/merge` | Creates pull request with proper description |
| `/main` | Returns to main branch and pulls latest |
| `/quality` | Runs quality review and fixes issues |

### Specialized Agents

Sub-agents Claude delegates to for specific tasks:

| Agent | Purpose |
|-------|---------|
| `python-pytest-agent` | Test creation, isolation fixes, coverage improvements |
| `python-debug-specialist` | Complex issue analysis and troubleshooting |
| `python-code-reviewer` | Code quality review and style fixes |
| `python-git-commit` | Commit message creation and git workflow |
| `python-docs-generator` | Docstrings, headers, README generation |
| `python-refactor-specialist` | Code restructuring and architecture improvements |

### Supporting Docs

- `docs/coding-standards.md` - Python coding conventions
- `docs/tool-use-guidelines.md` - When to use which Claude tool
- `docs/claude_code.md` - Reference documentation

## Directory Structure

```
~/.claude/
├── CLAUDE.md              # Main instructions (loaded globally)
├── settings.json          # Permissions, hooks, statusline config
├── agents/                # Sub-agent definitions
├── commands/              # Slash command definitions
├── skills/                # Skill definitions with scripts
├── docs/                  # Reference documentation
└── scripts/               # Helper scripts (statusline, permission checks)
```

## Requirements

- Claude Code CLI
- macOS or Linux (no Windows support)
- Git
- GitHub CLI (`gh`) for PR operations
- Python 3.x with virtual environment support
