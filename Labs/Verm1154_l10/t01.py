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
from functions import customer_record

if __name__ == "__main__":
    with open('customers.txt', 'r') as file_handle:
        record_number = int(input("Enter a record number: "))
        result = customer_record(file_handle, record_number)
        print(result)
