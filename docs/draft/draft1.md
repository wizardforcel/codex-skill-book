# 第1章 安装与简介

这一章的目标很简单：把第一章后面所有章节都要用到的基本环境装好，理解 Codex 里两个最常见的概念——Skill 和 MCP。你不必理解很深，只需要按顺序完成每一步，并且知道每个命令是干什么的。学完这一章，你会拥有一个可以运行 Codex、可以安装技能、可以连接浏览器工具的电脑环境。先别急着一次装完全部，把每一项的命令和输出对上号，后面每一章都会用到这份基础；装错了也只是重来一遍，不丢面子。

## 1.1 安装 Python

### 简介

Python 是一种编程语言，也是大量 MCP 和 Skill 脚本层的运行前提。很多技能并不是“用魔法在工作”，而是先调用一个 Python 脚本做确定性的计算，再把结果交给模型去判断。因此，电脑上有一个能用的 Python 非常重要。装好 Python 只是第一步，后面大部分社区脚本和 Skill 都要靠它才能跑；安装时就把版本和 PATH 确认清楚，后面会少踩很多坑。

官方建议安装 Python 3.12 或更高版本。Windows 安装时务必勾选“Add Python to PATH”，否则后面你在终端里输入 `python`，电脑会告诉你找不到命令。如果你希望每个项目都有独立环境，可以再安装 `uv`，用 `uv venv` 建隔离环境，用 `uv pip install` 安装包，不与系统 Python 互相干扰。

### 调用记录

**我**：我不知道电脑里有没有 Python，怎么检查？

**Codex**：先直接问版本，电脑会自己回答：

```powershell
python --version
# Python 3.10.11

py --version
# Python 3.14.6
```

本机默认的 `python` 是 3.10.11，Windows 自带启动器 `py` 默认指向 3.14.6。如果你安装的是 3.12 以上，这里会直接看到对应版本号。出现版本号，就说明 Python 已经能用了。

**我**：`python` 和 `py` 为什么不一样？我该信谁？

**Codex**：这两个不是同一个程序。`python` 是你安装的那个 Python，`py` 是 Windows 的 Python 启动器，它可能管理着好几个 Python 版本。让电脑自己报出真实位置，就能看清：

```powershell
python -c "import sys; print(sys.executable)"
# D:\Python310\python.exe

py -0p
#  -V:3.14t *       D:\Python314\python3.14t.exe
#  -V:3.14          D:\Python314\python.exe
#  -V:3.10          D:\Python310\python.exe
```

`sys.executable` 的意思是“当前正在运行的这个 Python 文件在哪里”。这台机器上，`python` 指向 `D:\Python310\python.exe`，而 `py` 会优先选 3.14。初学者最容易踩的坑，就是以为 `python` 和 `py` 是完全一样的东西。

**我**：平常我也装了很多软件，怎么才能不让 Python 弄乱系统？

**Codex**：给每个项目单独建一个“小 Python”环境，也就是 `venv`。它会把 Python 和后来安装的包放进项目自己的文件夹里，不会碰系统 Python。建好后，直接用这个环境里的 `python.exe` 运行，不需要先激活：

```powershell
python -m venv D:\codex-python-verify

D:\codex-python-verify\Scripts\python.exe --version
# Python 3.10.11

D:\codex-python-verify\Scripts\python.exe -c "import sys; print(sys.executable)"
# D:\codex-python-verify\Scripts\python.exe
```

看到最后一行指向 `D:\codex-python-verify\Scripts\python.exe`，就说明这个项目已经开始使用自己的 Python，而不是系统里的 `D:\Python310\python.exe` 了。

**我**：如果检查 `uv` 呢？

**Codex**：

```powershell
uv --version
# uv 0.13.6 (329bf9448 2026-10-26 x86_64-pc-windows-msvc)
```

有版本号就说明 `uv` 能用。后面章节如果需要临时运行某个 Python 工具，又不希望永久安装，`uvx` 就是很顺手的选择。

**我**：创建 `venv` 时出现“Actual environment location may have moved due to redirects, links or junctions”是什么意思？

**Codex**：这是 Windows 临时目录用了 `ADMINI~1` 这种短路径名造成的。解决办法很简单：不要选在 `%TEMP%` 里建项目环境，换成 `D:\codex-python-verify` 这样的普通长路径。把路径写正常，提示就消失了。

**我**：这一步有没有什么容易被忽略的细节？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。先别怀疑工具本身，多数情况是环境、路径或前置条件没对上。

把这一节放回整条链路里看，它只是其中一段；真正动手时不必追求一次全对，先把命令跑通、把输出对上，遇到报错再回来查对应位置，往往比从头读一遍更快。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- `python --version` 能返回版本号，说明 Python 装好了。
- `python` 和 `py` 不是同一个东西，以 `sys.executable` 输出的真实路径为准。
- `venv` 能给项目一个独立环境；直接调用 `Scripts\python.exe` 比先激活脚本更不容易出错。
- `uv` 是可选工具，用来管理环境、安装包和临时运行工具，装好会节省很多折腾。

## 1.2 安装 Node.js

### 简介

Node.js 是一个让 JavaScript 在电脑本地运行的环境。你后面会遇到两件事依赖它：`npm install -g @openai/codex` 这条命令需要 Node.js 22 以上；`chrome-devtools-mcp` 等 MCP 服务器通过 `npx` 启动，也依赖 Node.js。如果只装 Python 不装 Node.js，很多工具还是跑不起来。Node.js 装好后你平时看不见它工作，但几乎所有按需启动的工具都靠它；这一节的重点是确认三个命令都能用，并弄清楚 npx 什么时候会帮你自动下载。

Windows 安装 LTS 版 `.msi` 时，安装向导里有个“Add to PATH”，不要取消。macOS 可以用 `brew install node@24`。需要维护多个 Node 版本时，可以用 `nvm` 管理。

### 调用记录

**我**：怎么知道 Node.js 装好了？

**Codex**：打开新终端，运行三个版本命令：

```powershell
node --version
# v22.19.0

npm --version
# 10.9.3

npx --version
# 10.9.3
```

`node` 是运行 JavaScript 的程序，`npm` 是随 Node.js 一起安装的包管理器，用来下载和管理工具包，`npx` 是 npm 附带的临时运行器。三个都有版本号，说明安装完整。

**我**：npx 到底有什么用？为什么要单独试一下？

**Codex**：很多工具不用先手动安装，npx 会自动从 npm 仓库下载一次再运行。比如运行 `cowsay`：

```powershell
npx --yes cowsay "Codex ready"
#  _____________
# < Codex ready >
#  -------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
```

`--yes` 表示“遇到下载确认提示时自动选择同意”，这样初学者不会卡在交互提示上。能看到那头牛，就说明 npx 能连接 npm 官方仓库，并且能下载、运行工具包。

**我**：为什么第二次运行明显更快？

**Codex**：因为第一次已经把 `cowsay` 下载缓存到本机了。这次只花了几秒，走的是本地缓存，不是重新下载。以后用其他 npx 工具也是这个逻辑。

**我**：怎么确认 npm 使用的是官方仓库？

**Codex**：

```powershell
npm config get registry
# https://registry.npmjs.org/
```

如果公司或学校把 npm 换成内部镜像，这里会显示其他地址。只要命令能正常下载工具，通常不用管它。

**我**：如果第一次没跑通，通常先查哪里？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。把这一步记下来，下次再遇到同类问题时能少走不少弯路。

这些步骤看起来零散，其实前后是有因果的：前一步的产物就是后一步的输入，中间哪一环没对上，后面就会以各种奇怪的方式报错。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- `node`、`npm`、`npx` 三个版本命令都要有输出，安装才算完整。
- npx 负责“临时下载并运行工具”，适合 `chrome-devtools-mcp` 这类按需启动的服务器。
- 第一次运行下载慢是正常的，之后会命中本地缓存。
- Windows 安装时不要取消“Add to PATH”，否则新终端找不到 `node`。

## 1.3 安装 Codex CLI

### 简介

Codex CLI 是全书终端操作的基础。它是 OpenAI 官方命令行工具，安装方式有两种：macOS/Linux 用安装脚本，Windows 用 PowerShell 安装脚本；如果已经在 1.2 节装好 Node.js 22 以上，也可以直接执行 `npm install -g @openai/codex`。装好之后要用 ChatGPT 账号或 API Key 登录，登录状态会保存下来，下次不用重新认证。Codex CLI 是后面所有 Skill 和 MCP 的主入口，值得多花几分钟把安装、登录、自检这三件事一次理顺，后面就不会在工具层面反复卡壳。

### 调用记录

**我**：怎么确认 Codex 已经装好？

**Codex**：

```powershell
codex --version
# codex-cli 0.155.1
```

**我**：怎么确认登录了？

**Codex**：

```powershell
codex login status
# Logged in using an API key - sk-mMY9A***9cPDN
```

这里只显示前几位和后四位，完整的密钥被隐藏了。如果你看到类似“Logged in”的句子，说明身份信息已经保存。

**我**：重启电脑或新开一个终端，登录状态还在吗？

**Codex**：在。Codex 会把登录信息保存到 `C:\Users\Administrator\.codex\auth.json`。用 `codex doctor` 可以做一个全面体检：

```powershell
codex doctor
# Codex Doctor v0.155.1 · windows-x86_64
# ✓ install      consistent
# ✓ auth         auth is configured
#    auth storage mode        File
#    stored API key           true
# ✓ config       config.toml  parse ok
```

看到 `stored API key true`，就说明下次打开终端直接输入 `codex` 就能用，不需要重新输账号密码。

**我**：登录成功就一定能正常对话吗？

**Codex**：不一定。有一次真正提问时，Codex 返回了：

```text
ERROR: unexpected status 503 Service Unavailable
```

原因是当前供应商的模型通道不可用，而不是 Codex 没装好或没登录。遇到这种情况，用 `codex doctor` 确认安装、配置、auth 三项正常，再去管模型供应商。这正是下一节 `CC Switch` 要解决的问题。

**我**：按这个流程做，最容易卡在哪一步？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。遇到时先按本节记录的顺序排查，通常都能定位到具体原因。

如果只记住一句，那就是：先让最小链路真实跑通，再谈优化和自动化；跳过验证直接堆功能，最后往往要花更多时间回头补。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- 安装成功的标志是 `codex --version` 有版本号。
- `codex login status` 能确认登录状态，密钥不会完整显示。
- 登录凭据保存在 `~/.codex/auth.json`，新终端仍然有效。
- `codex doctor` 是排错第一工具；它说“配置正常”但对话仍报 503，问题通常出在模型供应商，不在 Codex 本身。

## 1.4 安装 Codex Desktop

### 简介

Codex Desktop 是 Codex 的图形界面形态。它的好处是适合同时打开多个项目、并行处理多个任务线程，而且项目里的文件、审批、对话记录都看得见。macOS 从官方下载 `.dmg`，Windows 可以通过 `codex app` 自动打开安装器，也可以从 Microsoft Store 或 `winget` 安装。桌面版不是必须品，但对喜欢同时开多个项目、多看几个窗口的人来说，它比光秃秃的命令行直观得多，也更容易判断正在发生什么。

需要特别强调的是“审批边界”：桌面版打开本地文件夹后，并不会默认获得随意修改文件的权限。你第一次要求它做有副作用的事，它会弹审批；如果它未经提示就修改文件，说明审批策略需要调整。

### 调用记录

**我**：这台电脑上 Codex Desktop 装了吗？

**Codex**：我先检查了两处，没有发现桌面版安装记录：

```powershell
Get-AppxPackage *Codex* | Select-Object Name,PackageFullName
# 没有输出，说明不是 Microsoft Store 安装方式

winget search --id "Codex" --source msstore
# 找不到与输入条件匹配的程序包。
```

所以这台电脑目前只有命令行版，没有桌面版。

**我**：那 Windows 上怎么安装桌面版？

**Codex**：Codex CLI 自带一个入口：`codex app`。如果检测到桌面版不存在，它会自动打开安装器下载页面；已安装时则会直接启动桌面程序：

```powershell
codex app --help
# Launch the Desktop app (opens the app installer if missing)
# Usage: codex app [OPTIONS] [PATH]
# Arguments:
#  [PATH]   Workspace path to open in the Desktop app
```

也就是说，你不需要自己到处找安装包，安装好 CLI 后从终端敲 `codex app` 就行。

**我**：我只想让它看看目录，不想让它改文件，怎么验证审批边界？

**Codex**：先看当前策略，`codex doctor` 里有这段：

```text
✓ sandbox      restricted fs + restricted network · approval OnRequest
  approval policy          OnRequest
  filesystem sandbox       restricted
  network sandbox          restricted
```

`OnRequest` 的意思是“遇到需要权限的操作会先问你”。在桌面版里打开一个已有项目，然后对它说：**“解释目录结构，不要修改任何文件”**。如果它认真回答而没有弹修改权限，正常；如果它未经提示就创建或修改文件，说明这台机器的审批策略设置得过松，需要收紧。

**我**：这一步有没有什么容易被忽略的细节？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。先别怀疑工具本身，多数情况是环境、路径或前置条件没对上。

本节记录里保留了失败和阻断，不是为了吓人，而是让你知道正常使用中也会遇到这些情况，遇到了照着排查即可，不必怀疑自己。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- 桌面版不是 CLI 的必需品，但适合多任务并行。
- Windows 上可用 `codex app` 自动获取安装器，也可以用 Microsoft Store。
- 首次打开项目时，先做只读验证，确认它不会擅自修改文件。
- 看到“解释目录结构”也要留意是否弹了写权限；弹了才说明审批生效。

## 1.5 用 CC Switch 切换模型

### 简介

CC Switch 是一个图形化管理工具，用来管理 Codex 和 Claude Code 的模型供应商配置，避免手改 `~/.codex/auth.json` 和 `config.toml`。它内置 DeepSeek、Qwen、Kimi、GLM 等 50 多个供应商预设。你在界面上选择供应商，保存后，CC Switch 会自动更新 Codex 的配置文件；切换模型后重启或重新打开 Codex 对话，新模型就生效。模型供应商这件事平时看不见，可一旦切错，Codex 会在你真正提问时才报错；用 CC Switch 把这些配置统一管起来，相当于给模型切换上了一道保险。

Windows 上可以从 Releases 下载安装包，macOS 可执行 `brew install --cask cc-switch`。如果你已经让 CC Switch 接管 Codex 配置，`config.toml` 里的 `model_provider`、`model`、`base_url` 会指向它的本地代理。

### 调用记录

**我**：怎么知道 CC Switch 在管理 Codex 的配置？

**Codex**：先确认程序在运行，再看 Codex 配置文件。本机 CC Switch 确实在运行：

```powershell
Get-Process cc-switch | Select-Object Path
# C:\Users\Administrator\AppData\Local\Programs\CC Switch\cc-switch.exe
```

配置文件 `C:\Users\Administrator\.codex\config.toml` 的开头是：

```toml
model_provider = "custom"
model = "deepseek-ai/deepseek-v4.1-flash"
model_reasoning_effort = "high"

[model_providers.custom]
name = "custom"
base_url = "http://127.0.0.1:15721/v1"
```

`base_url` 指向 `127.0.0.1:15721`，这是 CC Switch 的本地代理地址。看到这两条，就说明 Codex 不直接连模型网站，而是先经过 CC Switch。

**我**：界面上到哪里看 Codex 的供应商？

**Codex**：打开 CC Switch，找到 Codex 分类。本机当前配置了两个供应商：

```text
ys365          当前使用
OpenAI Official
```

选中“ys365”的那一行，通常就是当前模型供应商。

**我**：切换供应商后，到底改了哪些文件？

**Codex**：仍然只有 Codex 的配置文件。CC Switch 会把 `config.toml` 里的 `model_provider`、`model`、`base_url` 等字段替换成新供应商的值，然后保存。具体字段取决于供应商类型，但你可以用同一条命令核对：打开 `~/.codex/config.toml`，看 `model_provider` 和 `model` 是不是已经变成新选择。切换之前，最好先确认新供应商的 API Key 有效。

**我**：我切换之后问 Codex，为什么还是报 503？

**Codex**：这说明“配置能切换”和“模型通道可用”是两回事。本机 `ys365` 供应商就曾经返回过：

```text
No available channel for model deepseek-ai/deepseek-v4.1-flash
```

意思是这个模型没有可用通道，不是 Codex 坏了。处理顺序是：先在 CC Switch 界面上看供应商 API Key 是否已填、模型名是否存在于该供应商；换一个能用的供应商；保存后重新打开 Codex 对话再试。

**我**：如果第一次没跑通，通常先查哪里？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。把这一步记下来，下次再遇到同类问题时能少走不少弯路。

做完这一节，建议把关键命令和输出随手记在自己的笔记里；下次再遇到同类任务，翻自己的记录通常比重新搜索更快。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- CC Switch 的作用是替你把模型供应商配置写到 `~/.codex/config.toml`。
- 看到 `base_url` 指向本机 `127.0.0.1` 端口，说明 Codex 走了 CC Switch 的本地代理。
- 切换供应商后，模型变化会体现在 `model_provider` 和 `model` 字段里。
- 503 “No available channel” 多半是供应商侧的问题，不是 Codex 的问题。

## 1.6 Skill 的目录结构与触发机制

### 简介

Skill 是给 Codex 的一套“工作说明书”，它不是模型本身自带的能力，而是一个文件夹。Codex 根据用户的话，决定要不要读取这个文件夹里的说明。一个最小的 Skill 包含一个 `SKILL.md` 文件，文件开头是 YAML 格式的 `name` 和 `description`；可选地，还可以有 `scripts/`、`references/`、`assets/` 等目录。技能文件看起来只是几个文本文件，但它们的摆放和组织方式决定了 Codex 什么时候会'想起'它们；把这个机制理解透，后面装再多技能也不会乱。

Skill 的触发是分阶段的：不管哪种任务，Codex 都能先看到 `name` 和 `description`，它们决定“这个技能要不要被考虑”；命中之后，Codex 才读取 `SKILL.md` 正文；只有正文需要时，才会加载 `scripts/`、`references/` 之类的附加资源。这就是“渐进加载”。

本机装有 Codex 自带的 `skill-creator`，它是一个交互式生成 Skill 骨架的工具。下面用它创建一个 `todo-check` 技能，实际看一下目录结构和验证过程。

### 调用记录

**我**：我想做一个技能，读取项目里的 `TODO.md`，列出没做完的事。你能帮我建吗？

**Codex**：好的，我按内置 `skill-creator` 的初始化脚本生成骨架：

```powershell
py C:\Users\Administrator\.codex\skills\.system\skill-creator\scripts\init_skill.py todo-check --path C:\Users\Administrator\AppData\Local\Temp\codex-skillcreate\.agents\skills
# Initializing skill: todo-check
#    Location: C:\Users\Administrator\AppData\Local\Temp\codex-skillcreate\.agents\skills
#    Resources: none (create as needed)
# [OK] Created skill directory: ...\.agents\skills\todo-check
# [OK] Created SKILL.md
# [OK] Created agents/openai.yaml
# [OK] Skill 'todo-check' initialized successfully
```

生成出来的目录只有两个文件，不需要的东西一个都没有。把它放在项目的 `.agents/skills/` 下，Codex 就能从项目里读取它：

```text
todo-check/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

**我**：为什么是这样？不是每个技能都要有脚本吗？

**Codex**：不是。`scripts/`、`references/`、`assets/` 都只在真正需要时才添加。`todo-check` 只需要读一个 Markdown 文件，把规则写在 `SKILL.md` 里就够了，加上脚本反而让技能变重。

**我**：那 `SKILL.md` 最关键的是哪部分？

**Codex**：是文件最开头的 frontmatter，也叫前置信息：

```markdown
---
name: todo-check
description: 只读检查项目根目录的 TODO.md，列出所有未完成的事项（- [ ]）。当用户问“看看我还有什么没做完”“还有什么待办”或类似问题时使用。
---

# Todo Check

只读检查项目根目录的 `TODO.md`，告诉用户还有哪些事没做完。不要修改任何文件。
```

`name` 是技能的唯一名字，`description` 是触发条件。Codex 会拿用户说的话和这段 `description` 匹配：用户说“看看我还有什么没做完”，正好落在 `description` 里写的触发场景上。

**我**：写完怎么验证这个技能文件格式合法？

**Codex**：用 `skill-creator` 自带的校验脚本。第一次运行会遇到两个真实问题：Python 3.10 缺少 `yaml` 模块，以及中文文件被系统编码误读。解决办法是临时提供 `pyyaml` 并加 UTF-8 模式：

```powershell
uvx --with pyyaml python -X utf8 C:\Users\Administrator\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\codex-skillcreate\.agents\skills\todo-check
# Skill is valid!
```

输出 `Skill is valid!` 就说明 `SKILL.md` 的格式可以被 Codex 读取。

**我**：现在让它真的列一下待办，看看技能规则有没有用。

**Codex**：项目里先放一个 `TODO.md`：

```markdown
# 我的待办

- [ ] 给登录页加上“忘记密码”入口
- [x] 修复首页图片加载失败的问题
- [ ] 把数据库连接超时改成 10 秒
- [ ] 给导出功能补一条使用说明
```

按 `SKILL.md` 执行：只收集 `- [ ]` 开头、跳过第二行 `- [x]`，结果如下：

```text
未完成事项：
1. 给登录页加上“忘记密码”入口
2. 把数据库连接超时改成 10 秒
3. 给导出功能补一条使用说明
共 3 条
```

`SKILL.md` 里的“跳过已完成项、按原顺序输出、不要新建文件”这三条规则，都真实地反映在结果里了。

**我**：按这个流程做，最容易卡在哪一步？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。遇到时先按本节记录的顺序排查，通常都能定位到具体原因。

把这一节放回整条链路里看，它只是其中一段；真正动手时不必追求一次全对，先把命令跑通、把输出对上，遇到报错再回来查对应位置，往往比从头读一遍更快。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- Skill 的最小单元是一个带 `SKILL.md` 的文件夹。
- `frontmatter` 的 `name` 决定名字，`description` 决定什么时候被触发。
- `scripts/`、`references/`、`assets/` 是可选资源，命中后才渐进加载。
- 校验技能时如果缺 `yaml`，用 `uvx --with pyyaml` 临时补上；中文乱码用 `-X utf8` 或设置 `PYTHONUTF8=1` 解决。

## 1.7 安装第一个 Skill 并验证隐式触发

### 简介

Codex 内置了 `skill-installer`，它可以从官方技能列表或任意 GitHub 仓库安装技能，不需要你手动克隆目录。第一个要安装的 Skill 是 `create-plan`，它专门在用户要求规划时，把需求整理成一份结构清晰的计划。第一个技能不必复杂，先把'装上、被触发、给出产出'这条最小链路完整跑通；这一关过了，后面再学什么技能都是同一套思路。

这里还要理解什么叫“隐式触发”：不需要输入 `$create-plan` 这种显式命令，只要你自然地说“给我一个计划”，Codex 就有机会根据 `description` 自动匹配到 `create-plan`。本书第4章会正式用它开发软件，所以这一章把它当作贯穿全书的种子技能。下面的记录来自 `create-plan` 的 `SKILL.md` 被加载后的一次真实执行。

### 调用记录

**我**：skill-installer 能列出哪些可安装技能吗？

**Codex**：可以，运行它的列表脚本（本机 `py` 是 3.14，能正常联网；默认 `python` 的 SSL 证书会报错，这里用 `py`）：

```powershell
py C:\Users\Administrator\.codex\skills\.system\skill-installer\scripts\list-skills.py
# 1. aspnet-core
# 2. chatgpt-apps
# 3. cli-creator
# ...
# 39. yeet
```

列表来自 GitHub 上的官方精选目录。不过 `create-plan` 不在这个精选列表里，它在 ComposioHQ 的 `awesome-codex-skills` 仓库中。

**我**：那帮我从那个仓库安装 `create-plan`。

**Codex**：使用 `skill-installer` 的安装脚本，指定仓库、技能路径和分支。这个仓库的默认分支是 `master`，不是 `main`，所以要加 `--ref master`：

```powershell
py C:\Users\Administrator\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo ComposioHQ/awesome-codex-skills --path create-plan --ref master
# Installed create-plan to C:\Users\Administrator\.codex\skills\create-plan
```

之后 `C:\Users\Administrator\.codex\skills\create-plan` 里就有 `SKILL.md` 了。

**我**：那我第一次不加 `--ref master`，为什么失败了？

**Codex**：真实报错是：

```text
fatal: Remote branch main not found in upstream origin
```

外面还可能包着一层 `destination path ... already exists`。这不是你的安装步骤错了，而是脚本默认去克隆 `main` 分支，而 `ComposioHQ/awesome-codex-skills` 仓库用的是 `master`。加上 `--ref master` 就能成功。如果失败后留下临时目录，清掉 `%TEMP%\codex\skill-install-*` 再重试。

**我**：`create-plan` 的 `SKILL.md` 里到底要求什么？

**Codex**：关键要求是这些：

- 保持只读，不写文件，最终计划直接放在回复里。
- 先快速扫描 `README.md`、`docs/` 和相关源码。
- 最多追问 1 到 2 个问题，而且只在“不问就没法负责任地规划”时才问；信息够用就做合理假设。
- 计划必须包含 Scope、Action items、Open questions，Action items 按“发现 → 修改 → 测试 → 收尾”排序。

**我**：那我现在给一个真实项目提需求：给命令行工具 `taskctl` 加一个 `--dry-run` 选项。

**Codex**：它先扫描了 `README.md`、`taskctl.py`、`test_taskctl.py`，发现这是一个用 `argparse` 管理 `add/list/done/clean` 四个子命令的小工具。因为需求信息足够，它没有反反复复追问，只记录了两个假设：`--dry-run` 是全局选项，只作用于会修改 JSON 的 `add/done/clean`，不改变 `list`。然后按模板给出计划：

```markdown
# Plan

为 taskctl 增加 --dry-run，让 add/done/clean 可预览变更而不写 tasks.json；复用现有 argparse/load/save 与命令处理器，补充 CLI/文件不变性测试和帮助文档。

## Scope
- In: taskctl.py 参数与执行路径；README 命令说明；test_taskctl.py 覆盖 add/done/clean 的 dry-run、不变性、退出码和参数解析。
- Out: 数据格式迁移、list 输出语义重做、非 dry-run 行为改变、打包发布。

## Action items
[ ] 明确 --dry-run 的全局位置与帮助文本，并检查现有 --db 参数在子命令前后的调用方式；必要时统一 CLI 参数解析以支持文档示例和现有测试。
[ ] 在 taskctl.py 的修改型命令路径中读取并计算变更，dry-run 时跳过 save，同时保留可区分的预览输出和成功退出码。
[ ] 保证非修改型 list 忽略或合理处理 --dry-run，避免误写文件并保持现有输出。
[ ] 更新 README.md，说明 --dry-run 的适用命令、输出含义、不会修改 tasks.json，以及 --db 示例。
[ ] 为 add/done/clean 增加测试：dry-run 后 JSON 完全不变；正常模式仍写入；done 找不到 ID 仍返回 1；clean 的预览数量准确。
[ ] 验证 argparse 帮助/参数位置、空库和重复运行等边界，运行 pytest，并手工执行 py taskctl.py --help 与各修改型命令的 dry-run。

## Open questions
- 无（按上述假设可直接实施）。
```

注意这里最值得学习的点：它没有一上来就说“我来写代码”，而是先读代码、识别边界、说明假设，再给你一份可以照着执行的计划。

**我**：这一步有没有什么容易被忽略的细节？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。先别怀疑工具本身，多数情况是环境、路径或前置条件没对上。

这些步骤看起来零散，其实前后是有因果的：前一步的产物就是后一步的输入，中间哪一环没对上，后面就会以各种奇怪的方式报错。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- `skill-installer` 能按仓库路径安装 Skill，装好后目录在 `~/.codex/skills` 下。
- `create-plan` 的流程约束是“先扫描、再假设、最后输出计划”。
- 它会先用问题清单覆盖验收条件；信息足够时，最多问 1 到 2 个问题，或者把假设写进 Open questions。
- 种子技能装好后，后续章节里的开发任务都会用到。

## 1.8 MCP 与 Skill 的分工

### 简介

MCP（Model Context Protocol）是“把外部工具连上”的标准协议，Skill 是“决定怎么用”的工作说明书。这句话是全书反复出现的基础认知：MCP 给 Codex 提供原子能力，比如打开浏览器、读文件、执行调试器；Skill 把这些能力组合成固定流程，比如“先启动、再定位、再填写、再校验”。MCP 和 Skill 的分工是全书反复出现的主线，这一节用一个小小的 echo 实例，把'配置被识别'和'真正握手成功'这两种状态的区别讲清楚。

Codex 的 MCP 服务器声明在 `~/.codex/config.toml` 中。使用 `command` 和 `args` 的是 stdio 服务器，也就是 Codex 启动一个本地命令，通过标准输入输出和它通信；使用 `url` 的是远程服务器。本节不引入复杂服务器，而是添加一个最简单的临时配置，让你看清配置长什么样、Codex 是怎么识别的。

### 调用记录

**我**：怎么查看 Codex 当前有哪些 MCP？

**Codex**：

```powershell
codex mcp list
# No MCP servers configured yet. Try `codex mcp add my-tool -- my-command`.
```

一开始是空的，说明还没有连接任何外部工具。

**我**：能不能加一个最简单的看看配置结构？

**Codex**：可以。加一个名叫 `echo` 的 stdio 服务器，它的命令就是 Windows 的 `cmd /c echo hello`。注意在 PowerShell 里执行，不要在 Git Bash 里执行，否则 `/c` 会被转换：

```powershell
codex mcp add echo -- cmd /c echo hello
# Added global MCP server 'echo'.
```

**我**：现在列表里是什么样？

**Codex**：

```powershell
codex mcp list
# Name             Command  Args                        Env  Cwd  Status   Auth
# chrome-devtools  npx      chrome-devtools-mcp@latest  -    -    enabled  Unsupported
# echo             cmd      /c echo hello               -    -    enabled  Unsupported
```

两个服务器状态都是 `enabled`。`chrome-devtools` 是另一节并行安装时加的，现在只关注 `echo`。

**我**：配置到底存在哪里？

**Codex**：在 `C:\Users\Administrator\.codex\config.toml`：

```toml
[mcp_servers.echo]
command = "cmd"
args = ["/c", "echo", "hello"]
```

**我**：这个 echo 算真正连上了吗？

**Codex**：不算。`cmd /c echo hello` 只是一个普通命令，单独运行它只会输出 `hello`，它不会实现 MCP 需要的初始化握手，所以 Codex 只是“能识别并保存这份配置”，并不是“成功连上一个有用的服务器”。这一节的目的就是区分“配置被识别”和“外部工具真正联通”。

**我**：那 Skill 和 MCP 到底怎么分工？

**Codex**：MCP 回答“我能做什么工具”，Skill 回答“这件事按什么顺序做”。例如浏览器 MCP 只负责打开页面、点击、求值、截图；而一个 RPA 技能决定“先打开、再定位搜索框、输入、提交、等结果出现、再读取前三条”。没有 MCP，技能没有手；没有技能，MCP 只是一堆孤立的工具按钮。

**我**：如果第一次没跑通，通常先查哪里？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。把这一步记下来，下次再遇到同类问题时能少走不少弯路。

如果只记住一句，那就是：先让最小链路真实跑通，再谈优化和自动化；跳过验证直接堆功能，最后往往要花更多时间回头补。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- MCP 配置写在 `~/.codex/config.toml`，stdio 用 `command` + `args`，远程用 `url`。
- `codex mcp add` 是添加服务器最可靠的入口。
- 配置显示 `enabled` 不等于服务器协议握手成功；对 echo 这种演示命令，要明确它只是配置验证。
- 记忆口诀：MCP 把外部工具“连上”，Skill 决定“怎么用”。

## 1.9 安装第一个 MCP：Chrome DevTools

### 简介

Chrome DevTools MCP 让 Codex 连接真实浏览器：打开页面、读取 DOM、截图、查看网络请求、跑 Lighthouse 审计。它对你的意义是，以后 Codex 不需要你手动打开浏览器再描述结果，它可以自己打开页面并返回结构化的数据。浏览器 MCP 是从'让 AI 看着网页猜'到'让 AI 直接读网页'的分水岭；这一节装好它，并把第一条链路真实验证一遍。

安装命令只有一个：

```powershell
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

由于它依赖 Node.js，请先完成 1.2 节。安装完成后，`codex mcp list` 里会出现 `chrome-devtools`。下面的实操会真正通过 MCP 打开 `https://example.com` 并读取页面内容。

### 调用记录

**我**：帮我添加 Chrome DevTools MCP。

**Codex**：

```powershell
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
# Added global MCP server 'chrome-devtools'.
```

再用列表确认：

```powershell
codex mcp list
# Name             Command  Args                        Env  Cwd  Status   Auth
# chrome-devtools  npx      chrome-devtools-mcp@latest  -    -    enabled  Unsupported
```

**我**：这个服务器提供哪些能力？

**Codex**：用 MCP 客户端枚举工具，与 Codex 实际会看到的工具列表相同。导航和检查相关的主要有：

```text
new_page        打开一个新页面
navigate_page   跳转到指定 URL
list_pages      列出当前所有标签页
evaluate_script 在页面里运行 JavaScript 并取回结果
take_snapshot   抓取页面可访问性快照
take_screenshot 给页面截图
lighthouse_audit 运行 Lighthouse 审计
list_network_requests 查看网络请求
list_console_messages 查看控制台消息
```

**我**：打开 `https://example.com` 试试。

**Codex**：调用 `new_page`，传入 `url`：

```text
=== CALL new_page url=https://example.com ===
## Pages
1: about:blank
2: Example Domain (https://example.com/) [selected]
```

返回结果里有一行“Example Domain”，这已经说明浏览器真的打开并加载了页面。

**我**：我第一次调用时看到 npx 在下载，这正常吗？

**Codex**：正常。`codex mcp add` 只写入配置，不下载服务器。第一次真正调用工具时，npx 才去拉取：

```text
npm warn exec The following package was not found and will be installed: chrome-devtools-mcp@1.12.0
```

下载完成之后，后面的调用会走本机缓存。

**我**：那页面的 `<h1>` 是什么？

**Codex**：调用 `evaluate_script`，让浏览器执行 `document.title` 和寻找 `h1` 标签的 JavaScript：

```text
=== CALL evaluate_script pageId=2 ===
{"title":"Example Domain","h1":[]}
```

这里有一个真实细节：现在的 `example.com` 网页标题是 “Example Domain”，但页面里并没有 `<h1>` 标签，所以 `h1` 是空数组。网上很多教程会写成“读取到 h1”，那是旧版页面的结果。正确做法是：先读取 `document.title`，或者读取 `document.body.innerText` 的第一段，再把结果和你的预期核对。

**我**：除了读文字，怎么确认页面真的渲染了？

**Codex**：可以同时抓可访问性快照和全页截图。快照中第一行就是结构化结果：

```text
RootWebArea "Example Domain" url="https://example.com/"
  ...
  link "Learn more" url="https://iana.org/help/example-domains"
```

截图命令返回：

```text
Took a screenshot of the full current page.
Saved screenshot to C:\Users\Administrator\AppData\Local\Temp\chrome-devtools-mcp-test\example-domain.png.
```

文件大小为 137420 字节，说明不是空图。

**我**：我另外开了一个客户端，还拿刚才的 `pageId=2` 继续调用，为什么一直报 `No page found`？

**Codex**：因为每次启动一个 MCP 客户端连接，都会启动一个独立的浏览器实例，页 ID 不能跨连接复用。正确做法是在同一个连接里按顺序执行：`new_page → evaluate_script → take_snapshot → take_screenshot`。如果中途必须换连接，先调用 `list_pages` 重新取得新的页 ID。

**我**：`new_page` 返回后马上求值，会不会拿到空结果？

**Codex**：可能。`new_page` 返回时页面不一定加载完成。保险做法是先调用 `wait_for`，等待关键文本出现，再做求值：

```text
wait_for  { pageId: 2, text: ["Example Domain"], visible: true }
```

看到匹配文本出现，说明页面已经进入可操作状态。

**我**：按这个流程做，最容易卡在哪一步？

**Codex**：最常见的是环境问题：命令找不到、版本不对、PATH 没生效，先重开终端再看版本，比反复重装有效。遇到时先按本节记录的顺序排查，通常都能定位到具体原因。

本节记录里保留了失败和阻断，不是为了吓人，而是让你知道正常使用中也会遇到这些情况，遇到了照着排查即可，不必怀疑自己。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- 安装 Chrome DevTools MCP 只需一条 `codex mcp add` 命令，服务器会在第一次调用时才真正下载。
- 它提供的核心工具是 `new_page`、`navigate_page`、`evaluate_script`、`take_snapshot`、`take_screenshot` 和 `wait_for`。
- `evaluate_script` 能返回结构化数据，比读整段网页文本更适合判断页面状态。
- 页 ID 只在同一个 MCP 连接内有效，换连接后要先 `list_pages`。
- 网页结构可能和教程不同：`example.com` 现在有标题但没有 `<h1>`，遇到这种情况要读 `document.title` 或正文文本，而不是照抄旧教程。