# FUNCTION MODULE

# stores functions in seperate files to allow for reusability across multiple files

# simulating making a pizza
def make_pizza(size, *toppings):
    """Summarizing the pizza to make"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
