# 第5章 逆向软件

逆向是阅读程序“留下的痕迹”来还原它做了什么。对初学者，最容易困住手的两件事是：不知道怎么让 AI 去看反汇编/内存/交叉引用，以及不知道“看得懂代码”算不算完成。这一章讲清楚逆向里的分工：**MCP 负责“连上执行层”**（IDA 给静态结构，x64dbg 给运行时状态），**Skill 负责“决定怎么看、怎么交叉验证、什么时候算完”**。

## 5.1 逆向中 MCP 与 Skill 的分工

### 简介

在逆向场景里，MCP 和 Skill 的分工比写小说更明显。IDA Pro MCP 和 x64dbg MCP 是“执行层”：它们把反汇编、内存、寄存器、断点、交叉引用这些能力暴露成一个个工具调用。`rust-reverse-engineering-skill` 是“编排层”示例：它不自己反汇编，而是规定流程——先做指纹识别、再找 crate 边界、再取伪代码、最后出报告，每一步明确调用哪个 MCP 工具、拿到什么产物、什么条件下进入下一步。

### 调用记录

**我**：为什么逆向要先装两个 MCP 还要一个 Skill？不能直接问吗？

**Codex**：直接问也没用，因为模型自己不会反汇编。IDA MCP 管“这个函数长什么样”，x64dbg MCP 管“运行时它实际做了什么”。Skill 是第三层：它不执行工具，它决定顺序和验收标准。`rust-reverse-engineering-skill` 的 README 自己就是这么定位的：

```text
- Fingerprinting Rust binaries and libraries
- Recovering likely crate boundaries and entry points
- Surfacing panic, unwind, async, and FFI edges
- Producing reviewable artifacts: demangled symbols, disassembly, pseudocode bundles
- Driving a repeatable static and dynamic analysis workflow
```

它服务的是“你拥有的或明确授权评估的二进制”，不是随便一个样本。

**我**：它需要哪些本机工具？

**Codex**：README 里的环境要求分两部分。必须有的：

```text
file、strings、nm 或 llvm-nm
objdump 或 llvm-objdump、readelf 或 llvm-readelf
```

推荐的：`rustfilt`（还原 Rust 符号）、`gdb` 或 `lldb`（动态调试）、Ghidra / IDA Pro / Binary Ninja（反编译器）。

**我**：Codex 怎么装这个编排 Skill？

**Codex**：官方 Codex 插件目录还没开放发布，仓库 `.codex/INSTALL.md` 给的本地安装流程是克隆到 `~/.codex/plugins/rust-reverse-engineering`，再在 `~/.agents/plugins/marketplace.json` 里登记一个指向本地的 marketplace：

```json
{
  "name": "personal-local-plugins",
  "plugins": [
    {
      "name": "rust-reverse-engineering",
      "source": { "source": "local", "path": "./.codex/plugins/rust-reverse-engineering" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" }
    }
  ]
}
```

重启 Codex 后在 `/plugins` 里安装。

**我**：那怎么验证它的“计划”合格？

**Codex**：最简单的方法是让它对样例二进制生成一份分析计划，然后检查计划是否满足三条硬要求：每一步写了要调用哪个 MCP 工具、每一步明确了要拿到什么产物、每一步写明了什么条件下进入下一步。这三项缺一就不是编排，只是罗列工具。后面的 5.2、5.3 会把两条执行层 MCP 分别跑通，作为这份计划的“手”。

### 总结

- 逆向三件套：执行层 MCP（IDA / x64dbg）+ 编排层 Skill。
- MCP 回答“结构/运行时事实”，Skill 回答“先看什么、怎么交叉验证、何时算完成”。
- `rust-reverse-engineering-skill` 的流程是指纹 → crate 边界 → 伪代码 → 可审查报告。
- 本地安装走 `~/.codex/plugins` + `~/.agents/plugins/marketplace.json`。
- 合格的编排计划必须逐条写明：哪个工具、什么产物、进入下一步的条件。

## 5.2 静态分析：IDA Pro MCP

### 简介

`ida-pro-mcp` 通过 `idalib` 提供无头反汇编、反编译、类型分析和交叉引用。Codex 可以通过 `decompile_function`、`list_functions`、`get_xrefs_to` 等工具读取结构化数据，而不是截一张反汇编窗口的图让它“看图说话”。它与 5.3 的 x64dbg MCP 刚好互补：IDA 回答“这个函数长什么样”，x64dbg 回答“运行时它实际做了什么”。

注意一个真实的演进：仓库 README 顶部已经明确推荐改用 Hex-Rays 官方的 IDA MCP Server，原版插件未来会逐步废弃。书里仍然用它做教学，是因为工具接口清晰、安装路径完整；真正长期使用时应优先看官方方案。

### 调用记录

**我**：Codex 这边怎么装？

**Codex**：走 Codex 插件市场，真实执行：

```powershell
codex plugin marketplace add mrexodia/codex-marketplace
# Added marketplace `mrexodia` ...
# Installed marketplace root: C:\Users\Administrator\.codex\.tmp\marketplaces\mrexodia

codex plugin add ida-pro-mcp@mrexodia
# Added plugin `ida-pro-mcp` from marketplace `mrexodia`.
# Installed plugin root: ...\.codex\plugins\cache\mrexodia\ida-pro-mcp\0.1.0
```

再确认状态：

```text
PLUGIN                STATUS              VERSION  SOURCE
ida-pro-mcp@mrexodia  installed, enabled  0.1.0    https://github.com/mrexodia/ida-pro-mcp.git
```

**我**：装好插件就能用了吗？

**Codex**：还差本机 IDA。README 的前置条件是：Python 3.11 以上、安装 `uv`、IDA Pro 8.3 以上（推荐 9），并且 **IDA Free 不支持**。还要把 `idalib` 激活到全局，Windows 上的命令是：

```powershell
uv run "C:\Program Files\IDA Professional 9.3\idalib\python\py-activate-idalib.py"
```

**我**：那我现在的环境能用吗？试一个查询看看。

**Codex**：我调了两个最基本的工具，真实结果是：

```text
check_connection  → MCP server "ida-pro-mcp" tool "check_connection" timed out after 1s
get_metadata      → MCP server "ida-pro-mcp" tool "get_metadata" timed out after 1s
```

这不是工具写错了，而是 MCP 服务器已经注册、但背后没有连上正在运行的 IDA 实例/插件。需要先启动 IDA、完成插件安装（`ida-pro-mcp --install`），再重开 MCP 客户端。这个超时就是“配置成功 ≠ 执行层可用”的最好例子。

**我**：它一共提供哪些工具？

**Codex**：本会话已注册的工具包括：

```text
check_connection / get_metadata
list_functions / list_globals / list_strings / list_imports
get_function_by_name / get_function_by_address
decompile_function / disassemble_function
get_xrefs_to / get_callers / get_callees / get_entry_points
get_defined_structures / analyze_struct_detailed / search_structures
set_comment / rename_function / rename_local_variable
```

这些名字本身就说明了分工：`decompile_function` 给你伪代码，`get_xrefs_to` 给你谁调用了它，`list_functions` 给你函数清单。编排 Skill 就是把这些原子调用串成“指纹 → 边界 → 伪代码 → 报告”。

### 总结

- IDA MCP 的执行层是 `idalib`，前置是 IDA Pro 8.3+（Free 不支持）、Python 3.11+、`uv` 和 `idalib` 激活。
- Codex 安装走 `codex plugin marketplace add` + `codex plugin add`，装完显示 `installed, enabled`。
- 插件装好不等于能用：IDA 实例/插件没连上时，工具会在 1 秒内超时。
- 核心工具是 `decompile_function`、`list_functions`、`get_xrefs_to`、`get_callers/callees`。
- README 已推荐改用 Hex-Rays 官方 IDA MCP Server，长期使用应以官方方案为准。

## 5.3 动态调试：x64dbg MCP

### 简介

`x64dbg-mcp` 也是两层桥接：x64dbg 原生插件暴露调试器状态、内存、寄存器、断点；MCP 客户端通过 HTTP/SSE 连上来，让 Codex 用工具调用动态调试。它和 5.2 的对照很直接：IDA MCP 回答“这个函数长什么样”，x64dbg MCP 回答“运行时它实际做了什么”。

仓库 `duty1g/x64dbg-mcp-server` 用 Zig 写成单文件插件，把 `dist/` 复制进 x64dbg 根目录后，启动 x64dbg 服务就会自动开始监听。默认端口：x64 是 `9094`，x32 是 `9095`，并且强制 Bearer Token 认证。

### 调用记录

**我**：本机装了 x64dbg，也有这个 MCP 插件吗？

**Codex**：有。`D:\Program Files\x64dbg\release\x64\x64dbg.exe` 存在，`plugins` 目录里已经有：

```text
x64dbg-MCP-Server.dp64
```

同目录的 `mcp_config.json` 记录监听地址、端口和 `AuthToken`（下面是脱敏后的字段名，不展示真实 token）：

```json
{ "IpAddress": "127.0.0.1", "Port": 9094, "AutoStart": true, "AuthToken": "<已脱敏>" }
```

**我**：怎么确认服务真的起来了？

**Codex**：先裸访问端口，得到 `401`，说明服务在监听、只是缺认证：

```text
curl http://127.0.0.1:9094/  →  HTTP 401
```

带上 `Authorization: Bearer <token>` 后用 MCP 客户端连接，`tools/list` 返回了 **80 个工具**（README 写的是 84，版本之间有差异，以实际返回为准）。节选：

```text
GetDebugState        LoadBinary          AttachProcess
WaitForPause         GetAllRegisters     Disassemble
SetBreakpoint        run                 StepInto / StepOver
ReadMemory           GetCallStack        ListModules
FindPattern          GetReferences       DumpModule
```

**我**：那我先查一下现在调试器在什么状态。

**Codex**：按技能的第一条规则，任何动作之前先 `GetDebugState`。真实返回：

```text
isDebugging: false
status: NO_TARGET
hint: Use LoadBinary to open an executable first.
```

这时如果直接调别的工具，会被明确拒绝：

```text
GetCurrentAddress → ERROR: Tool requires an active debug session.
Disassemble       → ERROR: Tool requires an active debug session.
```

这就是 x64dbg MCP 的 SKILL.md 反复强调的“先知道状态”：`NO_TARGET` 下不能读内存、不能反汇编，必须先 `LoadBinary` 或 `AttachProcess`。

**我**：加载之后标准动作是什么？

**Codex**：技能给出的标准链是：

```text
GetDebugState → LoadBinary (path) → WaitForPause
→ GetDebugState（确认 PAUSED）→ GetAllRegisters → ListModules → Disassemble
```

下断点则是：

```text
GetDebugState → SetBreakpoint (target) → run
→ WaitForPause / WaitForEvent → GetDebugState → Disassemble → GetAllRegisters
```

技能里还有一条“绝不假设两次调用之间状态没变”的规则：MCP 是请求/响应模型，两次调用之间可能命中破点、抛异常或用户手动操作，所以每次动手前都要重新 `GetDebugState`，并读每个响应末尾的 `[state]` 行。

### 总结

- x64dbg MCP 是原生插件 + HTTP/SSE 服务，默认端口 9094（x64）/ 9095（x32），强制 Bearer Token。
- 本机插件 `x64dbg-MCP-Server.dp64` 已安装，实际 `tools/list` 返回 80 个工具。
- 第一条规则永远是 `GetDebugState`；`NO_TARGET` 时其它工具会报“需要活动调试会话”。
- 标准链：LoadBinary → WaitForPause → 确认 PAUSED → 寄存器/模块/反汇编；下断点后再 run/WaitForEvent。
- 不要假设两次调用之间状态没变，每次动手前重新查状态、读 `[state]` 行。