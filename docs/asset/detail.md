## 第1章 安装与简介

### 1.1 安装 Python
**Skill**：无（运行时安装）  
**MCP**：无  
**仓库地址**：python.org；`uv` — `https://github.com/astral-sh/uv`  
**介绍**：Python 是大量社区 MCP 和 Skill 脚本层的运行前提，建议安装 3.12+ LTS 版本。Windows 安装时务必勾选“Add Python to PATH”，否则后续调用 `python` 会直接报错。如果希望隔离项目环境，可在装好 Python 后额外安装 `uv`，用 `uv venv` 建隔离环境、`uv pip install` 装包，不与系统 Python 纠缠。  
**小实操**：新建目录，`python -m venv .venv`，激活后运行 `python -c "import sys; print(sys.executable)"`，确认输出路径指向该目录下的 `.venv`，而不是系统 Python。

### 1.2 安装 Node.js
**Skill**：无（运行时安装）  
**MCP**：无  
**仓库地址**：`https://nodejs.org`  
**介绍**：`npm install -g @openai/codex` 需要 Node.js 22+，`chrome-devtools-mcp` 等 MCP 通过 `npx` 启动，也依赖 Node.js。Windows 安装 LTS `.msi` 时不要取消“Add to PATH”；macOS 可用 `brew install node@24`。如果需要在同一台机器维护多个 Node 版本，可以用 `nvm` 管理。  
**小实操**：重新打开终端，运行 `node --version`、`npm --version`、`npx --version`；再运行 `npx cowsay "Codex ready"`，验证 `npx` 的按需执行能力。

### 1.3 安装 Codex CLI
**Skill**：无（CLI 安装）  
**MCP**：无  
**仓库地址**：`https://chatgpt.com/codex`  
**介绍**：Codex CLI 是全书终端操作的基础。macOS/Linux 用 `curl -fsSL https://chatgpt.com/codex/install.sh | sh`，Windows 用 `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`；如果已经在 1.2 中装好 Node.js 22+，也可以直接用 `npm install -g @openai/codex`。  
**小实操**：`codex` 登录 ChatGPT 账号，退出后重新进入，确认登录态已持久化，而不是每次都要重新认证。

### 1.4 安装 Codex Desktop
**Skill**：无（桌面应用安装）  
**MCP**：无  
**仓库地址**：`https://chatgpt.com/codex`  
**介绍**：Codex Desktop 是 Codex 的图形界面形态，适合并行处理多个任务线程。macOS 从官方下载 `.dmg`，Windows 通过 Microsoft Store 或 `winget install Codex -s msstore` 安装。登录后打开本地文件夹即可开始。  
**小实操**：打开一个已有项目，要求 Codex“解释目录结构，不要修改任何文件”，验证只读审批边界生效。如果它未经提示就修改了文件，说明审批策略需要调整。

### 1.5 用 CC Switch 切换模型
**Skill**：无（配置工具）  
**MCP**：无  
**仓库地址**：`https://github.com/farion1231/cc-switch`；fork `https://github.com/kongkongyo/cc-switch`  
**介绍**：CC Switch 图形化管理 Codex / Claude Code 的供应商配置，避免手改 `~/.codex/auth.json` 和 `config.toml`。内置 DeepSeek、Qwen、Kimi、GLM 等 50 多个供应商预设。Windows 从 Releases 下载 `.msi`，macOS 可 `brew install --cask cc-switch`。  
**小实操**：添加 DeepSeek 供应商，保存后启动 Codex 测试；切换到另一供应商，重启后再测，确认两次模型不同，且 `config.toml` 中的 `model_provider` 被自动更新。

### 1.6 Skill 的目录结构与触发机制
**Skill**：`skill-creator`（Codex 内置）  
**MCP**：无  
**仓库地址**：Codex 内置，无需外部下载，直接 `$skill-creator` 调用  
**介绍**：`skill-creator` 交互式生成最小 Skill 骨架，拆开 `SKILL.md` 的 frontmatter 和可选目录，理解 `name` 与 `description` 如何决定触发，`scripts/` 和 `references/` 在命中后才被加载。  
**小实操**：让 `$skill-creator` 创建 `todo-check`（读取 `TODO.md` 并列出未完成项），复制到 `.agents/skills/`，用“看看我还有什么没做完”测试隐式触发是否生效。

### 1.7 安装第一个 Skill 并验证隐式触发
**Skill**：`skill-installer`（内置）+ `create-plan`  
**MCP**：无  
**仓库地址**：`create-plan` 位于 `https://github.com/ComposioHQ/awesome-codex-skills`（`create-plan` 子目录）；通过 `$skill-installer` 按名安装  
**介绍**：`skill-installer` 可从官方精选列表或任意 GitHub 仓库安装技能；`create-plan` 足够简单，但会在第4章开发软件时正式展开，作为贯穿全书的“种子技能”。  
**小实操**：对 `create-plan` 说“给命令行工具加一个 `--dry-run` 选项”，确认它先追问输入输出边界和验收条件，而不是直接写代码。

### 1.8 MCP 与 Skill 的分工
**Skill**：无（概念节）  
**MCP**：`~/.codex/config.toml` 中的 `[mcp_servers.<id>]` 配置结构  
**仓库地址**：无（本节不引入具体 MCP）  
**介绍**：Codex 的 MCP 服务器声明在 host-global 的 `~/.codex/config.toml` 中，stdio 服务器用 `command` + `args`，远程服务器用 `url`。本节建立全书反复使用的分工认知：**MCP 把外部工具“连上”，Skill 决定“怎么用”**。  
**小实操**：手工添加一个指向 `echo` 的 stdio 配置块，重启 Codex 后 `codex mcp list` 确认它出现在服务器列表中。

### 1.9 安装第一个 MCP：Chrome DevTools
**Skill**：无（MCP 安装）  
**MCP**：`chrome-devtools-mcp`  
**仓库地址**：`https://github.com/ChromeDevTools/chrome-devtools-mcp`  
**介绍**：Chrome DevTools MCP 让 Codex 连接真实浏览器，打开页面、读取 DOM、截图、跑 Lighthouse 审计。安装：`codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest`。  
**小实操**：让 Codex 打开 `https://example.com` 并读取 `<h1>`，确认返回 “Example Domain” 之类的结构化结果，而不是让你自己去浏览器里看。

---

## 第2章 编写小说

### 2.1 长篇写作的分层上下文与事实锁
**Skill**：`chinese-longnovel-skill`  
**MCP**：无  
**仓库地址**：`https://github.com/xiaofeng-928/chinese-longnovel-skill`；安装：`npx skills add xiaofeng-928/chinese-longnovel-skill`  
**介绍**：面向中文长篇网文，分层上下文组装、50 章分阶段规划、状态回证、伏笔追踪与回收、一致性审查和自动修复。它的核心不是“生成下一章”，而是用事实锁和分层证据让写到几百章后仍然一致。  
**小实操**：初始化一本经营流长篇，要求只出前 10 章细纲，检查输出中是否包含“事实锁”字段，而不是直接开始写正文。

### 2.2 轻量替代：可恢复的 Markdown 工作流
**Skill**：`ani-book-skill`  
**MCP**：无  
**仓库地址**：`https://github.com/ExplosiveCoderflome/ani-book-skill`；安装：`npx skills add https://github.com/ExplosiveCoderflome/ani-book-skill`  
**介绍**：面向 Codex 的长篇中文小说生产 Skill，以可恢复的 Markdown / YAML 工作流贯通灵感、规划、章节写作、审校与连续性管理。产物保存在可直接阅读和编辑的本地文件中，中断后可以从任意状态恢复。  
**小实操**：初始化最简项目，写 500 字后手动删除最近生成的章节文件，让 Skill“从中断处继续”，验证它能否根据状态文件恢复而非从头重写。

### 2.3 替代方案对照：vibe-noveling
**Skill**：`vibe-noveling`（Codex 适配版）  
**MCP**：无  
**仓库地址**：`https://github.com/wwt87/vibe-noveling`，`codex/` 目录包含 Codex Skill 适配  
**介绍**：完整中文网文创作工作流，含 13 个专业技能 + 4 个子 Agent，覆盖初始化、讨论、规划、写作、返修、同步。与 `chinese-longnovel-skill` 的重结构形成对照。  
**小实操**：用 `$vibe-noveling` 初始化一个中文网文项目，观察它是否先进入本地工作流初始化，而不是直接生成章节。

### 2.4 伏笔追踪与一致性审查
**Skill**：`chinese-longnovel-skill`（审查环节）  
**MCP**：无  
**仓库地址**：同 2.1  
**介绍**：伏笔在这个 Skill 中被当作“待偿债务”来管理：进入细纲计划、章节总结和阶段摘要，写作时检查是否被提前消费，审查时检查是否超期或变义。  
**小实操**：在细纲中插入“第3章埋下旧钥匙，计划第8章回收”，执行一致性审查，确认报告中列出埋设章 / 计划回收章 / 当前状态。

---

## 第3章 制作视频

### 3.1 口播视频的自动粗剪与字幕
**Skill**：`videocut-skills`  
**MCP**：无  
**仓库地址**：`https://github.com/ljiao0729-lang/videocut-skills`（维护中）；`https://github.com/Agentchengfeng/chengfeng-videocut-skills`（当前有效仓库）；安装：`git clone https://github.com/Ceeon/videocut-skills.git ~/.codex/skills/videocut`  
**介绍**：专为口播视频设计：静音检测阈值可调，语义理解识别重说和卡顿，重复句检测按“相邻句开头≥5字相同”删前保后，输出 `edited.mp4` 和 `edited.srt`。核心价值是把“粗剪 + 字幕”这条最耗时的链路交给 Skill，并给出可逐条审阅的删除清单。  
**小实操**：用 1—2 分钟口播素材触发剪口播，在审核界面查看标记出的静音段和口误段，只确认前 3 条删除建议后执行剪辑。

### 3.2 卡点转场与产品宣传片
**Skill**：`match-cut`  
**MCP**：无  
**仓库地址**：`https://github.com/Sac-Y/match-cut`  
**介绍**：默认 20 秒的产品宣传片 Skill，用“同一形状或动作延续、每刀切换一个世界”的匹配剪辑逻辑严格卡节拍，时长可调。  
**小实操**：提需求“桌面咖啡杯 20 秒匹配剪辑短片”，观察它是否先给出切入角度、每个世界的场景、文案和预算的方案，再进入渲染，而不是直接输出成片。

### 3.3 从粗剪到包装的衔接
**Skill**：`videocut-skills` → `match-cut`  
**MCP**：无  
**仓库地址**：同 3.1 和 3.2  
**介绍**：粗剪 Skill 清洗素材，卡点 Skill 做风格化包装，两者覆盖视频生产链上不同的工序。衔接的关键是粗剪产物能否被卡点 Skill 直接接受为输入。  
**小实操**：把 3.1 产出的 `edited.mp4` 作为 3.2 的输入素材，让 `match-cut` 基于这段粗剪做 20 秒卡点版本，验证两个 Skill 能否串联。

---

## 第4章 代码编写：React + FastAPI 全栈小项目

### 4.1 需求澄清：先想清楚“待办事项”到底做什么
**Skill**：`grill-me` 或 `hl-grill`，配合 `superpowers` 的 brainstorming 环节  
**MCP**：无  
**仓库地址**：`grill-me` — `https://github.com/mattpocock/skills`（`skills/productivity/grill-me`），`npx skills add mattpocock/skills --skill grill-me`；`hl-grill` — `https://github.com/HugoLopes45/hl-skills`，`npx skills add HugoLopes45/hl-skills` 后按需选用  
**介绍**：“做一个待办事项应用”至少藏着十几项未定决策：待办有没有截止日期？支不支持优先级？删除是硬删还是归档？列表默认按什么排序？哪些操作需要二次确认？`grill-me` / `hl-grill` 的作用是在写第一行代码之前，把这些分歧逐条逼出来，而不是让 Codex 基于模糊描述自行脑补功能。`superpowers` 的 brainstorming 环节则把追问结果收敛成一份边界明确的设计说明。  
**小实操**：用“我想做一个小的待办事项应用，后端 FastAPI、前端 React”触发 `grill-me` 或 `hl-grill`。要求至少问清楚数据字段、必做操作、列表默认排序、删除是否需要确认。整理成不超过 1 页的 `SPEC.md`，检查 Codex 是否在追问完成前拒绝直接生成代码或文件结构。

### 4.2 脚手架：让 Skill 把前后端骨架搭起来
**Skill**：`building-viewers`（含 React + TypeScript + FastAPI starter）或 `fastapi-fullstack`  
**MCP**：无（本节只搭结构，不跑浏览器）  
**仓库地址**：`building-viewers` — `https://github.com/xrwr/codex-skills`，`npx skills add xrwr/codex-skills --skill building-viewers`；`fastapi-fullstack` — `https://github.com/rebyteai-template/rebyte-skills`（`fastapi-fullstack` 子目录）  
**介绍**：`building-viewers` 附带 React + TypeScript + FastAPI 起始模板，但要求 scaffold 后替换 domain 层、对接目标仓库的依赖管理和启动命令，而不是把模板当成完成品。`fastapi-fullstack` 更“重”，基于 `tiangolo/full-stack-fastapi-template`，带 PostgreSQL 和 Docker Compose，适合想继续往生产形态走时选读。  
**小实操**：让 `building-viewers` 用 starter 生成前后端目录，先输出“将要对模板做哪些替换”的清单：后端改哪些路由和 schema、前端改哪些页面和组件、依赖里哪些用不到。对照 `SPEC.md` 检查覆盖所有必做操作，确认后再进入 4.3。

### 4.3 后端 API：用 TDD 写 FastAPI 的 CRUD
**Skill**：FastAPI 官方内置 skill + `hl-tdd` 或 `superpowers` 的 TDD 环节  
**MCP**：`context7`（按需查文档）  
**仓库地址**：FastAPI 官方 skill — 安装 FastAPI 后运行 `uvx library-skills install --skill fastapi --yes`，自动放入 `.agents/skills/fastapi`；`hl-tdd` — 同 4.1；`context7` — `https://github.com/upstash/context7`，`~/.codex/config.toml` 中配置 `npx -y @upstash/context7-mcp`  
**介绍**：FastAPI 官方随包附带 agent skill，按项目实际安装版本提供路由、依赖注入、Pydantic schema 指导，不依赖模型训练时的旧文档。`hl-tdd` / `superpowers` 确保先写一个会失败的 pytest，再写最小实现让它变绿。`context7` 在通用指导不够具体时拉取当前版本精确用法。  
**小实操**：让 Codex 先为“创建待办”和“标记完成”各写一个 pytest，运行确认 RED（失败原因是功能缺失，不是 import 错误）。再在 FastAPI skill 和 `hl-tdd` 约束下写最小实现，确认 GREEN 且原有测试未被破坏。保留每一步测试输出。

### 4.4 前端页面：组件先行，接口后接
**Skill**：`hl-tdd`（前端环节），配合 Vitest / React Testing Library 相关技能  
**MCP**：`context7`（按需查 React 当前版本用法）  
**仓库地址**：`hl-tdd` — 同 4.1；React 测试技能可参考 `maddhruv/absolute` 的 `jest-vitest` 或 Dify 的 `frontend-testing` 模式  
**介绍**：前端最容易滑向“先接 API 再调 UI”，结果接口一改组件全废。本节把顺序反过来：先按 `SPEC.md` 做列表、表单项、完成状态切换，用 mock 或本地 state 跑通交互，再用 Vitest + RTL 锁住行为，最后才把 fetch 指向 4.3 的真实后端。  
**小实操**：选“输入标题，点击添加，列表新增一项”，先写 RTL 测试断言输入、点击、列表变化，确认 RED 后写最小组件让测试变绿。完成后切 fetch 到本地 FastAPI，手动走一遍同样路径，检查行为与测试描述一致。

### 4.5 联调与浏览器验证：让 Skill 自己把服务跑起来
**Skill**：`test-run`（ASTRA Integration Testing）或 `chrome-devtools` 技能  
**MCP**：`chrome-devtools-mcp`  
**仓库地址**：`test-run` — 通过 LobeHub 或对应仓库安装；`chrome-devtools` 技能 — `https://github.com/kriscard/skills`；MCP — `https://github.com/ChromeDevTools/chrome-devtools-mcp`，`codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest`  
**介绍**：前后端分别跑通不等于流程跑通。`test-run` 自动探测技术栈、启动 FastAPI 和 React 服务、轮询端口就绪、捕获日志，再驱动真实 Chrome 做页面渲染和 API 行为验证。`chrome-devtools` 技能提供更底层的检查：控制台错误、网络请求、DOM 状态、截图。  
**小实操**：让技能自行启动前后端，完成“页面加载 → 输入‘写测试’ → 点击添加 → 列表出现 → 刷新后仍在”。要求报告启动命令、端口、console error 和网络 4xx/5xx；失败时先输出关键日志行和失败请求，不直接改代码。

### 4.6 审查与收尾：把“能跑”变成“可交付”
**Skill**：`hl-code-review` + `hl-verify`，或 `superpowers` 的 code review 环节  
**MCP**：`gh-fix-ci`（如项目已接入 GitHub Actions）  
**仓库地址**：`hl-code-review` / `hl-verify` — 同 4.1；`gh-fix-ci` — `https://github.com/openai/skills`，`$skill-installer gh-fix-ci`  
**介绍**：`hl-code-review` 针对分支做 bug 和回归审查，重点不是风格挑刺，而是“这个改动会不会破坏别的东西”。`hl-verify` 把 `SPEC.md` 拿回来逐条核对验收条件。`gh-fix-ci` 接手失败 Actions，区分真实失败和环境噪声。  
**小实操**：让 `hl-verify` 对照 `SPEC.md` 逐条打勾，每条给出验证方式（测试名、浏览器路径或手动步骤）。让 `hl-code-review` 至少指出一个“以后可能出问题”的风险点（空列表、重复提交、错误分支无反馈），写入 `REVIEW.md`。

### 4.7 收束：这一章真正固化的不是 Todo 应用
**Skill**：无（概念收束）  
**MCP**：无  
**仓库地址**：无  
**介绍**：Todo 本身没有价值，有价值的是顺序：需求澄清（grill）→ 脚手架（building-viewers）→ 后端 TDD（FastAPI skill + hl-tdd）→ 前端测试先行（hl-tdd）→ 真实浏览器联调（test-run / chrome-devtools）→ 对照规格验收（hl-verify）。你保留决定边界和验收标准的权力。  
**小实操**：把本章实际调用过、且产生可验证产出的 Skill 列成最小清单，删掉“装了但没用上”的，作为下个项目起点。

---

## 第5章 逆向软件

### 5.1 逆向中 MCP 与 Skill 的分工
**Skill**：`rust-reverse-engineering-skill`（编排示例）  
**MCP**：`ida-pro-mcp` / `x64dbg-mcp`（执行层，见 5.2 / 5.3）  
**仓库地址**：`https://github.com/jingjing2222/rust-reverse-engineering-skill`；安装：`claude plugin marketplace add jingjing2222/rust-reverse-engineering-skill` → `claude plugin install rust-reverse-engineering@jingjing2222-plugins`  
**介绍**：IDA 和 x64dbg 的 MCP 把反汇编、内存、断点、交叉引用暴露给 Codex；Skill 决定“先看什么、怎么交叉验证、什么条件下判定完成”。`rust-reverse-engineering-skill` 作为编排示例，把底层能力串成“指纹 → crate 边界 → 伪代码 → 报告”的流程。  
**小实操**：让编排 Skill 对样例二进制生成一份分析计划，检查计划中是否明确列出每一步要调用哪个 MCP 工具、拿到什么产物、什么条件下进入下一步。

### 5.2 静态分析：IDA Pro MCP
**Skill**：无（MCP 单独跑通）  
**MCP**：`ida-pro-mcp`  
**仓库地址**：`https://github.com/mrexodia/ida-pro-mcp`；安装：`codex plugin marketplace add mrexodia/codex-marketplace` → `codex plugin add ida-pro-mcp@mrexodia`  
**介绍**：通过 `idalib` 提供无头反汇编、反编译、类型分析和交叉引用。Codex 可以通过 `ida_get_pseudocode`、`ida_list_functions` 等工具读取结构化数据。作者原版 README 已推荐改用 Hex-Rays 官方 IDA MCP Server，正文可注明这一演进。  
**小实操**：加载样例二进制，要求“列出 `main` 调用的函数，并反编译其中参数为字符串常量的函数”，检查返回是否包含函数名、调用地址和伪代码片段。

### 5.3 动态调试：x64dbg MCP
**Skill**：无（MCP 单独跑通）  
**MCP**：`x64dbg-mcp`  
**仓库地址**：`https://github.com/CaptainNox/x64dbg-mcp`（Python MCP server）；`https://github.com/duty1g/x64dbg-mcp-server`（原生插件，HTTP 暴露）；另可搜索 `bromoket/x64dbg_mcp`  
**介绍**：两部分桥接：x64dbg 原生插件暴露调试器状态、内存、寄存器、断点；Python MCP server 让 Codex 通过 stdio 连接，支持 `registers`、`read_memory`、`execute_command` 等工具。与 5.2 的对照：IDA MCP 回答“这个函数长什么样”，x64dbg MCP 回答“运行时它实际做了什么”。  
**小实操**：在 `main` 入口下断点，命中后读取 `RAX` 和 `RIP` 的值，并反汇编 `RIP` 处的 3 条指令，验证返回真实寄存器数值和指令文本。

---

## 第6章 搭建知识库

### 6.1 规则优先的离线 RAG
**Skill**：`md-vault-rag-manager`  
**MCP**：无  
**仓库地址**：`https://github.com/zeal241064-droid/Obsidian-Knowledge-base-`，Skill 位于 `skills/md-vault-rag-manager`，复制到 `~/.codex/skills/`  
**介绍**：核心是一条引导式工作流：初始化 vault 时把规则区和导入区分开，正式知识必须有来源回证，检索是关键词 + 标签 + 路径 + 索引的混合方式，回答必须能追溯到原文。它解决的是“能搜到”和“敢用”之间的差距。  
**小实操**：初始化最小 vault，放入 2 篇互相支持、1 篇矛盾的短笔记，提一个检索问题，观察回答是否标出矛盾并引用具体笔记和行，而不是把 3 篇混在一起给出平滑但不可靠的答案。

### 6.2 插件市场安装与持久记忆
**Skill**：`obsidian-knowledge`  
**MCP**：无  
**仓库地址**：`https://github.com/crypdick/obsidian-knowledge`  
**介绍**：把 Obsidian vault 作为 Agent 的记忆层，支持搜索笔记、保存可复用知识、维护索引和链接，适合跨会话记住上下文。与 `md-vault-rag-manager` 的严格 RAG 工作流形成轻/重对照。  
**小实操**：会话中让 Codex 记住“我的项目代号是 `bluebird`”，结束会话后新开一个会话询问，验证跨会话记忆是否生效。

### 6.3 带证据的检索与结构报告
**Skill**：`md-vault-rag-manager`  
**MCP**：无  
**仓库地址**：同 6.1  
**介绍**：回答必须能追溯到原文，这是知识库“可用”和“能搜到”之间的分界线。结构报告应逐条列出正式知识的来源路径和检索命中证据。  
**小实操**：让 Skill 输出结构报告，要求列出每条正式知识的来源路径和最近一次被检索命中的次数；如果只有“知识库包含 N 篇笔记”的总量统计，说明它还在做“搜索”而不是“RAG 管理”。

### 6.4 接入实时文档知识库：Context7 MCP
**Skill**：无（MCP 单独跑通；可被 6.1 的检索流程编排调用）  
**MCP**：`context7`  
**仓库地址**：`https://github.com/upstash/context7`；npm 包：`@upstash/context7-mcp`  
**介绍**：Context7 是当前文档/知识类 MCP 中热度最高的项目之一，定位是“为 AI Agent 提供实时、版本精确的文档与代码示例”。它解决模型训练数据滞后的问题：回答库或框架用法时，按需拉取当前版本文档并给出可追溯来源。与 6.1—6.3 的分工是：Vault 管理个人知识，Context7 管理外部技术文档知识；两者都由 Skill/工作流决定“什么时候查、查哪个版本、如何引用证据”。  
**安装配置**：在 `~/.codex/config.toml` 中加入 stdio 配置（需 Node.js 22.13+）：
```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
```
重启 Codex 后运行 `codex mcp list` 确认 `context7` 出现。也可用 `npx ctx7 setup` 交互式认证并生成 API Key。  
**小实操**：让 Codex 通过 Context7 查询一个你本地项目正在使用的库（例如 `react` 或 `fastapi`）的当前版本文档，要求回答中同时给出库版本、文档来源/链接、关键 API 用法；再与不查文档时的回答对比，检查是否出现“旧版写法”被纠正。最后把来源链接写入 6.1 的 vault 笔记，验证“外部文档知识库 → 个人知识库”的回证链路。

---

## 第7章 数据分析：从 Kaggle 表格到时序

### 7.1 表格数据的 EDA 与建模：Titanic
**Skill**：`data-analysis-skills`  
**MCP**：`safe-kaggle-mcp`  
**仓库地址**：Skill — `https://github.com/cabbage2000-lab/data-analysis-skills`；MCP — PyPI `safe-kaggle-mcp`，`uvx --from safe-kaggle-mcp kaggle-mcp`  
**介绍**：Titanic 是 Kaggle 最经典的表格二分类数据集，891 行、12 个字段，天然带有缺失值、类别不平衡和需要特征工程的结构。`data-analysis-skills` 先确认业务背景，再执行清洗与 EDA，最后输出单文件 HTML 交互报告，统计纪律内置——不杜撰行业基准、相关不当因果、小样本不硬下结论。`safe-kaggle-mcp` 负责把数据集直接拉到本地，并提供紧凑的 pandas digest EDA 工具，返回 schema、缺失率、分布摘要这类结构化结果，而不是把原始行灌进上下文。  
**小实操**：让 Codex 用 `safe-kaggle-mcp` 拉取 Titanic 训练集，再用 `data-analysis-skills` 做“生存率影响因素”EDA。要求先给出缺失率表和目标变量分布，再重点检查 `Sex`、`Pclass`、`Age` 与 `Survived` 的关系，并明确标注哪些结论是描述性统计、哪些只是相关而非因果。检查 HTML 报告每张图是否配有解读，以及是否声明了样本量和缺失处理方式。

### 7.2 不平衡表格数据的审查与基线：Credit Card Fraud
**Skill**：`data-analysis-skills`（审查与报告环节）  
**MCP**：`safe-kaggle-mcp`  
**仓库地址**：同 7.1  
**介绍**：Credit Card Fraud Detection 是 Kaggle 上使用最广的表格数据集之一，28 万多笔交易中只有 492 笔欺诈，正类占比约 0.172%，是典型的极端不平衡场景。价值不是“再跑一个分类器”，而是学会不把 accuracy 当结论：必须看 precision / recall / PR-AUC，必须声明重采样或类别权重策略，必须把“模型抓到多少欺诈、误报多少正常交易”翻译成业务代价。  
**小实操**：让 Codex 先输出正类占比和特征缺失/量纲概况，再训练一个逻辑回归基线和一个带 `class_weight='balanced'` 的基线，同时报告 PR-AUC、precision、recall 和混淆矩阵，并明确回答：“如果只看 accuracy，这个模型会给人什么错觉？”检查报告是否指出 accuracy 在不平衡数据上的误导性，而不是给出一个 99.8% 的数字就结束。

### 7.3 零售时序的趋势、季节性与回测：Rossmann Store Sales
**Skill**：`data-analysis-skills`（时序 EDA 与报告）或 `automated-data-analyst`（按需）  
**MCP**：`Prophet_mcp`  
**仓库地址**：Skill — 同 7.1；`automated-data-analyst` — `codex plugin marketplace add saineshnakra/automated-data-analyst` → `codex plugin add ada@automated-data-analyst`；MCP — `https://github.com/ipradeep99/Prophet_mcp`  
**介绍**：Rossmann Store Sales 覆盖 1115 家德国药店的日销售记录，同时包含促销、竞争店距、节假日和门店元数据，是零售时序预测里最经典的“多序列 + 外生变量”数据集之一。时序分析和表格分析的第一个区别是必须按时间切分训练/验证，不能随机打乱；第二个区别是必须显式处理趋势、周季节性、年季节性和节假日效应。`Prophet_mcp` 把 Meta Prophet 封装成 MCP 工具：传入历史日期和销售额，返回趋势摘要、置信区间和可直接渲染的 Chart.js 配置。  
**小实操**：选一家门店，让 Codex 先输出按周和按月的销售曲线，标出促销周和节假日附近的变化；再用 `Prophet_mcp` 做 6 周预测，明确给出训练截止日和回测区间。检查报告是否区分“拟合历史”和“预测未来”，以及是否在回测区间上计算误差，而不是只展示一条漂亮的全历史拟合线。

### 7.4 多序列时序与层次结构：Walmart Store Sales Forecasting
**Skill**：`data-analysis-skills`（多序列 EDA 与报告）  
**MCP**：`Prophet_mcp` 或 `tslab-mcp`  
**仓库地址**：Skill — 同 7.1；`Prophet_mcp` — 同 7.3；`tslab-mcp` — `https://github.com/pedrobtz/tslab-mcp`  
**介绍**：Walmart Store Sales Forecasting 提供 2010—2012 年按门店 × 部门的周销售额，同时附带温度、油价、CPI、失业率和 markdown 等外生变量，是“多序列 + 层次聚合”的典型代表。这里要练的是多个序列放在一起时不能只盯一条线：不同门店/部门的量级、趋势和季节性可能完全不同；聚合到总销售额时，个体误差可能互相抵消，看起来“总预测很准”，但每个门店都偏。  
**小实操**：让 Codex 选 3 家门店（总销量高、中、低各一家），分别输出周销售曲线和促销标记，比较它们的季节性是否一致；然后用 `Prophet_mcp` 对其中一条序列做预测，要求报告 MAPE 或 RMSE，并回答“这条序列的误差能否代表其他门店”。检查它是否明确拒绝用单条序列的结论覆盖全部门店。

### 7.5 从“跑通一次”到“可复用分析 SOP”
**Skill**：回到 `skill-creator`（内置）或 `data-analysis-skills`  
**MCP**：同 7.1—7.4（不新增）  
**仓库地址**：`skill-creator` — Codex 内置，`$skill-creator`  
**介绍**：这一节不引入新数据集，而是把 7.1—7.4 重复出现的动作收束成一个可复用的 SOP：拿到数据 → 先看 schema/缺失/目标分布 → 按数据类型选 EDA 路径（表格 vs 时序）→ 用 MCP 拉数据或跑预测 → 按时间或分层回测 → 报告里标注证据边界。  
**小实操**：让 `$skill-creator` 生成一个最小 Skill 骨架，名字可以叫 `kaggle-eda-check`，`description` 收紧到一句话，覆盖“表格数据先查缺失和目标分布，时序数据先按时间切分并检查周期”。然后用“帮我看看这个 CSV 有没有问题”测试隐式触发，检查它是否在动手画图之前先要求确认数据类型和分析目标。

---

## 第8章 办公：文职人员的日常场景

### 8.1 文档写作与公文：从素材到可交付的 Word
**Skill**：`official-document-drafting` 或 `document-SKILLs` 的 `docx`  
**MCP**：无  
**仓库地址**：`official-document-drafting` — `https://github.com/zhaohui-yang/official-document-drafting`；`document-SKILLs` — `https://github.com/appautomaton/document-SKILLs`，克隆后为 `docx` 建符号链接到 `~/.codex/skills/`  
**介绍**：文职文档分两类。一类是有格式刚性的公文和正式报告：`official-document-drafting` 按 GB/T 9704-2012 的规范起草报告、通知、请示、纪要等 22 种文种，并导出 Word。另一类是通用 Word 写作与修订：`document-SKILLs` 的 `docx` 支持创建、批注、真正的修订记录，并在交付前校验没有未记录改动。两者的共同纪律是：先确认文种、受众和素材边界，再动笔。  
**小实操**：给 Codex 一段零散素材（本周完成三项工作、下周计划两项、有一个问题需要协调），要求用 `official-document-drafting` 生成一份“工作周报”的 DOCX。检查它是否先追问报送对象和用途，以及生成的文档是否套用了正确的文种骨架。如果换成通用 `docx`，要求它“只加批注、不改原文”，验证修订记录是否被正确标记。

### 8.2 表格与数据报表：把 Excel 变成可解释的结论
**Skill**：`data-analysis-skills` 或 `openai/spreadsheet`  
**MCP**：无  
**仓库地址**：`data-analysis-skills` — `https://github.com/cabbage2000-lab/data-analysis-skills`，克隆到 `~/.codex/skills/data-analysis-skills`；`openai/spreadsheet` — `npx skills add https://github.com/openai/skills --skill spreadsheet`  
**介绍**：文职人员处理表格，多数时候不是“建模型”，而是把一张别人发来的表变成自己能汇报的东西：清洗脏数据、算几个关键指标、做一两张图、写几句结论。`data-analysis-skills` 先确认行业和报告受众，再清洗分析，最后产出单文件 HTML 交互报告——结论先行、每张图配解读、数据处理过程可追溯，并内置统计纪律。`openai/spreadsheet` 更偏表格本身的操作：用 Python 读写 `.xlsx`/`.csv`，处理公式和格式，适合交付一个干净的 Excel 文件。选择标准：要“讲清楚数据说明了什么”用前者，要“把表改对、公式修好”用后者。  
**小实操**：找一张带缺失值、列名不规范的 CSV，先让 `data-analysis-skills` 分析。要求它在画图之前先输出缺失率、每列的类型推断和“它打算按什么业务视角组织报告”。如果它直接开始出图而没有确认受众，说明门禁没有生效。然后换 `openai/spreadsheet`，要求“把空值按业务规则填上、把日期列统一格式、保存为新文件”，检查原始文件是否未被覆盖。

### 8.3 PPT 汇报：先确认大纲，再生成页面
**Skill**：`build-ppt-from-sources`  
**MCP**：无（依赖环境中的演示文稿与图片生成能力）  
**仓库地址**：`https://github.com/2233531707/build-ppt-from-sources`；Codex 中直接 `$skill-installer` 安装该 URL，或克隆到 `~/.agents/skills/build-ppt-from-sources`  
**介绍**：办公场景的 PPT 有一个特殊约束：不能直接甩出一份成品让领导大改。`build-ppt-from-sources` 是一条门禁流程：资料分类 → 大纲确认 → 逐页文案确认 → 预览图分批确认（每批最多 5 页）→ 高清素材确认 → 制作 → 渲染质检。每一道门禁不确认，就不进入下一步；用户修改上游内容时，它会退回对应阶段并同步更新后续产物。它明确拒绝“用常识补关键成果”“把整页预览图直接当最终页面”。  
**小实操**：给 Codex 一份项目周报文档和一张数据表，要求“用 `$build-ppt-from-sources` 做一份 8 页的领导汇报 PPT，先给我资料分类和大纲”。检查它是否停在大纲门禁处等你确认，而不是直接生成全部页面。确认大纲后，要求它只出前 3 页的预览，验证是否遵守“每批最多 5 页”的约束。最后检查生成的页面中，数据来源是否有标注，而不是凭空出现一个没有出处的百分比。

### 8.4 会议纪要：录音到结构化纪要，关键是不编造
**Skill**：`meeting-minutes-skill` 或 `meeting_offline`  
**MCP**：无  
**仓库地址**：`meeting-minutes-skill` — `https://github.com/Jiale077/meeting-minutes-skill`，克隆到 `~/.codex/skills/meeting-minutes`；`meeting_offline` — `https://github.com/sunxuwang001-sketch/meeting_offline`  
**介绍**：会议纪要的核心风险不是“写得不够漂亮”，而是人名、数字、承诺、期限被模型顺手编出来。`meeting-minutes-skill` 的路线是“通义听悟负责听准，大模型负责写好”：录音经说话人分离转写后，按模板提炼成正式中文纪要，同时生成 `review-notes.md` 标出可疑的姓名、单位、专业词和需要人工回听的时间段。`meeting_offline` 走另一条路：本地转写、无需 API Key，交付可编辑 HTML 和 PNG 图片，版式可在公文、卡片、时间轴之间切换；纪律是“负责人和期限只写会上说过的，没说就留空”。  
**小实操**：用一段 2—3 分钟的模拟会议录音（或已有转写稿），让 `meeting-minutes-skill` 生成纪要。重点检查 `review-notes.md` 是否真的列出了需要人工确认的点，而不是一片空白。如果使用 `meeting_offline`，检查纪要中“负责人”和“期限”为空的行——如果会上确实没提，它应该留空而不是替你填一个“合理”的日期。

### 8.5 邮件与日程：读取可以自动化，发送必须停下来
**Skill**：`outlook-skill`，配合 `codex-work-starter` 的安全方法论  
**MCP**：无（`outlook-skill` 通过 Microsoft Graph API 工作）  
**仓库地址**：`outlook-skill` — `https://github.com/dbhq-uk/outlook-skill`；`codex-work-starter` — `https://github.com/fanko1217/codex-work-starter`  
**介绍**：邮件和日程是办公场景里权限最敏感的部分。`outlook-skill` 提供 `outlook` 和 `outlook-to-md` 两个技能：前者读写 Microsoft 365 邮件和日历，后者把 PST 归档转成可搜索的 Markdown。安全设计包括：回复默认保留全部原始收件人；发送是独立命令，起草和发送不是同一个动作，可用 `OUTLOOK_READ_ONLY=1` 把整个会话锁成只读；创建带参会人的事件必须显式 `--send-invites`，删除被拒绝而改用 `cancel`。`codex-work-starter` 提供更上层原则：读取、整理、起草可以在授权范围内进行；发送、退订、邀请、删除、发布、购买一律停下等确认。  
**小实操**：让 Codex 用 `outlook` 读取今天未读邮件，按“紧急 / 需要回复 / 仅知会”分类，并起草一封回复。检查它是否停在草稿阶段，而不是直接发送。然后开启 `OUTLOOK_READ_ONLY=1`，尝试让它“把某封邮件标记为已读”，确认只读模式下写操作被拒绝。

### 8.6 PDF 与合同：提取、翻译、比对，先问清楚“要什么”
**Skill**：`pdf-visual-translate-zh` 或 `fast-pdf-to-markdown`  
**MCP**：无  
**仓库地址**：`pdf-visual-translate-zh` — `https://github.com/Eim-aa/pdf-visual-translate-zh`；`fast-pdf-to-markdown` — `https://github.com/NewTurn2017/fast-pdf-to-markdown`  
**介绍**：文职人员碰到 PDF，通常不是“读一遍”，而是三类任务：翻译（研报、公告、合同的中文版）、提取（把 PDF 变成可检索、可引用的文本）、比对（两版合同哪里改了）。`pdf-visual-translate-zh` 面向版式保真的中文翻译，尽量保留表格、图表和页面结构。`fast-pdf-to-markdown` 做页锚定的 Markdown 转换，输出时附带 JSON 报告，区分 `clean`、`review_required`、`ocr_required`——它不假装每一页都完美识别，而是告诉你哪些页需要人工看一眼。  
**小实操**：用一份带表格的 PDF，让 `fast-pdf-to-markdown` 转换。检查它是否生成了 `review_required` 或 `ocr_required` 的页面标记，以及这些标记是否对应真实存在识别难度的页面。如果做翻译，要求它先输出术语表（比如“甲方/乙方”的译法），再开始正文，验证它是否在长文档翻译前先锁定一致性。

### 8.7 收束：办公场景的判断力，比“全自动”更重要
**Skill**：无（概念收束，回扣 `codex-work-starter`）  
**MCP**：无  
**仓库地址**：同 8.5  
**介绍**：这一章没有引入任何“一键替代文职人员”的 Skill，恰恰是因为办公场景的失败代价往往不是“代码报错”，而是发错了人、删错了文件、纪要里多了一个没人说过的承诺。`codex-work-starter` 给出的顺序值得作为全章的收束：先写清楚规则 → 只连必要的应用 → 手动跑通一个真实任务 → 确认没跑偏 → 再固化成可复用流程 → 最后才考虑定时。  
**小实操**：把 8.1—8.6 中你实际用过的 Skill 列成一张“允许 / 需确认 / 禁止”三列清单。例如：读取邮件 = 允许；起草回复 = 需确认；发送邮件 = 禁止（除非逐次授权）。清单上的每一行都配一个你亲自验证过的触发方式。

---

## 第9章 RPA

### 9.1 浏览器 MCP 的选择：Chrome 还是 Firefox
**Skill**：无（MCP 选型）  
**MCP**：`chrome-devtools-mcp` / `firefox-devtools-mcp`  
**仓库地址**：Chrome — `https://github.com/ChromeDevTools/chrome-devtools-mcp`；Firefox — `https://github.com/mozilla/firefox-devtools-mcp`  
**介绍**：Chrome MCP 偏“开发调试 + 质量审计”，Firefox MCP 基于 WebDriver BiDi，支持 `--headless` 和 `--viewport` 参数。两者都写进 `~/.codex/config.toml`，不冲突。浏览器 MCP 应使用专用 profile，避免接触日常浏览器中的 cookie 和已保存会话。  
**小实操**：分别用两个 MCP 打开同一页面读取 `<title>`，比较返回时间和是否需要额外参数，感受 Chrome 的开箱即用与 Firefox 的显式配置差异。

### 9.2 浏览器自动化的 Skill 编排
**Skill**：`realbrowser`（编排层）  
**MCP**：Chrome / Firefox MCP（执行层）  
**仓库地址**：`https://github.com/darkamenosa/realbrowser`；安装：`git clone https://github.com/darkamenosa/realbrowser ~/.codex/skills/realbrowser`，使用 `agents/openai.yaml` 配置  
**介绍**：MCP 提供“打开、点击、填表、截图”的原子能力，Skill 负责编排成“启动 → 定位 → 填写 → 提交 → 校验 → 重试”的固定步骤。核心产出不是“跑通一次”，而是把一次跑通固化成可重复的 Skill。  
**小实操**：对一个搜索框 + 结果列表的公开页面，让 Skill 编排“输入 `codex skill`、提交、读取前 3 条标题”，重点观察提交后是否显式校验结果列表非空。

### 9.3 桌面自动化：Windows-MCP
**Skill**：无（MCP 单独跑通）  
**MCP**：`Windows-MCP`  
**仓库地址**：`https://github.com/CursorTouch/Windows-MCP`；PyPI：`windows-mcp`，支持 `uvx windows-mcp serve`  
**介绍**：轻量开源的 MCP server，让 AI Agent 与 Windows 操作系统集成，支持文件导航、应用控制、UI 交互和窗口操作。在 `~/.codex/config.toml` 中添加 `[mcp_servers.windows-mcp]`，`command = "uvx"`，`args = ["windows-mcp", "serve"]`。桌面自动化权限远大于浏览器自动化，必须限制在隔离环境或明确授权的应用上。  
**小实操**：让 Codex 通过 Windows-MCP 在桌面创建 `codex-rpa-test` 文件夹并写入 `result.txt`，手动去桌面确认文件真实存在，而不仅仅是 MCP 返回“成功”。

### 9.4 跨浏览器 + 桌面的混合流程
**Skill**：Skill 编排层（跨段校验）  
**MCP**：Chrome MCP（浏览器段）+ Windows-MCP（桌面段）  
**仓库地址**：同 9.1 和 9.3  
**介绍**：每个 MCP 只负责自己那一段，跨段编排才是 Skill 的工作。这个实操的全部价值在于让读者看到：**MCP 各自跑通不等于流程跑通，跨段校验才是编排**。  
**小实操**：Chrome MCP 读取 `example.com` 的 `<h1>`，Windows-MCP 写入桌面 `example-h1.txt`，Skill 校验文件内容与页面标题是否一致；不一致时输出差异。

---

## 第10章 编写论文

### 10.1 中文优先的学术写作与学位论文
**Skill**：`research-writing-skill`  
**MCP**：无  
**仓库地址**：`https://github.com/Norman-bury/research-writing-skill`；安装：`git clone https://github.com/Norman-bury/research-writing-skill.git ~/.codex/research-writing-skill`  
**介绍**：中文优先的学术写作 Skill，覆盖头脑风暴、章节写作、文献综述、Python 图表和 LaTeX 输出，支持“帮我写毕业论文”这类隐式触发。它的价值在于把中文学术写作的规范内置到生成过程中，而不是先出英文再翻译。  
**小实操**：给出“帮我写一篇深度学习图像分割的毕业论文引言，约 500 字”，观察它是否先追问论文类型、学科、研究背景、方法，而不是直接生成一段泛泛的引言。

### 10.2 数学建模竞赛论文的模板与检查
**Skill**：`mathmodel-latex-skill`  
**MCP**：无  
**仓库地址**：`https://github.com/wangling-miao/mathmodel-latex-skill`（v1.0.8）  
**介绍**：面向 MCM/ICM、CUMCM 的 LaTeX 论文 Skill，解决竞赛特有的“格式合规 + 交付安全”问题，包含 LaTeX 编译预检、匿名检查、引用/关键词校验和 CUMCM 优秀论文风格规则。  
**小实操**：生成空的竞赛论文模板，故意留一个 `\cite{missing}`，执行引用检查，确认它报出未定义引用，而不是让 PDF 编译静默通过。

### 10.3 从零生成骨架与可编译初稿
**Skill**：`academic-researcher` / `research-writing-skill`  
**MCP**：无  
**仓库地址**：`academic-researcher` — `npx skills add academic-researcher-skill --skill academic-researcher`（安装前建议在 npm / GitHub 确认最新状态）；`research-writing-skill` 同 10.1  
**介绍**：端到端链路：研究主题 → 章节骨架 → 引用格式 → LaTeX 输出。重点观察骨架是否有论证层次的递进，以及 `.tex` 是否能无错误编译。  
**小实操**：给定“基于图神经网络的推荐系统”，要求输出三级标题 + 每节预期字数的骨架，并生成一个可直接 `pdflatex` 编译的最小 `.tex`；检查骨架有层次、`.tex` 无错误编译。

---

## 第11章 运营自媒体

### 11.1 公众号从选题到草稿箱
**Skill**：`publish-gzh`  
**MCP**：无  
**仓库地址**：`https://github.com/AnziBai/codex-skills`，Skill 位于 `skills/publish-gzh`；安装：克隆后运行 `powershell -NoProfile -ExecutionPolicy Bypass -File ".\skills\publish-gzh\scripts\register-local-skill.ps1" -Json`  
**介绍**：覆盖公众号的完整生产链：选题、来源约束、中文写作、独立审稿、可选语义配图、确定性校验，最终进入草稿箱。设计重点是把“审稿”作为独立环节，而不是写作的附属。  
**小实操**：给具体选题“Codex Skill 和 MCP 的区别”，观察它写作前是否先输出来源清单或事实约束，而不是直接开始写正文。

### 11.2 跨平台草稿生成与上传
**Skill**：`filler`  
**MCP**：无（底层用 Playwright）  
**仓库地址**：`https://github.com/AnziBai/codex-skills`，Skill 位于 `skills/filler`；安装：`.\skills\filler\scripts\filler.ps1 setup-draft-fill -Json`  
**介绍**：把已完成作品转成平台发布草稿：AI 写标题文案，CLI 校验素材，Playwright 自动上传到小红书、抖音、视频号的草稿箱。与 `publish-gzh` 互补：一个负责“从无到有写公众号”，一个负责“把已有内容适配到多平台草稿箱”。  
**小实操**：把 11.1 的文章交给 `filler` 生成小红书版本，只到“草稿箱生成”为止，不实际发布；检查它是否为小红书做了标题长度、分段和话题标签适配，而不是原样搬运。

### 11.3 图文视觉物料的生成
**Skill**：`guizang-social-card-skill`  
**MCP**：无  
**仓库地址**：`https://github.com/op7418/guizang-social-card-skill`；安装：`npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill`  
**介绍**：从小红书图文组图到公众号封面对，把“找图”变成“按内容生成匹配的视觉物料”。对于不擅长设计的初学者，它降低了封面和组图的门槛；对于已经产出内容的读者，它是发布前最后一块拼图。  
**小实操**：用 11.1 的标题和摘要生成 3 张小红书图文卡片，检查卡片与内容主题相关，而不是套用一个通用模板。

---

## 第12章 金融：选股、因子、风控与研报

### 12.1 A 股多因子选股与组合构建
**Skill**：`stockaskill`  
**MCP**：无  
**仓库地址**：`https://github.com/axjing/stockaskill`；安装到 `.agents/skills/stockaskill/` 或 `~/.agents/skills/stockaskill/`，也可 `npx skills add axjing/stockaskill`  
**介绍**：基于 AKShare + SQLite 缓存，做多因子评分、排名和组合构建，覆盖价值、质量、成长、动量、低波、规模等维度。定位是可审计的研究流程，不是投资建议；数据质量判断、因子经济逻辑和风控决策仍然由读者承担。  
**小实操**：运行 `python stockaskill/scripts/run.py scan A --top 10`，让 Skill 解释第一名在价值、质量、成长、动量各维度的分数和数据报告期，验证评分可逐维度追溯，而不是一个黑箱总分。

### 12.2 研报解析：把 PDF/网页/文本变成可审计的复现包
**Skill**：`quant-research-replication`（主推，全链路）；`alphaear-finance`（轻量替代，只做结构化提取）  
**MCP**：无  
**仓库地址**：`quant-research-replication` — `https://github.com/quantskills/skill-quant-research-replication`；`alphaear-finance` — `https://github.com/Lupumbba/alphaear-finance`，`uv sync` 后符号链接 `alphaear-finance/` 到 `~/.codex/skills/`  
**介绍**：`quant-research-replication` 的定位不是“读一篇研报然后总结”，而是把一篇量化研报或论文变成一套可运行的复现包：来源发现 → 全文中文翻译 → 因子公式重建 → 用真实数据做因子有效性验证 → 生成 BACKTEST 策略代码并本地执行回测 → 输出中文复现报告。硬约束是“所有图表和指标必须能追溯到产物，不能运行或数据不足的环节须如实标为未完成或结论不确定”。`alphaear-finance` 则轻得多：把研报结构化为可检索的字段和摘要，适合快速判断“值不值得深读”，但不做复现和回测。  
**小实操**：找一篇带因子公式的公开量化研报，让 `quant-research-replication` 只执行到“因子公式重建 + 数据可用性检查”，暂不进入回测。要求输出：重建的因子表达式、所需字段清单、当前工作区中哪些字段可用、哪些缺失、以及如果缺失它打算如何降级或标记。检查它是否在数据不足时如实标注“未完成”，而不是用一个替代字段强行计算出一个 IC 数字。

### 12.3 辩论式因子挖掘与评估
**Skill**：`skill-factormad-debate-factor-mining`  
**MCP**：无  
**仓库地址**：`https://github.com/quantskills/skill-factormad-debate-factor-mining`；安装：克隆后 `pip install -r requirements.txt`，先跑 `dry_run` 验证  
**介绍**：这个 Skill 不是因子库，也不是回测引擎，而是一个 FactorMAD 风格的双 Agent 辩论式因子挖掘流程：一个 Agent 提出候选因子的代码实现，另一个 Agent 从可运行性、未来函数、NaN/inf、索引对齐、零成交量等角度批评和修正，最终输出可执行 Python 函数而非只有公式的表达式，并做轻量 Pearson IC、RankIC、ICIR 筛选，所有候选、辩论意见和筛选结果按时间戳归档。它反复强调的边界是：IC/RankIC 只是内部筛选指标，不能替代组合级回测；样本外、交易成本、风险暴露和组合构建需要另走独立流程。与 12.2 的复现链路衔接：复现产出候选因子，辩论环节负责精炼和轻量筛选。  
**小实操**：用仓库自带的 `toy_market_data.csv` 跑一次 `dry_run`，确认它能输出辩论记录和候选因子 JSON，不调用 LLM。然后开启真实运行，只要求生成 1 个候选因子，并明确回答：这个因子在辩论中被反方指出了哪些问题、最终版本修正了什么、IC/RankIC 是在哪个时间区间和样本上计算的。检查输出目录中是否同时存在 `debate` 记录和 `accepted_factors`。

### 12.4 风控（一）：财报排雷——先问“能不能信”，再问“值多少钱”
**Skill**：`annual-report-red-flag-auditor`（`financial-red-flag-auditor-skill`）  
**MCP**：无  
**仓库地址**：`https://github.com/noahnan-max/financial-red-flag-auditor-skill`；安装：`git clone ... ~/.codex/skills/annual-report-red-flag-auditor`  
**介绍**：这个 Skill 的立场非常克制，开篇就说明它不预测股价、不做估值、不生成交易信号，它只回答一个更基础的问题：“这家公司的财报是否可信到值得继续研究？”。工作流是：收集官方财报证据 → 用结构化数据与官方披露交叉核对 → 检查会计政策/估计/列报可比性 → 应用确定性的红旗筛选规则 → 在 15 个维度上做 100 分制财务质量评分 → 区分事实、计算、第三方数据、解释、开放问题 → 生成 P0/P1/P2 问题卡 → 输出长版排雷报告和 HTML。安全边界明确：除非监管、法院、交易所、审计师或公司公告已经认定，否则不能把欺诈、虚假披露、占用资金等作为事实陈述，只能说“识别到风险信号”。  
**小实操**：用一家上市公司最近一期年报，触发 `$annual-report-red-flag-auditor`。要求它只输出 P0/P1/P2 问题卡和对应的证据出处，暂不生成完整 HTML 报告。重点检查：每一张问题卡是否附带了具体的报表科目、年份、数值和原文位置；以及它在描述风险时是否使用了“风险信号/待核实”而不是“存在造假”。

### 12.5 风控（二）：组合风险预算——把信号变成可审计的决策，而不是直接下单
**Skill**：`quant-portfolio-risk`  
**MCP**：无  
**仓库地址**：`https://github.com/quantskills/skill-quant-portfolio-risk`  
**介绍**：财报排雷解决的是“单一标的能不能信”，组合风控解决的是“在给定 mandate、风险预算和约束下，一个信号应该变成多大的仓位”。输入不是“买什么”，而是 mandate、风险预算、硬/软约束、流动性边界、交易成本、压力情景和治理控制；输出是可审计的组合决策，而不是订单。它严格区分目标权重、可执行订单、成交持仓、会计持仓，并在风险输入缺失或过期时默认阻断；换手、价差、冲击、融资成本、借券和压力损失都被纳入决策和归因。默认仅用于分析、模拟和纸面交易，未经明确授权不改变经纪商或账户状态。  
**小实操**：给定一个极简场景：3 只股票、一个等权基线、一个“单票权重不超过 20%”的硬约束、一个“组合波动率目标 10%”的风险预算。让 Skill 输出目标权重和约束校验结果，并明确回答：在当前的波动率估计下，等权基线是否已经违反波动率目标；如果违反，它建议的调整方向是什么，以及这个建议是否触发了任何流动性或换手约束。检查它是否停在“分析/模拟”层面，而不是直接生成订单或声称“已执行”。

### 12.6 研报编写：先确认范围，再动笔，关键数据必须有出处
**Skill**：`equity-research-skill`（主推，个股深度报告）；`market-research-reports-v2`（替代，行业/市场研究）  
**MCP**：无  
**仓库地址**：`equity-research-skill` — `https://github.com/rollingSirius/equity-research-skill`；`market-research-reports-v2` — `https://github.com/kikiyang0129/market-research-reports-v2`，`npx skills add ... --skill market-research-reports-v2 -g -y`  
**介绍**：`equity-research-skill` 把“研究一下某只股票”这类模糊请求转化为一份机构级九章报告：一页速览、业务详情、竞争与护城河、管理层与治理、财务分析、多方法估值、分析师观点汇总、新闻与催化剂、投资结论。核心纪律不是“写得像研报”，而是估值必须至少三种方法交叉验证，所有计算由脚本执行、禁止心算，假设以 JSON 留档，同一组数字不会两次给出不同结论；事实与判断分离，每个关键数据标注来源和时间，缺失数据如实标注“未获取到”。`market-research-reports-v2` 更偏行业/市场研究，防幻觉规则包括：所有关键数据必须包含来源链接、发布日期和机构名称；无支撑的数据不得编造，标记为“待验证”；事实、估计、判断、假设分开；投资结论必须包含反方论据和风险，且默认不提供直接买卖建议。  
**小实操**：用 `equity-research-skill` 研究一只你熟悉的美股或 A 股，但要求它只输出“一页速览 + 财务分析 + 估值方法清单”三部分，暂不生成完整九章。检查：一页速览中的每个关键数字是否有来源和时间戳；估值方法清单是否列出了至少三种方法以及每种方法所需的关键假设；如果某个数据源不可用，它是否标注了降级路径或“未获取到”，而不是悄悄跳过。然后换 `market-research-reports-v2` 做一个行业小专题，故意不给它足够的市场规模数据，观察它是否把相关数字标为 `待验证`，而不是编造一个“合理”的百分比。

### 12.7 收束：从选股到研报的完整链路
**Skill**：无（概念收束）  
**MCP**：无  
**仓库地址**：无  
**介绍**：本章链路顺序为选股与组合（12.1）→ 研报解析（12.2）→ 因子挖掘与评估（12.3）→ 风控（12.4/12.5）→ 研报编写（12.6）。判断标准是每个数字和结论能否沿 Skill 留下的路径找到出处、复现计算或说清降级点；选股是在已有因子上做截面排序，因子挖掘是生成新的可评估因子，两者粒度不同但属于同一研究流程。  
**小实操**：任选两个 Skill 对照输出，例如 12.2 重建的因子公式是否在 12.3 中被检查未来函数和可运行性，12.4 的排雷问题卡是否在 12.6 中被引用为风险披露；再用 12.1 排名靠前的一只股票，让 12.3 生成一个“动量”相关候选因子，检查该股票在该因子上的暴露方向是否与 12.1 的动量评分方向一致。若链路断掉，先补交接而不是继续装更多 Skill。

---

## 第13章 AI 命理：从排盘引擎到多术数解读

### 13.1 计算引擎层：八字 + 紫微，算法排盘不靠 LLM 猜
**Skill**：`bazi-ziwei-skill`  
**MCP**：无  
**仓库地址**：`https://github.com/mingze21/bazi-ziwei-skill`；八字对照：`https://github.com/xuemian168/bazi-skill`  
**介绍**：八字四柱、紫微十二宫、大运流年由内置算法计算，不让 LLM 自己排盘，因为纯 LLM 排盘常把日柱、日主、格局算错。提供“八字独立 / 紫微独立 / 综合印证”三种模式，综合印证的核心增量是两套独立体系的结论交叉对账。  
**小实操**：输入出生信息，选择“综合印证”，只要求输出事实层——四柱、紫微命宫与主星、两套体系在“事业方向”上是否一致；不要求解读。检查是否有 `structured_data` 类字段（四柱、宫位、主星、大运起运时间），而不是一段像命理分析的自然语言。

### 13.2 占卜类（一）：六爻 / 梅花，一事一断的确定性起卦
**Skill**：`taibu-divination`（六爻、梅花模块）  
**MCP**：无  
**仓库地址**：`https://github.com/hhszzzz/taibu`；安装：`npx skills add https://github.com/hhszzzz/taibu --skill taibu-divination`  
**介绍**：太卜提供 15 种本地计算引擎，包含六爻、梅花易数、奇门、大六壬、小六壬、太乙、塔罗、西方占星、黄历等；计算引擎随 Skill 打包，本地运行，要求 Node.js 18+。起卦是确定性计算，解读是 LLM 在卦象基础上的生成。  
**小实操**：用数字起卦问“这次合作的结果”，要求输出本卦、互卦、变卦、动爻、体用关系；用同一组数字再跑一次，确认两次卦象完全一致，验证起卦来自脚本而非模型临场“编卦”。

### 13.3 占卜类（二）：奇门遁甲 / 大六壬，时空决策的排盘 JSON
**Skill**：`taibu-divination`（奇门 / 大六壬模块）或 `horosa-agent`  
**MCP**：无  
**仓库地址**：太卜 — `https://github.com/hhszzzz/taibu`；`horosa-agent` — `https://github.com/Horace-Maxwell/horosa-skill`，安装：`npx skills add https://github.com/Horace-Maxwell/horosa-skill --skill horosa-agent`  
**介绍**：奇门和大六壬是“时空决策”类术数，输入需要时间 + 地点 + 具体问题。太卜使用确定性 Python 脚本排盘，以结构化 JSON 输入/输出让 Agent 在解读前能核对时间、历法、规则集和盘面字段；`horosa-agent` 覆盖紫微、大六壬、奇门、太乙、金口诀、三式合一等更广范围。  
**小实操**：对奇门给一个择时问题，要求先输出排盘 JSON（时间、局数、值符值使、九宫字段），确认时间与输入一致、规则集被显式声明，再生成解读；对大六壬检查是否先校时并核实农历转换，再出四课三传。

### 13.4 西方体系：塔罗与占星
**Skill**：`tarot-skill`（塔罗） / `taibu-divination`（占星模块）  
**MCP**：无  
**仓库地址**：`tarot-skill` — `https://github.com/daman-ovo-0404/tarot-skill`；安装：`npx skills add https://github.com/daman-ovo-0404/tarot-skill --skill tarot`；占星可复用 `taibu-divination` 的西方占星引擎  
**介绍**：`tarot-skill` 提供 78 张完整牌义、6 种牌阵、牌间关系理论体系，以及一个密码学安全随机源的 Python 抽牌脚本，支持正逆位概率和 `--seed` 复现；安全设计包括禁用巴纳姆废话清单和自伤信号处理协议。占星侧通过 `taibu-divination` 或专用占星 Skill 输出星盘事实数据。  
**小实操**：塔罗用 `--seed 42` 跑一次三牌阵，记录牌面和正逆位，再用同一 seed 重跑，确认结果完全一致；占星侧只要求输出星盘事实数据（上升、月亮、宫主星、Dasha 顺序），暂不进入完整解读。

### 13.5 综合路由：一个 Skill 覆盖多术数时怎么选
**Skill**：`metaphysics-synthesis-skill` / `fortune-telling-skill`  
**MCP**：无  
**仓库地址**：`metaphysics-synthesis-skill` — `https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill`；`fortune-telling-skill` — `https://github.com/sgxhui111/fortune-telling-skill`  
**介绍**：`metaphysics-synthesis-skill` 覆盖八字、梅花易数、六爻、风水和塔罗的综合解读，带输入契约、脚本和 bounded evidence；`fortune-telling-skill` 是娱乐导向的命理 Skill，把八字、五行、塔罗、星座、流年主题和图片/视频取象结合，并设有医疗/法律/金融重大决策的安全边界。综合路由的价值在于“先选方法，再排盘”，而不是不声不响地选一个术数开始算。  
**小实操**：用同一句模糊问题“最近事业有点卡，想看看方向”分别喂给综合路由和你在 13.2—13.4 中的某一个专项 Skill，观察综合路由是否先追问“短期决策 / 时空择时 / 命盘结构”再选术数。

### 13.6 边界收束：可复现 + 不越界
**Skill**：本章全部；参照 `tarot-skill` 的安全边界 + 各排盘 Skill 的计算约束  
**MCP**：无  
**仓库地址**：同 13.1—13.5  
**介绍**：不引入新 Skill，而是把全章的验证标准收束成两条。第一条是可复现：排盘/起卦必须有脚本输出、可核对字段、可重复的结果；第二条是不越界：解读层必须自带边界声明，`tarot-skill` 的“禁用巴纳姆废话 + 自伤信号处理协议”和 `fortune-telling-skill` 的安全边界是可直接借鉴的模板。  
**小实操**：任选一个跑通的命理 Skill，检查输出是否同时满足：(a) 包含排盘/起卦的事实字段（四柱 / 卦象 / 排盘 JSON / 塔罗 seed）；(b) 包含显式边界声明或高风险话题处理规则。只有 (a) 没有 (b) 是“算得准但不敢用”；只有 (b) 没有 (a) 是“话说得漂亮但不可验证”。

---

## 第14章 结语：边界与判断力

### 14.1 Skill 不能替你做的事
**Skill**：`grill-me`（需求澄清的反面参照）+ 第12、13章领域 Skill  
**MCP**：无  
**仓库地址**：`grill-me` — `https://github.com/mattpocock/skills`（`skills/productivity/grill-me`）；安装：`npx skills add mattpocock/skills --skill grill-me`；Codex 适配 fork：`https://github.com/chaseai-yt/grill-me-codex`  
**介绍**：`grill-me` 逼你想清楚需求，但它不能替你想；因子是否有经济逻辑、命理解读是否越界，Skill 无法替你回答。这一节用这些 Skill 作为反面镜子，让读者把前面十三章建立的“Skill 能力感”收敛回“判断力仍然在你手里”。  
**小实操**：用 `grill-me` 对一个真实任务做需求追问，统计有多少问题是你此前未想清楚的。如果有，说明这个 Skill 的价值是“暴露盲区”，而不是“给出答案”。然后把这个问题带回到第12章或第13章的领域判断上。

### 14.2 从使用 Skill 到设计自己的 SOP
**Skill**：回到 `skill-creator`（内置）  
**MCP**：无  
**仓库地址**：Codex 内置，直接 `$skill-creator` 调用  
**介绍**：第1章用 `skill-creator` 是为了理解机制；到这里，读者已经走过了十二个场景，有了“什么工作流值得固化”的直觉。收束原则：一个 Skill 只做一件事，描述前载触发词，装上大量技能之前先确认每一个都有明确的触发边界。  
**小实操**：从日常中挑一个反复出现的 SOP（例如“CSV 列名 / 空值率 / 异常值分布检查”），用 `$skill-creator` 生成骨架，手动把 `description` 收紧到一句话，删掉 `scripts/` 中不必要的部分，再用隐式提示测试它是否按预期触发。
