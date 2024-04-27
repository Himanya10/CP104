"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
# Constants

from functions import common_end

if __name__ == "__main__":
    test_cases = [
        ("abc", "ABC"),
        ("running", "jumping"),
        ("apple", "pineapple"),
    ]

    for str1, str2 in test_cases:
        suffix = common_end(str1, str2)
        print(f"Common Ending of '{str1}' and '{str2}': {suffix}")
