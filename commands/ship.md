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
6. Report the pull request URI to the user

**GATE CHECK**: PR must be created before proceeding.

## PHASE 6: Pipeline Monitoring & Remediation

After PR creation, monitor CI/CD pipelines by polling until all checks complete.

### Step 6.1: Poll Pipeline Status

Poll every 30 seconds until all checks resolve:

```bash
gh pr checks --json name,state,conclusion
```

**State transitions:**
- `state: "pending"` or `"in_progress"` → `sleep 30`, poll again
- All `conclusion: "success"` → Proceed to Phase 7
- Any `conclusion: "failure"` → Step 6.2

### Step 6.2: Handle Pipeline Failures

1. Get failure details:
   ```bash
   gh run list --branch $(git branch --show-current) --json databaseId,conclusion --jq '.[] | select(.conclusion == "failure")'
   gh run view <run-id> --log-failed
   ```
2. Fix the issue, commit (use `python-git-commit` sub-agent), and push
3. Return to Step 6.1 (pipelines restart automatically)

**GATE CHECK**: All pipelines must pass before proceeding.

## PHASE 7: Post-Merge Cleanup

After pipelines pass, notify the user the PR is ready for merge, then poll for merge completion.

### Step 7.1: Poll Merge Status

Store the feature branch name, then poll every 30 seconds:

```bash
FEATURE_BRANCH=$(git branch --show-current)
gh pr view --json state,mergedAt --jq '{state: .state, merged: (.mergedAt != null)}'
```

**State transitions:**
- `state: "OPEN"` → `sleep 30`, poll again
- `state: "MERGED"` or `merged: true` → Step 7.2
- `state: "CLOSED"` with `merged: false` → PR closed without merge; notify user and stop

### Step 7.2: Cleanup

Once merged:
```bash
git fetch origin && git checkout main && git pull origin main
git branch -d $FEATURE_BRANCH
```

Confirm repository is on main and working directory is clean.

**SHIP COMPLETE**: Repository is ready for the next feature.

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
- If a phase fails repeatedly (3+ attempts), ask the user for guidance
- Use the TodoWrite tool to track progress through each phase
- Report status after each phase completion

### Polling Behavior
- Phases 6 and 7 use polling loops - continue through them without waiting for user input
- Polling interval: 30 seconds
- Timeout: 60 polls (30 minutes) - if reached, ask user for guidance
