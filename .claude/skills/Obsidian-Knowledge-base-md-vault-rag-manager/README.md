# Obsidian Personal Vault RAG Skills

This repository provides Codex Skills for building and using an Obsidian personal knowledge vault with rule-first offline RAG. It is not just a search script. It is a guided workflow for helping an AI assistant initialize a vault, respect your rules, separate raw captures from reviewed knowledge, and answer from evidence.

## One-Line Summary

Turn an Obsidian vault into an AI-usable personal knowledge system: you capture, judge, and refine; the AI follows the rules, organizes material, retrieves evidence, and states gaps clearly.

## Who It Is For

- People who use Obsidian as a long-term personal knowledge base.
- People with many Markdown notes but unstable structure or retrieval.
- People who want AI answers to come primarily from their own vault.
- People who need local-first or disconnected workflows.
- People who want to turn reading notes, projects, reflections, logs, and clippings into reviewed knowledge.

## What It Includes

- A reusable Chinese rules-folder template: `templates/zh-CN/00_规则`.
- A Codex Skill: `skills/md-vault-rag-manager`.
- First-use onboarding so the model knows what to read and check first.
- Personal vault boundaries: rules, imports, processing, formal library, trash, generated index.
- Hybrid retrieval guidance: keyword search, tag filtering, path filtering, index recall, original Markdown evidence.
- Dependency-free local scripts for offline search.
- Chinese and English documentation for open-source use.

## Repository Structure

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

Uploading only `skills/md-vault-rag-manager` is not enough. The Skill is the executor; `templates/zh-CN/00_规则` is the reusable rules layer. Publish the whole `github-md-vault-rag-skills` folder.

## Recommended Vault Structure

```text
your-obsidian-vault/
  00_规则/            AI entry, rule overview, retrieval rules, onboarding
  01_导入原始材料/     raw captures, clippings, chats, temporary material
  02_入库处理区/       material being cleaned, split, tagged, or reviewed
  10_正式库/           reviewed knowledge used for retrieval and answers
  99_垃圾区/           duplicate, rejected, obsolete, or low-value material
  00_检索索引/         generated local retrieval index
```

The core principle: raw material is not knowledge, MOCs are not evidence, and the formal library is the default answer source.

## First-Time Guide

### 1. Prepare an Obsidian vault

Use either a new vault or an existing one. Back up important vaults before restructuring.

### 2. Copy the rules template

Copy this folder into the root of your Obsidian vault:

```text
templates/zh-CN/00_规则
```

Keep the copied folder name as:

```text
00_规则
```

### 3. Install the Skill

Copy the Skill folder:

```bash
cp -R skills/md-vault-rag-manager ~/.codex/skills/
```

On Windows, copy:

```text
skills\md-vault-rag-manager
```

to:

```text
%USERPROFILE%\.codex\skills\md-vault-rag-manager
```

### 4. Ask Codex to initialize the vault

Start a new Codex session and say:

```text
Use $md-vault-rag-manager to initialize my Obsidian personal knowledge vault. Read 00_规则 first and follow the first-use guide.
```

The model should first read:

```text
00_规则/00_AI工作入口.md
```

It should then give a short report: rules read, current structure, missing folders, and the next recommended action.

### 5. Start using it personally

Typical requests:

```text
Put these new materials into the import area and decide whether they are worth processing.
Clean the processing folder according to the rules: split, name, tag, and route notes.
Search the formal library and answer my question from vault evidence.
Check the formal library for duplicates, conflicts, or stale notes.
Turn this reflection into a formal note that can be promoted into the library.
```

## Retrieval And Answering Logic

Default loop:

```text
user question
-> read 00_规则
-> search 10_正式库 or the rule-defined formal area
-> filter by path, tag, and status
-> open original Markdown files
-> answer only from supported evidence
-> state insufficiency when evidence is weak
```

Indexes, MOCs, Bases, and directory pages are navigation aids. Final answers should return to concrete Markdown notes.

## Offline Search

Build an index:

```bash
python skills/md-vault-rag-manager/scripts/build_hybrid_index.py --vault-root /path/to/vault
```

Search:

```bash
python skills/md-vault-rag-manager/scripts/search_hybrid.py --vault-root /path/to/vault "your question"
```

The scripts are dependency-free and designed for local or disconnected environments.

## Personal Usage Pattern

This Skill is designed for long-term maintenance, not just one-time cleanup.

- Capture: put uncertain material into the import area.
- Process: split, summarize, deduplicate, tag, and add sources.
- Promote: move only stable, valuable, reusable notes into the formal library.
- Retrieve: search the formal library first when answering.
- Reflect: synthesize projects, ideas, and long-term themes.
- Maintain: audit broken links, empty MOCs, duplicate files, tag drift, and rule conflicts.

## What Is Not Included

This open-source package does not include your private formal library, raw material, processing queue, or personal notes. It includes only the rule template, Skill instructions, and local retrieval scripts.
