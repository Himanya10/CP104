"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-10-14"
-------------------------------------------------------
"""
# Imports
# Constants
from functions import lawn_mow_time

width = 20
length = 50
speed = 4

time = lawn_mow_time(width, length, speed)
print(f"lawn_mow_time({width}, {length}, {speed}) -> {time}")
