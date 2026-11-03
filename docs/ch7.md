# 第7章 RPA

RPA 不是“让 AI 替你乱点鼠标”，而是把一条可以重复的操作流程固定下来：启动、定位、填写、提交、校验、失败时重试。浏览器自动化和桌面自动化要分开看：浏览器 MCP 只接触网页，桌面 MCP 能碰文件、窗口和系统应用，后者权限更大，也更需要隔离环境和明确授权。RPA 不是让 AI 替你把所有事情一口气做完，而是把一条可重复的流程固定下来；这一章就围绕浏览器和桌面两段展开，最后再合起来看。

## 7.1 浏览器 MCP 的选择：Chrome 还是 Firefox

### 简介

Chrome DevTools MCP 偏开发调试和质量审计：打开页面、读 DOM、跑脚本、检查网络、跑 Lighthouse。Firefox DevTools MCP 基于 WebDriver BiDi，除了页面交互，也强调 Firefox 的调试模块、独立 profile、headless 和 viewport 参数。两者可以同时配置，不冲突；选择标准不是“哪个更高级”，而是你正在验证哪个浏览器、需要哪套开发工具。浏览器自动化面前有两个常用选项，选择标准不是哪一个更高级，而是你正在验证哪个浏览器。

两个浏览器 MCP 都应该使用专用 profile，不能接入日常浏览器，因为 MCP 能访问页面、Cookie 和已保存会话。

### 调用记录

**我**：先把 Chrome DevTools MCP 装好。

**Codex**：

```powershell
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

安装后实际用 MCP 打开 `https://example.com`，`new_page` 返回：

```text
1: about:blank
2: Example Domain (https://example.com/) [selected]
```

再用 `evaluate_script` 读取页面：

```json
{"title":"Example Domain","url":"https://example.com/","ready":"complete","h1Count":0,"h1Text":null}
```

Chrome 这一条链已经真实跑通；实际页面有标题，但没有 `<h1>`，所以不能把标题伪装成 H1。

**我**：Firefox 怎么装？

**Codex**：Firefox MCP 的 Codex 配置命令是：

```powershell
codex mcp add firefox-devtools -- npx @mozilla/firefox-devtools-mcp@latest
```

真实执行后，`codex mcp list` 同时显示：

```text
chrome-devtools   npx chrome-devtools-mcp@latest             enabled
firefox-devtools  npx @mozilla/firefox-devtools-mcp@latest   enabled
```

本机 Firefox 也确实存在：

```text
C:\Program Files\Mozilla Firefox\firefox.exe
```

**我**：Firefox MCP 和 Chrome 有什么特别不同？

**Codex**：Firefox 的 CLI 帮助里直接列出了这些参数：

```text
--firefoxPath       指定 Firefox 可执行文件
--headless          无界面启动
--viewport 1280x720 初始窗口尺寸
--profilePath       指定独立 profile
--toolPreset        slim / basic / developer / mozilla / all
--tools             显式选择 pages/network/script 等模块
```

最小的 headless 配置可以写成：

```powershell
codex mcp add firefox-devtools -- npx @mozilla/firefox-devtools-mcp@latest -- --headless --viewport 1280x720
```

`basic` 默认包含 `evaluate_script`；`developer` 会加入调试、网络、控制台和 profiler；`slim` 会删掉脚本能力。Firefox README 还特别提醒：Firefox MCP 只能在本地浏览器运行，不能直接放到云端浏览器里。

**我**：什么时候选 Chrome，什么时候选 Firefox？

**Codex**：

| 需求 | 选择 |
|---|---|
| 开发 Chrome 页面、Lighthouse、Chrome DevTools 网络/性能工具 | Chrome DevTools MCP |
| 验证 Firefox 兼容性、WebDriver BiDi、headless/viewport | Firefox DevTools MCP |
| 只读 DOM 与截图 | 两者都可以，优先项目实际浏览器 |
| 需要调试/网络/控制台 | 选择对应浏览器的 developer 工具 preset |

无论选哪一个，都要专用 profile、限制访问站点，并警惕网页返回的 prompt injection。

把这一节放回整条链路里看，它只是其中一段；真正动手时不必追求一次全对，先把命令跑通、把输出对上，遇到报错再回来查对应位置，往往比从头读一遍更快。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- Chrome MCP 偏 Chrome DevTools 开发与审计；Firefox MCP 偏 WebDriver BiDi 与 Firefox 兼容性验证。
- Chrome 已实际打开 `example.com`；Firefox 已实际加入 Codex MCP 配置并发现本机 Firefox。
- Firefox 的 `--headless`、`--viewport`、`--profilePath` 和 `--tool-preset` 适合自动化测试环境。
- 两者都不要连接日常浏览器 profile，浏览器自动化天然能接触 Cookie 和已保存会话。
- 自动化不是“点了按钮”，必须有显式成功条件；realbrowser 用 `wait ready` 和结果非空校验保证这一点。

## 7.2 浏览器自动化的 Skill 编排

### 简介

浏览器 MCP 提供的是“打开、点击、填表、截图”这些原子能力；真正把一次操作变成固定流程的是编排 Skill。`realbrowser` 就是一个 target-first 的浏览器自动化 Skill：先创建/取得一个标签页目标，之后的读取、动作、等待、截图、网络抓取都通过同一个 `-t <label>` 目标句柄来做。它的核心产出不是“跑通一次”，而是把一套“启动 → 定位 → 填写 → 提交 → 校验 → 重试”的步骤固化下来。MCP 给的是原子能力，Skill 给的是流程；真正可持续的自动化，是后者把前者串成带成功条件的固定步骤。

### 调用记录

**我**：realbrowser 怎么装？

**Codex**：Claude Code 用插件市场，Codex 则把仓库放到 `$HOME/.codex/skills/realbrowser`，使用 `agents/openai.yaml` 配置。它的 CLI 是零依赖 Node 脚本，先看帮助：

```powershell
node ...\scripts\realbrowser.mjs help
```

帮助明确给出 target-first 模型，所有读/动作都必须带 `-t`：

```text
tab ensure/select/new returns a stable suggested target.
every read/action/debug command requires -t/--target or --handle.
```

**我**：先在匿名会话里打开 example.com。

**Codex**：真实执行：

```powershell
$RB = "C:\Users\Administrator\AppData\Local\Temp\ch7\rb\skills\realbrowser\scripts\realbrowser.mjs"
node $RB tab ensure https://example.com --anonymous --session check --label page --background
# created page https://example.com
# task-tab origin=https://example.com label=page target=B9D01BF9 status=active
# next: realbrowser read observe -t page

node $RB read observe -t page --anonymous --session check
# target page Example Domain
# https://example.com/
# ready=complete visibility=visible focus=true
# controls: Learn more
# 页面正文：...Example Domain 多语言说明...
```

“target-first”体现在流程上：先有稳定标签 `page`，后面的读取都通过 `-t page`，而不是每次重新定位。

**我**：对一个搜索框 + 结果列表的页面，编排步骤是什么？

**Codex**：realbrowser 的 `SKILL.md` 明确要求先读页面再选择器，不能把站点名或按钮文案硬编码进工作流。一次搜索流程的最小骨架：

```text
1. tab ensure <search homepage> --label app --background
2. read observe -t app                # 看表单与结果区，拿到 ref/控件
3. action fill / action type -t app   # 填搜索词
4. action submit -t app --text "Search"   # 提交按钮的可见文案
5. wait ready -t app --visual-stable --timeout 30000
6. read item / read observe -t app    # 读结果区
7. 校验结果列表非空，为空则按错误路径重试
```

它不是点了提交就说成功；`SKILL.md` 的守则是“提交后必须等页面稳定、显式校验结果列表非空”。没有这一步，表单报错也会被当作成功。

这些步骤看起来零散，其实前后是有因果的：前一步的产物就是后一步的输入，中间哪一环没对上，后面就会以各种奇怪的方式报错。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- realbrowser 是 target-first：先 `tab ensure` 建目标，之后所有命令用 `-t <label>`。
- 匿名会话 `--anonymous --session check` 提供独立临时状态，不碰日常浏览器。
- 真实运行：创建 `example.com` 标签页，`read observe` 返回 `ready=complete` 与控件列表。
- 搜索流程六步：建目标 → 观察 → 填写 → 提交 → 等待稳定 → 读取并校验结果非空。
- 自动化不是“点了按钮”，必须有显式成功条件；realbrowser 用 `wait ready` 和结果非空校验保证这一点。

## 7.3 桌面自动化：Windows-MCP

### 简介

浏览器 MCP 只操作网页，Windows-MCP 则把 AI Agent 接到 Windows 系统：文件导航、应用控制、窗口操作、键盘鼠标、UI QA，以及浏览器的 UIA/DOM 状态。它的能力边界比浏览器 MCP 更大，所以权限也更敏感：应放在隔离环境或明确授权的应用上，不要让它接触日常桌面里的密钥和私人文件。桌面自动化权限更大，也因此更需要先确认控制权、再动手、最后回读，每一步都该留下证据。

仓库现在支持 Windows 10/11，当前 PyPI 包要求 Python 3.14+、`uv`，可用 `uvx windows-mcp serve` 启动。

### 调用记录

**我**：怎么安装 Windows-MCP？

**Codex**：仓库 README 给出的运行方式是：

```powershell
uvx windows-mcp serve
```

Codex 配置块使用 stdio：

```toml
[mcp_servers.windows-mcp]
command = "uvx"
args = ["windows-mcp", "serve"]
```

首次启动会安装 `pyproject.toml` 里的依赖，可能需要一两分钟；README 还提醒首次运行超时后重启一次。

**我**：按小实操在桌面创建 `codex-rpa-test/result.txt`。

**Codex**：先读取桌面控制状态：

```json
{"state":"user","generation":56,"wait_seconds":9.99}
```

这表示当前桌面控制权在用户手里。随后调用 Windows-MCP 的文件写工具，真实返回：

```text
USER_CONTROL
```

因此本次没有假装“文件已经创建成功”：Windows-MCP 遵守控制权边界，用户正在操作桌面时拒绝替 Agent 写入。要完成该实操，需要等控制权交给 Agent，再执行写入并用 FileSystem read/list 回读确认；不能只看工具返回“成功”就下结论。

**我**：Windows-MCP 和浏览器 MCP 怎么选？

**Codex**：

```text
Chrome/Firefox MCP → 页面 DOM、标签页、表单、网络、截图、开发者工具
Windows-MCP       → 桌面文件、应用窗口、系统 UI、键盘鼠标、跨应用操作
```

桌面 MCP 的权限更大，优先用 FileSystem 这类窄工具；需要窗口控制时先取状态、确认目标窗口，再点击；所有写入都要回读验证。

**我**：搜索 MCP 能找到 Windows-MCP 的公开使用教程吗？

**Codex**：检索到几条桌面 MCP 的泛化配置教程，例如用本地脚本启动 `mcp-serve`，但它们不是 Windows-MCP 本身。能借鉴的只有通用原则：先确认服务在监听、再确认控制权、最后回读结果。本节的具体命令和 `USER_CONTROL` 行为仍来自仓库 README 与本机实跑。

如果只记住一句，那就是：先让最小链路真实跑通，再谈优化和自动化；跳过验证直接堆功能，最后往往要花更多时间回头补。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- Windows-MCP 的安装入口是 `uvx windows-mcp serve`，当前要求 Python 3.14+ 和 `uv`。
- 它可以操作文件、应用、窗口和 UI，但权限远大于浏览器 MCP。
- 真实测试中，桌面控制状态为 `user` 时，写文件返回 `USER_CONTROL`，操作没有发生。
- 桌面自动化必须先确认控制权、再执行写入、最后回读确认；不能把“调用发出”当成“文件已创建”。

## 7.4 跨浏览器 + 桌面的混合流程

### 简介

跨段 RPA 的关键不是让一个 MCP 包办一切，而是让每个 MCP 只负责自己最擅长的一段，再由 Skill 在段与段之间做校验。浏览器段读取网页，桌面段保存结果，最后比较两边的数据是否一致。MCP 各自跑通不等于流程跑通，跨段校验才是编排。把两段自动化接起来时，最容易被忽略的是段与段之间的数据契约；这一节演示了该在哪一步停下来、什么才算真正的通过。

### 调用记录

**我**：做一个最小混合流程：Chrome 读取 `example.com` 的页面标题，Windows-MCP 写入桌面 `example-h1.txt`，再检查文件内容是否一致。

**Codex**：流程应拆成五步：

```text
1. Chrome MCP new_page("https://example.com")
2. Chrome MCP evaluate_script 读取 document.title / 页面根节点
3. 把读取结果作为下一步的明确输入，不靠模型记忆转述
4. Windows-MCP 在用户授权的桌面目录写入文件
5. Windows-MCP read 回读文件，逐字比较页面值和文件值
```

本机 Chrome 段真实得到：

```json
{"title":"Example Domain","h1Count":0,"h1Text":null}
```

Windows-MCP 段因当前控制状态是 `user`，写入返回 `USER_CONTROL`，所以流程应停在第 4 步并报告阻断，不能宣布“跨段校验通过”。

**我**：如果桌面控制权恢复，什么才算通过？

**Codex**：必须同时满足：文件确实创建、回读成功、内容与 Chrome 返回的值逐字一致。如果 Chrome 返回的是标题，就写标题并比较标题；不能把“页面没有 H1”擅自改成一个伪造的 H1。

本节记录里保留了失败和阻断，不是为了吓人，而是让你知道正常使用中也会遇到这些情况，遇到了照着排查即可，不必怀疑自己。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- 混合流程是“浏览器读取 → 显式传值 → 桌面写入 → 桌面回读 → 比较”。
- 每段由对应 MCP 负责，Skill 负责段间数据契约和失败停止条件。
- 控制权、文件写入、回读和逐字比较都是完成条件。
- 本次真实流程在 Windows-MCP 的 `USER_CONTROL` 阶段停止，证明跨段校验不能用“看起来成功”代替证据。

