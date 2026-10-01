#!/usr/bin/env python3

import shutil
from pathlib import Path

# Master template directory (where this script lives)
source_dir = Path(__file__).resolve().parent

# Look for ~/Desktop/*/n
desktop_dir = source_dir.parent

def ignore(dir, names):
    ignored = []

    rel = Path(dir).relative_to(source_dir)

    # Don't copy these from the root
    if rel == Path():
        ignored.extend([".git", ".gitignore", "chaps"])

    # Never recurse into .git
    if Path(dir).name == ".git":
        ignored.extend(names)

    return ignored

for folder in desktop_dir.iterdir():
    target = folder / "n"

    # Only sync directories that contain a notes installation
    if not (target / "input_chaps.py").exists():
        continue

    print(f"[SYNCING] {target}")

    shutil.copytree(
        source_dir,
        target,
        dirs_exist_ok=True,
        ignore=ignore,
    )

    print(f"[DONE]    {target}")

print("Finished syncing all classes.")
