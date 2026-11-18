---
name: md-vault-rag-manager
description: Build, initialize, audit, and use Obsidian personal knowledge bases with rule-first offline RAG. Use when Codex needs to guide a first-time personal vault setup, read or create a `00_规则` rules folder, organize raw notes into a formal library, generate human onboarding guidance, build or refresh a local hybrid retrieval index, answer questions primarily from a mounted Obsidian/Markdown vault, enforce formal-content-only retrieval, or prepare vertical-domain personal knowledge bases that should avoid external sources unless explicitly requested.
---

# Obsidian Personal Vault RAG Manager

Use this skill to make Codex treat an Obsidian personal vault as a governed knowledge system: capture first, process deliberately, promote only reviewed notes into the formal library, and retrieve evidence before answering.

## Core Contract

Always keep these boundaries:

- Treat the rules folder as the authority. Default name: `00_规则`; common English equivalent: `00_rules`.
- Treat the vault as a personal working system, not a public encyclopedia. Preserve the user's structure, language, naming habits, and review gates unless asked to redesign them.
- Treat indexes, MOCs, guides, and Bases as navigation or status views, not final evidence.
- Treat raw records, inboxes, pending candidates, rejected content, archives, and trash as excluded from final answers unless the task is cleanup or source tracing.
- Prefer formal, reviewed, source-backed, or self-confirmed notes as answer evidence.
- If the vault has no adequate evidence, say that the vault does not contain enough support. Do not fill gaps from general knowledge unless the user asks for it.

## Personal Vault Structure

Use this default mental model unless the local rules say otherwise:

```text
00_规则/            rules, onboarding, workflow boundaries
01_导入原始材料/     raw captures, imports, clippings, chat logs
02_入库处理区/       notes being cleaned, split, tagged, or reviewed
10_正式库/           reviewed knowledge used for retrieval and answers
99_垃圾区/           rejected, duplicate, obsolete, or low-value material
00_检索索引/         generated local retrieval index
```

For Obsidian, keep Markdown links, tags, aliases, frontmatter, MOCs, and Bases useful for navigation, but do not treat navigation artifacts as final evidence.

## Workflow

1. Locate the vault root.
2. Find the rules folder. Prefer `00_规则`; otherwise look for `00_rules`, `rules`, or a user-provided path.
3. Read the entry rule first. Prefer `00_AI工作入口.md` or `00_AI_entry.md`.
4. Select the task path:
   - First-time onboarding or initialization: read `references/rules.zh-CN.md` or `references/rules.en.md`.
   - Question answering over the vault: read `references/offline-rag.zh-CN.md` or `references/offline-rag.en.md`.
   - Retrieval evaluation: read `references/evaluation.zh-CN.md` or `references/evaluation.en.md`.
5. Use scripts only when local indexing or search is useful:
   - Build index: `scripts/build_hybrid_index.py`
   - Search index: `scripts/search_hybrid.py`
6. Open original Markdown files before final answers. Use index chunks only as candidate retrieval results.

## First-Time Onboarding

When the user asks to initialize a vault, connect a new model, or follow first-use guidance:

1. Read the rule entry, rule overview, global structure, SOP, human guide, and first-access rule if present.
2. If the vault has no rules folder and the repository template is available, propose copying `templates/zh-CN/00_规则` into the vault root as `00_规则`.
3. Check that the vault has a rules folder, import queue, processing queue, formal library, trash/archive area, and generated-index location.
4. Confirm there is a concise human-facing usage guide and make it easy for the user to follow.
5. Confirm content areas do not contain competing rule files.
6. Produce a short human report: rules read, current vault state, missing folders, suggested first action, and how the user should ask questions next.

Do not output the full AI rule corpus to the user. Summarize human-facing usage.

## Personal Use Modes

Map ordinary personal usage to one of these modes:

- Capture: place raw material into the import area without treating it as knowledge.
- Process: clean, split, summarize, tag, and route material through the processing area.
- Promote: move only reviewed or trusted notes into the formal library.
- Retrieve: search the formal library first, then open original Markdown evidence.
- Reflect: support thinking, synthesis, and project review while marking uncertainty and evidence boundaries.
- Maintain: audit duplicate notes, broken links, stale tags, empty MOCs, and rule conflicts.

## Forced Offline RAG

For normal user questions, do not ask the model to decide whether to search. Search first.

Use this fixed loop:

```text
question
-> read rules
-> search formal index or formal Markdown paths
-> filter by path and metadata
-> open original Markdown evidence
-> answer only from supported evidence
-> state uncertainty when evidence is insufficient
```

Use external/web knowledge only when the user explicitly asks for it or the vault rules allow it for the task.

## Suggested Vault Defaults

Default formal scope:

```text
10_正式库/
10_formal_library/
formal/
knowledge/
```

Default exclusions:

```text
01_导入原始材料
02_入库处理区
99_垃圾区
05_Inbox
Inbox
Archive
trash
raw
pending
rejected
unverified
```

Default stable evidence signals:

```text
status: reviewed
status: evergreen
truth_status: source_backed
truth_status: self_confirmed
#入库/已入库
#归类/已归类
```

## Commands

Build a local index:

```bash
python skills/md-vault-rag-manager/scripts/build_hybrid_index.py --vault-root /path/to/vault
```

Search the local index:

```bash
python skills/md-vault-rag-manager/scripts/search_hybrid.py --vault-root /path/to/vault "your question"
```

Both scripts are dependency-free Python and are designed for disconnected environments.
