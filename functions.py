# FUNCTIONS

# basic function that greets users
print("Basic function:")
def greet_user(): # keyword 'def' defines a function
    """Display a simple greeting""" # docstring
    print("Hello.")

greet_user() # function call
print()


# passing information to a function
print("Basic Function with Arguements: ")
def greet_user(username): # takes in parameter/arguement 'username'
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

greet_user('jesse') # function call with 'jesse' as the value for arguement 'username'
print()


# positional arguements (order matters) -> each arguement in the funtion call below must be matched with a parameter in the function definition
print("Same Function Using Positional Arguements: ")
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
print()
# keyword arguements -> reduce confusion about which value an arguement hamster
print("Same Function Call Using Keyword Arguements: ")
describe_pet(animal_type='hamster', pet_name='harry')
print()


# return Values
print("Using Return Values: ")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title() # this is the value the function returns

musician = get_formatted_name('jimi', 'hendrix') # return value is stored in 'musician'
print(musician)
print()


# returning a Dictionary
print("Creating a Function to Return and Output a Dictionary: ")
def build_person(first_name, last_name, age=''): # age is optional param -> has an empty string value until assigned something
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
print()


# passing in a list as a parameter
print("Passing a List to a Function: ")
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print()


# modifying a list using multiple functions -> modifications will be permanent
print("Modifying a List Using Functions: ")
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design until none are left. Move each design to completed_models after printing """
    while len(unprinted_designs) > 0:
        current_design = unprinted_designs.pop()
        # simulate creating a 3d print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Output all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print()

# this function call will make sure the list that is passed in is NOT MODIFIED
print("This Function Call Makes sure Original List is Not Modified, Only a Copy: ")
print_models(unprinted_designs[:], completed_models) # 'unprinted_designs[:]' makes a copy slice of the entire list
print()

# passing an arbitrary number of Arguements -> useful when number of arguement needed isn't known beforehand
def make_pizza(*toppings): # (*ParamaterName) accepts as many arguements as needed
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print()

# using arbitrary keyword arguements
def build_profile(first,last,**user_info): # '**user_info' -> the double asterisks create an empty dictionary called user_info and packs whatever name-value pairs it recives into this dict
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstien', location = 'princeton', field = 'physics')
print(user_profile)
print()
