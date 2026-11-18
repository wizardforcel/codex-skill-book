# Public Source Notes

These sources orient the skill. They are not exhaustive authorities and do not prove any objective "world number one master." Use web search for fresh or contested claims.

## Research Principle

- Prefer classical/primary text lines for method skeletons.
- Use modern tutorials to see how practitioners operationalize the method.
- Use reader/community signals such as Douban or Goodreads only as popularity/validation signals, not proof of truth.
- Mark old sources as stable tradition rather than current science.
- For AI skill/package design, inspect public repositories for input contracts, scripts, routers, localization, and validation patterns. Borrow architecture, not private data or copyrighted prose.

## Public GitHub Skill / Tool Benchmarks

- `cantian-ai/bazi-persona-skill`: multilingual BaZi persona skill surface and cross-agent packaging: https://github.com/cantian-ai/bazi-persona-skill
- `cantian-ai/bazi-mcp`: BaZi MCP/tooling emphasis on deterministic data and calculation service: https://github.com/cantian-ai/bazi-mcp
- `jinchenma94/bazi-skill`: BaZi skill-style data collection and classical-analysis framing: https://github.com/jinchenma94/bazi-skill
- `muyen/meihua-yishu`: Meihua AI skill with compact entrypoint, references, scripts, 体用, external omens, and timing guides: https://github.com/muyen/meihua-yishu
- `daman-ovo-0404/tarot-skill`: Tarot skill packaging with card/spread resources and draw workflow: https://github.com/daman-ovo-0404/tarot-skill
- `bopo/najia`: Python Najia/Liuyao fields such as hexagram marks, moving lines, 六亲, 六神, 世应, 纳甲: https://github.com/bopo/najia
- `likeSo/liu-yao`: Liuyao app with multiple casting methods and calendar parsing: https://github.com/likeSo/liu-yao
- `voidforall/fengshui.skill`: Feng Shui skill packaging pattern and persona surface: https://github.com/voidforall/fengshui.skill
- `shizhilya/yuan`: multi-system metaphysics API/MCP/skill project; useful for router and module separation ideas: https://github.com/shizhilya/yuan
- `ai-freer/fortune-skill`: fortune skill structure with privacy checking and report templates: https://github.com/ai-freer/fortune-skill
- `Brhiza/mingyu`: multi-system fortune-telling service structure: https://github.com/Brhiza/mingyu
- `eamanc-lab/fortune-telling-skills`: multi-skill hub structure for Chinese metaphysics agent skills: https://github.com/eamanc-lab/fortune-telling-skills

## BaZi / 子平

- 《子平真诠评注》 pages on 用神, 格局成败, and救应: https://www.suanzhun.net/dianji/zipingzhenpingzhu/320.html and https://www.suanzhun.net/dianji/zipingzhenpingzhu/318.html
- 千里命稿-style step summaries are commonly listed as first看八字强弱, then格局, 用神, 喜忌, 岁运: https://www.xishuxin.com/article/1137.html
- Reader validation examples: 豆瓣 entries for 《子平真诠评注》, 《千里命稿》, 《滴天髓阐微》, 《命理探原》. Use their ratings/comments only as community signals.

Method distilled into the skill:

- 月令/格局 lens and 旺衰/病药 lens must be separated before synthesis.
- 大运 is the stage; 流年 is the trigger.
- Event timing needs repeated confirmation, not one clash or one god/sha.

## 六爻 / 纳甲

- Tianjiyao 六爻 overview describes 纳甲, 世应, 六亲, 六神, 月日, 动变, 空亡 as core working parts: https://wiki.tianjiyao.com/yijing/liuyao.html
- Public classical repositories for 《增删卜易》 and related materials: https://www.zhonghuadiancang.com/xuanxuewushu/zengshanbuyi/
- 《卜筮正宗》 public text repositories are used as a classical method reference where available.

Method distilled into the skill:

- 用神 selection is the first decision.
- 月建/日辰 and 动变 are stronger than decorative storytelling.
- 空墓绝破, 伏神/飞神, 回头生克, and进退神 decide delay, rescue, or reversal.

## 梅花易数 / 邵雍象数

- Public 《梅花易数》 repositories: https://www.zhonghuadiancang.com/xuanxuewushu/meihuayishu/
- Wikisource has 《梅花易数》卷三 material: https://zh.wikisource.org/zh-hans/%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8/%E5%8D%B7%E4%B8%89
- Modern summaries consistently emphasize 主卦, 互卦, 变卦, 体用, 五行生克, 动爻, 外应, 应期.
- The public `muyen/meihua-yishu` skill README describes a梅花专精 skill with time/number/sound/color/direction casting, 体用生克, 通关化解, 卦气旺衰, 十应, 八卦万物类象, 十八类分占, and应期 guides: https://github.com/muyen/meihua-yishu/blob/main/README.zh-TW.md

Method distilled into the skill:

- 体用生克 controls the main verdict.
- 主/互/变 show present/hidden/outcome stages.
- 外应 narrows detail but cannot overturn clear体用.
- When using外应, classify the omen first and use it only after主互变 and体用 decide the main trend.
- For应期, combine moving line/trigram/成卦之数, seasonal strength, user's motion state, and real-world schedule.

## 风水 / 方位

- Flying star and 玄空 introductions commonly require period, sitting/facing, mountain/water stars, and form context: https://www.ifengshui101.com/book_flyingstar.html
- Modern summaries of flying star method and yearly star claims are time-sensitive; verify current-year claims before relying on them.

Method distilled into the skill:

- 形势 first: backing, front field, door/window/traffic/noise/clutter.
- 八方类象 can guide symbolic adjustment.
- 玄空飞星 requires precise inputs; no compass/floor plan means no confident飞星 reading.

## Tarot

- A. E. Waite's public-domain Pictorial Key tradition: https://www.sacred-texts.com/tarot/pkt/
- Reader validation examples: Goodreads pages for Rachel Pollack's *Seventy-Eight Degrees of Wisdom* and Mary K. Greer's *Tarot for Your Self*.
- Ethics references such as tarot association codes commonly caution readers not to replace medical, legal, or financial professionals: https://tarotassociation.net/code-of-ethics/

Method distilled into the skill:

- RWS image evidence comes before generic keywords.
- Spread position, image interaction, suit/element balance, and anchor card decide the verdict.
- Reversals are contextual: blocked, internalized, excessive, delayed, or shadow.
