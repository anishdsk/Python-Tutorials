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
