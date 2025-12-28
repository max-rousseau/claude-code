#!/bin/bash
# Quality checks script - deterministic execution of code quality tools
# All tools read configuration from pyproject.toml when available

set -o pipefail

echo "=== BLACK (formatting) ==="
./.venv/bin/python -m black . || true

echo ""
echo "=== FLAKE8 (style violations) ==="
./.venv/bin/python -m flake8 . || true

echo ""
echo "=== VULTURE (dead code analysis) ==="
./.venv/bin/python -m vulture . || true

echo ""
echo "=== QUALITY CHECKS COMPLETE ==="
