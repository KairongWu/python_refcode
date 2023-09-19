from docx import Document

docx_file = Document('./output/test.docx')

for paragraph in doc.paragraphs:
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None

docx_file.save("./output/test.docx")