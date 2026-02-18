## Core Principles
- All code must pass `terraform fmt` and `terraform validate`
- Use `tflint` for additional quality checks
- Follow HashiCorp's style conventions

## Naming Conventions
- `snake_case` for all resource names, variables, outputs, and locals
- Resource names should be descriptive: `aws_instance.web_server` not `aws_instance.this`
- Variable names describe the value: `vpc_cidr_block` not `cidr`
- Boolean variables prefixed with `enable_` or `is_`

## File Organization
- `main.tf` - Primary resources
- `variables.tf` - Input variable declarations
- `outputs.tf` - Output declarations
- `providers.tf` - Provider configuration and versions
- `locals.tf` - Local values
- `data.tf` - Data sources
- `terraform.tf` - Backend and terraform block configuration
- Split large configurations by logical grouping (networking, compute, storage)

## Resource Standards
- Always specify provider versions with `~>` constraints
- Use `for_each` over `count` for collections (better state management)
- Tag all resources with at minimum: Name, Environment, ManagedBy
- Use `locals` for computed values referenced multiple times
- Avoid inline blocks when separate resources provide better control

## Variable Standards
- Always include `description` for every variable
- Always include `type` constraint
- Use `validation` blocks for input validation
- Provide sensible `default` values where appropriate
- Group related variables with comments

## Module Standards
- Modules should be focused on a single concern
- Pin module versions: `source = "..." version = "~> 1.0"`
- Document inputs, outputs, and usage in module README
- Use consistent variable naming across modules

## Security Standards
- Never hardcode credentials or secrets in `.tf` files
- Use `sensitive = true` for sensitive variables and outputs
- Encrypt all storage resources (S3, EBS, RDS, etc.)
- Restrict security group rules to minimum required access
- Enable logging for all auditable resources
- Use IAM roles with least-privilege policies
