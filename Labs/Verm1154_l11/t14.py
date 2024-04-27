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

from functions import matrix_transpose


def print_matrix(matrix):
    for row in matrix:
        print('\t'.join(map(str, row)))


def test_matrix_transpose():
    # Test case 1
    matrix1 = [[6, 4, 24], [1, -9, 8]]
    print("Original Matrix:")
    print_matrix(matrix1)

    transposed1 = matrix_transpose(matrix1)

    print("\nTransposed Matrix:")
    print_matrix(transposed1)


if __name__ == '__main__':
    test_matrix_transpose()
