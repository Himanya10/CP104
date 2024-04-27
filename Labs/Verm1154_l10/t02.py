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

from functions import customer_by_id

if __name__ == "__main__":
    # Open the file in read mode
    with open('customers.txt', 'r') as file_handle:
        # Get user input for the ID to search
        id_to_search = input("Enter an ID: ")

        # Call the function and print the result
        result = customer_by_id(file_handle, id_to_search)
        print(result)
