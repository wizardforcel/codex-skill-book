# building-viewers 调用记录：脚手架替换清单与模板验证

## 背景

细纲第 4.2 节要求使用 `building-viewers` 的 React + TypeScript + FastAPI starter 生成前后端骨架：先输出“将要对模板做哪些替换”的清单并对照 `SPEC.md` 查覆盖，确认后再进入下一步；同时验证模板本身能跑通，并与重型方案 `fastapi-fullstack` 对照。共 3 条实操。

---

## 实操一：验证替换清单门禁

我们首先让模型生成骨架并输出替换清单：

> **提示词**：请使用 building-viewers 的 starter 模板为我的“待办事项”项目生成前后端目录。要求：先生成目录，然后输出“将要对模板做哪些替换”的清单——后端要改哪些路由和 schema、前端要改哪些页面和组件、依赖里哪些用不到。先不要进入下一步，我对照 SPEC.md 检查覆盖后再说。

> **Codex 输出**

> 思考过程：building-viewers 的原理是带一个可用的起始模板，但模板不等于成品——scaffold 后必须替换 domain 层、对接目标项目的依赖管理和启动命令。所以正确顺序是先给出“替换清单”，让用户对照规格确认，而不是闷头把所有文件生成完。SPEC.md 里待办事项的必做操作是：数据字段（标题、完成状态、创建时间）、添加操作、标记完成、按创建时间倒序列出、删除需要确认。
>
> 按照 starter 的目录结构，我把它拆成了三类替换项：

### 后端（FastAPI）替换清单

| 文件 | 模板现状 | 需要替换成 |
|------|---------|-----------|
| app/models.py | 示例的 User/Item 模型 | Todo 模型（id、title、completed、created_at） |
| app/schemas.py | 示例的 ItemSchema | TodoCreate / TodoOut / TodoUpdate |
| app/routers/items.py | 示例 CRUD | 待办 CRUD（列表、创建、标记完成、删除） |
| tests/ | 示例测试 | 对应 Todo 的 pytest（4.3 节做 TDD） |

### 前端（React + TypeScript）替换清单

| 文件 | 模板现状 | 需要替换成 |
|------|---------|-----------|
| src/App.tsx | 示例页面 | 待办列表页（输入框 + 列表 + 完成状态切换） |
| src/api.ts | 示例 fetch | 对接后端 /todos 的 API 封装 |
| src/components/* | 示例组件 | TodoList / TodoInput / TodoItem |

### 依赖中可能用不到的

- 模板自带的示例 UI 库（如 storybook 配置）——如果 SPEC 没有组件库要求，先不引入
- 用于演示的 mock 数据文件——正式开发用不到

以上清单已输出，等你对照 SPEC.md 确认覆盖所有必做操作后，我再进入下一步搭建。

---

## 实操二：验证模板可跑通

接着验证模板本身能不能跑：

> **提示词**：先不替换任何业务代码，直接按 starter 自带的说明启动一次前后端。我想确认傻瓜模板本身能跑起来（页面能开、默认 API 有响应），这样后面改动出问题才能分清是“模板坏了”还是“我们的改动坏了”。

> **Codex 输出**

> 思考过程：先跑通模板是排查问题的基础。如果模板本身就是坏的，后面所有替换都会归因错乱。所以这一步只做“启动冒烟测试”，不改任何业务逻辑。
>
> 按模板的 README 操作：后端 `uvicorn app.main:app` 启动在 8000 端口，访问 `/docs` 能看到示例 API 文档，访问 `/` 返回示例 JSON；前端 `npm run dev` 启动在 5173 端口，浏览器打开能看到 starter 的默认页面，默认 fetch 能调通示例接口。
>
> 冒烟结果：模板本身可运行，前后端都能启动、默认链路（前端页面 → 示例接口）通。这下基线确立了——之后的改动如果出错，可以确定责任在我们这边。

---

## 实操三：对照重型方案

最后只读地对照备选方案：

> **提示词**：fs.add("请你不要实际运行 fastapi-fullstack，只读地打开它的 README 和配置，列出它与 building-viewers 的差异点（数据库、容器、目录结构），用 5 行的表格总结一下，说明什么情况值得选‘重’方案。

> **Codex 输出**

> 思考过程：fastapi-fullstack 基于 tiangolo/full-stack-fastapi-template，默认就带 PostgreSQL 和 Docker Compose，是“生产形态”的重量级方案；building-viewers 是轻量 starter，适合快速起骨架、学 TDD。对照它们只为了知道什么时候切换，不是真的要装。

| 维度 | building-viewers | fastapi-fullstack |
|------|-----------------|-------------------|
| 数据库 | 默认 SQLite（轻量起跑） | PostgreSQL（生产标配） |
| 容器 | 无 Docker，本地直接跑 | Docker Compose 一键起 |
| 目录结构 | 简单前后端两段 | 多目录（backend/app、frontend、nginx 等） |
| 引入成本 | 低，适合教学和快速原型 | 高，适合要往生产走的项目 |
| 适用场景 | 本书 4.3—4.6 的 TDD 流程 | 想继续往 CI/CD、部署形态演进时选读 |

结论：先学轻的，够用；等要上生产形态（多人协作、数据库迁移、容器化部署）再考虑切重的。

---

## 总结

三个实操验证了 4.2 节的核心：替换清单门禁让模板不被当成完成品；冒烟测试确立了“模板可跑”的基线；与 fastapi-fullstack 的对照明确了轻/重方案的取舍。脚手架这一步的关键产出不是目录本身，而是“你知道模板里每一块将来怎么改”。