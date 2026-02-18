---
name: quality-checks
description: Run Terraform code quality tools (terraform fmt, tflint) and fix issues found.
allowed-tools: Bash, Read, Glob, Grep, Edit, Write, Task, Skill
---

# Quality Checks

Runs Terraform code quality tools and fixes issues found.

## Step 0: Verify Prerequisites

Before running quality checks, verify:
1. `.tf` files exist in the project
2. Terraform CLI is installed: `terraform version`
3. Check if `tflint` is installed: `which tflint`

## Step 1: Run Quality Checks

Execute the quality checks script:
```bash
~/.claude/plugins/marketplaces/maxkits/plugins/terraform-toolkit/skills/quality-checks/quality-checks.sh
```

This will output:
- TERRAFORM FMT: Formatting check results
- TERRAFORM VALIDATE: Configuration validation
- TFLINT: Lint results (if installed)

## Step 2: Analyze and Fix Issues

### TERRAFORM FMT
- Auto-fix with `terraform fmt -recursive`
- Review any files that were modified

### TERRAFORM VALIDATE
- Fix any configuration errors
- Ensure all required variables are defined

### TFLINT (if available)
- Address flagged issues
- Focus on deprecated syntax, best practices

## Step 3: Fix Issues

Using the `tf-code-reviewer` sub-agent, fix any issues identified.

## Step 4: Completion

Upon completion of corrections, re-invoke the `quality-checks` skill to verify all issues are resolved.
