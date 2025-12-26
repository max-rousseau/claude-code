---
name: quality-checks
description: Run code quality tools (black, flake8, vulture) and fix issues found.
allowed-tools: Bash, Read, Glob, Grep, Edit, Write, Task, Skill
---

# Quality Checks

Runs code quality tools and fixes issues found.

## Step 0: Verify Prerequisites

Before running quality checks, verify pyproject.toml exists and has proper tool configuration:

1. Check if `pyproject.toml` exists in the project root
2. If missing or incomplete, invoke the `python-pyproject` skill to create/configure it
3. Ensure `[tool.black]`, `[tool.flake8]`, and `[tool.vulture]` sections are present
4. Verify `flake8-pyproject` is in dev dependencies (required for flake8 to read pyproject.toml)

## Step 1: Run Quality Checks

Execute the quality checks script:
```bash
~/.claude/skills/quality-checks/quality-checks.sh
```

This will output:
- BLACK: Code formatting results
- FLAKE8: Style violations
- VULTURE: Dead code analysis

## Step 2: Analyze and Fix Issues

Review the output from each tool:

### BLACK (formatting)
- Automatically reformats code
- Review any files that were modified

### FLAKE8 (style violations)
- Fix all violations except those explicitly ignored in pyproject.toml
- Focus on unused imports, undefined names, complexity issues

### VULTURE (dead code analysis)
- Investigate flagged code to confirm it's actually dead
- Vulture can produce false positives - verify before removing

## Step 3: Fix Issues

Using the `python-code-reviewer` sub-agent, fix any issues identified. THINK HARD, MAKE A PLAN, CREATE A TODO LIST FIRST.

## Step 4: Completion

Upon completion of corrections, re-invoke the `quality-checks` skill to verify all issues are resolved.
