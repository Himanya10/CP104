"""
-------------------------------------------------------
Converts Fahrenheit to Celcius 
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2023-09-16"
-------------------------------------------------------
"""
# Imports
# Constants

FREEZING_POINT_F = 32  # Freezing point of water in Fahrenheit


def fahrenheit_to_celsius(fahrenheit_temperature):
    celsius_temperature = (fahrenheit_temperature - FREEZING_POINT_F) * 5/9
    return celsius_temperature


# Get user input for Celsius temperature as an integer
fahrenheit_temperature = int(input("Temperature (F): "))
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"Temperature (C): {celsius_temperature}")
