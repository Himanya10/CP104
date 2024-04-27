"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-09-28"
-------------------------------------------------------
"""
# Imports
# Constants

Breakfast_Price = float(input("Enter the cost of breakfast:$"))
Lunch_Price = float(input("Enter the cost of lunch:$"))
Supper_Price = float(input("Enter the cost of supper:$"))

Total = Breakfast_Price + Lunch_Price + Supper_Price
print(f" Meal         Cost")
print(f"Breakfast     ${Breakfast_Price: 7.2f}")
print(f"Lunch         ${Lunch_Price: 7.2f}")
print(f"Supper        ${Supper_Price: 7.2f}")
print(f"Total         ${Total: 7.2f}")
