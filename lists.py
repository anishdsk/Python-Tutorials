# lists in python

# list declaration and initialization
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# print first element
print(bicycles[0])
# title() will capitalize first letter
print(bicycles[0].title())
# to return last item in list, type"-1" as compartment number
print(bicycles[-1])
# to return second to last item in list, type "-2" as compartment number
print(bicycles[-2])

# print statement using an element of a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print()

#second list manipulation example
relatives = ['mom', 'dad', 'uncle']
print(relatives[0].title() + ", " + relatives[1].title() + ", " + relatives[2].title())

message = "Hello " + relatives[0]
print(message)
message = "Hello " + relatives[1]
print(message)
message = "Hello " + relatives[2]
print(message)
print()

#modifying elements of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
