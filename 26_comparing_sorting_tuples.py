# GETTING KEY-SORTED VERSION OF DICTIONARY
dict = {'a': 10, 'b': 1, 'c': 22}
dict.items()  # -> dict_items([('a', 10), ('b', 1), ('c', 22)])
sorted(dict.items())  # -> [('a', 10), ('b', 1), ('c', 22)]
# By using the .items() method and the sorted() function it's possible to get a sorted list of the dictionary's key value tuples, sorted by the keys in ascending order
# "sorted of d sub items"


# VALUE-SORTED VERSION OF DICTIONARY
temp = []
for k, v in dict.items():
    temp.append((v, k))
sorted(temp)  # -> [(1, 'b'), (10, 'a'), (22, 'c')]

sorted(temp, reverse=True)  # -> [(22, 'c'), (10, 'a'), (1, 'b')]  sort in descending order by providing second argument to sorted()


# LAMBDAS / CLOSED FORM OF THE ABOVE - highly compressed way to write the same code
c = {'a': 10, 'b': 1, 'c': 22}
result = sorted([(v, k) for k, v in c.items()])  # -> this is a quick way of creating a list of tuples from a dictionary

print(result)  # -> [(1, 'b'), (10, 'a'), (22, 'c')]
