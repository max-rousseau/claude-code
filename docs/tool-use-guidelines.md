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
- Running project scripts and build commands
- Package management (language-specific package managers)
- Quality/lint tools via plugin skills
- Test execution via plugin skills
- Git operations (git add, commit, push, etc.)
- Other system commands without built-in alternatives

## NEVER use `cd` in Bash commands

**NEVER** prefix Bash commands with `cd /path && ...`. Instead, use absolute paths directly:

| BAD | GOOD |
|-----|------|
| `cd /project && .venv/bin/pytest tests/` | `.venv/bin/pytest /project/tests/` |
| `cd /project && ./script.sh` | `/project/script.sh` |
| `cd /project && ls src/` | `ls /project/src/` |

For tools that don't support absolute paths natively, pass the directory as an argument or environment variable rather than using `cd`.

**Exception — git and gh**: Do NOT use `git -C /path`. Use plain `git` commands directly; the working directory is already the project root.

## Rationale

Built-in tools provide:
- Better error handling and user experience
- Consistent output formatting
- Proper permission handling
- Integration with Claude Code's context system
