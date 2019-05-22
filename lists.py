# LISTS

# list declaration and initialization
print("Basic List Declaration and Element Access: ")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# print first element
print(bicycles[0])
# title() will capitalize first letter
print(bicycles[0].title())
# to return last item in list, type "-1" as compartment number
print(bicycles[-1])
# to return second to last item in list, type "-2" as compartment number...so on
print(bicycles[-2])

# print statement using an element of a list
print("Basic Print Statement Using a List Element: ")
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print()

# second list manipulation example
print("Another List Example:")
relatives = ['mom', 'dad', 'uncle']
print(relatives)
print(relatives[0].title() + ", " + relatives[1].title() + ", " + relatives[2].title())

message = "Hello " + relatives[0]
print(message)
message = "Hello " + relatives[1]
print(message)
message = "Hello " + relatives[2]
print(message)
print()

# modifying elements of a list
print("Modifying Elements of a List:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print()

# appending elements to the end of a list using the append() method
print("Appending Elements to the End of a List Using the append() Method:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)
print()

# adding an element to a list at any position using the insert() method
print("Adding an Element to a List at any Position Using the insert() Method:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati') # inserts 'ducati' at position 0 of the list
print(motorcycles)
print()

# removing an element of a list
print("Removing an Element of a List Using 'del' and 'pop' (both do different things):")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0] # del statement deletes a chosen element of a list
print(motorcycles)
popped_motorcycle = motorcycles.pop() # pop() removes last element from list and allows that last element to be worked with/on
print(motorcycles)
print(popped_motorcycle)
motorcycles.append('kawasaki')
first_owned = motorcycles.pop(0) # pops element at index 0 of list
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print()

# removing an item by value -> useful when you do not know the index of a list element -> use remove() method
# remove() function DELETES ONLY THE FIRST OCCURENCE of the value. If the value occurs twice,
# then you'll have to use a loop to determine if all occurences have been removed
print("Removing an Item by Value Using the remove() Function (only removes first occurence, use loop to remove all occurences):")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# using remove() to work with the removed element
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print("A " + too_expensive.title() + " is too expensive for me.")
print()

# organizing/sorting a list using the sort() method
print("Sorting a List Using sort() Method(permanently sorts list):")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # will sort the list alphabetically. An irreversible change
print(cars)
# to reverse the alphabetical ordering, pass the arguement 'reverse=True' to sort()
print("Reversing Alphabetical Ordering of list Elements (sort(reverse=true)):")
cars.sort(reverse=True)
print(cars)
print()

# organizing/sorting a list using the sorted() function. This method sorts the list but
# does not make the change permanent -> actual order of list will not change permanently in the end
print("Sorting a List Using sorted() Function(temporarily sorts the list):")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)
print()

# printing a list in reverse order of its original order -> does not mean it sorts backward alphabetically
# changes ordering permanently but you can revert back by using reverse() again
print("Printing List in Reverse Order Using the reverse() Method(doesn't mean alphabetically reverse):")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print()

# use len() to find the length of a list
print("Using len() Function to Find Length of List:")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(len(cars))
