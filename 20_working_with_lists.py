# CONCATENATING LISTS WITH +
[1, 2, 3] + [4, 5, 6]  # -> [1, 2, 3, 4, 5, 6]


# LIST SLICING (WORKS THE SAME AS STRING SLICING)
nums = [9, 41, 12, 3, 74, 15]
nums[1:3]  # -> [41, 12]
# [start index, non-inclusive end index], if either is omitted, it goes to that respective end


# MORE LIST METHODS
dir(nums)
# -> ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# CREATE A LIST USING CONSTRUCTOR
stuff = list()  # this is the constructor function

# Examples
stuff.append('book')
stuff.append(99)
stuff.append('cookie')

# Check if an item is / isn't in list
99 in stuff  # -> True
'book' not in stuff  # -> False


# BUILT-IN FUNCTIONS FOR WORKING WITH LISTS
len(stuff)
max(nums)
min(nums)
sum(nums)