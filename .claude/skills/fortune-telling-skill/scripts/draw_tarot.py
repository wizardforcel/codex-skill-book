#!/usr/bin/env python3
"""Draw tarot cards for an entertainment-oriented reading.

The script can output a simple card draw or a more immersive ritual-style
session with shuffle, cut, lay, and reveal steps.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from datetime import datetime, timezone


MAJOR = [
    ("The Fool", "愚人", ["beginning", "risk", "trust"]),
    ("The Magician", "魔术师", ["agency", "tools", "skill"]),
    ("The High Priestess", "女祭司", ["intuition", "hidden knowledge", "silence"]),
    ("The Empress", "皇后", ["care", "abundance", "embodiment"]),
    ("The Emperor", "皇帝", ["structure", "authority", "boundaries"]),
    ("The Hierophant", "教皇", ["tradition", "learning", "institution"]),
    ("The Lovers", "恋人", ["choice", "values", "union"]),
    ("The Chariot", "战车", ["direction", "will", "control"]),
    ("Strength", "力量", ["courage", "patience", "inner power"]),
    ("The Hermit", "隐士", ["solitude", "study", "inner light"]),
    ("Wheel of Fortune", "命运之轮", ["cycle", "turning point", "timing"]),
    ("Justice", "正义", ["truth", "balance", "consequence"]),
    ("The Hanged Man", "倒吊人", ["pause", "surrender", "new perspective"]),
    ("Death", "死神", ["ending", "transition", "clearing"]),
    ("Temperance", "节制", ["integration", "moderation", "rhythm"]),
    ("The Devil", "恶魔", ["attachment", "temptation", "shadow"]),
    ("The Tower", "高塔", ["disruption", "revelation", "release"]),
    ("The Star", "星星", ["hope", "renewal", "guidance"]),
    ("The Moon", "月亮", ["uncertainty", "dream", "projection"]),
    ("The Sun", "太阳", ["clarity", "joy", "vitality"]),
    ("Judgement", "审判", ["calling", "review", "awakening"]),
    ("The World", "世界", ["completion", "wholeness", "integration"]),
]

SUITS = {
    "Wands": ("权杖", ["action", "desire", "creativity", "momentum"]),
    "Cups": ("圣杯", ["emotion", "intimacy", "intuition", "belonging"]),
    "Swords": ("宝剑", ["thought", "language", "conflict", "decision"]),
    "Pentacles": ("星币", ["money", "body", "work", "stability"]),
}

MINORS = [
    ("Ace", "一", ["seed", "opening", "gift"]),
    ("Two", "二", ["choice", "duality", "exchange"]),
    ("Three", "三", ["growth", "collaboration", "first result"]),
    ("Four", "四", ["stability", "pause", "container"]),
    ("Five", "五", ["friction", "change", "challenge"]),
    ("Six", "六", ["support", "movement", "repair"]),
    ("Seven", "七", ["test", "strategy", "persistence"]),
    ("Eight", "八", ["practice", "speed", "adjustment"]),
    ("Nine", "九", ["ripening", "self-reliance", "threshold"]),
    ("Ten", "十", ["completion", "burden", "overflow"]),
    ("Page", "侍从", ["message", "beginner mind", "curiosity"]),
    ("Knight", "骑士", ["pursuit", "movement", "intensity"]),
    ("Queen", "皇后", ["receptivity", "maturity", "care"]),
    ("King", "国王", ["mastery", "responsibility", "direction"]),
]

SPREADS = {
    "single": ["Theme"],
    "three-card": ["Past / root", "Present / challenge", "Near future / advice"],
    "mind-heart-action": ["Mind", "Heart", "Action"],
    "relationship": ["You", "Other person", "Relationship dynamic"],
    "crossroads": ["Current position", "Path A", "Path B", "Hidden influence", "Advice"],
    "celtic-cross": [
        "Present",
        "Crossing challenge",
        "Root",
        "Recent past",
        "Possible direction",
        "Near future",
        "Self",
        "Environment",
        "Hope or fear",
        "Outcome tendency",
    ],
}


def build_deck() -> list[dict[str, object]]:
    deck: list[dict[str, object]] = []
    for name, zh_name, keywords in MAJOR:
        deck.append({"name": name, "zh_name": zh_name, "arcana": "Major", "keywords": keywords})
    for suit, (zh_suit, suit_keywords) in SUITS.items():
        for rank, zh_rank, rank_keywords in MINORS:
            deck.append(
                {
                    "name": f"{rank} of {suit}",
                    "zh_name": f"{zh_suit}{zh_rank}",
                    "arcana": "Minor",
                    "suit": suit,
                    "zh_suit": zh_suit,
                    "keywords": rank_keywords + suit_keywords[:2],
                }
            )
    return deck


def stable_seed(question: str, seed: str | None) -> str:
    if seed:
        return seed
    if question:
        return hashlib.sha256(question.encode("utf-8")).hexdigest()
    return datetime.now(timezone.utc).isoformat()


def cut_deck(deck: list[dict[str, object]], rng: random.Random) -> tuple[list[dict[str, object]], dict[str, object]]:
    first_cut = rng.randint(17, 31)
    second_cut = rng.randint(first_cut + 12, 61)
    piles = [deck[:first_cut], deck[first_cut:second_cut], deck[second_cut:]]
    order = [0, 1, 2]
    rng.shuffle(order)
    reassembled = [card for pile_index in order for card in piles[pile_index]]
    return reassembled, {
        "pile_sizes": [len(pile) for pile in piles],
        "reassembly_order": [index + 1 for index in order],
    }


def draw(
    spread: str,
    question: str,
    seed: str | None,
    reversed_cards: bool,
    ritual: bool = False,
) -> dict[str, object]:
    if spread not in SPREADS:
        raise SystemExit(f"Unknown spread '{spread}'. Choose one of: {', '.join(SPREADS)}")
    rng = random.Random(stable_seed(question, seed))
    deck = build_deck()
    shuffle_rounds = rng.randint(5, 9)
    for _ in range(shuffle_rounds):
        rng.shuffle(deck)
    cut_info = None
    if ritual:
        deck, cut_info = cut_deck(deck, rng)
    cards = []
    for reveal_index, (position, card) in enumerate(zip(SPREADS[spread], deck), start=1):
        orientation = "reversed" if reversed_cards and rng.random() < 0.38 else "upright"
        cards.append({"position": position, "reveal_index": reveal_index, "orientation": orientation, **card})
    result: dict[str, object] = {
        "question": question,
        "spread": spread,
        "seed": seed,
        "cards": cards,
        "note": "For entertainment and reflection; not a deterministic prediction.",
    }
    if ritual:
        result["ritual"] = {
            "deck_size": len(deck),
            "shuffle_rounds": shuffle_rounds,
            "cut": cut_info,
            "steps": [
                "Set the question and reading boundary.",
                f"Shuffle the full 78-card deck for {shuffle_rounds} rounds.",
                "Cut the deck into three piles and reassemble them.",
                f"Lay {len(cards)} card(s) into the selected spread.",
                "Reveal cards one by one and synthesize the story.",
            ],
        }
    return result


def format_markdown(result: dict[str, object]) -> str:
    lines = [
        "# Tarot Reading",
        "",
        f"Question: {result.get('question') or '(open reading)'}",
        f"Spread: `{result['spread']}`",
        "",
        "> Entertainment and reflection only; this is not a deterministic prediction.",
        "",
    ]
    ritual = result.get("ritual")
    if isinstance(ritual, dict):
        lines += [
            "## Ritual Process",
            "",
            f"- Deck: {ritual['deck_size']} cards",
            f"- Shuffle: {ritual['shuffle_rounds']} rounds",
        ]
        cut = ritual.get("cut")
        if isinstance(cut, dict):
            lines.append(f"- Cut: three piles {cut['pile_sizes']}, reassembled as {cut['reassembly_order']}")
        lines += ["- Reveal: one card at a time", ""]
    lines += ["## Cards", ""]
    for card in result["cards"]:
        orientation = "逆位" if card["orientation"] == "reversed" else "正位"
        lines.append(
            f"{card['reveal_index']}. **{card['position']}**: "
            f"{card['zh_name']} / {card['name']} ({orientation})"
        )
        lines.append(f"   Keywords: {', '.join(card['keywords'])}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Draw tarot cards as JSON or Markdown.")
    parser.add_argument("--spread", default="three-card", choices=sorted(SPREADS))
    parser.add_argument("--question", default="")
    parser.add_argument("--seed", default=None)
    parser.add_argument("--no-reversed", action="store_true")
    parser.add_argument("--ritual", action="store_true", help="Include shuffle, cut, lay, and reveal steps.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    result = draw(args.spread, args.question, args.seed, not args.no_reversed, args.ritual)
    if args.format == "markdown":
        print(format_markdown(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
