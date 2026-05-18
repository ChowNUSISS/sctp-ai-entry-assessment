# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName): 		# expects 2 string parameters
    firstName = firstName.capitalize()		# built in function, converts the first character of a string to uppercase and all remaining characters to lowercase.
    lastName = lastName.capitalize()
    return f"{lastName}, {firstName}"		# returns the parameters in a lastname first format
    pass


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):	# expects 2 string parameters
    firstInitial = firstName[0].upper()		# extracts the first character only using [0] indexing, converts it into upper case
    lastInitial = lastName[0].upper()		# extracts the first character only using [0] indexing, converts it into upper case
    return f"{firstInitial}.{lastInitial}."	# returns the parameters in a firstname character first format
    pass


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

print(formatName("Alice", "Tan"))        # Expected: "Tan, Alice" 	# testing
print(formatName("bob", "lim"))         # Expected: "Lim, Bob"		# testing

print(formatInitials("Alice", "Tan"))   # Expected: "A.T."		# testing
print(formatInitials("bob", "lim"))     # Expected: "B.L."		# testing
