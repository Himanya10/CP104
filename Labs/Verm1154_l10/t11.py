"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
# Constants

from functions import find_longest

if __name__ == "__main__":
    # Open the file in read mode
    with open('words.txt', 'r') as file_handle:
        # Call the function and print the result
        longest_word = find_longest(file_handle)
        print(f"'{longest_word}' is the last longest word")
