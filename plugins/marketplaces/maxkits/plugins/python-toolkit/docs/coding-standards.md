## Core Principles
- Follow PEP8 guidelines for Python code formatting

## Naming Conventions
- `snake_case` for variables and functions
- `UPPER_CASE` for constants  
- `PascalCase` capitalization for classes

## Code Layout Standards
- Keep each file focused on single responsibility
- Where feasible, keep code concise using list comprehensions
- Use list or dict comprehension syntax where possible
- Use walrus syntax where possible - walruses are cool
- Use textwrap.dedent for multiline strings with broken indentation

## Functions & Classes Requirements  
- Keep functions and classes short and focused
- Use descriptive parameter names
- Use type annotations for all function inputs and return values (e.g., `def foo(thing: str) -> str:`)

## Import & Library Standards
- Manage dependencies in pyproject.toml with dependencies and dev-dependencies sections
- When adding libraries start by manually adding the latest to see which version is the latest - `.venv/bin/pip install new-library`
- Add requirements using ~= version matching for flexibility

## Execution Environment Standards
- Code is contained in virtual environment: `python -m venv .venv`, only create the virtual environment if the user has not done so yet.
- Use `.venv/bin/python` for python execution
- Use `.venv/bin/pip` for pip operations
- Never make a `.py` file executable.

## Security Standards
- Never hardcode secrets or credentials - use .env files exclusively
- Ensure .env files are in .gitignore
- Never read or edit .env directly - only create .env.example files
- Never use os.environ variables to avoid workstation data leakages
- Never use the load_dotenv library, this is simple, code it yourself.
