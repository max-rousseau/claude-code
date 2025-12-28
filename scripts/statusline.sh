#!/bin/bash

# Claude Code Status Line Script
# Displays: Model | Directory | Session Info

# Read JSON input from stdin
input=$(cat)

# Extract values from JSON
model_name=$(echo "$input" | jq -r '.model.display_name')
current_dir=$(echo "$input" | jq -r '.workspace.current_dir')
session_id=$(echo "$input" | jq -r '.session_id')
output_style=$(echo "$input" | jq -r '.output_style.name')

# Get directory basename for cleaner display
dir_name=$(basename "$current_dir")

# Get git branch info if in a git repo
git_info=""
if cd "$current_dir" 2>/dev/null; then
    branch=$(git branch --show-current 2>/dev/null)
    if [[ -n "$branch" ]]; then
        git_status=""
        if [[ -n $(git status --porcelain 2>/dev/null) ]]; then
            git_status=" ✗"
        fi
        git_info=" git:($branch$git_status)"
    fi
fi

# Truncate session ID to first 8 characters for readability
short_session=$(echo "$session_id" | cut -c1-8)

# Build status line with colors
printf '\033[1;36m%s\033[0m \033[1;32m%s\033[0m\033[1;33m%s\033[0m \033[1;90m[%s]\033[0m' \
    "$model_name" \
    "$dir_name" \
    "$git_info" \
    "$short_session"