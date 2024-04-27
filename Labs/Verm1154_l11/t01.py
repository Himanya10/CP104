"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
# Constants
from functions import generate_matrix_num

# Test case 1: Valid 'float' range
matrix_float = generate_matrix_num(3, 4, -10, 10, "float")
print("Matrix (float):")
print(matrix_float)

# Test case 2: Valid 'int' range
matrix_int = generate_matrix_num(3, 4, -10, 10, "int")
print("\nMatrix (int):")
print(matrix_int)
