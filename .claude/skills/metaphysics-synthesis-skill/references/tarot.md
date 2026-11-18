# Tarot Reference

## Core Lineage

Default to Rider-Waite-Smith (RWS):

- A. E. Waite: esoteric structure and The Pictorial Key tradition.
- Pamela Colman Smith: visual storytelling and card imagery; treat the image as primary evidence.
- Rachel Pollack: symbolic, mythic, psychological integration.
- Mary K. Greer: interactive, reflective, reader-centered technique.

Use Thoth only when user explicitly uses Thoth/Crowley deck:

- Aleister Crowley and Lady Frieda Harris: astrological, Qabalistic, elemental, and Thoth-specific symbolism.

## Input Gate

1. Confirm question, spread, deck, and whether reversals are used.
2. If no spread is given, choose a compact spread:
   - One card: immediate tone.
   - Three cards: situation / obstacle / direction.
   - Five cards: past trigger / current / hidden factor / advice / likely outcome.
3. For predictive questions, define horizon. Tarot is weaker when the time range is vague.

## Draw Discipline

Use these rules when the user asks the assistant to draw cards:

1. If the user already provides cards, do not redraw. Interpret the provided cards and positions.
2. If the user asks for a draw but gives no cards, run:

   ```bash
   python scripts/tarot_draw.py --spread three --question "..."
   ```

   Use `--json` if the result will be parsed or copied into a report.
3. Always show the spread name and seed. The seed makes the draw reproducible and prevents "redraw until desired answer."
4. Do not redraw the same unchanged question. A new draw needs a new question, a new time window, or a clearly new decision point.
5. Treat the script as a symbolic randomization tool, not physical supernatural proof. The reading still depends on spread structure and interpretation.

## Spread Selection

| User need | Spread | Why |
| --- | --- | --- |
| Quick tone or daily focus | `single` | One direct anchor card. |
| General direction | `three` | Situation / obstacle / direction. |
| Timing arc | `past-present-future` | Clean story line. |
| Two choices | `decision` | Compares paths without over-reading. |
| Relationship dynamic | `relationship` | Separates user, other person, bond, obstacle, next step. |
| Serious process question | `five` | Adds hidden factor and likely outcome. |
| Deep life cross-section | `celtic` | Use sparingly; it is broad and slower. |

## Master-Style Reading Order

1. Read position first, then card image, then title/keyword.
2. Scan the whole spread before card-by-card detail:
   - major/minor/court distribution.
   - suits and elements.
   - numbers and sequences.
   - direction of figures and gaze.
   - repeated symbols, colors, tools, landscapes, weather.
   - reversals as blocked/internal/overdone/delayed, not automatically negative.
3. Identify the anchor card: the card that best answers the question or changes the rest of the spread.
4. Read interactions:
   - Who looks at whom?
   - Which card moves toward or away?
   - Which suit dominates or is missing?
   - Is the outcome card supported by the path cards?
5. Separate event pattern, psychological dynamic, advice/action, and verification signs.

## Decisive Verdict Rules

- If the outcome card, anchor card, and majority tone align, give a direct yes/no/leaning verdict.
- If the spread is split, name the dominant force and the turning card.
- Major Arcana concentration: larger life/theme pressure; less controllable by small tactics.
- Court card concentration: people, roles, maturity, or social dynamics are central.
- Sword dominance: thought, conflict, contracts, truth, anxiety.
- Cup dominance: emotion, attachment, relationship, taste, memory.
- Wand dominance: drive, initiative, conflict, speed, ambition.
- Pentacle dominance: money, body, work, material proof, time.
- Missing suit: missing resource or blind spot.

Use this structure:

```text
结论：直接回答。
牌面主证：位置 + 图像 + 互动。
阻力/转机：哪张牌卡住，哪张牌打开。
行动：该做/不该做。
验证：未来会出现什么信号。
```

## Ethics and Boundaries

- Avoid fatalism. Tarot is best for relationship texture, decision reflection, and hidden motivations, not deterministic long-range biography.
- Do not replace medical, legal, financial, or safety advice.
- For third-party mind-reading questions, focus on observable dynamics and user choices rather than claiming total access to another person's mind.
- Do not repeatedly redraw until the user likes the answer.
- Avoid generic Barnum readings. Every claim must tie back to card position, imagery, suit/element distribution, or card interaction.

## Reversals

Read reversals by context:

- blocked: energy cannot express.
- internalized: happening inside rather than outside.
- excessive: too much of the upright quality.
- delayed: not yet active.
- shadow: the card's lesson is avoided.

Choose one reversal mode from spread evidence; do not stack all meanings.
