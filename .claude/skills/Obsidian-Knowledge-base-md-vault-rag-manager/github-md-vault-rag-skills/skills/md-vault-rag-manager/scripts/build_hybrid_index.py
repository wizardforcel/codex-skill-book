#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


sys.dont_write_bytecode = True

DEFAULT_EXCLUDE_PARTS = {
    "00_检索索引",
    "00_search_index",
    "01_导入原始材料",
    "01_import_raw",
    "02_入库处理区",
    "02_processing_queue",
    "99_垃圾区",
    "99_trash",
    "05_Inbox",
    "Inbox",
    "Archive",
    "archive",
    "trash",
    "raw",
    "pending",
    "rejected",
    "unverified",
}

DEFAULT_EXCLUDE_MARKERS = {
    "status: raw",
    "type: inbox",
    "truth_status: unverified",
    "truth_status: discarded",
    "入库/待确认",
    "入库/拒绝",
    "归类/待归类",
    "pending",
    "rejected",
}


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            pass
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(text: str) -> tuple[dict[str, object], str, str]:
    if not text.startswith("---"):
        return {}, text, ""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not match:
        return {}, text, ""
    raw = match.group(1)
    body = text[match.end() :]
    meta: dict[str, object] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and current_key:
            value = stripped[2:].strip().strip("'\"")
            meta.setdefault(current_key, [])
            if isinstance(meta[current_key], list):
                meta[current_key].append(value)
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            if not value:
                meta[key] = []
            elif value.startswith("[") and value.endswith("]"):
                meta[key] = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
            else:
                meta[key] = value.strip("'\"")
    return meta, body, raw


def meta_text(meta: dict[str, object], key: str) -> str:
    value = meta.get(key, "")
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


def meta_list(meta: dict[str, object], key: str) -> list[str]:
    value = meta.get(key, [])
    if isinstance(value, list):
        return [str(item) for item in value]
    if value:
        return [str(value)]
    return []


def find_formal_root(vault_root: Path, formal_root_arg: str | None) -> Path:
    if formal_root_arg:
        path = Path(formal_root_arg)
        return path if path.is_absolute() else vault_root / path
    for candidate in ("10_正式库", "10_formal_library", "formal", "knowledge"):
        path = vault_root / candidate
        if path.exists():
            return path
    return vault_root


def default_index_dir(formal_root: Path, index_dir_arg: str | None) -> Path:
    if index_dir_arg:
        path = Path(index_dir_arg)
        return path if path.is_absolute() else formal_root / path
    for candidate in ("00_检索索引", "00_search_index"):
        path = formal_root / candidate
        if path.exists():
            return path
    return formal_root / "00_search_index"


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def should_exclude(path: Path, root: Path, frontmatter: str) -> str | None:
    parts = set(path.relative_to(root).parts)
    excluded_parts = sorted(parts & DEFAULT_EXCLUDE_PARTS)
    if excluded_parts:
        return "path:" + ",".join(excluded_parts)
    lower_frontmatter = frontmatter.lower()
    for marker in DEFAULT_EXCLUDE_MARKERS:
        if marker.lower() in lower_frontmatter:
            return "marker:" + marker
    return None


def infer_title(path: Path, body: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    return match.group(1).strip() if match else path.stem


def infer_role(path: Path, body: str) -> str:
    rel = path.as_posix()
    name = path.name
    if "%% Begin Waypoint %%" in body:
        return "navigation"
    if "MOC" in rel or "索引" in name or "index" in name.lower() or "导读" in name:
        return "navigation"
    if "提炼卡片" in rel or "extracted_cards" in rel or "cards" in rel:
        return "stable_card"
    if "source" in rel or "raw" in rel:
        return "source_trace"
    if "project" in rel.lower() or "项目" in rel:
        return "project"
    if "日志" in rel or "daily" in rel.lower():
        return "daily_log"
    return "formal_note"


def split_sections(body: str, max_chars: int) -> list[tuple[str, str]]:
    if len(body) <= max_chars:
        return [("", body.strip())] if body.strip() else []
    matches = list(re.finditer(r"^(#{1,6})\s+(.+?)\s*$", body, re.M))
    if not matches:
        return split_long("", body, max_chars)
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        heading = match.group(2).strip()
        sections.extend(split_long(heading, body[start:end], max_chars))
    return sections


def split_long(heading: str, text: str, max_chars: int) -> list[tuple[str, str]]:
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if len(text) <= max_chars:
        return [(heading, text)] if text else []
    chunks: list[tuple[str, str]] = []
    start = 0
    overlap = min(220, max_chars // 5)
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            cut = max(text.rfind("\n\n", start, end), text.rfind("。", start, end), text.rfind(".", start, end))
            if cut > start + max_chars * 0.55:
                end = cut + 1
        chunk = text[start:end].strip()
        if chunk:
            chunks.append((heading, chunk))
        if end >= len(text):
            break
        start = max(0, end - overlap)
    return chunks


def tokenize(text: str) -> list[str]:
    text = text.lower()
    tokens = re.findall(r"[a-z0-9_+#./-]{2,}", text)
    for seq in re.findall(r"[\u4e00-\u9fff]+", text):
        if len(seq) == 1:
            tokens.append(seq)
        else:
            tokens.extend(seq[i : i + 2] for i in range(len(seq) - 1))
            if len(seq) > 2:
                tokens.extend(seq[i : i + 3] for i in range(len(seq) - 2))
    return tokens


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a dependency-free hybrid index for a Markdown vault.")
    parser.add_argument("--vault-root", default=".", help="Vault root directory")
    parser.add_argument("--formal-root", help="Formal library directory, relative to vault root when not absolute")
    parser.add_argument("--index-dir", help="Index output directory")
    parser.add_argument("--max-chars", type=int, default=1800, help="Maximum chunk size")
    args = parser.parse_args()

    vault_root = Path(args.vault_root).resolve()
    formal_root = find_formal_root(vault_root, args.formal_root)
    index_dir = default_index_dir(formal_root, args.index_dir)
    index_dir.mkdir(parents=True, exist_ok=True)

    chunks: list[dict[str, object]] = []
    excluded: list[dict[str, str]] = []
    token_counts: list[dict[str, int]] = []

    for path in sorted(formal_root.rglob("*.md")):
        text = read_text(path)
        meta, body, frontmatter = parse_frontmatter(text)
        reason = should_exclude(path, formal_root, frontmatter)
        if reason:
            excluded.append({"path": relative(path, vault_root), "reason": reason})
            continue

        title = infer_title(path, body)
        role = infer_role(path, body)
        summary = meta_text(meta, "summary")
        tags = meta_list(meta, "tags")
        preface = "\n".join(
            item
            for item in [
                f"Title: {title}",
                f"Path: {relative(path, vault_root)}",
                f"Summary: {summary}" if summary else "",
                f"Tags: {' '.join(tags)}" if tags else "",
            ]
            if item
        )
        for chunk_index, (heading, content) in enumerate(split_sections(body, args.max_chars)):
            text_for_index = f"{preface}\n\nHeading: {heading}\n\n{content}".strip()
            chunk = {
                "chunk_id": f"c{len(chunks):05d}",
                "path": relative(path, vault_root),
                "title": title,
                "heading": heading,
                "doc_role": role,
                "type": meta_text(meta, "type"),
                "status": meta_text(meta, "status"),
                "truth_status": meta_text(meta, "truth_status"),
                "summary": summary,
                "tags": tags,
                "chunk_index": chunk_index,
                "text": text_for_index,
            }
            chunks.append(chunk)
            token_counts.append(dict(Counter(tokenize(text_for_index))))

    with (index_dir / "chunks.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for chunk in chunks:
            handle.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    (index_dir / "tokens.json").write_text(json.dumps(token_counts, ensure_ascii=False), encoding="utf-8")
    (index_dir / "excluded_files.json").write_text(json.dumps(excluded, ensure_ascii=False, indent=2), encoding="utf-8")
    metadata = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "vault_root": str(vault_root),
        "formal_root": relative(formal_root, vault_root),
        "index_dir": relative(index_dir, vault_root),
        "chunk_count": len(chunks),
        "excluded_file_count": len(excluded),
        "algorithm": "bm25_plus_exact_and_role_weight",
    }
    (index_dir / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
