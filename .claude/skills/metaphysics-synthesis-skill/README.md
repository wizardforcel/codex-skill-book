# Metaphysics Synthesis Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/Agent%20Skill-Metaphysics%20Synthesis-6f42c1)](SKILL.md)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab)](scripts/)


Metaphysics Synthesis Skill is a portable agent skill for structured divination and symbolic reasoning. It helps AI assistants handle BaZi, Meihua Yishu, Liuyao, Feng Shui, and Tarot questions with a repeatable workflow: choose the right method, check the inputs, give a clear verdict, explain the evidence, define the timing, propose actions, and list verification signals. It is designed for Codex, Claude Code, and any agent environment that can load a folder of instructions, references, and scripts.

This project is not a generic fortune-telling prompt. A generic prompt often collapses every system into the same vague style: a little comfort, a few symbolic words, and no falsifiable path. This skill does the opposite. It keeps each tradition internally coherent before synthesis. BaZi is used for life structure and luck cycles; Meihua Yishu is used for sudden events, omens, and near-term movement; Liuyao is used for concrete outcomes and process questions; Feng Shui is used for space, direction, and environmental support; Tarot is used for relationship dynamics, psychological texture, and decision reflection. When several systems are combined, each system speaks first, and only overlapping signals become the final synthesis.

The skill is decisive but bounded. It can say "this is the dominant reading" when the evidence converges, but it also marks uncertainty. It distinguishes runnable methods, partial readings, and blocked readings. It does not pretend that missing birth data, unclear line order, an unmeasured compass direction, or an undefined Tarot spread can produce a full professional judgment. It also treats medical, legal, investment, disaster, death, and personal-safety questions as cultural reflection only, not professional advice.

## Languages

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [한국어](README.ko-KR.md)
- [日本語](README.ja-JP.md)
- [Français](README.fr-FR.md)
- [Español](README.es-ES.md)

## Why This Skill Exists

AI assistants can imitate metaphysical language easily, but stable divination requires procedure. If the user asks a BaZi question, the assistant must know whether the birth time is solar or lunar, whether the location and timezone matter, whether the hour pillar is reliable, and whether a claim belongs to the natal chart, decade luck, annual trigger, or real-world condition. If the user asks a Meihua Yishu question, the assistant must know the casting source: time, numbers, object, sound, direction, or outer omen. If the user asks a Liuyao question, the assistant must know the line order from bottom to top and whether Najia details can be established. If the user asks Feng Shui, the assistant must start from observable form before jumping to formulas. If the user asks Tarot, the assistant must respect the spread and avoid redrawing until the answer feels pleasant.

This repository turns those rules into a reusable package. The root `SKILL.md` is the routing layer. The `references/` directory holds method-specific rules. The `scripts/` directory contains deterministic helpers for repeated operations, including Meihua structure calculation, reproducible Tarot draws, package validation, and public-release privacy checks. The result is a skill that can be installed into one agent, copied to another, or used manually as a reference workflow.

## Supported Systems

| System | 100-word overview | Main reference |
| --- | --- | --- |
| [BaZi / Four Pillars of Destiny](https://en.wikipedia.org/wiki/Four_Pillars_of_Destiny) | BaZi, also called Four Pillars, reads the year, month, day, and hour of birth as stem-branch pillars. In this skill it is used for long-range structure: temperament, career tendency, wealth rhythm, relationship timing, health tendency, decade luck, and annual triggers. The workflow separates calculable chart facts from interpretation, so the assistant does not invent details when birth data is incomplete. | `references/bazi.md` |
| [Meihua Yishu / I Ching omen reading](https://en.wikipedia.org/wiki/I_Ching) | Meihua Yishu is a practical image-number approach connected with the Book of Changes. It is strongest for near-term movement, sudden questions, timestamps, numbers, outer omens, directions, and symbolic changes. The skill treats the main hexagram, moving line, mutual hexagram, changed hexagram, Ti/Yong relation, and external omen as separate evidence layers. | `references/meihua.md` |
| [Liuyao / Wenwanggua / Najia](https://en.wikipedia.org/wiki/Wenwanggua) | Liuyao reads six lines and their changes for concrete outcomes. It is useful for promotions, contracts, bosses, salary, projects, product traction, relationships with a specific person, and process blockers. The skill requires bottom-to-top line order and marks the reading partial if month/day, Najia, six relatives, six spirits, or 世应 cannot be established. | `references/liuyao.md` |
| [Feng Shui](https://en.wikipedia.org/wiki/Feng_shui) | Feng Shui studies how place, orientation, flow, backing, openings, pressure lines, and symbolic directions affect lived experience. In this skill, form comes first: wall, door, window, aisle, noise, glare, privacy, and movement. Compass formulas are used only when enough data exists. The output focuses on practical adjustments rather than expensive cures. | `references/fengshui.md` |
| [Tarot](https://en.wikipedia.org/wiki/Tarot) | Tarot uses a card spread to explore relationship dynamics, choices, psychological pressure, obstacles, turning points, and symbolic outcomes. The skill defaults to Rider-Waite-Smith style interpretation unless another deck is specified. It reads position, imagery, suits, elements, card interaction, upright/reversed orientation, and the anchor card before giving a verdict. | `references/tarot.md` |

## How The Skill Works

The workflow follows five decisions:

1. Identify the real question. If the prompt mixes unrelated targets, split them.
2. Select the method that fits the question. Life arc goes to BaZi; sudden movement to Meihua; concrete yes/no or process to Liuyao; environment to Feng Shui; psychological dynamics to Tarot.
3. Validate the inputs. Missing data is marked instead of silently filled.
4. Produce method-level judgment before synthesis.
5. Give the final answer with verdict, evidence, timing, action, and verification.

The default answer shape is:

```text
Verdict:
Evidence:
Timing / strength:
Action:
Verification signals:
Low-confidence inferences:
```

For strict single-method readings, the assistant uses:

```text
System used:
Verdict:
Main evidence:
Conflict:
Timing / number:
Action:
Verification:
Confidence tier:
```

## Installation For Different Agents

The repository can be used in any agent that can read local files. Some tools have a dedicated skill directory. Other tools can use a neutral folder and an instruction that points to `SKILL.md`.

### Universal Clone

Use this when you want one copy that any agent can reference:

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis
cd ~/agent-skills/metaphysics-synthesis
python3 scripts/validate_skill.py
```

Then tell your agent:

```text
Use the local skill at ~/agent-skills/metaphysics-synthesis/SKILL.md. Load only the relevant reference file for the requested system.
```

### Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
python3 ~/.codex/skills/metaphysics-synthesis/scripts/validate_skill.py
```

Restart or reload Codex if your environment requires it.

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.claude/skills/metaphysics-synthesis
python3 ~/.claude/skills/metaphysics-synthesis/scripts/validate_skill.py
```

If your Claude environment uses a different skills directory, clone into that directory or create a symbolic link.

### Generic Skill Directory

For any agent with a custom skills folder:

```bash
AGENT_SKILLS_DIR="$HOME/.your-agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git "$AGENT_SKILLS_DIR/metaphysics-synthesis"
python3 "$AGENT_SKILLS_DIR/metaphysics-synthesis/scripts/validate_skill.py"
```

### Symlink From A Shared Copy

Use this if you want one shared repository but several agents:

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis

mkdir -p ~/.codex/skills ~/.claude/skills
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.codex/skills/metaphysics-synthesis
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.claude/skills/metaphysics-synthesis
```

## Usage Examples

### BaZi

```text
Analyze this BaZi chart for career, wealth, marriage, and health tendencies from 2026 to 2036. Separate natal structure, decade luck, annual triggers, high-confidence conclusions, and low-confidence speculation.
```

### Meihua Yishu

```text
Use Meihua Yishu to read whether this product launch can create a visible career breakthrough. The question arose at 2026-06-12 10:36, and the external omen was a manager discussing scheduling in the northwest direction.
```

### Liuyao

```text
Use Liuyao to judge whether this project can become the main evidence for a promotion. The six lines from bottom to top are 5 / 4 / 25 / 12 / 22 / 17. Do not use previous readings.
```

### Feng Shui

```text
Analyze this workstation layout with Feng Shui direction logic. My seat faces southeast, my direct manager sits northwest, a senior leader sits south, and a cross-team manager sits east.
```

### Tarot

```text
Draw a five-card Tarot spread for a career decision. Show the seed, card positions, upright/reversed cards, verdict, action, and verification signs.
```

## Scripts

### Meihua Structure Calculator

The helper calculates structure only. Interpretation remains in the reference workflow.

```bash
python3 scripts/meihua_calc.py time 2026 6 12 10
python3 scripts/meihua_calc.py classic 7 4 27 10
python3 scripts/meihua_calc.py num 22 5 18
```

### Tarot Draw Helper

The Tarot helper creates reproducible symbolic draws. It outputs card names, spread positions, orientation, seed, and timestamp.

```bash
python3 scripts/tarot_draw.py --spread relationship --question "Will this collaboration mature?" --seed 42
python3 scripts/tarot_draw.py --spread five --question "Career decision" --json
```

### Validate The Package

```bash
python3 scripts/validate_skill.py
python3 scripts/privacy_check.py
```

## Repository Structure

```text
metaphysics-synthesis-skill/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── bazi.md
│   ├── fengshui.md
│   ├── liuyao.md
│   ├── meihua.md
│   ├── method-contracts.md
│   ├── router.md
│   ├── output-templates.md
│   ├── examples.md
│   ├── sources.md
│   └── tarot.md
├── scripts/
│   ├── meihua_calc.py
│   ├── tarot_draw.py
│   ├── privacy_check.py
│   └── validate_skill.py
└── README.*.md
```

## Safety And Scope

This repository treats divination as a cultural, reflective, symbolic, and strategic reasoning framework. It should not be used to make deterministic claims about death, disasters, medical outcomes, legal outcomes, investment returns, or personal safety. If a question touches health, law, money, emergency response, or self-harm risk, use qualified professionals and direct evidence first.

## License

MIT License. See [LICENSE](LICENSE).
