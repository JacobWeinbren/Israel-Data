from docx import Document
import re

import pandas as pd

path = "19.docx"
doc = Document(path)

data = [['\nצורפ ל-', 'בוחרי\nכנסת', 'נגישה\nמיוחדת', '\nנגישה', '\nמקום קלפי', '\nכתובת קלפי', 'סמל\nקלפי', '\nשם ישוב בחירות', 'סמל ישוב\nבחירות', '\nשם ועדה', '\nסמל ועדה']]

for table_num, table in enumerate(doc.tables):
    for row_num, row in enumerate(table.rows):
        row_text = [c.text for c in row.cells]

        if (row_text != data[0]):

	        val = row_text[5]
	        
	        val = re.sub('(\d+(\.\d+)?)', r' \1 ', val)
	        val = val.replace(' ,', '')
	        val = val.replace('\n','')

	        row_text[5] = val
	       
	        data.append(row_text)
        print(table_num, row_num)

df = pd.DataFrame(data)
writer = pd.ExcelWriter('merged.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='DataSheet', index=False)
writer.save()