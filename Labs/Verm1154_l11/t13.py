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
from functions import matrix_scalar_multiply


def print_matrix(matrix):
    for row in matrix:
        print(row)


def test_matrix_scalar_multiply():
    # Test case 1
    matrix1 = [[-6, -3, -7], [-4, 5, -10]]
    print("Original Matrix:")
    print_matrix(matrix1)

    num1 = 5
    matrix_scalar_multiply(matrix1, num1)

    print(f"\nMatrix after multiplying by {num1}:")
    print_matrix(matrix1)


if __name__ == '__main__':
    test_matrix_scalar_multiply()
