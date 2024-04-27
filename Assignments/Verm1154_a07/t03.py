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

from functions import get_indexes, list_positives

numbers = list_positives()  # Assume the user enters [5, 1, 8, 9, 5, 2, 5, 3]
target_number = 5
result = get_indexes(numbers, target_number)
print(result)

numbers = list_positives()  # Assume the user enters [3, 7, 2, 5, 7, 3, 8]
target_number = 7
result = get_indexes(numbers, target_number)
print(result)

numbers = list_positives()  # Assume the user enters [1, 2, 3, 4, 5, 6]
target_number = 8
result = get_indexes(numbers, target_number)
print(result)
