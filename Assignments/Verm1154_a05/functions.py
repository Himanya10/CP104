"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Himanya Verma
ID:        169051154
Email:   Verm1154@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
# Constants


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    if number < 0:
        product = None
    elif number == 0:
        product = 1
    else:
        product = 1
        for i in range(1, number + 1):
            product *= i
        return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of calories burned every five minutes on a treadmill.
    Use: total = calories_treadmill(number)
    Parameters:
        per_min - calories burned per minute (float)
        minutes - total number of minutes run (int)
    Returns:
        calories_treadmill(4.1, 20) ->
          5  20.5
         10  41.0
         15  61.5
         20  82.0
    -------------------------------------------------------
    """
    print("Minute     Calories Burned")

    for time in range(5, minutes + 1, 5):
        calories_burned = per_min * time
        print(f"{time:2}    {calories_burned:.1f}")
    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an arrow of '#' characters pointing up.
    Use: arrow = arrow_up(4)  
    Parameters:
        rows (int): Number of rows in the arrow.

    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(1, rows + 1):
        if i == 1:
            print(" " * (rows - 1) + "#")
        else:
            print(" " * (rows - i) + "#" + " " * ((i - 2) * 2 + 1) + "#")
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    string = "      "
    for i in range(start_num, stop_num+1):
        string = string+"    "+str(i)
    print(string)
    print('      '+'-'*(len(string)-6))

    for i in range(start_num, stop_num+1):
        string = ""
        space = "    "
        string = space + str(i)+' |'

        for j in range(start_num, stop_num+1):
            space = " "*(5-(len(str(i*j))))
            string = string + space + str(i*j)

        print(string)
    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ---------
    """
    total = 0
    for _ in range(count):
        total += start
        start += increment
    return total
