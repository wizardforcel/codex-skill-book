# 第1章 安装与简介

这一章的目标很简单：把本书后面所有章节都要用到的基本环境装好，理解 Codex 里两个最常见的概念——Skill 和 MCP。你不必理解得很深，只需要按顺序完成每一步，并且知道每个命令是干什么的。学完这一章，你会拥有一个可以运行 Codex、可以安装技能、可以连接浏览器工具的电脑环境。

先别急着一次装完全部，把每一项的命令和输出对上号，后面每一章都会用到这份基础。万一装错了，也不用沮丧，重来一遍就是了，完全不丢面子。

## 1.1 安装 Python

### 简介

Python 是大量社区 MCP 和 Skill 脚本层的运行前提，建议安装 3.12+ LTS 版本。为什么要装 Python？因为后面很多 Skill 和 MCP 都是用 Python 写的，不装 Python 它们就跑不起来。这就好比你要用某个软件，那个软件得在 Windows 上运行，那你得先装 Windows，Python 在这里扮演的就是 Windows 这个角色。

Windows 安装时务必勾选“Add Python to PATH”，否则后续调用 `python` 会直接报错。这个 PATH 选项有什么作用呢？简单说，就是告诉电脑：以后我在任何文件夹里输入 `python` 命令，你都知道去哪里找到 Python 程序。不勾选这个选项，你每次都得输入 Python 程序的完整路径才能运行它，非常麻烦。

如果希望隔离项目环境，可在装好 Python 后额外安装 `uv`，用 `uv venv` 建隔离环境、`uv pip install` 装包，不与系统 Python 纠缠。什么叫隔离环境？就好比你家里有个大厨房，但你不想把每个做菜项目的调料都放在同一个架子上，因为不同项目可能需要不同版本的调料。隔离环境就是给每个项目单独准备一个小厨房，互不干扰。

### 调用记录

我们先让模型演示怎么创建隔离环境并确认 Python 路径：

> **提示词**：新建一个目录，用 python -m venv .venv 创建虚拟环境，激活后运行 python -c "import sys; print(sys.executable)"，确认输出路径指向该目录下的 .venv，而不是系统 Python。

> **Codex 输出**
>
> 思考过程：用户要验证虚拟环境是否正确创建，需要检查激活后的 Python 可执行文件路径是否指向 .venv 目录，而不是系统自带的 Python。
>
> Codex：先在当前目录新建一个文件夹，然后进入这个文件夹，用 python -m venv .venv 创建虚拟环境。创建完成后，激活虚拟环境，再运行检查命令：
>
> ```powershell
> mkdir test-python
> cd test-python
> python -m venv .venv
> .venv\Scripts\Activate.ps1
> python -c "import sys; print(sys.executable)"
> ```
>
> 如果输出类似 `D:\test-python\.venv\Scripts\python.exe`，说明路径指向了 .venv 目录，虚拟环境创建成功。如果输出是 `C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe` 这样的系统路径，说明激活失败，还是在用系统 Python。

### 总结

- Python 是本书后面所有 Skill 和 MCP 的运行基础，建议安装 3.12+ LTS 版本。
- Windows 安装时务必勾选“Add Python to PATH”，否则 `python` 命令直接报错。
- 用 `python -m venv .venv` 创建隔离环境，激活后运行 `python -c "import sys; print(sys.executable)"` 确认路径指向 `.venv` 目录，而不是系统 Python。
- 隔离环境能让不同项目使用不同的 Python 版本和依赖包，互不干扰。

---

## 1.2 安装 Node.js

### 简介

`npm install -g @openai/codex` 需要 Node.js 22+，`chrome-devtools-mcp` 等 MCP 通过 `npx` 启动，也依赖 Node.js。Node.js 是什么？简单说，它是一个让 JavaScript 可以在浏览器之外运行的环境。很多开发者工具都是用 JavaScript 写的，不装 Node.js 这些工具就没法运行。

Windows 安装 LTS `.msi` 时不要取消“Add to PATH”；macOS 可用 `brew install node@24`。LTS 版本是指长期支持版本，比较稳定，适合一般用户使用。Add to PATH 的作用和 Python 一样，是为了让你在任何地方都能输入 `node`、`npm`、`npx` 命令。

如果需要在同一台机器维护多个 Node 版本，可以用 `nvm` 管理。`nvm` 是 Node Version Manager 的缩写，好比 Python 里的 `pyenv` 或 `uv`，可以让你在不同项目之间切换不同的 Node.js 版本，不用卸载重装。

### 调用记录

我们先让模型演示怎么验证 Node.js 安装是否成功：

> **提示词**：重新打开终端，运行 node --version、npm --version、npx --version；再运行 npx cowsay "Codex ready"，验证 npx 的按需执行能力。

> **Codex 输出**
>
> 思考过程：用户要验证 Node.js 和 npm 是否正确安装，以及 npx 是否能按需下载并运行包。需要给出真实的命令输出示例。
>
> Codex：重新打开终端（这一步很重要，因为 PATH 环境变量是在安装完成后才生效的，旧终端窗口可能还不知道新安装的 Node.js），依次运行以下命令：
>
> ```powershell
> node --version
> npm --version
> npx --version
> npx cowsay "Codex ready"
> ```
>
> 如果安装成功，前三条命令会分别输出版本号，比如 `v22.12.0`、`10.9.0`、`10.9.0`。第四条 `npx cowsay "Codex ready"` 会下载 cowsay 包并运行，输出一个会说话的牛的 ASCII 艺术图案。如果第四条报错说找不到 cowsay，说明 npx 无法正常下载包，可能是网络问题或 npm 配置问题。

### 总结

- Node.js 22+ 是运行 Codex 和各种 MCP 的基础环境。
- Windows 安装 LTS `.msi` 时不要取消“Add to PATH”，macOS 可用 `brew install node@24`。
- 重新打开终端后，运行 `node --version`、`npm --version`、`npx --version` 验证安装成功。
- 用 `npx cowsay "Codex ready"` 验证 `npx` 的按需执行能力，能下载并运行包说明环境正常。

---

## 1.3 安装 Codex CLI

### 简介

Codex CLI 是全书终端操作的基础。macOS/Linux 用 `curl -fsSL https://chatgpt.com/codex/install.sh | sh`，Windows 用 `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`；如果已经在 1.2 中装好 Node.js 22+，也可以直接用 `npm install -g @openai/codex`。

Codex CLI 是什么？它是一个命令行工具，让你在终端里直接和 AI 对话，而不需要打开浏览器。全书后面的很多操作都是在终端里完成的，Codex CLI 就是那个终端入口。

### 调用记录

我们先让模型演示怎么登录并验证登录态持久化：

> **提示词**：codex 登录 ChatGPT 账号，退出后重新进入，确认登录态已持久化，而不是每次都要重新认证。

> **Codex 输出**
>
> 思考过程：用户要验证 Codex CLI 的登录态是否持久化，需要先登录，然后退出再重新进入，看是否还需要重新登录。
>
> Codex：先用以下命令安装 Codex CLI（如果已经通过 npm 安装过，跳过这一步）：
>
> ```powershell
> powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
> ```
>
> 安装完成后运行 `codex` 登录 ChatGPT 账号。登录过程中会打开浏览器让你授权，授权完成后终端会显示登录成功。然后退出 Codex（输入 `exit` 或按 Ctrl+D），再重新进入 `codex`。如果重新进入后不需要再次登录，直接能看到对话界面，说明登录态已持久化。
>
> 如果每次进 `codex` 都要重新登录，可能是登录信息没有正确保存，检查 `~/.codex/auth.json` 文件是否存在且有内容。

### 总结

- Codex CLI 是全书终端操作的基础工具。
- Windows 用 PowerShell 安装命令，已经装好 Node.js 也可用 `npm install -g @openai/codex`。
- 登录 ChatGPT 账号后，退出再重新进入，确认不需要重新认证，说明登录态已持久化。

---

## 1.4 安装 Codex Desktop

### 简介

Codex Desktop 是 Codex 的图形界面形态，适合并行处理多个任务线程。macOS 从官方下载 `.dmg`，Windows 通过 Microsoft Store 或 `winget install Codex -s msstore` 安装。登录后打开本地文件夹即可开始。

Codex CLI 是命令行界面，Codex Desktop 则是图形界面，适合不太习惯命令行的用户，或者需要同时处理多个任务的场景。两者可以同时安装，根据自己的喜好选择使用。

### 调用记录

我们先让模型演示怎么验证只读审批边界：

> **提示词**：打开一个已有项目，要求 Codex“解释目录结构，不要修改任何文件”，验证只读审批边界生效。如果它未经提示就修改了文件，说明审批策略需要调整。

> **Codex 输出**
>
> 思考过程：用户要验证 Codex Desktop 的只读审批边界，需要打开一个项目，要求 Codex 只解释目录结构而不修改文件，观察它是否会擅自修改文件。
>
> Codex：打开 Codex Desktop，登录后选择一个已有项目文件夹。然后在对话框中输入：
>
> ```
> 请解释这个项目的目录结构，不要修改任何文件。
> ```
>
> 观察 Codex 的回复。它应该只列出目录结构，解释每个文件夹和文件的用途，而不应该修改、创建或删除任何文件。如果 Codex 未经提示就修改了文件（比如自动添加了某个配置文件、修改了某个代码文件），说明审批策略需要调整，应该在 Codex Desktop 的设置里找到“审批”或“权限”相关选项，把默认行为改为“询问后再执行”或“只读模式”。

### 总结

- Codex Desktop 是 Codex 的图形界面，适合并行处理多个任务线程。
- Windows 通过 Microsoft Store 或 `winget install Codex -s msstore` 安装，macOS 从官方下载 `.dmg`。
- 登录后打开本地文件夹即可开始使用。
- 用“解释目录结构，不要修改任何文件”测试只读审批边界，确认 Codex 不会擅自修改文件。

---

## 1.5 用 CC Switch 切换模型

### 简介

CC Switch 图形化管理 Codex / Claude Code 的供应商配置，避免手改 `~/.codex/auth.json` 和 `config.toml`。内置 DeepSeek、Qwen、Kimi、GLM 等 50 多个供应商预设。Windows 从 Releases 下载 `.msi`，macOS 可 `brew install --cask cc-switch`。

什么叫供应商配置？就是告诉 Codex 你要用哪个 AI 模型服务。默认可能是 OpenAI 的模型，但你也可以切换到 DeepSeek、Qwen 等其他供应商。不手改配置文件是为了避免配置错误导致无法连接，CC Switch 提供图形界面让你安全地切换。

### 调用记录

我们先让模型演示怎么添加供应商并验证切换：

> **提示词**：添加 DeepSeek 供应商，保存后启动 Codex 测试；切换到另一供应商，重启后再测，确认两次模型不同，且 config.toml 中的 model_provider 被自动更新。

> **Codex 输出**
>
> 思考过程：用户要验证 CC Switch 能否正确添加供应商、切换模型，以及配置文件是否自动更新。
>
> Codex：打开 CC Switch 应用程序，点击“添加供应商”，选择 DeepSeek，填入 API Key 等必要信息，保存。然后启动 Codex，发送一条测试消息，观察回复是否来自 DeepSeek 模型。
>
> 接着在 CC Switch 里切换到另一供应商（比如 Qwen），保存后重启 Codex，再发送同样的测试消息。如果两次回复的风格明显不同，说明模型已成功切换。
>
> 最后检查 `~/.codex/config.toml` 文件，找到 `model_provider` 字段，确认它的值已自动更新为当前选中的供应商。如果 `model_provider` 没变，说明配置没有正确写入，需要手动检查 CC Switch 的设置。

### 总结

- CC Switch 图形化管理 Codex / Claude Code 的供应商配置，避免手改配置文件。
- 内置 DeepSeek、Qwen、Kimi、GLM 等 50 多个供应商预设。
- Windows 从 Releases 下载 `.msi`，macOS 可 `brew install --cask cc-switch`。
- 添加供应商后，重启 Codex 测试，确认模型已切换且 `config.toml` 中的 `model_provider` 被自动更新。

---

## 1.6 Skill 的目录结构与触发机制

### 简介

`skill-creator` 交互式生成最小 Skill 骨架，拆开 `SKILL.md` 的 frontmatter 和可选目录，理解 `name` 与 `description` 如何决定触发，`scripts/` 和 `references/` 在命中后才被加载。

Skill 是什么？简单说，Skill 就是给 Codex 安装的“插件”或“技能”，让它在特定场景下能做特定的事情。比如有一个 Skill 专门写小说，有一个 Skill 专门做数据分析。Skill 的目录结构决定了它什么时候会被触发，怎么工作。

`SKILL.md` 是 Skill 的说明文件，里面的 frontmatter 是 YAML 格式的元数据，包含 `name`、`description` 等字段。`name` 决定 Skill 的名字，`description` 决定什么样的用户输入会触发这个 Skill。`scripts/` 目录存放 Skill 实际运行的脚本，`references/` 目录存放参考资料，这两个目录只有在 Skill 被触发后才会被加载。

### 调用记录

我们先让模型创建一个 todo-check Skill：

> **提示词**：让 $skill-creator 创建 todo-check（读取 TODO.md 并列出未完成项），复制到 .agents/skills/，用“看看我还有什么没做完”测试隐式触发是否生效。

> **Codex 输出**
>
> 思考过程：我需要先理解 skill-creator 的输出结构。skill-creator 是 Codex 内置的 Skill 创建工具，它会生成包含 SKILL.md frontmatter 和可选 scripts/ 目录的最小 Skill 骨架。key 字段包括 name、description、scripts、references 等。description 决定隐式触发时的匹配优先级，需要收紧到一句能被“看看我还有什么没做完”命中的话。
>
> todo-check 的核心逻辑是：读取 TODO.md → 解析 Markdown 复选框 → 筛选未完成项（- [ ] 或 - [ ] 后跟内容）→ 输出列表。需要处理不同格式的复选框（- [ ]、- [x]、* [ ] 等），也要容错（没有 TODO.md 文件的情况）。
>
> 生成 SKILL.md 时，name 设为 todo-check，description 收紧为“读取项目根目录下的 TODO.md，列出所有未完成的任务项”，这样“看看我还有什么没做完”才能隐式命中。scripts/ 目录放一个简单的 Python 脚本，实现读取和解析逻辑。
>
> ### SKILL.md
>
> ---
> name: todo-check
> description: 读取项目根目录下的 TODO.md，列出所有未完成的任务项
> metadata:
>   type: utility
> ---
>
> ### todo-check
>
> 读取 `TODO.md` 并列出其中未完成的任务项。
>
> #### 触发方式
>
> - 隐式触发：输入“看看我还有什么没做完”“还有哪些任务没做”等类似表述
> - 显式调用：`$todo-check`
>
> ### scripts/todo_check.py
>
> ```python
> #!/usr/bin/env python3
> """读取 TODO.md 并列出未完成的任务项。"""
>
> import re
> from pathlib import Path
>
>
> def find_uncompleted(todo_path: Path = Path("TODO.md")) -> list[str]:
>     """解析 TODO.md，返回未完成任务列表。"""
>     if not todo_path.exists():
>         return ["未找到 TODO.md 文件，请先在项目根目录创建。"]
>
>     uncompleted = []
>     checkbox_pattern = re.compile(r"^\s*[-*+]\s+\[(\s|x)\]:\s*(.+)$", re.IGNORECASE)
>     simple_pattern = re.compile(r"^\s*[-*+]\s+\[(\s|x)\]\s+(.+)$", re.IGNORECASE)
>
>     for line in todo_path.read_text(encoding="utf-8").splitlines():
>         stripped = line.strip()
>         match = checkbox_pattern.match(stripped) or simple_pattern.match(stripped)
>         if match:
>             checked = match.group(1).strip().lower() == "x"
>             content = match.group(2).strip()
>             if not checked:
>                 uncompleted.append(content)
>
>     return uncompleted
>
>
> if __name__ == "__main__":
>     items = find_uncompleted()
>     if items and items[0].startswith("未找到"):
>         print(items[0])
>     elif items:
>         print("你还有以下任务未完成：")
>         for i, item in enumerate(items, 1):
>             print(f"{i}. {item}")
>     else:
>         print("恭喜，所有任务都已完成！")
> ```
>
> 接着测试隐式触发：
>
> **提示词**：在项目根目录创建一个 TODO.md，内容如下：
>
> - [ ] 写第一章细纲
> - [x] 安装 Python 环境
> - [ ] 整理 Skill 调用记录
>
> 然后用“看看我还有什么没做完”测试 todo-check 的隐式触发。
>
> 以下是模型输出的测试结果：
>
> 首先检查项目根目录是否有 TODO.md。根据 skill-creator 生成的 todo-check 脚本逻辑，需要解析 Markdown 复选框语法。给定的 TODO.md 中有三项：第一项“- [ ] 写第一章细纲”未完成，第二项“- [x] 安装 Python 环境”已完成，第三项“- [ ] 整理 Skill 调用记录”未完成。
>
> 隐式触发“看看我还有什么没做完”应当命中 todo-check Skill，因为其 description 是“读取项目根目录下的 TODO.md，列出所有未完成的任务项”，与用户意图匹配。
>
> 你还有以下任务未完成：
> 1. 写第一章细纲
> 2. 整理 Skill 调用记录

### 总结

- `skill-creator` 是 Codex 内置的 Skill 创建工具，直接用 `$skill-creator` 调用。
- `SKILL.md` 的 frontmatter 中 `name` 决定 Skill 名字，`description` 决定什么样的输入会触发该 Skill。
- `scripts/` 和 `references/` 在 Skill 被触发后才会被加载。
- 用“看看我还有什么没做完”测试隐式触发，能命中 todo-check 说明触发机制生效。

---

## 1.7 安装第一个 Skill 并验证隐式触发

### 简介

`skill-installer` 可从官方精选列表或任意 GitHub 仓库安装技能；`create-plan` 足够简单，但会在第4章开发软件时正式展开，作为贯穿全书的“种子技能”。

什么叫“种子技能”？就是一个比较简单、基础的 Skill，后面会在更复杂的场景中反复用到。`create-plan` 就是这种 Skill，它帮助你在写代码之前先理清需求，而不是直接开始写。

### 调用记录

我们先让模型对 create-plan 提出需求：

> **提示词**：对 create-plan 说“给命令行工具加一个 --dry-run 选项”，确认它先追问输入输出边界和验收条件，而不是直接写代码。

> **Codex 输出**
>
>create-plan 的工作方式是：在写第一行代码之前，先追问输入输出边界和验收条件，而不是直接生成代码或文件结构。
>
>收到“给命令行工具加一个 --dry-run 选项”后，我不能直接添加 --dry-run 选项，因为需要先明确以下问题：
>
> 1. 输入边界：命令行工具目前接受哪些参数？--dry-run 应该放在什么位置？
> 2. 输出边界：--dry-run 模式下，什么操作会被跳过？什么操作仍会执行？
>3. 验收条件：如何判断 --dry-run 正常工作？（例如：不写入文件、不修改数据库、只打印计划操作）
>4. 交互方式：--dry-run 是布尔开关还是需要额外参数？
>
>在这些问题答复完毕并达成共识之前，我不会直接修改代码或添加 --dry-run 选项。

### 总结

- `skill-installer` 可从官方精选列表或任意 GitHub 仓库安装技能。
- `create-plan` 是“种子技能”，在第 4 章开发软件时会正式展开。
- 对 `create-plan` 提出需求时，它会先追问输入输出边界和验收条件，而不是直接写代码。
- 只有在追问完成并达成共识后，才会生成代码。

---

## 1.8 MCP 与 Skill 的分工

### 简介

Codex 的 MCP 服务器声明在 host-global 的 `~/.codex/config.toml` 中，stdio 服务器用 `command` + `args`，远程服务器用 `url`。本节建立全书反复使用的分工认知：**MCP 把外部工具“连上”，Skill 决定“怎么用”**。

MCP（Model Context Protocol）是什么？简单说，它是一个让 AI 能够连接外部工具的协议。没有 MCP，AI 只能在自己的“脑子”里思考，不能碰外部的文件、数据库、浏览器等。有了 MCP，AI 就可以通过标准的方式连接到这些外部工具。

Skill 和 MCP 的分工很重要：MCP 负责连接，比如把浏览器连上来、把数据库连上来；Skill 负责决定怎么使用这些连接好的工具，比如“先打开网页，再读取 DOM，最后截图”。两者缺一不可，MCP 没有 Skill 就只能连上工具但不知道怎么用，Skill 没有 MCP 就只知道怎么用但连不上工具。

### 调用记录

我们先让模型演示怎么添加一个 echo MCP：

> **提示词**：手工添加一个指向 echo 的 stdio 配置块，重启 Codex 后 codex mcp list 确认它出现在服务器列表中。

> **Codex 输出**
>
> 思考过程：用户要在 ~/.codex/config.toml 中添加一个指向 echo 命令的 stdio MCP 服务器，然后重启 Codex 并验证它出现在服务器列表中。
>
> Codex：在 `~/.codex/config.toml` 中添加以下配置块：
>
> ```toml
> [mcp_servers.echo]
> command = "echo"
> args = ["hello"]
> ```
>
> 保存后重启 Codex，然后运行 `codex mcp list` 命令。如果 `echo` 出现在服务器列表中，说明 MCP 服务器配置成功。如果没有出现，检查配置文件的语法是否正确，路径是否写对，以及 Codex 是否已经重启。
>
> stdio 服务器用 `command` + `args` 指定，这里的 `command` 是 `echo`，`args` 是 `["hello"]`，意思是运行 `echo hello` 命令。

### 总结

- MCP 服务器声明在 `~/.codex/config.toml` 中。
- stdio 服务器用 `command` + `args`，远程服务器用 `url`。
- MCP 负责把外部工具“连上”，Skill 负责决定“怎么用”。
- 手工添加 MCP 配置后，重启 Codex 并用 `codex mcp list` 确认服务器出现在列表中。

---

## 1.9 安装第一个 MCP：Chrome DevTools

### 简介

Chrome DevTools MCP 让 Codex 连接真实浏览器，打开页面、读取 DOM、截图、跑 Lighthouse 审计。安装：`codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest`。

为什么要装 Chrome DevTools MCP？因为后面很多章节都需要用到浏览器自动化，比如打开网页查看内容、截图保存、检查网络请求等。没有这个 MCP，Codex 无法直接控制浏览器，只能让你自己去操作。

### 调用记录

我们先让模型演示怎么用 Chrome DevTools MCP 打开网页并读取标题：

> **提示词**：让 Codex 打开 https://example.com 并读取 <h1>，确认返回 “Example Domain” 之类的结构化结果，而不是让你自己去浏览器里看。

> **Codex 输出**
>
> 思考过程：用户要验证 Chrome DevTools MCP 是否正确安装并能正常工作，需要让 Codex 打开一个网页并读取页面上的 h1 元素。
>
> Codex：先安装 Chrome DevTools MCP：
>
> ```powershell
> codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
> ```
>
> 安装完成后，让 Codex 打开 https://example.com 并读取 <h1>。如果配置正确，Codex 会通过 MCP 连接到 Chrome 浏览器，打开页面，然后读取 <h1> 标签的内容，返回类似 "Example Domain" 的结构化结果。
>
> 如果返回的是错误信息，或者让你自己去浏览器里看，说明 MCP 没有正确连接，需要检查 Chrome 浏览器是否已经启动，以及 MCP 服务器是否正常运行。

### 总结

- Chrome DevTools MCP 让 Codex 连接真实浏览器，打开页面、读取 DOM、截图、跑 Lighthouse 审计。
- 安装命令：`codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest`。
- 用 Codex 打开 https://example.com 并读取 <h1>，确认返回 “Example Domain” 之类的结构化结果。
- 这是本书反复使用的 MCP，后面很多章节都会用到。

---

本章安装和配置的内容看起来不少，但真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- Python 和 Node.js 是后面所有 Skill 和 MCP 的运行基础，安装时务必勾选“Add to PATH”。
- Codex CLI 是终端操作入口，登录后确认登录态持久化。
- `skill-creator` 创建 Skill 骨架，`skill-installer` 安装现成 Skill，`create-plan` 是“种子技能”。
- MCP 把外部工具“连上”，Skill 决定“怎么用”，两者分工明确。
- Chrome DevTools MCP 是第一章安装的第一个 MCP，后面会反复用到。

