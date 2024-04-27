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
from functions import file_copy
if __name__ == "__main__":
    with open('words.txt', 'r') as source_file:
        with open('new_words.txt', 'w') as target_file:
            file_copy(source_file, target_file)
    print("Copying 'words.txt' to 'new_words.txt'")
