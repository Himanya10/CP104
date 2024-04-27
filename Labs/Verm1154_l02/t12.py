"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports
# Constants
# Define a constant for seconds per minute
SECONDS_PER_MINUTE = 60

Seconds = int(input("Number of seconds: "))

Days = Seconds // (3600 * 24)
Seconds %= 3600 * 24

Hours = Seconds // 3600
Seconds %= 3600

Minutes = Seconds // SECONDS_PER_MINUTE
Seconds %= 60

# Step 3: Display the results
print(f"Days: {Days}")
print(f"Hours: {Hours}")
print(f"Minutes: {Minutes}")
print(f"Seconds: {Seconds}")
