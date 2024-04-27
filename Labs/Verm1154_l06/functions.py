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


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """

    total = 0
    for current in range(start, finish + 1, increment):
        total += current
    return total


def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    if width < 1:
        return

    for i in range(width):
        if i == 0 or i == width - 1:
            print(char * (i + 1))
        else:
            spaces = " " * (i - 1)
            line = char + spaces + char
            print(line)


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None


    ------------------------------------------------------
"""
    print("Age        Salary")
    print("-----------------")
    for i in range(age, 66,):
        print(f"{i}{salary:>15,.2f}")
        salary = salary*(1+(increase/100))
    return


def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    print("              Cross-Sectional  Moment of    Section")
    print("Base  Height  Area             Inertia      Modulus")
    print("---------------------------------------------------")

    for base in range(b_min, b_max + b_inc, b_inc):
        for height in range(h_min, h_max + h_inc, h_inc):
            area = base * height
            inertia = base * (height**3) / 12
            modulus = base * height ** 2 / 6
            print(
                f"{base:>4d}  x  {height:>5d}{area:>17.2f}{inertia:>11.2f}{modulus:>9.2f}")

    return None


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6-week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------

    total_hours = 0

    for week in range(1, 7):
        print(f"Week {week}")
        week_total = 0

        for ia in range(1, ia_count + 1):
            ia_hours = float(input(f"  Marking hours for IA {ia}: "))
            week_total += ia_hours

        total_hours += week_total

    return total_hours
    """
    time_keep = []
    NUM_WEEKS = 6
    for y in range(1, NUM_WEEKS+1, 1):
        print(f"week {y}")
        for x in range(1, ia_count+1, 1):
            hr_worked = float(input(f"Marking hours for IA {x}:"))
            time_keep.append(hr_worked)
    total_hours = sum(time_keep)
    return total_hours
