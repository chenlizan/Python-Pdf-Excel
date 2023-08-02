import os

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from pypdf import PdfReader
import tabula

wb = Workbook()

HERE = os.path.abspath(os.path.dirname(__file__))
file_dir = HERE + "\\files"

for f in os.listdir(file_dir):
    ws = wb.active
    for df in tabula.read_pdf(os.path.join(file_dir, f), pages='all', multiple_tables=True):
        for r in dataframe_to_rows(df):
            ws.append(r)
    wb.save(f + ".xlsx")
    print(f + ".xlsx" + " saved")
