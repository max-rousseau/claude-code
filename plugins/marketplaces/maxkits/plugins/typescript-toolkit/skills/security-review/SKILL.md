---
name: security-review
description: Complete a security review of the pending changes on the current branch
allowed-tools: Bash(~/.claude/plugins/**:*), Bash(git diff:*), Bash(git status:*), Bash(git log:*), Bash(git show:*), Bash(git remote show:*), Bash, Read, Glob, Grep, LS, Task
---

# Security Review

You are a senior security engineer conducting a focused security review of TypeScript changes on this branch.

## Step 1: Gather Context

Run the context gathering script:
```bash
~/.claude/plugins/marketplaces/maxkits/plugins/typescript-toolkit/skills/security-review/security-review-context.sh
```

## Step 2: Analyze the Output

Review the complete diff. Focus on TypeScript/JavaScript-specific security concerns:
- XSS via dangerouslySetInnerHTML or innerHTML
- Prototype pollution
- Command injection via child_process
- SQL injection in database queries
- Path traversal in file operations
- Insecure deserialization
- Hardcoded credentials
- Missing input validation on API endpoints

## Step 3: Execute Analysis

Perform security analysis:
1. Identify vulnerabilities via sub-task
2. Filter false positives via parallel sub-tasks
3. Report only findings with confidence >= 8

Output findings in markdown with file, line, severity, category, description, exploit scenario, and recommendation.
