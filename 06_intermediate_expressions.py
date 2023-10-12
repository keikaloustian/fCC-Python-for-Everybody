# NUMERIC OPERATORS
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Power **
# Remainder (Modulo) %


# OPERATOR PRECEDENCE
# Parenthesis
# Power
# Multiplication/Division/Remainder
# Addition/Subtraction
# Left to right

# When writing code, use parenthesis and keep expressions simple so they can be easily understood. Break up long operations into steps if necessary.


# DATA TYPES
type()  # Function that returns the type of the input

# Integer
x = 5
# Floating Point
y = -1.24

# Type Conversions
float(x)  # -> 5.0
int(y)  # -> -1 (truncates decimals)

# When an integer and a float meet in an expression, the integer is implicitly converted into a float

# Division will always result in a float in Python 3
print(10 / 2)  # -> 5.0
print(10.0 / 2.0)  # -> 5.0

# int() and float() can also convert strings that are just numeric characters
int('123')  # -> 123
float('123')  # -> 123.0


# USER INPUT
input('prompt')  # function prompts user for input and returns a string

name = input("What's your name?")
# prints What's your name? and then user types Bob
print('Welcome', name)  # -> Welcome Bob
# (comma separated arguments in print() get separated by spaces automatically)
