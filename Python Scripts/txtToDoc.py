from docx import Document
import os
doc = Document()
with open("Assignment.txt", 'r', encoding='utf-8') as file:
    doc.add_paragraph(file.read())
doc.save("DS.docx")
print('Done')
os.startfile("DS.docx")