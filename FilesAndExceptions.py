# FILES AND EXCEPTIONS

print("Opening 'pi_digits.txt' and Reading/Printing its Contents:")
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
