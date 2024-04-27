"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports
# Constants

Hourly_rate = float(input("Hourly rate of pay: "))
Hours_worked = float(input("Hours worked in the week: "))


def total_pay(Hourly_rate, Hours_worked):
    total_pay = Hourly_rate * Hours_worked
    return total_pay


total_pay = total_pay(Hourly_rate, Hours_worked)

print(f"Total pay for the week:{total_pay}")
