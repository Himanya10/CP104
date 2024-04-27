"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""
# Imports
# Constants

Number = float(input("Enter Number: "))
Percent = float(input("Enter Percent: "))
Percentage = Percent / 100
Total = Number * Percentage
Amount = "{:.1f}".format(Total)  # Format Total with 1 decimal place
print(f"A {Percent:.1f} Percent discount on {Number:.1f} is {Amount}")
