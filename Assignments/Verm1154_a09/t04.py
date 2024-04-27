"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   Verm1154@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering
# Constants

# Process
fh_read = open("/Users/hl/Desktop/wilde.txt", "r", encoding= "utf-8")
fh_write = open("/Users/hl/Desktop/wilde_numbered.txt", "w", encoding= "utf-8")

line_numbering(fh_read, fh_write)