import os

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo
from pypdf import PdfReader
import tabula

HERE = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(HERE,
                    "files/Bertonia(2021)_Teachers' Preferences for Proximity and the Implications for Staffing Schools.pdf")

# pr = PdfReader(path)
#
# print(pr.pages[9].extract_text())

wb = Workbook()
ws = wb.active

dfs = tabula.read_pdf(path, pages='all', multiple_tables=True)

print(len(dfs))

for df in dfs:
    for r in dataframe_to_rows(df):
        ws.append(r)

wb.save("table.xlsx")
