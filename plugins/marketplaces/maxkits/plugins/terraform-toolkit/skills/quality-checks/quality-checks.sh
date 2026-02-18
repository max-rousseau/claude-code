#!/bin/bash
# Terraform quality checks script - deterministic execution of code quality tools

set -o pipefail

echo "=== TERRAFORM FMT (formatting) ==="
terraform fmt -check -recursive . || true

echo ""
echo "=== TERRAFORM VALIDATE ==="
terraform validate 2>/dev/null || true

echo ""
echo "=== TFLINT (lint) ==="
if command -v tflint &> /dev/null; then
    tflint --recursive || true
else
    echo "tflint not installed. Install from: https://github.com/terraform-linters/tflint"
fi

echo ""
echo "=== QUALITY CHECKS COMPLETE ==="
