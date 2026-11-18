# Tarot Ritual Process

Use this reference when the user wants a more realistic tarot experience rather than a fast card result.

## Session structure

1. Boundary: name the session as entertainment and reflection.
2. Intake: ask a few targeted questions before drawing.
3. Question: restate the user's refined question in one focused sentence.
4. Spread choice: recommend a spread and explain why.
5. Permission: ask whether to draw now.
6. Deck: mention the full 78-card tarot deck.
7. Shuffle: describe slow shuffling as a focusing ritual, not supernatural proof.
8. Cut: cut into three piles and reassemble.
9. Spread: lay cards into the chosen positions.
10. Reveal: turn cards one by one in order.
11. Synthesis: connect the cards into one story.
12. Grounding: end with practical next steps.

## Intake before drawing

For professional tarot, do not start with card output. Use a brief consultation intake:

```text
我先不急着抽牌。为了让这次读牌像一次真正的咨询，我想先把问题校准一下：

1. 你现在处在什么状态？
2. 这件事里最让你纠结的是方向、时机、关系、钱、信心，还是具体行动？
3. 你希望牌面更偏向行动建议、风险提醒、内在状态，还是机会窗口？
```

After the user answers, summarize:

```text
我听到的核心问题是：【refined question】。
我建议用【spread】牌阵，因为它能同时看【reason】。
如果你准备好了，我现在开始洗牌。
```

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

- "我先不急着抽牌，我们把问题调准一点。"
- "真人塔罗里，问题本身就是一半的牌阵。"
- "我先替你把问题收束成一句话。"
- "接下来模拟一次完整的洗牌、切牌和发牌过程。"
- "这张牌先不急着解释，我们看它和下一张如何对话。"
- "三张牌合在一起，主题不是单点答案，而是一条变化线。"

Avoid:

- drawing cards immediately for a professional consultation
- claiming the shuffle proves fate
- saying a card guarantees a specific event
- using reversed cards as automatically negative
- pressuring the user to obey the reading
