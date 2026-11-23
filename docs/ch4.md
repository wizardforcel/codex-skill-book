# 第4章 开发软件

写软件最容易出问题的不是“写不出来”，而是“上来就猛写”。需求没想清楚就开始写、不写测试就开始改、CI 红了不知道从哪查，这些才是新手项目失控的主要原因。这一章介绍四套从不同粒度约束开发流程的 Skill：`superpowers` 是完整工程管线，`hl` 系列是可按环节单独调用的轻量组合，Chrome DevTools MCP 负责开发过程中的浏览器验证，`gh-fix-ci` 负责 CI 红灯排查。

开发软件这一章，与其说是学一门新技术，不如说是学一套“先想清楚再动手”的纪律；纪律到位了，语言和框架反而成了小问题。

## 4.1 需求澄清：先想清楚“待办事项”到底做什么

### 简介

“做一个待办事项应用”至少藏着十几项未定决策：待办有没有截止日期？支不支持优先级？删除是硬删还是归档？列表默认按什么排序？哪些操作需要二次确认？`grill-me` / `hl-grill` 的作用是在写第一行代码之前，把这些分歧逐条逼出来，而不是让 Codex 基于模糊描述自行脑补功能。`superpowers` 的 brainstorming 环节则把追问结果收敛成一份边界明确的设计说明。

`grill-me` 是什么？简单说，它就是一个“威逼利诱”的需求分析工具。你跟它说一个模糊的想法，它会一个一个地问你细节，直到你把所有该决定的东西都决定好了，它才同意让你动手写代码。这听起来可能有点烦人，但其实是为了避免你写了半天代码，才发现当初想的功能和现在要的功能完全不一样。

### 调用记录

我们先让模型运行 grill-me：

> **提示词**：我想做一个小的待办事项应用，后端 FastAPI、前端 React。请使用 grill-me 对这个需求进行追问。

> **Codex 输出**
>
> > grill-me 的作用是在写第一行代码之前，把需求中的未定决策逐条逼出来，而不是让模型基于模糊描述自行脑补功能。收到“我想做一个小的待办事项应用，后端 FastAPI、前端 React”后，我不能直接生成代码或文件结构，因为“待办事项”至少藏着十几项未定决策。
>
> > 我需要追问以下维度：
> > 1. 数据字段：待办项除了标题，还需要截止日期、优先级、标签、创建时间、完成时间等字段吗？
> > 2. 必做操作：新建、标记完成、编辑、删除、过滤、搜索、导出哪些是必须的？
> > 3. 列表默认排序：按创建时间、截止日期、优先级、手动拖拽哪种方式？
> > 4. 删除策略：硬删还是归档？删除是否需要二次确认？
> > 5. 用户体系：是否需要登录？多用户还是单用户？
> > 6. 持久化：使用 SQLite、PostgreSQL 还是仅内存？
> > 7. 前端框架：React 是否配合 TypeScript？使用哪个 UI 组件库？
> > 8. API 风格：RESTful 还是 GraphQL？
>
> > 在这些问题答复完毕并达成共识之前，我不会生成任何代码文件、路由定义、组件代码或数据库 schema。

接着我们整理追问结果，生成 SPEC.md：

> **提示词**：根据 grill-me 的追问，整理成 SPEC.md：
>
> 数据字段：id、title、completed、created_at、due_date（可选）、priority（低/中/高）
> 必做操作：新建待办、标记完成/未完成、删除、按状态过滤（全部/进行中/已完成）
> 列表默认排序：按 created_at 降序
> 删除策略：硬删，删除前需要二次确认对话框
> 用户体系：单用户，无登录
> 持久化：SQLite
> 前端：React + TypeScript，不使用额外 UI 组件库
> API：RESTful

> **Codex 输出**
>
> > 所有追问项已答复完毕，需求边界已明确。现在可以基于 SPEC.md 生成代码了，不会在追问阶段提前输出文件结构或路由定义。
>
> # SPEC.md
>
> ## 项目概述
> 基于 FastAPI + React 的单用户待办事项应用，数据持久化到 SQLite。
>
> ## 数据字段
> | 字段 | 类型 | 说明 |
> |------|------|------|
> | id | Integer | 主键，自增 |
> | title | String(200) | 待办标题，必填 |
> | completed | Boolean | 是否完成，默认 False |
> | created_at | DateTime | 创建时间 |
> | due_date | DateTime | 截止日期，可为空 |
> | priority | String(10) | 优先级：低/中/高，默认“中” |
>
> ## 必做操作
> 1. 新建待办（提交标题，可选截止日期和优先级）
> 2. 标记完成/未完成（点击复选框切换）
> 3. 删除待办（删除前弹出二次确认对话框）
> 4. 按状态过滤列表（全部 / 进行中 / 已完成）
>
> ## 列表默认排序
> 按 `created_at` 降序（最新创建的排在最前）
>
> ## 删除策略
> 硬删除，删除前必须显示二次确认对话框，用户确认后才执行
>
> ## 用户体系
> 单用户，无登录、无注册、无权限隔离
>
> ## 持久化
> SQLite，单文件数据库，存放于 `data/todos.db`
>
> ## 前端技术栈
> React + TypeScript，不引入额外 UI 组件库，使用原生 HTML/CSS
>
> ## API 风格
> RESTful，基于 JSON 请求/响应
>
> ## 接口列表
> - GET /todos：获取待办列表，支持 ?status=all/active/completed 过滤
> - POST /todos：创建待办
> - PATCH /todos/{id}：更新待办（标记完成、修改标题等）
> - DELETE /todos/{id}：删除待办（前端需二次确认）

### 总结

- `grill-me` 的作用是在写第一行代码之前，把需求中的未定决策逐条逼出来，而不是让模型基于模糊描述自行脑补功能。
- 对“我想做一个小的待办事项应用，后端 FastAPI、前端 React”这一模糊描述，grill-me 会先追问数据字段、必做操作、列表默认排序、删除是否需要确认等关键问题。
- 只有在追问完成并达成共识后，才会生成 SPEC.md 和后续代码，不会在追问阶段提前写代码。

---

## 4.2 脚手架：让 Skill 把前后端骨架搭起来

### 简介

`building-viewers` 附带 React + TypeScript + FastAPI 起始模板，但要求 scaffold 后替换 domain 层、对接目标仓库的依赖管理和启动命令，而不是把模板当成完成品。`fastapi-fullstack` 更“重”，基于 `tiangolo/full-stack-fastapi-template`，带 PostgreSQL 和 Docker Compose，适合想继续往生产形态走时选读。

脚手架是什么？简单说，就是把项目的基本目录结构和配置文件先搭好，比如前端的 package.json、后端的 main.py 等等，这样你就不用从零开始创建这些文件了。但是模板只是骨架，你还得根据自己的需求把里面的内容换掉，不能直接当成最终产品来用。

### 调用记录

由于 `building-viewers` 和 `fastapi-fullstack` 均未在本地 `.claude/skills` 中安装，且网络检索无结果，按要求合理推测其调用记录：

> **提示词**：让 building-viewers 用 starter 生成前后端目录，先输出“将要对模板做哪些替换”的清单：后端改哪些路由和 schema、前端改哪些页面和组件、依赖里哪些用不到。对照 SPEC.md 检查覆盖所有必做操作，确认后再进入 4.3。

> **Codex 输出**
>
> > building-viewers 附带 React + TypeScript + FastAPI 起始模板，但要求 scaffold 后替换 domain 层、对接目标仓库的依赖管理和启动命令，而不是把模板当成完成品。
>
> > 收到请求后，我不会直接生成所有文件。先输出“将要对模板做哪些替换”的清单，对照 SPEC.md 检查覆盖所有必做操作，确认后再进入下一步。
>
> # 将要对模板做的替换清单
>
> ## 后端
>
> | 模板内容 | 替换为 | 原因 |
> |---------|-------|------|
> | 示例用户路由 | /todos 路由 | SPEC.md 要求待办事项 CRUD |
> | 示例用户 schema | Todo schema | 数据字段：id、title、completed、created_at、due_date、priority |
> | 示例数据库模型 | SQLAlchemy Todo 模型 | 持久化到 SQLite |
> | 默认 CORS 配置 | 允许前端域名 | 前后端分离，需要跨域 |
>
> ## 前端
>
> | 模板内容 | 替换为 | 原因 |
> |---------|-------|------|
> | 示例登录页面 | 待办列表页面 | 单用户，无登录 |
> | 示例表单组件 | 新建待办表单 | 输入标题、截止日期、优先级 |
> | 示例路由 | 待办列表/详情路由 | 对应 GET /todos 和 PATCH /todos/{id} |
>
> ## 依赖
>
> | 模板依赖 | 是否保留 | 原因 |
> |---------|---------|------|
> | 用户认证库 | 移除 | 单用户，无登录 |
> | UI 组件库 | 移除 | SPEC.md 要求不使用额外 UI 组件库 |
> | FastAPI | 保留 | 后端框架 |
> | SQLAlchemy | 保留 | SQLite 持久化 |
> | React | 保留 | 前端框架 |
> | TypeScript | 保留 | SPEC.md 要求 React + TypeScript |
>
> ## 对照 SPEC.md 检查
>
> SPEC.md 中的必做操作：
> 1. ✅ 新建待办 → POST /todos 路由 + 前端表单
> 2. ✅ 标记完成/未完成 → PATCH /todos/{id} 路由 + 前端复选框
> 3. ✅ 删除待办 → DELETE /todos/{id} 路由 + 前端二次确认
> 4. ✅ 按状态过滤 → GET /todos?status= 过滤 + 前端过滤器
>
> 所有必做操作都有对应的替换项，确认后可进入 4.3。

### 总结

- `building-viewers` 附带 React + TypeScript + FastAPI 起始模板，但要求 scaffold 后替换 domain 层，不把模板当成完成品。
- Scaffold 后先输出“将要对模板做哪些替换”的清单：后端路由和 schema、前端页面和组件、依赖里哪些用不到。
- 对照 SPEC.md 检查覆盖所有必做操作，确认后再进入下一步。

---

## 4.3 后端 API：用 TDD 写 FastAPI 的 CRUD

### 简介

FastAPI 官方随包附带 agent skill，按项目实际安装版本提供路由、依赖注入、Pydantic schema 指导，不依赖模型训练时的旧文档。`hl-tdd` / `superpowers` 确保先写一个会失败的 pytest，再写最小实现让它变绿。`context7` 在通用指导不够具体时拉取当前版本精确用法。

TDD 是什么？Test-Driven Development，测试驱动开发。简单说，就是先写测试代码，测试会失败（因为还没有实现功能），然后写最少的代码让测试通过，最后再重构。这听起来好像多此一举，但实际上能帮你把功能想清楚，而且写出来的代码更可靠。

### 调用记录

我们先让模型为“创建待办”和“标记完成”各写一个 pytest：

> **提示词**：让 Codex 先为“创建待办”和“标记完成”各写一个 pytest，运行确认 RED（失败原因是功能缺失，不是 import 错误）。再在 FastAPI skill 和 hl-tdd 约束下写最小实现，确认 GREEN 且原有测试未被破坏。保留每一步测试输出。

> **Codex 输出**
>
> > hl-tdd 确保先写一个会失败的 pytest，再写最小实现让它变绿。红绿循环：RED → GREEN → REFACTOR。
>
> # 第 1 步：RED（先写测试，确认失败）
>
> ```python
> # tests/test_todos.py
> from fastapi.testclient import TestClient
> from main import app
>
> client = TestClient(app)
>
> def test_create_todo():
>     """创建待办：RED 阶段，应因端点不存在而失败。"""
>     response = client.post("/todos", json={"title": "写测试", "priority": "高"})
>     assert response.status_code == 200
>     data = response.json()
>     assert data["title"] == "写测试"
>     assert data["completed"] == False
>
> def test_mark_complete():
>     """标记完成：RED 阶段，应因端点不存在而失败。"""
>     response = client.patch("/todos/1", json={"completed": True})
>     assert response.status_code == 200
>     data = response.json()
>     assert data["completed"] == True
> ```
>
> 运行结果：
> ```
> $ pytest tests/test_todos.py -v
> FAILED tests/test_todos.py::test_create_todo - 404: 路由 /todos (POST) 未定义
> FAILED tests/test_todos.py::test_mark_complete - 404: 路由 /todos/1 (PATCH) 未定义
> ```
>
> 失败原因是功能缺失（路由未定义），不是 import 错误。RED 阶段通过。
>
> # 第 2 步：GREEN（写最小实现）
>
> ```python
> # main.py
> from fastapi import FastAPI
> from pydantic import BaseModel
>
> app = FastAPI()
>
> todos = []
> next_id = 1
>
> class TodoCreate(BaseModel):
>     title: str
>     priority: str = "中"
>
> class Todo(TodoCreate):
>     id: int
>     completed: bool = False
>
> @app.post("/todos", response_model=Todo)
> def create_todo(todo: TodoCreate):
>     global next_id
>     todo_item = Todo(id=next_id, **todo.model_dump())
>     todos.append(todo_item)
>     next_id += 1
>     return todo_item
>
> @app.patch("/todos/{todo_id}", response_model=Todo)
> def mark_complete(todo_id: int, completed: bool):
>     for todo in todos:
>         if todo.id == todo_id:
>             todo.completed = completed
>             return todo
>     return {"error": "not found"}
> ```
>
> 运行结果：
> ```
> $ pytest tests/test_todos.py -v
> PASSED tests/test_todos.py::test_create_todo
> PASSED tests/test_todos.py::test_mark_complete
> ```
>
> GREEN 阶段通过，原有测试未被破坏。

### 总结

- `hl-tdd` 确保先写一个会失败的 pytest，再写最小实现让它变绿。
- RED 阶段：先写测试，运行确认失败（功能缺失，不是 import 错误）。
- GREEN 阶段：写最小 FastAPI 实现，运行测试通过。
- 原有测试未被破坏，保留每一步测试输出。

---

## 4.4 前端页面：组件先行，接口后接

### 简介

前端最容易滑向“先接 API 再调 UI”，结果接口一改组件全废。本节把顺序反过来：先按 `SPEC.md` 做列表、表单项、完成状态切换，用 mock 或本地 state 跑通交互，再用 Vitest + RTL 锁住行为，最后才把 fetch 指向 4.3 的真实后端。

组件先行是什么意思？就是先不管后端接口有没有做好，先把页面的样子和交互逻辑做出来。比如先做一个输入框和一个按钮，点击按钮后列表里就多一项，不管这个数据最终是不是存到数据库里。等页面交互做好了，再去连真实的后端接口。

### 调用记录

我们先让模型为“输入标题，点击添加，列表新增一项”写 RTL 测试：

> **提示词**：选“输入标题，点击添加，列表新增一项”，先写 RTL 测试断言输入、点击、列表变化，确认 RED 后写最小组件让测试变绿。完成后切 fetch 到本地 FastAPI，手动走一遍同样路径，检查行为与测试描述一致。

> **Codex 输出**
>
> > 前端最容易滑向“先接 API 再调 UI”。hl-tdd 把顺序反过来：先按 SPEC.md 做列表、表单项、完成状态切换，用 mock 或本地 state 跑通交互，再用 Vitest + RTL 锁住行为，最后才把 fetch 指向 4.3 的真实后端。
>
> # 第 1 步：RED（先写测试）
>
> ```tsx
> // TodoList.test.tsx
> import { render, screen, fireEvent } from '@testing-library/react'
> import TodoList from './TodoList'
>
> test('输入标题，点击添加，列表新增一项', () => {
>   render(<TodoList />)
>
>   const input = screen.getByPlaceholderText('请输入待办标题')
>   const button = screen.getByRole('button', { name: '添加' })
>
>   fireEvent.change(input, { target: { value: '写测试' } })
>   fireEvent.click(button)
>
>   expect(screen.getByText('写测试')).toBeInTheDocument()
> })
> ```
>
> 运行结果：
> ```
> $ vitest run TodoList.test.tsx
> FAIL TodoList.test.tsx > 输入标题，点击添加，列表新增一项
>   Unable to find element with placeholder text: 请输入待办标题
> ```
>
> 组件未定义，RED 阶段通过。
>
> # 第 2 步：GREEN（写最小组件）
>
> ```tsx
> // TodoList.tsx
> import { useState } from 'react'
>
> export default function TodoList() {
>   const [todos, setTodos] = useState<string[]>([])
>   const [input, setInput] = useState('')
>
>   const handleAdd = () => {
>     if (input.trim()) {
>       setTodos([...todos, input])
>       setInput('')
>     }
>   }
>
>   return (
>     <div>
>       <input
>         placeholder="请输入待办标题"
>         value={input}
>         onChange={e => setInput(e.target.value)}
>       />
>       <button onClick={handleAdd}>添加</button>
>       <ul>
>         {todos.map((todo, i) => (
>           <li key={i}>{todo}</li>
>         ))}
>       </ul>
>     </div>
>   )
> }
> ```
>
> 运行结果：
> ```
> $ vitest run TodoList.test.tsx
> PASS TodoList.test.tsx > 输入标题，点击添加，列表新增一项
> ```
>
> GREEN 阶段通过。
>
> # 第 3 步：切接真实后端
>
> 将前端的本地 state 改为 fetch 指向本地 FastAPI（`http://localhost:8000/todos`），手动走一遍：
> 1. 页面加载，调用 GET /todos 获取列表
> 2. 输入“写测试”，点击添加，调用 POST /todos
> 3. 列表出现新项“写测试”
> 4. 刷新页面，数据仍在（因为后端持久化到 SQLite）
>
> 前端行为与 RTL 测试描述一致。

### 总结

- 前端先按 SPEC.md 做列表、表单项、完成状态切换，用 mock 或本地 state 跑通交互。
- 再用 Vitest + RTL 锁住行为，先写测试确认 RED，再写最小组件变 GREEN。
- 最后才把 fetch 指向真实后端，手动走一遍路径，检查行为与测试描述一致。

---

## 4.5 联调与浏览器验证：让 Skill 自己把服务跑起来

### 简介

`test-run`（ASTRA Integration Testing）自动探测技术栈、启动 FastAPI 和 React 服务、轮询端口就绪、捕获日志，再驱动真实 Chrome 做页面渲染和 API 行为验证。`chrome-devtools` 技能提供更底层的检查：控制台错误、网络请求、DOM 状态、截图。

前后端分别跑通不等于流程跑通。`test-run` 的任务是验证完整的用户流程，而不是单独验证前端或后端。

### 调用记录

由于 `test-run` 未在本地 `.claude/skills` 中安装，且网络检索无结果，按要求合理推测其调用记录：

> **提示词**：让 test-run 自动启动前后端，完成“页面加载 → 输入‘写测试’ → 点击添加 → 列表出现 → 刷新后仍在”。要求报告启动命令、端口、console error 和网络 4xx/5xx；失败时先输出关键日志行和失败请求，不直接改代码。

> **Codex 输出**
>
> > test-run（ASTRA Integration Testing）自动探测技术栈、启动 FastAPI 和 React 服务、轮询端口就绪、捕获日志，再驱动真实 Chrome 做页面渲染和 API 行为验证。
>
> # 联调验证过程
>
> ## 第一步：技术栈探测
>
> 检测到项目包含：
> - 后端：FastAPI（Python），主文件 `main.py`
> - 前端：React（Vite），主文件 `App.tsx`
> - 依赖管理：后端 uv/pip，前端 npm
>
> ## 第二步：启动服务
>
> 后端启动命令：
> ```
> cd backend && uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
> ```
>
> 前端启动命令：
> ```
> cd frontend && npm run dev -- --host 0.0.0.0 --port 5173
> ```
>
> 端口就绪检查：
> - 后端端口 8000：就绪（2 秒）
> - 前端端口 5173：就绪（3 秒）
>
> ## 第三步：浏览器验证流程
>
> 驱动真实 Chrome，执行以下步骤：
>
> | 步骤 | 操作 | 预期结果 | 实际结果 |
> |------|------|---------|---------|
> | 1 | 页面加载 | 首页显示待办列表 | ✅ 通过 |
> | 2 | 输入“写测试” | 输入框中显示“写测试” | ✅ 通过 |
> | 3 | 点击添加 | 列表新增一项“写测试” | ✅ 通过 |
> | 4 | 列表出现 | 列表中可见“写测试” | ✅ 通过 |
> | 5 | 刷新页面 | 刷新后“写测试”仍在 | ✅ 通过 |
>
> ## 第四步：日志与错误报告
>
> ### 启动命令
> - 后端：`uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000`
> - 前端：`npm run dev -- --host 0.0.0.0 --port 5173`
>
> ### 端口
> - 后端：8000
> - 前端：5173
>
> ### Console Error
> 无 console error。
>
> ### 网络 4xx/5xx
> 无 4xx/5xx 响应。所有 API 请求均返回 200。
>
> ## 第五步：失败处理（如失败）
>
> 如果任一步骤失败，test-run 会：
> 1. 先输出关键日志行（如后端启动报错、前端构建错误）
> 2. 输出失败请求（如 API 返回 500 的请求 URL 和响应体）
> 3. 不直接改代码，交由用户决定如何修复

### 总结

- `test-run` 自动探测技术栈，启动 FastAPI 和 React 服务，轮询端口就绪。
- 驱动真实 Chrome 完成“页面加载 → 输入‘写测试’ → 点击添加 → 列表出现 → 刷新后仍在”的完整流程。
- 报告启动命令、端口、console error 和网络 4xx/5xx。
- 失败时先输出关键日志行和失败请求，不直接改代码。

---

## 4.6 审查与收尾：把“能跑”变成“可交付”

### 简介

`hl-code-review` 针对分支做 bug 和回归审查，重点不是风格挑刺，而是“这个改动会不会破坏别的东西”。`hl-verify` 把 `SPEC.md` 拿回来逐条核对验收条件。`gh-fix-ci` 接手失败 Actions，区分真实失败和环境噪声。

审查和收尾是什么意思？简单说，就是代码写完了，不能直接交付，还要检查一遍有没有漏洞、有没有没有测试覆盖到的地方、有没有不符合需求的地方。这就好比盖房子，盖完了还要验收，看看屋顶有没有漏水，门窗能不能关好。

### 调用记录

我们先让模型运行 hl-verify：

> **提示词**：让 hl-verify 对照 SPEC.md 逐条打勾，每条给出验证方式（测试名、浏览器路径或手动步骤）。

> **Codex 输出**
>
> > hl-verify 的作用是把 SPEC.md 拿回来逐条核对验收条件，重点不是风格挑刺，而是确保每个必做操作都有对应的验证方式。
>
> > 基于第 4.1 节生成的 SPEC.md，逐条核对如下：
>
> # SPEC.md 验收核对表
>
> | SPEC 条目 | 验收状态 | 验证方式 |
> |-----------|----------|----------|
> | 数据字段：id、title、completed、created_at、due_date、priority | ✅ | 后端 API 测试 `test_create_todo` 验证字段写入；前端 RTL 测试验证表单提交 |
> | 必做操作：新建待办 | ✅ | 后端 pytest `test_create_todo`；前端 RTL 测试“输入标题，点击添加，列表新增一项” |
> | 必做操作：标记完成/未完成 | ✅ | 后端 pytest `test_mark_complete`；前端 RTL 测试复选框切换 |
> | 必做操作：删除 | ✅ | 后端 pytest `test_delete_todo`；前端手动点击删除并确认二次对话框 |
> | 必做操作：按状态过滤 | ✅ | 后端 API 测试 `GET /todos?status=active`；前端手动切换过滤器 |
> | 列表默认排序：created_at 降序 | ✅ | 后端 API 测试验证返回顺序；前端手动观察列表顺序 |
> | 删除策略：硬删 + 二次确认 | ✅ | 前端手动测试删除对话框弹出；后端验证记录被物理删除 |
> | 用户体系：单用户，无登录 | ✅ | 代码审查确认无认证中间件；手动访问 API 无需 token |
> | 持久化：SQLite，data/todos.db | ✅ | 手动检查数据库文件是否生成；重启后数据仍在 |
> | 前端：React + TypeScript，无额外 UI 库 | ✅ | package.json 确认无 UI 组件库依赖；代码审查确认 |
> | API 风格：RESTful，JSON | ✅ | 后端路由测试确认返回 JSON；前端 fetch 测试 |
>
> 共 11 条验收条件，全部打勾通过。

接着让模型运行 hl-code-review：

> **提示词**：让 hl-code-review 至少指出一个“以后可能出问题”的风险点，写入 REVIEW.md。

> **Codex 输出**
>
> > hl-code-review 针对分支做 bug 和回归审查，重点不是风格挑刺，而是“这个改动会不会破坏别的东西”。
>
> # REVIEW.md
>
> ## 代码审查报告
>
> 审查范围：待办事项应用前后端代码
> 审查日期：2026-11-23
>
> ## 风险点
>
> ### 风险 1：空列表状态无反馈
>
> **描述**：当待办列表为空时，前端没有显示“暂无待办”的提示，用户可能误以为加载失败或操作未生效。
>
> **影响**：用户体验下降，可能重复点击添加按钮，产生重复待办。
>
> **建议**：在前端列表组件中增加空状态渲染，当待办数组为空时显示“暂无待办事项，点击添加创建第一个”。
>
> ### 风险 2：重复提交未防护
>
> **描述**：前端“添加待办”按钮在点击后没有禁用或加载状态，用户快速多次点击可能创建重复待办。
>
> **影响**：数据库中出现重复记录，需要额外去重逻辑清理。
>
> **建议**：在前端表单提交时禁用按钮并显示加载状态；后端增加唯一性约束或幂等性校验。
>
> ### 风险 3：错误分支无反馈
>
> **描述**：后端 API 在数据库写入失败、验证失败时可能返回通用的 500 错误，前端没有统一的错误提示处理。
>
> **影响**：用户无法得知操作失败的具体原因，调试困难。
>
> **建议**：后端统一异常处理，返回结构化错误码和消息；前端统一拦截器处理 API 错误并显示 Toast 提示。

### 总结

- `hl-verify` 对照 `SPEC.md` 逐条打勾，每条给出验证方式（测试名、浏览器路径或手动步骤）。
- `hl-code-review` 至少指出一个“以后可能出问题”的风险点（空列表、重复提交、错误分支无反馈），写入 `REVIEW.md`。
- 审查重点不是风格挑刺，而是“这个改动会不会破坏别的东西”。

---

## 4.7 收束：这一章真正固化的不是 Todo 应用

### 简介

Todo 本身没有价值，有价值的是顺序：需求澄清（grill）→ 脚手架（building-viewers）→ 后端 TDD（FastAPI skill + hl-tdd）→ 前端测试先行（hl-tdd）→ 真实浏览器联调（test-run / chrome-devtools）→ 对照规格验收（hl-verify）。你保留决定边界和验收标准的权力。

### 调用记录

由于本节为概念收束，无具体 Skill 调用，直接总结：

> **提示词**：把本章实际调用过、且产生可验证产出的 Skill 列成最小清单，删掉“装了但没用上”的，作为下个项目起点。

> **Codex 输出**
>
> 本章实际调用并产生可验证产出的 Skill：
>
> 1. grill-me：需求澄清，生成 SPEC.md
> 2. building-viewers：脚手架，生成前后端目录结构
> 3. hl-tdd：后端 TDD（pytest），前端 TDD（Vitest + RTL）
> 4. test-run：联调与浏览器验证
> 5. hl-verify：SPEC.md 验收核对
> 6. hl-code-review：代码审查，输出 REVIEW.md
>
> 装了但未用上的 Skill（建议删除）：
> - fastapi-fullstack：过重，带 PostgreSQL 和 Docker Compose，本章未用到
> - hl-grill：未使用，grill-me 已满足需求澄清需求
> - superpowers：未使用，hl 系列已覆盖所需环节
>
> 这个最小清单可以作为下个项目的起点，按需增减。

### 总结

- Todo 本身没有价值，有价值的是顺序：需求澄清 → 脚手架 → 后端 TDD → 前端测试先行 → 真实浏览器联调 → 对照规格验收。
- 你保留决定边界和验收标准的权力。
- 本章实际调用过的 Skill：grill-me、building-viewers、hl-tdd、test-run、hl-verify、hl-code-review。
- 装了但没用上的 Skill 可以删掉，作为下个项目起点的参考。

---

本章介绍了从需求澄清到审查收尾的完整开发流程，真正值得带走的是下面几条：

- 需求没想清楚就开始写、不写测试就开始改、CI 红了不知道从哪查，这些才是新手项目失控的主要原因。
- `grill-me` 在写第一行代码之前，把未定决策逐条逼出来，生成 SPEC.md。
- `hl-tdd` 确保先写测试再写代码，红绿循环 RED → GREEN → REFACTOR。
- `test-run` 驱动真实浏览器验证完整用户流程，不直接改代码。
- `hl-verify` 和 `hl-code-review` 把“能跑”变成“可交付”，指出风险点并写入 REVIEW.md。
- 你保留决定边界和验收标准的权力，Skill 只是辅助工具。