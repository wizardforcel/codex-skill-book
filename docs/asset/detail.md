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

**Skill**：`skill-installer`（内置） + `create-plan`
**MCP**：无
**仓库地址**：`create-plan` 位于 `https://github.com/ComposioHQ/awesome-codex-skills`（`create-plan` 子目录）；通过 `$skill-installer` 按名安装
**介绍**：`skill-installer` 可从官方精选列表或任意 GitHub 仓库安装技能；`create-plan` 足够简单，但会在第4章开发软件时正式展开，作为贯穿全书的“种子技能”。
**小实操**：对 `create-plan` 说“给命令行工具加一个 `--dry-run` 选项”，确认它先追问输入输出边界和验收条件，而不是直接写代码。

### 1.8 MCP 与 Skill 的分工

**Skill**：无（概念节）
**MCP**：`~/.codex/config.toml` 中的 `[mcp_servers.<id>]` 配置结构
**仓库地址**：无（本节不引入具体 MCP）
**介绍**：Codex 的 MCP 服务器声明在 host-global 的 `~/.codex/config.toml` 中，stdio 服务器用 `command` + `args`，远程服务器用 `url`。本节建立全书反复使用的分工认知：**MCP 把外部工具“连上”，Skill 决定“怎么用”** 。
**小实操**：手工添加一个指向 `echo` 的 stdio 配置块，重启 Codex 后 `codex mcp list` 确认它出现在服务器列表中。

### 1.9 安装第一个 MCP：Chrome DevTools

**Skill**：无（MCP 安装）
**MCP**：`chrome-devtools-mcp`
**仓库地址**：`https://github.com/ChromeDevTools/chrome-devtools-mcp`
**介绍**：Chrome DevTools MCP 让 Codex 连接真实浏览器，打开页面、读取 DOM、截图、跑 Lighthouse 审计。安装：`codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest`。
**小实操**：让 Codex 打开 `https://example.com` 并读取 `<h1>`，确认返回 “Example Domain” 之类的结构化结果，而不是让你自己去浏览器里看。


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


## 第4章 开发软件

### 4.1 从需求到 TDD 的完整链路

**Skill**：`superpowers`
**MCP**：无
**仓库地址**：`https://github.com/obra/superpowers`；安装：`git clone https://github.com/obra/superpowers.git ~/.codex/superpowers`，并通过 symlink 接入 `~/.agents/skills/`
**介绍**：把“头脑风暴 → 设计确认 → 写实现计划 → TDD（红-绿-重构）→ 审查 → 收尾”固化成 Codex 必须遵循的工程管线，核心是用流程约束替代“上来就猛写”。
**小实操**：对一个最小功能（例如“给函数加参数校验”）触发 `superpowers`，观察它是否先进入 brainstorming 追问边界条件，确认设计后再写一个会失败的测试，然后才写实现。

### 4.2 轻量按需组合：hl 系列

**Skill**：`hl-skills`（`hl-tdd` / `hl-debug` / `hl-code-review`）
**MCP**：无
**仓库地址**：`https://github.com/HugoLopes45/hl-skills`
**介绍**：包含 27 个 Evidence-first Skill，允许按环节单独调用：`hl-debug` 强制先定位根因再改代码，`hl-code-review` 针对分支做 bug 和回归审查，适合不想一次性引入整套 `superpowers` 的读者。
**小实操**：故意制造一个失败测试，用 `hl-debug` 触发，观察它的第一步是读取测试输出并做根因分析，还是直接尝试修改代码。

### 4.3 开发阶段的浏览器验证：Chrome DevTools MCP

**Skill**：4.1 或 4.2 的验证环节（编排层）
**MCP**：`chrome-devtools-mcp`
**仓库地址**：`https://github.com/ChromeDevTools/chrome-devtools-mcp`
**介绍**：让 Codex 在开发过程中直接连接浏览器做实时调试、模拟响应式布局、跑 Lighthouse 审计。与第7章 RPA 的区别在于，这里聚焦“代码 → 浏览器验证”的开发内环，而不是流程自动化。
**小实操**：对本地开发页面让 Codex 通过 MCP“切到 375×667，检查是否有横向溢出”，观察返回的是具体溢出元素和宽度数值，而不是“看起来没问题”。

### 4.4 CI 红灯的自动排查

**Skill**：`gh-fix-ci`
**MCP**：无
**仓库地址**：`https://github.com/openai/skills`；通过 `$skill-installer gh-fix-ci` 安装
**介绍**：使用 `gh` 检查 GitHub Actions 日志、区分“真实失败”和“环境噪声”、总结根因并草拟修复计划，用户确认后再实施。它把 CI 排查这个高频琐碎环节变成 Codex 可以独立走通的标准动作。
**小实操**：在有失败 CI 的示例仓库上触发，确认输出引用具体失败步骤和关键日志行，并给出真实/噪声分类，而不是只说“CI 失败了，我来改”。


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


## 第7章 RPA

### 7.1 浏览器 MCP 的选择：Chrome 还是 Firefox

**Skill**：无（MCP 选型）
**MCP**：`chrome-devtools-mcp` / `firefox-devtools-mcp`
**仓库地址**：Chrome — `https://github.com/ChromeDevTools/chrome-devtools-mcp`；Firefox — `https://github.com/mozilla/firefox-devtools-mcp`
**介绍**：Chrome MCP 偏“开发调试 + 质量审计”，Firefox MCP 基于 WebDriver BiDi，支持 `--headless` 和 `--viewport` 参数。两者都写进 `~/.codex/config.toml`，不冲突。浏览器 MCP 应使用专用 profile，避免接触日常浏览器中的 cookie 和已保存会话。
**小实操**：分别用两个 MCP 打开同一页面读取 `<title>`，比较返回时间和是否需要额外参数，感受 Chrome 的开箱即用与 Firefox 的显式配置差异。

### 7.2 浏览器自动化的 Skill 编排

**Skill**：`realbrowser`（编排层）
**MCP**：Chrome / Firefox MCP（执行层）
**仓库地址**：`https://github.com/darkamenosa/realbrowser`；安装：`git clone https://github.com/darkamenosa/realbrowser ~/.codex/skills/realbrowser`，使用 `agents/openai.yaml` 配置
**介绍**：MCP 提供“打开、点击、填表、截图”的原子能力，Skill 负责编排成“启动 → 定位 → 填写 → 提交 → 校验 → 重试”的固定步骤。核心产出不是“跑通一次”，而是把一次跑通固化成可重复的 Skill。
**小实操**：对一个搜索框 + 结果列表的公开页面，让 Skill 编排“输入 `codex skill`、提交、读取前 3 条标题”，重点观察提交后是否显式校验结果列表非空。

### 7.3 桌面自动化：Windows-MCP

**Skill**：无（MCP 单独跑通）
**MCP**：`Windows-MCP`
**仓库地址**：`https://github.com/CursorTouch/Windows-MCP`；PyPI：`windows-mcp`，支持 `uvx windows-mcp serve`
**介绍**：轻量开源的 MCP server，让 AI Agent 与 Windows 操作系统集成，支持文件导航、应用控制、UI 交互和窗口操作。在 `~/.codex/config.toml` 中添加 `[mcp_servers.windows-mcp]`，`command = "uvx"`，`args = ["windows-mcp", "serve"]`。桌面自动化权限远大于浏览器自动化，必须限制在隔离环境或明确授权的应用上。
**小实操**：让 Codex 通过 Windows-MCP 在桌面创建 `codex-rpa-test` 文件夹并写入 `result.txt`，手动去桌面确认文件真实存在，而不仅仅是 MCP 返回“成功”。

### 7.4 跨浏览器 + 桌面的混合流程

**Skill**：Skill 编排层（跨段校验）
**MCP**：Chrome MCP（浏览器段）+ Windows-MCP（桌面段）
**仓库地址**：同 7.1 和 7.3
**介绍**：每个 MCP 只负责自己那一段，跨段编排才是 Skill 的工作。这个实操的全部价值在于让读者看到：**MCP 各自跑通不等于流程跑通，跨段校验才是编排**。
**小实操**：Chrome MCP 读取 `example.com` 的 `<h1>`，Windows-MCP 写入桌面 `example-h1.txt`，Skill 校验文件内容与页面标题是否一致；不一致时输出差异。


## 第8章 编写论文

### 8.1 中文优先的学术写作与学位论文

**Skill**：`research-writing-skill`
**MCP**：无
**仓库地址**：`https://github.com/Norman-bury/research-writing-skill`；安装：`git clone https://github.com/Norman-bury/research-writing-skill.git ~/.codex/research-writing-skill`
**介绍**：中文优先的学术写作 Skill，覆盖头脑风暴、章节写作、文献综述、Python 图表和 LaTeX 输出，支持“帮我写毕业论文”这类隐式触发。它的价值在于把中文学术写作的规范内置到生成过程中，而不是先出英文再翻译。
**小实操**：给出“帮我写一篇深度学习图像分割的毕业论文引言，约 500 字”，观察它是否先追问论文类型、学科、研究背景、方法，而不是直接生成一段泛泛的引言。

### 8.2 数学建模竞赛论文的模板与检查

**Skill**：`mathmodel-latex-skill`
**MCP**：无
**仓库地址**：`https://github.com/wangling-miao/mathmodel-latex-skill`（v1.0.8）
**介绍**：面向 MCM/ICM、CUMCM 的 LaTeX 论文 Skill，解决竞赛特有的“格式合规 + 交付安全”问题，包含 LaTeX 编译预检、匿名检查、引用/关键词校验和 CUMCM 优秀论文风格规则。
**小实操**：生成空的竞赛论文模板，故意留一个 `\cite{missing}`，执行引用检查，确认它报出未定义引用，而不是让 PDF 编译静默通过。

### 8.3 从零生成骨架与可编译初稿

**Skill**：`academic-researcher` / `research-writing-skill`
**MCP**：无
**仓库地址**：`academic-researcher` — `npx skills add academic-researcher-skill --skill academic-researcher`（安装前建议在 npm / GitHub 确认最新状态）；`research-writing-skill` 同 8.1
**介绍**：端到端链路：研究主题 → 章节骨架 → 引用格式 → LaTeX 输出。重点观察骨架是否有论证层次的递进，以及 `.tex` 是否能无错误编译。
**小实操**：给定“基于图神经网络的推荐系统”，要求输出三级标题 + 每节预期字数的骨架，并生成一个可直接 `pdflatex` 编译的最小 `.tex`；检查骨架有层次、`.tex` 无错误编译。


## 第9章 运营自媒体

### 9.1 公众号从选题到草稿箱

**Skill**：`publish-gzh`
**MCP**：无
**仓库地址**：`https://github.com/AnziBai/codex-skills`，Skill 位于 `skills/publish-gzh`；安装：克隆后运行 `powershell -NoProfile -ExecutionPolicy Bypass -File ".\skills\publish-gzh\scripts\register-local-skill.ps1" -Json`
**介绍**：覆盖公众号的完整生产链：选题、来源约束、中文写作、独立审稿、可选语义配图、确定性校验，最终进入草稿箱。设计重点是把“审稿”作为独立环节，而不是写作的附属。
**小实操**：给具体选题“Codex Skill 和 MCP 的区别”，观察它写作前是否先输出来源清单或事实约束，而不是直接开始写正文。

### 9.2 跨平台草稿生成与上传

**Skill**：`filler`
**MCP**：无（底层用 Playwright）
**仓库地址**：`https://github.com/AnziBai/codex-skills`，Skill 位于 `skills/filler`；安装：`.\skills\filler\scripts\filler.ps1 setup-draft-fill -Json`
**介绍**：把已完成作品转成平台发布草稿：AI 写标题文案，CLI 校验素材，Playwright 自动上传到小红书、抖音、视频号的草稿箱。与 `publish-gzh` 互补：一个负责“从无到有写公众号”，一个负责“把已有内容适配到多平台草稿箱”。
**小实操**：把 9.1 的文章交给 `filler` 生成小红书版本，只到“草稿箱生成”为止，不实际发布；检查它是否为小红书做了标题长度、分段和话题标签适配，而不是原样搬运。

### 9.3 图文视觉物料的生成

**Skill**：`guizang-social-card-skill`
**MCP**：无
**仓库地址**：`https://github.com/op7418/guizang-social-card-skill`；安装：`npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill`
**介绍**：从小红书图文组图到公众号封面对，把“找图”变成“按内容生成匹配的视觉物料”。对于不擅长设计的初学者，它降低了封面和组图的门槛；对于已经产出内容的读者，它是发布前最后一块拼图。
**小实操**：用 9.1 的标题和摘要生成 3 张小红书图文卡片，检查卡片与内容主题相关，而不是套用一个通用模板。


## 第10章 基本面选股与因子挖掘

### 10.1 A 股多因子选股与组合构建

**Skill**：`stockaskill`
**MCP**：无
**仓库地址**：`https://github.com/axjing/stockaskill`；安装到 `.agents/skills/stockaskill/` 或 `~/.agents/skills/stockaskill/`，也可 `npx skills add axjing/stockaskill`
**介绍**：基于 AKShare + SQLite 缓存，做多因子评分、排名和组合构建，覆盖价值、质量、成长、动量、低波、规模等维度。定位是可审计的研究流程，不是投资建议；数据质量判断、因子经济逻辑和风控决策仍然由读者承担。
**小实操**：运行 `python stockaskill/scripts/run.py scan A --top 10`，让 Skill 解释第一名在价值、质量、成长、动量各维度的分数和数据报告期，验证评分可逐维度追溯，而不是一个黑箱总分。

### 10.2 辩论式因子挖掘与评估

**Skill**：`skill-factormad-debate-factor-mining`
**MCP**：无
**仓库地址**：`https://github.com/quantskills/skill-factormad-debate-factor-mining`（安装前建议在 GitHub 确认仓库可访问性）
**介绍**：从日频 OHLCV 或时点一致的面板数据生成代码型 Alpha 因子，做代码检查和轻量 IC、RankIC、ICIR 评估，输出可审计 JSON。核心不是“多了一个因子库”，而是把“提出假设 → 生成代码 → 评估 → 归档”变成可辩论、可审计的流程。
**小实操**：在一小段样例日频数据上运行一次，要求输出候选因子的表达式、评估代码、IC/RankIC 数值和 JSON 归档路径；重点检查另一个人能否用同样的数据复现这个因子。

### 10.3 从选股到因子研究的粒度切换

**Skill**：`stockaskill` → `skill-factormad-debate-factor-mining`
**MCP**：无
**仓库地址**：同 10.1 和 10.2
**介绍**：选股是“在已有因子上做截面排序”，因子挖掘是“生成新的可评估因子”，两者粒度不同。交叉验证的价值在于让读者看到，选股和因子研究不是两个孤立章节，而是同一个研究流程的不同粒度。
**小实操**：用 10.1 中排名靠前的一只股票，让因子 Skill 生成一个“动量”相关候选因子，检查该股票在该因子上的暴露方向是否与 10.1 的动量评分方向一致。


## 第11章 AI 命理：从排盘引擎到多术数解读

### 11.1 计算引擎层：八字 + 紫微，算法排盘不靠 LLM 猜

**Skill**：`bazi-ziwei-skill`
**MCP**：无
**仓库地址**：`https://github.com/mingze21/bazi-ziwei-skill`；八字对照：`https://github.com/xuemian168/bazi-skill`
**介绍**：八字四柱、紫微十二宫、大运流年由内置算法计算，不让 LLM 自己排盘，因为纯 LLM 排盘常把日柱、日主、格局算错。提供“八字独立 / 紫微独立 / 综合印证”三种模式，综合印证的核心增量是两套独立体系的结论交叉对账。
**小实操**：输入出生信息，选择“综合印证”，只要求输出事实层——四柱、紫微命宫与主星、两套体系在“事业方向”上是否一致；不要求解读。检查是否有 `structured_data` 类字段（四柱、宫位、主星、大运起运时间），而不是一段像命理分析的自然语言。

### 11.2 占卜类（一）：六爻 / 梅花，一事一断的确定性起卦

**Skill**：`taibu-divination`（六爻、梅花模块）
**MCP**：无
**仓库地址**：`https://github.com/hhszzzz/taibu`；安装：`npx skills add https://github.com/hhszzzz/taibu --skill taibu-divination`
**介绍**：太卜提供 15 种本地计算引擎，包含六爻、梅花易数、奇门、大六壬、小六壬、太乙、塔罗、西方占星、黄历等；计算引擎随 Skill 打包，本地运行，要求 Node.js 18+。起卦是确定性计算，解读是 LLM 在卦象基础上的生成。
**小实操**：用数字起卦问“这次合作的结果”，要求输出本卦、互卦、变卦、动爻、体用关系；用同一组数字再跑一次，确认两次卦象完全一致，验证起卦来自脚本而非模型临场“编卦”。

### 11.3 占卜类（二）：奇门遁甲 / 大六壬，时空决策的排盘 JSON

**Skill**：`taibu-divination`（奇门 / 大六壬模块）或 `horosa-agent`
**MCP**：无
**仓库地址**：太卜 — `https://github.com/hhszzzz/taibu`；`horosa-agent` — `https://github.com/Horace-Maxwell/horosa-skill`，安装：`npx skills add https://github.com/Horace-Maxwell/horosa-skill --skill horosa-agent`
**介绍**：奇门和大六壬是“时空决策”类术数，输入需要时间 + 地点 + 具体问题。太卜使用确定性 Python 脚本排盘，以结构化 JSON 输入/输出让 Agent 在解读前能核对时间、历法、规则集和盘面字段；`horosa-agent` 覆盖紫微、大六壬、奇门、太乙、金口诀、三式合一等更广范围。
**小实操**：对奇门给一个择时问题，要求先输出排盘 JSON（时间、局数、值符值使、九宫字段），确认时间与输入一致、规则集被显式声明，再生成解读；对大六壬检查是否先校时并核实农历转换，再出四课三传。

### 11.4 西方体系：塔罗与占星

**Skill**：`tarot-skill`（塔罗） / `taibu-divination`（占星模块）
**MCP**：无
**仓库地址**：`tarot-skill` — `https://github.com/daman-ovo-0404/tarot-skill`；安装：`npx skills add https://github.com/daman-ovo-0404/tarot-skill --skill tarot`；占星可复用 `taibu-divination` 的西方占星引擎
**介绍**：`tarot-skill` 提供 78 张完整牌义、6 种牌阵、牌间关系理论体系，以及一个密码学安全随机源的 Python 抽牌脚本，支持正逆位概率和 `--seed` 复现；安全设计包括禁用巴纳姆废话清单和自伤信号处理协议。占星侧通过 `taibu-divination` 或专用占星 Skill 输出星盘事实数据。
**小实操**：塔罗用 `--seed 42` 跑一次三牌阵，记录牌面和正逆位，再用同一 seed 重跑，确认结果完全一致；占星侧只要求输出星盘事实数据（上升、月亮、宫主星、Dasha 顺序），暂不进入完整解读。

### 11.5 综合路由：一个 Skill 覆盖多术数时怎么选

**Skill**：`metaphysics-synthesis-skill` / `fortune-telling-skill`
**MCP**：无
**仓库地址**：`metaphysics-synthesis-skill` — `https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill`；`fortune-telling-skill` — `https://github.com/sgxhui111/fortune-telling-skill`
**介绍**：`metaphysics-synthesis-skill` 覆盖八字、梅花易数、六爻、风水和塔罗的综合解读，带输入契约、脚本和 bounded evidence；`fortune-telling-skill` 是娱乐导向的命理 Skill，把八字、五行、塔罗、星座、流年主题和图片/视频取象结合，并设有医疗/法律/金融重大决策的安全边界。综合路由的价值在于“先选方法，再排盘”，而不是不声不响地选一个术数开始算。
**小实操**：用同一句模糊问题“最近事业有点卡，想看看方向”分别喂给综合路由和你在 11.2—11.4 中的某一个专项 Skill，观察综合路由是否先追问“短期决策 / 时空择时 / 命盘结构”再选术数。

### 11.6 边界收束：可复现 + 不越界

**Skill**：本章全部；参照 `tarot-skill` 的安全边界 + 各排盘 Skill 的计算约束
**MCP**：无
**仓库地址**：同 11.1—11.5
**介绍**：不引入新 Skill，而是把全章的验证标准收束成两条。第一条是**可复现**：排盘/起卦必须有脚本输出、可核对字段、可重复的结果；第二条是**不越界**：解读层必须自带边界声明，`tarot-skill` 的“禁用巴纳姆废话 + 自伤信号处理协议”和 `fortune-telling-skill` 的安全边界是可直接借鉴的模板。
**小实操**：任选一个跑通的命理 Skill，检查输出是否同时满足：**(a)** 包含排盘/起卦的事实字段（四柱 / 卦象 / 排盘 JSON / 塔罗 seed）；**(b)** 包含显式边界声明或高风险话题处理规则。只有 (a) 没有 (b) 是“算得准但不敢用”；只有 (b) 没有 (a) 是“话说得漂亮但不可验证”。


## 第12章 结语：边界与判断力

### 12.1 Skill 不能替你做的事

**Skill**：`grill-me`（需求澄清的反面参照）+ 第10、11章领域 Skill
**MCP**：无
**仓库地址**：`grill-me` — `https://github.com/mattpocock/skills`（`skills/productivity/grill-me`）；安装：`npx skills add mattpocock/skills --skill grill-me`；Codex 适配 fork：`https://github.com/chaseai-yt/grill-me-codex`
**介绍**：`grill-me` 逼你想清楚需求，但它不能替你想；因子是否有经济逻辑、命理解读是否越界，Skill 无法替你回答。这一节用这些 Skill 作为反面镜子，让读者把前面十一章建立的“Skill 能力感”收敛回“判断力仍然在你手里”。
**小实操**：用 `grill-me` 对一个真实任务做需求追问，统计有多少问题是你此前未想清楚的。如果有，说明这个 Skill 的价值是“暴露盲区”，而不是“给出答案”。然后把这个问题带回到第10章或第11章的领域判断上。

### 12.2 从使用 Skill 到设计自己的 SOP

**Skill**：回到 `skill-creator`（内置）
**MCP**：无
**仓库地址**：Codex 内置，直接 `$skill-creator` 调用
**介绍**：第1章用 `skill-creator` 是为了理解机制；到这里，读者已经走过了十一个场景，有了“什么工作流值得固化”的直觉。收束原则：一个 Skill 只做一件事，描述前载触发词，装上大量技能之前先确认每一个都有明确的触发边界。
**小实操**：从日常中挑一个反复出现的 SOP（例如“CSV 列名 / 空值率 / 异常值分布检查”），用 `$skill-creator` 生成骨架，手动把 `description` 收紧到一句话，删掉 `scripts/` 中不必要的部分，再用隐式提示测试它是否按预期触发。