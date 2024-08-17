# A list is a collection which is ordered and changeable. Allows duplicate members

# Creating a list

numbers = [1,3,4,5,6,7]

# Use a constructor

# numbers1 = list((1,2,4,5,6))

fruits = ['Apples', 'Orange', 'Grapes', 'Pears']

# Get a value

print(fruits[1])

# Get length

print(len(fruits))

# Append to list

fruits.append('Mangoes')

print(fruits)
# Remove from list

fruits.remove('Grapes')

print(fruits)

# Insert into position

fruits.insert(2, 'Strawberries')

print(fruits)

# Remove with pop

fruits.pop(2)

print(fruits)

# Reverse list

fruits.reverse()

print(fruits)

# Sort list

fruits.sort()

print(fruits)

# Change value

fruits[0] = 'Blueberries'

print(fruits)