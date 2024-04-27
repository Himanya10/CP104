"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Himanya Verma
ID:        169051154
Email:   Verm1154@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
# Constants
DIGIT_NAMES = ["zero", "one", "two", "three",
               "four", "five", "six", "seven", "eight", "nine"]


def get_digit_name(n):
    """
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    """
    return DIGIT_NAMES[n]


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = largest = total = values[0]

    for value in values[1:]:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
        total += value

    average = total / len(values)

    return smallest, largest, total, average


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    indexes = [i for i, v in enumerate(values) if v == value]
    return indexes


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    if len(source1) != len(source2):
        raise ValueError("Input lists must be of the same length")
    target = [sum(x) for x in zip(source1, source2)]
    return target


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = list(set(source1) & set(source2))
    return target 
