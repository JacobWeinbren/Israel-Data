import tabula
import pandas as pd
from functools import reduce
 
pdf_path = "../data/19/AllStations.pdf"
 
tables = tabula.read_pdf(pdf_path, pages = "all", multiple_tables = True)
tables = pd.concat(tables)
tables.to_excel("../output/19_fixed.xlsx", sheet_name='DataSheet', index = False)