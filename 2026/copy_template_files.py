#!/usr/bin/env python3

import shutil
from pathlib import Path

# Source directory
source_dir = Path("~/Desktop/notes_files").expanduser()

# Destination directory (where the script is run from)
destination_dir = Path.cwd()

if not source_dir.exists():
    raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

def ignore(dir, names):
    ignored = []
    if Path(dir).relative_to(source_dir) == Path():
        ignored.extend([".git", ".gitignore", "chaps"])
    elif Path(dir).name == ".git":
        ignored.extend(names)
    return ignored

for item in source_dir.iterdir():
    if item.name in {".gitignore", "chaps"}:
        continue

    destination_path = destination_dir / item.name

    if item.is_dir():
        shutil.copytree(
            item,
            destination_path,
            dirs_exist_ok=True,
            ignore=ignore,
        )
    else:
        shutil.copy2(item, destination_path)

print(f"Copied contents of {source_dir} to {destination_dir}")
