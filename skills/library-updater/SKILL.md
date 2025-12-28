---
name: library-updater
description: Upgrade Python project dependencies (libraries) to latest versions. Use when the user wants to update, upgrade, or refresh their project dependencies or libraries.
allowed-tools: Bash
---

# Library Updater

Upgrades all dependencies in pyproject.toml to their latest versions.

## Execution

```bash
./.venv/bin/python ~/.claude/skills/library-updater/library-updater.py
```

## Post-Upgrade Tasks

1. Review output for failed upgrades
2. Run tests to verify compatibility
3. Update version constraints in pyproject.toml
4. Test installing the sections from pyproject.toml after updating, e.g.: `./.venv/bin/pip install -e .`