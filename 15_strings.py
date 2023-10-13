# STRINGS - sequences of characters

# A string literal uses quotes
'Hello'
"Hello"

# Concatenation
fruit = 'Ban' + 'ana'  # fruit is 'Banana'

input()  # function returns a string, which needs to be converted when working with numbers

# Each character in a string can be accessed via its index using the square bracket notation (zero-indexed)
fruit = 'apple'
fruit[4]  # -> e
# Attempting to index beyond the end of a string will throw an error

# Length built-in function
len(fruit)  # -> 5


# LOOPING THROUGH STRINGS
# Both indeterminate (while) and determinate (for...in) loops can be used to go through strings
# All else being equal, for loops are preferred 