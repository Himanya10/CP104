"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-10-14"
-------------------------------------------------------
"""
# Imports
# Constants
from functions import multiply_fractions

num1 = 1
den1 = 2
num2 = 3
den2 = 4

num, den, product = multiply_fractions(num1, den1, num2, den2)
print(
    f"multiply_fractions({num1}, {den1}, {num2}, {den2}) -> {num}, {den}, {product}")
