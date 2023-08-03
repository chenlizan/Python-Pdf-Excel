import os
import re

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from pypdf import PdfReader
import tabula

HERE = os.path.abspath(os.path.dirname(__file__))
file_dir = os.path.join(HERE, "files")

pattern = re.compile("table\\s[0-9a-zA-Z]+\\.", re.IGNORECASE)

for f in os.listdir(file_dir):
    print("开始分析 " + f + ".xlsx")
    reader = PdfReader(os.path.join(file_dir, f))
    wb = Workbook()
    ws = wb.active
    for paper_index in range(len(reader.pages)):
        print("#", end="")
        for df in tabula.read_pdf(os.path.join(file_dir, f), pages=paper_index + 1, multiple_tables=True):
            title = ""
            for chars in reader.pages[paper_index].extract_text().splitlines():
                mo = pattern.search(chars)
                if mo:
                    title = chars[mo.start():]
            ws.append([])
            ws.append(["第%d页" % (paper_index + 1), title])
            for r in dataframe_to_rows(df):
                ws.append(r)
    wb.save(f + ".xlsx")
    print("\n" + f + ".xlsx" + " 保存结果\n")
