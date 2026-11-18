# 🧰 Codex 工作起步器 · Codex Work Starter

> 把邮件、日历、会议、表格、文档、学习、网页这些日常活，变成**安全、可检查、可复用**的 Codex 流程——先跑通一个真实任务，再谈自动化。
> Turn everyday email, calendar, meeting, spreadsheet, document, study, and web work into **safe, checkable, reusable** Codex workflows — prove one real task first, then automate.

**中文** · [English](README.en.md)

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skill-Standard-8B5CF6?style=for-the-badge)](#-快速开始)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)](#-快速开始)
[![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)](#-快速开始)

一个开源 **Agent Skill**，给不写代码的人一条上手 Codex 做真实工作的安全路线：写自定义指令、只连必要的应用、按「一个项目一件大事」组织长线程、搭幕僚（chief-of-staff）工作流。核心是**先手动跑通一个真实任务、确认没跑偏，再把它变成可复用流程**——不是一上来就全自动。兼容 Claude Code、Codex。

## 📋 目录

[✨ 亮点](#-亮点) · [🎯 它解决什么](#-它解决什么) · [⚔️ 和「直接让 Codex 全自动」比](#️-和直接让-codex-全自动比) · [🚀 快速开始](#-快速开始) · [🧭 工作流](#-工作流) · [🔒 安全边界](#-安全边界) · [🌟 关于作者](#-关于作者--fanko-ai-范式)

---

## ✨ 亮点

- **📝 先写自定义指令**：把你的角色、偏好语言、要多直白、格式和隐私边界写清楚，Codex 才知道按谁的规矩办事。
- **🔌 只连必要的应用**：任务需要什么才连什么，不给它无谓的权限面。
- **🗂 一项目一件大事**：一个项目管一个大责任，一个长线程跟一件持续的事；跨应用的活单开一个幕僚线程。
- **✋ 危险动作必停**：读取、整理、起草可以在授权范围内进行；**发送、退订、邀请、删除、发布、购买、改权限一律停下等你确认**，除非你明确授权了这个具体动作。
- **🔐 隐私不外泄**：保留有用的来源链接，去掉不必要的敏感细节；报告和录屏里绝不出现密码、身份证号、支付信息或密钥。
- **✅ 先手动、再复用、最后才定时**：跑通 → 复用为提示词/skill → 才变成定时任务，顺序不能反。

---

## 🎯 它解决什么

你想用 Codex 处理日常工作，但要么不知道从哪下手，要么一上来就让它「全自动收发邮件、改日历」——结果它替你发了不该发的、删了不该删的，事后才发现。

Codex 工作起步器做三件事：**① 立规矩**（自定义指令 + 只连必要应用 + 项目/线程组织）→ **② 先手动跑通一个真实任务**（查覆盖、纠语气、堵隐私漏）→ **③ 确认稳了才复用、才定时**。它给的是一条「敢放手」的安全路线，不是一个替你乱按按钮的机器人。

---

## ⚔️ 和「直接让 Codex 全自动」比

| | 直接让 Codex 全自动 | 全手动自己干 | 🧰 Codex 工作起步器 |
|---|---|---|---|
| **危险动作** | 可能自己发/删/买 | 安全但累 | 读/整理/起草可做，发/删/买必停等确认 |
| **上手** | 容易翻车 | 无从下手 | 先跑通一个真实任务再扩 |
| **隐私** | 易把敏感信息写进报告 | 靠自觉 | 强制去敏，密钥/身份证/支付不外泄 |
| **自动化** | 一步到位、难排错 | 没自动化 | 手动→复用→定时，可检查可回溯 |

---

## 🚀 快速开始

**作为 Agent Skill 用**：把 `codex-work-starter` 文件夹复制进你的 Agent skills 目录——

```bash
# Claude Code
cp -R codex-work-starter ~/.claude/skills/
# Codex
cp -R codex-work-starter ~/.codex/skills/
```

然后对 Claude Code / Codex 说任一句即可触发：

```
我不会写代码，想用 Codex 干活   帮我整理邮件和会议   搭个幕僚工作流   先手动跑通再自动化   清一下这个表格
```

完整执行规则见 [codex-work-starter/SKILL.md](codex-work-starter/SKILL.md)，完整提示词库见 [codex-work-starter/references/prompts.md](codex-work-starter/references/prompts.md)。

---

## 🧭 工作流

1. 写一段简短的自定义指令：你的角色、偏好语言、直白程度、格式、隐私边界。
2. 只连当前任务需要的应用。
3. 一个项目管一个大责任，一个长线程跟一件持续的事。
4. 跨应用的活单开一个幕僚线程。
5. 手动跑一遍提示词 → 检查来源覆盖和结果 → 纠正语气/遗漏/隐私泄露 → 把成功方法存成提示词或 skill → **确认稳了才变成定时任务**。

每个任务都报：读了什么、改了什么、没动什么、结果怎么核的、还有哪个重要动作在等你确认。

---

## 🔒 安全边界

- 读取、整理、起草可在授权范围内进行。
- **发送、退订、邀请、删除、发布、购买、改权限必须停下等人工确认**，除非你明确授权了那个具体动作。
- 保留有用的来源链接，去掉不必要的敏感细节。
- 报告或录屏里**绝不暴露密码、身份证号、支付数据或密钥**。

---

## 🌟 关于作者 · Fanko AI 范式

这个工具来自 **Fanko AI 范式**——我（fanko）会亲手跑一遍 AI 方法，把真实过程、踩坑、提示词和 Skill 整理出来。每一期视频，都在公众号留下**可以直接复用的资料**。

关注公众号「**Fanko AI 范式**」，第一时间拿到每期的实操资料、提示词与开源工具更新：

<p align="center">
  <img src="docs/wechat-qr.jpg" width="200" alt="Fanko AI 范式 · 微信公众号"><br>
  <sub>微信扫码关注 · <b>Fanko AI 范式</b></sub>
</p>

如果这个 Skill 帮到了你，点个 ⭐ **Star** 就是最大的鼓励；有问题或想法，欢迎提 [Issue](../../issues)。

---

## 📄 License

MIT © 2026 fanko
