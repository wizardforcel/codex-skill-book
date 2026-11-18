# 八字 / 子平 Reference

## Core Lineage

Use 子平法 as the default. Consult these method lenses:

- 《渊海子平》: basic ten gods, structures, classical Zi Ping foundation.
- 《三命通会》: broad case tradition, gods/sha, patterns, life-event references.
- 《滴天髓》 and 任铁樵 commentary: qi flow, strength, disease/medicine, passage through luck cycles.
- 《子平真诠》 and 沈孝瞻/徐乐吾 lineage: 月令取格, 用神, 相神, 清浊, success/failure/salvage of structure.
- 《穷通宝鉴》: monthly command, climate, 调候, cold/hot/dry/wet balance.
- Modern case lenses: 徐乐吾, 韦千里, 袁树珊 as calibration references, never as a single authority.

## Input Gate

Before judging:

1. Confirm solar/lunar calendar, birth date, time, place, gender, and time zone.
2. If the birth time is near a two-hour boundary, produce branch alternatives instead of pretending certainty.
3. If place/time implies true solar time correction and the hour may change, flag it before judging.
4. If only date is known, read structure and luck coarsely; do not judge spouse/children/hour-pillar details.

## Canonical Data Contract

For serious BaZi work, normalize the data before interpretation:

```json
{
  "calendar_type": "solar|lunar|unknown",
  "birth_date": "YYYY-MM-DD",
  "birth_time": "HH:MM",
  "birth_place": "city/country",
  "timezone": "IANA timezone if known",
  "gender": "",
  "hour_convention": "early_zi|late_zi|unknown",
  "true_solar_time_checked": false,
  "chart_source": "tool|user_provided|manual_estimate"
}
```

If any field is uncertain, mark the reading `partial`. Do not present spouse, children, and hour-pillar conclusions as fixed when the hour pillar can change.

## Calculation vs Interpretation

Borrow this engineering discipline from strong BaZi tools: calculate first, interpret second.

- Deterministic layer: calendar conversion, four pillars, hidden stems, ten gods, twelve growth stages, luck cycles, annual/monthly pillars.
- Interpretive layer: 格局, 用神, 调候, event timing, life strategy, and real-world action.
- If no reliable calculator or user-provided chart is available, say the deterministic layer is approximate and keep the verdict narrower.
- Public examples must be fictional. Never publish real names, exact birth details, workplace facts, family facts, or private life events.

## Master-Style Reading Order

1. **Set the question**: career, wealth, marriage, family, health tendency, timing, or life structure. Do not read everything with equal force.
2. **Establish 日主 and 月令**: season, command qi, root,透干,藏干, and climate.
3. **Build the original chart**:
   - 十神 distribution and role balance.
   - 藏干/透干 and whether useful qi is exposed, hidden, blocked, or mixed.
   - 根气, 得令/得地/得助, and qi flow.
   - 格局, 用神, 相神, 忌神, 仇神, 闲神.
   - 调候 need: cold/hot/dry/wet first when climate is severe.
   - 宫位: 年/月/日/时, especially spouse palace, parents, children, career stage.
   - 刑冲合害破, 墓库, 空亡 if used.
4. **Run two lenses in order**:
   - 格局 lens: 月令定格, see whether格成, 格败, 有救, 有情, 清 or浊.
   - 旺衰/病药 lens: judge body strength, disease, medicine,通关,扶抑,调候.
5. **Decide useful force**: what the chart needs to function, not what sounds auspicious.
6. **Read 大运 before 流年**: luck cycle sets the stage; year triggers the event.
7. **Calibrate known events**: ask which star, palace, luck, year, and real-world trigger matched. Recalibrate if history contradicts the first read.

## Decisive Verdict Rules

When signs converge, speak plainly:

- If structure is clear and the useful force appears in chart/luck, say what rises and why.
- If useful force is absent, trapped, or repeatedly attacked, say the weakness directly and name the workaround.
- If 格局 and 旺衰 disagree, do not average them. Decide which one controls the asked event:
  - Career/title questions often privilege 官杀/印/月令 structure.
  - Money execution often needs 食伤生财, 财星 access, and luck support.
  - Health tendency first checks climate imbalance and overstrain; do not diagnose disease.
  - Marriage needs spouse star plus 日支 interaction, not only gender formula.
- 调候 can become the practical first medicine when climate is extreme, but it does not erase格局.

Use confidence labels:

- **高置信**: original chart + 大运 + 流年 + real-world condition point the same way.
- **中置信**: chart and luck agree, but real-world data is thin.
- **低置信**: one pillar/sign suggests it, or input time is uncertain.

## Event Lenses

- **Career/position**: 官杀, 印, 月令, 格局成败, 大运/流年 touching official, document, platform, boss, or resource signs.
- **Wealth**: 财星, 食伤生财, 财库, market opportunity, liquidity, asset conversion, whether body/structure can carry wealth.
- **Marriage for male chart**: 财星 and 日支. For female chart: 官杀 and 日支. Always read interaction, quality, timing, and lived context.
- **Parents/family**: palace plus 印/财 and known family facts; do not force one formula across every chart.
- **Health tendency**: read imbalance tendencies only: excessive heat/cold/dryness/dampness, stress timing, symbolic organ load. Refer to professional care for symptoms.

## Timing / 应期

Use event confirmation, not single-sign guessing:

1. 大运 opens or closes the ten-year theme.
2. 流年 activates star, palace, clash/combination, tomb/storehouse, or useful force.
3. 流月/流日 can time near events only when the larger luck already permits it.
4. Strong timing usually has at least three hits: star + palace + luck/year + real-world schedule.
5. For bad outcomes, give prevention window and mitigation, not fatalistic certainty.

## Cautions

- Death timing is not responsibly deterministic. Give risk windows and prevention only.
- Do not infer one exact year from one clash alone.
- 神煞 may enrich texture but must not override structure, season, useful force, and known facts.
- If a prior prediction is contradicted by fact, state the error and recalibrate.
