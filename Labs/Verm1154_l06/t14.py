"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Himanya Verma
ID:        169051154
Email:   Verm1154@mylaurier.ca
__updated__ = "2023-10-26"
-------------------------------------------------------
"""
# Imports
# Constants

from functions import ia_hours

ia_count = int(input("Enter the number of IAs: "))
total_hours = ia_hours(ia_count)
print(f"\nTotal hours worked by all IAs: {total_hours:.2f}")
