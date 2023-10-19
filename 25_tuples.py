# TUPLES ARE LIKE LISTS - but more efficient, more limitations
# Zero indexed
# FOR...IN loops
# Parentheses instead of square brackets
# Elements are ORDERED, i.e. order is maintained
# Immutable - once created, contents cannot be altered
# Best used when the collecion doesn't need to be altered


# TUPLE METHODS
t = tuple()
dir(t) # -> ['count', 'index']


# TUPLE ASSIGNMENT - one statement instead of multiple
(x, y) = (4, 'fred')
a, b = 87, False


# DICTIONARIES' .items() method returns a list of tuples, each containing a key / value pair
dict = {'foo': 1, 'bar': 2}
tups = dict.items()


# TUPLES CAN BE COMPARED
# It compares items in order, one at a time, until it finds elements that differ
(0, 1, 2) < (5, 1, 2)  # -> True
('ACDC') > ('Beatles')  # -> False