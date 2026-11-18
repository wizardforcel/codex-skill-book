#!/usr/bin/env python3
"""Summarize five-element balance from Chinese stems and branches."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter


STEMS = {
    "甲": {"element": "Wood", "yin_yang": "Yang"},
    "乙": {"element": "Wood", "yin_yang": "Yin"},
    "丙": {"element": "Fire", "yin_yang": "Yang"},
    "丁": {"element": "Fire", "yin_yang": "Yin"},
    "戊": {"element": "Earth", "yin_yang": "Yang"},
    "己": {"element": "Earth", "yin_yang": "Yin"},
    "庚": {"element": "Metal", "yin_yang": "Yang"},
    "辛": {"element": "Metal", "yin_yang": "Yin"},
    "壬": {"element": "Water", "yin_yang": "Yang"},
    "癸": {"element": "Water", "yin_yang": "Yin"},
}

BRANCHES = {
    "子": {"element": "Water", "hidden_stems": ["癸"]},
    "丑": {"element": "Earth", "hidden_stems": ["己", "癸", "辛"]},
    "寅": {"element": "Wood", "hidden_stems": ["甲", "丙", "戊"]},
    "卯": {"element": "Wood", "hidden_stems": ["乙"]},
    "辰": {"element": "Earth", "hidden_stems": ["戊", "乙", "癸"]},
    "巳": {"element": "Fire", "hidden_stems": ["丙", "戊", "庚"]},
    "午": {"element": "Fire", "hidden_stems": ["丁", "己"]},
    "未": {"element": "Earth", "hidden_stems": ["己", "丁", "乙"]},
    "申": {"element": "Metal", "hidden_stems": ["庚", "壬", "戊"]},
    "酉": {"element": "Metal", "hidden_stems": ["辛"]},
    "戌": {"element": "Earth", "hidden_stems": ["戊", "辛", "丁"]},
    "亥": {"element": "Water", "hidden_stems": ["壬", "甲"]},
}

ELEMENTS = ["Wood", "Fire", "Earth", "Metal", "Water"]
CN_ELEMENT = {"Wood": "木", "Fire": "火", "Earth": "土", "Metal": "金", "Water": "水"}


def analyze(text: str, include_hidden: bool) -> dict[str, object]:
    chars = re.findall(r"[甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥]", text)
    visible = Counter()
    hidden = Counter()
    tokens = []

    for char in chars:
        if char in STEMS:
            element = STEMS[char]["element"]
            visible[element] += 1
            tokens.append({"char": char, "type": "stem", **STEMS[char]})
        elif char in BRANCHES:
            element = BRANCHES[char]["element"]
            visible[element] += 1
            token = {"char": char, "type": "branch", **BRANCHES[char]}
            tokens.append(token)
            if include_hidden:
                for stem in BRANCHES[char]["hidden_stems"]:
                    hidden[STEMS[stem]["element"]] += 1

    total = Counter({element: visible[element] + hidden[element] for element in ELEMENTS})
    strongest = [e for e, count in total.items() if count == max(total.values(), default=0)]
    weakest = [e for e, count in total.items() if count == min(total.values(), default=0)]

    return {
        "input": text,
        "tokens": tokens,
        "visible_counts": {CN_ELEMENT[e]: visible[e] for e in ELEMENTS},
        "hidden_counts": {CN_ELEMENT[e]: hidden[e] for e in ELEMENTS} if include_hidden else {},
        "total_counts": {CN_ELEMENT[e]: total[e] for e in ELEMENTS},
        "strongest": [CN_ELEMENT[e] for e in strongest if total[e] > 0],
        "weakest": [CN_ELEMENT[e] for e in weakest],
        "note": "This is a symbolic five-element summary, not a full Bazi calculation.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize five-element balance from stems/branches.")
    parser.add_argument("pillars", help="Chinese stems/branches, e.g. '甲子 丙寅 辛巳 壬辰'")
    parser.add_argument("--no-hidden", action="store_true", help="Ignore hidden stems in branches.")
    args = parser.parse_args()

    print(json.dumps(analyze(args.pillars, not args.no_hidden), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
