import ctypes
import os
import camelot

from ctypes.util import find_library

print(find_library("".join(("gsdll", str(ctypes.sizeof(ctypes.c_voidp) * 8), ".dll"))))

HERE = os.path.abspath(os.path.dirname(__file__))
file_dir = os.path.join(HERE, "files")

for f in os.listdir(file_dir):
    tables = camelot.read_pdf(os.path.join(file_dir, f), pages="1-30")
    print(tables)

