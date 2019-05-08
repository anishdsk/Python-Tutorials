# MORE ADVANCED TOPICS RELATED TO LISTS

# ***Python uses indentation to determine when a line(s) is conencted to the line above it

# using a for loop to loop through a list to print every single element
magicians = ['alice', 'david', 'carolina']
for magician in magicians: # 'magician' is the loop variable that goes to every element in the list. Any name would work
    print(magician) # prints each new list element 'magician' takes on as it goes through the list indices
print()

# another looping-through-lists example
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + " is a good magician.") # will be executed once for each element in the list
print()

# the range() function prints values in the range of the listed numbers including the lower bound BUT EXLCUDES UPPER BOUND
for value in range(1,5):
    print(value)
print()

# using range to create a list structure of numbers
numbers = list(range(1,6))
print(numbers)
print()

# range() can also skip numbers in a given range. Following example prints even numbers in the given range
even_numbers = list(range(2,11,2)) # third parameter is the value added to every value starting from the first parameter '2'
print(even_numbers)
print()

# another range() example
squares =[]
for value in range(1,11):
    square =value*2
    squares.append(square)
print(squares)
print()


# simple statistics with a list of numbers using min(), max(), sum()
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))
print()

# List Comprehensions -> Builds a list of elements in a single line
squares = [value**2 for value in range(1,11)]
print(squares)