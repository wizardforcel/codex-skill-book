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

## 1.2 安装并验证 Node.js 与 npx

接着验证 Node.js 环境：

> **提示词**：我装好了 Node.js，请你验证三个版本命令都能用，并用 npx 跑一个演示包：node --version、npm --version、npx --version，然后执行 npx cowsay "Codex ready"。

> **Codex 输出**

> 思考过程：Node.js 22+ 是 Codex npm 安装和很多 MCP（如 chrome-devtools-mcp）的运行前提。验证要点：三个命令都在 PATH 里，npx 能按需拉取并执行包。
>
> 执行结果：node 为 v22.11.0，npm 为 10.9.0，npx 为 10.9.0。`npx cowsay "Codex ready"` 首次会询问是否安装 cowsay（或直接拉取），随后输出 ASCII 牛的对话气泡“Codex ready”，npx 按需执行能力验证通过。

---

## 1.3 安装并验证 Codex CLI 登录态

接着验证 Codex CLI：

> **提示词**：我已经装好了 Codex CLI。请你验证：登录 ChatGPT 账号后退出再重新进入，确认登录态是持久的，不需要每次重新认证；另外让我看一下 codex mcp list 和 codex exec 能不能正常用。

> **Codex 输出**

> 思考过程：登录态持久化的原理是 Codex 把凭证写入 ~/.codex/auth.json，退出只是退出交互界面，不会删凭证，所以再次进入应直接可用。mcp list 列的是 ~/.codex/config.toml 里声明的 MCP 服务器。
>
> 执行结果：`codex` 首次进入完成账号登录；退出再进入无需重新认证，登录态持久化确认。`codex mcp list` 正常列出当前已配置的服务器（此处为空列表或返回已配置项）；`codex exec "你好"` 单次执行模式返回正常回复。CLI 核心命令可用。

---

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

## 总结

1.1—1.4 的四个实操验证了环境地基：Python 虚拟环境隔离（sys.executable 指向 .venv）、Node.js 三命令与 npx 按需执行、Codex CLI 登录态持久化与核心命令可用、Codex Desktop 只读审批边界。任何一项不过关，后面的 Skill 和 MCP 都可能踩坑。