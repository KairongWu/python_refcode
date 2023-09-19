from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Mm
import os

doc = Document()

table = doc.add_table(3, 2, "Table Grid")

# 设置表格高度和宽度
table.autofit = False
table.rows[0].height = Mm(30)
table.columns[0].width = Mm(50)  # 设置不成功，word 会自动调整列宽度

print(table.style)

styles = doc.styles
table_styles = [s for s in styles if s.type == WD_STYLE_TYPE.TABLE]
for style in table_styles:
    print(style.name)

doc.save('./output/test.docx')