# What our player currently holds
Inventory = ["Wooden Sword", "Magic Hat", "Flame Orb"]

# What our player has stumbled upon and wishes to add to their inventory
Chest = ["Health Potion", "Stamina Potion", "Map of Floor"]

# We could do this

# for item in Chest:
#     Inventory.append(item)

# Instead of using the for loop, we could use Python's built in extend function
Inventory.extend(Chest)

print(Inventory)
