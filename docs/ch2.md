# 第2章 编写小说

写小说和写短回复完全不同：一本几十万字的书，写到后面要记得前面的角色、时间线、伏笔和设定，纯靠对话慢慢来，上下文很快就会被冲掉。这一章介绍三套专门面向长篇中文小说的 Skill，它们的共同思路是在正文之外维护一套“可恢复的项目状态”：一本书不是一个对话，而是一个有目录、有状态文件、有检查工具的工程。读完这一章，你会理解长篇写作为什么需要 Skill，并学会选一套适合自己工作方式的流程。

## 2.1 长篇写作的分层上下文与事实锁

### 简介

`chinese-longnovel-skill` 面向中文长篇网文，特点是“分层上下文 + 事实锁”。它把全书拆成宏观阶段、50 章规划窗口、分章细纲三层；写作前先组装一个小而关键的“上下文包”，再把里面绝对不能改错的数值和事实固化成“事实锁”。它最强调的不是“生成下一章”，而是写到几百章之后仍然一致：每个事实锁都记录来源文件、原文锚点、哈希值和期望值，正文或审查时发现候选改了锁，就立刻拦截。

安装方式：

```powershell
npx skills add xiaofeng-928/chinese-longnovel-skill -a codex -g -y
```

装好后它在 `~/.codex/skills` 或 `~/.agents/skills` 下出现一个名字叫 `my-novel` 的技能（`SKILL.md` 的 `name` 是 `my-novel`）。

### 调用记录

**我**：我想写一本经营流长篇，先出前 10 章细纲，不要正文。

**Codex**：技能先看自己的路由表。你这条请求对应“开书”“总大纲”“分阶段大纲细化”三个环节，它不会跳过前置直接编细纲。

**我**：它第一步做什么？

**Codex**：先检查有没有 30 天内的扫榜归档（市场证据）。真实执行中，本机没有任何扫榜归档，技能按“人工补充数据 / 低可信度探索”规则继续，但要求一律记录覆盖原因。现场生成的 `创作依据/开书方案.md` 开头是这样：

```markdown
# 开书方案

## 一、扫榜元数据与证据等级
- 来源平台：无（本演示项目未进行真实榜单抓取）
- 市场验证状态：unvalidated（未完成市场验证）
- 证据等级：低可信度探索（low-confidence exploration）

### 覆盖原因
本项目的开书目标不是真实市场推书，而是演示技能路由的完整执行。
当前不存在 30 天内且题材匹配、至少 5 本含
management_loop/system_loop 证据的扫榜归档。
因此按技能允许的路径：“缺少新鲜扫榜归档，按低可信度探索继续”。
不得据此声称已完成当前市场验证。
```

它不允许用模型记忆凭空填充“当前热度”。这是它和普通聊天最大的差别：开书判定要落到文件里，而不是对话里。

**我**：然后呢？给我看总纲领头长什么样。

**Codex**：先建最小项目壳（`novel-config.md`、`创作依据/开书方案.md`、`设定/`、`plan/`），再走“总大纲 → 分阶段大纲细化”。现场生成的这部书叫《老街食光记》（经营+美食+系统），`novel-config.md` 里已经写死目标 1000 章、当前规划窗口第 1-50 章、窗口合同与剧情预算锁都是 `locked`。

总大纲头部是技能规定的格式：

```markdown
## 类型标签
- 主类型：经营流（美食小馆）+ 系统爽文，辅以老街人情悬疑线。
- 爽点模式：打脸（质疑→真实出品→口碑反杀）+ 经营成长盘账爽点 + 伏笔回收。
- 类型承诺检查重点：每次涨价/促销后要展示顾客支付能力变化；每次开发新菜要完成一次可围观的真做真吃。

## 系统设计档案（摘要）
- 系统名称/核心循环：灶神簿——试菜/口碑账页→获灶神点→兑换菜谱残页与食材票→再投入经营。
- 永久限制：系统商店与面馆经营账严格分账；食材票货物只能自用；灶神点不得兑换现金。
```

`plan/总大纲.md` 里还生成了 6 个 `MYNOVEL:STAGE` 宏观阶段块（初立门户 / 站稳脚跟 / 连锁扩张 / 城市争锋 / 区域称雄 / 祖业传承），每个块都有非空的 `exit_condition`。技能明确要求：大纲只维护“计划状态”，正文后才能回写“当前状态”，两件事在文件上分开。

**我**：到最后出前 10 章细纲时长什么样？

**Codex**：细化前先过三道闸门：同范围系统发展计划存在、窗口合同章号与宏观阶段匹配、剧情预算锁为 `locked`；第 1-50 章还要先有黄金三章微操细纲，缺了就停在上游。细纲每一章都带 `MYNOVEL:PLAN-NODE` 规划块，并且每章附“事实锁”清单。事实锁的结构由技能规定（以下为按提示词生成的简化示例）：

```markdown
## 第3章 事实锁
- 硬事实：主线锚点 = 第2章末 "福记面馆招牌挂上"；expected_value = "福记面馆"
- 时间锚：当前年份 = 同第1章；expected_value = "开业第3天"
- 角色认知：赵全不知道旧账本在库房里；expected_value = "不知情"
- 能力与资源：账面现金 = 3940 元；expected_value = "3940"
- 关系承诺：欠供货商一笔旧账；expected_value = "第5章结清"
- 因果债：第3章埋下旧钥匙；expected_value = "第8章回收"
- 伏笔：禁止在回收前被使用或改义
```

字段含义是：`来源相对路径` 说明这条锁来自哪个文件，`选点文本/锚点` 指出它在原文的哪个位置，`expected_value` 是正文候选必须原样保留的稳定事实。写作时这些锁负责“防跑偏”，审查时负责“防改义”。

**我**：这不就是写个清单吗，跟直接在对话里注意一下有什么区别？

**Codex**：清单人人会列，区别在“绑定”和“验证”。技能把每一条锁都绑定到具体文件的锚点和哈希；正文生成只允许同义改写，不能动 `expected_value`。你跨会话继续写、或者让另一个模型来续写，它读的不是你的记忆，而是这串可复核的事实锁。写几百章后的一致性，靠的就是这些稳定的 token 对照，而不是“我记得”。

### 总结

- 长篇小说 Skill 的核心不是“写得多”，而是“写得一致、能找回”。
- 开书必须先有市场证据；没有证据就用低可信度探索并写清覆盖原因，不能拿模型记忆冒充热度。
- 结构分三层：宏观阶段 → 50 章窗口 → 分章细纲，细纲要先过闸门（系统计划、预算锁、黄金三章）。
- 事实锁记录来源、锚点、哈希和 `expected_value`，是跨会话保证一致性的关键机制。

## 2.2 轻量替代：可恢复的 Markdown 工作流

### 简介

`ani-book-skill` 是另一套面向 Codex 的长篇中文小说生产 Skill（Codex 原生适配后的技能名为 `produce-long-form-novel`）。它同样强调“可恢复”，但落地方式更直白：所有产物都是你能直接阅读和编辑的本地 Markdown / YAML 文件，外加一个叫 `novel-state.yaml` 的状态索引和一个控制器脚本 `novelctl.py`。中断后重新打开项目，技能先读状态文件判断你做到哪一步，再决定唯一的下一个动作，而不是从头重写。

安装方式：

```powershell
npx skills add https://github.com/ExplosiveCoderflome/ani-book-skill -a codex -g -y
```

### 调用记录

**我**：初始化一个最简小说项目。

**Codex**：用技能自带的控制器初始化（本机 `python` 缺 `yaml`，这里用 `uvx --with pyyaml` 临时补依赖）：

```powershell
uvx --with pyyaml python -X utf8 C:\Users\Administrator\.agents\skills\produce-long-form-novel\scripts\novelctl.py init --title "雾城回声" D:\novel-test
```

真实输出：

```json
{ "created": "D:\\novel-test",
  "schema_version": 3,
  "mode": "milestone_approval" }
```

工作区里立刻生成状态索引和骨架：

```text
novel-state.yaml           # 唯一状态源
production/recovery.md     # 恢复提示，由状态文件生成
production/token-usage.jsonl
chapters/  volumes/  characters/  context-packages/  continuity/  exports/
```

**我**：怎么知道现在该做什么？

**Codex**：刚初始化时运行 `status`，它老实告诉你 7 个必需文件还缺着：

```json
{
  "title": "雾城回声",
  "artifact_counts": { "missing": 7, "ready": 0, "in_progress": 0 },
  "next_action": {
    "type": "collect_opening_choices",
    "target": "opening_choices",
    "reason": "开书前需确认频道、发布形态和主要阅读回报",
    "requires_approval": true
  }
}
```

每完成一步，它就推进一格。等书级简报、故事圣经、世界设定、角色索引、卷战略、卷骨架、节奏板、章节计划、上下文包和第一章正文都生成后，真实状态变成：

```json
{
  "artifact_counts": { "missing": 0, "ready": 10, "in_progress": 0 },
  "next_action": {
    "type": "produce_artifact",
    "target": "chapter_001_humanized",
    "reason": "第 1 章下一生产步骤：humanization_revision"
  }
}
```

`production/recovery.md` 每次都按 `novel-state.yaml` 重新生成，所以它永远和最新状态一致。

**我**：那第一章的计划和上下文长什么样？

**Codex**：`chapters/chapter-001/plan.md` 是本章合同，节选：

```markdown
## 基本任务
- 本章即时目标：陈默修好一只停摆的旧怀表，并在表盖内侧发现与妹妹有关的编号。
- 主要阻力：怀表来源不明；回声带来剧烈头痛；开发公司的人当天下午就来取表。
- 必须推进的剧情和信息：
  1. 展示回声能力及其代价（W-001）。
  2. 确认怀表与妹妹陈雾有关，但不解释她是否还活着。
  3. 让陈默从“不想再碰旧事”转为“决定去旧港查证”。
- 禁止越过的边界：不得让回声直接说出完整真相；不得让陈默凭空知道旧港路线。
```

`context-package.md` 则只挑本章真正需要的权威文件，并明确写“裁掉了什么”：

```markdown
## 已选权威文件
| 文件 | 用途 |
| novel-brief.md | 频道、阅读承诺、叙事偏好、字数例外 |
| story-bible.md | 长期对立、主角成长路径、揭示梯度 |
| characters/character-roster.md | 陈默、林小雨、老周的当下呈现 |

## 因无关或超窗而裁掉
- 第二卷的证人线、第三卷的妹妹现身。
- 旧港内部结构、闸门记录细节。
```

这就是“分层上下文”的实际样子：不是把整本书塞给模型，而是按本章需要选文件、写清约束、裁掉无关内容。

**我**：那写 500 字的一章试试。

**Codex**：按章节计划实际写出了 `chapters/chapter-001/draft.md`。字数统计：不含空白 529 字符，其中汉字 446 字，落在计划的 450–650 字可接受区间附近。开头是：

> 表盖合上的时候，指针停在两点十七分。
>
> 陈默把放大镜卡回眼眶，拿镊子挑开第一颗螺丝。这表不旧，壳子擦得发亮，可机芯里全是干掉的盐霜。有人带着它下过水，又把它泡在盐里十年。
>
> “从旧港出来的。”老周在电话里只说了这一句，就挂了。

写完后 `next` 自动指向下一步——给正文做人类化润色，而不是回头重做大纲。

**我**：写完一章怎么登记？

**Codex**：先 `start-step`，返回唯一 `run_id` 并把该工件标成 `in_progress`；写完正文后 `finish-step`。这里有一个真实护栏：

```text
novelctl failed: measured records require input_tokens, output_tokens, or total_tokens
```

技能不接受“生成了但不知道花了多少”的记录。要么补上 token 数写入用量账本，要么像这次一样如实登记 `unavailable`（宿主没有暴露模型用量），绝不编一个数字。

**我**：如果我手滑把刚才的章节文件删了，再从“继续”叫它，它会从头重写吗？

**Codex**：不会。真实执行分三步暴露了它的恢复逻辑：

```text
rm chapters/chapter-001/draft.md
```

第一步，删完后看 `status` 和 `next`——它们居然没变，仍然是 `ready: 10`、下一步是润色。原因是 `status` / `next` 只读 `novel-state.yaml` 的状态投影，本身不扫描文件。

第二步，跑 `validate`，它立刻发现文件真的没了：

```json
{
  "valid": false,
  "errors": [
    "ready artifact is missing: chapter_001_draft -> ...\\chapters\\chapter-001\\draft.md"
  ]
}
```

第三步，跑 `reconcile`，它把缺失当成一次“受保护变更”，写回状态并重算唯一动作：

```json
{
  "changed": ["chapter_001_draft"],
  "stale": [],
  "next_action": {
    "type": "produce_artifact",
    "target": "chapter_001_draft",
    "reason": "首个 missing 产物：chapter_001_draft"
  }
}
```

恢复点被精确定位到“重写第 1 章正文”，计划和上下文包仍然 `ready`，整本书不用重做。之后直接 `start-step` 还会被拒绝——`artifact is protected; approve overwrite first`，必须先 `approve --overwrite` 授权，再只重写这一章；重写完成 `validate` 回到 `"valid": true`。

**我**：所以“可恢复”到底是什么在保证？

**Codex**：三样东西分工：`novel-state.yaml` 记录项目做到哪，`status` / `next` 给出当前唯一的下一步，`validate` / `reconcile` 负责发现“状态说好了、文件却不在”的偏差并把它修正成一个可执行的恢复动作。它不是靠模型记忆，也不是靠目录里数文件。

### 总结

- `ani-book-skill` 的产物是纯 Markdown / YAML，能直接读、能编辑、能备份。
- `novelctl.py` 提供 `init / status / next / start-step / finish-step / validate / reconcile / export` 等确定性命令。
- 状态索引（`novel-state.yaml`）记录项目做到哪，`recovery.md` 由它自动生成。
- `status` / `next` 只读状态投影，不检查文件是否真的在；文件丢失由 `validate` 发现，再由 `reconcile` 重算恢复点。
- `finish-step` 强制登记 token 用量，是防止“生成了什么都不知道”的护栏。
- 中断后续写，先 `status` / `next` 看下一步，再 `validate` 核对文件，缺失时用 `reconcile` 恢复，而不是从头重建。

## 2.3 替代方案对照：vibe-noveling

### 简介

`vibe-noveling` 是一套更完整的网文创作工作流，仓库同时提供 Claude 插件版和 Codex 适配版。Claude 插件层包含 13 个技能目录和 4 个子 Agent；Codex 适配层则收敛成一个伞形技能，用路由决定当前该做讨论、规划还是写作。它用“先初始化项目、再逐步讨论 → 规划 → 写作”的节奏，避免一上来就憋正文。对比前两节：`chinese-longnovel-skill` 重结构、`ani-book-skill` 重可恢复文件，`vibe-noveling` 重创作者对话节奏与“世界记忆”。

安装要注意一个差异点：`npx skills add` 只会把 Claude 插件层的 11 个工作流子技能装进 `~/.agents/skills`，`$vibe-noveling` 伞形技能要按仓库 `codex/README.md` 手动复制适配层到 `~/.codex/skills/vibe-noveling`，并用技能自带的 `quick_validate.py` 校验。

### 调用记录

**我**：装好后直接说 `$vibe-noveling` 就能用吗？

**Codex**：不能直接用。实测 `npx skills add wwt87/vibe-noveling -a codex -g -y` 只安装了 11 个子技能（`novel-init`、`novel-discuss`、`novel-bookplan`、`novel-plan`、`novel-write`、`novel-revise`、`novel-sync`、`novel-progress`、`novel-snapshot`，以及 `booming`、`fuck-it`），并没有 `$vibe-noveling` 伞形技能。按仓库 `codex/README.md` 把 `codex/skills/vibe-noveling` 复制到 `~/.codex/skills/vibe-noveling` 后，用校验脚本确认：

```text
Skill is valid!
```

**我**：那怎么初始化一本书？

**Codex**：技能路由到 `/novel-init`，读取 `references/init.md`，然后执行它的初始化脚本：

```powershell
python C:\Users\Administrator\.codex\skills\vibe-noveling\scripts\init_project.py . --title "一个失业的39岁程序员" --genre "都市现实"
```

真实输出：

```text
Vibe Noveling project initialized: ...\my-novel
Created files:
- CLAUDE.md
- memory\_graph.json
- memory\_index.json
- memory\past.md
- ...（共 14 个文件、16 个子目录）
```

**我**：初始化之后它会直接开始写章节吗？

**Codex**：不会。验收骨架的几个实测点：

```text
chapters\vol-01\ch-0001   → 真实文件数为 0
memory\past.md            → “尚无已完成章节。”
future\10-book.md         → “待规划。”
CLAUDE.md 中的“灵魂、爽感公式、主角光谱” → 待定
```

也就是说，初始化只搭“骨架”，正文一个字都没写。

**我**：它有专业技能和子 Agent 吗？各是什么？

**Codex**：以仓库实际文件为准，Claude 插件层是 13 个技能目录，其中 `novel-knowledge`、`novel-name` 是内部辅助，其余 11 个是工作流技能；另有 4 个子 Agent：`context-collector`（收集上下文）、`consistency-guard`（一致性检查）、`writer-dazhongma` 与 `writer-zhouzi`（两种风格稿作者）。Codex 适配层则是 1 个伞形技能，内部用 14 个 reference 文件做路由。

**我**：它是按什么顺序推进创作？

**Codex**：`CLAUDE.md` 里写明的工作流是 `discuss → bookplan → plan → write`：先讨论世界和角色，再做全书规划，然后单章规划，最后才写正文。每完成一章，还有 `novel-sync` 负责把剧情摘要回写到 `memory/` 的知识图谱，`novel-snapshot` 负责存档打点。

### 总结

- `vibe-noveling` 提供的是“讨论节奏 + 世界记忆”，比前两套更强调先聊清楚再动笔。
- 安装时记住差异：`npx skills add` 不装伞形技能，需要按 `codex/README.md` 手动复制适配层。
- 初始化只建骨架（`memory/`、`future/`、`chapters/vol-01/ch-0001` 等），不会直接出章。
- 子 Agent 分工明确：收集上下文、一致性守卫、两位不同文风的写手。

## 2.4 伏笔追踪与一致性审查

### 简介

伏笔在这套技能里被当作“待偿债务”来管理：埋下时登记为债务，写入细纲计划、章节总结和阶段摘要；写作时检查它是否被提前消费，审查时检查它是否超期、变义或悄悄消失。这一节用 2.1 的技能做一次伏笔登记与一致性审查，展示输出格式和“当前状态”那一列的意义。

### 调用记录

**我**：在细纲里登记一条伏笔：第 3 章埋下旧钥匙，计划第 8 章回收。

**Codex**：按技能要求，伏笔不进对话，进 `plan/伏笔追踪.md`，每条记录至少含：埋设章、计划回收章、当前状态、来源文件与锚点：

```markdown
## 伏笔：旧钥匙
- 埋设章：第3章（主线锚点：周承在福记面馆的暗格里发现旧钥匙）
- 计划回收章：第8章
- 当前状态：pending（未释放）
- 来源：plan/大纲_第1-50章.md → 第3章 PLAN-NODE
- 禁止事项：回收前不得使用、不得改义、不得由无关角色持有
```

在正文创作阶段，这条债务会进入第 3 章的事实锁（“因果债”和“伏笔”两行），第 5-7 章的事实锁里也会带“不得使用旧钥匙”的提醒；只有第 8 章才把它标成 `released`。

**我**：那我怎么检查它没被乱写？

**Codex**：执行一致性检查，技能输出按固定四类分类：硬伤 / 风险 / 伏笔状态 / 通过项。伏笔状态必须给出“埋设章、计划回收章、当前状态”三个要素。检查本章（第 8 章）对应伏笔的示例输出：

```text
硬伤：无
风险：
- 第6章正文提及“周承腰间的钥匙”，疑似提前使用 → 需回看锚点确认不是同物
伏笔状态：
- 旧钥匙：第3章埋设，计划第8章回收，当前 pending
- 若第6章为同物：状态改判为由无关场景提前消费，方案为回写第6章或调整第8章回收方式
通过项：
- 第7章对话未提及钥匙，未提前泄漏
- 角色认知与事实锁一致
```

这里的关键点是检查报告不做“看起来没关系”的模糊结论，而是逐条给出证据位置与修复方向。

**我**：为什么把伏笔叫“债务”？

**Codex**：因为它需要兑现。作家记录它、技能盯着它：没到回收窗口就用了，叫“提前消费”；过了窗口太久没用，叫“超期”；被改成了别的东西，叫“变义”。一致性审查本质上是查这三点，再加死人复活、时间线错位、能力凭空升级这些硬伤。

### 总结

- 伏笔 = 待偿债务：埋设章、计划回收章、当前状态三要素齐全才可追踪。
- 审查输出固定分为硬伤 / 风险 / 伏笔状态 / 通过项，每一条都要有证据位置和修复方向。
- 伏笔三宗罪：提前消费、超期未收、改义。
- 伏笔登记进 `plan/伏笔追踪.md`，写作与审查阶段通过事实锁联动提醒。