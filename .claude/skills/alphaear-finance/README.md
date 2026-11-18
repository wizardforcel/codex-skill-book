# AlphaEar Finance for Codex

面向 Codex 的本地财经研究 skill，覆盖 A 股、港股、美股行情与基本面、财经新闻、情绪分析、搜索与本地 RAG、Kronos 预测、信号整理、研报结构化和图表输出。

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

> 本项目用于研究与信息整理，不构成投资建议。行情、新闻、情绪和模型预测均可能延迟、缺失或出错。

## 仓库结构

```text
.
├── alphaear-finance/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/api-reference.md
│   └── scripts/
├── tests/smoke_test.py
├── pyproject.toml
└── README.md
```

`alphaear-finance/` 是 Codex 可直接发现的 skill。本 README 只负责安装、运行和 GitHub 维护说明。

## 本机安装

要求 Python 3.11+ 和 [uv](https://docs.astral.sh/uv/)。

```bash
git clone https://github.com/Lupumbba/alphaear-finance.git
cd alphaear-finance
uv sync
ln -s "$(pwd)/alphaear-finance" "$HOME/.codex/skills/alphaear-finance"
```

如果目标链接已经存在，先确认它指向哪里，不要直接覆盖。重新启动 Codex 后，可在对话中使用：

```text
使用 $alphaear-finance 分析 NVDA 最近三个月的价格、基本面和相关新闻，并列出风险。
```

## 依赖层级

基础能力（数据库、股票、新闻、DeepEar）：

```bash
uv sync
```

研究能力（LLM、情绪、搜索、RAG、图表）：

```bash
uv sync --extra research
```

重型预测能力（包含研究能力、PyTorch 与 Kronos）：

```bash
uv sync --extra predictor
```

## 环境变量

按需设置，不要提交 `.env`：

| 变量 | 用途 |
|---|---|
| `LLM_PROVIDER`, `LLM_MODEL`, `LLM_HOST` | 默认 LLM 路由 |
| `OPENAI_API_KEY` | OpenAI |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `DASHSCOPE_API_KEY` | 通义千问 |
| `OPENROUTER_API_KEY` | OpenRouter |
| `JINA_API_KEY` | Jina 搜索与正文提取 |
| `SENTIMENT_MODE` | `auto`、`bert` 或 `llm` |
| `EMBEDDING_MODEL` | 搜索或预测所用 embedding 模型 |

完整配置和类签名见 [API 参考](alphaear-finance/references/api-reference.md)。

## 验证

```bash
uv run python tests/smoke_test.py
uv run python /path/to/quick_validate.py alphaear-finance
```

Smoke test 不访问外部网络，只验证基础模块导入、SQLite 写入/读取和核心类可用性。研究与预测 extras 需要单独安装后再验证对应导入。

## 本地运行与 GitHub 同步

本机 Codex 通过符号链接直接读取这个 Git 仓库中的 `alphaear-finance/`，因此仓库内的修改会立即成为本地 skill 的修改。推送流程：

```bash
git status --short
git --no-pager diff
git add README.md pyproject.toml tests alphaear-finance
git commit -m "update alphaear finance skill"
git push
```

运行 skill 不会自动提交或上传 API key、SQLite 数据、缓存或 `.env`；这些文件均由 `.gitignore` 排除。只有明确执行 Git 提交和推送后，变更才会同步到 GitHub。

## 关键约定

- 只从 `core`、`news`、`sentiment`、`search`、`predictor`、`tracker`、`reporter`、`visualizer`、`deepear` 顶层包导入。
- 不要混用 `tracker/utils`、`reporter/utils`、`predictor/utils` 的镜像模块。
- SQLite 使用绝对路径。
- 美股最新历史行情优先直接使用 `yfinance`。
- Kronos 预测需要 `predictor` extra，并可能首次下载 Hugging Face 模型。
- 输出必须标明数据时间、来源、假设、缺失项和风险。

## 来源与许可证

本 Codex 封装基于 [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) 整理和适配。上游项目采用 Apache License 2.0；仓库根目录的 [LICENSE](LICENSE) 是从上游原样附带的许可证文件。

本仓库包含上游发布的新闻投影 checkpoint。运行 Kronos 预测时还会从 Hugging Face 下载 `NeoQuasar/Kronos-base` 和 `NeoQuasar/Kronos-Tokenizer-base`，它们标注为 MIT License。完整归属与分发说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
