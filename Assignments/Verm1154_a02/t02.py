"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports
# Constants
# Input
num = int(input("Enter a positive digit number: "))

# Check if the number is a positive two-digit integer
if 10 <= num <= 99:
    # Extract the tens and ones digits
    tens_digit = num // 10
    ones_digit = num % 10

    # Calculate the difference
    difference = tens_digit - ones_digit

    # Display the result
    print(f"The difference of the digits of {num} is {difference}")
else:
    print("Please enter a valid positive two-digit integer.")
