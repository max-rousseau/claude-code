"""
Repository setup script - configures git hooks and GitHub Actions workflow.

Applies opinionated quality guardrails consistently across all projects.
Templates are copied from the python-toolkit plugin templates directory.

Usage: python3 ~/.claude/plugins/marketplaces/maxkits/plugins/python-toolkit/skills/repo-setup/setup.py [project_path]
"""

import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = SCRIPT_DIR / "templates"

REQUIRED_PIPX_TOOLS = ["black", "flake8", "bandit", "vulture"]

REQUIRED_TOOL_SECTIONS = [
    "tool.black",
    "tool.flake8",
    "tool.bandit",
    "tool.vulture",
    "tool.pytest",
]


def print_header(msg: str) -> None:
    print(f"\n{'='*60}\n{msg}\n{'='*60}")


def print_status(success: bool, msg: str) -> None:
    symbol = "[OK]" if success else "[!!]"
    print(f"  {symbol} {msg}")


def check_pyproject(project_path: Path) -> bool:
    """Verify pyproject.toml exists and has required tool sections."""
    pyproject = project_path / "pyproject.toml"

    if not pyproject.exists():
        print_status(False, "pyproject.toml not found")
        print("       Run /python-pyproject skill to create it first")
        return False

    content = pyproject.read_text()
    missing = [
        section for section in REQUIRED_TOOL_SECTIONS if f"[{section}]" not in content
    ]

    if missing:
        print_status(False, f"Missing sections: {', '.join(missing)}")
        print("       Run /python-pyproject skill to add missing sections")
        return False

    print_status(True, "pyproject.toml has all required tool sections")
    return True


def setup_git_hooks(project_path: Path) -> bool:
    """Copy hook templates and configure git to use them."""
    hooks_dest = project_path / "scripts" / "hooks"
    hooks_src = TEMPLATE_DIR / "hooks"

    hooks_dest.mkdir(parents=True, exist_ok=True)

    for hook_file in hooks_src.iterdir():
        dest_file = hooks_dest / hook_file.name
        shutil.copy2(hook_file, dest_file)
        dest_file.chmod(0o755)
        print_status(True, f"Copied {hook_file.name} to scripts/hooks/")

    result = subprocess.run(
        ["git", "config", "core.hooksPath", "scripts/hooks"],
        cwd=project_path,
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print_status(True, "Configured git to use scripts/hooks/")
        return True
    else:
        print_status(False, f"Failed to configure git: {result.stderr}")
        return False


def setup_github_workflow(project_path: Path) -> bool:
    """Copy GitHub Actions workflow template."""
    workflow_dest = project_path / ".github" / "workflows"
    workflow_src = TEMPLATE_DIR / "github" / "quality.yml"

    workflow_dest.mkdir(parents=True, exist_ok=True)

    dest_file = workflow_dest / "quality.yml"
    shutil.copy2(workflow_src, dest_file)
    print_status(True, "Copied quality.yml to .github/workflows/")
    return True


def check_pipx_tools() -> bool:
    """Verify required tools are available via pipx."""
    all_found = True

    for tool in REQUIRED_PIPX_TOOLS:
        result = subprocess.run(["which", tool], capture_output=True, text=True)
        if result.returncode == 0:
            print_status(True, f"{tool} available at {result.stdout.strip()}")
        else:
            print_status(False, f"{tool} not found - install with: pipx install {tool}")
            all_found = False

    return all_found


def main() -> int:
    project_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    project_path = project_path.resolve()

    print_header(f"REPO SETUP: {project_path}")

    if not (project_path / ".git").exists():
        print_status(False, "Not a git repository")
        return 1

    print_header("1. CHECKING PYPROJECT.TOML")
    pyproject_ok = check_pyproject(project_path)

    print_header("2. SETTING UP GIT HOOKS")
    if pyproject_ok:
        setup_git_hooks(project_path)
    else:
        print("  Skipping - fix pyproject.toml first")

    print_header("3. SETTING UP GITHUB WORKFLOW")
    if pyproject_ok:
        setup_github_workflow(project_path)
    else:
        print("  Skipping - fix pyproject.toml first")

    print_header("4. CHECKING LOCAL TOOLS (pipx)")
    check_pipx_tools()

    print_header("SETUP COMPLETE")

    if not pyproject_ok:
        print("\nAction required: Run /python-pyproject to configure pyproject.toml")
        return 1

    print("\nRepository is configured with quality guardrails:")
    print("  - Git hooks: scripts/hooks/pre-commit, pre-push")
    print("  - GitHub Actions: .github/workflows/quality.yml")
    print("  - Config source: pyproject.toml")

    return 0


if __name__ == "__main__":
    sys.exit(main())
