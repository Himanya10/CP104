"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
# Constants

# functions.py


def total_wins():
    """
    -------------------------------------------------------
    Prints the output of a game using user input.
    Use: result = total_wins()
    Parameters:
        none
    Returns:
        total_wins() ->
        Enter the winning team: purple
        Enter the winning team: purple
        Enter the winning team: yellow
        Enter the winning team: purple
        Enter the winning team: gold
        Enter the winning team: gold
        Enter the winning team: orange
        Enter the winning team:
        (3, 2)
    -------------------------------------------------------
    """
    purple_count = 0
    gold_count = 0

    while True:
        team = input("Enter the winning team: ")

        if team == "":
            break  # Break the loop if an empty string is entered

        if team.lower() == "purple":
            purple_count += 1
        elif team.lower() == "gold":
            gold_count += 1

    return purple_count, gold_count


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    prime = True
    if number <= 1:
        prime = False
    elif number > 3:
        if number % 2 == 0 or number % 3 == 0:
            prime = False
        else:
            i = 5
            while i * i <= number and prime:
                if number % i == 0 or number % (i + 2) == 0:
                    prime = False
                i += 6
    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    month = 1
    print(f"Principal: ${principal_amount}")
    print(f"Interest Rate: {interest_rate}%")
    print(f"Monthly Payment: ${payment}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while principal_amount > 0:
        interest = (interest_rate / 100 / 12) * principal_amount
        principal_amount = principal_amount + interest - payment
        if principal_amount < 0:
            payment += principal_amount
            principal_amount = 0
        print("{:<5} {:<10.2f} {:<10.2f} {:<10.2f}".format(
            month, interest, payment, principal_amount))
        month += 1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    if number < 0:
        number = abs(number)

    if number == 0:
        digits = 1

    digits = 0

    while number > 0:
        number //= 10
        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    return total
