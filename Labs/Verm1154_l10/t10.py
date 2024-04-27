"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
# Constants
from functions import count_frequency_word

if __name__ == "__main__":
    # Open the file in read mode
    with open('words.txt', 'r') as file_handle:
        # Get user input for the word to count
        word_to_count = input("Word to count: ")
        count = count_frequency_word(file_handle, word_to_count)
        print(f"'{word_to_count}' appears {count} time(s)")
