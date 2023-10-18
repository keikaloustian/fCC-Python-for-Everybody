# DICTIONARIES ARE EQUIVALENT TO JS OBJECTS, aka
# Associative Arrays in Perl / PHP
# Properties / Map / HashMap in Java
# Property Bag in C# / .Net

# Unlike lists, dictionaties are unordered. Each value in the dictionary requires a "lookup tag"

bag = dict()  # -> constructor function
bag['money'] = 12
bag['candy'] = 5
bag[100] = 'hello'  # -> keys can be strings, numbers, etc

print(bag)  # -> {'money': 12, 'candy': 5, 100: 'hello'}