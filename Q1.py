# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

#def convertTemp(value, unit):
 #   # Add your code here
  #  pass

def convertTemp(value, unit):			# define a function with 2 parameters requirement
    if unit == "C": 				# check if equivalent the charactor "C"
        result = (value * 9/5) + 32 		# if True, convert c to f
        return round(result, 2) 		# return the results in 2 decimal piece
    elif unit == "F": 				# check if equivalent the charactor "F"
        result = (value - 32) * 5/9		# # if True, convert f to c
        return round(result, 2)			# return the results in 2 decimal piece
    else:
        return -1				# return -1 if all fails

    pass
# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

# Add your code here
print(convertTemp(100, "C"))      # Testing the code, call the function, pass two parameters to it.
print(convertTemp(32, "F"))     
print(convertTemp(37, "C")) 
print(convertTemp("invalid","X"))


