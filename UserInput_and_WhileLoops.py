# USER INPUT AND WHILE LOOPS

# using the input() function
print("Using the input() function")
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
print()

# another input() example
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello " + name.title() + "!")
print()
