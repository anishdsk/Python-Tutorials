# DICTIONARIES

# dictionaries are a collection of key-value pairs. Similar to Java maps

# simple dictionary -> uses curly braces '{ }'
# every key is connected to is connected to its value by a colon
# individual key-value pairs are seperated by commas
alien_0 = {'color': 'green', 'points': 5}

# accessing individual values
print(alien_0['color'])
print(alien_0['points'])
print()

# pulls value of 'points' key
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print()

# add to the dictionary
print(alien_0)
alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print()

# modifying an element of a dictionary
print(alien_0['color'])
alien_0['color'] = 'yellow'
print(alien_0['color'])

# removing key-value pairs
# deleted key-value pairs are removed permanently
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
print("sarah's favorite language is " + favorite_languages['sarah'].title())
print()

# looping through a dictionary using items() method
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
# key, value are the names for the key-value pair contents but they could be any name
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

# looping through only the keys in a  using keys() method
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
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
friends = ['phil', 'sarah'] # keys with empty values
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
for language in set(favorite_languages.values()): # when set( ) is used it builds a set out of the unique contents so no repetitions
    print(language.title())
