## Core Principles
- Follow Effective Go guidelines
- Code must pass `go vet` and `staticcheck` cleanly
- All code must be formatted with `gofmt`

## Naming Conventions
- `camelCase` for unexported identifiers
- `PascalCase` for exported identifiers
- Short, descriptive variable names (prefer `r` over `reader` in small scopes)
- Acronyms are all caps: `HTTP`, `URL`, `ID` (not `Http`, `Url`, `Id`)
- Interface names: single-method interfaces use method name + "er" suffix (e.g., `Reader`, `Writer`)

## Code Layout Standards
- Keep each file focused on single responsibility
- Group related types, functions, and methods in the same file
- Order: types, constructors, methods, helpers
- Use early returns to reduce nesting

## Functions & Methods
- Keep functions short and focused
- Return errors, don't panic (except in init or truly unrecoverable situations)
- Wrap errors with context: `fmt.Errorf("doing X: %w", err)`
- Accept interfaces, return structs
- Use functional options pattern for complex configuration

## Error Handling
- Always check returned errors
- Never use `_` to discard errors unless explicitly justified
- Use sentinel errors or custom error types for expected conditions
- Wrap errors to preserve the chain: `%w` verb

## Package Organization
- Package names are lowercase, single-word, no underscores
- Avoid `util`, `common`, `misc` packages — name by what it provides
- Internal packages for implementation details

## Testing Standards
- Table-driven tests for comprehensive coverage
- Use `testify` or standard library assertions
- Test files in same package for white-box testing
- `_test` package suffix for black-box testing when needed
- Use `t.Helper()` in test helper functions

## Concurrency Standards
- Use channels for communication, mutexes for state
- Always pass `context.Context` as first parameter
- Use `errgroup` for coordinated goroutine management
- Prefer `sync.Once` for lazy initialization

## Security Standards
- Never hardcode secrets or credentials
- Use environment variables or config files for sensitive data
- Validate all external input
- Use `crypto/rand` not `math/rand` for security-sensitive randomness
