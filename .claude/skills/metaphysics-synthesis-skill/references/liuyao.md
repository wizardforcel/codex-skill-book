# 六爻 / 纳甲 Reference

## Core Lineage

Use 纳甲六爻. Reference:

- 《火珠林》: early framework.
- 《增删卜易》: practical, case-driven, emphasizes 用神, reality checks, and repeatable tests.
- 《卜筮正宗》: structured rules and classical method.

## Input Gate

1. Lock one concrete question and a time range.
2. Record casting time, place/time zone, method, and six lines from bottom to top.
3. If the user asks several outcomes, split them. One卦 should not carry unrelated questions.
4. Do not re-cast an unchanged question unless a new factual trigger appears.

## Line Input Contract

Six-line divination fails when the line order or numeric mapping is ambiguous. Use this contract:

```json
{
  "question": "",
  "casting_time": "",
  "timezone": "",
  "method": "coins|numbers|manual_hexagram|unknown",
  "lines_bottom_to_top": [],
  "moving_lines": [],
  "month_branch": "",
  "day_branch": "",
  "najia_available": false
}
```

Rules:

- Always state that the first line is the bottom line. If the user writes "第一爻", interpret it as 初爻 unless they explicitly say top-down.
- If numbers are used, state the mapping before reading. If mapping is not available, read hexagram structure only and mark Najia detail `partial`.
- If month/day, 世应, 六亲, or 纳甲 cannot be established, do not claim a full 纳甲六爻 judgment.
- Do not simulate coin throws unless the user asks. If a simulation is used, show seed or method so the cast is not silently mutable.

## Master-Style Reading Order

1. Build 本卦, 变卦, 世应, 纳甲, 六亲, 六神, 旬空.
2. Choose 用神 from the actual question:
   - Position/job/title/pressure: 官鬼.
   - Contract/document/process/evidence: 父母.
   - Salary, money, budget, deal value: 妻财.
   - Output/product/metrics/relief: 子孙.
   - Competition/peers/resource drain: 兄弟.
   - Company/counterparty/person asked about: 应爻 when context fits.
3. Judge 用神:
   - 月建 and 日辰 support/damage first.
   - 动爻 and变爻 next.
   - 生克冲合刑害, 空亡, 墓, 绝, 破.
   - 伏神/飞神 if the relevant sign is hidden.
   - 回头生/回头克, 进神/退神 where applicable.
4. Judge 世爻 and 应爻:
   - 世 is user capacity, position, intent, and current condition.
   - 应 is other side, external process, institution, partner, or market.
   - 用神生世/合世 is usable support; 用神克世 or 世克用 may show pressure, rejection, cost, or user forcing the matter.
5. Judge the process:
   - Which line moves?
   - Does movement rescue or damage the use-god?
   - Does the change hexagram show completion, delay, reversal, or new condition?
6. Determine verdict, timing, blocker, helper, and practical move.

## Decisive Verdict Rules

- **Likely yes / can happen**: 用神旺相, not empty/broken, moves to生世/合世, or 世 and用神 are both supported by月日.
- **Likely no / hard to happen**: 用神衰弱, 空破墓绝, repeatedly克 by月日/动爻, and no rescue.
- **Delayed**: 用神空而有气, 入墓待冲, 被合待冲, or世/应 not connected yet.
- **Costly yes**: matter can happen but兄弟/官鬼/回头克 shows price, pressure, paperwork, or conflict.
- **Hidden factor**: 用神伏藏, 应爻异常, or 六神/伏神 points to unspoken person, document, fear, or resource.

When signs are mixed, do not soften into vagueness. State: dominant verdict, obstacle, and what sign would flip the result.

## Role Mapping for Practical Questions

- Job offer: 官鬼=role, 父母=offer/contract/HR, 财=salary, 应=company, 兄弟=competitors.
- Promotion: 官鬼=title/authority, 父母=document/process, 印-like support via parent line, 世=readiness.
- Product/project: 子孙=output/user-visible result, 财=monetization, 父母=requirements/documents, 官鬼=bug/risk/regulation.
- Relationship: 应=other person, 世=querent, 财/官 depending on role context, 子孙=ease/joy, 官鬼=pressure/fear.
- Property: 父母=house/document, 财=price/value, 官鬼=legal/risk, 应=seller/other party.

## Timing / 应期

Use the earliest credible activation:

1. 出空 when an empty but useful sign becomes active.
2. 冲合 when a stuck, joined, or blocked relation is released.
3. 出墓/开库 when a sign hidden in tomb/storehouse is opened.
4. 旺日/月 when the use-god gains seasonal or daily force.
5. 动爻 number or hexagram number only as auxiliary timing, never alone.

## Cautions

- Month/day strength usually outweighs decorative 六神 storytelling.
- 六神 adds texture: 青龙 joy/help, 朱雀 speech/document, 勾陈 delay/land, 腾蛇 worry/entanglement, 白虎 injury/conflict, 玄武 hidden/private. It should not overturn core use-god strength.
- Do not promise medical/legal/financial outcomes. Give risk signals and practical checks.
