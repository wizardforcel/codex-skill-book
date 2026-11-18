# Market Research Reports V2
Market Research Reports V2 is a Codex skill for consulting-style market research and investment research reports. It is adapted from the `market-research-reports` skill distributed via `davila7/claude-code-templates`, with extra interactive intake and investment research guardrails.
## What It Does
- Generate comprehensive market research reports in a consulting/research-institution style.
- Support market sizing, value chain analysis, competitive landscape, growth drivers, risks, strategic recommendations, and investment thesis sections.
- Reuse the original report assets, references, LaTeX template, and visual generation script.
- Ask scoping questions before writing when the user has not provided enough context.
- Add investment research anti-hallucination rules for source-traceable data and safer conclusions.
## What's New In V2
- One scoping question at a time before report generation.
- Each question uses `A/B/C/Other` choices to reduce user input friction.
- Custom answers are supported through `D. Other`.
- The collected scope is summarized for confirmation before generation starts.
- Investment research workflows automatically add stricter source, uncertainty, and risk-disclosure rules.
## Installation
Install with the Codex skill installer:
```bash
npx skills add https://github.com/kikiyang0129/market-research-reports-v2.git --skill market-research-reports-v2 -g -y
```
You can also ask Codex:
```text
请安装这个 skill：https://github.com/kikiyang0129/market-research-reports-v2.git
```
## Trigger
Use one of these phrases:
```text
请使用 market-research-reports-v2 skill，帮我研究半导体行业。
```
```text
请使用 market-research-reportsV2，帮我做一份光模块行业投资研究报告。
```
## Interactive Intake Example
When scope is missing, the skill asks one question at a time:
```text
第 1 问：你的研究目的是什么？
A. 投资研究/行业投资框架（推荐）
B. 入门科普/快速看懂行业
C. 市场进入/战略规划
D. 其他：请直接填写
```
Reply with `A`, `B`, `C`, or write a custom answer.
## Investment Research Guardrails
For investment-oriented reports, V2 adds these rules:
- All key data must include source link, publication date, and institution name.
- Unsupported data must not be invented; mark it as `待验证`.
- Separate facts, estimates, judgments, and assumptions.
- When source methodologies differ, list the differences instead of forcing one merged number.
- Every chart number must be traceable to a source or calculation process.
- Investment conclusions must include counterarguments and risks.
- Do not provide direct buy/sell advice by default; provide research framework and decision evidence.
## Repository Structure
```text
SKILL.md
assets/
references/
scripts/
README.md
LICENSE
```
## Attribution
This repository is adapted from the `market-research-reports` skill distributed via [`davila7/claude-code-templates`](https://github.com/davila7/claude-code-templates).
The upstream `davila7/claude-code-templates` project credits [`K-Dense-AI/claude-scientific-skills`](https://github.com/K-Dense-AI/claude-scientific-skills) by K-Dense Inc. for Scientific Skills.
V2 modifications in this repository add interactive `A/B/C/Other` intake, scope confirmation, and investment research anti-hallucination rules.
## License
MIT License. Upstream copyright notices are retained in `LICENSE`.
## Disclaimer
This skill is for research and education workflows. It does not provide financial, legal, tax, or investment advice.
