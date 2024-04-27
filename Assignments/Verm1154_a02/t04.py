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
num_flyers = int(input("Number of flyers: "))
num_delivery_people = int(input("Number of delivery people: "))

# Calculate the division
flyers_per_person = num_flyers // num_delivery_people
flyers_left_over = num_flyers % num_delivery_people

# Display the results
print(f"Flyers per delivery person: {flyers_per_person}")
print(f"Flyers left over: {flyers_left_over}")
