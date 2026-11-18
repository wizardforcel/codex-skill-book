# Tarot Ritual Process

Use this reference when the user wants a more realistic tarot experience rather than a fast card result.

## Session structure

1. Boundary: name the session as entertainment and reflection.
2. Question: restate the user's question in one focused sentence.
3. Deck: mention the full 78-card tarot deck.
4. Shuffle: describe slow shuffling as a focusing ritual, not supernatural proof.
5. Cut: cut into three piles and reassemble.
6. Spread: lay cards into the chosen positions.
7. Reveal: turn cards one by one in order.
8. Synthesis: connect the cards into one story.
9. Grounding: end with practical next steps.

## Script

Use `scripts/draw_tarot.py --ritual` when the user does not choose physical cards or wants the system to draw:

```bash
python scripts/draw_tarot.py --ritual --spread three-card --format markdown --question "我接下来三个月的事业状态如何？"
```

The ritual output includes:

- deck size
- shuffle rounds
- three-pile cut sizes
- pile reassembly order
- reveal order
- bilingual card names
- orientation
- keywords

## Reading tone

Good phrases:

- "我先替你把问题收束成一句话。"
- "接下来模拟一次完整的洗牌、切牌和发牌过程。"
- "这张牌先不急着解释，我们看它和下一张如何对话。"
- "三张牌合在一起，主题不是单点答案，而是一条变化线。"

Avoid:

- claiming the shuffle proves fate
- saying a card guarantees a specific event
- using reversed cards as automatically negative
- pressuring the user to obey the reading
