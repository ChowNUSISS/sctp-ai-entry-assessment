# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Add your code here
inventory = []

# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

def addItem(itemName): 					# define a function with one parameter
    if itemName in inventory:				# check if an item is already inside the list called "inventory"
        print(f"{itemName} is already in inventory.")	# if yes print msg
    else:
        inventory.append(itemName)			# if no, add item into the list called "inventory"
    pass

# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

def listInventory():
    if len(inventory) == 0:				# check if the length is zero, if zero means empty
        print("Inventory is empty.")			# if empty print "empty" msg
    else:
        print(f"Inventory: {inventory}")		# if not empty, print out all items
    pass

# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")					# add "Laptop"
addItem("Mouse")					# add "Mouse"
addItem("Keyboard")					# add "Keyboard"
addItem("Mouse")   					# Should trigger duplicate warning
listInventory()						# print out all items

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']



