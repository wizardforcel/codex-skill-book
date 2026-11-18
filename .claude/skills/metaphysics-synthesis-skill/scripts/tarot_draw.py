#!/usr/bin/env python3
"""Deterministic-friendly Tarot draw helper.

This script outputs card names, spread positions, orientation, seed, and timestamp.
It intentionally does not include copyrighted deck art or long card meanings.
"""

from __future__ import annotations

import argparse
import json
import random
import secrets
from datetime import datetime, timezone


MAJOR = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World",
]

SUITS = {
    "Wands": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"],
    "Cups": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"],
    "Swords": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"],
    "Pentacles": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"],
}

SPREADS = {
    "single": ["Focus"],
    "three": ["Situation", "Obstacle", "Direction"],
    "past-present-future": ["Past", "Present", "Future"],
    "decision": ["Option A", "Option B", "Advice"],
    "relationship": ["You", "Other", "Bond", "Obstacle", "Next Step"],
    "five": ["Past Trigger", "Current State", "Hidden Factor", "Advice", "Likely Outcome"],
    "celtic": [
        "Present", "Challenge", "Root", "Past", "Possible Outcome", "Near Future",
        "Self", "Environment", "Hope/Fear", "Outcome",
    ],
}


def deck() -> list[str]:
    cards = [f"{name} (Major Arcana)" for name in MAJOR]
    for suit, ranks in SUITS.items():
        cards.extend(f"{rank} of {suit}" for rank in ranks)
    return cards


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draw Tarot cards for a spread.")
    parser.add_argument("--spread", default="three", choices=sorted(SPREADS.keys()))
    parser.add_argument("--seed", type=int, default=None, help="Optional seed for reproducible draws.")
    parser.add_argument("--question", default="", help="Optional reading question.")
    parser.add_argument("--no-reversals", action="store_true", help="Disable reversed cards.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of text.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    seed = args.seed if args.seed is not None else secrets.randbits(63)
    rng = random.Random(seed)
    positions = SPREADS[args.spread]
    cards = rng.sample(deck(), len(positions))
    rows = []
    for position, card in zip(positions, cards):
        orientation = "Upright" if args.no_reversals or rng.random() >= 0.5 else "Reversed"
        rows.append({"position": position, "card": card, "orientation": orientation})

    payload = {
        "spread": args.spread,
        "question": args.question,
        "seed": seed,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cards": rows,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print(f"spread: {payload['spread']}")
    if args.question:
        print(f"question: {args.question}")
    print(f"seed: {seed}")
    for idx, row in enumerate(rows, start=1):
        print(f"{idx}. {row['position']}: {row['card']} — {row['orientation']}")


if __name__ == "__main__":
    main()
