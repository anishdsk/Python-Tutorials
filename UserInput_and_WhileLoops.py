# USER INPUT AND WHILE LOOPS

# using the input() function
print("Using the input() function:")
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
print()

# another input() example
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello " + name.title() + "!")
print()

# using int() function to accept numerical input
print("Using int() to Accept Numerical Input:")
age = input("How old are you? ") # the age is taken as a string instead of a number -> so entering 21 = '21' -> can't use input as a number
# to resolve the problem in the above line, the int() function is used
age = input("How old are you again? ")
age = int(age)
print("100 - Your Age = " + str(100-age))
print()

# modulo operator -> divides one number by the other and outputs the remainder
print("Using the Modulo Operator: ")
print("4 % 3 = " + str(4%3))
print("6 % 3 = " + str(6%3))
print("7 % 2 = " + str(7%2))
print()

# while loops -> runs until condition is met
print("While Loop Outputs:")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print()

# letting users quit
print("Allowing Users to Quit Out of a Loop: ")
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
print()

# using a flag
# a flag is a variable that is set to true or false based on any of a set of conditions that can change its value
# that flag's value is then the only thing needing to be checked by a while loop to determine whether to keeep running or not
print("Using a Flag: ")
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False # sets the flag to false
    else:
        print(message)
print()

# using 'break' to exit a loop -> exits loop as soon as that statement is hit
print("Using 'break' to Exit Out of a Loop: ")
prompt = "Please enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "
# a loop that starts with 'while True' will run forever unless it reaches a 'break' statement
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
print()

# using 'continue' in a loop -> returns to beginning of loop based on the result of a conditional test
print("Using the 'continue' Statement: ")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print()

# moving items from one list to another using while loops
# example involves moving users that become verified from the unverified to verified list
print("Moving Items from One List to Another: ")
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []
# verifies each user until there are no more unconfirmed Users by moving each verified user to the new list
while len(unconfirmed_users) > 0:
    current_user = unconfirmed_users.pop()
    print("Verifiying user: " + current_user.title())
    confirmed_users.append(current_user)
# display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print()

# removing all instances of a specific value of a list using remove() and while loops
print("Removing All Instances of a Specific Value in a List Using remove() and While Loops: ")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
print()

# filling a dictionary with user input
responses = {}
polling_active = True # set a flag to indicate poll is still active
while polling_active:
    # prompting for person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # store the responses in a dictionary
    responses[name] = response
    # find out if anyone else wants to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# polling is complete. Show results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
print()
