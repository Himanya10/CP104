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


def list_factors(number):
    """
    -------------------------------------------------------
    Returns a list of factors for a given positive integer.
    Factors are the whole numbers that the integer can be
    evenly divided by, excluding the number itself.
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer greater than 0 (int)
    Returns:
        factors - a list of factors for the given number (list of int)
    -------------------------------------------------------
    """
    factors = [i for i in range(1, number) if number % i == 0]
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_lists = []

    while True:
        try:
            number = int(input("Enter Positive Number: "))
            if number <= 0:
                break
            number_lists.append(number)
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    return number_lists


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in numbers (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = [index for index, value in enumerate(
        numbers) if value == target_number]
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    indexes_to_remove = [index for index,
                         value in enumerate(minuend) if value in subtrahend]

    # Remove values from minuend based on indexes found
    for index in reversed(indexes_to_remove):
        minuend.pop(index)

    return None


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    result = True  # Assume the list is sorted
    index = -1

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            result = False
            index = i + 1
            break  # Found the first value not in order, no need to continue

    return result, index
