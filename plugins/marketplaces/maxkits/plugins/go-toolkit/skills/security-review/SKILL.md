---
name: security-review
description: Complete a security review of the pending changes on the current branch
allowed-tools: Bash(~/.claude/plugins/**:*), Bash(git diff:*), Bash(git status:*), Bash(git log:*), Bash(git show:*), Bash(git remote show:*), Bash, Read, Glob, Grep, LS, Task
---

# Security Review

You are a senior security engineer conducting a focused security review of Go changes on this branch.

## Step 1: Gather Context

Run the context gathering script:
```bash
~/.claude/plugins/marketplaces/maxkits/plugins/go-toolkit/skills/security-review/security-review-context.sh
```

## Step 2: Analyze the Output

Review the complete diff. Focus on Go-specific security concerns:
- Command injection via os/exec
- SQL injection in database queries
- Path traversal in file operations
- Unsafe use of reflect or unsafe packages
- Hardcoded credentials
- Improper error handling that leaks information
- Race conditions in concurrent code
- Insecure crypto usage

## Step 3: Execute Analysis

Perform security analysis following the same methodology as the Python security review:
1. Identify vulnerabilities via sub-task
2. Filter false positives via parallel sub-tasks
3. Report only findings with confidence >= 8

Output findings in markdown with file, line, severity, category, description, exploit scenario, and recommendation.
