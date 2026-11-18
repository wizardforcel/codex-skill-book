# Obsidian Personal Vault RAG Skills / 黑曜石个人知识库 RAG Skills

English: Codex Skills for building and using an Obsidian personal knowledge vault with rule-first offline RAG.

中文：这是一套面向 Obsidian/黑曜石个人知识库构建的 Codex Skills，用于首次引导、规则化整理、本地混合检索和基于正式库证据的问答。

## What It Is / 这是什么

This repository helps an AI assistant treat your Obsidian vault as a governed personal knowledge system rather than a loose folder of Markdown files.

这个仓库让 AI 把你的 Obsidian 库当成一个有规则、有边界、可长期维护的个人知识系统，而不是随便搜索一堆 Markdown。

## Core Idea / 核心思想

```text
Rules folder defines workflow and boundaries.
Import area stores raw captures.
Processing area cleans and reviews material.
Formal library provides answer evidence.
Indexes and MOCs are navigation only.
The model must return to original Markdown evidence before answering.
```

```text
规则区决定流程和边界。
导入区保存原始材料。
处理区负责清洗和审核。
正式库提供回答依据。
索引和 MOC 只负责导航。
模型回答前必须回到原始 Markdown 证据。
```

## What To Upload / 发布时上传什么

Upload the whole `github-md-vault-rag-skills` folder.

请上传整个 `github-md-vault-rag-skills` 文件夹。

```text
github-md-vault-rag-skills/
  skills/md-vault-rag-manager/       # Codex Skill: executor and workflow
  templates/zh-CN/00_规则/            # Chinese Obsidian rules template
  templates/README.zh-CN.md
  templates/README.en.md
  README.md
  README.zh-CN.md
  README.en.md
```

Important: `skills/md-vault-rag-manager` alone is not the full rule library. The intended open-source package is the Skill plus `templates/zh-CN/00_规则`.

注意：只上传 `skills/md-vault-rag-manager` 不够。Skill 是执行层，`templates/zh-CN/00_规则` 才是规则模板本体。

## First-Time Use / 初次使用

1. Prepare or back up an Obsidian vault.
2. Copy `templates/zh-CN/00_规则` into the vault root and keep the folder name `00_规则`.
3. Copy `skills/md-vault-rag-manager` into your Codex skills directory.
4. Start a new Codex session and invoke:

```text
Use $md-vault-rag-manager to initialize my Obsidian personal knowledge vault. Read 00_规则 first and follow the first-use guide.
```

中文可这样说：

```text
使用 $md-vault-rag-manager 初始化我的 Obsidian 个人知识库，先读取 00_规则，并按首次使用引导检查结构。
```

The model should first read:

```text
00_规则/00_AI工作入口.md
```

## Recommended Vault Structure / 推荐库结构

```text
your-obsidian-vault/
  00_规则/            rules, onboarding, retrieval boundaries
  01_导入原始材料/     raw captures, clippings, chats, temporary material
  02_入库处理区/       material being cleaned, split, tagged, or reviewed
  10_正式库/           reviewed knowledge used for retrieval and answers
  99_垃圾区/           duplicate, rejected, obsolete, or low-value material
  00_检索索引/         generated local retrieval index
```

## Daily Personal Use / 日常个人用法

```text
把这些新材料放入导入区，并判断是否值得入库。
整理处理区里的文件，按规则拆分、命名、打标签。
检索正式库，回答我关于某个主题的问题。
检查正式库里是否有重复、冲突或过时内容。
帮我把这段思考提炼成可入库的正式笔记。
```

## Offline Search / 断网检索

Build an index:

```bash
python skills/md-vault-rag-manager/scripts/build_hybrid_index.py --vault-root /path/to/vault
```

Search:

```bash
python skills/md-vault-rag-manager/scripts/search_hybrid.py --vault-root /path/to/vault "your question"
```

The scripts are dependency-free and can run in disconnected environments.

## More Docs / 更多说明

- [中文完整说明](README.zh-CN.md)
- [English README](README.en.md)
- [中文模板说明](templates/README.zh-CN.md)
- [Template Guide](templates/README.en.md)

## License

MIT
