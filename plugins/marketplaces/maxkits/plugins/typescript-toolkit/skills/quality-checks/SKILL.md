---
name: quality-checks
description: Run TypeScript code quality tools (eslint, prettier) and fix issues found.
allowed-tools: Bash, Read, Glob, Grep, Edit, Write, Task, Skill
---

# Quality Checks

Runs TypeScript code quality tools and fixes issues found.

## Step 0: Verify Prerequisites

Before running quality checks, verify:
1. `package.json` exists in the project root
2. `eslint` and `prettier` are available (check `node_modules/.bin/`)
3. ESLint and Prettier configs exist (`.eslintrc.*`, `.prettierrc.*`, or in `package.json`)

## Step 1: Run Quality Checks

Execute the quality checks script:
```bash
~/.claude/plugins/marketplaces/maxkits/plugins/typescript-toolkit/skills/quality-checks/quality-checks.sh
```

This will output:
- PRETTIER: Code formatting results
- ESLINT: Lint violations

## Step 2: Analyze and Fix Issues

### PRETTIER (formatting)
- Auto-fix with `npx prettier --write .`
- Review any files that were modified

### ESLINT (lint violations)
- Fix auto-fixable issues with `npx eslint --fix .`
- Manually address remaining violations

## Step 3: Fix Issues

Using the `ts-code-reviewer` sub-agent, fix any issues identified.

## Step 4: Completion

Upon completion of corrections, re-invoke the `quality-checks` skill to verify all issues are resolved.
