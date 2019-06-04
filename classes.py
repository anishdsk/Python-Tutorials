# CLASSES

# involves object-oriented programming
# ***A function that is part of a class is a method


# class example
class Dog():
    """a simple class detailing dog information:"""

    # the '__init()__' method is a special method run whenever an instance of a class is created
    def __init___(Self, name, age):
        """initialze name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate a dog rolling over"""
        print(self.name.title() + "rolled over.")
