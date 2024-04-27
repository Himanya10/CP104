"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-10-05"
-------------------------------------------------------
"""
# Imports
# Constants
from functions import total_change

# Test the total_change function
nickels = 5
dimes = 8
quarters = 5
loonies = 3
toonies = 4

total = total_change(nickels, dimes, quarters, loonies, toonies)
print(total)
