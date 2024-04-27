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

from functions import verify_sorted, list_positives


numbers1 = list_positives()  # Assume the user enters [23, 41, 99]
result1 = verify_sorted(numbers1)
print(result1)


numbers2 = list_positives()  # Assume the user enters [99, 23, 41]
result2 = verify_sorted(numbers2)
print(result2)

numbers3 = list_positives()  # Assume the user enters [1, 2, 3, 4, 5, 6]
result3 = verify_sorted(numbers3)
print(result3)
