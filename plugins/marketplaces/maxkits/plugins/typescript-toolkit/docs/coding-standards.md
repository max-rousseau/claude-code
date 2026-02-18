## Core Principles
- Strict TypeScript mode enabled (`strict: true`)
- ESLint and Prettier for consistent formatting
- Prefer functional patterns where appropriate

## Naming Conventions
- `camelCase` for variables, functions, and methods
- `PascalCase` for classes, interfaces, type aliases, enums, and React components
- `UPPER_CASE` for constants
- `I` prefix for interfaces is discouraged — use descriptive names
- Boolean variables prefixed with `is`, `has`, `should`, `can`

## Code Layout Standards
- Keep each file focused on single responsibility
- One component per file (React)
- Barrel exports via `index.ts` for clean imports
- Organize by feature, not by type

## Functions & Types
- Keep functions short and focused
- Use descriptive parameter names
- Always provide explicit return types on exported functions
- Prefer `type` over `interface` unless declaration merging is needed
- Use `readonly` for immutable data structures
- Prefer `unknown` over `any`

## Import Standards
- Use path aliases (e.g., `@/components/`) when configured
- Group imports: external, internal, relative
- No circular dependencies
- Use named exports (avoid default exports for better refactoring)

## Error Handling
- Always handle promise rejections
- Use typed error handling (custom error classes)
- Never swallow errors silently
- Use Result types or discriminated unions for expected failures

## Testing Standards
- Test files co-located with source or in `__tests__/` directories
- Use `describe`/`it` blocks with clear descriptions
- Mock external dependencies at boundaries
- Test behavior, not implementation

## Security Standards
- Never hardcode secrets or credentials
- Sanitize user input before rendering (avoid `dangerouslySetInnerHTML`)
- Use parameterized queries for database operations
- Validate all external input with schemas (zod, joi, etc.)
