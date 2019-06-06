# CLASSES and INHERITANCE

# involves object-oriented programming
# ***A function that is part of a class is a method

# class example
class Dog():
    """a simple class detailing dog information:"""

    # the '__init()__' method is a special method run whenever an instance of a class is created
    # 'self' param is required and must be before the other params. Every method associated with a class automatically passes 'self', which is a reference to the instance itself.
    # 'self' gives instant access to attributes and methods in the class
    # so no need to provid value for self, just the other params following it
    def __init__(self, name, age):
        """initialze name and age attributes"""
        # any variable prefixed with 'self' is available to every method in the class. These variables can be accessed by any instance of the class
        # next line takes value stored in param 'name' and stores it in the variable 'name'
        self.name = name
        # same process as described above
        self.age = age
        # ^ the above variables, 'name' and 'age', are attached to the instance being created
        # ^ the above variables, which are accessible through instances, are called attributes

    def sit(self):
        """simulate a dog sitting"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate a dog rolling over"""
        print(self.name.title() + " rolled over.")

# making an instance of the 'Dog' class
print("Making an Instance of the 'Dog' Class and Using the Attributes:")
my_dog = Dog('willie', 6) # param values for the two params in the '__init()__' after 'self' -> remember 'self' shouldn't be assigned anything

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print()

print("Calling Methods of the Class: ")
my_dog.sit()
my_dog.roll_over()
print()

# creating another instance of the same class
your_dog = Dog('lucy', 3)


# writing the 'Car' class
class Car():
    """An attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # setting initial value -> allows the attribute to not be included as a parameter

    def get_descriptive_name(self):
        """Return a descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage): # made to modify the 'odometer_reading' attribute
        """Set the odometer rading to the given value. Reject the change if the new value is less than the old value"""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer.")

    def increment_odometer(self, miles): # made to incremenet, but not change entirely, the odometer value
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

print("The Output of the Car Class's Attributes and Methods:")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()

print("Changing Attribute Values:")
# modifying an attribute directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print()

# modifying an attribute through a method
my_new_car.update_odometer(25)
my_new_car.read_odometer()
print()

# incrementing an attribute's value through a method
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# INHERITANCE is when one class takes on all the attributes and methods of the first class
