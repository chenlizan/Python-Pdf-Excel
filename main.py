import os
import pdfplumber
import tabula

HERE = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(HERE,
                    "files/Bertonia(2021)_Teachers' Preferences for Proximity and the Implications for Staffing Schools.pdf")
# with pdfplumber.open(path) as pdf:
#     print(len(pdf.pages))
#     # for i in range(len(pdf.pages)):
#     #     page = pdf.pages[i]
#     #     t = page.extract_tables(
#     #         {
#     #             "horizontal_strategy": "lines",
#     #             "vertical_strategy": "explicit",
#     #             "explicit_vertical_lines": [50, 100, 150],
#     #         })
#     #     print(t)
#
#     page = pdf.pages[7]
#     t = page.extract_text()
#     print(t)

dfs = tabula.read_pdf(path, pages='all')

print(len(dfs))

dfs
