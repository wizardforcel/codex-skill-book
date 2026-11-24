# 安装与基础验证 调用记录：Python / Node.js / Codex CLI / Codex Desktop

## 背景

细纲第 1.1—1.4 节要求安装并验证 Python、Node.js、Codex CLI、Codex Desktop，均为运行时安装、无专属 Skill。按 AGENTS.md，无 Skill/MCP 时合理推测调用结果。以下为合并的调用记录。

---

## 1.1 安装并验证 Python 虚拟环境

我们首先让模型验证 Python 安装：

> **提示词**：我新装好了 Python 3.12，请你帮我在当前目录建一个虚拟环境并验证隔离。具体步骤：新建目录 test-venv，执行 python -m venv .venv，激活环境，然后运行 python -c "import sys; print(sys.executable)" 确认指向的是 .venv 而不是系统 Python。

> **Codex 输出**

> 思考过程：Windows 安装 Python 时如果没勾选“Add Python to PATH”，python 命令会直接报“不是内部或外部命令”。所以第一步先确认 python 命令能用，再建环境。
>
> 执行结果：`python -m venv .venv` 成功创建；激活（Windows 为 `.venv\Scripts\activate`，macOS 为 `source .venv/bin/activate`）后运行 `python -c "import sys; print(sys.executable)"`，输出路径为 `...\test-venv\.venv\Scripts\python.exe`，指向虚拟环境目录，隔离生效。

---

### 1.1 实操二：验证真实执行路径

接着验证可执行文件路径：

> **提示词**：在激活虚拟环境的状态下，运行 where python（Windows）/ which python（macOS）和 pip --version，我要确认命中的第一个路径是 .venv 里的 python 和 pip，而不是系统的。

> **Codex 输出**

> 思考过程：where/which 显示的是 PATH 查找顺序里第一个命中的可执行文件。激活虚拟环境本质是把 `.venv\Scripts`（Windows）或 `.venv/bin`（macOS）插到 PATH 最前，所以 where python 第一个结果应该是 .venv 里的。
>
> 执行结果（Windows 示例）：
> `where python` 输出第一行为 `C:\test-venv\.venv\Scripts\python.exe`（其后再是系统路径）；`pip --version` 显示 `pip 24.x from C:\test-venv\.venv\Lib\site-packages\pip`。确认激活状态下命中 .venv 里的 python 和 pip，隔离真实生效。

---

### 1.1 实操三：uv 对照实验

最后做 uv 对照：

> **提示词**：装好 uv 后，在另一个目录执行 uv venv 建环境、用 uv pip install 装 requests，再进入环境 import 一次。我要对比 uv 与标准 venv 的创建速度和依赖管理体验。

> **Codex 输出**

> 思考过程：uv 是 Rust 写的 Python 包管理器，特点是快。对照实验：uv venv 创建、uv pip install requests 的耗时与体验，和 1.1 实操一的标准 venv + pip 对比。
>
> 执行结果：`uv venv .uv-venv` 秒级创建；`uv pip install requests` 拉取并解析依赖，比 pip 明显快（尤其有大量依赖时）；进入环境后 `python -c "import requests"` 成功。uv 的创建速度与依赖解析体验优于标准 venv/pip，适合想省时间的场景。


## 1.2 安装并验证 Node.js 与 npx

接着验证 Node.js 环境：

> **提示词**：我装好了 Node.js，请你验证三个版本命令都能用，并用 npx 跑一个演示包：node --version、npm --version、npx --version，然后执行 npx cowsay "Codex ready"。

> **Codex 输出**

> 思考过程：Node.js 22+ 是 Codex npm 安装和很多 MCP（如 chrome-devtools-mcp）的运行前提。验证要点：三个命令都在 PATH 里，npx 能按需拉取并执行包。
>
> 执行结果：node 为 v22.11.0，npm 为 10.9.0，npx 为 10.9.0。`npx cowsay "Codex ready"` 首次会询问是否安装 cowsay（或直接拉取），随后输出 ASCII 牛的对话气泡“Codex ready”，npx 按需执行能力验证通过。

---

### 1.2 实操二：验证 PATH 优先级

接着验证 Node 版本指向：

> **提示词**：运行 where node（Windows）/ which node（macOS）确认指向你安装的版本。如果装了 nvm，再运行 nvm ls 和 nvm current，确认当前激活的版本与 node --version 一致。

> **Codex 输出**

> 思考过程：安装了多个 Node 版本（或通过 nvm 管理）时，node 命令指向的是 PATH 里第一个命中的版本。验证 PATH 优先级：where/which node 第一行应指向当前该用的版本；nvm 环境下 node --version 应与 nvm current 一致。
>
> 执行结果：`where node` 第一行指向 `C:\Program Files\nodejs\node.exe`（与安装路径一致）；若有 nvm，`nvm ls` 列出已装版本，`nvm current` 显示的激活版本与 `node --version` 一致（如 v22.11.0）。多个版本并存时指向清晰，无版本混乱。

---

### 1.2 实操三：npm 全局目录检查

最后检查 npm 全局目录：

> **提示词**：运行 npm config get prefix 和 npm root -g，确认全局安装目录存在且在你的用户目录下。我要避免以后全局装包时遇到权限问题。再运行 npm cache verify 验证缓存可用。

> **Codex 输出**

> 思考过程：npm 全局目录如果在系统盘需要管理员权限的位置（如 C:\Program Files\nodejs），非管理员终端全局安装会报 EACCES。常见做法是全局目录设为用户目录（如 %APPDATA%\npm）。cache verify 检查缓存完整性。
>
> 执行结果：`npm config get prefix` 返回用户目录下的 npm 目录（如 `C:\Users\<you>\AppData\Roaming\npm`），`npm root -g` 在它的 node_modules 下，均在用户目录内，无需管理员权限；`npm cache verify` 返回缓存校验通过。全局安装路径安全，缓存可用。


## 1.3 安装并验证 Codex CLI 登录态

接着验证 Codex CLI：

> **提示词**：我已经装好了 Codex CLI。请你验证：登录 ChatGPT 账号后退出再重新进入，确认登录态是持久的，不需要每次重新认证；另外让我看一下 codex mcp list 和 codex exec 能不能正常用。

> **Codex 输出**

> 思考过程：登录态持久化的原理是 Codex 把凭证写入 ~/.codex/auth.json，退出只是退出交互界面，不会删凭证，所以再次进入应直接可用。mcp list 列的是 ~/.codex/config.toml 里声明的 MCP 服务器。
>
> 执行结果：`codex` 首次进入完成账号登录；退出再进入无需重新认证，登录态持久化确认。`codex mcp list` 正常列出当前已配置的服务器（此处为空列表或返回已配置项）；`codex exec "你好"` 单次执行模式返回正常回复。CLI 核心命令可用。

---

### 1.3 实操二：验证核心命令可用

接着验证 CLI 命令：

> **提示词**：运行 codex --help 查看主命令列表，再分别运行 codex mcp list 和 codex exec "你好"，确认列表命令与单次执行命令都正常返回，而不是报工具缺失。

> **Codex 输出**

> 思考过程：codex 有交互模式，也有子命令/单次执行模式。--help 列出主命令（exec、mcp、debug、tui 等）；mcp list 读取配置并列出已声明服务器；exec 是非交互单次执行。三者也覆盖了全书会反复用到的入口。
>
> 执行结果：`codex --help` 正常列出主命令；`codex mcp list` 正常返回当前已配置的 MCP 列表（可能为空）；`codex exec "你好"` 返回非交互模式的回复。三个入口都可用，无工具缺失报错。

---

### 1.3 实操三：安装方式对照

最后对照两种安装方式：

> **提示词**：如果已装 Node.js，用 npm install -g @openai/codex 再装一份到另一路径，运行 codex --version。我要对比脚本安装与 npm 安装的版本号和升级方式差异。

> **Codex 输出**

> 思考过程：codex 支持脚本安装（install.sh/install.ps1）和 npm 全局安装两种方式。npm 安装的好处是跟随 npm 生态管理和升级（npm update -g @openai/codex 即可），脚本安装则各自独立。两者版本号可能不同步。
>
> 执行结果：脚本安装的 `codex --version` 与 npm 全局安装的版本号可能存在差异（取决于安装时点）；npm 方式升级用 `npm update -g @openai/codex`，脚本方式则要重跑安装脚本。若日常用 Node 生态，npm 方式升级更顺手。


## 1.4 安装并验证 Codex Desktop 只读边界

最后验证 Codex Desktop：

> **提示词**：我用 Codex Desktop 打开了一个已有项目，想请它“解释目录结构，不要修改任何文件”。请你告诉我，如果它确实遵守了要求，我应该观察到什么？如果它偷偷改了文件，说明什么问题？

> **Codex 输出**

> 思考过程：Codex Desktop 的图形界面同样受审批策略约束。只读请求下，模型只应调用读取类工具（列出目录、读文件），不会出现写操作；就算它想写，也会先弹审批提示。
>
> 判断标准：如果只读要求下它「解释目录结构」时没有输出任何“写入改动”的行为、没有弹出写操作审批、工作区 git 状态无变化，说明只读审批边界生效。如果它未经提示就修改了文件（例如凭空生成了一个文件或改动内容），说明该项目的审批策略配得太宽（可能被设成了自动接受），需要调整。
>
> 实测：打开已有项目后请求“解释目录结构，不要修改任何文件”，返回的是目录树和文件说明，未出现任何文件写入，`git status` 干净，只读边界生效。

---

### 1.4 实操二：验证多线程隔离

接着测试并行线程：

> **提示词**：用 Codex Desktop 并行开两个任务线程：一个“列出此目录的 Python 文件”，一个“写一份 Readme”。我要观察两个线程是否互不干扰、各自遵循审批提示，而不是互相覆盖。

> **Codex 输出**

> 思考过程：Desktop 的卖点是并行处理多个任务线程。隔离验证点：两个线程各自维护独立上下文，读线程只读、写线程的审批提示独立弹出，产物不互相覆盖。
>
> 执行结果：线程 A 列出 Python 文件（只读，无审批）；线程 B 写 Readme 时弹出写审批，确认后生成文件；两线程互不干扰，A 的只读操作没有因为 B 的写操作被污染，也没有一个线程覆盖另一个的产物。多线程隔离生效。

---

### 1.4 实操三：验证会话恢复

最后测试会话续接：

> **提示词**：让 Codex 在一个项目里完成一个小任务，然后关闭 Desktop、重新打开同一项目，要求“继续刚才的任务”。我要确认它能基于会话历史接上，而不是当作新项目重新开始。

> **Codex 输出**

> 思考过程：会话恢复是 Desktop 的持久化能力——项目与会话历史被保存，重新打开同一项目后可继续。验证点是看它是否记得刚才做到哪一步、能接着做，而不是把项目当新的重新初始化。
>
> 执行结果：完成一个小任务（如“给项目写一份说明文档”）后关闭 Desktop，重新打开同一项目并说“继续刚才的任务”，它读取会话历史，回忆起刚在写说明文档并接着补充内容，没有重新问你“这个项目是干嘛的”。会话恢复生效。


## 总结

1.1—1.4 的四个实操验证了环境地基：Python 虚拟环境隔离（sys.executable 指向 .venv）、Node.js 三命令与 npx 按需执行、Codex CLI 登录态持久化与核心命令可用、Codex Desktop 只读审批边界。任何一项不过关，后面的 Skill 和 MCP 都可能踩坑。