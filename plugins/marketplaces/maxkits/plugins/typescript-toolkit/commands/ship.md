---
description: Full pre-deployment pipeline for TypeScript - security, quality, tests, commit, PR creation, CI/CD monitoring, and post-merge cleanup.
---

# CONTEXT

- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

# SHIP COMMAND - TypeScript Pre-Deployment Pipeline

You are orchestrating the complete ship process for a TypeScript project. This is a sequential pipeline where each phase must complete successfully before proceeding.

This pipeline runs autonomously. Do not stop for user confirmation between phases.

## PHASE 1: Code Quality Gates

### Step 1.1: Security Assessment
Invoke the `security-review` skill.
- If vulnerabilities are found, FIX THEM before proceeding

### Step 1.2: Quality Checks
Invoke the `quality-checks` skill.
- If issues are found, FIX THEM before proceeding
- Re-run until clean

**GATE CHECK**: All Phase 1 steps must pass cleanly.

## PHASE 2: Testing

Run the test suite:
```bash
npm test
```
- Ensure all tests pass
- Fix any failing tests

**GATE CHECK**: All tests must pass.

## PHASE 3: Git Commit

- Review all changes made during this pipeline
- Create thoughtful, professional commit(s)
- Follow conventional commit format

**GATE CHECK**: All changes must be committed.

## PHASE 4: Pull Request Creation

1. Ensure we are on a non-protected branch
2. Ensure the local branch is clean
3. Create a professional Pull Request description
4. Push commits to origin
5. Create the pull request using `gh pr create`
6. Report the pull request URI

**GATE CHECK**: PR must be created.

## PHASE 5: Pipeline Monitoring & Remediation

Poll every 30 seconds until all checks resolve:
```bash
gh pr checks --json name,state,conclusion
```

If failures occur, get details with `gh run view <id> --log-failed`, fix, commit, push.

## PHASE 6: Post-Merge Cleanup

Notify user PR is ready for merge, then poll for merge completion. Once merged:
```bash
git fetch origin && git checkout main && git pull origin main
git branch -d $FEATURE_BRANCH
```

## EXECUTION NOTES

- Run all phases continuously without stopping for confirmation
- Each phase is a hard gate
- If a phase fails 3+ times, ask the user for guidance
- Polling interval: 30 seconds, timeout: 60 polls
