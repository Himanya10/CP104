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

from functions import add_spaces

# Sample test cases
if __name__ == "__main__":
    test_cases = [
        "StopAndSmellTheRoses.",
        "HelloWorld.",
        "PythonIsAwesome."
    ]

    for sentence in test_cases:
        spaced_sentence = add_spaces(sentence)
        print(f"Original: {sentence} -> Spaced: {spaced_sentence}")
