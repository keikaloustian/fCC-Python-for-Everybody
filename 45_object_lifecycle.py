# OBJECT LIFECYCLE - how objects are created, used and destroyed

# There are special methods that get called at the time of creation (constructor) and at the time of destruction (destructor)
# Constructors are used a lot, destructors rarely


# CONSTRUCTOR
# Generally used to set up instance variables with the proper initial values
# Each different instance of a class has its own copy of the instance variables

# Example
class PartyAnimal:
    x = 0

    # Define a constructor
    def __init__(self):
        print('I am constructed')
    
    # A method
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    # Define a destructor
    def __del__(self):
        print('I am destructed', self.x)

# The self argument is automatically passed when an object is constructed
# Additional parameters can be given to the constructor function

class PartyAnimal2:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')

# Instantiate PartyAnimal2 a couple times
s = PartyAnimal2('Sally')  # -> argument "Sally" goes to name parameter
j = PartyAnimal2('Jim')

