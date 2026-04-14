#!/usr/bin/env python3
"""Read-only search helper for a digoal/blog checkout."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


def looks_like_blog_root(path: Path) -> bool:
    return (
        (path / "README.md").is_file()
        and (path / "CLAUDE.md").is_file()
        and (path / "class").is_dir()
    )


def discover_blog_root() -> Path:
    env_root = os.environ.get("DIGOAL_BLOG_ROOT")
    if env_root:
        root = Path(env_root).expanduser().resolve()
        if looks_like_blog_root(root):
            return root
        raise SystemExit(f"DIGOAL_BLOG_ROOT is not a digoal/blog root: {root}")

    starts = [Path.cwd().resolve(), Path(__file__).resolve()]
    for start in starts:
        for candidate in [start, *start.parents]:
            if looks_like_blog_root(candidate):
                return candidate

    raise SystemExit(
        "Could not locate digoal/blog root. Run from the blog repository, "
        "place this skill under skill/digoal, set DIGOAL_BLOG_ROOT, or pass --blog."
    )


def iter_markdown_files(root: Path):
    skip = {".git", "skill"}
    for path in root.rglob("*.md"):
        if any(part in skip for part in path.parts):
            continue
        yield path


def title_for(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                stripped = line.strip()
                if stripped.startswith("#"):
                    return stripped.lstrip("#").strip()
    except OSError:
        pass
    return ""


def search_file(path: Path, pattern: re.Pattern[str], titles_only: bool):
    title = title_for(path)
    if titles_only:
        if pattern.search(title):
            return [(0, title)]
        return []

    matches = []
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            for lineno, line in enumerate(handle, 1):
                if pattern.search(line):
                    matches.append((lineno, line.strip()))
                    if len(matches) >= 3:
                        break
    except OSError:
        return []
    return matches


def main() -> int:
    parser = argparse.ArgumentParser(description="Search digoal/blog markdown files without modifying them.")
    parser.add_argument("query", help="Regex or literal query. Use --literal for plain text.")
    parser.add_argument("--blog", help="Blog root path. Defaults to auto-discovery.")
    parser.add_argument("--limit", type=int, default=20, help="Maximum files to print.")
    parser.add_argument("--literal", action="store_true", help="Treat query as literal text.")
    parser.add_argument("--ignore-case", action="store_true", default=True, help="Case-insensitive search.")
    parser.add_argument("--titles-only", action="store_true", help="Search first markdown heading only.")
    args = parser.parse_args()

    root = Path(args.blog).expanduser().resolve() if args.blog else discover_blog_root()
    if not root.exists():
        raise SystemExit(f"Blog root does not exist: {root}")

    query = re.escape(args.query) if args.literal else args.query
    flags = re.IGNORECASE if args.ignore_case else 0
    pattern = re.compile(query, flags)

    printed = 0
    for path in sorted(iter_markdown_files(root), reverse=True):
        matches = search_file(path, pattern, args.titles_only)
        if not matches:
            continue
        rel = path.relative_to(root)
        print(f"{rel} :: {title_for(path)}")
        for lineno, text in matches:
            if lineno:
                print(f"  L{lineno}: {text[:240]}")
        printed += 1
        if printed >= args.limit:
            break

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
