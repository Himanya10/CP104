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

from functions import get_digit_name

n = int(input("Enter a digit (0-9): "))  # Correct the input line
name = get_digit_name(n)

print(f"get_digit_name({n}):")
print(name)
