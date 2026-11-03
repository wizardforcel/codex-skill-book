# 第4章 开发软件

写软件最容易出问题的不是“写不出来”，而是“上来就猛写”。需求没想清楚就开始写、不写测试就开始改、CI 红了不知道从哪查，这些才是新手项目失控的主要原因。这一章介绍四套从不同粒度约束开发流程的 Skill：`superpowers` 是完整工程管线，`hl` 系列是可按环节单独调用的轻量组合，Chrome DevTools MCP 负责开发过程中的浏览器验证，`gh-fix-ci` 负责 CI 红灯排查。开发软件这一章，与其说是学一门新技术，不如说是学一套'先想清楚再动手'的纪律；纪律到位了，语言和框架反而成了小问题。

## 4.1 从需求到 TDD 的完整链路

### 简介

`superpowers` 把“头脑风暴 → 设计确认 → 写实现计划 → TDD（红-绿-重构）→ 审查 → 收尾”固化成 Codex 必须遵守的工程管线。它的核心思想是：用流程约束替代“上来就猛写”，特别适合初学者，因为每一步都有明确文件和检查点，不会被一句“帮我做个功能”直接带偏。开发最怕的不是慢，而是方向错了还继续往下冲；这套流程把每个决策点都变成有产出的检查点，跑偏了也能早点回头。

仓库里实际上是一组技能：`using-superpowers` 是入口，`brainstorming` 负责需求澄清，`writing-plans` 负责计划，`test-driven-development` 规定红-绿-重构，`systematic-debugging` 负责故障定位，`requesting-code-review` / `receiving-code-review` 负责审查，`verification-before-completion` 负责收尾验证。

### 调用记录

**我**：帮我的计算器模块加一个加法函数吧。

**Codex**：按 `using-superpowers` 的规则，动手前必须先检查有没有技能适用：

```text
Let's build X → superpowers:brainstorming first, then implementation skills.
Fix this bug → superpowers:systematic-debugging first, then domain skills.
```

“加一个功能”命中 brainstorming，所以不会先写代码，而是先确认需求。

**我**：这还要确认什么？不就是 `a + b` 吗？

**Codex**：`brainstorming/SKILL.md` 的第一条是“你相信的通常比你以为的薄”。它要求实现前按顺序做三件事：先把可选方案列出来让你选、写一份设计文档、得到你的批准后才调用计划技能。最小需求也至少要确认边界，比如：边界值怎么处理？输入能不能是负数？溢出要不要检查？

**我**：好，那边界就按“负数也能加”处理。

**Codex**：设计确认后进入 TDD。`test-driven-development/SKILL.md` 写了一条铁律：

```text
The Iron Law
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

如果先写了生产代码再补测试，要删掉重来，不能留着“参考”。我按这个原则先写测试：

```python
from calc import add

def test_add_positive():
    assert add(1, 2) == 3

def test_add_overflow_guard():
    assert add(-1, 1) == 0
```

跑到红阶段，真实输出：

```text
FAILED test_calc.py::test_add_positive - NotImplementedError
FAILED test_calc.py::test_add_overflow_guard - NotImplementedError
2 failed in 0.09s
```

**我**：为什么要先看它失败？

**Codex**：TDD 的核心原则是“如果你没看过测试失败，你就不知道它测的是不是对的东西”。第一次跑失败，证明这个测试真的在检查未实现的行为；然后再写最小实现：

```python
def add(a, b):
    return a + b
```

跑绿阶段，真实输出：

```text
..                                                                       [100%]
2 passed in 0.01s
```

这就是“红-绿”的最小闭环。接下来如果还能做重构，就必须在测试继续全绿的前提下改，改完再跑一遍。

**我**：完整链路最后还有什么？

**Codex**：按 `superpowers` 的管线，最后还有代码审查和收尾验证：`requesting-code-review` 会把改动交给审查者；`verification-before-completion` 要求提交前重新运行测试、确认工作区干净、并核对“我确实完成了用户要求”，而不是“看起来完成了”。

把这一节放回整条链路里看，它只是其中一段；真正动手时不必追求一次全对，先把命令跑通、把输出对上，遇到报错再回来查对应位置，往往比从头读一遍更快。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- `superpowers` 是一组技能，不是单文件，入口强制先检查技能再回答问题。
- 新功能先走 `brainstorming`：列方案、写设计文档、得到批准。
- TDD 的铁律是“没有失败测试就不许写生产代码”，先看红、再变绿、最后重构。
- 收尾不只跑测试，还要做代码审查和完成前验证，避免“看起来完成”。
- 这套流程对新人最大的帮助是：每一步都有产出和检查点，不会跑偏太远才回头。

## 4.2 轻量按需组合：hl 系列

### 简介

`hl-skills` 是一套 27 个“证据优先”（Evidence-first）的 Skill，特点是**按环节单独调用**：`hl-debug` 强制先定位根因再改代码，`hl-code-review` 针对分支做 bug 和回归审查，`hl-tdd` 负责测试先行。和 `superpowers` 不同，它不要求你一次性引入整套管线，而是“哪里出问题就调哪个”。适合还不想被完整流程约束、但希望关键动作有纪律的读者。如果还不想把整套流程都背上，就可以按环节单独选：出 bug 用调试技能，审代码用审查技能，各取所需。

### 调用记录

**我**：27 个技能怎么选？

**Codex**：仓库 `skills/` 下就是这 27 个，各有触发词。和开发最相关的几个：

```text
hl-debug        出 bug / 行为异常 / 变慢 → 先建快速反馈回路再下结论
hl-code-review  审分支 / PR / commit 的 diff → 静态、只读、定位在指定修订上
hl-tdd          实现功能或修 bug 前 → 先写失败测试
hl-verify       收尾验证
hl-ci-fix       修 CI 检查失败（专用于 pr checks，不用 hl-debug）
```

`hl-debug` 的触发词明确写着“不是用来修 PR 失败检查的”（那是 `hl-ci-fix` 的事）。它会要求每个故障先分离三件事：症状（观察到什么）、触发（什么变化让它现在出现）、缺陷（错的代码或状态）。

**我**：那故意制造一个失败测试，看它第一步做什么。

**Codex**：我建了一个 `stats.py`，函数只想算平均数，实现却用了整除：

```python
def avg(a, b):
    return (a + b) // 2
```

测试断言 `avg(3, 4) == 3.5`，pytest 真实失败输出：

```text
E   assert 3 == 3.5
E    +  where 3 = avg(3, 4)
test_stats.py:4: AssertionError
FAILED test_stats.py::test_avg_returns_float - assert 3 == 3.5
1 failed in 0.08s
```

**我**：`hl-debug` 第一步会直接改代码吗？

**Codex**：不会。它的规则原文是：

```text
Before any hypothesis, build one command that shows the user's exact symptom, and run it.
```

也就是“先有反馈回路，再做假设”。这个测试本身就是那条回路——它每次都以同样的原因失败、几秒跑完、不需要人工参与。在此之上才允许进入 `Investigate`，把症状、触发、缺陷分开：症状是“返回 3 而非 3.5”；触发是“函数一直用 `//`”；缺陷是“整除丢掉了小数部分”。它还给出一条更严格的规矩：你读过的代码才算证据，不能凭函数名猜测它做什么。

**我**：那修呢？

**Codex**：修要放在失败回归测试之后。改成浮点除法：

```python
def avg(a, b):
    return (a + b) / 2
```

再跑：

```text
.                                                                        [100%]
1 passed in 0.01s
```

根因对比很清楚：`7 // 2 = 3`，`7 / 2 = 3.5`。

**我**：如果比较的是分支代码呢？

**Codex**：那就是 `hl-code-review`。它的要求是只看指定修订的 diff，不 checkout、不跑测试、不提交，逐条给你：触发、后果、证据和严重度，严重度只分“数据/安全失败、实质性 bug、有限问题、风格”四档，且只数“diff 引入或暴露”的缺陷，不数本来就在的问题。对上面这个修复 diff，它会判实质 bug 已修，但会提醒后续影响：`avg` 的返回类型从 int 变成了 float，如果调用方之前依赖整数，需要连到调用者一起确认。

这些步骤看起来零散，其实前后是有因果的：前一步的产物就是后一步的输入，中间哪一环没对上，后面就会以各种奇怪的方式报错。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- `hl-skills` 是 27 个证据优先技能，按环节调用，不需要整套引入。
- `hl-debug` 先建反馈回路再假设，先分症状/触发/缺陷，最后才改代码且必须配失败回归测试。
- `hl-code-review` 静态审 diff，只数 diff 引入或暴露的缺陷，每条给出触发、后果、证据和严重度。
- 触发词之间要分清：CI 红灯找 `hl-ci-fix`，一般 bug 找 `hl-debug`。
- 与 `superpowers` 的关系：前者是完整工程管线，后者是可按需单点调用的工具箱。

## 4.3 开发阶段的浏览器验证：Chrome DevTools MCP

### 简介

开发网站时，很多“看起来没问题”其实是骗人的：响应式布局在窄屏溢出、某段 JS 报错、首屏太慢。Chrome DevTools MCP 让 Codex 在开发过程中直接连接真实浏览器，做实时调试、模拟响应式布局、跑 Lighthouse 审计。它和第一章里“打开 example.com 读标题”用的是同一个 MCP，只是这一节聚焦“代码 → 浏览器验证”的开发内环：改完代码，让浏览器告诉我真实宽度、真实溢出元素，而不是让它模糊地说“应该没问题”。写网页的人最常翻车的地方，就是'本地看着没问题的页面，一换到窄屏就溢出'；浏览器 MCP 的价值，就是把这个'看着没问题'变成数字和清单。

### 调用记录

**我**：接好之后，怎么让 Codex 检查一个页面在手机宽度下有没有横向溢出？

**Codex**：先加 MCP（第一章已经装过）：

```powershell
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

然后打开页面调用 `resize_page` 切到 375×667，再用 `evaluate_script` 量视口宽度和文档滚动宽度，比较两者是否溢出。

**我**：跑一下看看。

**Codex**：连接浏览器后，先用页面脚本拿到桌面视口的基线：

```text
evaluate_script(pageId=2, function=...)
{"viewport":1036,"scrollWidth":1021,"overflowX":false,"offenders":[]}
```

再调用 `resize_page({pageId:2,width:375,height:667})`，重新量：

```text
{"viewport":501,"scrollWidth":486,"overflowX":false,"offenders":[]}
```

这里有一个真实的细节：我请求的是 375 宽，但浏览器实际报的 `innerWidth` 是 501。原因是浏览器窗口有最小宽度限制，`resize_page` 设的是窗口尺寸，不一定能压到真实的 375 设备像素。所以教科书式的做法不是“看见 375 就信”，而是**以 `window.innerWidth` 返回的真实值为准**，再判断溢出。

**我**：判断溢出的逻辑是什么？

**Codex**：三合一：

```javascript
const overflowX = document.documentElement.scrollWidth > window.innerWidth;
```

再列出真正右侧溢出视口的元素（`scrollWidth > clientWidth` 且右边界超出视口宽）：

```text
{"viewport":501,"scrollWidth":486,"overflowX":false,"offenders":[]}
```

两个容器都是绿色结果：文档滚动宽度 486 小于视口 501，没有横向溢出，异常元素数组为空。这个输出和“看起来没问题”的区别在于，它给了你真实的宽度数值（501 和 486）和被判定的依据（`overflowX: false`、`offenders: []`）。

**我**：如果你想强制真实设备像素，而不是房间大小的窗口呢？

**Codex**：可以使用 MCP 的 `emulate` 工具设置设备指标（Imdea width flag 类似桌面浏览器的设备模拟），或者用 `set_viewport` 相关的命令让视口严格等于目标值。判断思路不变：一切以浏览器返回的 `documentElement.scrollWidth` 和 `innerWidth` 为准，溢出不溢出用两数比较，不靠肉眼看。

如果只记住一句，那就是：先让最小链路真实跑通，再谈优化和自动化；跳过验证直接堆功能，最后往往要花更多时间回头补。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- Chrome DevTools MCP 在开发内环里的价值是“真实数据代替感觉”。
- 响应式检查的标准姿势：`resize_page` 切窄 → `evaluate_script` 取 `scrollWidth` 与 `innerWidth` → 比较并列出溢出元素。
- 请求的宽不等于实际视口宽：浏览器有最小窗口限制，以 `window.innerWidth` 返回的真实值为准。
- 溢出判断的判据是数字（`scrollWidth vs innerWidth`）和元素清单，而不是一句“应该没问题”。
- 需要严格设备像素时用 `emulate`/设备模拟能力。

## 4.4 CI 红灯的自动排查

### 简介

CI 红灯排查是高频又琐碎的事：打开 Actions 页面、点进红色 run、找日志里的红字、判断是代码真错还是环境噪声。`gh-fix-ci` 就是把这套动作固化成流程：用 `gh` 找失败的 PR 检查、拉 GitHub Actions 日志、把失败摘要总结成根因、草拟修复计划，并且**在用户确认后才实施**。它对“真实失败 / 环境噪声”做了区分，只修该修的。CI 红灯处理是高频又琐碎的事，把整个排查过程标准化之后，你真正需要负责的只剩下最后拍板。

### 调用记录

**我**：我这边 CI 红了，怎么让它自己查？

**Codex**：先装技能（skill-installer 可以从官方 curated 列表按名安装）：

```powershell
py C:\Users\Administrator\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo openai/skills --path skills/.curated/gh-fix-ci --ref main
# Installed gh-fix-ci to C:\Users\Administrator\.codex\skills\gh-fix-ci
```

然后第一步验证 `gh` 认证：

```text
github.com
  ✓ Logged in to github.com account wizardforcel (GH_TOKEN)
  - Token scopes: ... 'repo' ... 'workflow' ...
```

**我**：那我用哪个仓库练手？

**Codex**：用 `openai/skills` 仓库里一次真实失败来演示。用 `gh` 拉最近失败的 runs：

```bash
gh api "repos/openai/skills/actions/runs?status=failure&per_page=3" \
  --jq '.workflow_runs[] | {id, name, conclusion, event}'
# {"conclusion":"failure","event":"dynamic","head_branch":"refs/pull/410/head","id":25770460351,"workflow_name":"Copilot code review"}
```

再细看这一次的 job 结论，马上能看出“哪个环节红的”：

```text
Prepare          success
Agent            success
Upload results   success
Cleanup artifacts  failure   ← 只红这里
```

**我**：这一步是不是已经能看出点什么？

**Codex**：能。真正的代码检查和评审步骤（Agent、Upload results）都是 `success`，只有收尾的 `Cleanup artifacts` 红了。这通常指向环境/清理类问题，而不是代码缺陷——这就是“真实失败 / 环境噪声”的第一层区分。

**我**：那它怎么把日志拉出来确认？

**Codex**：按技能流程拉 job 日志。这里遇到一个真实情况，GitHub 返回了：

```text
{"message":"Server Error", ..., "status":"410"}
# failed to get run log: HTTP 410: Server Error
```

410 表示这份日志已经过期不存在了。这正是技能要求处理的边界：`Call out missing logs explicitly`——缺日志就明说缺日志，绝不拿猜测当证据。我随后再跑一次本地 pytest 制造一份“真实的红色日志”，让“引用具体失败步骤和关键日志行”有可展示的输出：

```text
E   assert 3 == 3.5
FAILED test_stats.py::test_avg_returns_float - assert 3 == 3.5
1 failed in 0.08s
```

**我**：那它总结根因后，会直接改代码吗？

**Codex**：不会。`gh-fix-ci` 明确要求：`draft a fix plan, and implement only after explicit approval`。先给方案（可以用 `create-plan` 或内联），你批准后才动手；改完再建议重跑相关测试和 `gh pr checks` 确认。也就是说，它的角色是“把红灯变成可读的根因摘要 + 计划”，最终拍板的是你。

**我**：搜索 MCP 能找到 gh-fix-ci 的公开教程或失败日志样例吗？

**Codex**：检索到的主要是这个技能在技能仓库里的条目，以及一些泛化的 GitHub Actions 排查文章，没有可直接复用的失败日志。技能本身也预判了这种情况：日志拉不到就明确写“缺少日志”，而不是编一段错误信息。本次 410 过期日志的处理，正好是这条规则的实例。

本节记录里保留了失败和阻断，不是为了吓人，而是让你知道正常使用中也会遇到这些情况，遇到了照着排查即可，不必怀疑自己。

### 总结

这一节的内容说起来不少，真正值得带走的是下面几条；把它们串起来看一遍，比单独记某一条更有用。

- `gh-fix-ci` 的流程：验认证 → 解析 PR → 查失败检查 → 拉日志 → 总结根因 → 出计划 → 你批准 → 实施 → 重查。
- 第一步用 `gh pr checks --json` 或脚本看清“哪个 job 红了”，代码步骤 vs 清理步骤的失败性质不同。
- 日志可能过期（HTTP 410）；技能的要求是明说缺日志，不拿猜测当证据。
- 区分“真实失败 / 环境噪声”是其核心价值，确认失败步骤后再定是修代码还是不理会。
- 实施前必须显式批准，改完重跑测试并建议复查 `gh pr checks`。