# FILES AND EXCEPTIONS

print("Opening 'pi_digits.txt' and Reading/Printing its Contents:")
with open('pi_digits.txt') as file_object:
    contents = file_object.read() # read() leaves a blank line at the end of the output, use rstrip() to get rid of that line if needed
    print(contents.rstrip()) # this output will match exactly with the text file
