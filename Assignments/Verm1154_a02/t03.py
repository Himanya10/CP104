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
date_input = int(input("Enter a date in the format YYYYMMDD: "))

# Extract year, month, and day
year = date_input // 10000
month = (date_input % 10000) // 100
day = date_input % 100

# Display the reformatted date
print(f"The reformatted date: {year}/{month:02}/{day:02}")
