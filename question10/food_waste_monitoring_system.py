# Food Waste Monitoring System

# Get number of food items
n = int(input("Enter number of food items: "))

food_items = []
waste = []

# Enter food details
for i in range(n):
    name = input("Enter food name: ")
    quantity = float(input("Enter prepared quantity (kg): "))
    wasted = float(input("Enter wasted quantity (kg): "))

    food_items.append(name)
    waste.append(wasted)

# Display food waste details
print("\nFood Waste Report")

total_waste = 0

for i in range(n):
    print(food_items[i], ":", waste[i], "kg wasted")
    total_waste = total_waste + waste[i]

# Calculate total waste
print("\nTotal Food Waste:", total_waste, "kg")

# Find food with maximum waste
if n > 0:
    highest = waste[0]
    highest_food = food_items[0]

    for i in range(n):
        if waste[i] > highest:
            highest = waste[i]
            highest_food = food_items[i]

    print("Food with Maximum Waste:", highest_food)
    print("Maximum Waste:", highest, "kg")