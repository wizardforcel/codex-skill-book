#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from build_hybrid_index import default_index_dir, find_formal_root, tokenize


def load_chunks(path: Path) -> list[dict[str, object]]:
    chunks: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                chunks.append(json.loads(line))
    return chunks


def bm25(query: str, token_counts: list[dict[str, int]]) -> list[float]:
    query_terms = Counter(tokenize(query))
    doc_lengths = [sum(counts.values()) for counts in token_counts]
    avgdl = sum(doc_lengths) / max(1, len(doc_lengths))
    df = Counter()
    for counts in token_counts:
        df.update(counts.keys())
    n = max(1, len(token_counts))
    k1 = 1.5
    b = 0.75
    scores: list[float] = []
    for counts, length in zip(token_counts, doc_lengths):
        score = 0.0
        for term in query_terms:
            freq = int(counts.get(term, 0))
            if not freq:
                continue
            idf = math.log((n - df[term] + 0.5) / (df[term] + 0.5) + 1.0)
            denom = freq + k1 * (1 - b + b * length / max(1.0, avgdl))
            score += idf * (freq * (k1 + 1)) / denom
        scores.append(score)
    return scores


def role_weight(role: str) -> float:
    return {
        "stable_card": 0.20,
        "formal_note": 0.12,
        "project": 0.10,
        "reference": 0.06,
        "daily_log": 0.02,
        "navigation": -0.18,
        "source_trace": -0.12,
    }.get(role, 0.0)


def exact_bonus(query: str, chunk: dict[str, object]) -> float:
    fields = " ".join(str(chunk.get(key, "")) for key in ("title", "heading", "summary", "path", "tags")).lower()
    bonus = 0.0
    for token in re.findall(r"[\u4e00-\u9fff]{2,}|[a-z0-9_+#./-]{2,}", query.lower()):
        if token in fields:
            bonus += 0.08
    return min(bonus, 0.30)


def snippet(text: str, query: str, width: int = 180) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    lower = compact.lower()
    start = 0
    for term in tokenize(query):
        index = lower.find(term.lower())
        if index >= 0:
            start = max(0, index - width // 3)
            break
    return compact[start : start + width]


def main() -> None:
    parser = argparse.ArgumentParser(description="Search a dependency-free Markdown vault hybrid index.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--vault-root", default=".", help="Vault root directory")
    parser.add_argument("--formal-root", help="Formal library directory")
    parser.add_argument("--index-dir", help="Index directory")
    parser.add_argument("--top", type=int, default=8, help="Number of results")
    parser.add_argument("--no-dedupe", action="store_true", help="Show multiple chunks from the same file")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    vault_root = Path(args.vault_root).resolve()
    formal_root = find_formal_root(vault_root, args.formal_root)
    index_dir = default_index_dir(formal_root, args.index_dir)

    chunks = load_chunks(index_dir / "chunks.jsonl")
    token_counts = json.loads((index_dir / "tokens.json").read_text(encoding="utf-8"))
    raw_scores = bm25(args.query, token_counts)
    max_score = max(raw_scores) if raw_scores else 0.0

    results = []
    for index, chunk in enumerate(chunks):
        normalized = raw_scores[index] / max_score if max_score > 0 else 0.0
        score = normalized + exact_bonus(args.query, chunk) + role_weight(str(chunk.get("doc_role", "")))
        results.append(
            {
                "score": round(score, 4),
                "path": chunk.get("path"),
                "title": chunk.get("title"),
                "heading": chunk.get("heading"),
                "doc_role": chunk.get("doc_role"),
                "summary": chunk.get("summary"),
                "snippet": snippet(str(chunk.get("text", "")), args.query),
            }
        )

    results.sort(key=lambda item: item["score"], reverse=True)
    if not args.no_dedupe:
        deduped = []
        seen = set()
        for result in results:
            if result["path"] in seen:
                continue
            seen.add(result["path"])
            deduped.append(result)
        results = deduped
    results = results[: max(1, args.top)]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    for idx, result in enumerate(results, start=1):
        print(f"{idx}. score={result['score']} role={result['doc_role']}")
        print(f"   {result['title']}")
        if result["heading"]:
            print(f"   heading: {result['heading']}")
        print(f"   path: {result['path']}")
        if result["summary"]:
            print(f"   summary: {result['summary']}")
        print(f"   {result['snippet']}")
        print()


if __name__ == "__main__":
    main()
