# A tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Creating a tuple

fruits = ('Apples', 'Oranges', 'Grapes')

# Using constructor
# fruits2 = tuple(('Apples', 'Strawberries', 'Mangoe'))

print(fruits)

# Single value needs trailing comma
fruits2 = ('Apples',)

print(fruits2, type(fruits2))

# Can't assign new value to tuple
# fruits[0] = 'Pears'

# delete the tuple
# del fruits

# print(fruits)

print(len(fruits))



# A set is a collection which is unordered and unindexed. No duplicate members

# Create set

fruits_set = {'Apples', 'Oranges', 'Mangoe'}

print(fruits_set, type(fruits_set))

# Check if value is in set

print('Apples' in fruits_set)

fruits_set.add('Grapes')

print(fruits_set)

