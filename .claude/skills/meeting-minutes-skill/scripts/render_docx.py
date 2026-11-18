#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt


def set_font(run, size=11, bold=False):
    run.font.name = "仿宋"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "仿宋")
    run.font.size = Pt(size)
    run.bold = bold


def set_para(paragraph, first_line=True):
    paragraph.paragraph_format.line_spacing = 1.5
    paragraph.paragraph_format.space_after = Pt(4)
    if first_line:
        paragraph.paragraph_format.first_line_indent = Pt(22)


def add_heading(document, text, level):
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER if level == 1 else WD_ALIGN_PARAGRAPH.LEFT
    run = paragraph.add_run(text)
    set_font(run, size=16 if level == 1 else 12, bold=True)
    set_para(paragraph, first_line=False)


def add_body(document, text):
    paragraph = document.add_paragraph()
    set_para(paragraph)
    run = paragraph.add_run(text)
    set_font(run)


def add_bullet(document, text):
    paragraph = document.add_paragraph(style=None)
    set_para(paragraph, first_line=False)
    run = paragraph.add_run(text)
    set_font(run)


def set_page_margins(section):
    section.top_margin = Pt(72)
    section.bottom_margin = Pt(72)
    section.left_margin = Pt(72)
    section.right_margin = Pt(72)


def main():
    parser = argparse.ArgumentParser(description="Render Chinese meeting-minutes Markdown to DOCX.")
    parser.add_argument("markdown", help="Input Markdown path")
    parser.add_argument("docx", help="Output DOCX path")
    args = parser.parse_args()

    markdown = Path(args.markdown).expanduser().resolve()
    output = Path(args.docx).expanduser().resolve()
    text = markdown.read_text(encoding="utf-8")

    document = Document()
    for section in document.sections:
        set_page_margins(section)

    styles = document.styles
    styles["Normal"].font.name = "仿宋"
    styles["Normal"]._element.rPr.rFonts.set(qn("w:eastAsia"), "仿宋")
    styles["Normal"].font.size = Pt(11)

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            add_heading(document, line[2:].strip(), 1)
        elif line.startswith("## "):
            add_heading(document, line[3:].strip(), 2)
        elif re.match(r"^[-*]\s+", line):
            add_bullet(document, re.sub(r"^[-*]\s+", "", line))
        else:
            line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
            add_body(document, line)

    output.parent.mkdir(parents=True, exist_ok=True)
    document.save(output)
    print(output)


if __name__ == "__main__":
    main()
