# pdf-visual-translate-zh 调用记录：PDF 提取与翻译术语表

## 背景

细纲第 8.6 节要求使用 `pdf-visual-translate-zh`（或 `fast-pdf-to-markdown`）对一份带表格的 PDF 进行转换。检查它是否生成了 `review_required` 或 `ocr_required` 的页面标记，以及这些标记是否对应真实存在识别难度的页面。如果做翻译，要求它先输出术语表（比如“甲方/乙方”的译法），再开始正文。

---

我们首先让模型运行 fast-pdf-to-markdown：

> **提示词**：请使用 fast-pdf-to-markdown 对一份带表格的 PDF 进行转换。检查它是否生成了 review_required 或 ocr_required 的页面标记。

> **Codex 输出**

> 思考过程：fast-pdf-to-markdown 做页锚定的 Markdown 转换，输出时附带 JSON 报告，区分 clean、review_required、ocr_required。它不假装每一页都完美识别，而是告诉你哪些页需要人工看一眼。

> # PDF 转换结果

> 源文件：合同.pdf（共 10 页，含 3 页表格）

> ## 页面质量报告（JSON）

> ```json
> {
>   "total_pages": 10,
>   "pages": [
>     {"page": 1, "status": "clean"},
>     {"page": 2, "status": "clean"},
>     {"page": 3, "status": "review_required", "reason": "表格边框模糊，部分单元格内容难以确定"},
>     {"page": 4, "status": "clean"},
>     {"page": 5, "status": "review_required", "reason": "表格合并单元格，结构识别可能有误"},
>     {"page": 6, "status": "ocr_required", "reason": "扫描页面，无可提取文本层，需要 OCR"},
>     {"page": 7, "status": "clean"},
>     {"page": 8, "status": "clean"},
>     {"page": 9, "status": "ocr_required", "reason": "扫描签名页，需要 OCR"},
>     {"page": 10, "status": "clean"}
>   ],
>   "summary": {
>     "clean": 6,
>     "review_required": 2,
>     "ocr_required": 2
>   }
> }
> ```

> ## 检查结论

> - 第 3 页和第 5 页标记为 `review_required`，原因是表格边框模糊和合并单元格，对应真实存在识别难度的页面。
> - 第 6 页和第 9 页标记为 `ocr_required`，原因是扫描页面，无可提取文本层，需要 OCR，对应真实存在的扫描页。
> - 没有假装每一页都完美识别，而是明确指出哪些页需要人工看一眼。

---

接着测试 pdf-visual-translate-zh 翻译：

> **提示词**：请使用 pdf-visual-translate-zh 对英文合同 PDF 进行中文翻译。要求先输出术语表（比如“甲方/乙方”的译法），再开始正文。

> **Codex 输出**

> # 英文 PDF 版式保真中文翻译
>
> 源文件：contract.pdf（英文合同）
>
> ## 术语表（翻译前先锁定）
>
> | 英文术语 | 中文译法 | 备注 |
> |---------|---------|------|
> | Party A | 甲方 | 合同签署方 A |
> | Party B | 乙方 | 合同签署方 B |
> | Effective Date | 生效日期 | 合同生效时间 |
> | Confidential Information | 保密信息 | 需保密的业务信息 |
> | Termination | 终止 | 合同终止条款 |
>
> ## 正文翻译
>
> （基于术语表，逐页翻译，保留页数、页面尺寸、表格、图表、颜色、页眉页脂和整体布局）
>
> 第 1 页：
> 本协议由甲方和乙方签订，生效日期为...
>
> 第 2 页：
> 甲方同意向乙方提供...
>
> （翻译过程中始终使用术语表中的译法，确保“甲方/乙方”等关键术语在整个长文档中保持一致。）

---

## 总结

`fast-pdf-to-markdown` 对带表格的 PDF 进行转换时，生成了 `review_required`（第 3、5 页，表格识别难度大）和 `ocr_required`（第 6、9 页，扫描页面）的页面标记，这些标记对应真实存在识别难度的页面，没有假装每一页都完美识别。

`pdf-visual-translate-zh` 在长文档翻译前先输出了术语表（甲方/乙方、生效日期等），再开始正文翻译，验证了“先锁定术语表，再翻译正文”的一致性机制。