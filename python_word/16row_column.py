from docx import Document
from docx.shared import Mm

doc = Document()
table = doc.add_table(3, 2)

table.add_row()
table.add_column(width=Mm(50))

print(table.rows, len(table.rows))
print(table.columns, len(table.columns))

for row in table.rows[2:]:
    print("row: ", row)
    print("row: ", row._index, row.height)
    row.height = Mm(30)

for column in table.columns:
    print("column: ", column)
    print("column: ", column._index, column.width.mm)

doc.save('./output/test.docx')