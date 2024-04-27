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
# Input
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_concrete = float(input("Cost of concrete ($/m^3): "))
cost_bricks = float(input("Cost of bricks ($/m^2): "))

# Calculate the volume of concrete needed for the foundation
foundation_volume = foundation_length * foundation_width * foundation_height

# Calculate the area of walls
wall_area = 2 * (foundation_length * wall_height +
                 foundation_width * wall_height)

# Calculate the volume of bricks needed for the walls
bricks_volume = wall_area

# Calculate the total cost of concrete and bricks
total_cost_concrete = foundation_volume * cost_concrete
total_cost_bricks = bricks_volume * cost_bricks

# Calculate the total cost
total_cost = total_cost_concrete + total_cost_bricks

# Display the results
print(f"Concrete needed for foundation (m^3): {foundation_volume:.2f}")
print(f"Cost of concrete: ${total_cost_concrete:,.2f}")
print(f"Bricks needed for walls (m^2): {bricks_volume:.2f}")
print(f"Cost of bricks: ${total_cost_bricks:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
