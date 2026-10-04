"""
Project Setup Script for Lab 01
AI Project Design and Development (AI-316) - Air University Islamabad
Project: AI-Based Laboratory Theft Detection & Prevention System
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output encoding for Windows command line / PowerShell
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def setup_project_structure():
    directories = [
        "configs",
        "data/raw",
        "data/processed",
        "logs",
        "models",
        "notebooks",
        "src",
    ]

    print("[*] Initializing AI Project Directory Structure...")
    base_dir = Path(__file__).resolve().parent

    for dir_path in directories:
        target = base_dir / dir_path
        target.mkdir(parents=True, exist_ok=True)
        # Create .gitkeep for empty folders to track them in Git
        gitkeep = target / ".gitkeep"
        if not gitkeep.exists() and not any(target.iterdir()):
            gitkeep.touch()
        print(f" [+] Verified directory: {dir_path}/")

    print("\n[*] Project structure setup complete.")


def display_tree(start_path: Path, prefix: str = "", max_depth: int = 3, current_depth: int = 0):
    if current_depth > max_depth:
        return

    use_ascii = sys.platform.startswith("win") and getattr(sys.stdout, "encoding", "").lower() not in ("utf-8", "utf8")
    branch = "|-- " if use_ascii else "├── "
    last_branch = "\\-- " if use_ascii else "└── "
    vertical = "|   " if use_ascii else "│   "
    indent = "    "

    ignored = {".git", "aipdd_env", ".venv", "venv", "__pycache__", ".ipynb_checkpoints"}
    items = sorted(
        [item for item in start_path.iterdir() if item.name not in ignored],
        key=lambda x: (not x.is_dir(), x.name.lower()),
    )

    for index, item in enumerate(items):
        is_last = index == (len(items) - 1)
        connector = last_branch if is_last else branch
        print(f"{prefix}{connector}{item.name}{'/' if item.is_dir() else ''}")

        if item.is_dir():
            extension = indent if is_last else vertical
            display_tree(item, prefix + extension, max_depth, current_depth + 1)



if __name__ == "__main__":
    setup_project_structure()
    print("\n[*] Directory Tree View:")
    display_tree(Path(__file__).resolve().parent)
