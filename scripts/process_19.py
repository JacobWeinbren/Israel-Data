from fastnumbers import fast_real
from docx import Document
import pandas as pd
import re

"""
The 19th Knesset is a PDF, this makes it a .xlsx file
"""

#Read Document
path = "../data/19/AllStations.docx"
doc = Document(path)

#To add space after numbers
rx = re.compile(r'(-?[0-9]+\.?[0-9]*)')

#Headers
data = [['\nצורפ ל-', 'בוחרי\nכנסת', 'נגישה\nמיוחדת', '\nנגישה', '\nמקום קלפי', '\nכתובת קלפי', 'סמל\nקלפי', '\nשם ישוב בחירות', 'סמל ישוב\nבחירות', '\nשם ועדה', '\nסמל ועדה']]

for table_num, table in enumerate(doc.tables):
    for row_num, row in enumerate(table.rows):
        row_text = [c.text for c in row.cells]

        if (row_text != data[0]):

            #Clear the text
            for val in range(0,11):
                row_text[val] = row_text[val].replace("\n", "")
            
            #Remove stray brackets
            row_text[6] = row_text[6].replace("(","")

            #add space to numbers and convert to type
            for val in range(0,11):
                temp = row_text[val]
                temp = fast_real(temp)

                if isinstance(temp, str):
                    temp = rx.sub(" \\1 ", temp)
                    temp = temp.rstrip(',').strip()

                row_text[val] = temp

            data.append(row_text)

    if table_num % 10 == 0:
        print("Reading Page", table_num)

#Writes to meta file
df = pd.DataFrame(data)
writer = pd.ExcelWriter('../output/meta/19.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='DataSheet', index=False)
writer.save()