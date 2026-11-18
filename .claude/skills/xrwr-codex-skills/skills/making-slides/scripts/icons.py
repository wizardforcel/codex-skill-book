"""Search the bundled Lucide icons and print them as JSX helpers for slide SVGs.

Usage:
    python icons.py search <word> [<word> ...]     # names whose name or tags match all words
    python icons.py jsx <name> [<name> ...]        # print one helper per icon

Each helper is a lowercase function to paste above `export default`:
    const iLightbulb = (x, y, s, c, f = 'none') => <g transform=...>...</g>;
Call it inside the SVG as `{iLightbulb(64, 440, 40, N)}`: (x, y) is the top-left corner,
s the size in viewBox units, c the stroke colour, f an optional fill colour.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets" / "lucide"
ATTR_NAMES = {"stroke-width": "strokeWidth", "fill-rule": "fillRule", "clip-rule": "clipRule"}


def _load() -> tuple[dict[str, list], dict[str, list[str]]]:
    nodes = json.loads((ASSETS / "icon-nodes.json").read_text(encoding="utf-8"))
    tags = json.loads((ASSETS / "tags.json").read_text(encoding="utf-8"))
    return nodes, tags


def search(words: list[str]) -> list[str]:
    nodes, tags = _load()
    words = [w.lower() for w in words]
    hits = []
    for name in sorted(nodes):
        haystack = " ".join([name, *tags.get(name, [])]).lower()
        if all(w in haystack for w in words):
            hits.append(name)
    return hits


def _camel(name: str) -> str:
    return "i" + "".join(part.capitalize() for part in name.split("-"))


def jsx(name: str) -> str:
    nodes, _ = _load()
    if name not in nodes:
        raise SystemExit(f"unknown icon {name!r}; try: python icons.py search <word>")
    parts = []
    for tag, attrs in nodes[name]:
        rendered = " ".join(f"{ATTR_NAMES.get(k, k)}='{v}'" for k, v in attrs.items())
        parts.append(f"<{tag} {rendered}/>")
    body = "".join(parts)
    return (
        f"const {_camel(name)} = (x, y, s, c, f = 'none') => "
        "<g transform={`translate(${x} ${y}) scale(${s / 24})`} fill={f} stroke={c} "
        f"strokeWidth='2' strokeLinecap='round' strokeLinejoin='round'>{body}</g>;"
    )


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] not in {"search", "jsx"}:
        print(__doc__, file=sys.stderr)
        return 2
    if sys.argv[1] == "search":
        hits = search(sys.argv[2:])
        print("\n".join(hits) if hits else "no match")
    else:
        for name in sys.argv[2:]:
            print(jsx(name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
