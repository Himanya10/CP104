"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports
# Constants
TAX_RATE = 0.185  # 18.5% tax rate

# Input
total_sales = float(input("Enter the total sales: $"))

# Calculate Tax
annual_tax = total_sales * TAX_RATE

# Display the Tax Report
print("\nProjected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {total_sales:.2f}")
print(f"Annual tax:    % {TAX_RATE * 100:.2f}")
print("--------------------------")
print(f"Tax:           $ {annual_tax:.2f}")
