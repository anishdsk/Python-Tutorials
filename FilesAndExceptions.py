# FILES AND EXCEPTIONS

print("Opening 'pi_digits.txt' and Reading/Printing its Contents:")
with open('pi_digits.txt') as file_object: # open() returns an object representing the file and the object is stored in 'file_object'
    contents = file_object.read() # read() leaves a blank line at the end of the output, use rstrip() to get rid of that line if needed
    print(contents.rstrip()) # this output will match exactly with the text file
print()

print("Opening and 'pi_digits.txt' Printing its contents Line by Line Using a Loop:")
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # to get rid of the invis newline character space plus the print() space generated when printing text file contents
print()

print("Open and Print Contents of 'pi_digits.txt' once more using the readLines() Method:")
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() # readlines() method takes each line from file and stores it in a list, this list is then stored in 'lines'
                                    # to be able to be worked with if file content is needed past the 'with' block
for line in lines:
    print(line.rstrip())
print()

print("Building a Single String Containing All the Digits of the File With No Whitespace Included and Print Length:")
pi_string = ''
for line in lines:
    pi_string += line.strip() # take each line aka number, strip any whitespace to left or right of numbers and append

print(pi_string)
print(len(pi_string))
print()

### NOTE: When Python reads from a text file it interprets all text in the file as a string, even numbers included.
### So if you want to work with a value in number form, convert it to an integer using int() or to a float using float()

print("Using Large Files:")
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
print()

print("Writing to a File:")
filename = 'programming.txt'
# second open() param says to open file in 'write mode' -> if file already exists then opening in this mode will erase file before returning file object first
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
print()

print("Writing Multiple Lines") # write() doesnt know when to create new line unless specified
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n") # '\n' is key here
    file_object.write("I love creating new games.\n")
print()

print("Appending to a File:")
filename = 'programming.txt'
with open(filename, 'a') as file_object: # second open() param 'a' is used to append to the contents of a file rather than overwriting
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a brwoser.\n")

print("Using 'try-except' Blocks:") # if an error occurs try-except blocks can handle the error to make sure the program keeps running
try:
    print(5/0)
except ZeroDivisionError: # default error from python given whenever dividing by zero
    print("You can't divide by zero!")

print("Handling a 'FileNotFound' Exception:")
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f_obj: # encoding needed when system encoding is different from file encoding
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
# NOTE: some systems may show 'IOError' instead of 'FileNotFound'
