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
from functions import employee_payroll

total, average = employee_payroll()
print(f"Total net wages: ${total:.2f}")
print(f"Average net wage: ${average:.2f}")
