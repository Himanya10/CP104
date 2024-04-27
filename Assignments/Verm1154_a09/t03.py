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
from functions import file_statistics
# Constants

# Process
file_handle = open("/Users/hl/Desktop/addresses.txt", "r", encoding="utf-8")

print(file_statistics(file_handle))