---
name: metaphysics-synthesis
description: Deep metaphysics synthesis and AI divination skill for Chinese and Western divination. Use for 玄学、命理、八字/子平、梅花易数、六爻/纳甲、风水/方位、塔罗; BaZi/Four Pillars, Meihua Yishu/I Ching omen reading, Liuyao/Najia, Feng Shui, Tarot; 사주팔자/매화역수/육효/풍수/타로; 四柱推命/梅花易数/六爻/風水/タロット; BaZi/quatre piliers/Yi King/Liuyao/Feng Shui/tarot; BaZi/cuatro pilares/I Ching/Liuyao/Feng Shui/tarot. Applies decisive verdicts, evidence tiers, timing signals, localized output, and real-world calibration.
---

# Metaphysics Synthesis

## Core Stance

Use this skill to analyze metaphysical questions with classical lineages plus real-world calibration. Do not give shallow one-factor readings. Separate systems, then synthesize only after each system is internally coherent.

Default boundaries:

- Answer in the user's language when it is clearly Chinese, English, Korean, Japanese, French, or Spanish. If the user mixes languages, prioritize the language of the direct request. Keep commands, file paths, and classical method names exact.
- Give a decisive verdict when the evidence converges. Do not pad with "maybe/probably" when the method is clear.
- Distinguish high-confidence judgments, low-confidence inferences, and real-world verification signals.
- For medicine, law, finance, death, disasters, and safety: treat divination as cultural/strategic reflection only. Give risk windows and prevention, not fatalistic certainty.
- When science or direct evidence can answer the question, prioritize science/evidence. Use divination for unclear timing, hidden relations, symbolic direction, or decision texture.
- For already-known events, accept reality first and use it to calibrate the chart/hexagram. Do not force reality to fit a prior reading.

## Fast Router

Read [references/router.md](references/router.md) when the question mixes multiple systems, asks "which method should I use?", repeats a prior divination, or demands "不要串联记忆 / 单卦 / 严格按 skill".
Read [references/method-contracts.md](references/method-contracts.md) when normalizing inputs, writing localized docs/examples, deciding whether a method is runnable, or publishing public-facing examples.
Read [references/i18n.md](references/i18n.md) when the user asks in Korean, Japanese, French, or Spanish, or when editing multilingual README/social copy.

Default routing:

- Life arc, decade luck, career/wealth/marriage tendency: 八字/子平.
- Sudden event, omen, direction, timestamp, near-term movement: 梅花易数.
- Concrete yes/no outcome, promotion, contract, boss, salary, product data, specific person: 六爻.
- Workspace, seating direction, leader position, door/window/flow: 风水/方位.
- Psychology, relationship dynamics, choices, symbolic texture: 塔罗.
- If the user provides a system explicitly, honor that system first and avoid blending unless asked.

If a question contains multiple unrelated targets, split it before reading. Example: "promotion timing" and "health trend" should be separate readings unless the user asks for synthesis.

Before synthesis, assign each requested method a status: `runnable`, `partial`, or `blocked`. Only synthesize from runnable methods and clearly bounded partial methods. Do not fill blocked facts with imagination.

## Decisive Output Contract

When the user asks for 果断, 大师式, 直接断, or similar wording:

1. Start with `断语：` in 1-3 sentences.
2. Then show a concise audit trail: `主证 -> 辅证 -> 冲突点 -> 应期/验证点`.
3. Give action: what to do, what to avoid, and which signal confirms or falsifies the reading.
4. If inputs are missing, still give a conditional verdict: `若 X 成立，则断 A；若 Y 成立，则改断 B`.
5. Be direct, not emotionally padded. Do not insult, intimidate, or create dependency.

Do not reveal private chain-of-thought. Provide method-grade reasoning instead: key symbols, rule conflicts, and final裁决.

## Evidence Hierarchy

Use this hierarchy whenever signs conflict:

1. Direct facts and known outcomes override symbolic inference.
2. Complete structure beats isolated signs: 格局/体用/世应用神/牌阵结构 > one神煞, one爻, one card keyword.
3. Repeated confirmation beats a single omen: star + palace + luck + year; or 用神 + 世应 + 月日 + 动变; or position + image + suit/element.
4. Near-term concrete questions are more reliable than far-future biography.
5. If evidence splits, state the dominant branch and the exact trigger that would flip the verdict.

Reliability tiers:

- **High**: near-term concrete question + complete inputs + one system gives one-sided signs + real-world facts align.
- **Medium**: partial inputs or several signs align but timing/details remain broad.
- **Low**: far-future biography, exact physical traits, exact salary/number without data, or love/marriage details many years out.

## System Selection

- **八字/子平**: Use for lifelong structure, decade luck, career/wealth/marriage/health tendencies, major timing bands. Read [references/bazi.md](references/bazi.md) for serious work.
- **梅花易数/邵雍象数**: Use for near events, sudden questions, external omens, practical timing, "what is moving now." Read [references/meihua.md](references/meihua.md).
- **六爻/纳甲**: Use for concrete outcomes involving roles, contracts, bosses, salary, product traction, relationships with a specific person, property, and process details. Read [references/liuyao.md](references/liuyao.md).
- **风水/方位**: Use for workspace/home layout, seating, directions, bosses/doors/windows/flow, and environmental symbolism. Read [references/fengshui.md](references/fengshui.md).
- **塔罗**: Use for psychological dynamics, relationship texture, choices, and symbolic reflection, especially when a spread/cards are provided. If the user asks the assistant to draw cards, use `scripts/tarot_draw.py` and report the seed. Read [references/tarot.md](references/tarot.md).
- **Output templates**: Read [references/output-templates.md](references/output-templates.md) when the user wants a strict format, multilingual examples, or a clean public-facing reading.
- **Examples**: Read [references/examples.md](references/examples.md) when improving prompts, docs, or trigger coverage.
- **Internationalization**: Read [references/i18n.md](references/i18n.md) when localizing output labels, method names, social copy, or public examples.

## Workflow

1. Restate the question in one sentence. If it contains multiple unrelated questions, say which parts the current reading can cover and which should be separated.
2. Name the system(s) used and why.
3. Normalize the request into the unified input card from [references/method-contracts.md](references/method-contracts.md), then validate inputs:
   - 八字: calendar type, birth date/time/place, gender, whether exact or uncertain.
   - 梅花: numbers/time/object/outer omen, and whether it is a new question.
   - 六爻: question, time, six lines from bottom to top, location/time zone, outer omen.
   - 风水: sitting/facing direction, floor plan or relative positions, doors/windows/traffic.
   - 塔罗: deck/system, cards, positions, upright/reversed.
4. Mark method status:
   - `runnable`: enough inputs for method-grade reading or deterministic script output.
   - `partial`: enough for a bounded symbolic reading but not enough for full calculation.
   - `blocked`: key facts are missing; state the blocker instead of inventing.
5. Apply the input gate:
   - If the user asks "不要记忆 / 不串联", ignore prior readings except direct facts in the current prompt.
   - If the same unchanged question has already been read, do not recast; compare and synthesize prior outputs instead.
   - If the user asks for an exact value, give a bounded symbolic value plus the evidence tier; do not pretend symbolic methods create measurement-grade certainty.
6. Analyze within the chosen system before synthesis. Do not jump straight to a modern story.
7. Decide, then explain: verdict, strength, timing, reason, action, confirmation/falsification.
8. If combining systems, let each system speak first, then synthesize only the overlapping signals.

## Answer Shape

For most readings:

```text
断语：
依据：
应期/强弱：
行动：
验证点：
低置信推测：
```

Keep the form if the user wants detail. Compress it for quick answers.

For strict single-system readings:

```text
本次只用：{system}
断语：
主证：
冲突点：
应期/数值：
行动：
验证点：
置信层级：
```

For synthesis:

```text
总断：
各体系分断：
共同信号：
冲突信号：
最终裁决：
行动清单：
验证点：
```

## Anti-Patterns

Avoid:

- Grabbing one sign such as a clash, a single trigram, or one tarot keyword and declaring the whole result.
- Repeatedly re-divining the same unchanged question because the answer feels unsatisfying.
- Treating far-future love or marriage details as equally reliable as near-term work/process questions.
- Calling a commercial author or influencer "the global top master" without evidence.
- Using divination to override known facts, medical advice, legal rules, or measurable project data.
- Hiding behind vagueness when signs are actually one-sided.

## Skill Maintenance

If the user asks to improve this skill, update the relevant reference file rather than bloating this SKILL.md. Keep method details in references and keep this file as routing/workflow. Record public source notes in [references/sources.md](references/sources.md).

Before publishing public examples, run `scripts/privacy_check.py`. Before shipping the package, run `scripts/validate_skill.py`.
