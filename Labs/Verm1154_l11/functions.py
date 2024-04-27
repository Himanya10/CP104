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
import random
# Constants


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if value_type == "float":
                row.append(random.uniform(low, high))
            elif value_type == "int":
                row.append(random.randint(low, high))
        matrix.append(row)
    return matrix, i, j


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    if not matrix:
        print("Empty matrix.")
        return

    # Print column headings
    print(f"{' ':>8}", end="")
    for j in range(len(matrix[0])):
        print(f"{j:>7}", end="")
    print()

    # Print matrix rows
    for i in range(len(matrix)):
        print(f"{i:>2}", end="")
        for j in range(len(matrix[i])):
            if value_type == 'float':
                if isinstance(matrix[i][j], float):
                    print(f"{matrix[i][j]:>7.2f}", end="")
                else:
                    print(f"{matrix[i][j]:>7}", end="")
            elif value_type == 'int':
                print(f"{matrix[i][j]:>7}", end="")
        print()


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    if not matrix or not matrix[0]:
        raise ValueError("Empty matrix.")

    rows, cols = len(matrix), len(matrix[0])
    min_val, max_val = matrix[0][0], matrix[0][0]
    s_loc, l_loc = [0, 0], [0, 0]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                s_loc = [i, j]
            elif matrix[i][j] > max_val:
                max_val = matrix[i][j]
                l_loc = [i, j]

    return s_loc, l_loc


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= num
    return None


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = [[matrix[j][i]
                   for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed
