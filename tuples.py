# TUPLES

# Tuples are immutable lists (cannot change) unless fully overwritten
# Tuples look exactly like lists except the brackets become PARANTHESIS ONLY FOR DECLARATION AND INITIALIZATION

# tuples example
dimensions = (200,50)
print(dimensions[0]) # bracket notation is still maintained here
print(dimensions[1])
print()

# 'dimensions[0] = 250' will throw error as it is changing an index's element

# looping through all variables in a tuple
for dimension in dimensions:
    print(dimension)
print()

# writing over a tuple -> can't modify a tuple but can assign a new value to a variable that holds a tuple
dimensions = (200,50)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)
# 'dimensions' holds a tuple so changing the entire value of 'dimensions' aka the tuple makes it possible to change the tuple entirely -> only way for any change
dimensions = (400, 50)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)
print()
