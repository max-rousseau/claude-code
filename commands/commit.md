---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git log:*), Bash(git diff:*), Bash(git branch:*)
description: Create a git commit
---

# CONTEXT

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

# PRIME DIRECTIVE

Carefully review the current repository' state and changes and make thoughtful commits with meaningful and professional messages (indicate if its bugfix, feature, chore, etc.). Remember to never include claude code as a co-author on commits. Make sure all changes are committed. If your confidence level is low (less than 0.8), you can ask the user if specific files should be added or ignored. Otherwise, just proceed without requiring more user input knowing that the user can always revert the changes if it's displeased.

Based on the changes made, review the `pyproject.toml` and ensure that one of the commits increases the version logically according to the proper development practices for major version changes, minor versions and patches (x.y.z).