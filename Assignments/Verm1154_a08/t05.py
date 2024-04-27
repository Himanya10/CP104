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
from functions import has_word_chain
if __name__ == "__main__":
    test_cases = [
        ['camel', 'leopard', 'dog', 'giraffe', 'elephant'],  # True
        ['apple', 'elephant', 'tiger', 'rabbit'],  # False
        ['bird', 'dog', 'giraffe', 'elephant'],  # True
    ]

    for words in test_cases:
        word_chain = has_word_chain(words)
        print(f"Word Chain: {words} -> {word_chain}")
