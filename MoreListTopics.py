# MORE ADVANCED TOPICS RELATED TO LISTS

# ***Python uses indentation to determine when a line(s) is connected to the line above it

# using a for loop to loop through a list to print every single element
print("Using a For Loop with Lists:")
magicians = ['alice', 'david', 'carolina']
print(magicians)
for magician in magicians: # 'magician' is the loop variable that goes to every element in the list. Any name would work
    print(magician) # prints each new list element 'magician' takes on as it goes through the list indices
print()

# another looping-through-lists example
print("Another Looping Example:")
magicians = ['alice', 'david', 'carolina']
print(magicians)
for magician in magicians:
    print(magician.title() + " is a good magician.") # will be executed once for each element in the list
print()

# the range() function prints values in the range of the listed numbers including the lower bound BUT EXLCUDES UPPER BOUND
print("Using the range() Function to Print Values in the Range of the Listed Numbers(lower bound to 1-(upper bound)):")
for value in range(1,5):
    print(value)
print()

# using range to create a list structure of numbers
print("Using range() to Create a List Structure of Numbers:")
numbers = list(range(1,6))
print(numbers)
print()

# range() can also skip numbers in a given range. Following example prints even numbers in the given range
print("Using range()'s Third Parameter to Print Only Even Numbers(third param is value added to every value starting from the first parameter value):")
even_numbers = list(range(2,11,2)) # third parameter is the value added to every value starting from the first parameter '2'
print(even_numbers)
print()

# another range() example
print("Another range() Example:")
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print()


# simple statistics with a list of numbers using min(), max(), sum()
print("Basic Statistics Functions:")
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
print()

# list Comprehensions -> Builds a list of elements in a single line
print("Using List Comprehensions to Build a List in a Single Line of Code:")
squares = [value**2 for value in range(1,11)]
print(squares)
print()

# slicing a list
print("Slicing a List:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3]) # prints the elements at indices 0, 1, and 2 -> last value printed is the (upper bound bracket value - 1) index
print(players[-3:]) # outputs the last three players as the slicing starts from the third to last values
print()

# looping through a slice
print("Looping Through the Slice:")
for player in players[:3]:
    print(player.title()) # prints first three players
print()

# copying a list
print("Copying a List:")
my_foods = ['pizza', 'falafel', 'carrot cake']
print(my_foods)
friends_foods = my_foods[:] # [:] means all elements are selected in the slice
print("My favorite foods are: " + str(my_foods))
print("My friend's favorite foods are: " + str(friends_foods))
