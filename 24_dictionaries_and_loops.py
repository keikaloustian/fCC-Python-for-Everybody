# FOR...IN LOOP - iterate through the keys in a dictionary
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
# -> jan 100
#    chuck 1
#    fred 42
     

# TWO ITERATION VARIABLES (ALTERNATIVE TO FOR...IN LOOP)
counts
for name, score in counts.items():
    print(name, score)
# -> jan 100
#    chuck 1
#    fred 42




# RETRIEVE LISTS OF KEYS / VALUES / BOTH (ITEMS)
list(counts)  # -> ['jan','chuck', 'fred']
counts.keys()   # -> ['jan','chuck', 'fred']

counts.values()  # -> [100, 1, 42]

counts.items()  # -> [('jan', 100), ('chuck', 1), ('fred', 42)]


