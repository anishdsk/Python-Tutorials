# IF STATEMENTS

# if statement example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

# using and/or to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)
print()

# checking whether a value is in a list using 'in' keyword
cars = ['audi', 'bmw', 'subaru', 'toyota']
print('honda' in cars)
print('bmw' in cars)
print('subaru' not in cars)

# if else
age = 17
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are too young to vote")
