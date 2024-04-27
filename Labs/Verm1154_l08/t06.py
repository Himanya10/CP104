"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Himanya Verma
ID:        169051154
Email:   Verm1154@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""
# Imports
# Constants

from functions import list_stats

values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]
smallest, largest, total, average = list_stats(values)

print("list_stats([94, 96, -22, -79, -28, -26, -50, 71, 24, -32])")
print((smallest, largest, total, average))
