#!/usr/bin/env python3
import argparse
import html
import sys
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def slide_number(name: str) -> int:
    stem = Path(name).stem
    digits = "".join(ch for ch in stem if ch.isdigit())
    return int(digits or 0)


def extract_slide_text(zf: ZipFile, member: str) -> list[str]:
    root = ET.fromstring(zf.read(member))
    texts = []
    for paragraph in root.findall(".//a:p", NS):
        parts = []
        for node in paragraph.findall(".//a:t", NS):
            if node.text:
                parts.append(node.text.strip())
        text = "".join(parts).strip()
        if text:
            texts.append(text)
    return texts


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from a PPTX file into Markdown notes.")
    parser.add_argument("pptx", help="PPTX file path")
    parser.add_argument("--output", required=True, help="Markdown output path")
    args = parser.parse_args()

    pptx = Path(args.pptx).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if pptx.suffix.lower() != ".pptx":
        print("Only .pptx is supported. Convert .ppt to .pptx first.", file=sys.stderr)
        raise SystemExit(2)
    if not pptx.exists():
        print(f"File not found: {pptx}", file=sys.stderr)
        raise SystemExit(1)

    lines = [f"# PPT 要点提取", "", f"- 文件：{pptx.name}", ""]
    with ZipFile(pptx) as zf:
        members = sorted(
            [m for m in zf.namelist() if m.startswith("ppt/slides/slide") and m.endswith(".xml")],
            key=slide_number,
        )
        for index, member in enumerate(members, start=1):
            texts = extract_slide_text(zf, member)
            if not texts:
                continue
            lines.append(f"## 第 {index} 页")
            lines.append("")
            for text in texts:
                lines.append(f"- {html.unescape(text)}")
            lines.append("")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
