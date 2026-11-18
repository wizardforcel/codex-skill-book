# Offline RAG Implementation

## Core Model

An LLM starts fresh on each call. The fixed retrieval behavior must live outside the model, in a local controller program.

Standard loop:

```text
user question
-> local RAG controller
-> retrieve from knowledge base
-> filter by rules and metadata
-> collect evidence snippets
-> compose prompt
-> call offline LLM
-> produce answer
```

Do not ask the model to decide whether retrieval is needed. For offline knowledge-base QA, retrieve first every time.

## Prompt Template

```text
Answer only from the knowledge-base content below.
If the knowledge base does not contain enough support, say: The vault does not contain enough support.
Do not fill gaps with external knowledge.

Rule summary:
{rules_summary}

Retrieved knowledge-base content:
{contexts}

User question:
{question}
```

## Retrieval Steps

```text
1. Receive the user question.
2. Load the entry rule and retrieval rules.
3. Search the formal-library index.
4. Exclude raw, pending, rejected, unverified, Inbox, Archive, and trash.
5. Prefer stable cards, formal notes, project home pages, and vetted references.
6. Open original Markdown for verification.
7. Put evidence, paths, titles, and summaries into the prompt.
8. Ask the model to answer from evidence.
```

## Metadata Filtering

Prefer:

```text
status: reviewed
status: evergreen
truth_status: source_backed
truth_status: self_confirmed
```

Exclude:

```text
status: raw
truth_status: unverified
truth_status: discarded
type: inbox
pending
rejected
unclassified
```

## Vertical-Domain Vaults

Each vertical domain should have its own rule entry and formal retrieval scope:

```text
Legal vault -> search only the legal formal library
Medical vault -> search only the medical formal library
Project vault -> search only the project formal library
Personal thinking vault -> prefer extracted cards
```

The fixed behavior comes from:

```text
controller-enforced retrieval
rule-limited scope
metadata-based trust filtering
prompt-level ban on unsupported answers
insufficient-evidence fallback
```
