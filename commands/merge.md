---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git log:*), Bash(git diff:*), Bash(git branch:*)
description: Create the pull request for the new code.
---

# CONTEXT

- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

# PRIME DIRECTIVE

1. Make sure we are on a non-protected branch (e.g: main or master). If so, create a new branch for our code. The branch prefix should align with the committed code's main purpose -- e.g.: is it a feature? bugfix? refactor? something else?
2. Make sure the current local branch is clean, meaning all of the code has been committed.
3. Review the commits and from those, create a thoughtful, short, clean, crisp and professional Pull Request description.
4. Push the commits to the git origin.
5. Create a pull request.
6. Provide the user the pull request URI.

# GH CLI REFERENCE

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
