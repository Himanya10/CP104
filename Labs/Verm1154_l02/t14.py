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
# Define constants for the ingredients
INGREDIENT = 6
MILK_PER_SERVING = 4 / INGREDIENT  # 4 cups for 6 servings
BUTTER_PER_SERVING = 8 / INGREDIENT  # 8 tablespoons for 6 servings
FLOUR_PER_SERVING = 0.5 / INGREDIENT  # 0.5 cups for 6 servings
SALT_PER_SERVING = 2 / INGREDIENT  # 2 teaspoons for 6 servings

# Step 1: Ask the user how many servings of Mac and Cheese they want to make
Servings = int(input("Enter servings of Mac & Cheese: "))

# Step 2: Calculate the ingredient amounts for the specified number of servings
Milk_amount = MILK_PER_SERVING * Servings
Butter_amount = BUTTER_PER_SERVING * Servings
Flour_amount = FLOUR_PER_SERVING * Servings
Salt_amount = SALT_PER_SERVING * Servings

# Step 3: Display the resulting ingredient list with 2 decimal places
print(f"{Servings}servings of Mac & Cheese requires:")
print(f"Milk (cups): {Milk_amount:.2f}")
print(f"Butter (tablespoons): {Butter_amount:.2f}")
print(f"Flour (cups): {Flour_amount:.2f}")
print(f"Salt: (teaspoons) {Salt_amount:.2f}")
