from docx import Document

# new word
docx_file = Document()
docx_file.save("./output/test.docx")


# open word
# docx_file = Document("./output/test.docx")


# doc convert docx    use module: pywin32 (windows)