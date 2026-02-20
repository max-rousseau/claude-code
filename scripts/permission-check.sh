#!/bin/bash
# Permission check hook - denies heretical tool invocations

input=$(cat)
command=$(echo "$input" | jq -r '.tool_input.command // empty')

# Check for direct quality tool invocation
if echo "$command" | grep -qE '\.venv/bin/(black|flake8|bandit|vulture|pip-audit)'; then
    echo '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"HERESY DETECTED: Direct quality tool invocation is FORBIDDEN. Invoke the quality-checks skill instead. See CLAUDE.md directive #5.","interrupt":true}}}'
    exit 0
fi

# Check for python -m quality tools
if echo "$command" | grep -qE '\.venv/bin/python.*-m (black|flake8|bandit|vulture)'; then
    echo '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"HERESY DETECTED: Direct quality tool invocation is FORBIDDEN. Invoke the quality-checks skill instead. See CLAUDE.md directive #5.","interrupt":true}}}'
    exit 0
fi

# Check for inline python -c
if echo "$command" | grep -qE '\.venv/bin/python.*-c '; then
    echo '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"HERESY DETECTED: Inline python -c execution is FORBIDDEN. Write script to ./tmp/ and execute it. See tool-use-guidelines.md.","interrupt":true}}}'
    exit 0
fi

# Check for command chaining with && or ;
if echo "$command" | grep -qE '&&|;\s'; then
    echo '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"HERESY DETECTED: Do not chain commands with && or ;. Make separate tool calls instead. Pipes (|) and redirects (>) are fine.","interrupt":true}}}'
    exit 0
fi

# Check for git -C usage
if echo "$command" | grep -qE '^git\s+-C\s'; then
    echo '{"hookSpecificOutput":{"hookEventName":"PermissionRequest","decision":{"behavior":"deny","message":"HERESY DETECTED: Do not use git -C. Use plain git commands; the working directory is already the project root. See tool-use-guidelines.md.","interrupt":true}}}'
    exit 0
fi

# No match - allow normal processing
exit 0
