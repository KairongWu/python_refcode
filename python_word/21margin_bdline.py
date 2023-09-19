from docx import Document
from docx.shared import Cm

# 页边距和装订线

doc = Document()

section = doc.sections[0]

print(section.top_margin.cm)
print(section.bottom_margin.cm)
print(section.left_margin.cm)
print(section.right_margin.cm)

section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(3)
section.right_margin = Cm(3)

print(section.gutter.cm)

section.gutter = Cm(1)

doc.save('./output/test.docx')