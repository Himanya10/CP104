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

# Step 1: Ask for user input
Mortgage_Principle = float(input("Enter the principal amount ($): "))
Monthly_Payment = int(input("Enter the number of years: "))
Intrest = float(input("Enter the annual interest rate (%): "))

# Step 2: Convert annual interest rate to monthly interest rate
Monthly_Intrest = (Intrest / 100) / 12

# Step 3: Convert number of years to number of months
n_months = Monthly_Payment * 12

# Step 4: Calculate the monthly mortgage payment using the correct formula
Mortgage = (Mortgage_Principle * Monthly_Intrest) / \
    (1 - (1 + Monthly_Intrest) ** -n_months)

# Display the monthly payment with 2 decimal places
print(f"The monthly mortgage payment is: ${Mortgage:.2f}")
