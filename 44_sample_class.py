# CLASS AND OBJECT EXAMPLE

class PartyAnimal:
    # A piece of data
    x = 0

    # A method
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

# Constructing an instance
anim = PartyAnimal()

# Calling the method
anim.party()

type(anim) # -> <class '__main__.PartyAnimal'>  The class we created is a "new type"


# dir() shows all available methods and attributes
x = list()
dir(x)  # ->  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# The ones surrounded by __ are private, used by Python itself


