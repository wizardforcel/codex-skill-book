# build-ppt-from-sources

一个面向 Codex 的中文 Agent Skill：根据用户提供的 Word、PDF、PPT、表格、图片和文本资料，通过逐阶段确认的门禁流程，制作可编辑、可追溯并经过渲染质检的 PowerPoint 演示文稿。

它适合研究汇报、项目汇报、领导汇报和方案汇报，尤其适用于“先确认大纲和页面效果，再交付可编辑 PPT”的场景。

## 核心特点

- 先检查并分类资料，不用常识或网络内容擅自补足关键成果。
- 依次确认大纲、逐页文案和页面预览，避免直接生成成品后大范围返工。
- 页面预览每批最多 5 页，用户确认当前批次后才继续。
- 区分预览图、高清素材和 PPT 原生组件，不把整页扁平化为图片。
- 对数据、成果、系统界面和图片来源保持可追溯，避免虚构。
- 交付前逐页渲染，检查溢出、重叠、裁切、变形和可编辑性。

## 工作流程

```text
资料就绪
  → 大纲已确认
  → 逐页文案已确认
  → 预览图分批确认中
  → 全部预览已确认
  → 高清素材已确认
  → PPT 已制作
  → 质检通过
```

每个箭头都是一个确认门禁。用户修改上游内容时，Skill 会退回对应阶段，并同步更新受影响的后续产物。

## 前置条件

- 支持 Agent Skills 的 ChatGPT 桌面端、Codex CLI 或 Codex IDE 扩展。
- 当前环境可以使用演示文稿制作与渲染能力。
- 需要生成页面预览或高清插图时，当前环境可以使用图片生成能力。
- 用户需要提供支撑汇报内容的源资料；Skill 不会凭空生成关键数据、成果或系统界面。

本 Skill 会在执行时调用演示文稿和图片生成相关技能。不同 Codex 环境的可用能力可能不同，请先确认对应能力已经安装或由系统提供。

## 安装

### 使用 Skill Installer

在 Codex 中输入：

```text
Use $skill-installer to install https://github.com/2233531707/build-ppt-from-sources
```

安装后若没有立即出现在技能列表中，请重启 Codex。

### 手动安装

Codex 会从用户级的 `$HOME/.agents/skills` 目录发现 Skill。macOS、Linux 或 WSL：

```bash
git clone https://github.com/2233531707/build-ppt-from-sources.git \
  "$HOME/.agents/skills/build-ppt-from-sources"
```

Windows PowerShell：

```powershell
git clone https://github.com/2233531707/build-ppt-from-sources.git `
  "$HOME\.agents\skills\build-ppt-from-sources"
```

安装位置与 Skill 结构参考 [Codex 官方 Build skills 文档](https://developers.openai.com/codex/build-skills)。

## 使用

显式调用：

```text
Use $build-ppt-from-sources to create a presentation from my uploaded source files.
```

中文示例：

```text
使用 $build-ppt-from-sources，根据我上传的项目报告、数据表和参考 PPT，
制作一份面向领导汇报的 15 页演示文稿。先给我资料分类和大纲方案，
每个阶段等我确认后再继续。
```

也可以直接描述相匹配的任务，由 Codex 根据 Skill 的 `description` 自动选择它。

## 仓库结构

```text
.
├── SKILL.md                         # 核心工作流与约束
├── agents/
│   └── openai.yaml                 # 显示信息与调用策略
└── references/
    └── workflow-templates.md        # 输出模板与质检清单
```

## 设计边界

本 Skill 负责把“基于资料制作 PPT”变成可审阅、可回退的工作流，不提供固定视觉模板，也不保证在缺少演示文稿或图片生成能力的环境中完成最终文件制作。

它不会：

- 把研究计划改写为已完成的成果；
- 用生成图片伪装真实系统截图、现场照片或数据图表；
- 未经确认跳过大纲、文案、预览或素材门禁；
- 把整张页面预览图直接作为最终 PPT 页面。

## 贡献

欢迎通过 Issue 报告触发不准确、流程缺口或输出模板问题，也欢迎提交 Pull Request。请让改动保持聚焦，并说明用于验证的真实调用示例和预期行为。

## 许可证

本项目使用 [MIT License](LICENSE)。

OpenAI、ChatGPT 和 Codex 是其各自权利人的商标。本项目为社区项目，与 OpenAI 无隶属或官方背书关系。
