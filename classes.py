# CLASSES and INHERITANCE

# involves object-oriented programming
# **A function that is part of a class is a method

# class example
class Dog():
    """a simple class detailing dog information:"""

    # the '__init()__' method is a special method run whenever an instance of a class is created
    # 'self' param is required and must be before the other params. Every method associated with a class automatically passes 'self', which is a reference to the instance itself.
    # 'self' gives instant access to attributes and methods in the class
    # so no need to provide value for self, just the other params following it
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

    # method added to explain OVERRIDING later in the file
    def fill_gas_tank(self):
        """Fully filling up gas tank"""
        print("Your gas tank is filling up")
        print("...")
        print("Your gas tank is now full")

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
print()


# INHERITANCE is when one class (child class) takes on all the attributes and methods of the first class (parent class)

# COME BACK TO THIS METHOD AFTER ANALYZING THE 'ElectricCar' CLASS FURTHER BELOW
# Splitting large classes into multiple classes
# the following 'ElectricCar' class has a lot of info about batteries so break the battery attribute information into a seperate class that stores all battery info
class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's Attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

# continuation from line 114
# the parent class must be in the same file as the child class and appear before/above the child class
# a child class of the 'Car' class is defined
class ElectricCar(Car): # name of parent class must be included in parantheses
    """Represent a type of car - an electric car"""

    def __init__(self, make, model, year): # takes in the info required to make an instance of 'Car'
        """Initialize attributes of the parent class"""
        # super() function allows connections to be made between the child and parent class.
        # this next line tells Python to call the __init__() class from "ElectricCar"'s parent class
        super().__init__(make, model, year)
        self.battery_size = 70 # creating a new attribute; can be associated with all instances of the 'ElectricCar' class but not 'Car' class
        # the next line creates a new instance of the 'Battery' class (with a default size of 70 if no value is provided) and stores it in the 'self.battery' attribute
        # any 'ElectricCar' instance will have a 'Battery' instance created automatically
        self.battery = Battery()

    # OVERRIDING
    # to do this, define a method in the child class with the same name as the method to be overriden in the parent class
    # electric cars don't need gas so we override the method to do something else
    # if someone tries to call the next method with an electric car, it will call this method instead of the method in the 'Car' class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank.")

# next line calls the __init() method defined in 'ElectricCar' which then calls the __init__() method in the parent class 'Car'
print("Creating and Using a New Child Class ('ElectricCar') of the Parent Class ('Car') and Battery() Class: ")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # call the newly created child class method
my_tesla.battery.get_range()
my_tesla.fill_gas_tank() # calling the overriden method

my_tesla.battery.describe_battery() # using "Battery()"'s describe_battery' method since the '.battery' attribute has an instance of 'Battery()'
my_tesla.battery.get_range() # using "Battery()"'s 'get_range' method
