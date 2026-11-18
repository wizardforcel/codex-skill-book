# 玄学合参技能

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab)](scripts/)


玄学合参技能是一套给智能体使用的结构化术数推演包，覆盖八字/子平命理、梅花易数、六爻/纳甲、风水方位和塔罗牌阵。它不是一段“算命提示词”，而是一套可以复用、可以安装、可以验证、可以迁移到不同智能体环境的工作流。它的目标很明确：让人工智能在回答玄学问题时，不再靠模糊安慰和临场发挥，而是先选体系、再验输入、再断结论、再列依据、再定应期、再给行动、最后给验证点。

很多人工智能的玄学回答会犯两个错误。第一，把所有系统混在一起，把八字、塔罗、易经、风水都说成同一种“感觉”；第二，抓住一个符号就无限展开，比如看到一个冲、一个动爻、一张塔牌，就直接下很大的判断。这套技能的设计刚好反过来：每个体系先内部自洽，再做合参。八字看人生结构和大运流年；梅花看起心动念、外应、时间和近事变化；六爻看具体成败、流程、角色和阻力；风水看空间方位、动线、背靠、可见度和环境压力；塔罗看关系动力、心理结构、选择分歧和象征转折。

它也不是让人工智能变得玄乎，而是让人工智能更有边界。输入不足时，它会标记为“可部分判断”或“阻塞”，而不是硬编。出生时间不准，就不硬断时柱细节；六爻顺序不明，就不硬做纳甲细断；风水没有罗盘和户型，就不硬讲飞星；塔罗没有牌阵，就先确认或使用可复现抽牌脚本。它能给果断断语，但不会把文化推演说成科学事实，也不会替代医疗、法律、投资、心理健康和安全建议。

## 多语言版本

- [英文](README.md)
- [简体中文](README.zh-CN.md)
- [韩文](README.ko-KR.md)
- [日文](README.ja-JP.md)
- [法文](README.fr-FR.md)
- [西班牙文](README.es-ES.md)

## 适合谁使用

这个仓库适合三类人。

第一类，是想让 Codex、Claude Code 或其他智能体稳定处理玄学问题的人。你不需要每次把方法论重新写一遍，只要把这套技能放进智能体能读取的位置，智能体就能按 `SKILL.md` 和 `references/` 里的流程执行。

第二类，是想把八字、梅花、六爻、风水、塔罗做成结构化产品的人。你可以把这里的路由、输入契约、输出模板、脚本和隐私扫描当作基础模板，再接自己的排盘工具、前端页面或自动化流程。

第三类，是对术数感兴趣但又不希望人工智能胡说的人。这个仓库的思路不是“越神秘越好”，而是“越可复核越好”：断语可以果断，依据必须可看；应期可以明确，验证点必须可追踪；合参可以综合，但每个体系的原始范围不能被改写。

## 支持体系

| 体系 | 约 100 字介绍 | 主要文件 |
| --- | --- | --- |
| [八字命学 / 子平法](https://zh.wikipedia.org/zh-cn/%E5%85%AB%E5%AD%97%E5%91%BD%E5%AD%A6) | 八字以出生年月日时形成四柱，每柱由天干地支组成，用来观察命局结构、大运流年、事业财运、婚恋健康等长期趋势。本技能会先区分排盘事实和解释，不会在出生时间、历法或地点不清楚时硬断细节。 | `references/bazi.md` |
| [梅花易数 / 邵雍象数](https://zh.wikipedia.org/zh-cn/%E9%82%B5%E9%9B%8D) | 梅花易数重视起心动念、时间、数字、声音、方位、外应和卦象变化，适合看近事、突发事件、项目推进和当下什么在动。本技能会拆分主卦、动爻、互卦、变卦、体用生克和外应，不用一个象乱断全部。 | `references/meihua.md` |
| [六爻神卦 / 纳甲六爻](https://zh.wikipedia.org/zh-cn/%E5%85%AD%E7%88%BB%E7%A5%9E%E5%8D%A6) | 六爻以六条爻和动变关系判断具体事情的成败、阻力、角色和时间，适合职位、合同、老板、薪资、产品数据、关系成败等问题。本技能强制确认初爻到上爻的顺序，纳甲信息不足时只做有限判断。 | `references/liuyao.md` |
| [风水 / 方位](https://zh.wikipedia.org/zh-cn/%E9%A3%8E%E6%B0%B4) | 风水关注环境、方位、气口、动线、背靠、明堂、门窗、噪声和可见度。这套技能先看真实空间形势，再看八卦方位和理气，不鼓励昂贵迷信改造，重点是让环境更支持注意力、稳定性和可见度。 | `references/fengshui.md` |
| [塔罗牌](https://zh.wikipedia.org/zh-cn/%E5%A1%94%E7%BD%97%E7%89%8C) | 塔罗通过牌阵、牌位、图像、正逆位、元素和牌间关系观察心理动力、关系互动、选择分歧和象征性结果。本技能支持可复现抽牌，显示 seed、牌位和正逆位，避免为了得到喜欢的答案反复重抽。 | `references/tarot.md` |

## 工作方式

本技能的核心流程是：

1. 先重述问题，确认它到底问的是人生结构、近期变化、具体成败、空间关系，还是心理/关系动力。
2. 选择对应体系。不是所有问题都适合八字，也不是所有问题都适合塔罗。
3. 检查输入。八字看历法、时间、地点；梅花看时间、数字、外应；六爻看六爻顺序；风水看方位和布局；塔罗看牌阵和正逆位。
4. 标记状态：可运行、可部分判断、阻塞。
5. 单体系内部先下判断，再做多体系合参。
6. 输出断语、依据、应期/强弱、行动、验证点和低置信推测。

标准输出形态：

```text
断语：
依据：
应期/强弱：
行动：
验证点：
低置信推测：
```

严格单体系输出：

```text
本次只用：
断语：
主证：
冲突点：
应期/数值：
行动：
验证点：
置信层级：
```

## 安装到不同智能体

这个仓库不只给 Codex 用。任何可以读取本地文件的智能体，都可以把它作为一套本地技能说明、参考资料和脚本工具来使用。

### 通用安装

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis
cd ~/agent-skills/metaphysics-synthesis
python3 scripts/validate_skill.py
```

然后在你的智能体里说明：

```text
请使用本地技能：~/agent-skills/metaphysics-synthesis/SKILL.md。根据问题只读取相关 references 文件。
```

### Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
python3 ~/.codex/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.claude/skills/metaphysics-synthesis
python3 ~/.claude/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### 任意自定义技能目录

```bash
AGENT_SKILLS_DIR="$HOME/.your-agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git "$AGENT_SKILLS_DIR/metaphysics-synthesis"
python3 "$AGENT_SKILLS_DIR/metaphysics-synthesis/scripts/validate_skill.py"
```

### 多个智能体共用一份

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis

mkdir -p ~/.codex/skills ~/.claude/skills
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.codex/skills/metaphysics-synthesis
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.claude/skills/metaphysics-synthesis
```

## 使用示例

### 八字

```text
用八字看 2026-2036 年事业、财运、婚恋和健康趋势，严格区分命局结构、大运、流年触发点、高置信判断和低置信推测。
```

### 梅花易数

```text
用梅花易数看这个项目上线后是否形成可汇报的结果。起心动念时间是 2026-06-12 10:36，外应是西北方主管在讨论排期。
```

### 六爻

```text
用六爻判断这个项目能不能成为升职主功。六个数字从初爻到上爻是 5 / 4 / 25 / 12 / 22 / 17，不串联旧卦。
```

### 风水

```text
按风水方位看我的工位：我面向东南，主管在西北，大领导在南方，跨团队负责人在东方。这个格局对可见度和汇报机会有什么影响？
```

### 塔罗

```text
用五张塔罗牌阵看这次职业选择。请抽牌并显示 seed、牌位、正逆位、断语、行动和验证点。
```

## 脚本

### 梅花起卦结构计算

```bash
python3 scripts/meihua_calc.py time 2026 6 12 10
python3 scripts/meihua_calc.py classic 7 4 27 10
python3 scripts/meihua_calc.py num 22 5 18
```

### 塔罗抽牌

```bash
python3 scripts/tarot_draw.py --spread relationship --question "这段合作会不会成熟？" --seed 42
python3 scripts/tarot_draw.py --spread five --question "职业选择" --json
```

### 校验与隐私检查

```bash
python3 scripts/validate_skill.py
python3 scripts/privacy_check.py
```

## 目录结构

```text
metaphysics-synthesis-skill/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── bazi.md
│   ├── fengshui.md
│   ├── liuyao.md
│   ├── meihua.md
│   ├── method-contracts.md
│   ├── router.md
│   ├── output-templates.md
│   ├── examples.md
│   ├── sources.md
│   └── tarot.md
├── scripts/
│   ├── meihua_calc.py
│   ├── tarot_draw.py
│   ├── privacy_check.py
│   └── validate_skill.py
└── README.*.md
```

## 安全边界

本仓库把玄学视为文化、象征、反思和策略工具。它不能用于确定死亡、灾难、疾病结果、法律结果、投资收益或人身安全。涉及医疗、法律、投资、心理危机和紧急安全问题时，应以专业意见和直接证据优先。

## 许可证

MIT License。见 [LICENSE](LICENSE)。
