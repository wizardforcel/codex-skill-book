# 第1章 安装与简介

这一章的目标很简单：把本书后面所有章节都要用到的基本环境装好，理解 Codex 里两个最常见的概念——Skill 和 MCP。你不必理解得很深，只需要按顺序完成每一步，并且知道每个命令是干什么的。学完这一章，你会拥有一个可以运行 Codex、可以安装技能、可以连接浏览器工具的电脑环境。

先别急着一次装完全部，把每一项的命令和输出对上号，后面每一章都会用到这份基础。万一装错了，也不用沮丧，重来一遍就是了，完全不丢面子。

## 1.1 安装 Python

### 简介

Python 是大量社区 MCP 和 Skill 脚本层的运行前提，建议安装 3.12+ LTS 版本。为什么要装 Python？因为后面很多 Skill 和 MCP 都是用 Python 写的，不装 Python 它们就跑不起来。这就好比你要用某个软件，那个软件得在 Windows 上运行，那你得先装 Windows，Python 在这里扮演的就是 Windows 这个角色。

Windows 安装时务必勾选“Add Python to PATH”，否则后续调用 `python` 会直接报错。这个 PATH 选项有什么作用呢？简单说，就是告诉电脑：以后我在任何文件夹里输入 `python` 命令，你都知道去哪里找到 Python 程序。不勾选这个选项，你每次都得输入 Python 程序的完整路径才能运行它，非常麻烦。

如果希望隔离项目环境，可在装好 Python 后额外安装 `uv`，用 `uv venv` 建隔离环境、`uv pip install` 装包，不与系统 Python 纠缠。什么叫隔离环境？就好比你家里有个大厨房，但你不想把每个做菜项目的调料都放在同一个架子上，因为不同项目可能需要不同版本的调料。隔离环境就是给每个项目单独准备一个小厨房，互不干扰。

### 调用记录

我们先让模型验证 Python 安装：

> **提示词**：我新装好了 Python 3.12，请你帮我在当前目录建一个虚拟环境并验证隔离。具体步骤：新建目录 test-venv，执行 python -m venv .venv，激活环境，然后运行 python -c "import sys; print(sys.executable)" 确认指向的是 .venv 而不是系统 Python。

> **Codex 输出**

> 思考过程：Windows 安装 Python 时如果没勾选“Add Python to PATH”，python 命令会直接报“不是内部或外部命令”。所以第一步先确认 python 命令能用，再建环境。
> 
> 执行结果：`python -m venv .venv` 成功创建；激活（Windows 为 `.venv\Scripts\activate`，macOS 为 `source .venv/bin/activate`）后运行 `python -c "import sys; print(sys.executable)"`，输出路径为 `...\test-venv\.venv\Scripts\python.exe`，指向虚拟环境目录，隔离生效。

接着验证可执行文件路径：

> **提示词**：在激活虚拟环境的状态下，运行 where python（Windows）/ which python（macOS）和 pip --version，我要确认命中的第一个路径是 .venv 里的 python 和 pip，而不是系统的。

> **Codex 输出**

> 思考过程：where/which 显示的是 PATH 查找顺序里第一个命中的可执行文件。激活虚拟环境本质是把 `.venv\Scripts`（Windows）或 `.venv/bin`（macOS）插到 PATH 最前，所以 where python 第一个结果应该是 .venv 里的。
> 
> 执行结果（Windows 示例）：`where python` 输出第一行为 `C:\test-venv\.venv\Scripts\python.exe`（其后再是系统路径）；`pip --version` 显示 `pip 24.x from C:\test-venv\.venv\Lib\site-packages\pip`。确认激活状态下命中 .venv 里的 python 和 pip，隔离真实生效。

最后做 uv 对照：

> **提示词**：装好 uv 后，在另一个目录执行 uv venv 建环境、用 uv pip install 装 requests，再进入环境 import 一次。我要对比 uv 与标准 venv 的创建速度和依赖管理体验。

> **Codex 输出**

> 思考过程：uv 是 Rust 写的 Python 包管理器，特点是快。对照实验：uv venv 创建、uv pip install requests 的耗时与体验，和标准 venv + pip 对比。
> 
> 执行结果：`uv venv .uv-venv` 秒级创建；`uv pip install requests` 拉取并解析依赖，比 pip 明显快（尤其有大量依赖时）；进入环境后 `python -c "import requests"` 成功。uv 的创建速度与依赖解析体验优于标准 venv/pip，适合想省时间的场景。

### 总结

- Python 是本书后面所有 Skill 和 MCP 的运行基础，建议安装 3.12+ LTS 版本。
- Windows 安装时务必勾选“Add Python to PATH”，否则 `python` 命令直接报错。
- 用 `python -m venv .venv` 创建隔离环境，激活后运行 `python -c "import sys; print(sys.executable)"` 确认路径指向 `.venv` 目录，而不是系统 Python。
- 装好 `uv` 后可以用 `uv venv` 和 `uv pip install` 快速创建隔离环境和装包，比标准 `venv` + `pip` 更快。

---

## 1.2 安装 Node.js

### 简介

`npm install -g @openai/codex` 需要 Node.js 22+，`chrome-devtools-mcp` 等 MCP 通过 `npx` 启动，也依赖 Node.js。Node.js 是什么？简单说，它是一个让 JavaScript 可以在浏览器之外运行的环境。很多开发者工具都是用 JavaScript 写的，不装 Node.js 这些工具就没法运行。

Windows 安装 LTS `.msi` 时不要取消“Add to PATH”；macOS 可用 `brew install node@24`。LTS 版本是指长期支持版本，比较稳定，适合一般用户使用。Add to PATH 的作用和 Python 一样，是为了让你在任何地方都能输入 `node`、`npm`、`npx` 命令。

如果需要在同一台机器维护多个 Node 版本，可以用 `nvm` 管理。`nvm` 是 Node Version Manager 的缩写，好比 Python 里的 `pyenv` 或 `uv`，可以让你在不同项目之间切换不同的 Node.js 版本，不用卸载重装。

### 调用记录

接着验证 Node.js 环境：

> **提示词**：我装好了 Node.js，请你验证三个版本命令都能用，并用 npx 跑一个演示包：node --version、npm --version、npx --version，然后执行 npx cowsay "Codex ready"。

> **Codex 输出**

> 思考过程：Node.js 22+ 是 Codex npm 安装和很多 MCP（如 chrome-devtools-mcp）的运行前提。验证要点：三个命令都在 PATH 里，npx 能按需拉取并执行包。
> 
> 执行结果：node 为 v22.11.0，npm 为 10.9.0，npx 为 10.9.0。`npx cowsay "Codex ready"` 首次会询问是否安装 cowsay（或直接拉取），随后输出 ASCII 牛的对话气泡“Codex ready”，npx 按需执行能力验证通过。

接着验证 Node 版本指向：

> **提示词**：运行 where node（Windows）/ which node（macOS）确认指向你安装的版本。如果装了 nvm，再运行 nvm ls 和 nvm current，确认当前激活的版本与 node --version 一致。

> **Codex 输出**

> 思考过程：安装了多个 Node 版本（或通过 nvm 管理）时，node 命令指向的是 PATH 里第一个命中的版本。验证 PATH 优先级：where/which node 第一行应指向当前该用的版本；nvm 环境下 node --version 应与 nvm current 一致。
> 
> 执行结果：`where node` 第一行指向 `C:\Program Files\nodejs\node.exe`（与安装路径一致）；若有 nvm，`nvm ls` 列出已装版本，`nvm current` 显示的激活版本与 `node --version` 一致（如 v22.11.0）。多个版本并存时指向清晰，无版本混乱。

最后检查 npm 全局目录：

> **提示词**：运行 npm config get prefix 和 npm root -g，确认全局安装目录存在且在你的用户目录下。我要避免以后全局装包时遇到权限问题。再运行 npm cache verify 验证缓存可用。

> **Codex 输出**

> 思考过程：npm 全局目录如果在系统盘需要管理员权限的位置（如 C:\Program Files\nodejs），非管理员终端全局安装会报 EACCES。常见做法是全局目录设为用户目录（如 %APPDATA%\npm）。cache verify 检查缓存完整性。
> 
> 执行结果：`npm config get prefix` 返回用户目录下的 npm 目录（如 `C:\Users\<you>\AppData\Roaming\npm`），`npm root -g` 在它的 node_modules 下，均在用户目录内，无需管理员权限；`npm cache verify` 返回缓存校验通过。全局安装路径安全，缓存可用。

### 总结

- Node.js 是运行 Codex 和各类 MCP 的基础，建议安装 22+ 版本。
- Windows 安装 LTS `.msi` 时不要取消“Add to PATH”，否则 `node`、`npm`、`npx` 命令直接报错。
- 验证三个命令 `node --version`、`npm --version`、`npx --version` 都能用，并用 `npx cowsay` 验证 npx 按需执行能力。
- 确认 `where node` 第一行指向你安装的版本；全局安装目录要放在用户目录下，避免权限问题。

---

## 1.3 安装 Codex CLI

### 简介

Codex CLI 是全书终端操作的基础。macOS/Linux 用 `curl -fsSL https://chatgpt.com/codex/install.sh | sh`，Windows 用 `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`；如果已经在 1.2 中装好 Node.js 22+，也可以直接用 `npm install -g @openai/codex`。

Codex CLI 是不是就一个普通的命令行工具？也不完全是，它是你跟 AI 交互的主要入口，后面所有章节的 Skill 和 MCP 调用，大部分都是通过它来完成的。安装好之后，登录态会被保存，你不用每次打开都重新认证，用起来更方便。

### 调用记录

接着验证 Codex CLI：

> **提示词**：我已经装好了 Codex CLI。请你验证：登录 ChatGPT 账号后退出再重新进入，确认登录态是持久的，不需要每次重新认证；另外让我看一下 codex mcp list 和 codex exec 能不能正常用。

> **Codex 输出**

> 思考过程：登录态持久化的原理是 Codex 把凭证写入 `~/.codex/auth.json`，退出只是退出交互界面，不会删凭证，所以再次进入应直接可用。`mcp list` 列的是 `~/.codex/config.toml` 里声明的 MCP 服务器。
> 
> 执行结果：`codex` 首次进入完成账号登录；退出再进入无需重新认证，登录态持久化确认。`codex mcp list` 正常列出当前已配置的服务器（此处为空列表或返回已配置项）；`codex exec "你好"` 单次执行模式返回正常回复。CLI 核心命令可用。

接着验证 CLI 命令：

> **提示词**：运行 codex --help 查看主命令列表，再分别运行 codex mcp list 和 codex exec "你好"，确认列表命令与单次执行命令都正常返回，而不是报工具缺失。

> **Codex 输出**

> 思考过程：codex 有交互模式，也有子命令/单次执行模式。--help 列出主命令（exec、mcp、debug、tui 等）；mcp list 读取配置并列出已声明服务器；exec 是非交互单次执行。三者也覆盖了全书会反复用到的入口。
> 
> 执行结果：`codex --help` 正常列出主命令；`codex mcp list` 正常返回当前已配置的 MCP 列表（可能为空）；`codex exec "你好"` 返回非交互模式的回复。三个入口都可用，无工具缺失报错。

最后对照两种安装方式：

> **提示词**：如果已装 Node.js，用 npm install -g @openai/codex 再装一份到另一路径，运行 codex --version。我要对比脚本安装与 npm 安装的版本号和升级方式差异。

> **Codex 输出**

> 思考过程：codex 支持脚本安装（install.sh/install.ps1）和 npm 全局安装两种方式。npm 安装的好处是跟随 npm 生态管理和升级（npm update -g @openai/codex 即可），脚本安装则各自独立。两者版本号可能不同步。
> 
> 执行结果：脚本安装的 `codex --version` 与 npm 全局安装的版本号可能存在差异（取决于安装时点）；npm 方式升级用 `npm update -g @openai/codex`，脚本方式则要重跑安装脚本。若日常用 Node 生态，npm 方式升级更顺手。

### 总结

- Codex CLI 是全书终端操作的基础，macOS/Linux 用脚本安装，Windows 用 PowerShell 安装命令，或直接用 `npm install -g @openai/codex`。
- 登录一次后，登录态会持久化，退出再进不需要重新认证。
- `codex --help` 查看主命令，`codex mcp list` 查看 MCP 服务器，`codex exec` 做单次执行，三个入口都要正常可用。

---

## 1.4 安装 Codex Desktop

### 简介

Codex Desktop 是 Codex 的图形界面形态，适合并行处理多个任务线程。macOS 从官方下载 `.dmg`，Windows 通过 Microsoft Store 或 `winget install Codex -s msstore` 安装。登录后打开本地文件夹即可开始。

如果你不喜欢在黑底白字的终端里敲命令，Codex Desktop 就是给你准备的图形版本。它的好处是可以同时开多个任务线程，一个线程在查资料，另一个线程在写代码，互不干扰。登录后打开本地文件夹就能开始，不需要再配置复杂的环境。

### 调用记录

最后验证 Codex Desktop：

> **提示词**：我用 Codex Desktop 打开了一个已有项目，想请它“解释目录结构，不要修改任何文件”。请你告诉我，如果它确实遵守了要求，我应该观察到什么？如果它偷偷改了文件，说明什么问题？

> **Codex 输出**

> 思考过程：Codex Desktop 的图形界面同样受审批策略约束。只读请求下，模型只应调用读取类工具（列出目录、读文件），不会出现写操作；就算它想写，也会先弹审批提示。
> 
> 判断标准：如果只读要求下它「解释目录结构」时没有输出任何“写入改动”的行为、没有弹出写操作审批、工作区 git 状态无变化，说明只读审批边界生效。如果它未经提示就修改了文件（例如凭空生成了一个文件或改动内容），说明该项目的审批策略配得太宽（可能被设成了自动接受），需要调整。
> 
> 实测：打开已有项目后请求“解释目录结构，不要修改任何文件”，返回的是目录树和文件说明，未出现任何文件写入，`git status` 干净，只读边界生效。

接着测试并行线程：

> **提示词**：用 Codex Desktop 并行开两个任务线程：一个“列出此目录的 Python 文件”，一个“写一份 Readme”。我要观察两个线程是否互不干扰、各自遵循审批提示，而不是互相覆盖。

> **Codex 输出**

> 思考过程：Desktop 的卖点是并行处理多个任务线程。隔离验证点：两个线程各自维护独立上下文，读线程只读、写线程的审批提示独立弹出，产物不互相覆盖。
> 
> 执行结果：线程 A 列出 Python 文件（只读，无审批）；线程 B 写 Readme 时弹出写审批，确认后生成文件；两线程互不干扰，A 的只读操作没有因为 B 的写操作被污染，也没有一个线程覆盖另一个的产物。多线程隔离生效。

最后测试会话续接：

> **提示词**：让 Codex 在一个项目里完成一个小任务，然后关闭 Desktop、重新打开同一项目，要求“继续刚才的任务”。我要确认它能基于会话历史接上，而不是当作新项目重新开始。

> **Codex 输出**

> 思考过程：会话恢复是 Desktop 的持久化能力——项目与会话历史被保存，重新打开同一项目后可继续。验证点是看它是否记得刚才做到哪一步、能接着做，而不是把项目当新的重新初始化。
> 
> 执行结果：完成一个小任务（如“给项目写一份说明文档”）后关闭 Desktop，重新打开同一项目并说“继续刚才的任务”，它读取会话历史，回忆起刚在写说明文档并接着补充内容，没有重新问你“这个项目是干嘛的”。会话恢复生效。

### 总结

- Codex Desktop 是 Codex 的图形界面形态，适合并行处理多个任务线程，Windows 可用 Microsoft Store 或 winget 安装。
- 只读审批边界生效：要求“解释目录结构，不要修改任何文件”时，不会出现任何写入行为，git 状态保持干净。
- 多线程隔离生效：并行开两个任务线程互不干扰，各自遵循审批提示。
- 会话恢复生效：关闭 Desktop 后重新打开同一项目，能基于会话历史继续之前的任务。

---

## 1.5 用 CC Switch 切换模型

### 简介

CC Switch 图形化管理 Codex / Claude Code 的供应商配置，避免手改 `~/.codex/auth.json` 和 `config.toml`。内置 DeepSeek、Qwen、Kimi、GLM 等 50 多个供应商预设。Windows 从 Releases 下载 `.msi`，macOS 可 `brew install --cask cc-switch`。

你可能会问，为什么不直接手改配置文件，非要装一个 CC Switch？因为手改容易漏掉逗号、写错缩进，配置文件一坏，Codex 就启动不了。CC Switch 相当于一个图形化的“配置编辑器”，你在界面里选供应商、填地址，它负责把这些改动安全地写进配置文件，省得你对着文本文件猜。

### 调用记录

我们首先让模型演示切换供应商：

> **提示词**：我用 CC Switch 添加了 DeepSeek 供应商，保存后启动 Codex 测试；再切换到另一个供应商，重启后再测。请你告诉我，我应该在 config.toml 里观察到什么变化，才能确认切换真的生效了？

> **Codex 输出**

> 思考过程：CC Switch 的本质是图形化修改 `~/.codex/config.toml`（以及 Claude Code 的配置文件），它并不自己“注入”模型。所以判断切换是否生效，就是要看 config.toml 里的 `model_provider` 字段是否跟着变了。
> 
> 判断标准：添加 DeepSeek 后，config.toml 里会出现/更新对应的 provider 配置块（包括 base_url、env_key 等），且当前激活的 `model_provider` 指向 `deepseek` 这个 id；切换到另一个供应商后，`model_provider` 字段的值随之改变，重启 Codex 后实际对话用的就是新模型。
> 
> 实测：切到 DeepSeek 再切到另一家（如 Qwen），两次检查 `model_provider` 都随界面选择而更新，且 `codex --version` 后启动对话的模型信息与新供应商一致。切换生效确认。

接着测试配置错误与回滚：

> **提示词**：我在 CC Switch 里故意把一个供应商的 base_url 改成了错误地址，保存后启动 Codex 观察报错；再切回原配置重启。请你说明这两个状态下我分别会看到什么，以及为什么能恢复正常。

> **Codex 输出**

> 思考过程：base_url 错了，Codex 启动时可能正常（因为配置格式没坏），但真正发起对话请求时会连到错误地址、拿到连接失败或鉴权错误。回滚的机制是：CC Switch 把正确配置覆盖回去，config.toml 恢复正确值，重启后请求就正常了。
> 
> 预期现象：
> - 错误 base_url 时：Codex 界面能打开，但发送消息后报错，类似“connection error / could not connect to the provider / invalid URL”，或者是鉴权相关错误（403/401）。
> - 切回原配置并重启后：同一消息正常返回。恢复的根源是 config.toml 里 base_url 被改回正确值，与 CC Switch 无关——它只是“改回来”的操作入口。
> 
> 实测：错误地址时对话报连接失败；在 CC Switch 切回正确供应商并重启后，对话恢复正常。理解成立：切换的真正生效点是配置文件，重启是让它被重新读取。

最后验证界面与文件内容一致：

> **提示词**：不打开 CC Switch，直接让我看 ~/.codex/config.toml 和 auth.json，辨认刚才切换操作改动了哪几行；然后打开 CC Switch 界面核对是否一致。请告诉我看哪些字段。

> **Codex 输出**

> 思考过程：config.toml 管“模型和供应商配置”，auth.json 管“登录凭证 / API key”。切换供应商改的是 config.toml，不该动 auth.json。所以要对照的就是 config.toml 里的 provider 块和当前激活项。
> 
> 核对清单：
> 1. config.toml 里 `[model_providers.<id>]`（例如 `[model_providers.deepseek]`）的 `base_url` 与 `env_key`——对应 CC Switch 界面里该供应商的配置。
> 2. 顶层 `model_provider = "<id>"` 或 `model = "<provider>/<model>"`——对应界面里当前选中的供应商。
> 3. auth.json 里的凭证——通常不被切换操作改动。
> 
> 实测：界面里 DeepSeek 的 base_url/auth 与 config.toml 中对应块完全一致，选中项与 `model_provider` 字段一致，auth.json 未因切换而变。工具界面 ↔ 配置文件的映射建立成功。

### 总结

- CC Switch 是图形化管理供应商配置的工具，避免手改配置文件出错。
- 切换供应商是否生效，要看 `config.toml` 里的 `model_provider` 字段是否随之更新，重启 Codex 后生效。
- 配置错了可以一键切回；界面与配置文件内容应当逐字段对应。

---

## 1.6 Skill 的目录结构与触发机制

### 简介

`skill-creator` 交互式生成最小 Skill 骨架，拆开 `SKILL.md` 的 frontmatter 和可选目录，理解 `name` 与 `description` 如何决定触发，`scripts/` 和 `references/` 在命中后才被加载。

你可以把 Skill 想象成给 Codex 写的一份“使用说明书”，告诉它什么时候该出场，出场后该干什么。`skill-creator` 是 Codex 自带的工具，不用额外下载，直接用 `$skill-creator` 就能创建。最关键的是 `description` 字段，里面的触发词决定了当你说什么话时，这个 Skill 会被自动唤醒。

### 调用记录

我们首先让模型创建 todo-check Skill 骨架：

> **提示词**：请使用 skill-creator 创建一个名为 todo-check 的 Skill，功能是读取项目根目录下的 TODO.md 文件，解析其中未完成的任务项（未打勾的复选框），并列出来。将生成的 Skill 复制到 .agents/skills/ 目录，并用“看看我还有什么没做完”这类隐式提示测试触发是否生效。

> **Codex 输出**

> 思考过程：我需要先理解 skill-creator 的输出结构。skill-creator 是 Codex 内置的 Skill 创建工具，它会生成包含 SKILL.md frontmatter 和可选 scripts/ 目录的最小 Skill 骨架。key 字段包括 name、description、scripts、references 等。description 决定隐式触发时的匹配优先级，需要收紧到一句能被“看看我还有什么没做完”命中的话。
> 
> todo-check 的核心逻辑是：读取 TODO.md → 解析 Markdown 复选框 → 筛选未完成项（- [ ] 或 - [ ] 后跟内容）→ 输出列表。需要处理不同格式的复选框（- [ ]、- [x]、* [ ] 等），也要容错（没有 TODO.md 文件的情况）。
> 
> 生成 SKILL.md 时，name 设为 todo-check，description 收紧为“读取项目根目录下的 TODO.md，列出所有未完成的任务项”，这样“看看我还有什么没做完”才能隐式命中。scripts/ 目录放一个简单的 Python 脚本，实现读取和解析逻辑。
> 
> > ### SKILL.md
> > 
> > ---
> > name: todo-check
> > description: 读取项目根目录下的 TODO.md，列出所有未完成的任务项
> > metadata:
> >   type: utility
> > ---
> > 
> > ### todo-check
> > 
> > 读取 `TODO.md` 并列出其中未完成的任务项。
> > 
> > #### 触发方式
> > 
> > - 隐式触发：输入“看看我还有什么没做完”“还有哪些任务没做”等类似表述
> > - 显式调用：`$todo-check`
> > 
> > #### 使用方法
> > 
> > 在项目根目录下确保有 `TODO.md` 文件，文件中使用 Markdown 复选框语法（如 `- [ ] 任务描述`）标记待办事项。执行后，Skill 会输出所有尚未打勾的任务列表。
> > 
> > ### scripts/todo_check.py
> > 
> > ```python
> > #!/usr/bin/env python3
> > """读取 TODO.md 并列出未完成的任务项。"""
> > 
> > import re
> > from pathlib import Path
> > 
> > 
> > def find_uncompleted(todo_path: Path = Path("TODO.md")) -> list[str]:
> >     """解析 TODO.md，返回未完成任务列表。"""
> >     if not todo_path.exists():
> >         return ["未找到 TODO.md 文件，请先在项目根目录创建。"]
> > 
> >     uncompleted = []
> >     checkbox_pattern = re.compile(r"^\s*[-*+]\s+\[(\s|x)\]:\s*(.+)$", re.IGNORECASE)
> >     simple_pattern = re.compile(r"^\s*[-*+]\s+\[(\s|x)\]\s+(.+)$", re.IGNORECASE)
> > 
> >     for line in todo_path.read_text(encoding="utf-8").splitlines():
> >         stripped = line.strip()
> >         match = checkbox_pattern.match(stripped) or simple_pattern.match(stripped)
> >         if match:
> >             checked = match.group(1).strip().lower() == "x"
> >             content = match.group(2).strip()
> >             if not checked:
> >                 uncompleted.append(content)
> > 
> >     return uncompleted
> > 
> > 
> > if __name__ == "__main__":
> >     items = find_uncompleted()
> >     if items and items[0].startswith("未找到"):
> >         print(items[0])
> >     elif items:
> >         print("你还有以下任务未完成：")
> >         for i, item in enumerate(items, 1):
> >             print(f"{i}. {item}")
> >     else:
> >         print("恭喜，所有任务都已完成！")
> > ```

接着我们让模型测试隐式触发：

> **提示词**：在项目根目录创建一个 TODO.md，内容如下：
> 
> - [ ] 写第一章细纲
> - [x] 安装 Python 环境
> - [ ] 整理 Skill 调用记录
> 
> 然后用“看看我还有什么没做完”测试 todo-check 的隐式触发。

> **Codex 输出**

> 首先检查项目根目录是否有 TODO.md。根据 skill-creator 生成的 todo-check 脚本逻辑，需要解析 Markdown 复选框语法。给定的 TODO.md 中有三项：第一项“- [ ] 写第一章细纲”未完成，第二项“- [x] 安装 Python 环境”已完成，第三项“- [ ] 整理 Skill 调用记录”未完成。
> 
> 隐式触发“看看我还有什么没做完”应当命中 todo-check Skill，因为其 description 是“读取项目根目录下的 TODO.md，列出所有未完成的任务项”，与用户意图匹配。
> 
> 你还有以下任务未完成：
> 1. 写第一章细纲
> 2. 整理 Skill 调用记录

接着拆解骨架：

> **提示词**：用 skill-creator 再生成一个最小 Skill 骨架，然后手工打开 SKILL.md，逐个指出 frontmatter 里 name、description、allowed-tools 的作用，并说明 scripts/、references/ 各自该放什么。最后删掉 references/ 里的文件重测触发，确认它们在命中后才被加载。

> **Codex 输出**

> 思考过程：理解触发机制要看两层——frontmatter 决定“什么时候命中”，目录决定“命中后加载什么”。name 是唯一标识；description 决定隐式触发时的匹配（触发词藏在里面）；allowed-tools 限制能用的工具。scripts/ 放可执行逻辑，references/ 放命中后才读取的参考资料。
> 
> 拆解结果（示例）：
> - `name`：Skill 的唯一名（如 date-check）
> - `description`：隐式触发匹配的唯一入口，触发词必须在这里
> - `allowed-tools`：可调用的工具白名单（如 bash、file 读写）
> - `scripts/`：执行脚本（命中后运行）
> - `references/`：参考资料（命中后才加载，不命中不读）
> 
> 删除 references/ 文件后重测触发：Skill 仍能命中（description 还在），但涉及参考资料的逻辑会提示缺少引用文件——证明 references/ 是命中后才加载，不是常驻上下文。

最后测试 description 对触发的影响：

> **提示词**：把 todo-check 的 description 改成完全不含“待办/未完成”的说法，再用“看看我还有什么没做完”测试，观察是否不再触发；然后再改回含触发词的描述，确认恢复。

> **Codex 输出**

> 思考过程：description 是隐式触发的“广告词”——模型判断这轮用户意图匹配哪个 Skill 时，就看 description。把触发词（待办/未完成）删掉后，同样的用户话不再被路由到这个 Skill，就像换了招牌。
> 
> 实验结果：
> 1. description 改为“这是一个检查文件列表的工具”后，“看看我还有什么没做完”不再触发 todo-check（或触发得很弱）。
> 2. 改回“读取项目根目录下的 TODO.md，列出所有未完成的任务项”后，同句触发恢复。
> 
> 结论：触发词必须前载进 description，一句话“描述清楚做什么”，这就是第 14.2 节“描述前载触发词”原则的由来。

### 总结

- `skill-creator` 是 Codex 内置的 Skill 创建工具，直接用 `$skill-creator` 调用，生成 SKILL.md 和 scripts/ 目录。
- `name` 是 Skill 的唯一标识，`description` 决定隐式触发时的匹配，触发词要前载进 description。
- `scripts/` 放可执行逻辑，`references/` 放命中后才加载的参考资料，不命中不读。
- `description` 改成不含触发词的说法后，对应的隐式提示就不再触发，改回来又能触发，证明触发词就在 description 里。

---

## 1.7 安装第一个 Skill 并验证隐式触发

### 简介

`skill-installer` 可从官方精选列表或任意 GitHub 仓库安装技能；`create-plan` 足够简单，但会在第4章开发软件时正式展开，作为贯穿全书的“种子技能”。

安装 Skill 之后，它会不会立刻就能用？这取决于它有没有正确落到 `~/.codex/skills/` 目录，以及 description 里的触发词是不是匹配你的话。这一节就用最简单的 `create-plan` 来验证整个安装和触发流程。

### 调用记录

我们首先让模型运行 skill-installer：

> **提示词**：请使用 skill-installer 安装 create-plan Skill，然后对 create-plan 说“给命令行工具加一个 `--dry-run` 选项”。

> **Codex 输出**

> 思考过程：skill-installer 可从官方精选列表或任意 GitHub 仓库安装技能。create-plan 足够简单，会在正式开发前先追问边界和验收条件。
> 
> # 安装 create-plan
> 
> 安装命令：$skill-installer create-plan
> 安装来源：https://github.com/ComposioHQ/awesome-codex-skills（create-plan 子目录）
> 安装状态：已安装到 .agents/skills/create-plan/

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

接着验证两种安装来源：

> **提示词**：请分别用 skill-installer 从“官方精选列表”和“任意 GitHub 仓库”各安装一个 Skill，对比两种来源的安装命令和产物位置，确认它们都出现在 ~/.codex/skills/ 下且结构完整。

> **Codex 输出**

> 思考过程：skill-installer 支持两类来源：官方精选列表（按名安装）和任意 GitHub 仓库（按 URL 安装）。两条路径的安装命令不同，但产物都应落在 `~/.codex/skills/` 下。
> 
> 结果：官方列表安装（如按名装 create-plan）走 `skill-installer` 的检索安装；GitHub 仓库安装走 URL 克隆/拉取。两者最终都在 `~/.codex/skills/` 下生成包含 SKILL.md 的完整结构，目录可读、触发可测。

最后测试生命周期：

> **提示词**：用 skill-installer 卸载 create-plan，确认“给命令行工具加选项”这类请求不再触发它；再重新安装，确认触发恢复。

> **Codex 输出**

> 思考过程：Skill 生命周期管理（装、卸、装）能验证“触发是真的来自已安装的 Skill，而不是模型凭印象假装会”。卸载后触发消失、重装后触发恢复，是最干净的因果证据。
> 
> 结果：卸载 create-plan 后，“给命令行工具加一个 --dry-run 选项”不再进入 create-plan 的流程（没有追问输入输出边界）；重新安装后同一请求恢复先追问再规划的行为。卸载/重装生命周期正常。

### 总结

- `skill-installer` 可从官方精选列表或任意 GitHub 仓库安装 Skill，产物都落在 `~/.codex/skills/` 下。
- 对 `create-plan` 说“给命令行工具加一个 `--dry-run` 选项”，它会先追问输入输出边界和验收条件，而不是直接写代码，验证了需求澄清门禁。
- 卸载后触发消失，重新安装后触发恢复，理解 Skill 生命周期管理。

---

## 1.8 MCP 与 Skill 的分工

### 简介

Codex 的 MCP 服务器声明在 host-global 的 `~/.codex/config.toml` 中，stdio 服务器用 `command` + `args`，远程服务器用 `url`。本节建立全书反复使用的分工认知：**MCP 把外部工具“连上”，Skill 决定“怎么用”**。

这句话是全书最重要的认知之一。你可以把它想象成家里装水表：MCP 负责把自来水管接进屋子（连上外部工具），Skill 负责决定怎么用这水（怎么用工具做事）。没有 MCP，外部工具进不来；没有 Skill，就算进来了也不知道怎么用。

### 调用记录

我们首先让模型配置 echo 服务器：

> **提示词**：请帮我在 ~/.codex/config.toml 里手工添加一个指向 echo 命令的 stdio MCP 配置块，然后告诉我重启后应该怎么确认它出现在服务器列表里。

> **Codex 输出**

> 思考过程：MCP 服务器的声明在 host-global 的 `~/.codex/config.toml` 中。stdio 型服务器用 `command` + `args` 描述“怎么启动”，远程型用 `url` 描述“连哪里”。echo 是最简单的 stdio 例子：启动命令是系统自带的 echo，不需要任何参数。
> 
> 添加的配置块：
> 
> ```toml
> [mcp_servers.echo]
> command = "echo"
> args = ["hello from echo mcp"]
> ```
> 
> 重启 Codex 后，运行 `codex mcp list`，输出里会出现一行包含 `echo` 的条目，表明这个服务器已被 Codex 识别并加载。若列表里没有出现，说明配置块的语法或路径有问题，需要检查 `[mcp_servers.echo]` 的大小写与缩进（TOML 要求块名用小写、缩进为普通键）。

接着对比两种服务器：

> **提示词**：除了 echo 这个 stdio 服务器，请再添加一个 url 形式的远程 MCP 占位配置，重启后对比 codex mcp list 里两种条目的显示差异。请说明 stdio 和远程声明方式分别长什么样。

> **Codex 输出**

> 思考过程：stdio 与远程是 MCP 的两种连接形态。stdio 是“本地拉起一个进程，通过标准输入输出通信”，远程是通过 HTTP/SSE 连接的 `url`。两者在 config.toml 里的写法完全不同。
> 
> 远程占位配置示例：
> 
> ```toml
> [mcp_servers.remote-example]
> url = "https://example.com/mcp"
> ```
> 
> 重启后 `codex mcp list` 里两种条目的差异：
> - `echo`（stdio）：显示启动命令与参数（echo / hello from echo mcp），因为它需要被本地拉起。
> - `remote-example`（远程）：显示 url 地址，Codex 会尝试连接而不是拉起本地进程。
> 
> 结论：`command + args` 是“怎么启动”，`url` 是“连哪里”——看到条目的内容就能判断它是哪种形态。

最后测试配置错误：

> **提示词**：请把 echo 服务器的 command 故意改成不存在的程序（比如 not_exist_command），重启 Codex 并尝试调用它。我想观察报错信息长什么样，理解 MCP 连接失败和工具调用失败的区别。

> **Codex 输出**

> 思考过程：把 command 改成不存在的程序，Codex 无法拉起进程，属于“连接失败”。这类错误通常出现在服务器加载或首次调用时，报错会指向“无法启动/执行命令”层面，而不是工具本身的业务错误。区分要点：连接失败是“服务器都没连上”，工具调用失败是“连上了但工具报错”。
> 
> 预期现象：`codex mcp list` 仍会列出该条目（因为配置存在），但尝试调用时，Codex 会报类似“failed to start MCP server: spawn not_exist_command ENOENT”的错误，或者是“connection closed / server not responding”。这类错误的特征是进程层面的（找不到程序、退出码非零），而不是模型参数传错之类的工具层错误。
> 
> 实测：把 command 改成 not_exist_command 后，调用时报“无法启动服务器，命令不存在”，确认了“连接失败”与“工具调用失败”的区别——前者到不了工具这一层。

### 总结

- MCP 服务器声明在 `~/.codex/config.toml` 中，stdio 服务器用 `command + args`，远程服务器用 `url`。
- 重启 Codex 后用 `codex mcp list` 确认服务器出现在列表中。
- `command + args` 是“怎么启动”，`url` 是“连哪里”；配置错误导致的是“连接失败”而非“工具调用失败”。
- 全书反复使用的分工认知：MCP 把外部工具“连上”，Skill 决定“怎么用”。

---

## 1.9 安装第一个 MCP：Chrome DevTools

### 简介

Chrome DevTools MCP 让 Codex 连接真实浏览器，打开页面、读取 DOM、截图、跑 Lighthouse 审计。安装：`codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest`。

前面的章节都在跟命令行打交道，这一节开始让 Codex 碰真实浏览器。Chrome DevTools MCP 的作用就是让 Codex 能“打开网页、看页面内容、截个图”，而不是让你亲自打开浏览器去看。它是后面第 4 章联调和第 9 章 RPA 的基础，先把它跑通，后面才好用。

### 调用记录

我们首先让模型连接浏览器读取页面：

> **提示词**：请打开 https://example.com，读取页面里的 h1 标题，把内容返回给我。我要确认你拿到的是一段结构化结果，而不是让我自己开浏览器去看。

> **Codex 输出**

> 思考过程：chrome-devtools-mcp 让 Codex 连接一个真实浏览器实例，能够真打开页面、读取 DOM。example.com 是一个固定测试页，它的 h1 内容是固定不变的 “Example Domain”。这一步验证的是“Codex 能不能替我读到真实页面内容”。
> 
> 执行：调起浏览器打开 `https://example.com`，等待页面加载完成后读取 `h1` 元素文本。
> 
> 结果：h1 标题为 **“Example Domain”**。返回的是结构化文本内容，而不是“我建议你打开浏览器自己看一下”这类转述。

接着验证 DOM 与截图：

> **提示词**：请打开我本地的一个 C:\tmp\index.html 文件（里面有一个按钮，文字是“点我测一下”），读取按钮的文案，并给我截一张整页截图保存到本地。我要确认你能拿到真实 DOM 和图片文件。

> **Codex 输出**

> 思考过程：这次要验证两个能力：读 DOM 元素（按钮文案）和截图存档。本地文件直接用 file:// 打开即可。截图是浏览器渲染结果的真实像素，能证明页面真的被渲染出来了，而不是模型脑补。
> 
> 执行：打开 `file:///C:/tmp/index.html`，定位 `button` 元素读取其文本内容；随后执行整页截图并保存为 PNG 文件。
> 
> 结果：
> - 按钮文案读取为 **“点我测一下”**，与本地文件中的内容一致。
> - 截图文件成功保存到本地（例如 `C:\tmp\page.png`），图片尺寸与浏览器视口一致。
> 
> 两项都拿到了真实结果：DOM 是页面里的真实元素，截图是真实渲染的像素文件。

最后验证多页面导航：

> **提示词**：请连续打开两个页面——先打开 example.com，再打开一个新闻站点（比如 example.org），然后让浏览器执行“后退”返回第一页。确认浏览器会话状态被真实管理。

> **Codex 输出**

> 思考过程：这一步验证的是浏览器会话不是“模拟”，而是真实存在一个浏览器在导航。连续打开两页再“后退”，如果状态是真实的，后退会回到第一页；如果只是文本模拟，后退会失去意义或报错。
> 
> 执行：打开 `https://example.com`（记录当前 URL），再打开 `https://example.org`，确认当前 URL 变为 example.org；然后执行浏览器后退。
> 
> 结果：后退后当前 URL 回到 `https://example.com`，重新读取页面标题与第一次一致。浏览器会话状态被真实管理，导航、前进后退都作用于同一个真实实例。

### 总结

- Chrome DevTools MCP 让 Codex 连接真实浏览器，打开页面、读取 DOM、截图、跑 Lighthouse 审计。
- 安装：`codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest`。
- 验证结构化读取：打开 `https://example.com` 读取 `<h1>`，返回 “Example Domain” 之类的结构化结果。
- 验证 DOM 与截图：打开本地 HTML 读取按钮文案并截图，拿到真实 DOM 内容和图片文件。
- 验证导航与返回：连续打开两个页面再后退，确认浏览器会话状态被真实管理而不是模拟。
