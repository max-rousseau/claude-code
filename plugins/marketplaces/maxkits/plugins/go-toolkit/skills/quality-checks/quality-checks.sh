#!/bin/bash
# Go quality checks script - deterministic execution of code quality tools

set -o pipefail

echo "=== GO VET (correctness) ==="
go vet ./... || true

echo ""
echo "=== STATICCHECK (static analysis) ==="
if command -v staticcheck &> /dev/null; then
    staticcheck ./... || true
else
    echo "staticcheck not installed. Install with: go install honnef.co/go/tools/cmd/staticcheck@latest"
fi

echo ""
echo "=== GO FMT CHECK ==="
UNFMT=$(gofmt -l . 2>/dev/null)
if [ -n "$UNFMT" ]; then
    echo "Unformatted files:"
    echo "$UNFMT"
else
    echo "All files formatted correctly"
fi

echo ""
echo "=== QUALITY CHECKS COMPLETE ==="
