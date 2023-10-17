# LISTS ARE THE ARRAYS OF PYTHON
# Lists are mutable, i.e. item assignment is allowed, but strings are not
fruit = 'Banana'
fruit[0] = 'b'  # -> Traceback

# len(array) gives the number of elements in the list

# range[n] - RETURNS A LIST OF NUMBERS FROM 0 TO ONE LESS THAN THE ARG
range[4]  # -> returns [0, 1, 2, 3]

# Loop through a list using range() to keep access to the index
letters = ['a', 'b', 'c']
for i in range(len(letters)):
    print(i)
    print(letters[i])