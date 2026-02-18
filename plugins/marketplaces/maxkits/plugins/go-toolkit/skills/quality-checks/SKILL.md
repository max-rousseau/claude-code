---
name: quality-checks
description: Run Go code quality tools (go vet, staticcheck) and fix issues found.
allowed-tools: Bash, Read, Glob, Grep, Edit, Write, Task, Skill
---

# Quality Checks

Runs Go code quality tools and fixes issues found.

## Step 0: Verify Prerequisites

Before running quality checks, verify:
1. `go.mod` exists in the project root
2. Go toolchain is installed and accessible
3. Check if `staticcheck` is installed: `which staticcheck`

## Step 1: Run Quality Checks

Execute the quality checks script:
```bash
~/.claude/plugins/marketplaces/maxkits/plugins/go-toolkit/skills/quality-checks/quality-checks.sh
```

This will output:
- GO VET: Code correctness issues
- STATICCHECK: Static analysis results (if installed)

## Step 2: Analyze and Fix Issues

Review the output from each tool:

### GO VET
- Suspicious constructs, unreachable code, shadowed variables
- Fix all issues reported

### STATICCHECK (if available)
- Additional static analysis beyond go vet
- Fix all flagged issues

## Step 3: Fix Issues

Using the `go-code-reviewer` sub-agent, fix any issues identified.

## Step 4: Completion

Upon completion of corrections, re-invoke the `quality-checks` skill to verify all issues are resolved.
