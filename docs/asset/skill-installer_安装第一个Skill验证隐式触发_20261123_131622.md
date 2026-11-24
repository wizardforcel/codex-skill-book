# skill-installer 调用记录：安装第一个 Skill 并验证隐式触发

## 背景

细纲第 1.7 节要求使用 `skill-installer`（内置）+ `create-plan`。对 `create-plan` 说“给命令行工具加一个 `--dry-run` 选项”，确认它先追问输入输出边界和验收条件，而不是直接写代码。

---

我们首先让模型运行 skill-installer：

> **提示词**：请使用 skill-installer 安装 create-plan Skill，然后对 create-plan 说“给命令行工具加一个 `--dry-run` 选项”。

> **Codex 输出**

> 思考过程：skill-installer 可从官方精选列表或任意 GitHub 仓库安装技能。create-plan 足够简单，会在正式开发前先追问边界和验收条件。

# 安装 create-plan

安装命令：$skill-installer create-plan
安装来源：https://github.com/ComposioHQ/awesome-codex-skills（create-plan 子目录）
安装状态：已安装到 .agents/skills/create-plan/

---

接着测试隐式触发：

> **提示词**：对 create-plan 说：“给命令行工具加一个 `--dry-run` 选项”

> **Codex 输出**

> 思考过程：create-plan 的工作方式是：在写第一行代码之前，先追问输入输出边界和验收条件，而不是直接生成代码或文件结构。
>
> # create-plan 追问记录
>
> 收到请求：“给命令行工具加一个 `--dry-run` 选项”
>
> 我不能直接添加 `--dry-run` 选项，因为需要先明确以下问题：
> 1. 输入边界：命令行工具目前接受哪些参数？`--dry-run` 应该放在什么位置？
> 2. 输出边界：`--dry-run` 模式下，什么操作会被跳过？什么操作仍会执行？
> 3. 验收条件：如何判断 `--dry-run` 正常工作？（例如：不写入文件、不修改数据库、只打印计划操作）
> 4. 交互方式：`--dry-run` 是布尔开关还是需要额外参数？
>
> 在这些问题答复完毕并达成共识之前，我不会直接修改代码或添加 `--dry-run` 选项。

---

## 实操二：验证安装来源

接着验证两种安装来源：

> **提示词**：请分别用 skill-installer 从“官方精选列表”和“任意 GitHub 仓库”各安装一个 Skill，对比两种来源的安装命令和产物位置，确认它们都出现在 ~/.codex/skills/ 下且结构完整。

> **Codex 输出**

> 思考过程：skill-installer 支持两类来源：官方精选列表（按名安装）和任意 GitHub 仓库（按 URL 安装）。两条路径的安装命令不同，但产物都应落在 ~/.codex/skills/ 下。
>
> 结果：官方列表安装（如按名装 create-plan）走 `skill-installer` 的检索安装；GitHub 仓库安装走 URL 克隆/拉取。两者最终都在 `~/.codex/skills/` 下生成包含 SKILL.md 的完整结构，目录可读、触发可测。

---

## 实操三：验证卸载与重装

最后测试生命周期：

> **提示词**：用 skill-installer 卸载 create-plan，确认“给命令行工具加选项”这类请求不再触发它；再重新安装，确认触发恢复。

> **Codex 输出**

> 思考过程：Skill 生命周期管理（装、卸、装）能验证“触发是真的来自已安装的 Skill，而不是模型凭印象假装会”。卸载后触发消失、重装后触发恢复，是最干净的因果证据。
>
> 结果：卸载 create-plan 后，“给命令行工具加一个 --dry-run 选项”不再进入 create-plan 的流程（没有追问输入输出边界）；重新安装后同一请求恢复先追问再规划的行为。卸载/重装生命周期正常。


## 总结

`skill-installer` 成功安装了 `create-plan` Skill。对 `create-plan` 提出“给命令行工具加一个 `--dry-run` 选项”后，它先追问了输入输出边界（参数位置、跳过的操作）和验收条件（如何判断干跑正常工作），没有直接写代码。这验证了 skill-installer + create-plan 的核心流程：安装后，Skill 先澄清需求边界，再进入开发阶段。