# Obsidian Personal Vault RAG Skills 中文说明

这是一套面向 Obsidian 个人知识库的 Codex Skills。它不是简单的“搜索脚本”，而是一套让 AI 帮你建立、维护、检索个人知识库的规则化工作流：先读规则区，再区分原始材料和正式知识，最后基于正式库证据回答。

## 一句话介绍

把 Obsidian 知识库变成一个可被 AI 稳定使用的个人知识系统：你负责记录、判断和沉淀，AI 负责按规则整理、检索、提示缺口和辅助回答。

## 适合谁

- 想用 Obsidian 管理长期个人知识的人。
- 已经有大量 Markdown 笔记，但结构混乱、检索不稳定的人。
- 希望 AI 回答问题时优先查自己的知识库，而不是凭空发挥的人。
- 需要断网或本地优先工作流的人。
- 想把思辨、项目、阅读、日记、资料剪藏逐步整理成正式库的人。

## 它提供什么

- 一套可复制的中文规则区模板：`templates/zh-CN/00_规则`。
- 一个 Codex Skill：`skills/md-vault-rag-manager`。
- 首次接入引导：让模型第一次打开知识库时知道先读什么、检查什么、输出什么。
- 个人知识库分区规则：规则区、导入区、处理区、正式库、垃圾区、检索索引。
- 混合检索规则：关键词检索、标签过滤、路径过滤、索引召回、回到原文证据。
- 断网可用脚本：无需第三方依赖即可构建本地检索索引。
- 双语说明：中文主用，英文方便开源传播。

## 仓库结构

```text
github-md-vault-rag-skills/
  skills/md-vault-rag-manager/       # Codex Skill，负责执行流程
  templates/zh-CN/00_规则/            # Obsidian 中文规则区模板
  templates/README.zh-CN.md
  templates/README.en.md
  README.md
  README.zh-CN.md
  README.en.md
```

只上传 `skills/md-vault-rag-manager` 不够。Skill 是执行层，`templates/zh-CN/00_规则` 才是规则模板本体。开源时请上传整个 `github-md-vault-rag-skills` 文件夹。

## 推荐的个人知识库结构

```text
你的Obsidian库/
  00_规则/            AI 工作入口、规则总览、检索规则、首次接入说明
  01_导入原始材料/     剪藏、聊天记录、网页摘录、临时材料
  02_入库处理区/       等待清洗、拆分、打标签、审核的材料
  10_正式库/           已整理、可检索、可作为回答依据的内容
  99_垃圾区/           重复、低价值、废弃、拒绝入库内容
  00_检索索引/         自动生成的本地索引
```

核心原则很简单：原始材料不等于知识，MOC 不等于证据，正式库才是默认回答依据。

## 初次使用引导

### 1. 准备一个 Obsidian 库

可以是全新的库，也可以是已经使用了一段时间的库。建议先备份原库。

### 2. 复制规则区模板

把下面这个目录复制到你的 Obsidian 库根目录：

```text
templates/zh-CN/00_规则
```

复制后保持名称为：

```text
00_规则
```

### 3. 安装 Skill

把 Skill 目录复制到 Codex 的 skills 目录：

```text
skills\md-vault-rag-manager
```

Windows 默认位置：

```text
%USERPROFILE%\.codex\skills\md-vault-rag-manager
```

### 4. 第一次让 AI 接入

新开一个 Codex 会话后，可以这样说：

```text
使用 $md-vault-rag-manager 初始化我的 Obsidian 个人知识库，先读取 00_规则，并按首次使用引导检查结构。
```

模型应该先读取：

```text
00_规则/00_AI工作入口.md
```

然后给你一份简短报告：读了哪些规则、当前结构是否完整、缺什么目录、下一步应该怎么做。

### 5. 开始个人使用

日常可以按这几类请求使用：

```text
把这些新材料放入导入区，并判断是否值得入库。
整理处理区里的文件，按规则拆分、命名、打标签。
检索正式库，回答我关于某个主题的问题。
检查正式库里是否有重复、冲突或过时内容。
帮我把这段思考提炼成可入库的正式笔记。
```

## 检索与回答逻辑

默认流程是：

```text
用户问题
-> 读取 00_规则
-> 检索 10_正式库 或规则指定的正式内容区
-> 用路径、标签、状态过滤
-> 打开原始 Markdown 文件
-> 只基于证据回答
-> 证据不足时明确说明不足
```

索引、MOC、Bases、目录页只负责导航，不能直接当最终依据。最终回答必须回到具体 Markdown 笔记。

## 断网检索

构建索引：

```bash
python skills/md-vault-rag-manager/scripts/build_hybrid_index.py --vault-root /path/to/vault
```

搜索：

```bash
python skills/md-vault-rag-manager/scripts/search_hybrid.py --vault-root /path/to/vault "你的问题"
```

这两个脚本无第三方依赖，适合本地和断网环境。

## 个人使用方式

这套 Skill 更适合“长期维护”而不是“一次性整理”。

- 捕获：先把不确定材料放入导入区。
- 处理：拆分、摘要、去重、打标签、补来源。
- 入库：只有稳定、有价值、可复用的内容进入正式库。
- 检索：提问时优先检索正式库。
- 反思：对观点、项目和长期主题做周期复盘。
- 维护：定期检查坏链接、空 MOC、重复文件、标签漂移和规则冲突。

## 不包含什么

这个开源包不包含你的私人正式库、原始材料、处理区和个人笔记。它只提供规则模板、Skill 指令和本地检索脚本。

## 开源发布建议

上传整个 `github-md-vault-rag-skills` 文件夹即可。别人克隆后，可以复制 `templates/zh-CN/00_规则` 到自己的 Obsidian 库，再安装 `skills/md-vault-rag-manager`，按首次引导开始构建自己的个人知识库。
