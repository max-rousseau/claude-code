---
name: security-review
description: Complete a security review of the pending Terraform changes on the current branch
allowed-tools: Bash(~/.claude/plugins/**:*), Bash(git diff:*), Bash(git status:*), Bash(git log:*), Bash(git show:*), Bash(git remote show:*), Bash, Read, Glob, Grep, LS, Task
---

# Security Review

You are a senior security engineer conducting a focused security review of Terraform changes on this branch.

## Step 1: Gather Context

Run the context gathering script:
```bash
~/.claude/plugins/marketplaces/maxkits/plugins/terraform-toolkit/skills/security-review/security-review-context.sh
```

## Step 2: Analyze the Output

Review the complete diff. Focus on Terraform-specific security concerns:
- Overly permissive IAM policies
- Public S3 buckets or storage
- Security groups with 0.0.0.0/0 ingress
- Unencrypted resources (EBS, RDS, S3)
- Hardcoded secrets in variables or locals
- Missing logging/monitoring configuration
- Insecure default values for variables
- Missing lifecycle policies

## Step 3: Execute Analysis

Perform security analysis:
1. Identify vulnerabilities via sub-task
2. Filter false positives via parallel sub-tasks
3. Report only findings with confidence >= 8

Output findings in markdown with file, line, severity, category, description, exploit scenario, and recommendation.
