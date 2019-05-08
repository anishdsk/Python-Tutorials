# python basics

message = "hello"
print(message)
message = "69"
print(message)
print()

name = "Ada lovelace"
print(name.title()) # title() makes the first letter of each word uppercase and everything else becomes lowercase
print(name.upper()) # upper() = all uppercase
print(name.lower()) # lower() = all lowercase
print()

#concatenation
secondMessage = "Hello " + name.title() + "!"
print(secondMessage)
print()

language = "python   "
language = language.rstrip() # rstrip() eliminates extra white space to the right of the string
print(language)
language = "   python"
print(language)
language = language.lstrip() # lstrip eliminates extra white space to left of string
print(language)
print()

#arithmetic
print(3 ** 2) # = 3^2; ** is the exponent sign in python
print(3 + 4*2) # uses order of operations
print((3+4)*2) # uses paranthesis for precedence
print()

# combination of ints and strings
age = 20
# sentence = "Happy " + age + "th Birthday!" -> you cant do this because python can't combine ints with string using "+"
sentence =  "Happy " + str(age) + "th Birthday!" # instead do this as str() converts int to string for one single string statement
print(sentence)
