## File Operations - MANDATORY

For ALL file operations, you MUST use Claude Code's built-in tools:

| Operation | USE | NEVER USE |
|-----------|-----|-----------|
| Reading files | `Read` | cat, head, tail, less |
| Editing files | `Edit` | sed, awk, perl -i |
| Creating files | `Write` | echo >, cat <<EOF, heredocs |
| Searching content | `Grep` | grep, rg, ag |
| Finding files | `Glob` | find, ls, locate |

## Bash Reserved For

Use `Bash` EXCLUSIVELY for operations with no built-in equivalent:
- Running Python scripts (`.venv/bin/python`)
- Package management (`.venv/bin/pip`)
- Quality tools (black, flake8, bandit, pip-audit)
- Test execution (`.venv/bin/pytest`)
- Git operations (git add, commit, push, etc.)
- Other system commands without built-in alternatives

## Python Execution - NO INLINE CODE

**NEVER** use `.venv/bin/python -c "..."` to run inline Python code.

Instead:
1. Write the script to `./tmp/` using the `Write` tool
2. Execute with `.venv/bin/python ./tmp/script_name.py`

**Script Documentation Requirements:**
- Every tmp/ script MUST have a docstring at the top explaining its purpose
- Use descriptive filenames (e.g., `debug_api_response.py`, `migrate_data.py`)
- Scripts may be kept for reuse - clear documentation enables future reference

**Example:**
```python
"""
Validates API response structure against expected schema.
Usage: .venv/bin/python ./tmp/validate_api_response.py
"""
```

This ensures:
- Code is reviewable before execution
- Proper syntax highlighting and error messages
- Reproducible debugging
- No shell escaping issues with complex code
- Scripts can be referenced and reused later

## Rationale

Built-in tools provide:
- Better error handling and user experience
- Consistent output formatting
- Proper permission handling
- Integration with Claude Code's context system
