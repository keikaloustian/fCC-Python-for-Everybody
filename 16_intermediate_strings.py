# SLICING STRINGS - [start index : end (non-inclusive)]
string = 'Monty Python'
string[0:4]  # read as s sub zero through 4 -> 'Mont'
string[6:7] # -> 'P'
string[6:20]  # if end is beyond end of string, stops at end -> 'Python'
string[ :2]  # if start is omitted, it assumes start of string
string[8: ]  # if end is omitted, it assumes end of string


# IN KEYWORD TO CHECK IF STRING IS SUBSTRING OF ANOTHER
fruit = 'banana'
'n' in fruit  # -> True
'z' in fruit  # -> False
'nana' in fruit  # -> True

# Strings can be compared using > / <, but keep in mind lexicographic order can be unpredictable depending on a computer's character set, special characters, upper case / lower case


# STRING LIBRARY - library of methods available to all strings (which are objects)
# String methods do not modify the original string; instead they return a copy with the alterations
greet = 'HellO'
greet_lower = greet.lower()  # -> 'hello', and greet stays as is
'HELLO'.lower()  # -> 'hello'

# To see all methods available to a variable
dir(string)

# .find('substring') - returns the index of the first occurence of the substring, or -1 otherwise
fruit = 'banana'
pos = fruit.find('na')  # -> 2
# Optional second arg can specify search start index

# .upper()
# .lower()
# .replace('search string', 'replacement string') - replaces all instances
# .lstrip(), .rstrip(), .strip() - strip whitespaces from beginning/end/both
# .startswith() - returns True if string starts with the arg, otherwise False


# IN PYTHON 3, ALL STRINGS ARE UNICODE