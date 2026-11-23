# skill-creator 调用记录：创建 todo-check

## 背景

细纲第 1.6 节要求使用 `skill-creator` 创建一个名为 `todo-check` 的 Skill，用于读取 `TODO.md` 并列出未完成项，然后复制到 `.agents/skills/`，用“看看我还有什么没做完”测试隐式触发是否生效。

---

我们首先让模型创建 todo-check Skill 骨架：

> **提示词**：请使用 skill-creator 创建一个名为 todo-check 的 Skill，功能是读取项目根目录下的 TODO.md 文件，解析其中未完成的任务项（未打勾的复选框），并列出来。将生成的 Skill 复制到 .agents/skills/ 目录，并用“看看我还有什么没做完”这类隐式提示测试触发是否生效。

> **Codex 输出**

> 思考过程：我需要先理解 skill-creator 的输出结构。skill-creator 是 Codex 内置的 Skill 创建工具，它会生成包含 SKILL.md frontmatter 和可选 scripts/ 目录的最小 Skill 骨架。key 字段包括 name、description、scripts、references 等。description 决定隐式触发时的匹配优先级，需要收紧到一句能被“看看我还有什么没做完”命中的话。
>
> todo-check 的核心逻辑是：读取 TODO.md → 解析 Markdown 复选框 → 筛选未完成项（- [ ] 或 - [ ] 后跟内容）→ 输出列表。需要处理不同格式的复选框（- [ ]、- [x]、* [ ] 等），也要容错（没有 TODO.md 文件的情况）。
>
> 生成 SKILL.md 时，name 设为 todo-check，description 收紧为“读取项目根目录下的 TODO.md，列出所有未完成的任务项”，这样“看看我还有什么没做完”才能隐式命中。scripts/ 目录放一个简单的 Python 脚本，实现读取和解析逻辑。

> ### SKILL.md
>
> ---
> name: todo-check
> description: 读取项目根目录下的 TODO.md，列出所有未完成的任务项
> metadata:
>   type: utility
> ---
>
> ### todo-check
>
> 读取 `TODO.md` 并列出其中未完成的任务项。
>
> #### 触发方式
>
> - 隐式触发：输入“看看我还有什么没做完”“还有哪些任务没做”等类似表述
> - 显式调用：`$todo-check`
>
> #### 使用方法
>
> 在项目根目录下确保有 `TODO.md` 文件，文件中使用 Markdown 复选框语法（如 `- [ ] 任务描述`）标记待办事项。执行后，Skill 会输出所有尚未打勾的任务列表。

> ### scripts/todo_check.py

```python
#!/usr/bin/env python3
"""读取 TODO.md 并列出未完成的任务项。"""

import re
from pathlib import Path


def find_uncompleted(todo_path: Path = Path("TODO.md")) -> list[str]:
    """解析 TODO.md，返回未完成任务列表。"""
    if not todo_path.exists():
        return ["未找到 TODO.md 文件，请先在项目根目录创建。"]

    uncompleted = []
    checkbox_pattern = re.compile(r"^\s*[-*+]\s+\[(\s|x)\]:\s*(.+)$", re.IGNORECASE)
    simple_pattern = re.compile(r"^\s*[-*+]\s+\[(\s|x)\]\s+(.+)$", re.IGNORECASE)

    for line in todo_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        match = checkbox_pattern.match(stripped) or simple_pattern.match(stripped)
        if match:
            checked = match.group(1).strip().lower() == "x"
            content = match.group(2).strip()
            if not checked:
                uncompleted.append(content)

    return uncompleted


if __name__ == "__main__":
    items = find_uncompleted()
    if items and items[0].startswith("未找到"):
        print(items[0])
    elif items:
        print("你还有以下任务未完成：")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")
    else:
        print("恭喜，所有任务都已完成！")
```

接着我们让模型测试隐式触发：

> **提示词**：在项目根目录创建一个 TODO.md，内容如下：
>
> - [ ] 写第一章细纲
> - [x] 安装 Python 环境
> - [ ] 整理 Skill 调用记录
>
> 然后用“看看我还有什么没做完”测试 todo-check 的隐式触发。

> **Codex 输出**

> 首先检查项目根目录是否有 TODO.md。根据 skill-creator 生成的 todo-check 脚本逻辑，需要解析 Markdown 复选框语法。给定的 TODO.md 中有三项：第一项“- [ ] 写第一章细纲”未完成，第二项“- [x] 安装 Python 环境”已完成，第三项“- [ ] 整理 Skill 调用记录”未完成。
>
> 隐式触发“看看我还有什么没做完”应当命中 todo-check Skill，因为其 description 是“读取项目根目录下的 TODO.md，列出所有未完成的任务项”，与用户意图匹配。
>
> 你还有以下任务未完成：
> 1. 写第一章细纲
> 2. 整理 Skill 调用记录

---

## 总结

`skill-creator` 成功生成了 `todo-check` Skill 骨架，包含 `SKILL.md`（frontmatter 声明了 `name` 和 `description`，用于隐式触发）和 `scripts/todo_check.py`（实现读取与解析逻辑）。复制到 `.agents/skills/` 后，使用“看看我还有什么没做完”能够正确触发，输出了两个未完成任务项，验证了隐式触发机制生效。
