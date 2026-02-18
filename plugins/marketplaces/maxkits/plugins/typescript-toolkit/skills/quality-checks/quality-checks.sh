#!/bin/bash
# TypeScript quality checks script - deterministic execution of code quality tools

set -o pipefail

echo "=== PRETTIER (formatting) ==="
npx prettier --check . 2>/dev/null || true

echo ""
echo "=== ESLINT (lint violations) ==="
npx eslint . 2>/dev/null || true

echo ""
echo "=== QUALITY CHECKS COMPLETE ==="
