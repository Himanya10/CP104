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
from functions import budget

available = 200.0
expenses, balance, status = budget(available)
print(f"Total expenses: ${expenses:.2f}")
print(f"Balance: ${balance:.2f}")
print(f"Status: {status}")
