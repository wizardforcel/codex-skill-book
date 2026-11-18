# 断网 RAG 实现流程

## 核心理解

大模型每次调用都是新的开始。固定检索逻辑不靠模型记忆，而靠模型外部的本地程序。

标准流程：

```text
用户问题
-> 本地 RAG 控制程序
-> 检索知识库
-> 过滤规则和 metadata
-> 取出证据片段
-> 拼接 prompt
-> 调用断网大模型
-> 输出答案
```

不要让模型自己决定是否检索。断网知识库问答应默认每次先检索。

## Prompt 模板

```text
你必须只根据下面的知识库内容回答。
如果知识库没有足够依据，请说：库内没有足够依据。
不要使用外部知识补完。

知识库规则摘要：
{rules_summary}

检索到的知识库内容：
{contexts}

用户问题：
{question}
```

## 检索步骤

```text
1. 接收用户问题。
2. 读取规则入口和检索规则。
3. 在正式库索引中检索。
4. 排除 raw、pending、rejected、unverified、Inbox、Archive、trash。
5. 优先选择稳定卡片、正式笔记、项目主页、参考资料。
6. 打开原始 Markdown 核验。
7. 把证据、路径、标题、summary 放入 prompt。
8. 让模型基于证据回答。
```

## metadata 过滤

优先保留：

```text
status: reviewed
status: evergreen
truth_status: source_backed
truth_status: self_confirmed
```

排除：

```text
status: raw
truth_status: unverified
truth_status: discarded
type: inbox
待确认
拒绝
待归类
```

## 垂直领域库

每个垂直领域应有自己的规则入口和正式库范围：

```text
法律库 -> 只检索法律正式库
医学库 -> 只检索医学正式库
项目库 -> 只检索项目正式库
个人思辨库 -> 优先检索提炼卡片
```

固定逻辑来自：

```text
程序强制检索
规则限制范围
metadata 过滤可信度
prompt 禁止外部补完
无依据则说明不足
```
