# 🧰 Codex Work Starter

> Turn everyday email, calendar, meeting, spreadsheet, document, study, and web work into **safe, checkable, reusable** Codex workflows — prove one real task first, then automate.

[中文](README.md) · **English**

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skill-Standard-8B5CF6?style=for-the-badge)](#-quick-start)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)](#-quick-start)
[![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)](#-quick-start)

An open-source **Agent Skill** giving non-programmers a safe route to real work with Codex: write custom instructions, connect only the apps you need, organize long threads as "one project, one responsibility," and build a chief-of-staff workflow. The core is to **run one real task manually and confirm it didn't drift before turning it into a reusable flow** — not full autopilot from day one. Works with Claude Code and Codex.

## ✨ Highlights

- **📝 Custom instructions first** — spell out your role, preferred language, candor, formatting, and privacy boundaries so Codex knows whose rules to follow.
- **🔌 Connect only what's needed** — link the apps the task requires, nothing more.
- **🗂 One project, one big thing** — one project per major responsibility, one long thread per continuing task; a separate chief-of-staff thread for cross-app work.
- **✋ Dangerous actions must stop** — reading, organizing, and drafting proceed within scope; **sending, unsubscribing, inviting, deleting, publishing, purchasing, or changing permissions stop for confirmation** unless you explicitly authorized that exact action.
- **🔐 No privacy leaks** — keep useful source links, drop unnecessary sensitive detail; never expose passwords, ID numbers, payment data, or secret keys in a report or recording.
- **✅ Manual → reuse → schedule** — prove it, save it as a prompt/skill, and only then make it a recurring task; never reverse the order.

## 🎯 What it solves

You want Codex handling daily work, but you either don't know where to start, or you jump straight to "auto-send my email, edit my calendar" — and it sends what it shouldn't, deletes what it shouldn't, and you find out after.

This Skill does three things: **① set the rules** (custom instructions + only necessary apps + project/thread structure) → **② prove one real task manually** (check coverage, fix tone, plug privacy leaks) → **③ reuse and schedule only once it's stable**. You get a route you can trust to let go of, not a robot pushing buttons for you.

## 🚀 Quick start

Copy the `codex-work-starter` folder into your Agent skills directory:

```bash
# Claude Code
cp -R codex-work-starter ~/.claude/skills/
# Codex
cp -R codex-work-starter ~/.codex/skills/
```

Then say any of these to Claude Code / Codex:

```
I can't code but want to use Codex for work   organize my email and meetings   build a chief-of-staff workflow   prove it manually before automating   clean up this spreadsheet
```

Full rules: [codex-work-starter/SKILL.md](codex-work-starter/SKILL.md). Complete prompt library: [codex-work-starter/references/prompts.md](codex-work-starter/references/prompts.md).

## 🧭 Workflow

1. Write short custom instructions: role, preferred language, candor, formatting, privacy boundaries.
2. Connect only the apps the current task needs.
3. One project per major responsibility, one long thread per continuing task.
4. A dedicated chief-of-staff thread for cross-app work.
5. Run the prompt manually → check source coverage and result → fix tone/omissions/privacy leaks → save the working method as a prompt or skill → **only then make it recurring**.

Each task reports: what was read, what changed, what was not changed, how the result was checked, and which important action still awaits confirmation.

## 🔒 Safety boundary

- Reading, organizing, and drafting proceed within the authorized scope.
- **Sending, unsubscribing, inviting, deleting, publishing, purchasing, or changing permissions must stop for human confirmation** unless you explicitly authorized that exact action.
- Keep useful source links; remove unnecessary sensitive detail.
- **Never expose passwords, identity numbers, payment data, or secret keys** in a report or recording.

## 🌟 About the author · Fanko AI 范式

This tool comes from **Fanko AI 范式** — I (fanko) run each AI method by hand and publish the real process, the pitfalls, the prompts, and the Skill. Every episode leaves **directly reusable material** on the WeChat account.

<p align="center">
  <img src="docs/wechat-qr.jpg" width="200" alt="Fanko AI 范式 · WeChat"><br>
  <sub>Scan to follow · <b>Fanko AI 范式</b></sub>
</p>

If this Skill helped, a ⭐ **Star** means a lot. Questions or ideas → [Issues](../../issues).

## 📄 License

MIT © 2026 fanko
