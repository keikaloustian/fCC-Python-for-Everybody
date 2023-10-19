# HISTOGRAMS (aka COUNTER)
fruits_count = dict()
if 'banana' in fruits_count:
    fruits_count['banana'] += 1
else:
    fruits_count['banana'] = 1

# This is such a common pattern that dictionaries have a method for it, the .get() method
# The .get(key, default_val) method returns the respective value, if the key already exists in the dictionary or it creates the key with the provided default value and returns it
produce = ['banana', 'banana', 'apple', 'orange']
for fruit in produce:
    fruits_count[fruit] = fruits_count.get(fruit, 0) + 1
print(fruits_count)
