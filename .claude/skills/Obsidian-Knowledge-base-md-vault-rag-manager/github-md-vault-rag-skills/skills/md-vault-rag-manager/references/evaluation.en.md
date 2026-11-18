# RAG Testing Without Gold Answers

You can evaluate knowledge-base QA without a gold answer. First test whether the answer is grounded in the vault, not whether it matches a reference answer.

## Recommended Metrics

```text
Rule compliance: Did the agent read rules and search only allowed scope?
Retrieval hit rate: Does Top K include the expected formal evidence?
Faithfulness: Are answer claims supported by retrieved context?
Relevance: Does the answer directly address the question?
Context utilization: Did it use the most important formal cards/notes?
Abstention quality: Does it say evidence is insufficient when needed?
```

## Metrics That Need More Data

```text
Answer correctness: usually needs a gold answer.
Context recall: usually needs reference contexts or a gold answer.
```

## Test Case Format

```yaml
- question: What is emotional dissociation, and when does it tend to appear?
  expected_scope: formal/thinking/extracted_cards
  must_use:
    - Emotions are radar, not the steering wheel
  should_use:
    - In low periods, restore life order before redesigning life
    - How to tell whether a relationship is growth or depletion
  forbidden:
    - using raw records as final conclusions
    - letting external sources override the vault
```

## Scoring

```text
5: Fully rule-compliant, grounded, and clear.
4: Mostly compliant with minor missing context.
3: Relevant answer but incomplete evidence chain.
2: Clear retrieval or boundary mistake.
1: Mostly answered from common knowledge or external sources.
0: Did not search the vault or used forbidden sources.
```
