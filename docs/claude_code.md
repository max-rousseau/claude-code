# Claude Code Comprehensive Documentation

## Overview
Claude Code is a terminal-based AI coding assistant that helps developers turn ideas into code quickly by working directly in the terminal environment. It can build features from descriptions, debug code, navigate complex codebases, and automate repetitive tasks.

## Table of Contents
1. [Installation & Setup](#installation--setup)
2. [Settings Configuration](#settings-configuration)
3. [Sub-Agents](#sub-agents)
4. [Memory Management](#memory-management)
5. [CLI Commands & Flags](#cli-commands--flags)
6. [Slash Commands](#slash-commands)
7. [Hooks System](#hooks-system)
8. [Common Workflows](#common-workflows)
9. [Interactive Mode & Keyboard Shortcuts](#interactive-mode--keyboard-shortcuts)
10. [IDE Integrations](#ide-integrations)
11. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
12. [SDK & Programmatic Access](#sdk--programmatic-access)

## Installation & Setup

### Prerequisites
- Node.js 18 or newer

### Quick Start
```bash
npm install -g @anthropic-ai/claude-code
cd your-project
claude
```

### Authentication Methods
1. **Anthropic API Key**
   - Create key in Anthropic Console
   - Set `ANTHROPIC_API_KEY` environment variable

2. **Third-Party Providers**
   - Amazon Bedrock: `CLAUDE_CODE_USE_BEDROCK=1`
   - Google Vertex AI: `CLAUDE_CODE_USE_VERTEX=1`

## Settings Configuration

### Settings File Hierarchy (Highest to Lowest Priority)
1. Enterprise managed policies (cannot be overridden)
2. Command line arguments (temporary session overrides)
3. Local project settings (`.claude/settings.local.json`)
4. Shared project settings (`.claude/settings.json`)
5. User settings (`~/.claude/settings.json`)

### Settings File Locations
- **User settings**: `~/.claude/settings.json` (global)
- **Project settings**: `.claude/settings.json` (shared with team)
- **Local project settings**: `.claude/settings.local.json` (personal, not version controlled)
- **Enterprise settings**: System-specific paths

### Key Configuration Options

#### Permissions
```json
{
  "permissions": {
    "allow": ["Bash", "Read", "Write"],
    "deny": ["WebSearch"],
    "additionalDirectories": ["/path/to/dir"],
    "defaultMode": "ask"
  }
}
```

#### Environment Variables
```json
{
  "environment": {
    "ANTHROPIC_API_KEY": "sk-...",
    "CLAUDE_CODE_USE_BEDROCK": "1"
  }
}
```

#### Global Settings
```json
{
  "autoUpdates": true,
  "theme": "dark",
  "verbose": false
}
```

### Available Tools
- **Bash**: Execute shell commands (requires permission)
- **Edit**: Modify existing files
- **Glob**: Pattern-based file search
- **Grep**: Content search
- **Read**: Read file contents
- **Write**: Create/overwrite files
- **WebFetch**: Fetch and process web content
- **WebSearch**: Search the web

## Sub-Agents

### What are Sub-Agents?
Specialized AI assistants within Claude Code that operate with separate context windows from the main conversation, designed for specific task types.

### Available Sub-Agent Types
1. **Code Reviewer**: Reviews code quality, security, and maintainability
2. **Debugger**: Root cause analysis and minimal fixes
3. **Data Scientist**: SQL and data analysis expertise
4. **API Designer**: API development specialization
5. **Performance Optimizer**: Performance improvement focus

### Configuration Structure
Sub-agents are defined as Markdown files with YAML frontmatter:

```markdown
---
name: subagent-name
description: Purpose and when to invoke
tools: [Read, Write, Bash]
---
System prompt with specialized instructions
```

### Sub-Agent Locations
- **Project-level**: `.claude/agents/` (team-shared, version controlled)
- **User-level**: `~/.claude/agents/` (personal, cross-project)

### Creation Methods
1. Interactive `/agents` command
2. Direct file management
3. Claude-assisted generation (recommended)

### Best Practices
- Single responsibility principle
- Detailed system prompts
- Limited tool access
- Version control for project agents
- Clear descriptions for automatic delegation

## Memory Management

### Memory Hierarchy (Highest to Lowest Priority)
1. **Enterprise Policy Memory**: OS-specific system directories
2. **Project Memory**: `./CLAUDE.md`
3. **User Memory**: `~/.claude/CLAUDE.md`
4. **Local Project Memory** (Deprecated): `./CLAUDE.local.md`

### Key Features
- Automatic loading on startup
- File imports with `@path/to/import` syntax
- Recursive discovery up directory tree
- Maximum import depth of 5 hops

### Quick Memory Management
- Use `#` to quickly add a memory
- Use `/memory` command to edit memory files
- Use `/init` to bootstrap project's CLAUDE.md

### Best Practices
- Be specific with instructions
- Use structured markdown
- Organize under descriptive headings
- Periodically review and update

## CLI Commands & Flags

### Core Commands
```bash
# Start interactive REPL
claude

# Start with initial prompt
claude "explain this project"

# Query via SDK, then exit
claude -p "explain this function"

# Process piped content
cat logs.txt | claude -p "analyze these logs"

# Continue most recent conversation
claude -c

# Resume specific session
claude -r "<session-id>" "continue the task"

# Update to latest version
claude update

# Configure MCP servers
claude mcp
```

### Important Flags
- `--add-dir`: Add additional working directories
- `--allowedTools`: Specify allowed tools without permission
- `--print / -p`: Print response without interactive mode
- `--output-format`: Specify output format (text, json, stream-json)
- `--verbose`: Enable detailed logging
- `--model`: Set session model
- `--permission-mode`: Begin in specific permission mode
- `--continue`: Load most recent conversation
- `--resume`: Show conversation picker

## Slash Commands

### Built-in Commands
- `/add-dir`: Add working directories
- `/agents`: Manage AI subagents
- `/bug`: Report bugs to Anthropic
- `/clear`: Clear conversation history
- `/config`: View/modify configuration
- `/help`: Get usage help
- `/init`: Initialize project
- `/login`: Switch Anthropic accounts
- `/model`: Select or change AI model
- `/review`: Request code review
- `/memory`: Edit memory files
- `/vim`: Enable Vim mode

### Custom Slash Commands
Create custom commands in:
- Project-level: `.claude/commands/`
- Personal-level: `~/.claude/commands/`

Example custom command:
```bash
mkdir -p .claude/commands
echo "Analyze for performance issues" > .claude/commands/optimize.md
```

### MCP Slash Commands
- Format: `/mcp__<server-name>__<prompt-name>`
- Dynamically discovered from connected servers
- Can accept server-defined arguments

## Hooks System

### Hook Types
1. **PreToolUse**: Before tool usage
2. **PostToolUse**: After successful tool completion
3. **Notification**: During system notifications
4. **UserPromptSubmit**: When user submits prompt
5. **Stop**: When main agent finishes
6. **SubagentStop**: When subagent completes
7. **PreCompact**: Before context compaction
8. **SessionStart**: Starting/resuming session

### Configuration Example
```json
{
  "hooks": {
    "PreToolUse": {
      "command": "./scripts/validate.sh",
      "timeout": 5000,
      "matchers": ["Write", "Edit"]
    }
  }
}
```

### Key Features
- Receive JSON input with session/event details
- Can block or modify tool usage
- Support for adding context
- Configurable timeout and execution parameters

### Use Cases
- Validate file operations
- Add context to prompts
- Log system events
- Implement custom workflow controls

## Common Workflows

### Understanding New Codebases
- Ask about architecture, data models, authentication
- Start broad, then narrow down
- Use Claude to get quick project overviews

### Extended Thinking
For complex tasks like architectural changes or debugging:
- Basic: Use "think"
- Deeper: Use "think harder" or "think longer"

### Image Interaction
- **Methods**: Drag and drop, Ctrl+v, provide path
- **Use cases**: Code analysis, UI review, error diagnosis

### Resume Conversations
- `--continue`: Resume most recent
- `--resume`: Show conversation picker
- Preserves full context and tool state

### Parallel Work with Git Worktrees
- Create isolated working directories
- Run multiple Claude Code sessions
- Maintain independent file states

### Unix Utility Integration
- Integrate into build scripts
- Support piping input/output
- Configurable output formats

## Interactive Mode & Keyboard Shortcuts

### General Controls
- `Ctrl+C`: Cancel current input/generation
- `Ctrl+D`: Exit session
- `Ctrl+L`: Clear screen
- Up/Down arrows: Navigate history
- `Esc` + `Esc`: Edit previous message

### Multiline Input
- Quick escape: `\` + `Enter`
- macOS: `Option+Enter`
- Terminal setup: `Shift+Enter`

### Vim Mode
Enable with `/vim` command

**Mode Switching:**
- `Esc`: Enter NORMAL mode
- `i`: Insert before cursor
- `a`: Insert after cursor
- `o`: Open line below

**Navigation (NORMAL mode):**
- `h/j/k/l`: Move left/down/up/right
- `w/b`: Next/previous word
- `0/$`: Beginning/end of line
- `gg/G`: Beginning/end of input

**Editing (NORMAL mode):**
- `x`: Delete character
- `dd`: Delete line
- `D`: Delete to end of line
- `cw`: Change word
- `.`: Repeat last change

## IDE Integrations

### Visual Studio Code & Forks
**Supported:** VS Code, Cursor, Windsurf, VSCodium

**Features:**
- Quick launch: Cmd+Esc (Mac) / Ctrl+Esc (Windows/Linux)
- Diff viewing in IDE
- Automatic selection/tab context sharing
- File reference shortcuts
- Diagnostic error sharing

### JetBrains IDEs
**Supported:** IntelliJ, PyCharm, Android Studio, WebStorm, PhpStorm, GoLand

**Installation:**
- Via marketplace plugin
- Or run `claude` in terminal
- Requires IDE restart

### General IDE Support
- Works with any IDE with terminal
- Use `/ide` command to connect from external terminals
- Start from project root for best file access

## Model Context Protocol (MCP)

### Overview
Open-source standard for AI-tool integrations allowing Claude Code to connect to external tools, databases, and APIs.

### Server Types
1. **Local stdio servers**: Run on local machine
2. **Remote SSE servers**: Real-time streaming
3. **Remote HTTP servers**: Standard request/response

### Installation Scopes
- **Local**: Personal, project-specific
- **Project**: Team-shared configurations
- **User**: Cross-project utility servers

### Popular MCP Servers
**Development & Testing:**
- GitHub
- Sentry (error monitoring)

**Project Management:**
- Linear
- Asana
- Notion

**Commerce & Payments:**
- Stripe

**Design & Media:**
- Figma

### Authentication
- OAuth 2.0 for cloud-based servers
- Use `/mcp` command to authenticate

### Example Use Cases
- Implement features from issue trackers
- Analyze monitoring data
- Query databases
- Integrate designs
- Automate workflows

## SDK & Programmatic Access

### Command Line Usage
```bash
# Single prompt
claude -p "Write a Fibonacci function"

# JSON output
claude -p "Generate code" --output-format json

# Process piped input
echo "code" | claude -p "review this"
```

### TypeScript Integration
```typescript
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "Write a haiku about foo.py",
  options: { maxTurns: 3 }
})) {
  // Process messages
}
```

### Python Integration
```python
from claude_code_sdk import query, ClaudeCodeOptions

async for message in query(
  prompt="Write a haiku about foo.py",
  options=ClaudeCodeOptions(max_turns=3)
):
    # Process messages
```

### Advanced Features
- Multi-turn conversations
- Custom system prompts
- Permission management
- Flexible input/output formats
- MCP integration support

## Security Considerations

### Hooks Security
- Execute shell commands automatically
- Requires careful validation
- Users responsible for hook security

### MCP Security
- Use third-party servers at own risk
- Verify server security before use
- Review permissions granted

### Best Practices
- Never hardcode secrets
- Use environment variables
- Review tool permissions
- Validate all inputs
- Regular security audits

## Performance Tips

### Context Management
- Use sub-agents for specialized tasks
- Clear conversation history when needed
- Leverage memory files effectively

### Efficiency
- Batch related requests
- Use appropriate sub-agents
- Configure tool permissions properly
- Utilize hooks for automation

### Parallel Processing
- Git worktrees for parallel work
- Multiple Claude sessions
- Async SDK operations

## Troubleshooting

### Common Issues
- Authentication failures: Check API keys
- Tool permission errors: Review settings.json
- Memory not loading: Check file paths and syntax
- IDE integration issues: Restart IDE after installation

### Getting Help
- Report bugs: `/bug` command
- GitHub issues: https://github.com/anthropics/claude-code/issues
- Documentation: https://docs.anthropic.com/en/docs/claude-code

## Updates & Maintenance

### Updating Claude Code
```bash
claude update
```

### Configuration Management
```bash
# View configuration
claude config

# Edit settings
/config
```

### Memory Maintenance
- Review memories periodically
- Remove outdated instructions
- Organize by project phase

---

*This documentation compiled from official Claude Code documentation. For the latest updates, visit https://docs.anthropic.com/en/docs/claude-code*