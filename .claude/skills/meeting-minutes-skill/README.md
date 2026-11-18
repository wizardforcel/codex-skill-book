<div align="center">

# 🎙️ Meeting Minutes Skill · 会议纪要

![Jiale的AI工坊 · 正式会议纪要：录音转写、整理纪要、导出 Word](docs/images/hero-jiale-ai-workshop.png)

**录音一键转写 → 结构化正式会议纪要 → 导出 Word**

把一段会议录音、背景信息和可选的 PPT，自动变成一份排版规整、可直接交付的中文会议纪要。

[![Skill](https://img.shields.io/badge/Claude_Code-Skill-6C4DF4?style=flat-square)](https://docs.claude.com/en/docs/claude-code/skills)
[![ASR](https://img.shields.io/badge/ASR-通义听悟-FF6A00?style=flat-square)](https://tingwu.aliyun.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](./LICENSE)

</div>

---

## ✨ 这个 Skill 能做什么

| 能力 | 说明 |
|------|------|
| 🎧 **录音转写** | 上传音频到 OSS，调用 **通义听悟** 离线转写，自带说话人分离（`说话人1/2/3`），转写完自动删除临时音频 |
| 📑 **PPT 提取** | 从会议用的 `.pptx` 提取文字要点，作为纪要的补充材料（不替代转写稿） |
| ✍️ **正式纪要** | 按「售前交流记录表 / 研讨会」两套模板，把口语逐字稿提炼成结构化、正式口吻的中文纪要 |
| 🔍 **质量复核** | 自动生成 `review-notes.md`，标出可疑的姓名/单位/专业词、说话人映射、需人工回听的时间段 |
| 📄 **导出 Word** | 一键渲染成仿宋、1.5 倍行距、首行缩进的 `.docx`，直接可交付 |

> 设计哲学：**通义听悟负责听准，大模型负责写好。** 转写稿是权威事实来源，模型不臆造姓名、预算、承诺和产品能力，所有不确定项都落到 `review-notes.md` 供人工复核。

---

## 🔄 工作流程

```
   🎧 音频 ──┐
            │   ┌──────────────────┐    ┌──────────────────┐
   📊 PPT ──┼──▶│  1. 通义听悟转写   │──▶ │  transcript.md   │
            │   │     (说话人分离)   │    │  + 质量评估       │
   📝 背景 ──┘   └──────────────────┘    └────────┬─────────┘
                                                  │
                 ┌──────────────────┐    ┌────────▼─────────┐
                 │  3. 导出 Word     │◀── │  2. 起草中文纪要  │
                 │   (仿宋/正式版式)  │    │   + review-notes │
                 └────────┬─────────┘    └──────────────────┘
                          │
                          ▼
                 📄 meeting-minutes.docx
```

每次运行的产物都落在 `outputs/meeting-minutes-YYYYMMDD-HHMMSS/`：

```
outputs/meeting-minutes-20260623-101530/
├── transcript.md          # 带时间戳和说话人的原始转写稿
├── ppt-notes.md           # （可选）PPT 要点
├── meeting-minutes.md     # 正式纪要（Markdown）
├── meeting-minutes.docx   # 正式纪要（Word，可交付）
└── review-notes.md        # 人工复核指引
```

---

## 📦 安装

将整个目录放到你的 Claude Code / Codex skills 目录下：

```bash
# Claude Code
git clone https://github.com/Jiale077/meeting-minutes-skill.git \
  ~/.claude/skills/meeting-minutes

# 或 Codex
git clone https://github.com/Jiale077/meeting-minutes-skill.git \
  ~/.codex/skills/meeting-minutes
```

安装 Python 依赖：

```bash
python -m pip install -r scripts/requirements.txt
```

---

## 🔑 配置

转写依赖 **阿里云 OSS + 通义听悟**。复制示例配置并填入你自己的密钥：

```bash
cp meeting-minutes.env.example ~/.codex/meeting-minutes.env
# 然后编辑 ~/.codex/meeting-minutes.env 填入真实值
```

需要的密钥：

| 变量 | 说明 |
|------|------|
| `ALIBABA_CLOUD_ACCESS_KEY_ID` / `_SECRET` | 阿里云 AccessKey |
| `TINGWU_APPKEY` | 通义听悟应用 AppKey |
| `OSS_BUCKET` / `OSS_ENDPOINT` / `OSS_REGION` | 音频临时上传用的 OSS 桶 |
| `TINGWU_ENDPOINT` | 可选，默认 `tingwu.<region>.aliyuncs.com` |

> ⚠️ **密钥安全**：配置文件放在 skills 目录**之外**（`~/.codex/`），仓库里只有 `*.env.example` 占位文件。`.gitignore` 已屏蔽所有 `*.env`，请勿把填好真实值的文件提交上来。

---

## 🚀 使用

在 Claude Code / Codex 里直接对它说，例如：

> 用 meeting-minutes 把这段录音 `~/Desktop/会议.m4a` 整理成纪要，客户是 XX 公司，我方是售前团队，主题是某方案交流。

它会自动按流程跑：转写 → （可选）PPT 提取 → 起草纪要 → 复核标注 → 导出 Word。

也可以单独调用脚本：

```bash
# 仅转写
python scripts/tingwu_transcribe.py "~/Desktop/会议.m4a"

# 提取 PPT 要点
python scripts/extract_ppt_notes.py "deck.pptx" --output "outputs/ppt-notes.md"

# Markdown 渲染成 Word
python scripts/render_docx.py "meeting-minutes.md" "meeting-minutes.docx"
```

---

## 🗂️ 项目结构

```
meeting-minutes/
├── SKILL.md                    # Skill 定义：输入 / 流程 / 起草规则
├── agents/openai.yaml          # Codex 注册元信息
├── references/templates.md     # 纪要模板与自检清单
└── scripts/
    ├── tingwu_transcribe.py    # OSS 上传 + 通义听悟离线转写
    ├── extract_ppt_notes.py    # PPTX 文字提取
    ├── render_docx.py          # Markdown → 正式 Word
    └── requirements.txt        # Python 依赖
```

---

## 📐 模板与风格

内置两套模板（见 [`references/templates.md`](references/templates.md)）：

- **售前交流记录表**（默认）：基础信息 → 我方汇报 → 客户需求探讨 → 双方技术解答 → 后续行动计划
- **研讨会 / 专家会 / 专题会议**（长版）：会议背景 → 参会人员 → 主要内容 → 形成共识 → 后续建议 → 会议结论

模板里的行业关注点和产品关键词都是**占位示例**，请按你自己的团队和行业替换。

---

## ❓ 常见问题

**Q: 提示 `AudioDurationQuotaLimit`？**
A: 通义听悟账户的音频转写额度不足，需在阿里云控制台补充。

**Q: 流程中断了，OSS 上还留着音频？**
A: 脚本会打印保留的 OSS object 路径，按提示手动清理即可（正常完成会自动删除）。

**Q: 能直接让模型"听"音频复核吗？**
A: 不能。纪要起草是基于文本的，转写稿是权威来源；可疑片段会带时间戳写进 `review-notes.md`，由人工回听核对。

---

## 📄 License

[MIT](./LICENSE) © 2026 Jiale077
