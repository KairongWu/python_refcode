from docx import Document
from docx.enum.section import WD_ORIENTATION
from docx.shared import Cm

# 纸张方向与尺寸

doc = Document()

section = doc.sections[0]
print(section.page_width.cm)  # 页面宽度
print(section.page_height.cm)  # 页面高度

# 修改页面为 A4 大小
section.page_width = Cm(21)
section.page_height = Cm(29.7)

# 修改纵向与横向
print(section.orientation)
section.orientation = WD_ORIENTATION.LANDSCAPE
print(section.orientation)  # 修改失败， 尺寸没有发生改变

# section.page_width = Cm(29.7)
# section.page_height = Cm(21)
section.page_width, section.page_height = section.page_height, section.page_width

doc.save('./output/test.docx')