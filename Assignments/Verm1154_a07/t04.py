"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
# Constants

from functions import list_subtract, list_positives


minuend = list_positives()  # Assume the user enters [5, 5, 4, 5]
subtrahend = [5]
list_subtract(minuend, subtrahend)
print("minuend after:", minuend)  # Output: [4]


minuend = list_positives()  # Assume the user enters [3, 7, 2, 5, 7, 3, 8]
subtrahend = [7, 3]
list_subtract(minuend, subtrahend)
print("minuend after:", minuend)

minuend = list_positives()  # Assume the user enters [1, 2, 3, 4, 5, 6]
subtrahend = [8]
list_subtract(minuend, subtrahend)
print("minuend after:", minuend)
