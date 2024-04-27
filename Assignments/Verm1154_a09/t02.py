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
from functions import read_integers
# Constants

# Process
file_handle = open("/Users/hl/Desktop/numbers.txt", "r", encoding="utf-8")

print(read_integers(file_handle))