# Method Contracts

This file defines the normalized input and output contracts borrowed from high-quality vertical divination skills: calculate facts first where possible, then interpret; mark unsupported facts as blocked instead of fabricating.

## Unified Input Card

Use this card internally before any serious reading:

```json
{
  "question": "",
  "system_requested": "bazi|meihua|liuyao|fengshui|tarot|synthesis|unknown",
  "language": "zh|en|ko|ja|fr|es|auto",
  "time_context": {
    "event_time": "",
    "timezone": "",
    "calendar_type": "solar|lunar|unknown",
    "precision": "exact|approximate|unknown"
  },
  "person_context": {
    "birth_date": "",
    "birth_time": "",
    "birth_place": "",
    "gender": "",
    "is_fictional_example": true
  },
  "divination_input": {
    "numbers": [],
    "six_lines_bottom_to_top": [],
    "outer_omen": "",
    "cards": [],
    "spread": "",
    "direction_or_layout": ""
  },
  "focus": [],
  "constraints": {
    "single_system_only": false,
    "ignore_prior_readings": false,
    "strict_output": false
  }
}
```

## Method Status Card

For synthesis, normalize each system to:

```json
{
  "method": "",
  "status": "runnable|partial|blocked",
  "facts": [],
  "interpretation": "",
  "confidence": "high|medium|low",
  "blockers": [],
  "verification": []
}
```

Only synthesize from `runnable` and clearly bounded `partial` methods. Do not use `blocked` methods as evidence.

## Localized Trigger Surface

Use local terminology in docs and examples. Do not rely on direct machine translation only.

| System | Chinese | English | Korean | Japanese | French | Spanish |
| --- | --- | --- | --- | --- | --- | --- |
| BaZi | 八字, 子平, 四柱, 生辰八字 | BaZi, Four Pillars, Chinese astrology | 사주, 사주팔자, 사주명리 | 四柱推命, 八字, 命式 | BaZi, quatre piliers, astrologie chinoise | BaZi, cuatro pilares, astrología china |
| Meihua | 梅花易数, 邵雍, 外应, 起卦 | Meihua Yishu, Plum Blossom I Ching, omen reading | 매화역수, 매화역학, 외응 | 梅花易数, 梅花心易, 易占 | Meihua Yishu, Yi King, présage | Meihua Yishu, I Ching, presagio |
| Liuyao | 六爻, 纳甲, 世应, 用神 | Liuyao, six lines, Najia | 육효, 납갑, 세응 | 六爻, 納甲, 世応 | Liuyao, six lignes, Najia | Liuyao, seis líneas, Najia |
| Feng Shui | 风水, 堪舆, 八宅, 飞星, 方位 | Feng Shui, geomancy, flying stars, direction | 풍수, 양택, 방위 | 風水, 家相, 方位, 飛星 | Feng Shui, géomancie, directions | Feng Shui, geomancia, direcciones |
| Tarot | 塔罗, 牌阵, 抽牌, 正逆位 | tarot, tarot spread, card draw, reversed card | 타로, 타로 배열, 카드 뽑기 | タロット, スプレッド, 逆位置 | tarot, tirage, carte inversée | tarot, tirada, carta invertida |

## Public Example Rule

All public examples must use fictional or generic data. Never publish real user names, birth details, workplace facts, family facts, salaries, or private life events.
