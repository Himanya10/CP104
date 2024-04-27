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
from functions import number_stats

if __name__ == "__main__":
    # Open the file in read mode
    with open('numbers.txt', 'r') as file_handle:
        # Call the function and unpack the result
        smallest, largest, total, average = number_stats(file_handle)

        # Print the result
        print(f"Smallest: {smallest}")
        print(f"Largest: {largest}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
