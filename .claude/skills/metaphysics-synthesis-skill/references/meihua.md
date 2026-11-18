# 梅花易数 / 邵雍象数 Reference

## Core Lineage

Use 邵雍象数 thought and the common 《梅花易数》 method. Read the hexagram as living image:

- 主卦: current form.
- 互卦: inner process/hidden middle.
- 变卦: outcome/tendency.
- 体用: self/root vs matter/other/function.
- 动爻: trigger, stage, turning point.
- 外应: live omen that specifies role, direction, person, or timing; it must not replace the hexagram.
- 卦爻辞: classical texture and stage language, not literal-only prediction.

## Input Gate

1. Confirm this is one question and a fresh moment.
2. Record the 起卦 source: time, number, sound, object, direction, outer omen, or user-provided numbers.
3. State the number rule used so the reading can be reproduced.
4. If many questions are packed together, read the central qi only and ask for separation.
5. Enforce the classical discipline: 无疑不卜, 不动不占, and do not keep recasting the same unchanged question. If the user has asked the same matter repeatedly, preserve the earlier main hexagram and use new omens only for changed facts or sub-questions.

## Casting Rules

Use 先天八卦数 unless the user provides another method:

| Trigram | Number | Element |
| --- | ---: | --- |
| 乾 | 1 | 金 |
| 兑 | 2 | 金 |
| 离 | 3 | 火 |
| 震 | 4 | 木 |
| 巽 | 5 | 木 |
| 坎 | 6 | 水 |
| 艮 | 7 | 土 |
| 坤 | 8 | 土 |

- Time casting: year + month + day gives the upper trigram; year + month + day + earthly-branch hour gives the lower trigram and moving line. Use modulo 8 for trigram, modulo 6 for line; a remainder of 0 means 坤 for trigram and the 6th line for moving line.
- Number casting: two numbers give upper/lower trigrams; a third number can directly give the moving line. If six line numbers are provided, prefer 六爻/纳甲 unless the user explicitly says梅花.
- Same-hour separation: if the user deliberately asks several fresh questions within one时辰 and needs separate梅花卦, minutes may be used as a sub-hour refinement. State this exception explicitly.
- Sound, color, direction, size, object, and sudden movement can all start or refine a hexagram, but the rule must be named before judging.
- For strict or repeated calculation checks, run `scripts/meihua_calc.py` from this skill folder. It supports the skill's solar convention, number casting, and a classic lunar-branch mode; it outputs 主卦, 互卦, 变卦, 动爻, and体用生克. Interpretation still follows this reference.

## Master-Style Reading Order

1. Cast upper/lower trigrams and moving line.
2. Build 主卦, 互卦, 变卦.
3. Set 体用:
   - Common: moving trigram often 用, unmoving often 体.
   - Adjust by question context and state the mapping.
   - For work/relationship, name who/what each side represents.
4. Judge five-element relation:
   - 用生体: matter/person helps user.
   - 体生用: user spends energy/resources into matter.
   - 体克用: user can control/overcome matter.
   - 用克体: matter pressures/damages user.
   - 比和: same qi, cooperation, sameness, or stalemate depending on movement.
5. Add seasonal strength if timing/context makes it relevant:
   - Spring favors 震/巽 wood.
   - Summer favors 离 fire.
   - Autumn favors 乾/兑 metal.
   - Winter favors 坎 water.
   - Season-end/transition favors 坤/艮 earth.
6. Read image:
   - 乾: authority, father, rules, leadership, head, metal, northwest.
   - 坤: platform, mother, land, organization, support, mass, southwest.
   - 震: movement, launch, sound, project start, east.
   - 巽: wind, entry, information, AI/search/traffic, writing, hair, southeast.
   - 坎: risk, hidden flow, data, water, anxiety, obstacle, north.
   - 离: visibility, data, screen, documents, reputation, fire, south.
   - 艮: stop, boundary, team wall, mountain, stillness, northeast.
   - 兑: speech, joy, mouth, negotiation, west.
7. Check whether 互卦 or 变卦 provides a 通关 element when体用相克:
   - 金克木 -> 水通关.
   - 木克土 -> 火通关.
   - 土克水 -> 金通关.
   - 水克火 -> 木通关.
   - 火克金 -> 土通关.
8. Use 动爻 and 卦辞/爻辞 to locate stage and manner.
9. Use 外应 to narrow the concrete person, object, direction, or trigger.
10. Give 应期 through multiple signals: number, moving line, trigram number, element season, question horizon, and real-world schedule.

## External Omens / 十应 Lens

Classify the omen before interpreting it. Do not free-associate endlessly.

- 天时: weather, light, heat/cold, rain, wind, thunder.
- 地理: building, floor, road, water, tree, mountain, elevator, doorway, desk, seat.
- 人事: who appears, age/role/gender, conversation, laughter, argument, silence.
- 时令: season, workday/holiday, morning/noon/night, deadline pressure.
- 方位: where the omen happens relative to the user; use 后天八卦方向 for concrete space.
- 声音: ringtone, speech, music, sudden sound, animal sound, notification.
- 颜色/形状: visible colors, square/round/sharp/broken forms.
- 动作/身体: scratch, yawn, cough, head/hand/foot movement, pain, itch, heat, fatigue.

Rule: an omen specifies "who/where/how/when" only after the hexagram's体用 and主互变 have decided the main trend.

## Decisive Verdict Rules

- 体旺 and用生体: direct favorable verdict.
- 用旺克体: external pressure is real; do not call it "minor" unless there is rescue in互/变.
- 体克用: user has leverage, but may need action; if体弱, leverage is nominal.
- 体生用: user pays effort, money, emotion, or attention; outcome depends on whether变卦 returns support.
- 比和: easy contact or same camp; if movement is weak, it can also mean no breakthrough.
- If体用相克 but互卦/变卦 contains the bridge element, read as "blocked but can be resolved through a middle process"; name that practical bridge.
- If本卦 is favorable but互卦 is obstructive, the surface is good but the process has hidden cost.
- If本卦 is obstructive but互卦 or变卦 returns support, the matter starts blocked but can open after a concrete trigger.

Conflict hierarchy:

1. 体用生克 controls the main verdict.
2. 主卦 shows present condition; 互卦 shows hidden process; 变卦 shows trend.
3. 动爻 locates the trigger.
4. 外应 sharpens detail but cannot overturn a clear体用 relation.
5. 卦爻辞 gives tone/stage after the above are settled.

## Timing / 应期

- For near events, use moving line number, trigram number, or generated number as days/weeks/months only after matching the question horizon.
- Element seasons can widen timing: wood spring, fire summer, metal autumn, water winter, earth transition/month-end nodes.
- Use 成卦之数 as an auxiliary timing number, then choose the unit by question scale: hours for same-day matters, days for near work/process matters, weeks for project rollouts, months for year-scale issues.
- User state refines speed: walking/active tends faster; standing/neutral tends medium; sitting/resting tends slower.
- 用生体 or体旺 tends earlier; 用克体, 体生用, 艮/坤-heavy stillness, or negative互卦 tends later.
- If real-world schedules exist, align the symbolic number to the nearest plausible checkpoint.
- Do not force exact dates for far-future or emotionally charged questions.

## Topic Lenses

- Work/promotion: 乾=authority/rules, 坤=platform/organization, 离=visibility/data/documents, 巽=traffic/search/information, 兑=feedback/speech, 震=launch/action, 艮=block/boundary, 坎=risk/hidden flow.
- Product/traffic: 巽 and震 show launch and spreading; 坎 shows data flow and hidden risk; 离 shows dashboards and public visibility; 兑 shows user feedback and discussion.
- Relationship: use体用 for user/other, but rely on image and omens for meeting mode. Do not overclaim exact spouse biography from梅花 alone.
- Health/body: treat as symbolic and cultural only; prefer medical evidence and safety advice for real interventions.

## Reliability

Best for:

- Recent events.
- "Who moves this?"
- "What is the hidden trigger?"
- "When will this show?"
- Outer-omen-rich moments.

Weaker for:

- Far-future exact spouse details.
- Exact death/disaster year.
- Many unrelated questions in one hexagram.

## Direct Style

If the user asks for decisive 邵雍-style language, give a direct断语 first. Still show the supporting images. Use strong wording when体用 and变卦 align; use conditional wording only when the hexagram itself splits.
