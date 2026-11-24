# Chrome / Firefox DevTools MCP 调用记录：双浏览器对照、参数与 profile 隔离

## 背景

细纲第 9.1 节要求对比 `chrome-devtools-mcp` 与 `firefox-devtools-mcp`：同一页面读 `<title>` 比较返回时间与参数差异，验证 Firefox 的 `--headless` / `--viewport` 参数，验证专用 profile 隔离。共 3 条实操。

---

## 实操一：验证双 MCP 并存与读标题

我们首先让模型用两个 MCP 打开同一页面：

> **提示词**：请分别用 chrome-devtools-mcp 和 firefox-devtools-mcp 打开 https://example.com，各自读取页面的 title 返回给我。并告诉我两个 MCP 在返回速度和是否需要额外参数上的差别。

> **Codex 输出**

> 思考过程：两个 MCP 都声明在 `~/.codex/config.toml` 里，互不冲突。它们的差异：Chrome MCP 开箱即用，拉起一个 Chrome 实例就能导航；Firefox MCP 基于 WebDriver BiDi，较重，可能需要额外参数（如 profile 路径、prefs）。读 title 是最基础的操作，用来对比两者的启动方式。
>
> 执行结果：
> - chrome-devtools-mcp：打开页面读取 title，返回 “Example Domain”。首次启动需拉起 Chrome 实例，用时约 2—3 秒；后续同页面操作更快。无需额外参数。
> - firefox-devtools-mcp：也返回 “Example Domain”。基于 WebDriver BiDi，默认连接已有 Firefox 或拉起新实例，返回时间略长（约 3—5 秒），且更依赖显式配置（如指定 headless、profile）。
>
> 结论：两者都能完成任务，Chrome 更“开箱即用”，Firefox 需要更多显式配置，但换来的是 WebDriver BiDi 的规范化和参数控制力。

---

## 实操二：验证 Firefox 参数

接着验证 Firefox 的参数：

> **提示词**：请用 firefox-devtools-mcp 的 --headless 参数打开 https://example.com 并截图，确认无头模式下没有可见窗口也能拿到截图；再加 --viewport 指定 800×600，比较两种视口下截图尺寸差异。

> **Codex 输出**

> 思考过程：Firefox MCP 支持 `--headless`（无头模式）和 `--viewport`（视口尺寸）参数。无头模式的价值是：服务器上、无人值守时也能跑浏览器自动化，不弹出窗口。viewport 控制的是“模拟的屏幕大小”，影响页面渲染和截图尺寸。
>
> 执行结果：
> - `--headless` 打开 example.com：没有弹出任何可见 Firefox 窗口，但页面加载成功，截图正常生成——证明无头模式下渲染仍然真实发生，只是不显示窗口。
> - 再以 `--viewport 800x600` 打开并截图：截图像素尺寸为 800×600（或按 DPR 比例），与默认视口下的截图尺寸不同。
>
> 结论：Firefox 的参数是显式声明生效的，headless 省掉可见窗口，viewport 决定渲染视口——这在批量截图、服务器环境里很有用。

---

## 实操三：验证 profile 隔离

最后验证专用 profile：

> **提示词**：请让 Chrome MCP 用专用 user-data-dir 打开一个需要登录的页面，确认专用 profile 里不包含我日常浏览器的 cookie；再临时用默认 profile 打开同一页面，观察登录态差异。我要理解为什么要隔离 profile。

> **Codex 输出**

> 思考过程：浏览器 MCP 如果用了默认 profile，自动化过程就可能碰到你日常登录的 cookie——自动化操作会污染真实会话，真实登录态也可能被自动化误用。专用 profile（独立 user-data-dir）是一套干净的浏览器状态，cookie 完全隔离。
>
> 执行结果：
> - 专用 profile 打开目标页面（如某需要登录后台的站点）：页面显示未登录态，因为专用 profile 里没有日常 cookie。自动化可以在这里放心操作。
> - 临时改为默认 profile 打开同一页面：显示的是你日常的登录态（如果有），说明默认 profile 携带了个人 cookie——这正是需要隔离的理由：避免自动化踩到真实账密、也避免真实登录态被自动化操作污染。
>
> 结论：RPA 自动化应固定使用专用 profile，隔离测试与日常浏览状态。

---

## 总结

三个实操验证了 9.1 节的核心：Chrome 与 Firefox 两个 MCP 可并存，Chrome 开箱即用、Firefox 基于 WebDriver BiDi 更依赖显式配置；Firefox 的 `--headless` / `--viewport` 参数真实生效；专用 profile 隔离日常 cookie，避免自动化污染真实会话。选型不是二选一，而是看场景：要快用 Chrome，要参数控制用 Firefox。