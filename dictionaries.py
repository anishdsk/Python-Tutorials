# DICTIONARIES

# dictionaries are a collection of key-value pairs. Similar to Java maps

# simple dictionary -> uses curly braces '{ }'
# every key is connected to is connected to its value by a colon
# individual key-value pairs are seperated by commas
alien_0 = {'color': 'green', 'points': 5}

# accessing individual values
print("Accessing Individual Values:")
print(alien_0['color'])
print(alien_0['points'])
print()

# pulls value of 'points' key
print("Pulling Value of a Key")
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print()

# add to the dictionary
print("Adding Values to a Dictionary")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0)

# modifying an element of a dictionary
print("Modifying an Element of a Dictionary:")
print(alien_0['color'])
alien_0['color'] = 'yellow'
print(alien_0['color'])
print()

# removing key-value pairs
# deleted key-value pairs are removed permanently
print("Deleting Key-Value Pairs:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
print()

# storing one kind of information for many/multiple objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("New Dictionary Example:")
print(favorite_languages)
print("sarah's favorite language is " + favorite_languages['sarah'].title())
print()

# looping through a dictionary using items() method
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
# key, value are the names for the key-value pair contents but they could be any name
print("Looping Through a Dictionary Using items() Method:")
for key, value in user_0.items():
    print("\nKey:" + key)
    print('\nValue:' + value)
print()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())
print()

# looping through only the keys using keys() method
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Looping Through Keys only Using keys() Method:")
for name in favorite_languages.keys(): # behaviour is the same even without .keys()
    print(name.title())
print()

# example involving dictionaries, keys, and loops
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['phil', 'sarah'] # list of keys with empty values
print("Looping With Conditionals Example:")
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
print()

# looping through keys in order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Looping Through Keys in Order:")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print()

# looping through only the values in a dictionary using values() method
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Printing Only the Values Using the values() Method:")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print()

# to avoid repetitions of values when looping through a dictionary, use a set
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Printing Values Using set() Method to Avoid Reprinting Repeating Values:")
for language in set(favorite_languages.values()): # when set( ) is used it builds a set out of the unique contents so no repetitions
    print(language.title())
print()

# Nesting

# dictionaries in lists
# make multiple dictionaries using range
aliens = []
# make 30 green aliens
print("Make 30 Green Aliens(Dictionaries):")
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# output the first five aliens
print("Output the First Five Aliens:")
for alien in aliens[:5]:
        print(alien)
print("...")
# output the total count of aliens created
print("Total number of aliens: " + str(len(aliens)))
print()

# changing individual elements of the dictionary
print("Changing Individual Elements of the Dictionary and Printing the First Five:")
for alien in aliens[0:3]: # changes the first three elements/aliens
    if alien['color'] == 'green':
        alien['color'] = 'yellow',
        alien['speed'] = 'medium',
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red',
        alien['speed'] = 'fast',
        alien['points'] = 15
# output the first five aliens
for alien in aliens[:5]:
        print(alien)
print()

# lists inside dictionaries
# store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("New Dictionary About Pizza Toppings:")
# summarize the order
print("Summarizing an Order:")
print("you ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
print()

# dictionaries in dictionaries
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
print("New 'Users' Dictionary Involving Nesting:")
print(users)
print()
print("User Info:")
for username, user_info in users.items(): # 'username' holds keys and 'user_info' holds the values
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull Name: " + full_name.title())
    print("\tLocation" + location.title())
