# 第6章 搭建知识库

知识库的价值不在于“存了很多笔记”，而在于“需要的时候能搜到，并且敢用”。这两件事差得很远：全文搜索能给你十条结果，但其中可能互相矛盾、来源不明、甚至来自还没入库的草稿。这一章介绍两套 Obsidian 知识库 Skill，一套是规则优先的离线 RAG，一套是把 vault 当持久记忆的轻量方案，最后用一个结构报告把“能搜到”和“敢用”区分开。知识库的搭建不是收藏游戏，而是建立一套'敢用'的系统；这一章会一步步演示，怎么让每一条回答都有据可查、有源可追。

## 6.1 规则优先的离线 RAG

### 简介

`md-vault-rag-manager` 把 Obsidian vault 当成一个“有治理规则的知识系统”，而不是一个文件夹。它规定：规则区是权威，原始导入不等于知识，只有经过审阅的笔记才能进正式库；回答问题时强制先检索，再打开原文核对，最后只依据有来源的证据作答。它解决的是“能搜到”和“敢用”之间的差距。知识库的价值不在篇数，而在'敢用'：每一条结论都能追到原文，你才敢把它写进正式结论里。

默认目录结构是：

```text
00_规则/          规则与工作边界
01_导入原始材料/   原始剪藏、聊天记录、导入文件
02_入库处理区/     正在清洗、拆分、打标签、待审的笔记
10_正式库/         已审阅、可被检索和引用的正式知识
99_垃圾区/         拒绝、重复、过时、低价值内容
00_检索索引/       生成的本地检索索引
```

### 调用记录

**我**：我想按这套规则初始化一个最小 vault，放几篇笔记，然后问一个检索问题。

**Codex**：先建目录，再放三篇“正式库”笔记。为了验证它会不会发现矛盾，我故意让两篇互相支持、一篇冲突：

```markdown
# 项目A-计划.md
蓝鸟项目周期为 6 周，由李工负责，计划在第四季度上线。

# 项目A-复盘.md
项目复盘记录：蓝鸟项目周期 6 周，按期交付，客户验收通过。

# 供应商评估.md
供应商评估表格中，蓝鸟项目周期按 8 周预算，含两周缓冲。
```

**我**：索引怎么建？

**Codex**：技能自带无依赖的混合检索脚本，真实运行：

```powershell
python ...\scripts\build_hybrid_index.py --vault-root D:\vault
# {
#   "formal_root": "10_正式库",
#   "index_dir": "10_正式库/00_search_index",
#   "chunk_count": 3,
#   "excluded_file_count": 0,
#   "algorithm": "bm25_plus_exact_and_role_weight"
# }
```

三个 chunk 对应三篇笔记，算法是 BM25 + 精确匹配 + 角色权重；索引生成在 `10_正式库/00_search_index`。

**我**：问“蓝鸟项目周期多久”，会返回什么？

**Codex**：检索脚本真实返回三条：

```text
1. score=1.1    role=project      蓝鸟项目复盘
   path: 10_正式库/项目A-复盘.md
   ...蓝鸟项目周期 6 周，按期交付...

2. score=1.0869 role=project      蓝鸟项目计划
   path: 10_正式库/项目A-计划.md
   ...蓝鸟项目周期为 6 周...

3. score=0.8309 role=formal_note  供应商评估
   path: 10_正式库/供应商评估.md
   ...蓝鸟项目周期按 8 周预算，含两周缓冲...
```

**我**：那回答应该怎么给？直接说 6 周吗？

**Codex**：不能。按技能的强制离线 RAG 循环：

```text
question
-> read rules
-> search formal index or formal Markdown paths
-> filter by path and metadata
-> open original Markdown evidence
-> answer only from supported evidence
-> state uncertainty when evidence is insufficient
```

这三条结果是“候选”，必须打开原文核对。核对后的正确回答是：

```text
检索到 3 条正式库证据，存在口径冲突：
- 计划（项目A-计划.md）：6 周，李工负责
- 复盘（项目A-复盘.md）：6 周，按期交付
- 供应商评估（供应商评估.md）：8 周预算，含两周缓冲

冲突解释：前两条是项目口径（实际周期），第三条是预算口径（含缓冲）。
在作者确认“问的是实际周期还是预算口径”之前，不能把它们合并成一个数字。
```

**我**：它为什么不直接把三条揉成“大约 6 到 8 周”？

**Codex**：因为技能明确写了“不够支持就说不够支持，不要用通用知识补空白”。把矛盾磨平看起来聪明，实际是把两个不同口径的事实混成一个不可靠的数字。规则优先的 RAG 宁可在报告里暴露冲突，也不给你一个平滑但没法追责的答案。

把这一节放回整条链路里看，它只是其中一段；真正动手时不必追求一次全对，先把命令跑通、把输出对上，遇到报错再回来查对应位置，往往比从头读一遍更快。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- 规则区是权威，原始导入不是知识；只有审阅过的笔记进 `10_正式库`。
- 检索是混合式：BM25 + 精确匹配 + 角色权重，结果必须回原文核对。
- 强制离线 RAG 的固定顺序：读规则 → 检索 → 过滤 → 打开原文 → 只依据证据回答 → 不够就明说。
- 发现口径冲突时要标出冲突与来源，而不是把矛盾磨平成一个数字。
- 两篇 6 周、一篇 8 周的真实结果说明：知识库的“敢用”来自可追溯，而不是搜索条数。

## 6.2 插件市场安装与持久记忆

### 简介

`obsidian-knowledge` 把 Obsidian vault 当作 AI 的持久记忆层：搜索笔记、保存可复用知识、维护索引和链接，适合跨会话记住上下文。它与 6.1 的差异是轻重之分：`md-vault-rag-manager` 是严格的规则化 RAG 工作流，`obsidian-knowledge` 是更轻、更贴近“随手记”的记忆系统——把记忆写成 vault 里的笔记，下次会话搜回来。把 vault 当作记忆层是更轻的一种用法，适合跨会话记住上下文；这种路线的麻烦往往出在平台兼容上，这一节如实记下了。

它的记忆规则里有一条很关键：验证过的才能当事实写，并注明来源与不确定性；绝不未经批准写 `CLAUDE.md` / `AGENTS.md`。

### 调用记录

**我**：这个技能怎么装？

**Codex**：有两种路子。CLI 用 `uv` 装（需要 Python 3.12+）：

```powershell
uv tool install obsidian-knowledge
# Installed 3 executables: obsidian-knowledge, obsidian-knowledge-check, obsidian-knowledge-mcp
```

Codex 插件走市场：

```powershell
codex plugin marketplace add crypdick/obsidian-knowledge
# Added marketplace `obsidian-knowledge` ...

codex plugin add obsidian-knowledge@obsidian-knowledge
# Added plugin `obsidian-knowledge` from marketplace `obsidian-knowledge`.
# Installed plugin root: ...\obsidian-knowledge\3.30.19+codex.20261003154117
```

**我**：装完直接能用吗？

**Codex**：本机碰到一个真实的跨平台问题。`obsidian-knowledge --help` 报错：

```text
File "...\obsidian_knowledge\vault_index\index_lock.py", line 6, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'
```

`fcntl` 是 Linux/macOS 的模块，Windows 上没有。也就是说在 Windows 上直接跑 CLI 会崩；仓库是为 Unix 设计的，Windows 用户要么用 WSL，要么等作者发布 Windows 兼容版本，或者走插件宿主路径。

**我**：那跨会话记忆到底怎么工作？

**Codex**：按设计，vault 注册在 `~/.config/obsidian-knowledge/vaults.yaml`，记忆以笔记形式存在 vault 的 `wiki/` 目录，CLI 提供：

```bash
obsidian-knowledge search "概念或短语"
obsidian-knowledge read "wiki/某条笔记.md"
```

**我**：怎么演示“记住 → 新会话想起来”？

**Codex**：两种方式都能达到效果。理想流程是在会话里说“记住我的项目代号是 `bluebird`”，技能据此在 vault 里写一篇唯一的事实笔记（例如 `wiki/project-code.md`），并把“代号 bluebird”写进正文；下一次新会话问“我的项目代号是什么”，技能先 `search "bluebird"` 命中那篇笔记，`read` 后回答。关键是笔记自包含——不依赖原来那段对话也能看懂。

由于本机 CLI 在 Windows 上受 `fcntl` 阻塞，这次我用“按技能规则把笔记写入指定位置 + 搜索验证”来核对机制本身：记忆是文件，跨会话靠索引找回，而不是靠模型记住原文。等 Windows 兼容的发行改善了，这个闭环就能在本机完整跑通。

**我**：搜索 MCP 能找到 obsidian-knowledge 的公开教程吗？

**Codex**：检索到的是 Obsidian 通用教程和另一套 Obsidian Skills 的用法，不是这个项目的专门记录。它们能说明“vault + 笔记 + AI 编辑”这条大路，但命令不同，不能混用。因此本节仍以仓库 `SKILL.md` 和本机实跑为准：CLI 在 Windows 上因为 `fcntl` 缺失而失败，是真实结论；插件安装成功也是真实结论。

这些步骤看起来零散，其实前后是有因果的：前一步的产物就是后一步的输入，中间哪一环没对上，后面就会以各种奇怪的方式报错。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- `obsidian-knowledge` 把 vault 当记忆层：记忆 = 笔记文件，检索 = `search` + `read`。
- 安装有两条路：`uv tool install obsidian-knowledge`（CLI）与 Codex 插件市场（`codex plugin add obsidian-knowledge@...`）。
- 真实坑：Windows 上 CLI 会因缺少 Unix 专用模块 `fcntl` 崩溃，需要 WSL 或等兼容版本。
- 保存记忆前要验证事实并给出来源；跨会话复用靠 vault 索引，不靠模型记忆。
- 绝不未经批准写 `CLAUDE.md` / `AGENTS.md`。

## 6.3 带证据的检索与结构报告

### 简介

知识库“可用”和“能搜到”的分界线，是回答能不能追溯到原文。`md-vault-rag-manager` 要求结构报告逐条列出每条正式知识的来源路径和检索命中证据，而不是只给一个“知识库包含 N 篇笔记”的总量统计。只有总量的报告，说明它还在做“搜索”；有逐条来源和命中记录的，才是“RAG 管理”。能搜到和敢用之间的分界，就是报告里有没有逐条列出来源；这一节用一个结构报告让这个差别变得看得见。

### 调用记录

**我**：给 6.1 的 vault 出一份结构报告，要列出每条正式知识的来源路径和检索命中情况。

**Codex**：我用 6.1 的 vault 做了三轮真实检索（“蓝鸟项目周期多久”“负责人是谁”“供应商怎么评价”），把每次返回的命中记录下来。`build_hybrid_index.py` 在 `10_正式库/00_search_index/` 下生成了四个索引文件：

```text
chunks.jsonl          分块与路径
metadata.json         每条知识元数据
tokens.json           词项统计
excluded_files.json   被排除的文件
```

结合三轮检索结果，结构报告逐条如下：

```markdown
## 结构报告：蓝鸟知识库（10_正式库）

### 10_正式库/项目A-计划.md
- 正式知识：蓝鸟项目周期 6 周，负责人李工，第四季度上线
- 检索命中：3 轮查询全部命中，最高分 1.1
- 命中证据片段：# 蓝鸟项目计划 …周期为 6 周，由李工负责…

### 10_正式库/项目A-复盘.md
- 正式知识：蓝鸟项目周期 6 周，按期交付
- 检索命中：3 轮查询全部命中，最高分 1.1
- 命中证据片段：# 蓝鸟项目复盘 …周期 6 周，按期交付…

### 10_正式库/供应商评估.md
- 正式知识：周期按 8 周预算，含两周缓冲（预算口径）
- 检索命中：3 轮查询全部命中，最高分 1.12
- 命中证据片段：# 供应商评估 …周期按 8 周预算…
```

**我**：这份报告和“知识库包含 3 篇笔记”有什么区别？

**Codex**：区别在“能否追责”。总量统计只回答了广度；逐条报告回答的是“这个结论来自哪篇、有没有被检索命中过、命中证据长什么样”。你在上面能看到矛盾：两篇是 6 周、供应商评估是 8 周。如果只有总量统计，你会以为“库里有三篇，规模正常”；有了逐条命中记录，你才能在回答前发现口径冲突并让作者确认。

**我**：报告里“命中证据片段”是不是就够了？

**Codex**：不够，片段只是“候选检索结果”。技能规定最终回答前必须打开原始 Markdown 核对，索引分片只能当候选。所以结构报告的证据列给出的是路径引用，真正的核对动作是 `read` 那篇原文，再引用具体行。

如果只记住一句，那就是：先让最小链路真实跑通，再谈优化和自动化；跳过验证直接堆功能，最后往往要花更多时间回头补。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- 结构报告的价值是逐条可追责：每条正式知识给出来源路径、命中次数和证据片段。
- 只有总量统计（N 篇笔记）是“搜索”，有逐条来源是“RAG 管理”。
- 索引文件（chunks / metadata / tokens）是候选集合，不是最终证据。
- 回答前必须打开原文核对，并在报告里标注每篇命中的最高分与路径。
- 结构报告还会让口径冲突暴露在眼皮底下，而不是被藏在“大概可以”里。