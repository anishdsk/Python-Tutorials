# CALLS THE FUNCTION FROM THE 'functionModule'  FILE

# importing the module file
import functionModule


# importing just a/the specific function of the module file and using 'as' to give the function an alias name
from functionModule import make_pizza as  mp

# invoke the function
print("Invoking the Function from the 'functionModule' File and Using it: ")
functionModule.make_pizza(16, 'pepperoni')
functionModule.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# using the '*' allows every function to be imported from the module but this time the dot operator doesn't need to be used, just the function name
from functionModule import *
