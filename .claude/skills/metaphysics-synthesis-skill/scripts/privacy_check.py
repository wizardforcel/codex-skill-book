#!/usr/bin/env python3
"""Privacy scan for public metaphysics skill publishing."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}

PATTERNS = [
    r"OPENAI_API_KEY",
    r"ANTHROPIC_API_KEY",
    r"github_pat_",
    r"ghp_",
    r"sk-[A-Za-z0-9_-]{12,}",
    r"Bearer\s+[A-Za-z0-9._-]+",
    r"身份证",
    r"手机号",
    r"家庭住址",
    r"银行账号",
    r"父亲",
    r"母亲",
    r"前女友",
    r"阿里",
    r"\bP6\b",
]


def iter_text_files() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path == pathlib.Path(__file__).resolve():
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".py", ".yaml", ".yml", ".json"}:
            files.append(path)
    return files


def main() -> None:
    hits: list[str] = []
    compiled = [re.compile(pattern) for pattern in PATTERNS]
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pattern in compiled:
                if pattern.search(line):
                    rel = path.relative_to(ROOT)
                    hits.append(f"{rel}:{line_no}: {line.strip()}")
                    break
    if hits:
        print("Privacy scan failed:", file=sys.stderr)
        for hit in hits:
            print(hit, file=sys.stderr)
        raise SystemExit(1)
    print("OK: privacy scan passed")


if __name__ == "__main__":
    main()
