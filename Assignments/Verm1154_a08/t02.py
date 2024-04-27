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

from functions import pluralize

if __name__ == "__main__":
    test_cases = [
        "city",
        "student",
        "boss",
        "baby",
        "dog",
        "church",
        "toy",
    ]

    for word in test_cases:
        pluralized_word = pluralize(word)
        print(f"Singular: {word} -> Plural: {pluralized_word}")
