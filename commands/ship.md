---
description: Full pre-deployment pipeline - security, quality, tests, docs, commit, PR creation, CI/CD pipeline monitoring, and post-merge cleanup.
---

# CONTEXT

- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

# SHIP COMMAND - Full Pre-Deployment Pipeline

You are orchestrating the complete ship process. This is a sequential pipeline where each phase must complete successfully before proceeding to the next.

## PHASE 1: Code Quality Gates

Execute these skills IN ORDER. After each skill completes, resolve ALL issues before proceeding to the next. Do not skip or defer issues.

### Step 1.1: Pyproject Validation
Invoke the `python-pyproject` skill FIRST.
- Validate pyproject.toml structure
- Ensure all tool configurations are correct ([tool.black], [tool.flake8], etc.)
- Verify dependencies are properly specified
- Quality tools depend on this configuration being correct

### Step 1.2: Security Assessment
Invoke the `security-review` skill.
- If vulnerabilities are found, FIX THEM before proceeding
- Re-run security review until clean

### Step 1.3: Quality Checks
Invoke the `quality-checks` skill.
- If issues are found (black formatting, flake8 errors, dead code), FIX THEM before proceeding
- Re-run quality checks until clean

### Step 1.4: Library Updates
Invoke the `library-updater` skill.
- If updates are available, apply them
- Ensure dependencies install cleanly

**GATE CHECK**: All Phase 1 steps must pass cleanly before proceeding.

## PHASE 2: Testing

Launch the `python-pytest-agent` sub-agent to:
- Run all tests
- Ensure coverage is adequate
- Fix any failing tests
- Address test quality issues

**GATE CHECK**: All tests must pass before proceeding.

## PHASE 3: Documentation

Launch the `python-docs-generator` sub-agent to:
- Update/generate docstrings
- Ensure file headers are present
- Update README if needed

**GATE CHECK**: Documentation must be complete before proceeding.

## PHASE 4: Git Commit

Launch the `python-git-commit` sub-agent to:
- Review all changes made during this pipeline
- Create thoughtful, professional commit(s)
- Ensure version bump in pyproject.toml is appropriate

**GATE CHECK**: All changes must be committed before proceeding.

## PHASE 5: Pull Request Creation

Follow the merge process:
1. Ensure we are on a non-protected branch (not main/master). If on a protected branch, create a new feature/bugfix/refactor branch as appropriate.
2. Ensure the local branch is clean (all code committed)
3. Review all commits and create a professional Pull Request description
4. Push commits to origin
5. Create the pull request using `gh pr create`
6. Provide the user with the pull request URI

**GATE CHECK**: PR must be created before proceeding.

## PHASE 6: Pipeline Monitoring & Remediation

After the PR is created, monitor CI/CD pipelines until successful:

### Step 6.1: Check for Running Pipelines
```bash
gh pr checks --watch
```

Or poll status with:
```bash
gh pr checks
```

### Step 6.2: Wait for Pipeline Completion
- Monitor pipeline status periodically
- Use `gh pr checks` to view current status
- Wait until all checks complete (success or failure)

### Step 6.3: Handle Pipeline Failures
If any pipeline fails:
1. Investigate the failure using `gh pr checks --json name,state,conclusion,description`
2. View detailed logs: `gh run view <run-id> --log-failed`
3. Identify the root cause
4. Fix the issue in the codebase
5. Commit the fix (use `python-git-commit` sub-agent)
6. Push the updated code: `git push`
7. Return to Step 6.1 and repeat until all pipelines pass

### Step 6.4: Confirm Success
Once all pipelines pass:
1. Verify with `gh pr checks` showing all green
2. Report final status to user
3. Note: Repository uses squash commit merges by default

**GATE CHECK**: All CI/CD pipelines must pass before proceeding.

## PHASE 7: Post-Merge Cleanup

Once the user has merged the PR, return the repository to a clean state:

### Step 7.1: Wait for User Merge
- Inform the user that all pipelines have passed
- Wait for the user to merge the PR (do not auto-merge)
- Poll PR status to detect when merge occurs:
```bash
gh pr view --json state,mergedAt --jq '.state + " mergedAt:" + (.mergedAt // "null")'
```

### Step 7.2: Return to Main Branch
Once merged:
1. Fetch latest changes: `git fetch origin`
2. Checkout main branch: `git checkout main`
3. Pull latest: `git pull origin main`

### Step 7.3: Cleanup Feature Branch
1. Identify the feature branch that was just merged
2. Delete the local feature branch: `git branch -d <branch-name>`
3. Verify cleanup: `git branch` (should only show main)

### Step 7.4: Final Confirmation
1. Confirm repository is on main branch
2. Confirm working directory is clean
3. Report to user: repository is current and ready for new work

**SHIP COMPLETE**: Repository is clean and ready for the next feature.

## GH CLI REFERENCE

**CRITICAL**: When querying PR state via `gh pr view --json`, use the correct field names:

| Correct Field | WRONG (does not exist) | Purpose |
|---------------|------------------------|---------|
| `mergedAt` | ~~`merged`~~ | Check if PR was merged (null = not merged) |
| `state` | - | PR state: OPEN, CLOSED, MERGED |
| `mergeStateStatus` | - | Merge readiness status |

Example - check if PR is merged:
```bash
gh pr view <PR_NUMBER> --json state,mergedAt --jq '.state + " mergedAt:" + (.mergedAt // "null")'
```

## EXECUTION NOTES

- Each phase is a hard gate - do not proceed if issues remain
- If a phase fails repeatedly, stop and ask the user for guidance
- Use the TodoWrite tool to track progress through each phase
- Report status after each phase completion
- This process may take several iterations - that is expected
