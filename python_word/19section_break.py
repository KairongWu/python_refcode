from docx import Document
from docx.enum.section import WD_SECTION_START

# 节与分节符

doc = Document()

print(doc.sections, len(doc.sections))  # 默认必须有一个节

s1 = doc.add_section(WD_SECTION_START.NEW_PAGE)
print(s1.start_type)
s2 = doc.add_section(WD_SECTION_START.CONTINUOUS)
print(s2.start_type)
s3 = doc.add_section(WD_SECTION_START.ODD_PAGE)
print(s3.start_type)
s4 = doc.add_section(WD_SECTION_START.EVEN_PAGE)
print(s4.start_type)

print(doc.sections, len(doc.sections))  # 页数变成 5 页， 下一页分节符

doc.save("./output/test.docx")