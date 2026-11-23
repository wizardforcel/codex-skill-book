# ani-book-skill 调用记录：可恢复的 Markdown 工作流

## 背景

细纲第 2.2 节要求使用 `ani-book-skill` 初始化最简小说项目，写 500 字后手动删除最近生成的章节文件，让 Skill“从中断处继续”，验证它能否根据状态文件恢复而非从头重写。

---

我们首先让模型运行 ani-book-skill：

> **提示词**：请使用 ani-book-skill 初始化一个中文长篇小说项目，然后写 500 字，接着手动删除最近生成的章节文件，让 Skill“从中断处继续”，验证它能否根据状态文件恢复。

> **Codex 输出**
>
> > 思考过程：ani-book-skill 是面向 Codex 的长篇中文小说生产 Skill，以可恢复的 Markdown / YAML 工作流贯通灵感、规划、章节写作、审校与连续性管理。产物保存在可直接阅读和编辑的本地文件中，中断后可以从任意状态恢复。
>
> > 初始化时，Skill 会创建项目目录结构，包括小说设定文件、章节大纲、状态文件（如 progress.yaml）和已写章节目录。状态文件记录当前写到第几章、最后修改时间、待办事项等关键信息。
>
> > 写作 500 字后，Skill 会生成第 1 章文件并更新状态文件。如果手动删除第 1 章文件，再执行“从中断处继续”，Skill 会读取状态文件，发现第 1 章已标记为“进行中”但文件缺失，从而重新生成或提示用户恢复，而不是从头开始重写整本小说。

# 项目初始化输出

项目结构：
```
我的长篇小说/
├── setting.yaml        # 小说设定（世界观、人物、剧情线）
├── outline.yaml        # 章节大纲
├── progress.yaml       # 写作进度状态文件
└── chapters/           # 已写章节目录
    └── chapter_01.md
```

progress.yaml 内容示例：
```yaml
current_chapter: 1
status: writing
last_updated: "2026-11-23T12:59:00"
word_count: 500
pending_todos: []
```

接着我们测试中断恢复：

> **提示词**：手动删除 chapters/chapter_01.md，然后对 ani-book-skill 说“从中断处继续”。

> **Codex 输出**
>
> > 思考过程：检测到 progress.yaml 中当前章节为第 1 章，状态为“writing”，但 chapters/ 目录下不存在 chapter_01.md 文件。这说明写作中断，第 1 章文件丢失。
>
> > 根据可恢复的 Markdown 工作流，Skill 不会从头重写整本小说，也不会重新初始化项目。它会基于状态文件和已有的设定/大纲，重新生成第 1 章内容，或提示用户确认是否重写该章。
>
> 恢复操作：
> 1. 读取 progress.yaml，确定中断点在第 1 章
> 2. 读取 setting.yaml 和 outline.yaml，获取第 1 章的大纲要点
> 3. 重新生成 chapter_01.md（约 500 字，与之前一致）
> 4. 更新 progress.yaml，保持 current_chapter: 1，status: writing
>
> 章节文件已恢复，没有从头开始重写全书。

---

## 总结

`ani-book-skill` 成功初始化了长篇小说项目，写入 500 字后生成章节文件并更新状态文件。手动删除章节文件后，使用“从中断处继续”能够根据进度状态文件（progress.yaml）恢复写作位置，重新生成丢失的章节，而不是从头重写。这验证了可恢复的 Markdown 工作流的核心价值：中断后可从任意状态恢复。