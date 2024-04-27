"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Himanya Verma
ID:        169051154
Email:   Verm1154@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
# Constants
from functions import range_addition

# Test 1: Sum of values starting from 1 with an increment of 2 for 20 values
result1 = range_addition(1, 2, 20)
print(f"range_addition(1, 2, 20) -> {result1}")

# Test 2: Sum of values starting from 3 with an increment of 4 for 10 values
result2 = range_addition(3, 4, 10)
print(f"range_addition(3, 4, 10) -> {result2}")

# Test 3: Sum of values starting from -2 with an increment of 1 for 50 values
result3 = range_addition(-2, 1, 50)
print(f"range_addition(-2, 1, 50) -> {result3}")
