#!/usr/bin/env python3
"""
Library Updater - Upgrade all dependencies in pyproject.toml to latest versions.

Requires Python >= 3.11 (uses tomllib from stdlib).
No external dependencies.
"""

import re
import subprocess
import sys
from pathlib import Path
import tomllib

PYPROJECT = Path("pyproject.toml")
PIP = Path(".venv/bin/pip")


def parse_package_name(dep_string: str) -> str | None:
    """Extract package name from dependency string. Returns None for git/url deps."""
    dep = dep_string.strip()
    if " @ " in dep:
        return None
    match = re.match(r"^([a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?)", dep)
    return match.group(1) if match else None


def get_dependencies() -> tuple[list[str], list[str]]:
    """Parse pyproject.toml. Returns (packages, skipped)."""
    with open(PYPROJECT, "rb") as f:
        data = tomllib.load(f)

    packages, skipped = [], []
    all_deps = data.get("project", {}).get("dependencies", [])

    for group_deps in data.get("project", {}).get("optional-dependencies", {}).values():
        all_deps.extend(group_deps)

    for dep in all_deps:
        if name := parse_package_name(dep):
            packages.append(name)
        else:
            skipped.append(dep)

    return list(set(packages)), skipped


def main() -> int:
    if not PYPROJECT.exists():
        print("Error: pyproject.toml not found")
        return 1

    if not PIP.exists():
        print("Error: .venv/bin/pip not found")
        return 1

    packages, skipped = get_dependencies()

    if not packages:
        print("No dependencies found")
        return 0

    print(f"Upgrading {len(packages)} dependencies...")
    if skipped:
        print(f"Skipping {len(skipped)} git/url dependencies\n")

    failures = []
    for package in sorted(packages):
        print(f"  {package} ... ", end="", flush=True)
        result = subprocess.run(
            [str(PIP), "install", "--upgrade", package],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("OK")
        else:
            print("FAILED")
            failures.append((package, result.stderr.strip().split("\n")[-1]))

    print(f"\nDone: {len(packages) - len(failures)} upgraded, {len(failures)} failed")

    if failures:
        print("\nFailed:")
        for pkg, err in failures:
            print(f"  - {pkg}: {err[:80]}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
