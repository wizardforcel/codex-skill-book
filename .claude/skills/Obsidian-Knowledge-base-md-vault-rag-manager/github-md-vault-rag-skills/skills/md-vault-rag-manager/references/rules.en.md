# Rule-First Vault Specification

## Goal

Turn a Markdown/Obsidian folder into a governed offline knowledge base that an LLM can use reliably.

Core idea:

```text
The rules folder defines process and boundaries.
The formal library provides usable knowledge.
Indexes and MOCs are navigation only.
Retrieval indexes only recall candidates.
Final answers must return to original Markdown evidence.
```

## Recommended Structure

```text
00_rules/
01_import_raw/
02_processing_queue/
10_formal_library/
99_trash/
```

Formal library:

```text
10_formal_library/
  00_library_index.md
  00_search_index/
  01_notes/
  02_thinking/
  03_projects/
  04_daily_logs/
```

Chinese vaults may use equivalent names such as `00_规则` and `10_正式库`.

## Rules Folder

The rules folder should contain only workflows, boundaries, templates, reading order, and retrieval constraints.

Typical rule files:

```text
00_AI_entry.md
01_rules_overview.md
02_global_structure.md
06_call_filtering_and_tag_search.md
11_fixed_sop.md
18_hybrid_retrieval_and_vector_index.md
19_first_access_and_onboarding.md
```

Do not duplicate rules inside content areas. `00_index`, MOCs, guides, and status views are navigation or state, not rules.

## First Access

When a model first receives the vault, require:

```text
read entry rule
-> read rules overview
-> read global structure
-> read fixed SOP
-> inspect folder skeleton
-> inspect human-facing usage guide
-> detect scattered or conflicting rules
-> output a short onboarding report
```

The human guide should be concise and explain:

```text
where to put materials
available work modes
which labels humans edit
where results appear
rules folder vs content areas
```

Do not print the complete AI rule corpus to the user.

## Formal Library Boundaries

Default allowed signals:

```text
inside formal library
status: reviewed or evergreen
truth_status: source_backed or self_confirmed
approved/imported/classified tags
summary present
```

Default exclusions:

```text
import area
processing queue
trash
Inbox
Archive
raw
pending
rejected
unverified
raw chat logs as final evidence
```

## Thinking Area Boundary

If the vault has a thinking/speculative area:

```text
MOCs/indexes: navigation only.
Raw records: source tracing or pending extraction only.
Extracted cards: preferred stable viewpoint sources.
```

Do not use raw chats directly as stable knowledge.

## Answering Rule

Before answering:

```text
search formal library
filter metadata
open original Markdown
answer from evidence
```

If evidence is insufficient, say:

```text
The vault does not contain enough support.
```

Do not fill gaps from general model knowledge unless the user explicitly asks for external or general knowledge.
