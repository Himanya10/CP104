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

from functions import valid_isbn
if __name__ == "__main__":
    test_cases = [
        '978-3-12148410--0',  # False
        '978-3-16-148410-0',  # True
        '979-1-23456-789-0',  # True
    ]

    for isbn in test_cases:
        is_valid = valid_isbn(isbn)
        print(f"ISBN: {isbn} -> Valid: {is_valid}")
