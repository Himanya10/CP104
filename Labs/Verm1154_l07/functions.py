"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Himanya Verma
ID:        169051154
Email:   Verm1154@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
# Constants
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
     """
    number = randint(1, high)
    count = 0

    print("Welcome to the Higher-Lower Guessing Game!")
    print(f"Guess a number between 1 and {high}.")

    while True:
        count += 1
        guess = int(input("Guess: "))
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations - good guess!")
            break

    print(f"You made {count} guesses.")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    if target <= 0:
        power = 1
    while power < target:
        power *= 2
    return power


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    if target <= 0:
        square_sum = 1

    n = 1
    while True:
        square_sum = sum(x**2 for x in range(1, n+1))
        if square_sum >= target:
            return square_sum
        n += 1


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    total_expenses = 0.0
    while True:
        expense = input("Enter an expense (0 to quit): $")
        expense = float(expense)

        if expense == 0:
            break
        total_expenses += expense

        balance = available - total_expenses

        if balance > 0:
            status = "Surplus"
        elif balance < 0:
            status = "Deficit"
        else:
            status = "Balanced"

        return total_expenses, balance, status


OVERTIME = 40
OVERTIME_RATE = 1.5
TAX_RATE = 0.03625


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    total = 0.0
    count = 0

    while True:
        employee_id = input("Employee ID (0 to quit): ")

        if employee_id == '0':
            break

        hourly_wage_rate = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))

        if hours_worked > OVERTIME:
            regular_hours = OVERTIME
            overtime_hours = hours_worked - OVERTIME
            gross_salary = (regular_hours * hourly_wage_rate) + \
                (overtime_hours * (OVERTIME_RATE * hourly_wage_rate))
        else:
            gross_salary = hours_worked * hourly_wage_rate

        tax = TAX_RATE * gross_salary
        net_payment = gross_salary - tax

        print(f"Net payment for employee {employee_id}: ${net_payment:.2f}")

        total += net_payment
        count += 1

    if count > 0:
        average = total / count
    else:
        average = 0.0

    return total, average
