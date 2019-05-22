# IF STATEMENTS

# if statement example
print("Basic if Statement Example:")
cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

# using and/or to check multiple conditions
print("Using and/or to Check Multiple Conditions: ")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)
print()

# checking whether a value is in a list using 'in' keyword
print("Checking Whether a value is in a list using 'in' Keyword: ")
cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
print('honda' in cars)
print('bmw' in cars)
print('subaru' not in cars)
print()

# if-else
print("if-else Example: ")
age = 17
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are too young to vote")
print()

# if-elif-else
print("if-elif-else Example: ")
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")
