#!/bin/bash
# Security Review Context Gatherer for Go projects

set -o pipefail

echo "=== GIT STATUS ==="
git status
echo ""

echo "=== FILES MODIFIED (compared to origin/HEAD) ==="
git diff --name-only origin/HEAD... 2>/dev/null || git diff --name-only HEAD 2>/dev/null || echo "No changes detected"
echo ""

echo "=== COMMITS (compared to origin/HEAD) ==="
git log --no-decorate origin/HEAD... 2>/dev/null || git log --no-decorate -10 2>/dev/null || git log --no-decorate
echo ""

echo "=== DIFF CONTENT (full diff for review) ==="
git diff --merge-base origin/HEAD 2>/dev/null || git diff HEAD 2>/dev/null || echo "No diff available"
echo ""

echo "=== GOSEC SECURITY SCAN ==="
if command -v gosec &> /dev/null; then
    gosec ./... || true
else
    echo "gosec not installed. Install with: go install github.com/securego/gosec/v2/cmd/gosec@latest"
fi
echo ""

echo "=== SECURITY CONTEXT GATHERING COMPLETE ==="
