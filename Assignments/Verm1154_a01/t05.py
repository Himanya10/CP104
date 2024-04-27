"""
-------------------------------------------------------
Taking various variable to calculate how much an individual would have to pay after intrest
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""
# Imports
# Constants
Principal = float(input("Principal: $"))
Intrest = float(input("Intrest(%): "))
Years = int(input("Number of Years: "))
Compound = int(input("Number of times intrest compounded per year: "))

Interest_decimal = (Intrest/100)

Balance = Principal * (1 + Interest_decimal / Compound) ** (Compound * Years)

print(f"Balance: ${Balance}")
